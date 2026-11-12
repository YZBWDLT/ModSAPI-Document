"""Chinese guidance for server attributes, identity and native entity state."""

SERVER_STATE_GUIDES = {
    'packs/guides/server-attributes-and-state.md': r'''---
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

组件的 `isValid` 会检查所属实体和原生属性是否仍存在。已经移除的实体抛出 [InvalidEntityError](../common/reference/InvalidEntityError.md)，其 `id` 和 `type` 来自保留的身份信息，不会在异常属性读取时再访问引擎。没有捕获过实体类型时，`type` 为空字符串。属性本身消失时使用 [InvalidClientObjectError](../common/reference/InvalidClientObjectError.md) 报告该组件不可继续使用；该现有扩展错误同样覆盖实体对象失效。

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

上述属性只读，原生返回 None 等失败结果时抛出错误，不转换成 False。读写操作仍受实体种类、定义和当前原生状态限制，不能认为每一种实体都支持表中的所有字段。

修改使用明确的方法：`setAngry(...)`、`growUp()`、`setSheared(...)`、`setSitting(...)`、`setOutOfControl(...)`、`setChested(...)` 和 `promoteToIllagerCaptain()`。布尔参数必须是真正的布尔值；原生拒绝会报告对应操作错误。`growUp()` 依赖定义中的成长事件；熊猫坐姿采用其他原生逻辑，不能通过通用坐下操作保证效果。

```python
def make_angry(entity, target):
    entity.setAngry(True, target)

def clear_anger(entity):
    entity.setAngry(False)
```

启用怒气时必须传入有效的服务端 Entity 或 Player 目标，并满足原生感知范围要求；关闭怒气时省略目标。服务端的世界事件和系统事件可能有不同的生命周期所属对象，它们的对象地址不是服务器会话标识，不会据此拒绝仍然有效的目标。

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

[getOwner](../server/apis/entity.md#getOwner) 使用原生实体属主查询，覆盖驯服主人、掉落物丢弃者和弹射物发射者等关系；玩家会包装为 [Player](../server/apis/player.md)。没有属主或属主不再加载时返回 None。`setOwner()` 接受服务端包装对象或 None，拒绝直接传入标识符字符串。客户端同名读取仅使用其可用的驯服关系能力，范围见客户端教程。

## 死亡动画与位置例外

`deathTimeTicks` 读取原生死亡动画持续时间，每秒二十个逻辑刻；存活时为零，原生失败值会转换为错误。此查询允许仍被引擎保留的死亡实体，不会为了读取动画时间而让实体重新变为有效。凋零死亡动画具有原生例外。

服务端和客户端的 `location` 都保留原生脚底坐标约定。睡眠姿态属于原生例外，不额外伪造床朝向或骨骼坐标来修正位置。

## 装备槽位与空结果

[EntityEquippableComponent](../server/reference/EntityEquippableComponent.md) 支持主手、副手、头盔、胸甲、护腿、鞋子六个标准槽位，使用 EquipmentSlot 中对应的常量。`getEquipment()` 在空槽时返回 None；`setEquipment(slot, None)` 只清除指定位置，正常的原生拒绝返回 False。

写入可以传入服务端 ItemStack 或事件中的 EventItemStack 快照。传给引擎前会复制物品数据，不会把原生数据修改写回调用方的快照。

未知槽位不会落到头盔槽。SAPI 的 Body 槽暂不支持：网易 ArmorSlotType.BODY 表示胸甲，不能把名称相似当成同一个槽位；请求 Body 会抛出 UnsupportedFeatureError。组件失效后不能继续使用缓存的物品组件。

本页接口经过离线原生契约和回归测试。资源、具体生物行为、多人同步及平台表现仍待游戏实测；整体待补能力见 [ModSDK 功能映射与待补接口](../modsdk-coverage.md)。
''',
}

