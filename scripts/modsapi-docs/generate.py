"""Generate Docusaurus reference pages from the maintained adapter source.

Python 3.10+. Does not execute game modules. Writes a staging tree and a
hash-checked change manifest; apply() is an explicit separate operation.
"""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import os
import re
from functools import lru_cache
from collections import defaultdict
from pathlib import Path

from content import GUIDES, CLASS_EXAMPLES, NOTES, ACQUIRE_EXTRA
from ui_content import UI_GUIDES, UI_ACQUIRE, UI_EXAMPLES
from localization import chinese, MISSING
import references

SOURCE = Path(__file__).resolve().parents[2]
SITE = Path(r'D:\ModSAPI-Document\SAPI-Style-Document')
STAGE = SOURCE / 'audit/documentation-stage'
BASE = SOURCE / 'core_behavior/ModSAPI'
PAGES = {}
CLASSES = []
BY_NAME = defaultdict(list)
PRIVATE = {}
UI_CONSTRUCTORS = {'Form', 'Observable', 'ControlDescriptor', 'Button', 'Custom', 'Divider',
                   'Dropdown', 'Group', 'Label', 'ListView', 'ScrollingPanel', 'Slider', 'TextField', 'Toggle', 'UiItem'}
PYTHON_EXAMPLES = []
GUIDES.update(UI_GUIDES)
CLASS_EXAMPLES.update(UI_EXAMPLES)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def clean(value):
    return (str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('{', '&#123;').replace('}', '&#125;'))


def cell(value):
    return clean(value).replace('|', '\\|').replace('\n', '<br />')


def code(value):
    return '`' + str(value).replace('`', "'").replace('\n', ' ').replace('|', '\\|') + '`'


def python_example(value):
    """Keep printed lambda callbacks executable in the target Python 2 runtime."""
    value = value.rstrip()
    if (re.search(r'\blambda[^\n]*\bprint\s*\(', value)
            and not re.search(r'^from __future__ import .*\bprint_function\b', value, re.M)):
        value = 'from __future__ import print_function\n\n' + value
    return value


def fence(value):
    value = python_example(value)
    PYTHON_EXAMPLES.append(value)
    return '\n```python\n' + value + '\n```\n'


def put(path, text):
    PAGES[Path(path).as_posix()] = text.rstrip() + '\n'


def link(current, target, anchor=''):
    return Path(os.path.relpath(target, Path(current).parent)).as_posix() + ('#' + anchor if anchor else '')


def url_for(cls):
    overrides = {
        ('server', 'World'): 'packs/server/apis/world.md',
        ('server', 'Dimension'): 'packs/server/apis/dimension.md',
        ('server', 'Block'): 'packs/server/apis/block.md',
        ('server', 'Container'): 'packs/server/apis/container.md',
        ('server', 'Player'): 'packs/server/apis/player.md',
        ('server', 'Entity'): 'packs/server/apis/entity.md',
        ('server', 'ItemStack'): 'packs/server/apis/itemStack.md',
        ('server', 'WorldAfterEvents'): 'packs/server/events/afterEvents.md',
        ('server', 'WorldBeforeEvents'): 'packs/server/events/beforeEvents.md',
        ('client', 'Client'): 'packs/client/apis/manager.md',
        ('common', 'Vector3'): 'packs/server/extra/vector.md',
    }
    return overrides.get((cls['group'], cls['name']),
                         'packs/%s/reference/%s.md' % (cls['group'], cls['name']))


def classify(path):
    text = path.relative_to(BASE).as_posix()
    if text.startswith(('ui/', '_ui/')):
        return 'ui'
    if text.startswith('modules/server_ui/'):
        return 'server_ui'
    if text.startswith('modules/server/'):
        return 'server'
    if text.startswith('modules/client/'):
        return 'client'
    if text.startswith('architect/'):
        return 'architecture'
    return 'common'


def methods(node):
    result = {}
    for child in node.body:
        if isinstance(child, ast.FunctionDef):
            decorators = [ast.unparse(value) for value in child.decorator_list]
            setter = any(value.endswith('.setter') for value in decorators)
            if setter:
                result.setdefault(child.name, {})['setter'] = child
            else:
                result.setdefault(child.name, {})['node'] = child
                result[child.name]['kind'] = 'property' if 'property' in decorators else 'method'
                result[child.name]['static'] = 'staticmethod' in decorators or 'classmethod' in decorators
    return result


def parse(path):
    text = path.read_text(encoding='utf-8-sig')
    # Some game sources contain informal type comments rejected by Python 3's
    # strict type-comment parser. Recover function hints without executing them.
    tree = ast.parse(text)
    if path.suffix == '.pyi':
        expanded = []
        for item in tree.body:
            if (isinstance(item, ast.Assign) and len(item.targets) == 1
                    and isinstance(item.targets[0], ast.Name) and isinstance(item.value, ast.Call)
                    and isinstance(item.value.func, ast.Name) and item.value.func.id == 'TypedDict'
                    and len(item.value.args) == 2 and isinstance(item.value.args[1], ast.Dict)):
                body = [ast.AnnAssign(target=ast.Name(id=ast.literal_eval(key), ctx=ast.Store()),
                                     annotation=value, value=None, simple=1)
                        for key, value in zip(item.value.args[1].keys, item.value.args[1].values)]
                replacement = ast.ClassDef(name=item.targets[0].id,
                    bases=[ast.Name(id='TypedDict', ctx=ast.Load())], keywords=item.value.keywords,
                    body=body or [ast.Pass()], decorator_list=[])
                expanded.append(ast.copy_location(replacement, item))
            else:
                expanded.append(item)
        tree.body = expanded
        ast.fix_missing_locations(tree)
    lines = text.splitlines()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for line in lines[node.lineno:min(node.end_lineno, node.lineno + 7)]:
                match = re.search(r'#\s*type:\s*(\(.*->.*)', line)
                if match:
                    node.type_comment = match.group(1).strip()
                    break
    return tree


def load():
    CLASSES.clear(); BY_NAME.clear(); PRIVATE.clear()
    # Parse only the maintained package; no recursive repository-wide import.
    dirs = ('modules/server', 'modules/client', 'modules/server_ui', 'interfaces', 'enums', 'errors', 'architect')
    paths = []
    for folder in dirs:
        paths.extend((BASE/folder).rglob('*.py'))
        paths.extend(path for path in (BASE/folder).rglob('*.pyi') if not path.with_suffix('.py').exists())
    paths += [BASE/'utils/storage.py', BASE/'utils/promise.py', BASE/'utils/native_events.py',
              BASE/'utils/event_values.py', BASE/'utils/event_data.py', BASE/'utils/event_facade.py',
              BASE/'utils/expression.py', BASE/'utils/script_bridge.py', BASE/'utils/bridge_protocol.py']
    paths += [BASE / value for value in (
        'ui/service.py', 'ui/views.py', 'ui/controls.py', 'ui/events.py', 'ui/animations.py', 'ui/constants.py', 'ui/widgets.py', 'ui/choices.py', 'ui/minimap.py',
        '_ui/core/general/form.py', '_ui/core/general/observable.py',
        '_ui/core/utils/type.py', '_ui/interfaces/base/control.py',
        '_ui/interfaces/base/controls.py', '_ui/interfaces/base/theme.py',
        '_ui/core/general/controls/innerStyles.py',
        '_ui/core/general/interfaces/grid.pyi', '_ui/core/general/interfaces/controls.pyi',
        '_ui/core/general/interfaces/form.pyi')]
    hidden_files = {'modules/server/ClientEvents.py', 'modules/server/Particle.py',
                    'modules/client/UI.py', 'modules/server_ui/Forms.py'}
    hidden_classes = {'ConstMeta', 'EventManager', 'LisenerManager', 'EventListener', 'Events',
                      'BlockEvents', 'EntityEvents', 'InteractEvent', 'PlayerSpawnEvent',
                      'ButtonCallbackManager', 'BlankUI', 'ClientScheduler'}
    for path in sorted(set(paths)):
        relative = path.relative_to(BASE).as_posix()
        if relative in hidden_files or '/events/EventBases.py' in relative:
            continue
        tree = parse(path)
        stub_only=path.suffix=='.pyi'
        stub_path = path.with_suffix('.pyi')
        stub = parse(stub_path) if stub_path.is_file() else ast.Module(body=[], type_ignores=[])
        if relative.startswith(('_ui/', 'ui/')):
            aliases = {'FormShowResult': 'FormSession', 'FormShowResultArgs': 'FormCloseEvent'}
            for syntax in (tree, stub):
                for item in ast.walk(syntax):
                    if isinstance(item, ast.Name) and item.id in aliases:
                        item.id = aliases[item.id]
                    elif isinstance(item, ast.ClassDef) and item.name in aliases:
                        item.name = aliases[item.name]
        actual = {} if stub_only else {node.name:node for node in tree.body if isinstance(node, ast.ClassDef)}
        declared = {node.name:node for node in stub.body if isinstance(node, ast.ClassDef)}
        for name in sorted(actual.keys() | declared.keys()):
            if relative=='utils/bridge_protocol.py' and name!='ScriptBridgeError':
                continue
            if relative=='utils/expression.py' and name!='Expression':
                continue
            if name.startswith('_'):
                node=actual.get(name,declared.get(name))
                PRIVATE[name]={'name':name,'node':node,'source':actual.get(name),'stub':declared.get(name),
                    'members':methods(node),'stub_members':methods(declared[name]) if name in declared else {},
                    'bases':[ast.unparse(base).split('.')[-1] for base in node.bases if isinstance(base,(ast.Name,ast.Attribute))]}
                continue
            if name in hidden_classes:
                continue
            node = actual.get(name, declared.get(name))
            cls = {'name':name,'group':classify(path),'path':path,'node':node,
                   'source':actual.get(name),'stub':declared.get(name),
                   'members':methods(node),'stub_members':methods(declared[name]) if name in declared else {}}
            if cls['group'] == 'ui' and name not in UI_CONSTRUCTORS:
                cls['members'].pop('__init__', None)
            cls['bases'] = [ast.unparse(base).split('.')[-1] for base in node.bases if isinstance(base,(ast.Name,ast.Attribute))]
            if name in ('ClientAfterEvents', 'ClientBeforeEvents', 'WorldAfterEvents', 'WorldBeforeEvents'):
                for member, value in cls['stub_members'].items():
                    if (ast.get_docstring(value['node']) or '').startswith(('Native catalog signal:', 'Semantic event:')):
                        cls['members'].setdefault(member, value)
            cls['dynamic_native'] = path.name == 'NativeEventTypes.py'
            if name=='GameRules':
                factory=next(item for item in tree.body if isinstance(item,ast.FunctionDef) and item.name=='_rule')
                read=next(item for item in factory.body if isinstance(item,ast.FunctionDef) and item.name=='read')
                write=next(item for item in factory.body if isinstance(item,ast.FunctionDef) and item.name=='write')
                for item in node.body:
                    if isinstance(item,ast.Assign) and isinstance(item.value,ast.Call) and isinstance(item.value.func,ast.Name) and item.value.func.id=='_rule':
                        member=item.targets[0].id
                        getter=copy.deepcopy(read);getter.name=member
                        setter=copy.deepcopy(write);setter.name=member
                        kind=ast.unparse(item.value.args[2]) if len(item.value.args)>2 else 'bool'
                        getter.returns=ast.Name(id=kind)
                        cls['members'][member]={'node':getter,'setter':setter,'kind':'property','static':False}
                        NOTES['GameRules.'+member]='原生规则键 '+ast.literal_eval(item.value.args[1])+'；值类型为 '+kind+'。'+('范围 '+ast.unparse(item.value.args[3])+'。' if len(item.value.args)>3 else '传入真正的 bool，不接受整数代替。')
            cls['url'] = url_for(cls)
            # Re-exported classes live in their implementation file, not in an import-only stub.
            if any(existing['url']==cls['url'] for existing in CLASSES):
                existing = next(existing for existing in CLASSES if existing['url']==cls['url'])
                if existing['source'] is None and cls['source'] is not None:
                    CLASSES.remove(existing)
                    BY_NAME[name].remove(existing)
                else:
                    continue
            CLASSES.append(cls)
            BY_NAME[name].append(cls)
    # Public typed wrappers inherit through implementation-only base classes.
    # Flatten those bases so the published reference keeps all public methods.
    def flatten_private(cls,seen=None):
        seen=set() if seen is None else seen
        if cls['name'] in seen:return
        seen.add(cls['name'])
        bases=[]
        for name in cls['bases']:
            parent=PRIVATE.get(name)
            if not parent:
                bases.append(name)
                continue
            flatten_private(parent,seen)
            for key,member in parent['members'].items():
                hidden_constructor = key=='__init__' and (cls.get('path',Path()).name=='event_data.py'
                    or (cls.get('group')=='ui' and cls['name'] not in UI_CONSTRUCTORS))
                if (not key.startswith('_') or key=='__init__') and not hidden_constructor:
                    cls['members'].setdefault(key,member)
            cls['stub_members']={**parent['stub_members'],**cls['stub_members']}
            cls.setdefault('inherited_fields',{}).update(fields(parent))
            bases.extend(parent['bases'])
        cls['bases']=list(dict.fromkeys(bases))
    for cls in CLASSES:
        flatten_private(cls)
    for cls in CLASSES:
        cls['fields'] = fields(cls)
    references.TYPE_ALIASES.clear()
    references.TYPE_ALIASES.update(name for name, value, path in alias_rows())


