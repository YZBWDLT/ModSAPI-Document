"""Chinese item component and enchantment catalog guides."""

ITEM_COMPONENT_GUIDES = {
    'packs/guides/item-enchantments-and-durability.md': r'''---
title: 物品附魔、耐久与标签
---

# 物品附魔、耐久与标签

物品组件属于独立的 [ItemStack](../server/apis/itemStack.md)。编辑组件会改变这个物品值；要修改背包，需要再调用容器的 `setItem()`。读取物品、批量读取和写入恢复的完整流程见 [服务端容器与物品数据](server-containers-and-recovery.md)。

## 查询附魔类型

```python
from ModSAPI.server.beta import EnchantmentType, EnchantmentTypes

def get_sharpness_limit():
    value = EnchantmentTypes.get("minecraft:sharpness")
    return None if value is None else value.maxLevel

def describe_enchantment_types():
    return [(value.id, value.maxLevel) for value in EnchantmentTypes.getAll()]
```

[EnchantmentTypes](../server/reference/EnchantmentTypes.md) 使用当前原生注册目录。`get()` 未找到时返回 None；直接构造 [EnchantmentType](../common/reference/EnchantmentType.md) 时，未注册标识会报告 [EnchantmentTypeUnknownIdError](../common/reference/EnchantmentTypeUnknownIdError.md)。id 和 maxLevel 为只读属性，原版标识统一使用 minecraft: 前缀，自定义命名空间继续保留。

每次目录查询读取一次当前原生结果，不使用跨世界的永久缓存。返回的类型值保存查询时的等级上限；注册内容变更后应重新查询，不能把旧值当作持续更新的实时目录。

`Enchantment("sharpness", 2)` 的普通值构造不加载单端 SDK。它的 type 直接提供 EnchantmentType 引用；从原生物品读取的类型引用按需解析 maxLevel，因此仅仅读取或克隆物品不需要额外查询附魔目录。访问未注册旧类型的 maxLevel 仍可能报告错误。

## 添加附魔并写回

```python
from ModSAPI.server.beta import Enchantment, ItemEnchantableComponent

def enchant_first_item(container):
    item = container.getItem(0)
    if item is None:
        return False
    component = item.getComponent(ItemEnchantableComponent.componentId)
    if component is None:
        return False
    component.addEnchantments([
        Enchantment("minecraft:sharpness", 2),
        {"type": "minecraft:unbreaking", "level": 2},
    ])
    container.setItem(0, item)
    return True
```

[ItemEnchantableComponent](../server/reference/ItemEnchantableComponent.md) 使用 slots 中的原生槽位与附魔目录中的 primary_slots、incompatible 校验。公开 slots 名称沿用 [EnchantmentSlot](../common/reference/EnchantmentSlot.md) 风格，部分网易槽位名称是扩展，尚未识别的原生位不会被猜测为其他槽位。

`canAddEnchantment()` 对槽位不适用或附魔冲突返回 False；标识未知、等级非法、SDK 缺少能力或原生返回异常仍然报告错误。它不是吞掉所有错误的检查函数。`addEnchantment()` 对不兼容情况抛出 [EnchantmentTypeNotCompatibleError](../common/reference/EnchantmentTypeNotCompatibleError.md)，超出注册上限时抛出 [EnchantmentLevelOutOfBoundsError](../common/reference/EnchantmentLevelOutOfBoundsError.md)。

批量添加先校验整批内容，并使用同一次原生目录读取；任何一项失败，都不会留下半批修改。同一类型再次添加会替换等级，避免重复条目。实际写回背包仍是独立操作，服从容器的错误与恢复约定。

## 查询结果是独立值

```python
def read_enchantment_summary(item):
    component = item.getComponent("enchantable")
    if component is None:
        return []
    return [(value.type.id, value.level) for value in component.getEnchantments()]

def replace_sharpness_level(item, level):
    component = item.getComponent("enchantable")
    if component is None:
        return False
    value = component.getEnchantment("sharpness")
    if value is None:
        return False
    value.level = level
    component.addEnchantment(value)
    return True
```

[Enchantment](../common/reference/Enchantment.md) 的 type 是包装后的 EnchantmentType，level 是整数。传入组件的值和查询返回的值都会复制；修改查询结果不会直接修改组件，必须再次提交。`getEnchantment()` 未找到已知类型时为 None，`getEnchantments()` 返回列表，`hasEnchantment()` 返回布尔值。

`removeEnchantment()` 接受类型对象或字符串，移除指定类型；`removeAllEnchantments()` 是明确清空全部原生及自定义附魔的操作。

普通读取和克隆会保留原生已有的超上限等级、未知数字编号和自定义附魔通道，不将自定义数据误写入原版附魔数组。只有显式修改才重建相关数据。存在无法识别的旧附魔或未注册旧类型时，无法可靠验证新增兼容性，库会明确拒绝新增，不会猜测其冲突规则。没有可靠数字映射的新增无命名空间附魔，也不会被冒充为已支持的自定义通道。

## 调整耐久

```python
from ModSAPI.server.beta import ItemDurabilityComponent

def repair_item(container, index):
    item = container.getItem(index)
    if item is None:
        return False
    durability = item.getComponent(ItemDurabilityComponent.componentId)
    if durability is None:
        return False
    durability.damage = 0
    container.setItem(index, item)
    return True
```

[ItemDurabilityComponent](../server/reference/ItemDurabilityComponent.md) 中，damage 表示已经损耗的耐久，maxDurability 为该类型当前变种的最大值；网易扩展 remain 表示剩余耐久，等于最大值减去损耗。

公开编辑要求零到最大值之间的整数，拒绝 bool、浮点数、字符串和越界值。输入错误不会先改变另一个关联字段。读取和克隆原生已有的非标准耐久值时保留原值，不强行裁剪；这不代表允许通过公开编辑新增越界值。

当前未提供可靠的 unbreakable、`getDamageChance()` 和 `getDamageChanceRange()` 适配。原生基础信息不足以证明耐久损耗概率、附魔影响及不损坏状态与微软等价，因此不返回猜测结果。

## 变种与物品标签

```python
def is_tool(item):
    return item.hasTag("demo:tool")

def describe_item(item):
    return {"type": item.typeId, "variant": item.auxValue, "tags": item.getTags()}
```

auxValue 是只读的网易原生变种值，优先读取 newAuxValue；不能一律视为耐久。基础定义、耐久上限和标签查询都会使用这一变种，旧 auxValue 字段不会覆盖新字段。

`getTags()` 使用原生 GetItemTags，读取 minecraft:tags 定义并返回列表副本；`hasTag()` 判断指定标签是否存在。异常的原生结果报告 [NativeOperationError](../common/reference/NativeOperationError.md)，保留真实操作名称；不会从无关的基础信息字段推断空标签列表。

## 错误与当前边界

参数错误使用 TypeError、ValueError 或上述具名错误；原生调用失败与返回损坏数据使用 NativeOperationError，缺少能力或无法核验映射时使用 [UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)。不支持的组件不会伪造为可用对象。

本批校验基于网易公开附魔目录和物品接口契约。不同版本的原版附魔、次级槽位规则、附魔实际作用、铁砧和附魔台交互、跨存档与多人同步仍需实机核验，不能据此宣称与微软运行时完全等价。完整差异见 [官方对照与当前支持情况](../compatibility.md)。

接口参考：[微软附魔组件](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemenchantablecomponent?view=minecraft-bedrock-stable)、[微软耐久组件](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemdurabilitycomponent?view=minecraft-bedrock-stable)、[网易物品接口](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md)。
''',
}