SERVER_STATE_ACQUIRE = {
    'InvalidEntityError': '在服务端操作失效实体时捕获。id 和 type 为已捕获的诊断身份；尚未捕获类型时 type 为空字符串。无需主动构造。',
    'ArgumentOutOfBoundsError': '在参数超出当前原生边界时捕获；它继承 ValueError，可继续使用既有 ValueError 处理逻辑。',
    'EntityAttributeModifier': '通过 EntityAttributeComponent.getModifiers() 或 getModifier() 取得只读快照。无需主动构造；快照不持有实体，也不会自动更新。',
    'AttributeModifierOperation': '从 ModSAPI.server.beta 导入，向属性组件的 addModifier() 或 updateModifier() 传递运算常量。',
    'AttributeModifierOperand': '从 ModSAPI.server.beta 导入，选择修饰原生最小值、最大值或当前值。',
    'AttributeModifierOptions': '添加或更新修饰器时传入字典；可设置 operation 和 operand，默认分别为 Addition 和 Maximum。',
}

SERVER_STATE_NOTES = {
    'EntityAttributeComponent.addModifier': '网易扩展；默认使用 Addition 运算并影响 Maximum。仅增加指定修饰器，重复标识符的处理由引擎决定，不会自动覆盖。实际计算与持久化限制见属性修饰器教程。',
    'EntityAttributeComponent.updateModifier': '网易扩展；更新完整的 amount、operation、operand。省略选项会使用默认值，不表示保留旧字段。原生正常拒绝返回 False。',
    'EntityAttributeComponent.getModifiers': '每次执行一次原生列表查询，返回 EntityAttributeModifier 只读快照。空列表正常返回；缺失字段、未知原生枚举或重复标识符会报告 NativeOperationError，不返回不完整结果。',
    'EntityAttributeComponent.getModifier': '通过一次原生列表查询查找指定修饰器，未找到返回 None。只检查存在性时使用 hasModifier，避免读取整个列表。',
    'EntityAttributeComponent.hasModifier': '使用原生布尔查询检查指定标识符，不读取修饰器列表。False 表示原生报告不存在。',
    'EntityAttributeComponent.removeModifier': '仅移除指定标识符，正常拒绝返回 False；不会重置属性默认值或清除其他修饰器。',
    'EntityAttributeComponent.effectiveMin': '目前读取原生属性 NBT 的 Min；没有单独的原生有效最小值查询接口，额外最小值修饰因素尚未完成等价核验。不要将此字段视为已经证明所有环境因素均与微软运行时一致。',
    'EntityAttributeComponent.setCurrentValue': '先校验有限数值及当前原生最大值、NBT 最小值，再以保留默认值的方式写入。超界抛出 ArgumentOutOfBoundsError，原生正常拒绝返回 False；其他错误保留诊断信息。',
    'Entity.location': '保留 GetFootPos 的原生坐标约定，睡眠姿态有原生例外，不伪造床方向或模型骨骼位置。',
    'ClientEntity.location': '保留 GetFootPos 的原生坐标约定；睡眠姿态例外同样适用。',
    'Entity.deathTimeTicks': '特意允许仍被引擎保留的死亡实体。无效原生结果报告错误，不改变实体存活状态；凋零使用特殊死亡动画。',
    'EntityEquippableComponent.getEquipment': '支持 Mainhand、Offhand、Head、Chest、Legs、Feet 六种 EquipmentSlot 常量。空槽返回 None；SAPI Body 尚无经核验的原生映射，会抛出 UnsupportedFeatureError。',
    'EntityEquippableComponent.setEquipment': '接受服务端 ItemStack、事件 EventItemStack 或 None。参数在原生写入前复制；未知槽位与未支持的 Body 不会被映射到头盔或胸甲。原生正常拒绝返回 False。',
}