@lru_cache(maxsize=1)
def native_catalog():
    return json.loads((SOURCE/'audit/native-events-catalog.json').read_text(encoding='utf-8'))


@lru_cache(maxsize=1)
def semantic_catalog():
    return json.loads((SOURCE/'audit/semantic-events-catalog.json').read_text(encoding='utf-8'))


def native_description(value, current):
    """Retarget native documentation anchors to this site's event catalogs."""
    def replace(match):
        label, anchor = match.groups()
        candidates = [e for e in native_catalog() if e['name'].lower()==anchor.lower()]
        if not candidates:
            return label
        preferred = 'client' if '/client/' in current else 'server'
        event = next((e for e in candidates if e['side']==preferred), candidates[0])
        target = 'packs/client/events.md' if event['side']=='client' else 'packs/server/native-events.md'
        return '['+label+']('+link(current,target,event['name'].lower())+')'
    return clean(re.sub(r'\[([^\]]+)\]\(#([\w-]+)\)', replace, value.replace('(opens new window)', '（在新窗口打开）')))


def native_event_pages():
    """Publish every binding, field contract and original engine prerequisite."""
    catalog = native_catalog()
    for side, scope, title, url in (
        ('client', 'client', '客户端原生事件目录', 'packs/client/events.md'),
        ('server', 'world', '服务端原生事件目录', 'packs/server/native-events.md')):
        events = [e for e in catalog if e['side'] == side]
        out = ['---', 'sidebar_position: 3', 'title: '+title, '---', '', '# '+title, '',
               '本目录逐项对应 ModSDK 文档事件索引，包含 **%d 个事件绑定**。'%len(events), '',
               '属性名称采用 lowerCamelCase；保留准确的原生事件名用于检索。前置或可写引擎钩子放在 `beforeEvents`，通知放在 `afterEvents`。原生名称带 After 的钩子仍可能在后续力学计算前接收可写输出，按字段契约归入 before。', '',
               '每项都提供独立类型、订阅示例、字段说明和原生前提。索引覆盖不意味着所有网易引擎版本、平台或资源配置都会触发这些事件。', '',
               '**常用业务优先使用 [语义化事件与筛选]('+link(url, 'packs/guides/semantic-events.md')+')**：多个原生事件可以合并为统一入口，一个原生事件也可以拆成多个有明确用途的信号。下面保留准确的原生契约用于高级场景。', '',
               '[原生用法、取消语义与错误处理]('+link(url, 'packs/guides/native-events.md')+')', '',
               '## 全部事件', '', '| 原生事件 | 信号属性 | 可写输出 | 平台 |', '| --- | --- | --- | --- |']
        for event in events:
            access = native_access(event)
            writable = ', '.join(event['writable']) or '无'
            if event['cancellation'] and event['cancellation'][0] != 'cancel':
                writable += '；cancel 映射 '+('反转 ' if event['cancellation'][1] else '')+event['cancellation'][0]
            out.append('| ['+event['name']+'](#'+event['name'].lower()+') | '+code(access)+' | '+cell(writable)+' | '+event['platform']+' |')
        out += ['', '## 逐项契约', '']
        for event in events:
            payload = next(c for c in BY_NAME[event['payload']] if c['group']==side)
            access = native_access(event)
            doc = event['documentation']
            summary = doc.split('- 描述',1)[-1].split('- 参数',1)[0].strip()
            out += ['### '+event['name']+' {#'+event['name'].lower()+'}', '', native_description(summary,url), '',
                    '信号：'+code(access)+'。分类：'+cell(event['category'])+'。', '',
                    '参数类型：['+payload['name']+']('+link(url,payload['url'])+')；属性名、类型、读写性及完整示例见类型页。', '',
                    '按原生名取得同一信号：'+code(scope+'.'+event['phase']+'Events.getNativeEvent("'+event['name']+'")')+'。', '']
            if event['platform']=='Apollo':
                out += [':::warning 平台条件', '此事件仅在 Apollo 环境中提供；普通联机/单机不会因此得到同等能力。', ':::','']
            if event['fields']:
                out += ['| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |', '| --- | --- | --- | --- | --- |']
                for field in event['fields']:
                    out += ['| '+code(field['alias'])+' | '+code(field['name'])+' | '+cell(field['type'])+' | '+('同步回调中' if field['name'] in event['writable'] else '只读')+' | '+native_description(field['description'],url).replace('|','\\|').replace('\n','<br />')+' |']
                out += ['']
            else:
                out += ['此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。','']
            if event['cancellation'] and event['cancellation'][0]!='cancel':
                field, inverse = event['cancellation']
                out += ['取消映射：'+code('event.cancel = True')+' 等价于 '+code('event.'+field+' = '+str(not inverse))+'。只影响该原生动作。','']
            if '- 备注' in doc:
                remarks = doc.split('- 备注',1)[1].split('### ',1)[0].split('- 示例',1)[0]
                remarks = re.sub(r'```[\s\S]*?```', '', remarks)
                remarks = remarks.split('在零件中直接声明',1)[0].strip()
                if remarks:
                    out += ['**原生前提与限制：**', '', native_description(remarks,url), '']
        put(url, '\n'.join(out))
        current = 'packs/'+side+'/intro.md'
        put(current, PAGES[current]+'\n\n## 原生事件\n\n['+title+']('+link(current,url)+') · [事件用法与示例]('+link(current,'packs/guides/native-events.md')+')')


