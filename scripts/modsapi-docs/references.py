"""Resolve local API, nested annotation, and prose references for Markdown."""
import os
import re
from pathlib import Path

CLASSES = {}
EVENTS = {}
UNRESOLVED = set()
TYPE_ALIASES = set()
TYPE_PAGE = 'packs/common/type-system.md'
BUILTINS = {
    'str':'字符串；Python 2 运行时还须留意字节串与 Unicode 文本的区别。',
    'unicode':'Python 2 的 Unicode 文本。',
    'int':'整数；具体范围由所属接口校验。',
    'long':'Python 2 的长整数。',
    'float':'浮点数；位置、角度等接口通常要求有限值。',
    'bool':'布尔值 True 或 False；不应以整数代替严格布尔参数。',
    'None':'无结果或缺失值；其具体含义由字段约定确定。',
    'list':'有序、可修改的列表；方括号中的类型描述元素。',
    'tuple':'元组；多个类型按位置对应，省略号表示可变长度。',
    'dict':'键值字典；两个类型参数依次描述键和值。',
    'set':'不重复元素的集合。',
    'Any':'静态声明未限制具体类型；仍须满足接口的运行时约束。',
    'Optional':'允许给定类型或 None，例如 Optional[Entity]。',
    'Union':'多个允许类型之一；竖线连接的类型具有相同含义。',
    'Literal':'仅允许所列出的字面量值；其中的字符串是值，不是类型名。',
    'Callable':'可调用对象；Callable[[参数类型], 返回类型] 描述回调签名。',
    'FunctionType':'Python 函数对象；可接受的回调签名见所属事件或方法。',
    'GeneratorType':'Python 生成器对象，逐次产生任务步骤或值。',
    'Iterator':'迭代器，按需返回指定类型的元素。',
    'Iterable':'可迭代对象，可用于依次读取元素。',
    'Sequence':'序列，提供有序元素访问。',
    'Mapping':'键值映射；是否可修改取决于实际对象。',
    'object':'通用 Python 对象，不能据此推断其具有特定业务成员。',
    'type':'类对象，用于传递类型本身而不是实例。',
    'Generic':'泛型声明基类，其类型参数在具体使用位置确定。',
    'Final':'不可重新赋值的静态声明；具体值仍由源码和所属接口决定。',
    'BaseUIControl':'网易原生界面控件。仅用于明确需要调用原生接口的自定义控件回调。',
    'TypedDict':'描述字典字段的静态类型；运行时通常传普通字典。',
    'NamedTuple':'带命名字段的元组声明。',
    'TypeVar':'泛型类型变量；T、_TEvent 和 _TSemantic 表示由具体用法确定的类型。',
    'Exception':'Python 异常基类，可通过异常对象取得错误详情。',
    'TypeError':'参数或值的类型不符合要求。',
    'ValueError':'参数类型可接受，但值、范围或组合不合法。',
    'RuntimeError':'当前运行状态不允许操作，例如在同步分发结束后写入事件输出。',
    'AttributeError':'成员不存在或不允许写入。',
    'KeyError':'指定键或名称不存在。',
    'IndexError':'序列或槽位索引越界。',
    'NotImplementedError':'当前实现未提供所请求的功能。',
    'StopIteration':'迭代器已没有后续元素。',
    'ZeroDivisionError':'除数为零。',
    'ScreenNode':'网易原生屏幕基类。通过 client.screen.getScreenNode() 获取；其原生成员不属于本库封装接口。',
    'BlockPaletteComponent':'网易原生方块调色板组件；生命周期和原生数据约定由开发包规定。',
    'Matrix':'网易 mod.common.utils.mcmath 提供的矩阵类型，用于架构层坐标变换。由底层数学函数返回，不是模板入口导出的类。',
    'NativeVector3':'网易 mod.common.utils.mcmath 提供的三维向量类型，供底层矩阵运算使用；与本库公开的 Vector3 包装类不同。',
    '_Query':'架构层查询工厂返回的内部查询对象。此名称来自类型声明，不是模板导出的公共类；应通过所属查询函数获取。',
}
ALIASES = {'Dict':'dict','List':'list','Tuple':'tuple','Set':'set', 'any':'Any',
           'T':'TypeVar','_T':'TypeVar','_U':'TypeVar','_UiEventT':'TypeVar','_TEvent':'TypeVar','_TSemantic':'TypeVar','boolean':'bool',
           'string':'str','number':'float'}


def relative(current, target, anchor=''):
    return Path(os.path.relpath(target, Path(current).parent)).as_posix()+('#'+anchor if anchor else '')


def configure(classes, events):
    CLASSES.clear(); EVENTS.clear(); UNRESOLVED.clear()
    for cls in classes:
        CLASSES.setdefault(cls['name'], []).append(cls)
    for event in events:
        EVENTS.setdefault(event['name'], []).append(event)


def choose(name, current):
    candidates = CLASSES.get(name, [])
    group = current.split('/')[1] if current.startswith('packs/') else ''
    return next((c for c in candidates if c['group']==group),
                next((c for c in candidates if c['group']=='common'), candidates[0] if candidates else None))


def member_owner(cls, member, seen=None):
    seen=set() if seen is None else seen
    if cls['url'] in seen:return None
    seen.add(cls['url'])
    if member in cls['members'] or member in cls['fields']:return cls
    for name in cls['bases']:
        base=choose(name,cls['url'])
        if base:
            owner=member_owner(base,member,seen)
            if owner:return owner
    return None


