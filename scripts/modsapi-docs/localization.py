"""Chinese documentation prose; runtime docstrings remain in English."""
import json
import re
from pathlib import Path


def normalize(value):
    return re.sub(r'\s+', ' ', value).strip()


TRANSLATIONS = {normalize(k): v for k, v in json.loads(
    Path(__file__).with_name('translations.zh-CN.json').read_text('utf-8')).items()}
TRANSLATIONS.update({normalize(k): v for k, v in json.loads(
    Path(__file__).with_name('ui-translations.zh-CN.json').read_text('utf-8')).items()})
MISSING = set()


def chinese(value):
    """Translate reviewed prose and generated contracts without hiding omissions."""
    text = normalize(value)
    if text in TRANSLATIONS:
        return TRANSLATIONS[text]
    match = re.fullmatch(r'Native catalog signal: (\w+)\. See its payload and catalog prerequisites\.', text)
    if match:
        return '原生事件信号：'+match[1]+'。参数类型及触发前提见对应类型页和原生事件目录。'
    match = re.fullmatch(r'Native (\w+) payload; outputs expire after dispatch\.', text)
    if match:
        return match[1]+' 的事件参数；同步分发结束后不能再写入输出字段。'
    match = re.fullmatch(r'Native (\w+) \((.*)\); (read-only|synchronous output)\. Missing fields return None\.', text)
    if match:
        return ('数据来源为原生字段 `'+match[1]+'`；'+
                ('只读。' if match[3]=='read-only' else '仅可在同步回调内写入。')+
                '字段缺失时返回 None。公开类型及对象包装以本成员的返回类型为准。')
    match = re.fullmatch(r'Validate and write native (\w+) during synchronous dispatch\.', text)
    if match:
        return '在同步分发期间校验并写入原生 '+match[1]+' 输出。'
    match = re.fullmatch(r'Semantic event: (\w+)\. Sources: (.+)\. Supports filtered subscriptions\.', text)
    if match:
        categories = {'input':'按键输入','pointer':'指针交互','axis':'手柄轴输入','state':'玩家状态',
                      'presence':'实体可见性','screen':'界面栈变化','screenClose':'界面关闭',
                      'inventory':'库存变化','physics':'物理接触','area':'兴趣区域',
                      'effect':'效果变化','weather':'天气强度','itemUse':'物品使用',
                      'useOn':'对方块使用物品','block':'方块交互','loot':'战利品生成'}
        return categories[match[1]]+'事件，支持订阅筛选。原生来源：'+match[2]+'。'
    match = re.fullmatch(r'Semantic (\w+) observation\. Native details remain available through nativeEvent; handles are lazy and container values are detached\.', text)
    if match:
        return match[1]+' 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。'
    # Existing Chinese source prose and API identifiers need no translation.
    if re.search(r'[\u4e00-\u9fff]', text) or not re.search(r'[A-Za-z]{2}', text):
        return value
    MISSING.add(value)
    return '【待补充中文译文】'