def semantic_event_pages():
    """Present recommended operations before the exhaustive native catalog."""
    for side, scope, title in (('client','client','客户端语义事件'),('server','world','服务端语义事件')):
        url='packs/'+side+'/semantic-events.md'
        events=[e for e in semantic_catalog() if e['side']==side]
        out=['---','sidebar_position: 2','title: '+title,'---','','# '+title,'',
             '本页按开发用途组织 **%d 个事件入口**，采用 SAPI 风格的信号、类型化参数和订阅筛选。'%len(events),'',
             '可将多个互补的原生通知合并，也可将一个原生批次拆成多个事件。只在需要时注册原生监听；多个入口共享相同原生源，不重复安装引擎监听器。','',
             '[推荐用法与完整示例]('+link(url,'packs/guides/semantic-events.md')+') · [原生事件索引]('+link(url,'packs/client/events.md' if side=='client' else 'packs/server/native-events.md')+')','',
             '## 事件索引','','| 入口 | 参数类型 | 原生源数量 |','| --- | --- | --- |']
        for event in events:
            payload=BY_NAME[event.get('standardPayload',event['payload'])][0]
            out+=['| ['+event['phase']+'Events.'+event['name']+'](#'+event['name'].lower()+') | ['+payload['name']+']('+link(url,payload['url'])+') | '+str(len(event['sources']))+' |']
        for event in events:
            payload=BY_NAME[event.get('standardPayload',event['payload'])][0]
            access=scope+'.'+event['phase']+'Events.'+event['name']
            out+=['','## '+event['name']+' {#'+event['name'].lower()+'}','',
                  '信号：'+code(access)+'；参数：['+payload['name']+']('+link(url,payload['url'])+')。','',
                  '支持筛选：'+', '.join(map(code,('entities','entityTypes','dimensions')+tuple(event['options'])))+'。','',
                  '原生来源：','']
            native_url='packs/client/events.md' if side=='client' else 'packs/server/native-events.md'
            for name in event['sources']:
                out+=['- ['+name+']('+link(url,native_url,name.lower())+')']
            if event['select'] is not None:
                out+=['','此入口仅保留 '+code(event['select'])+' 对应的观察；其他入口仍可独立接收同一原生源。']
            out+=['',fence('from ModSAPI.'+('client' if side=='client' else 'server')+'.beta import '+scope+
                          '\n\ndef on_event(event):\n    print(event)\n\n'+access+
                          '.subscribe(on_event)\n\ndef cleanup():\n    '+access+'.unsubscribe(on_event)')]
        put(url,'\n'.join(out))
        current='packs/'+side+'/intro.md'
        put(current,PAGES[current]+'\n\n## 推荐事件入口\n\n['+title+']('+link(current,url)+') · [语义化设计与示例]('+link(current,'packs/guides/semantic-events.md')+')')


def fields(cls):
    result = dict(cls.get('inherited_fields',{}))
    for node in [cls['source'], cls['stub']]:
        if node is None:
            continue
        for child in node.body:
            if isinstance(child, ast.AnnAssign) and isinstance(child.target, ast.Name) and not child.target.id.startswith('_'):
                result.setdefault(child.target.id,{})['type'] = ast.unparse(child.annotation)
                if child.value:
                    result[child.target.id]['default'] = ast.unparse(child.value)
            elif isinstance(child, ast.Assign):
                for target in child.targets:
                    if isinstance(target,ast.Name) and not target.id.startswith('_'):
                        result.setdefault(target.id,{})['default'] = ast.unparse(child.value)
            elif isinstance(child,ast.FunctionDef) and child.name=='__init__':
                for item in ast.walk(child):
                    if isinstance(item,(ast.Assign,ast.AnnAssign)):
                        targets = item.targets if isinstance(item,ast.Assign) else [item.target]
                        for target in targets:
                            if isinstance(target,ast.Attribute) and isinstance(target.value,ast.Name) and target.value.id=='self' and not target.attr.startswith('_'):
                                result.setdefault(target.attr,{})['assignment'] = ast.unparse(item.value) if item.value else ''
                                if getattr(item,'type_comment',None):
                                    result[target.attr]['type'] = item.type_comment
    # namedtuple fields are declared in the base call, not normal assignments.
    for base in cls['node'].bases:
        if isinstance(base,ast.Call) and isinstance(base.func,ast.Name) and base.func.id=='namedtuple' and len(base.args)>1:
            names = ast.literal_eval(base.args[1]).split()
            for name in names:
                result.setdefault(name, {})['type'] = {'key':'int','isDown':'bool','screenName':'str','direction':'int','soundId':'str'}.get(name,'字段值')
    return {key:value for key,value in result.items() if key not in cls['members']}


def find_base(cls, name):
    candidates = BY_NAME.get(name, [])
    return next((candidate for candidate in candidates if candidate['group']==cls['group']),
                candidates[0] if candidates else None)


def typed_dictionary(cls, seen=None):
    seen=set() if seen is None else seen
    if cls['name'] in seen:return False
    seen.add(cls['name'])
    return ('TypedDict' in cls['bases'] or any(
        typed_dictionary(base,seen) for name in cls['bases']
        if (base:=find_base(cls,name)) is not None))


def inherited(cls, seen=None):
    seen = set() if seen is None else seen
    result = {}
    if cls['url'] in seen:
        return result
    seen.add(cls['url'])
    for name in cls['bases']:
        base = find_base(cls,name)
        if base:
            result.update(inherited(base,seen))
            result.update({member:base for member in list(base['members'])+list(base['fields']) if not member.startswith('_')})
    return result


PARAMS = {
 'player':'目标玩家对象；需要运行时有效且与操作所在端匹配。',
 'playerId':'玩家运行 ID，不是玩家显示名称。', 'entity':'目标实体句柄；是否接受运行 ID 取决于签名。',
 'entityId':'实体运行 ID；跨回调使用前重新确认实体有效性。',
 'id':'运行标识或类型标识，按本成员的说明传入。', 'identifier':'带命名空间的标识，推荐使用本模组前缀。',
 'namespace':'本功能独有的命名空间，避免与其他功能的持久化数据冲突。',
 'location':'位置向量；常用 (x, y, z)，维度由接收对象或选项确定。',
 'position':'位置或坐标；采用本接口所属的原生坐标约定。', 'rotation':'旋转角度，具体分量与单位参见成员说明。',
 'options':'附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。',
 'callback':'回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。',
 'data':'传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。',
 'key':'当前命名空间中的键名；存储接口要求非空字符串。',
 'value':'需要写入的值，类型、范围及副本语义见本成员说明。',
 'defaultValue':'缺省值；具体是缺失键、初始控件值还是原生默认值取决于所属接口。',
 'amount':'物品数量；新物品要求 1–255 的整数，并按最大堆叠数限制。',
 'itemStack':'物品堆叠对象；不是物品名称字符串。', 'slot':'零起始槽位索引，必须在容器容量内。',
 'eventName':'事件或请求名称，推荐加入自己的命名空间。',
 'dataName':'请求的数据通道名称，响应方需事先注册同名处理器。',
 'timeout':'等待秒数；有限且大于零，默认 10 秒。',
 'tickDelay':'延迟请求单位，每单位换算 0.05 秒；具体整数/下限校验见所属端说明。',
 'tickInterval':'周期请求单位，每单位换算 0.05 秒；不是原生渲染帧数。',
 'ticks':'等待请求单位，正整数；每单位换算 0.05 秒。',
 'runId':'run/runTimeout/runInterval 返回的任务标识，不能混用原生计时器 ID。',
 'jobId':'runJob 返回的任务标识。', 'generator':'可迭代的生成器任务；每一步应及时 yield。',
 'blockName':'方块类型标识，例如 minecraft:stone。', 'states':'方块状态字典；不等价于物品 aux 或方块实体数据。',
 'stateName':'方块状态名称。', 'volume':'BlockVolumeBase 或其子类型，端点按方块边界处理。',
 'text':'显示文本；RawMessage 仅支持已实现的字面形式。',
 'title':'标题文本，动态表单也可接受相应 Observable。',
 'label':'控件标签；是否支持 Observable 见当前方法签名。',
 'soundId':'资源包定义的声音标识，不是播放实例句柄的 id。',
 'effectName':'资源包内存在的粒子效果标识。', 'typeId':'带命名空间的实体、物品或资源类型名称。',
 'fadeOutSeconds':'停止时的淡出秒数，需为有限非负值。',
 'minimumValue':'滑块最小值，有限且不大于 maximumValue。',
 'maximumValue':'滑块最大值，有限且不小于 minimumValue。',
 'placeholderText':'输入框占位文本；当前客户端占位符布局尚未接入。',
 'items':'下拉选项集合；标准构建器使用文本列表，CustomForm 使用 label/value 字典列表。',
 'toggleOptions':'选项字典，常用 defaultValue；同时接受布尔初始值。',
 'sliderOptions':'选项字典，常用 defaultValue、valueStep；tooltip 尚无完整渲染。',
 'dropdownOptions':'选项字典，defaultValueIndex 从零起始且必须在列表范围内。',
 'textFieldOptions':'选项字典，常用 defaultValue；tooltip 尚无完整渲染。',
 'uiDef':'JSON UI 定义路径，例如 example.menu，需已存在于资源包。',
 'uiClass':'ScreenNode 子类或其完整 Python 类路径。',
 'extraData':'传给原生屏幕构造器的附加字典。',
 'layout':'布局字典；字段与长度约束见 FormLayout 或 MoreUILayout。',
}


def signature(fn, stub=None):
    args = fn.args
    typed = {arg.arg:ast.unparse(arg.annotation) for arg in (stub.args.args if stub else []) if arg.annotation}
    type_comment = getattr(fn,'type_comment',None) or (getattr(stub,'type_comment',None) if stub else None)
    comment_types=[]
    comment_return=None
    if type_comment and '->' in type_comment:
        before,comment_return=type_comment.rsplit('->',1)
        # Respect nested containers when splitting comment argument types.
        before=before.strip().strip('()')
        depth=0; current=''
        for char in before+',':
            if char in '[({': depth+=1
            if char in '])}': depth-=1
            if char==',' and depth==0:
                comment_types.append(current.strip());current=''
            else: current+=char
    values=[]; rows=[]
    positional=list(args.posonlyargs)+list(args.args)
    defaults=[None]*(len(positional)-len(args.defaults))+list(args.defaults)
    comment_index=0
    for arg,default in zip(positional,defaults):
        if arg.arg in ('self','cls'):
            continue
        annotation=ast.unparse(arg.annotation) if arg.annotation else typed.get(arg.arg)
        if not annotation and comment_index<len(comment_types):
            annotation=comment_types[comment_index]
        comment_index+=1
        item=arg.arg
        if annotation: item+=': '+annotation
        if default is not None: item+=' = '+ast.unparse(default)
        values.append(item)
        rows.append((arg.arg, annotation or '由值/所属选项确定', ast.unparse(default) if default is not None else '必填'))
    for prefix,arg in [('*',args.vararg),('**',args.kwarg)]:
        if arg:
            values.append(prefix+arg.arg)
            rows.append((prefix+arg.arg, '可变参数', '可省略'))
    result=ast.unparse(fn.returns) if fn.returns else (ast.unparse(stub.returns) if stub and stub.returns else comment_return)
    return '('+', '.join(values)+')'+(' -> '+result.strip() if result else ''),rows,result