def resolve(token, current):
    # Qualified Python annotations use implementation-module aliases.
    parts = token.split('.')
    scopes = {'client':'Client','world':'World','system':'System'}
    if parts[0] in scopes and len(parts)>1:
        owner = choose(scopes[parts[0]],current)
        if parts[1]=='scriptBridge' and len(parts)>2:
            owner=choose('ScriptBridge',current)
            if len(parts)>=4 and parts[2]=='afterEvents':
                owner=choose('ScriptBridgeAfterEvents',current)
        if parts[1]=='ui' and len(parts)>2:
            owner=choose('UiService',current)
        if len(parts)>=3 and parts[1] in ('beforeEvents','afterEvents'):
            containers = {'client':'Client','world':'World','system':'System'}
            owner=choose(containers[parts[0]]+parts[1][0].upper()+parts[1][1:],current)
        if owner and parts[-1] in owner['members']:
            return relative(current,owner['url'],parts[-1])
    if parts[-1]=='Vector3' and current=='packs/architecture/functions/architect-math-mat4.md':
        return relative(current, TYPE_PAGE, 'nativevector3')
    cls = choose(parts[-1], current)
    if cls:
        return relative(current, cls['url'])
    if len(parts)>1:
        cls = choose(parts[-2], current)
        if cls:
            member = parts[-1]
            cls=member_owner(cls,member)
        if cls:
            if member in cls['members']:
                return relative(current, cls['url'], 'constructor' if member=='__init__' else member)
            if member in cls['fields']:
                return relative(current, cls['url'], '字段与常量')
    name = ALIASES.get(parts[-1], parts[-1])
    if name in BUILTINS:
        return relative(current, TYPE_PAGE, name.lower())
    if name == 'VectorLike':
        return relative(current, 'packs/common/type-aliases.md', 'vectorlike')
    if token in EVENTS:
        candidates = EVENTS[token]
        side = 'client' if '/client/' in current else 'server'
        event = next((e for e in candidates if e['side']==side), candidates[0])
        target = 'packs/client/events.md' if event['side']=='client' else 'packs/server/native-events.md'
        return relative(current, target, token.lower())
    if name in TYPE_ALIASES:
        return relative(current, 'packs/common/type-aliases.md', name.lower())
    return None


TOKEN = re.compile(r'[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*')


def annotation(value, current):
    """Link every component, preserving literals and punctuation in type syntax."""
    literals = re.split(r'((?:typing\.)?Literal\[[^\]]*\])', value)
    if len(literals)>1:
        return ''.join(
            '['+part.split('[',1)[0]+']('+resolve('Literal',current)+')'+part[part.index('['):].replace('|','\\|')
            if re.fullmatch(r'(?:typing\.)?Literal\[[^\]]*\]',part) else annotation(part,current)
            for part in literals)
    def text_part(value):
        def replace(match):
            name = match[0]; target = resolve(name, current)
            if target:
                return '['+name+']('+target+')'
            UNRESOLVED.add((current, name))
            return '`'+name+'`'
        return TOKEN.sub(replace, value).replace('|', '\\|')
    # Quoted forward references can be type expressions; Literal values cannot.
    parts = re.split(r'("[^"\n]*"|\x27[^\x27\n]*\x27)', value)
    result=[]
    for part in parts:
        if part.startswith(('"', "'")):
            inner=part[1:-1]
            if resolve(inner,current):result.append(text_part(inner))
            else:result.append('`'+part.replace('|','\\|')+'`')
        else:result.append(text_part(part))
    return ''.join(result)


def prose(text, current):
    """Add references without touching fences, existing links, HTML or URLs."""
    def words(value):
        return TOKEN.sub(lambda m: '['+m[0]+']('+resolve(m[0],current)+')'
                         if resolve(m[0],current) else m[0], value)
    # This pass operates on authored/generated Markdown, never on Python code.
    fence=False; result=[]
    for line in text.splitlines():
        if line.startswith('```'):
            fence=not fence;result.append(line);continue
        if fence or line.startswith(('---','title:','sidebar_', '#')):
            result.append(line);continue
        fragments = re.split(r'(!?\[[^\]\n]*\]\([^\n)]*\)|<[^>]*>|`[^`]*`|https?://\S+)',line)
        for i,fragment in enumerate(fragments):
            if fragment.startswith('`'):
                token=fragment[1:-1]
                target=resolve(token,current) if TOKEN.fullmatch(token) else None
                if target:
                    fragments[i]='['+token+']('+target+')'
                elif re.match(r'^(?:Optional|Union|Callable|Literal|list|tuple|dict|List|Tuple|Dict)\[',token):
                    fragments[i]=annotation(token,current)
            elif not (fragment.startswith(('[','![','<','http://','https://'))):
                fragments[i]=words(fragment)
        result.append(''.join(fragments))
    return '\n'.join(result)


def type_page():
    lines=['---','title: 类型标记与原生类型','---','','# 类型标记与原生类型','',
           '类型名保留代码中的原文，说明统一使用中文。方括号表示类型参数，竖线表示多个允许类型之一。类型链接不代表该类型可以从模板直接导入，获取方式以各类型参考页为准。','']
    for name, description in BUILTINS.items():
        lines+=['## '+name+' {#'+name.lower()+'}','',''+description,'']
    return '\n'.join(lines)