ITEM_COMPONENT_ACQUIRE = {
    'ItemComponent': '通过 ItemStack.getComponent 或 getComponents 取得，表示独立物品上的组件；不会直接写入背包。',
    'ItemEnchantableComponent': '通过 item.getComponent("enchantable") 或 ItemEnchantableComponent.componentId 取得；不具备该组件时为 None。',
    'ItemDurabilityComponent': '通过 item.getComponent("durability") 或 ItemDurabilityComponent.componentId 取得；编辑后将物品写回容器。',
    'Enchantment': '从服务端入口创建附魔值，或从附魔组件的查询结果取得副本。type 提供包装后的 EnchantmentType。',
    'EnchantmentType': '从 EnchantmentTypes 查询，或使用注册标识创建。id 与 maxLevel 只读；原生旧物品的类型引用按需解析。',
    'EnchantmentTypes': '从服务端入口导入后直接调用静态 get 或 getAll，无需实例化。',
    'EnchantmentLevelOutOfBoundsError': '捕获附魔值或组件操作中等级为非正值、超出注册上限的错误。',
    'EnchantmentTypeNotCompatibleError': '捕获添加附魔时的槽位或冲突不兼容错误。',
    'EnchantmentTypeUnknownIdError': '捕获未注册附魔标识的查询或修改错误；目录 get 未找到时返回 None。',
}

ITEM_COMPONENT_NOTES = {
    'Enchantment.type': '返回 EnchantmentType 对象，使用 value.type.id 取得规范名称。类型引用的 maxLevel 可能按需查询当前服务端目录。',
    'ItemEnchantableComponent.addEnchantments': '整批使用一次原生目录读取，在全部校验通过后才修改独立物品；实际背包写回另行调用 setItem。',
    'ItemEnchantableComponent.getEnchantment': '返回独立值或 None，修改查询值不会改变组件；需要再次调用添加方法提交。',
    'ItemEnchantableComponent.canAddEnchantment': '槽位或冲突不兼容返回 False；非法等级、未知标识、无法核验旧附魔及原生故障仍会报告错误。',
    'ItemDurabilityComponent.remain': '网易扩展。公开编辑限制在零到最大值；已有原生非标准值只读保留，不在克隆时裁剪。',
    'ItemStack.auxValue': '网易原生变种，优先 newAuxValue；定义与标签查询都使用它，不能将该值一律当作耐久。',
    'ItemStack.getTags': '通过 GetItemTags 查询当前类型及变种的定义标签，返回独立列表；不是从 GetItemBasicInfo 的非标准 tags 字段读取。',
}