def empty(fn):
    body=[node for node in fn.body if not (isinstance(node,ast.Expr) and isinstance(node.value,ast.Constant) and isinstance(node.value.value,str))]
    return not body or all(isinstance(node,ast.Pass) or (isinstance(node,ast.Return) and (node.value is None or isinstance(node.value,ast.Constant) and node.value.value is None)) or (isinstance(node,ast.Expr) and isinstance(node.value,ast.Constant) and node.value.value is Ellipsis) for node in body)


def exception_rows(fn):
    result=[]
    for node in ast.walk(fn):
        if isinstance(node,ast.Raise) and node.exc:
            target=node.exc.func if isinstance(node.exc,ast.Call) else node.exc
            name=ast.unparse(target) if isinstance(target,(ast.Name,ast.Attribute)) else 'Exception'
            message=ast.unparse(node.exc.args[0]) if isinstance(node.exc,ast.Call) and node.exc.args else '参见本成员的前置条件。'
            row=(name,message)
            if row not in result: result.append(row)
    return result


def native_calls(fn):
    values=[]
    for node in ast.walk(fn):
        if isinstance(node,ast.Call):
            if isinstance(node.func,ast.Attribute) and node.func.attr[:1].isupper() and not node.func.attr.startswith('Create'):
                values.append(node.func.attr)
            elif isinstance(node.func,ast.Name) and node.func.id in ('call','checked') and len(node.args)>1 and isinstance(node.args[1],ast.Constant) and isinstance(node.args[1].value,str):
                values.append(node.args[1].value)
            elif isinstance(node.func,ast.Name) and node.func.id=='_readExtraData':
                # This shared adapter replaced a direct native read. Derive its
                # operation from the maintained helper, retaining traceability.
                helper=next(value for value in parse(BASE/'utils/extra_data.py').body
                            if isinstance(value,ast.FunctionDef) and value.name=='readExtraData')
                values.extend(native_calls(helper))
    return list(dict.fromkeys(values))


def description(cls,name,member):
    fn=member['node']
    doc=ast.get_docstring(fn)
    if not doc:
        stub=cls['stub_members'].get(name,{}).get('node')
        doc=ast.get_docstring(stub) if stub else None
    if doc: return clean(chinese(doc))
    if name=='__init__': return '构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。'
    calls=native_calls(fn)
    if member['kind']=='property':
        return '读取 '+code(name)+' 的当前值。'+('底层调用 '+', '.join(map(code,calls))+'。' if calls else '')
    if empty(fn): return '当前没有功能性实现，不应依赖此成员完成操作。'
    for node in ast.walk(fn):
        if isinstance(node,ast.Return) and isinstance(node.value,ast.Name) and node.value.id=='self':
            return '设置或追加 '+code(name)+' 对应的配置，返回当前对象以便继续构建。'
    if name.startswith('get'): prefix='读取'
    elif name.startswith('set'): prefix='设置'
    elif name.startswith(('remove','delete','clear','dispose','Destroy')): prefix='移除或清理'
    elif name.startswith(('has','is','contains','matches')): prefix='检查'
    elif name.startswith(('add','create','spawn','register')): prefix='创建或登记'
    else: prefix='执行'
    return prefix+' '+code(name)+' 操作。'+('原生实现使用 '+', '.join(map(code,calls))+'，行为受网易运行环境约束。' if calls else '参数形态和结果约定如下。')


ACQUIRE = {
 'World':'从服务端入口导入 `world` 单例。', 'System':'从服务端入口导入 `system` 单例。',
 'Client':'从客户端入口导入 `client` 单例。', 'Player':'通过 `world.getAllPlayers()`、玩家事件或有效玩家 ID 获取。',
 'Entity':'通过维度查询、事件参数或 `world.getEntity(id)` 获取；查找可能返回 None。',
 'Dimension':'使用 `world.getDimension("overworld")` 等；对象的维度也可从实体或方块读取。',
 'Block':'使用 `dimension.getBlock(location)`；这是位置包装器，不是不可变方块快照。',
 'BlockPermutation':'从 `block.permutation` 读取，或从服务端入口导入 BlockPermutation 并 resolve。',
 'BlockType':'通常从 `block.type` 或 `block.permutation.type` 读取。',
 'Container':'从实体/方块的库存组件读取 container。不要直接构造与引擎脱离的容器。',
 'ContainerSlot':'使用 `container.getSlot(index)`，index 从零开始。',
 'ItemStack':'从服务端入口导入 ItemStack，或从容器读取物品副本。',
 'ClientPlayer':'使用 `client.localPlayer`。', 'ClientEntity':'使用 `client.getEntity(id)` 或 `client.spawnEntity(...)`。',
 'ClientCamera':'使用 `client.camera`。',
 'Audio':'使用 `client.audio`。', 'SoundPlayback':'由 `client.audio.playSound(...)` 返回。',
 'Screen':'使用 `client.screen`。', 'Particle':'客户端发射器由 `client.spawnParticle(...)` 返回。',
 'DynamicParticle':'由 `client.spawnDynamicParticle(...)` 返回。',
 'KeyValueStorage':'使用 `world.getStorage(namespace)` 或 `client.getStorage(namespace, options)`。',
 'Promise':'从异步请求、表单或等待操作获取，不需要直接构造。',
 'Expression':'底层数值表达式对象，可从相关算术或界面变量操作取得。它不是文本表达式 ExpressionString，也不是模板入口的直接导出符号。',
 'ScriptEventCommandMessageAfterEvent':'通过 system.afterEvents.scriptEventReceive 的订阅回调取得。具体解析规则和示例见脚本指令事件指南。',
 'ScriptEventCommandMessageAfterEventSignal':'从 system.afterEvents.scriptEventReceive 获取信号；使用 subscribe 订阅，用 unsubscribe 注销。',
 'ScriptBridge':'使用 system.scriptBridge 或 client.scriptBridge；由对应端的生命周期管理，不自行构造。',
 'ScriptBridgeAfterEvents':'从 system.scriptBridge.afterEvents 或 client.scriptBridge.afterEvents 获取。',
 'ScriptBridgeMessageSignal':'从 scriptBridge.afterEvents.messageReceive 获取，使用 subscribe 和 unsubscribe 管理订阅。',
 'ScriptBridgeMessage':'通过桥接消息回调或已注册处理器的参数取得，不自行构造。',
 'ScriptBridgeError':'从模板入口导入以识别桥接失败；code 表示稳定错误码，remoteName 保留远端异常名称。',
 'MoreUI':'模板通过 `from ModSAPI.serverui.system import systems` 后使用 `systems.modules.MoreUI`；它未直接导出到 serverui.beta。',
 'UIManager':'从 serverui.beta 导入 uiManager 单例；也可获取 UIManager 类型。',
}
ACQUIRE.update(ACQUIRE_EXTRA)
ACQUIRE.update(UI_ACQUIRE)


def member_example(cls,name,member):
    fn=member['node']
    if empty(fn): return ''
    if name=='__init__': return ''
    if member['kind']=='property':
        value='def read_value(instance):\n    return instance.'+name
        if 'setter' in member:
            value+='\n\ndef write_value(instance, value):\n    instance.'+name+' = value'
        return fence(value)
    positional=[arg.arg for arg in fn.args.args if arg.arg not in ('self','cls')]
    count=len(positional)-len(fn.args.defaults)
    needed=positional[:max(0,count)]
    target='type_object' if member.get('static') else 'instance'
    decl=[target]+needed
    call=list(needed)
    if fn.args.vararg:
        decl.append('*'+fn.args.vararg.arg);call.append('*'+fn.args.vararg.arg)
    if fn.args.kwarg:
        decl.append('**'+fn.args.kwarg.arg);call.append('**'+fn.args.kwarg.arg)
    return fence('def call_'+name+'('+', '.join(decl)+'):\n    return '+target+'.'+name+'('+', '.join(call)+')')


def native_access(event):
    """Use explicit native lookup when the observation has a canonical entry."""
    collection=('client' if event['side']=='client' else 'world')+'.'+event['phase']+'Events'
    return collection+'.'+event['alias'] if event.get('publicAlias') else collection+'.getNativeEvent('+repr(event['name'])+')'


def event_sources():
    mappings={'ScriptEventCommandMessageAfterEvent':'system.afterEvents.scriptEventReceive',
              'ScriptBridgeMessage':'system.scriptBridge.afterEvents.messageReceive'}
    for event in semantic_catalog():
        mappings.setdefault(event.get('standardPayload',event['payload']),('client' if event['side']=='client' else 'world')+'.'+event['phase']+'Events.'+event['name'])
    for event in native_catalog():
        mappings[event['payload']] = native_access(event)
    for group,container,access in [('server','WorldAfterEvents','world.afterEvents'),('server','WorldBeforeEvents','world.beforeEvents'),('server','SystemAfterEvents','system.afterEvents'),('server','SystemBeforeEvents','system.beforeEvents')]:
        choices=[c for c in BY_NAME.get(container,[]) if c['group']==group]
        if not choices:continue
        cls=choices[0]; types={}
        for node in ast.walk(cls['node']):
            if isinstance(node,ast.Assign) and isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name):
                for target in node.targets:
                    if isinstance(target,ast.Attribute):types[target.attr]=node.value.func.id
        for name,member in cls['members'].items():
            if member['kind']!='property':continue
            for node in ast.walk(member['node']):
                if isinstance(node,ast.Return) and isinstance(node.value,ast.Attribute) and node.value.attr in types:
                    mappings[types[node.value.attr]]=access+'.'+name
    return mappings