SERVER_STATE_GUIDES['packs/guides/attribute-modifiers.md'] = r'''---
title: 属性修饰器
---

# 属性修饰器

修饰器由已有的 [EntityAttributeComponent](../server/reference/EntityAttributeComponent.md) 管理，不需要再创建服务或注册系统。生命、移动速度等已支持的服务端属性组件均继承这一组接口。这些方法属于网易扩展；微软稳定版属性组件尚无同名成员。

## 增加生命上限

```python
from ModSAPI.server.beta import AttributeModifierOperation, AttributeModifierOperand

def add_health_bonus(entity):
    health = entity.getComponent("health")
    if health is None:
        return False
    return health.addModifier("demo:health_bonus", 10, {
        "operation": AttributeModifierOperation.Addition,
        "operand": AttributeModifierOperand.Maximum,
    })
```

传入实体或玩家包装对象即可，不需要接触原生组件或实体标识符。修饰器自己的标识符是业务资源名，建议使用模组命名空间，以免与其他模组冲突。添加默认使用加法和最大值，因此也可以写成 `health.addModifier("demo:health_bonus", 10)`。

修改最大值不等于填满当前生命，也不改变本库中定义默认值的写入规则。若另行设置当前值，需要处理该方法的布尔结果和当前边界；不要把上限加成当成一次治疗。

## 查询、更新和移除

| 方法 | 返回结果 | 适用场景 |
| --- | --- | --- |
| addModifier | 布尔值 | 添加指定标识符的修饰器 |
| updateModifier | 布尔值 | 更新已有修饰器的全部字段 |
| getModifiers | EntityAttributeModifier 列表 | 查看此属性的所有修饰器 |
| getModifier | EntityAttributeModifier 或 None | 读取指定修饰器的完整快照 |
| hasModifier | 布尔值 | 只检查是否存在，无需读取列表 |
| removeModifier | 布尔值 | 只移除自己的指定修饰器 |

```python
def inspect_bonus(health):
    modifier = health.getModifier("demo:health_bonus")
    if modifier is None:
        return None
    return modifier.amount, modifier.operation, modifier.operand

def update_bonus(health, amount):
    return health.updateModifier("demo:health_bonus", amount)

def remove_bonus(health):
    return health.removeModifier("demo:health_bonus")
```

更新接口的选项是完整的新配置。省略 operation、operand 会恢复为 Addition、Maximum，不会自动沿用旧字段。添加不会自动更新已有修饰器，更新也不承诺在不存在时创建；两者都保留引擎返回的正常拒绝结果。存在检查和之后的写入不是事务，业务逻辑仍应处理 False。

[EntityAttributeModifier](../common/reference/EntityAttributeModifier.md) 包含只读的 id、amount、operation、operand。它不保留原生字典或实体引用。引擎中的修饰器改变后，旧快照保持原值；重新查询才能取得新值。`getModifier()` 只执行一次原生列表查询；只需存在性时使用 `hasModifier()`。

## 运算和操作数

[AttributeModifierOptions](../common/reference/AttributeModifierOptions.md) 使用 [AttributeModifierOperation](../common/reference/AttributeModifierOperation.md) 和 [AttributeModifierOperand](../common/reference/AttributeModifierOperand.md) 中的字符串常量，业务层无需填写网易原生数字枚举。

| 运算 | 原生含义 |
| --- | --- |
| Addition | 加法 |
| MultiplyBase | 基础值乘法 |
| MultiplyTotal | 总值乘法 |
| Cap | 上限运算 |

| 操作数 | 影响对象 |
| --- | --- |
| Minimum | 原生最小值 |
| Maximum | 原生最大值 |
| Current | 原生当前值 |

库仅负责校验和映射，由引擎执行运算，不在 Python 中重算整组修饰器。不同运算的叠加次序、基础值含义和 Cap 的具体行为仍需实机核对，不能直接套用 Java 版属性公式。amount 必须为有限数值，可以为零或负值；不接受布尔值、字符串数字、无穷或 NaN。

## 错误和能力边界

错误类型的参数、拼错的选项和未知常量在查询实体或写入引擎前报告。实体或组件失效时拒绝访问；缺少原生方法时抛出 [UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)，原生异常、异常返回类型或损坏的列表数据抛出 [NativeOperationError](../common/reference/NativeOperationError.md)。正常的原生布尔拒绝仍返回 False，不会伪装为成功。

`effectiveMax` 使用原生最大值查询；`effectiveMin` 目前读取 NBT 的 Min，尚未证明其包含所有最小值修饰因素。设置当前值时的预检查也以这个已知最小值为依据。使用 Minimum 修饰器时不能把该读数当成已验证的微软等价结果，实际边界与写入效果仍待实测。

修饰器跨存档、重载和实体卸载后的保留规则尚未核验。网易 `SaveAttr` 属于自定义属性存储，并不是此处的修饰器保存接口，因此库没有增加会造成误解的“保存修饰器”方法。

本页接口已进行离线原生契约检查；多人、持久化和具体运算结果仍待网易游戏实测。其他待补能力见 [ModSDK 功能映射与待补接口](../modsdk-coverage.md)。
'''
