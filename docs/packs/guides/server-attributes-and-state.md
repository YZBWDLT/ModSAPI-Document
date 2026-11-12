---
title: 服务端属性与实体状态
---

# 服务端属性与实体状态

本页介绍服务端 [Entity](../server/apis/entity.md) 的属性组件与网易扩展。客户端只读状态见[客户端实体、属性与玩家状态](client-entity-state.md)。修改世界状态应由服务端执行，客户端输入限制不能代替服务端校验。

## 修改当前属性，保留默认值

```python
def heal(entity, amount):
    health = entity.getComponent("health")
    if health is None:
        return False
    value = min(health.effectiveMax, health.currentValue + amount)
    return health.setCurrentValue(value)
```

[EntityAttributeComponent.setCurrentValue](../server/reference/EntityAttributeComponent.md#setCurrentValue) 使用网易属性枚举并明确保留原生默认值。参数必须是有限数值，布尔值和字符串会被拒绝。超出当前上下限时，在写入前抛出 [ArgumentOutOfBoundsError](../common/reference/ArgumentOutOfBoundsError.md)，不会把原生接口的自动截断当成准确设置成功。

合法请求被原生接口拒绝时返回 False；原生异常、畸形返回值会抛出 [NativeOperationError](../common/reference/NativeOperationError.md)。错误可通过 `operation`、`code`、`cause` 定位。这里没有跨模组事务，原生拒绝不代表引擎一定回滚了所有内部状态。

原有的 `entity.health = value` 使用同一条属性写入路径，保留默认生命值；因为属性赋值没有布尔返回结果，原生拒绝会报告错误。常规代码优先使用组件方法，以便显式处理 False。

## 当前值、默认值和上下限

| 成员 | 当前实现 |
| --- | --- |
| currentValue | 重新读取原生当前值，零是合法结果 |
| defaultValue | 读取实体属性 NBT 中的 Base，不把当前值伪装成默认值 |
| effectiveMax | 读取原生运行时最大值，不使用 NBT Max 代替；保留合法的正无穷上限 |
| effectiveMin | 读取属性 NBT 的 Min；没有独立的有效最小值查询接口，额外最小值修饰因素尚未完成等价核验 |

这些值来自 [EntityAttributeComponent](../server/reference/EntityAttributeComponent.md)。最大值查询不需要序列化整份实体 NBT。默认值和最小值需要读取原生 NBT，因此不适合无条件地按帧批量读取；NBT 缺失或格式不合法时明确报告读取错误，不回填一个看似正常的零。

```python
def configure_health(entity):
    health = entity.getComponent("health")
    if health is None:
        return False
    if not health.setMaxValue(40):
        return False
    return health.setCurrentValue(40)
```

[setMaxValue](../server/reference/EntityAttributeComponent.md#setMaxValue) 是网易扩展，用于设置有限、非负且不小于最小值的最大值。它不会自动突破原版引擎范围，也不会修改当前支持属性的默认值。设置失败返回 False；库不会为了完成一次当前值写入而偷偷扩大上限。

`resetToDefaultValue()` 和 `resetToMaxValue()` 使用原生重置操作；原生失败会抛出错误。对于从未显式设置过的正无穷最大值，网易重置到最大值的操作会恢复默认值，这与直接写入无穷大不同。`resetToMinValue()` 在读取一次最小值后按保留默认值的方式写入；负无穷最小值无法这样重置，会抛出 [UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)。

## 组件失效与实体身份

组件的 `isValid` 会检查所属实体和原生属性是否仍存在。已经移除的实体抛出 [InvalidEntityError](../common/reference/InvalidEntityError.md)，其 `id` 和 [type](../common/type-system.md#type) 来自保留的身份信息，不会在异常属性读取时再访问引擎。没有捕获过实体类型时，[type](../common/type-system.md#type) 为空字符串。属性本身消失时使用 [InvalidClientObjectError](../common/reference/InvalidClientObjectError.md) 报告该组件不可继续使用；该现有扩展错误同样覆盖实体对象失效。

同一实体标识的服务端包装对象保持原有相等比较，并使用一致的哈希值。将重复包装对象放入集合或作为字典键时，不会因为对象内存地址不同而破坏去重。身份字段仍不应被解析为业务信息。

## 读取生物和载具状态

```python
def inspect_entity(entity):
    return {
        "baby": entity.isBaby,
        "tamed": entity.isTamed,
        "sitting": entity.isSitting,
    }
```

| 属性 | 原生含义与限制 |
| --- | --- |
| isAngry | 是否处于激怒状态；是否支持取决于实体定义，铁傀儡有原生例外 |
| isBaby | 是否为幼年实体 |
| isPregnant | 怀孕状态，原生文档主要用于海龟 |
| isSheared | 剪毛状态，原生文档主要用于羊 |
| isSitting | 坐下状态 |
| isTamed | 是否已驯服 |
| isOutOfControl | 失控状态，原生文档主要用于船 |
| isIllagerCaptain | 是否为袭击队长，取决于生物定义 |
| isChested | 支持的羊驼、驴、骡是否背负箱子 |
| isSaddled | 是否装备鞍 |

上述属性只读，原生返回 [None](../common/type-system.md#none) 等失败结果时抛出错误，不转换成 False。读写操作仍受实体种类、定义和当前原生状态限制，不能认为每一种实体都支持表中的所有字段。

修改使用明确的方法：`setAngry(...)`、`growUp()`、`setSheared(...)`、`setSitting(...)`、`setOutOfControl(...)`、`setChested(...)` 和 `promoteToIllagerCaptain()`。布尔参数必须是真正的布尔值；原生拒绝会报告对应操作错误。`growUp()` 依赖定义中的成长事件；熊猫坐姿采用其他原生逻辑，不能通过通用坐下操作保证效果。

```python
def make_angry(entity, target):
    entity.setAngry(True, target)

def clear_anger(entity):
    entity.setAngry(False)
```

启用怒气时必须传入有效的服务端 [Entity](../server/apis/entity.md) 或 [Player](../server/apis/player.md) 目标，并满足原生感知范围要求；关闭怒气时省略目标。服务端的世界事件和系统事件可能有不同的生命周期所属对象，它们的对象地址不是服务器会话标识，不会据此拒绝仍然有效的目标。

## 变种、颜色、交易与携带强度

`variant`、`markVariant` 和 `tradeLevel` 返回对应的非负整数；原生失败哨兵不是正常值。通过 `setVariant(...)`、`setMarkVariant(...)`、`setTradeLevel(...)` 修改，具体可用值由实体定义和 SDK 决定，不按所有生物统一套用某个变种枚举。

```python
from ModSAPI.server.beta import DyeColor

def recolor(entity):
    entity.setColor(DyeColor.Lime)
    print(entity.color)
```

颜色使用标准 [DyeColor](../common/reference/DyeColor.md) 字符串。网易的浅绿枚举会映射到 Lime，银色映射到 Silver；业务代码不需要硬编码颜色整数。原生颜色操作主要针对羊和热带鱼，不能据此给所有实体重新染色。

`strength` 与 `maxStrength` 使用原生羊驼携带强度，范围为一到五。`setStrength(...)` 还会检查当前最大值，避免原生自动截断。`setMaxStrength(...)` 修改原生上限；引擎重新加载相关组件时，可能恢复实体 JSON 配置中的值。

## 属主直接使用对象

```python
def assign_owner(entity, owner):
    entity.setOwner(owner)

def clear_owner(entity):
    entity.setOwner(None)

def read_owner(entity):
    owner = entity.getOwner()
    return None if owner is None else owner.typeId
```

[getOwner](../server/apis/entity.md#getOwner) 使用原生实体属主查询，覆盖驯服主人、掉落物丢弃者和弹射物发射者等关系；玩家会包装为 [Player](../server/apis/player.md)。没有属主或属主不再加载时返回 [None](../common/type-system.md#none)。`setOwner()` 接受服务端包装对象或 [None](../common/type-system.md#none)，拒绝直接传入标识符字符串。客户端同名读取仅使用其可用的驯服关系能力，范围见客户端教程。

## 死亡动画与位置例外

`deathTimeTicks` 读取原生死亡动画持续时间，每秒二十个逻辑刻；存活时为零，原生失败值会转换为错误。此查询允许仍被引擎保留的死亡实体，不会为了读取动画时间而让实体重新变为有效。凋零死亡动画具有原生例外。

服务端和客户端的 `location` 都保留原生脚底坐标约定。睡眠姿态属于原生例外，不额外伪造床朝向或骨骼坐标来修正位置。

## 装备槽位与空结果

[EntityEquippableComponent](../server/reference/EntityEquippableComponent.md) 支持主手、副手、头盔、胸甲、护腿、鞋子六个标准槽位，使用 [EquipmentSlot](../common/reference/EquipmentSlot.md) 中对应的常量。`getEquipment()` 在空槽时返回 [None](../common/type-system.md#none)；`setEquipment(slot, None)` 只清除指定位置，正常的原生拒绝返回 False。

写入可以传入服务端 [ItemStack](../server/apis/itemStack.md) 或事件中的 [EventItemStack](../common/reference/EventItemStack.md) 快照。传给引擎前会复制物品数据，不会把原生数据修改写回调用方的快照。

未知槽位不会落到头盔槽。SAPI 的 Body 槽暂不支持：网易 ArmorSlotType.BODY 表示胸甲，不能把名称相似当成同一个槽位；请求 Body 会抛出 [UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)。组件失效后不能继续使用缓存的物品组件。

本页接口经过离线原生契约和回归测试。资源、具体生物行为、多人同步及平台表现仍待游戏实测；整体待补能力见 [ModSDK 功能映射与待补接口](../modsdk-coverage.md)。