def render(cls, signals):
    name=cls['name']; url=cls['url']; source=cls['path'].relative_to(SOURCE).as_posix()
    title=name
    out=['---','title: '+json.dumps(title,ensure_ascii=False),'sidebar_label: '+json.dumps(name,ensure_ascii=False),'---','', '# '+name, '']
    out += ['作用域：'+{'server':'服务端','client':'客户端','server_ui':'服务端表单 / 客户端 UI 底层类型','ui':'界面、控件和两端组合表单','common':'公共数据、选项、枚举与错误','architecture':'架构辅助接口'}[cls['group']]+'。', '',
            '源码：'+code(source)+('；声明补充了静态类型信息。' if cls['stub'] else '。'), '']
    if cls.get('dynamic_native'):
        out+=['此类型由运行时事件契约创建，并通过对应端的 `beta` 导出。通过 `subscribe` 回调取得实例；不要自行构造事件参数。','']
    elif cls['source'] is None:
        out+=[':::info 字典结构或静态声明','此类型只出现在补全声明中，不是可从模板直接实例化的运行时类。作为选项时使用符合字段约定的 Python 字典。',':::','']
    elif cls['group'] == 'ui' and '/interfaces/base/' in source:
        out+=['这是界面模板描述或登记入口，通过 ModSAPI.ui 获取。控件登记需要相应描述对象，不能用普通字典替代。','']
    elif 'interfaces/' in source or any('TypedDict' in ast.unparse(b) for b in cls['node'].bases):
        out+=['选项通常可直接传 Python 字典；包装类名本身不保证通过模板导出。只使用所属操作已经实现的字段。','']
    doc=ast.get_docstring(cls['node']) or (ast.get_docstring(cls['stub']) if cls['stub'] else None)
    if doc:out+=[clean(chinese(doc)),'']
    acquire = ('通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。' if cls.get('dynamic_native') or name in signals else
               {'ClientBeforeEvents':'从 client.beforeEvents 获取。', 'ClientAfterEvents':'从 client.afterEvents 获取。'}.get(name,
               ACQUIRE.get(name,'使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。')))
    if name in ('ScriptEventCommandMessageAfterEvent','ScriptEventCommandMessageAfterEventSignal',
                'ScriptBridgeMessage','ScriptBridgeMessageSignal','ScriptBridge','ScriptBridgeAfterEvents','ScriptBridgeError'):
        acquire=ACQUIRE[name]
    out+=['## 获取方式','',acquire,'']
    if name in signals:
        out+=['所属信号：'+code(signals[name])+'.','']
    bases=[find_base(cls,base) for base in cls['bases']]
    if any(bases):
        out+=['基类：'+', '.join('['+base['name']+']('+link(url,base['url'])+')' for base in bases if base)+'.','']
    if cls['fields']:
        out+=['## 字段与常量','', '| 名称 | 类型线索 | 默认值 / 来源 |','| --- | --- | --- |']
        for key,value in cls['fields'].items():
            out+=['| '+code(key)+' | '+references.annotation(value.get('type','由运行时值确定'),url)+' | '+code(value.get('default',value.get('assignment','运行时返回')))+' |']
        out+=['','字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。','']
    members={key:value for key,value in cls['members'].items() if not key.startswith('_') or key=='__init__'}
    if members:
        out+=['## 成员索引','', '| 名称 | 形态 |','| --- | --- |']
        for key,value in members.items():
            kind='只读属性' if value['kind']=='property' and 'setter' not in value else '可读写属性' if value['kind']=='property' else '构造器' if key=='__init__' else '静态/类方法' if value.get('static') else '方法'
            out+=['| ['+key+'](#'+('constructor' if key=='__init__' else key)+') | '+kind+' |']
        out+=['']
    inherited_members={key:owner for key,owner in inherited(cls).items() if key not in members and key not in cls['fields']}
    if inherited_members:
        out+=['## 继承成员','', '下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。','', '| 成员 | 定义位置 |','| --- | --- |']
        for key,owner in sorted(inherited_members.items()):
            anchor=key if key in owner['members'] else '字段与常量'
            out+=['| ['+key+']('+link(url,owner['url'],anchor)+') | '+owner['name']+' |']
        out+=['']
    for key,member in members.items():
        fn=member['node']; stub=cls['stub_members'].get(key,{}).get('node')
        sig,params,returns=signature(fn,stub)
        display=(key+(': '+returns.strip() if returns else '')) if member['kind']=='property' else (name if key=='__init__' else key)+sig
        out+=['## '+('构造器' if key=='__init__' else key)+' {#'+('constructor' if key=='__init__' else key)+'}','']
        if name=='WorldAfterEvents' and key=='entityHurt':
            out+=['<span id="entityhurt" />','']
        out+=['```python', display, '```','', description(cls,key,member),'']
        if name+'.'+key in NOTES:out+=[':::note 当前实现说明',native_description(NOTES[name+'.'+key],url) if cls.get('dynamic_native') else clean(NOTES[name+'.'+key]),':::','']
        if empty(fn) and cls['source'] is not None and not (ast.get_docstring(fn) or '').startswith(('Native catalog signal:', 'Semantic event:')):
            out+=[':::warning 空实现 / 基类占位','源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。',':::','']
        if member['kind']=='property':
            out+=['**访问：** '+('可读写。' if 'setter' in member else '只读。'),'']
            if 'setter' in member:
                setter=member['setter']; setter_sig,setter_params,_=signature(setter,cls['stub_members'].get(key,{}).get('setter'))
                out+=['写入方式：'+code('instance.'+key+' = value')+'。参数类型线索：'+code(setter_sig)+'。','']
                setter_doc=ast.get_docstring(setter)
                if setter_doc:out += [clean(chinese(setter_doc)),'']
                for param,typ,_ in setter_params:
                    out += ['写入参数 '+code(param)+'：'+references.annotation(typ,url)+'。','']
        elif params:
            out+=['### 参数','', '| 名称 | 类型线索 | 默认值 | 说明 |','| --- | --- | --- | --- |']
            for param,typ,default in params:
                explanation=PARAMS.get(param.lstrip('*'),'传给 '+name+'.'+key+' 的 '+param+' 参数；结合上方功能说明和下方调用示例使用。')
                out+=['| '+code(param)+' | '+references.annotation(typ,url)+' | '+code(default)+' | '+cell(explanation)+' |']
            out+=['']
        if returns:
            out+=['**返回类型：** '+references.annotation(returns.strip(),url)+'。静态声明不替代本页的实现限制。','']
        else:
            nodes=[node for node in ast.walk(fn) if isinstance(node,ast.Return)]
            if not nodes or all(node.value is None for node in nodes):return_note='当前实现不显式返回结果，Python 返回 None。'
            elif any(isinstance(node.value,ast.Name) and node.value.id=='self' for node in nodes):return_note='当前对象，可继续链式构建。'
            else:return_note='源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。'
            out+=['**返回值：** '+return_note,'']
        errors=exception_rows(fn)
        if 'setter' in member:errors+=exception_rows(member['setter'])
        if errors:
            out+=['### 显式异常','', '| 异常 | 校验信息 / 条件线索 |','| --- | --- |']
            out+=['| '+references.annotation(error,url)+' | '+code(message)+' |' for error,message in dict.fromkeys(errors)]
            out+=['']
        out+=['引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。','']
        calls=native_calls(fn)
        if calls:out+=['**原生调用：** '+', '.join(map(code,calls))+'。','']
        example=member_example(cls,key,member)
        if example:out+=['### 调用形状','', '此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。',example]
    out+=['## 使用示例','']
    example=CLASS_EXAMPLES.get(name)
    if cls['group']=='client' and name=='KeyValueStorage':example=example.replace('from ModSAPI.server.beta import world','from ModSAPI.client.beta import client').replace('world.getStorage','client.getStorage')
    if name in signals:
        access=signals[name]; singleton=access.split('.')[0]
        example='from ModSAPI.'+('client' if singleton=='client' else 'server')+'.beta import '+singleton+'\n\ndef on_event(event):\n    print(event)\n\n'+access+'.subscribe(on_event)\n\ndef cleanup():\n    '+access+'.unsubscribe(on_event)'
    if not example:
        readable=[key for key,member in members.items() if member['kind']=='property']+list(cls['fields'])
        structural=cls['source'] is None and typed_dictionary(cls)
        if structural and readable:
            example='def inspect_options(options):\n'+''.join('    print(options.get('+repr(key)+'))\n' for key in readable[:3])
        elif readable:
            example='def inspect_value(value):\n    # value 是上方获取方式取得的 '+name+' 对象。\n'+''.join('    print(value.'+key+')\n' for key in readable[:3] if key.isidentifier())
        else:example='def inspect_value(value):\n    # value 是所属 API 返回或接收的 '+name+' 值。\n    print(value)'
    out += [fence(example), '需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。', '', '[返回接口总览]('+link(url,'packs/guide.md')+') · [场景指南]('+link(url,'packs/examples.md')+')']
    return '\n'.join(out)


def indexes():
    put('packs/guides/_category_.json', json.dumps({'label':'场景指南','position':7},ensure_ascii=False))
    groups=[('server','服务端'),('client','客户端'),('server_ui','标准表单'),('ui','界面与主题表单'),('common','公共类型与错误'),('architecture','架构辅助接口')]
    for index,(group,title) in enumerate(groups,2):
        put('packs/'+group+'/_category_.json', json.dumps({'label':title,'position':index,'link':{'type':'doc','id':'intro'}},ensure_ascii=False,indent=2))
        url='packs/'+group+'/intro.md'
        lines=['---','sidebar_position: 1','title: '+title,'---','','# '+title,'']
        if group=='server':lines+=['入口：`from ModSAPI.server.beta import world, system`。其他导出见 [导出符号](../exports.md)。','']
        elif group=='client':lines+=['入口：`from ModSAPI.client.beta import client`。所有操作只影响本机；客户端数据不能替代服务端权限校验。','']
        elif group=='server_ui':lines+=['标准表单入口：`from ModSAPI.serverui.beta import ActionFormData, ModalFormData, MessageFormData`。其他类型与入口见 [导出符号](../exports.md)。','', '标准构建器在服务端调用；JSON UI 控件底层类型在客户端工作，不要混用执行端。','']
        elif group=='ui':lines+=['入口：client.ui、system.ui 和 ModSAPI.ui。视图、控件、主题、状态和组合表单共用现有运行时。','', '[视图与生命周期](../guides/managed-ui.md) · [布局与控件](../guides/ui-layout-and-widgets.md) · [选择控件与小地图](../guides/ui-choices-and-minimap.md) · [组合表单](../guides/themed-forms.md) · [动画与跟随界面](../guides/ui-animation-and-hud.md) · [自定义模板](../guides/ui-custom-controls.md)','']
        lines+=['[场景与完整示例](../examples.md) · [支持情况与差异](../compatibility.md)','',
                '<div className="modsapi-table-scroll" tabIndex={0} aria-label="接口表格，可横向滚动">','',
                '| 类型 | 说明 |','| --- | --- |']
        for cls in sorted((c for c in CLASSES if c['group']==group),key=lambda c:c['name'].lower()):
            doc=chinese(ast.get_docstring(cls['node']) or '').split('\n')[0]
            lines+=['| ['+cls['name']+']('+link(url,cls['url'])+') | '+cell(doc or '签名、字段、属性、方法与调用示例')+' |']
        lines+=['','</div>']
        put(url,'\n'.join(lines))
        put('packs/'+group+'/reference/_category_.json',json.dumps({'label':'类型参考','position':4},ensure_ascii=False))
    guide='packs/examples.md'
    lines=['---','sidebar_position: 2','title: 使用示例与场景指南','---','','# 使用示例与场景指南','','下列指南给出当前实现可对应的完整调用场景。标记为资源依赖的示例需要自己的资源包定义；模板中的导入写法与当前代码一致。','']
    for path,text in GUIDES.items():
        if '/guides/' not in path:continue
        title=next(line[7:] for line in text.splitlines() if line.startswith('title: '))
        lines+=['- ['+title+']('+link(guide,path)+')']
    put(guide,'\n'.join(lines))


def exports():
    path='packs/exports.md'
    lines=['---','sidebar_position: 3','title: 模板导出符号与获取方式','---','','# 模板导出符号与获取方式','','只有下列直接导出名可以按当前模板直接导入。参考页存在某个类型，不代表模板一定重新导出了它；返回类型、事件参数和底层包装器通常从所属对象取得。','']
    for side,folder in [('server','server'),('serverui','server_ui'),('client','client'),('ui','ui')]:
        file=(BASE/'ui/__init__.py') if side=='ui' else SOURCE/'mod_behavior/Scripts_Sample/ModSAPI'/side/'beta.py'
        tree=parse(file)
        names=[]
        for node in tree.body:
            if isinstance(node,ast.Assign):
                names.extend(target.id for target in node.targets if isinstance(target,ast.Name) and not target.id.startswith('_'))
        if side=='client':
            tree=parse(BASE/'modules/client/exports.py')
            names+=next(ast.literal_eval(node.value) for node in tree.body if isinstance(node,ast.Assign) and any(isinstance(target,ast.Name) and target.id=='__all__' for target in node.targets))
        if side=='ui':
            names=next(ast.literal_eval(node.value) for node in tree.body if isinstance(node,ast.Assign) and any(isinstance(target,ast.Name) and target.id=='__all__' for target in node.targets))
        if side in ('client', 'server'):
            names += ['NativeEventData', 'NativeEventSignal']
            names += [event['payload'] for event in native_catalog() if event['side']==side]
            if side=='server':
                names += ['WorldAfterEvents', 'WorldBeforeEvents']
            names += ['EventSignal','EventItemStack','EventBlock','InputDevice']
            names += sorted(set(event['payload'] for event in semantic_catalog()))
        module='ModSAPI.ui' if side=='ui' else 'ModSAPI.'+side+'.beta'
        names_example={'server':'world, system','serverui':'ActionFormData, ModalFormData, MessageFormData','client':'client','ui':'Form, Observable, Control, Theme'}[side]
        lines+=['## '+side,'', '```python','from '+module+' import '+names_example,'```','', '| 符号 | 类型参考 |','| --- | --- |']
        for name in dict.fromkeys(names):
            typ={'world':'World','system':'System','client':'Client','uiManager':'UIManager'}.get(name,name)
            options=BY_NAME.get(typ,[])
            cls=next((c for c in options if c['group']==folder),options[0] if options else None)
            target='['+typ+']('+link(path,cls['url'])+')' if cls else ('跨端函数装饰器，见 [通信指南](guides/communication.md)' if name.endswith('Callable') else '由模板提供的运行时对象')
            lines+=['| '+code(name)+' | '+target+' |']
        lines+=['']
    lines+=['## 提供器访问','','部分补充类型通过模块提供器获取，而不是从 beta 直接导入。',fence('from ModSAPI.serverui.system import systems\n\nMoreUI = systems.modules.MoreUI'), '其余类型请按对应参考页的获取方式使用。']
    put(path,'\n'.join(lines))


def compatibility():
    inventory=json.loads((SOURCE/'audit/API_INVENTORY.json').read_text(encoding='utf-8'))
    versions={value['module']: value['version'] for value in inventory['modules']}
    baseline='server '+versions['@minecraft/server']+' / server-ui '+versions['@minecraft/server-ui']
    lines=['---','sidebar_position: 4','title: 官方对照与当前支持情况','---','','# 官方对照与当前支持情况','','比较基准为微软稳定版 '+baseline+'。此页记录**结构对照**，不以名称存在、字典结构或枚举常量来宣称功能已经完整实现。客户端模块是网易扩展。','', '状态：未实现 = 当前没有对应运行时类型；结构契约 = 参数/数据形状；部分 = 存在缺失或显式拒绝；待行为核验 = 名称和成员存在，仍需核验原生语义。','']
    for module in inventory['modules']:
        lines+=['## '+module['module']+' '+module['version'],'', '[微软模块文档]('+module['documentation']+')','', '### 已知限制','']
        for name,reason in module['deferred_cases'].items():
            if 'dropdown/dynamic' in name:
                reason='当前实现会重建变化的下拉项目并复用未变化节点；真实客户端布局和更新时序仍需实机验证。'
            lines+=['- '+code(name)+'：'+clean(chinese(reason))]
        lines+=['','### 全部官方类型对照','', '| 名称 | 类别 | 当前结构状态 | 缺失 / 空成员 |','| --- | --- | --- | --- |']
        translations={'not_implemented':'未实现','structural_data_contract':'结构契约','partial':'部分','constant_definition':'常量定义','present_requires_behavior_review':'待行为核验'}
        for entry in module['entries']:
            gaps=[member['name'] for member in entry['members'] if member['status'] in ('not_implemented','empty_implementation','partial_explicitly_unsupported_case')]
            lines+=['| '+code(entry['name'])+' | '+{'class':'类','interface':'接口','enum':'枚举','type_alias':'类型别名','typeAlias':'类型别名','function':'函数','variable':'变量','constant':'常量'}.get(entry['kind'],entry['kind'])+' | '+translations.get(entry['status'],entry['status'])+' | '+cell(', '.join(gaps) or '—')+' |']
        lines+=['']
    put('packs/compatibility.md','\n'.join(lines))


def modsdk_coverage():
    report=json.loads((SOURCE/'audit/MODSDK_API_INVENTORY.json').read_text(encoding='utf-8'))
    url='packs/modsdk-coverage.md'
    labels={'reviewed_adapter_path':'已有离线核验路径', 'candidate_requires_review':'发现原生调用，待核对', 'unmapped':'尚未建立映射'}
    lines=['---','sidebar_position: 5','title: ModSDK 功能映射与待补接口','---','', '# ModSDK 功能映射与待补接口','',
           '本页按网易官方接口索引逐项保留执行端、原生文档和当前适配记录。原生列表共 '+str(report['summary']['native_bindings'])+' 条执行端绑定；同名接口在不同类别或两端出现时分别计算。','',
           '**目前不能确认本库已覆盖绝大多数 ModSDK 功能。** 名称匹配只用于定位候选调用；已有离线核验路径也只证明列出的功能子集，不表示支持原生接口的全部参数、平台或游戏时序。','',
           '| 当前记录 | 数量 | 含义 |','| --- | --- | --- |',
           '| 已有离线核验路径 | '+str(report['summary']['statuses'].get('reviewed_adapter_path',0))+' | 已核对公开入口并有具体契约测试；仍需游戏验证。 |',
           '| 发现原生调用，待核对 | '+str(report['summary']['statuses'].get('candidate_requires_review',0))+' | 源码出现了相同原生调用名，不能据此判断功能覆盖。 |',
           '| 尚未建立映射 | '+str(report['summary']['statuses'].get('unmapped',0))+' | 尚未建立可追溯记录；不能直接解释为原生能力不存在或无法封装。 |','',
           '常用界面流程见 [界面、控件与生命周期](guides/managed-ui.md)、[主题表单](guides/themed-forms.md) 和 [选择控件与小地图](guides/ui-choices-and-minimap.md)。原生模型控件、专有渲染和平台能力仍有大量接口待适配。使用 native 访问原生对象，不会自动使这些能力成为本库已实现的接口。','',
           '微软接口的对照与已知限制另见 [官方对照与当前支持情况](compatibility.md)。以下列表中的 Apollo 标记保留原文的服务端平台限制。','',
           '[网易官方接口索引]('+report['source']['url']+')','']
    groups=defaultdict(list)
    for row in report['bindings']:
        groups[row['category']].append(row)
    for category, rows in groups.items():
        lines+=['## '+category,'',
                '<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">','',
                '| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |','| --- | --- | --- | --- |']
        for row in rows:
            targets=[]
            for name in row['public_api']:
                target=references.resolve(name,url)
                if target is None:
                    raise ValueError('Reviewed public API cannot be linked: '+name)
                targets.append('['+name+']('+target+')')
            side={'client':'客户端','server':'服务端','unspecified':'未指定'}[row['side']]
            if row['platform']=='Apollo':side+='（Apollo）'
            lines+=['| ['+row['name']+']('+row['documentation']+') | '+side+' | '+labels[row['status']]+' | '+', '.join(targets or ['—'])+' |']
        lines+=['','</div>','']
    put(url,'\n'.join(lines))


def site_navigation(config):
    """Avoid two active doc items sharing Docusaurus's API sidebar."""
    ui_guides='(?:managed-ui|themed-forms|ui-animation-and-hud|ui-custom-controls|ui-layout-and-widgets|ui-choices-and-minimap)'
    definitions={
        'packs/server/intro': ('接口文档', '/docs/packs/server/intro',
            '^/docs/packs/(?!ui(?:/|$)|guides/'+ui_guides+'(?:/|$))'),
        'packs/ui/intro': ('界面', '/docs/packs/ui/intro',
            '^/docs/(?:packs/(?:ui(?:/|$)|guides/'+ui_guides+'(?:/|$))|extra_lib/(?:FormUI|Interfaces)(?:/|$))'),
    }
    config=config.replace("docId: 'extra_lib/FormUI/intro'", "docId: 'packs/ui/intro'").replace("label: '独立库'", "label: '界面'")
    for document, (label, route, active) in definitions.items():
        pattern=r"\{\s*type: 'doc',\s*position: 'left',\s*docId: '"+re.escape(document)+r"',\s*label: '"+label+r"',\s*\}"
        replacement="{\n            position: 'left',\n            to: '"+route+"',\n            label: '"+label+"',\n            activeBaseRegex: '"+active+"',\n        }"
        config=re.sub(pattern,lambda match:replacement,config)
        # Update already converted entries when a new UI guide is added.
        existing=r"(to: '"+re.escape(route)+r"',\s*label: '"+label+r"',\s*activeBaseRegex: ')[^']*(')"
        config=re.sub(existing,lambda match:match[1]+active+match[2],config)
    return config


def generate():
    load()
    MISSING.clear()
    references.configure(CLASSES, native_catalog())
    put(references.TYPE_PAGE, references.type_page())
    for event in native_catalog():
        for field in event['fields']:
            NOTES[event['payload']+'.'+field['alias']] = field['description'] + ('；此字段可在同步回调中赋值。' if field['name'] in event['writable'] else '；只读。')
    versions={value['module']: value['version'] for value in json.loads((SOURCE/'audit/API_INVENTORY.json').read_text(encoding='utf-8'))['modules']}
    for path,text in list(GUIDES.items()):
        text=text.replace('@@SERVER_VERSION@@', versions['@minecraft/server']).replace('@@SERVER_UI_VERSION@@', versions['@minecraft/server-ui'])
        text=re.sub(r'```python\s*\n(.*?)\n```',
                    lambda match:'```python\n'+python_example(match[1])+'\n```',text,flags=re.S)
        GUIDES[path]=text
        put(path,text)
        PYTHON_EXAMPLES.extend(re.findall(r'```python\s*\n(.*?)\n```',text,re.S))
    signals=event_sources()
    for cls in CLASSES:put(cls['url'],render(cls,signals))
    indexes();exports();compatibility();modsdk_coverage();function_pages();type_aliases();native_event_pages();semantic_event_pages()
    # Replace obsolete short reference pages with links to maintained, complete references.
    server_events = GUIDES['packs/guides/server-events.md'].replace('title: 服务端事件与实体查询','title: 事件监听与注销')
    server_events = server_events.replace('(../server/native-events.md)', '(../native-events.md)').replace('(native-events.md)', '(../../guides/native-events.md)')
    put('packs/server/events/event_listen.md',server_events+'\n\n[全部 after 事件](afterEvents.md) · [全部 before 事件](beforeEvents.md)')
    custom_ui=GUIDES['packs/guides/custom-screen.md']
    for guide in ('observable-forms', 'managed-ui', 'themed-forms', 'ui-animation-and-hud', 'ui-custom-controls', 'ui-layout-and-widgets', 'ui-choices-and-minimap'):
        custom_ui=custom_ui.replace('('+guide+'.md)', '(../../guides/'+guide+'.md)')
    put('packs/client/apis/customUI.md', custom_ui)
    options=['# 选项与数据结构','', '使用 Python 字典传入选项，以下参考列出当前包装类的字段、默认值和限制。','']
    for cls in CLASSES:
        if cls['path'].parent==BASE/'interfaces':options+=['- ['+cls['name']+']('+link('packs/server/extra/options.md',cls['url'])+')']
    put('packs/server/extra/options.md','\n'.join(options))
    info=['# 事件与命中信息','', '下列对象由实体、伤害或射线 API 返回，不应混用网易原生字典的字段名。','']
    for name in ('EntityDamageSource','BlockHitInformation','EntityHitInformation','EntityRaycastHit','BlockRaycastHit'):
        for cls in BY_NAME.get(name,[]):info+=['## '+name+' {#'+name+'}','', '['+name+' 完整参考]('+link('packs/server/extra/info.md',cls['url'])+')','']
    put('packs/server/extra/info.md','\n'.join(info))
    intro=(SITE/'docs/intro.md').read_text(encoding='utf-8-sig')
    intro=re.sub(r'\n\n## 继续学习\n[\s\S]*$', '', intro)
    intro=re.sub(r':::info\s*\n您可以指定导入的ModSAPI版本[\s\S]*?\n:::',
                 ':::info\n当前文档以正在维护的模板入口和核心实现为准。官方对照版本与本库发布版本不是同一概念，详见 [接口总览](packs/guide.md)。\n:::',intro)
    intro+='\n\n## 继续学习\n\n- [接口总览与模块入口](packs/guide.md)\n- [完整场景与使用示例](packs/examples.md)\n- [当前支持情况与官方差异](packs/compatibility.md)\n- [ModSDK 功能映射与待补接口](packs/modsdk-coverage.md)\n'
    put('intro.md',intro)
    # Keep existing routes while directing all UI usage to the integrated module.
    integrated_articles = {
        'FormUI/intro': ('界面模块', 'managed-ui'),
        'FormUI/quickstart': ('组合表单入门', 'themed-forms'),
        'FormUI/layout-parameters': ('界面布局', 'themed-forms'),
        'FormUI/group-controls': ('组合控件', 'ui-custom-controls'),
        'FormUI/custom-controls': ('自定义模板', 'ui-custom-controls'),
        'FormUI/flutter-ui': ('Flutter 风格控件', 'themed-forms'),
        'FormUI/fluent-ui': ('Fluent 风格控件', 'themed-forms'),
        'FormUI/skill-usage': ('界面开发步骤', 'managed-ui'),
        'FormUI/test-examples': ('界面示例', 'managed-ui'),
        'Interfaces/intro': ('界面类型入口', 'managed-ui'),
        'Interfaces/form': ('组合表单参考', 'themed-forms'),
        'Interfaces/observable': ('响应式状态参考', 'themed-forms'),
        'Interfaces/extra': ('控件与布局类型', 'ui-custom-controls'),
    }
    for relative, (title, guide) in integrated_articles.items():
        path='extra_lib/'+relative+'.md'
        text=['---', 'title: '+title, '---', '', '# '+title, '',
              '界面功能已整合到 ModSAPI.ui。通过 client.ui 或 system.ui 使用现有运行时，不需要额外注册系统。', '',
              '[完整教程与示例]('+link(path, 'packs/guides/'+guide+'.md')+') · '+
              '[界面模块全部类型]('+link(path, 'packs/ui/intro.md')+')', '',
              '```python', 'from ModSAPI.ui import Form, Observable, Control, Theme', '```', '',
              '服务端显示表单时传入 Player 对象；客户端省略目标时使用本地玩家。关闭结果通过 player 属性取得包装对象。', '',
              '[Form]('+link(path, 'packs/ui/reference/Form.md')+') · '+
              '[Observable]('+link(path, 'packs/ui/reference/Observable.md')+') · '+
              '[Control]('+link(path, 'packs/ui/reference/Control.md')+') · '+
              '[Theme]('+link(path, 'packs/ui/reference/Theme.md')+')']
        if relative in ('FormUI/flutter-ui', 'FormUI/fluent-ui'):
            image=relative.split('/')[-1]+'-preview.png'
            text+=['', '![内置主题预览]('+image+')']
        put(path, '\n'.join(text))
    for name in ('ocean_killer','yours_is_mine'):
        path='tutorials/'+name+'.md'
        text=(SITE/'docs'/path).read_text(encoding='utf-8-sig')
        put(path,text.replace('#entityhurt','#entityHurt'))
    STAGE.mkdir(parents=True,exist_ok=True)
    (STAGE/'missing-translations.json').write_text(json.dumps(sorted(MISSING),ensure_ascii=False,indent=2),encoding='utf-8')
    if MISSING:
        raise ValueError('Missing Chinese translations: %d; see missing-translations.json' % len(MISSING))
    for relative,text in list(PAGES.items()):
        if relative.endswith('.md'):
            PAGES[relative]=references.prose(text,relative)
    if references.UNRESOLVED:
        (STAGE/'unresolved-types.json').write_text(json.dumps(sorted(references.UNRESOLVED),ensure_ascii=False,indent=2),encoding='utf-8')
        raise ValueError('Unresolved type references: %d; see unresolved-types.json' % len(references.UNRESOLVED))
    for relative,text in list(PAGES.items()):
        data=text.encode('utf-8')
        path=STAGE/'docs'/relative
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(data)
    # Inventory uses local source members only; official gaps are kept separate.
    manifest={'source_root':str(SOURCE),'target_site':str(SITE),'classes':[], 'changes':[], 'deletions':[],
              'guides':len(GUIDES), 'example_blocks':len(PYTHON_EXAMPLES)}
    for cls in CLASSES:
        manifest['classes'].append({'name':cls['name'],'group':cls['group'],'source':cls['path'].relative_to(SOURCE).as_posix(),
            'source_sha256':digest(cls['path'].read_bytes()),'doc':'docs/'+cls['url'],
            'members':sorted(name for name in cls['members'] if not name.startswith('_')),'fields':sorted(cls['fields'])})
    for relative in sorted(PAGES):
        name='docs/'+relative; target=SITE/name
        manifest['changes'].append({'path':name,'before_sha256':digest(target.read_bytes()) if target.is_file() else None,
                                    'after_sha256':digest((STAGE/name).read_bytes())})
    # Retire only obsolete generated native payload pages. Their exact hashes
    # are reviewed with the writes, and apply preserves a recoverable backup.
    for side in ('client', 'server'):
        folder = SITE/'docs/packs'/side/'reference'
        marker = 'core_behavior/ModSAPI/modules/'+side+'/NativeEventTypes.py'
        for page in sorted(folder.glob('*.md')):
            relative = page.relative_to(SITE/'docs').as_posix()
            if relative not in PAGES and marker in page.read_text('utf-8-sig'):
                name = 'docs/'+relative
                manifest['deletions'].append({'path':name, 'before_sha256':digest(page.read_bytes())})
                stale = (STAGE/name).resolve()
                if not stale.is_relative_to(STAGE.resolve()):raise ValueError('Path escaped staging')
                if stale.is_file():stale.unlink()
    # Include the portable generator and hand-authored guide module for future synchronization.
    for filename in ('generate.py','content.py','ui_content.py','localization.py','references.py','translations.zh-CN.json','ui-translations.zh-CN.json','build.cjs','api-tables.css'):
        destination=STAGE/'scripts/modsapi-docs'/filename
        destination.parent.mkdir(parents=True,exist_ok=True)
        destination.write_bytes((Path(__file__).parent/filename).read_bytes())
        target=SITE/'scripts/modsapi-docs'/filename
        manifest['changes'].append({'path':'scripts/modsapi-docs/'+filename,
                                   'before_sha256':digest(target.read_bytes()) if target.is_file() else None,
                                   'after_sha256':digest(destination.read_bytes())})
    readme='''# ModSAPI 文档同步\n\n需要 Python 3.10 或更新版本。同步器读取维护包的源码与声明，不执行游戏模块。\n\n```powershell\npython scripts/modsapi-docs/generate.py --source-root "<ModSAPI项目目录>" --site-root "." --stage-root "<临时输出目录>"\npython scripts/modsapi-docs/generate.py --source-root "<ModSAPI项目目录>" --site-root "." --stage-root "<临时输出目录>" --apply\nnpm run build\n```\n\n先生成，再检查临时目录中的 manifest.json 和页面，最后 --apply。应用会核对目标文件原哈希，遇到生成后被修改的文件会停止；修改前的文件保存在临时目录 original/。\n\ncontent.py 保存人工编写的场景指南、核心示例与能力限制。translations.zh-CN.json 与 localization.py 保存中文译文及重复事件契约的翻译规则；缺少译文时停止生成。references.py 解析嵌套类型和正文引用；无法解析的类型会阻止生成。源码的英文注释不受文档语言影响。自动参考页的签名来自当前实现；声明提供类型线索，不能代替原生行为验证。修改这些参考页时应同步更新同步器或模板，否则下次生成会覆盖手写变更。\n'''
    filename='scripts/modsapi-docs/README.md'
    (STAGE/filename).write_text(readme,encoding='utf-8')
    target=SITE/filename
    manifest['changes'].append({'path':filename,'before_sha256':digest(target.read_bytes()) if target.is_file() else None,
                                'after_sha256':digest((STAGE/filename).read_bytes())})
    package=json.loads((SITE/'package.json').read_text(encoding='utf-8'))
    package['scripts']['build']='node scripts/modsapi-docs/build.cjs'
    additions={'package.json':json.dumps(package,ensure_ascii=False,indent=2)+'\n'}
    css=(SITE/'src/css/custom.css').read_text(encoding='utf-8')
    css=re.sub(r'/\* ModSAPI generated API table layout\. \*/[\s\S]*?/\* End ModSAPI generated API table layout\. \*/\s*','',css)
    additions['src/css/custom.css']=css.rstrip()+'\n\n'+Path(__file__).with_name('api-tables.css').read_text(encoding='utf-8')
    ignored=(SITE/'.gitignore').read_text(encoding='utf-8')
    if '/.docusaurus-build/' not in ignored:
        ignored=ignored.rstrip()+'\n/.docusaurus-build/\n'
    additions['.gitignore']=ignored
    config=(SITE/'docusaurus.config.ts').read_text(encoding='utf-8')
    config=site_navigation(config)
    additions['docusaurus.config.ts']=config
    for relative, text in additions.items():
        target=SITE/relative; destination=STAGE/relative
        destination.parent.mkdir(parents=True,exist_ok=True)
        destination.write_text(text,encoding='utf-8')
        manifest['changes'].append({'path':relative,'before_sha256':digest(target.read_bytes()),
                                    'after_sha256':digest(destination.read_bytes())})
    (STAGE/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    (STAGE/'examples.json').write_text(json.dumps(PYTHON_EXAMPLES,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Generated %d reference types, %d pages, %d example blocks.' % (len(CLASSES),len(PAGES),len(PYTHON_EXAMPLES)))


def function_pages():
    entries=[]
    for path in sorted((BASE/'architect').rglob('*.py')):
        nodes=[node for node in parse(path).body if isinstance(node,ast.FunctionDef) and not node.name.startswith('_')]
        if not nodes:continue
        relative=path.relative_to(BASE).with_suffix('').as_posix()
        url='packs/architecture/functions/'+relative.replace('/','-')+'.md'
        out=['---','title: '+relative.replace('/','.'),'---','','# '+relative.replace('/','.'),'',
             '这是核心包的架构辅助模块，不是模板 beta 入口的直接导出。下方示例中的 module 是此模块对象；仅在核心包开发或已经取得模块对象时使用。','']
        for node in nodes:
            sig,params,returns=signature(node)
            out+=['## '+node.name+' {#'+node.name+'}','', '```python',node.name+sig,'```','',clean(chinese(ast.get_docstring(node) or '执行 '+node.name+' 架构辅助操作。')),'']
            if params:
                out+=['| 参数 | 类型线索 | 默认值 |','| --- | --- | --- |']
                out+=['| '+code(name)+' | '+references.annotation(typ,url)+' | '+code(default)+' |' for name,typ,default in params]
                out+=['']
            if returns:out+=['返回类型：'+references.annotation(returns,url)+'.','']
            errors=exception_rows(node)
            if errors:out+=['显式异常：'+', '.join(code(name)+': '+code(message) for name,message in errors),'']
            needed=[arg.arg for arg in node.args.args][:len(node.args.args)-len(node.args.defaults)]
            if not empty(node):out+=[fence('def use_function(module'+(', '+', '.join(needed) if needed else '')+'):\n    return module.'+node.name+'('+', '.join(needed)+')')]
        put(url,'\n'.join(out))
        entries.append((relative,url))
    if entries:
        current='packs/architecture/intro.md'
        put(current,PAGES[current]+'\n\n## 模块函数\n\n'+'\n'.join('- ['+name.replace('/','.')+']('+link(current,url)+')' for name,url in entries))
        put('packs/architecture/functions/_category_.json',json.dumps({'label':'模块函数','position':5},ensure_ascii=False))


def alias_rows():
    rows=[]
    for path in sorted(BASE.rglob('*.pyi')):
        for item in parse(path).body:
            if isinstance(item,ast.Assign) and isinstance(item.value,(ast.BinOp,ast.Subscript)):
                for target in item.targets:
                    if isinstance(target,ast.Name) and not target.id.startswith('_'):
                        rows.append((target.id,ast.unparse(item.value),path.relative_to(SOURCE).as_posix()))
            elif (isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name)
                  and ast.unparse(item.annotation) == 'TypeAlias' and item.value is not None
                  and not item.target.id.startswith('_')):
                rows.append((item.target.id, ast.unparse(item.value), path.relative_to(SOURCE).as_posix()))
    return rows


def type_aliases():
    rows=alias_rows()
    out=['---','title: 类型别名','---','','# 类型别名','', '类型别名只用于静态补全，不是构造函数。VectorLike 表示接口接受的几种坐标输入；仍要满足各方法的有限值和字段校验。','', '| 名称 | 类型 | 声明来源 |','| --- | --- | --- |']
    out=out[:-2]
    for name,value,path in rows:
        out+=['## '+name+' {#'+name.lower()+'}','','| 名称 | 类型 | 声明来源 |','| --- | --- | --- |',
              '| '+code(name)+' | '+references.annotation(value,'packs/common/type-aliases.md')+' | '+code(path)+' |','']
    put('packs/common/type-aliases.md','\n'.join(out))


def apply():
    manifest=json.loads((STAGE/'manifest.json').read_text(encoding='utf-8'))
    assert Path(manifest['target_site']).resolve()==SITE.resolve()
    for change in manifest['changes']:
        destination=(SITE/change['path']).resolve()
        if not destination.is_relative_to(SITE.resolve()):raise ValueError('Path escaped site')
        current=digest(destination.read_bytes()) if destination.is_file() else None
        if current not in (change['before_sha256'],change['after_sha256']):
            raise ValueError('File changed after generation: '+change['path'])
    for change in manifest.get('deletions', []):
        destination=(SITE/change['path']).resolve()
        if not destination.is_relative_to(SITE.resolve()):raise ValueError('Path escaped site')
        if destination.is_file() and digest(destination.read_bytes()) != change['before_sha256']:
            raise ValueError('Obsolete page changed after generation: '+change['path'])
    for change in manifest['changes']:
        source=STAGE/change['path'];destination=SITE/change['path']
        assert digest(source.read_bytes())==change['after_sha256']
        if destination.is_file() and digest(destination.read_bytes())==change['after_sha256']:continue
        if destination.is_file():
            backup=STAGE/'original'/change['path'];backup.parent.mkdir(parents=True,exist_ok=True)
            if not backup.exists():backup.write_bytes(destination.read_bytes())
        destination.parent.mkdir(parents=True,exist_ok=True)
        destination.write_bytes(source.read_bytes())
    for change in manifest.get('deletions', []):
        destination=(SITE/change['path']).resolve()
        if destination.is_file():
            backup=STAGE/'retired'/change['path']
            backup.parent.mkdir(parents=True,exist_ok=True)
            backup.write_bytes(destination.read_bytes())
            destination.unlink()
    print('Applied %d reviewed documentation files.' % len(manifest['changes']))
    print('Retired %d obsolete generated pages with backups.' % len(manifest.get('deletions', [])))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,default=SOURCE)
    parser.add_argument('--site-root',type=Path,default=SITE)
    parser.add_argument('--stage-root',type=Path,default=STAGE)
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    SOURCE=args.source_root.resolve();SITE=args.site_root.resolve();STAGE=args.stage_root.resolve()
    BASE=SOURCE/'core_behavior/ModSAPI'
    apply() if args.apply else generate()
