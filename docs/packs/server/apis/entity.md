---
title: "Entity"
sidebar_label: "Entity"
---

# Entity

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Entity.py`；声明补充了静态类型信息。

世界中的实体状态，包括生物、玩家、矿车等对象。

## 获取方式

通过维度查询、事件参数或 `world.getEntity(id)` 获取；查找可能返回 [None](../../common/type-system.md#none)。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [id](#id) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [dimension](#dimension) | 只读属性 |
| [isClimbing](#isClimbing) | 只读属性 |
| [isFalling](#isFalling) | 只读属性 |
| [isInWater](#isInWater) | 只读属性 |
| [isOnGround](#isOnGround) | 只读属性 |
| [isSleeping](#isSleeping) | 只读属性 |
| [isSitting](#isSitting) | 只读属性 |
| [isSneaking](#isSneaking) | 只读属性 |
| [isSprinting](#isSprinting) | 只读属性 |
| [isSwimming](#isSwimming) | 只读属性 |
| [location](#location) | 只读属性 |
| [nameTag](#nameTag) | 可读写属性 |
| [health](#health) | 可读写属性 |
| [scoreboardIdentity](#scoreboardIdentity) | 只读属性 |
| [typeId](#typeId) | 只读属性 |
| [addEffect](#addEffect) | 方法 |
| [addTag](#addTag) | 方法 |
| [applyDamage](#applyDamage) | 方法 |
| [applyImpulse](#applyImpulse) | 方法 |
| [applyKnockback](#applyKnockback) | 方法 |
| [clearDynamicProperties](#clearDynamicProperties) | 方法 |
| [clearVelocity](#clearVelocity) | 方法 |
| [extinguishFire](#extinguishFire) | 方法 |
| [getBlockFromViewDirection](#getBlockFromViewDirection) | 方法 |
| [getComponent](#getComponent) | 方法 |
| [getComponents](#getComponents) | 方法 |
| [getDynamicProperty](#getDynamicProperty) | 方法 |
| [getDynamicPropertyIds](#getDynamicPropertyIds) | 方法 |
| [getDynamicPropertyTotalByteCount](#getDynamicPropertyTotalByteCount) | 方法 |
| [getEffect](#getEffect) | 方法 |
| [getEffects](#getEffects) | 方法 |
| [getEntitiesFromViewDirection](#getEntitiesFromViewDirection) | 方法 |
| [getHeadLocation](#getHeadLocation) | 方法 |
| [getRotation](#getRotation) | 方法 |
| [getTags](#getTags) | 方法 |
| [getVelocity](#getVelocity) | 方法 |
| [getNbt](#getNbt) | 方法 |
| [getProperty](#getProperty) | 方法 |
| [getViewDirection](#getViewDirection) | 方法 |
| [getFamilies](#getFamilies) | 方法 |
| [hasComponent](#hasComponent) | 方法 |
| [hasTag](#hasTag) | 方法 |
| [hasTarget](#hasTarget) | 方法 |
| [getTarget](#getTarget) | 方法 |
| [hasFamily](#hasFamily) | 方法 |
| [kill](#kill) | 方法 |
| [matches](#matches) | 方法 |
| [playAnimation](#playAnimation) | 方法 |
| [remove](#remove) | 方法 |
| [removeEffect](#removeEffect) | 方法 |
| [removeTag](#removeTag) | 方法 |
| [resetProperty](#resetProperty) | 方法 |
| [runCommand](#runCommand) | 方法 |
| [setDynamicProperties](#setDynamicProperties) | 方法 |
| [setDynamicProperty](#setDynamicProperty) | 方法 |
| [setOnFire](#setOnFire) | 方法 |
| [setProperty](#setProperty) | 方法 |
| [setRotation](#setRotation) | 方法 |
| [teleport](#teleport) | 方法 |
| [triggerEvent](#triggerEvent) | 方法 |
| [tryTeleport](#tryTeleport) | 方法 |
| [asPlayer](#asPlayer) | 方法 |
| [isAngry](#isAngry) | 只读属性 |
| [isBaby](#isBaby) | 只读属性 |
| [isPregnant](#isPregnant) | 只读属性 |
| [isSheared](#isSheared) | 只读属性 |
| [isTamed](#isTamed) | 只读属性 |
| [isOutOfControl](#isOutOfControl) | 只读属性 |
| [isIllagerCaptain](#isIllagerCaptain) | 只读属性 |
| [isChested](#isChested) | 只读属性 |
| [isSaddled](#isSaddled) | 只读属性 |
| [variant](#variant) | 只读属性 |
| [markVariant](#markVariant) | 只读属性 |
| [tradeLevel](#tradeLevel) | 只读属性 |
| [strength](#strength) | 只读属性 |
| [maxStrength](#maxStrength) | 只读属性 |
| [deathTimeTicks](#deathTimeTicks) | 只读属性 |
| [color](#color) | 只读属性 |
| [setAngry](#setAngry) | 方法 |
| [growUp](#growUp) | 方法 |
| [setSheared](#setSheared) | 方法 |
| [setSitting](#setSitting) | 方法 |
| [setOutOfControl](#setOutOfControl) | 方法 |
| [setChested](#setChested) | 方法 |
| [promoteToIllagerCaptain](#promoteToIllagerCaptain) | 方法 |
| [setVariant](#setVariant) | 方法 |
| [setMarkVariant](#setMarkVariant) | 方法 |
| [setTradeLevel](#setTradeLevel) | 方法 |
| [setStrength](#setStrength) | 方法 |
| [setMaxStrength](#setMaxStrength) | 方法 |
| [setColor](#setColor) | 方法 |
| [getOwner](#getOwner) | 方法 |
| [setOwner](#setOwner) | 方法 |

## 构造器 {#constructor}

```python
Entity(entityId)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` | 实体运行 ID；跨回调使用前重新确认实体有效性。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## id {#id}

```python
id: str
```

实体的唯一标识。不要解析或推断标识的内部结构；[Entity.isValid](entity.md#isValid) 为 False 时仍可读取。跨存档重载时是否保持一致取决于原生引擎，不应以包装类代替持久身份校验。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## isValid {#isValid}

```python
isValid: bool
```

实体是否有效；从世界移除后可能失效。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'CreateGame'` |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'IsEntityAlive'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsEntityAlive`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## dimension {#dimension}

```python
dimension: Dimension
```

实体当前所在的维度。

**访问：** 只读。

**返回类型：** [Dimension](dimension.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** [Dimension](dimension.md), `GetEntityDimensionId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.dimension
```

## isClimbing {#isClimbing}

```python
isClimbing: bool
```

实体是否接触可攀爬的方块，例如靠近梯子的玩家或靠近石墙的蜘蛛。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `EvalMolangExpression`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isClimbing
```

## isFalling {#isFalling}

```python
isFalling: bool
```

实体是否具有大于零的下落距离；滑翔时以大于一为条件。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEntityFallDistance`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isFalling
```

## isInWater {#isInWater}

```python
isInWater: bool
```

实体是否有任意部分位于水方块内。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `EvalMolangExpression`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isInWater
```

## isOnGround {#isOnGround}

```python
isOnGround: bool
```

实体是否站在实体方块上。此状态可能存在特殊行为：刚生成时可能恒为 True，无重力实体的结果也可能不准确。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `EvalMolangExpression`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isOnGround
```

## isSleeping {#isSleeping}

```python
isSleeping: bool
```

实体是否正在睡眠。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `EvalMolangExpression`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isSleeping
```

## isSitting {#isSitting}

```python
isSitting: bool
```

实体是否正坐着。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsSitting`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isSitting
```

## isSneaking {#isSneaking}

```python
isSneaking: bool
```

实体是否处于移动更慢、更安静的潜行状态。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `EvalMolangExpression`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isSneaking
```

## isSprinting {#isSprinting}

```python
isSprinting: bool
```

实体是否正在疾跑，例如玩家疾跑、逃跑的豹猫或被胡萝卜钓竿加速的猪。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `EvalMolangExpression`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isSprinting
```

## isSwimming {#isSwimming}

```python
isSwimming: bool
```

实体是否处于游泳状态，例如执行游泳动作的玩家或水中的鱼。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `EvalMolangExpression`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isSwimming
```

## location {#location}

```python
location: Vector3
```

独立的原生脚底坐标 [Vector3](../extra/vector.md)；睡眠姿态保留原生坐标例外。

:::note 当前实现说明
保留 GetFootPos 的原生坐标约定，睡眠姿态有原生例外，不伪造床方向或模型骨骼位置。
:::

**访问：** 只读。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetFootPos`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.location
```

## nameTag {#nameTag}

```python
nameTag: str
```

实体的自定义名称。

**访问：** 可读写。

写入方式：`instance.nameTag = value`。参数类型线索：`(name: str) -> None`。

实体的自定义名称。

写入参数 `name`：[str](../../common/type-system.md#str)。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetName`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.nameTag

def write_value(instance, value):
    instance.nameTag = value
```

## health {#health}

```python
health: float
```

通过实时生命属性组件读取生命值。

**访问：** 可读写。

写入方式：`instance.health = value`。参数类型线索：`(value: float) -> None`。

在当前上下限内修改生命值，并保留原生默认值。

写入参数 `value`：[float](../../common/type-system.md#float)。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'SetAttrValue'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.health

def write_value(instance, value):
    instance.health = value
```

## scoreboardIdentity {#scoreboardIdentity}

```python
scoreboardIdentity
```

读取 `scoreboardIdentity` 的当前值。

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.scoreboardIdentity
```

## typeId {#typeId}

```python
typeId: str
```

实体类型标识，例如 minecraft:skeleton；实体失效后仍可读取。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEngineTypeStr`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## addEffect {#addEffect}

```python
addEffect(effectType: 'str|EffectType', duration: int, options: 'EntityEffectOptions|dict|None' = None) -> 'Effect'
```

为实体添加或更新状态效果，例如中毒。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `effectType` | `'str\|EffectType'` | `必填` | 传给 [Entity.addEffect](entity.md#addEffect) 的 effectType 参数；结合上方功能说明和下方调用示例使用。 |
| `duration` | [int](../../common/type-system.md#int) | `必填` | 传给 [Entity.addEffect](entity.md#addEffect) 的 duration 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | `'EntityEffectOptions\|dict\|None'` | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [Effect](../reference/Effect.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `AddEffectToEntity`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addEffect(instance, effectType, duration):
    return instance.addEffect(effectType, duration)
```

## addTag {#addTag}

```python
addTag(tag: str) -> bool
```

为实体添加指定标签。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `tag` | [str](../../common/type-system.md#str) | `必填` | 传给 [Entity.addTag](entity.md#addTag) 的 tag 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `AddEntityTag`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addTag(instance, tag):
    return instance.addTag(tag)
```

## applyDamage {#applyDamage}

```python
applyDamage(amount: int, options: 'dict|EntityApplyDamageByProjectileOptions|EntityApplyDamageOptions' = None) -> bool
```

对实体施加伤害。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `amount` | [int](../../common/type-system.md#int) | `必填` | 物品数量；新物品要求 1–255 的整数，并按最大堆叠数限制。 |
| `options` | `'dict\|EntityApplyDamageByProjectileOptions\|EntityApplyDamageOptions'` | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `Hurt`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_applyDamage(instance, amount):
    return instance.applyDamage(amount)
```

## applyImpulse {#applyImpulse}

```python
applyImpulse(vector: 'Vector3') -> None
```

向当前速度添加冲量，也适用于玩家。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `vector` | [Vector3](../extra/vector.md) | `必填` | 传给 [Entity.applyImpulse](entity.md#applyImpulse) 的 vector 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Could not read entity velocity'` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Could not update entity velocity'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetMotion`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_applyImpulse(instance, vector):
    return instance.applyImpulse(vector)
```

## applyKnockback {#applyKnockback}

```python
applyKnockback(horizontalForce: 'VectorXZ', verticalStrength: float) -> None
```

执行 `applyKnockback` 操作。原生实现使用 `SetMobKnockback`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `horizontalForce` | [VectorXZ](../../common/reference/VectorXZ.md) | `必填` | 传给 [Entity.applyKnockback](entity.md#applyKnockback) 的 horizontalForce 参数；结合上方功能说明和下方调用示例使用。 |
| `verticalStrength` | [float](../../common/type-system.md#float) | `必填` | 传给 [Entity.applyKnockback](entity.md#applyKnockback) 的 verticalStrength 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Knockback forces must be finite'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Knockback force is too large'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetMobKnockback`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_applyKnockback(instance, horizontalForce, verticalStrength):
    return instance.applyKnockback(horizontalForce, verticalStrength)
```

## clearDynamicProperties {#clearDynamicProperties}

```python
clearDynamicProperties() -> None
```

清除该实体的全部动态属性。原生删除或保存失败时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)；引擎不保证回滚此前已经发生的修改。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetWholeExtraData`, `SaveExtraData`, `CleanExtraData`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clearDynamicProperties(instance):
    return instance.clearDynamicProperties()
```

## clearVelocity {#clearVelocity}

```python
clearVelocity() -> None
```

移除或清理 `clearVelocity` 操作。参数形态和结果约定如下。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Could not clear entity velocity'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clearVelocity(instance):
    return instance.clearVelocity()
```

## extinguishFire {#extinguishFire}

```python
extinguishFire(useEffects: bool = True) -> bool
```

熄灭实体身上的火焰。可通过 getComponent('minecraft:onfire') 检查燃烧组件。useEffects 决定是否显示灭火相关的视觉效果，默认启用。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `useEffects` | [bool](../../common/type-system.md#bool) | `True` | 传给 [Entity.extinguishFire](entity.md#extinguishFire) 的 useEffects 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsEntityOnFire`, `SetEntityOnFire`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_extinguishFire(instance):
    return instance.extinguishFire()
```

## getBlockFromViewDirection {#getBlockFromViewDirection}

```python
getBlockFromViewDirection(options: 'dict|BlockRaycastOptions|None' = None) -> 'BlockRaycastHit|None'
```

返回最近的原生方块命中结果；目前只支持 maxDistance。尚未实现的筛选会在原生调用前报错，不会静默忽略。没有命中时返回 [None](../../common/type-system.md#none)；无法确定表面方向时，返回对象的 face 属性为 [None](../../common/type-system.md#none)。

:::note 当前实现说明
当前只支持 maxDistance，且必须是非负有限数；布尔值和数值字符串会被拒绝。液体、可穿过方块以及类型、标签、状态筛选尚未实现，显式设置会抛出 [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md)，未知选项抛出 [ValueError](../../common/type-system.md#valueerror)。没有命中时返回 [None](../../common/type-system.md#none)；表面方向无法确定时，返回对象的 face 为 [None](../../common/type-system.md#none)。原生射线检测还会忽略没有有效碰撞盒的方块。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | `'dict\|BlockRaycastOptions\|None'` | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** `'BlockRaycastHit\|None'`。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown block raycast option: %s' % ', '.join(sorted((str(key) for key in unknown)))` |
| [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md) | `'Block raycast filters are not implemented: %s' % ', '.join(sorted(unsupported))` |
| [TypeError](../../common/type-system.md#typeerror) | `'options must be a dictionary or BlockRaycastOptions'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** [Block](block.md)。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getBlockFromViewDirection(instance):
    return instance.getBlockFromViewDirection()
```

## getComponent {#getComponent}

```python
getComponent(componentId: str) -> 'EntityComponent|None'
```

读取实体组件，以访问实体的附加能力。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `componentId` | [str](../../common/type-system.md#str) | `必填` | 传给 [Entity.getComponent](entity.md#getComponent) 的 componentId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** `'EntityComponent\|None'`。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getComponent(instance, componentId):
    return instance.getComponent(componentId)
```

## getComponents {#getComponents}

```python
getComponents() -> 'list[EntityComponent]'
```

返回此实体具有且当前接口支持的全部组件。

**返回类型：** `'list[EntityComponent]'`。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAllComponentsName`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getComponents(instance):
    return instance.getComponents()
```

## getDynamicProperty {#getDynamicProperty}

```python
getDynamicProperty(identifier: str) -> Any
```

读取属性值。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |

**返回类型：** [Any](../../common/type-system.md#any)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetExtraData`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDynamicProperty(instance, identifier):
    return instance.getDynamicProperty(identifier)
```

## getDynamicPropertyIds {#getDynamicPropertyIds}

```python
getDynamicPropertyIds() -> 'list[str]'
```

返回此实体已使用的动态属性标识集合。

**返回类型：** `'list[str]'`。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetWholeExtraData`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDynamicPropertyIds(instance):
    return instance.getDynamicPropertyIds()
```

## getDynamicPropertyTotalByteCount {#getDynamicPropertyTotalByteCount}

```python
getDynamicPropertyTotalByteCount() -> int
```

返回此实体存储的全部动态属性大小，单位为字节，包含键和值。可用于排查性能问题；大量动态属性可能使部分设备上的实体加载变慢。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetWholeExtraData`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDynamicPropertyTotalByteCount(instance):
    return instance.getDynamicPropertyTotalByteCount()
```

## getEffect {#getEffect}

```python
getEffect(effectType: 'str|EffectType') -> 'Effect|None'
```

读取 `getEffect` 操作。原生实现使用 `GetAllEffects`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `effectType` | `'str\|EffectType'` | `必填` | 传给 [Entity.getEffect](entity.md#getEffect) 的 effectType 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** `'Effect\|None'`。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAllEffects`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEffect(instance, effectType):
    return instance.getEffect(effectType)
```

## getEffects {#getEffects}

```python
getEffects() -> 'list[Effect]'
```

读取此实体当前的状态效果集合。

**返回类型：** `'list[Effect]'`。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAllEffects`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEffects(instance):
    return instance.getEffects()
```

## getEntitiesFromViewDirection {#getEntitiesFromViewDirection}

```python
getEntitiesFromViewDirection(options: 'dict|None' = None) -> 'list[EntityRaycastHit]'
```

读取 `getEntitiesFromViewDirection` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | `'dict\|None'` | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** `'list[EntityRaycastHit]'`。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEntitiesFromViewDirection(instance):
    return instance.getEntitiesFromViewDirection()
```

## getHeadLocation {#getHeadLocation}

```python
getHeadLocation() -> 'Vector3'
```

读取实体头部的当前位置。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetSize`, `GetFootPos`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getHeadLocation(instance):
    return instance.getHeadLocation()
```

## getRotation {#getRotation}

```python
getRotation() -> 'Vector2'
```

读取实体当前的旋转。

**返回类型：** [Vector2](../../common/reference/Vector2.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetRot`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getRotation(instance):
    return instance.getRotation()
```

## getTags {#getTags}

```python
getTags() -> 'list[str]'
```

读取实体的全部标签。

**返回类型：** `'list[str]'`。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEntityTags`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getTags(instance):
    return instance.getTags()
```

## getVelocity {#getVelocity}

```python
getVelocity() -> 'Vector3'
```

读取实体当前的速度向量。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetMotion`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getVelocity(instance):
    return instance.getVelocity()
```

## getNbt {#getNbt}

```python
getNbt() -> dict
```

以 JSON 对象形式读取实体的 NBT 数据。

**返回类型：** [dict](../../common/type-system.md#dict)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEntityNBTTags`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getNbt(instance):
    return instance.getNbt()
```

## getProperty {#getProperty}

```python
getProperty(identifier: str)
```

读取实体定义属性。同一刻内通过 setProperty 写入的值，可能直到下一刻才反映在读取结果中。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAllProperties`, `EvalMolangExpression`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getProperty(instance, identifier):
    return instance.getProperty(identifier)
```

## getViewDirection {#getViewDirection}

```python
getViewDirection() -> 'Vector3'
```

读取实体当前的视线方向。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetRot`, `GetDirFromRot`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getViewDirection(instance):
    return instance.getViewDirection()
```

## getFamilies {#getFamilies}

```python
getFamilies() -> list[str]
```

读取 `getFamilies` 操作。原生实现使用 `GetTypeFamily`，行为受网易运行环境约束。

**返回类型：** [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetTypeFamily`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getFamilies(instance):
    return instance.getFamilies()
```

## hasComponent {#hasComponent}

```python
hasComponent(componentId: str) -> bool
```

检查此实体是否具有指定组件。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `componentId` | [str](../../common/type-system.md#str) | `必填` | 传给 [Entity.hasComponent](entity.md#hasComponent) 的 componentId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetComponents`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasComponent(instance, componentId):
    return instance.hasComponent(componentId)
```

## hasTag {#hasTag}

```python
hasTag(tag: str) -> bool
```

检查实体是否具有指定标签。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `tag` | [str](../../common/type-system.md#str) | `必填` | 传给 [Entity.hasTag](entity.md#hasTag) 的 tag 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `EntityHasTag`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasTag(instance, tag):
    return instance.hasTag(tag)
```

## hasTarget {#hasTarget}

```python
hasTarget() -> bool
```

检查实体是否具有目标。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAttackTarget`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasTarget(instance):
    return instance.hasTarget()
```

## getTarget {#getTarget}

```python
getTarget() -> Entity | None
```

读取实体当前的目标。

**返回类型：** [Entity](entity.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAttackTarget`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getTarget(instance):
    return instance.getTarget()
```

## hasFamily {#hasFamily}

```python
hasFamily(familyName: str) -> bool
```

检查实体是否属于指定类型族。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `familyName` | [str](../../common/type-system.md#str) | `必填` | 传给 [Entity.hasFamily](entity.md#hasFamily) 的 familyName 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetTypeFamily`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasFamily(instance, familyName):
    return instance.hasFamily(familyName)
```

## kill {#kill}

```python
kill() -> bool
```

杀死此实体，并按正常规则掉落战利品。可执行击杀时返回 True，即使实体已经死亡；否则返回 False。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `KillEntity`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_kill(instance):
    return instance.kill()
```

## matches {#matches}

```python
matches(options: 'dict|None' = None) -> bool
```

检查 `matches` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | `'dict\|None'` | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_matches(instance):
    return instance.matches()
```

## playAnimation {#playAnimation}

```python
playAnimation(animationName: str, options: 'dict|PlayAnimationOptions' = {}) -> None
```

让实体播放指定动画。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `animationName` | [str](../../common/type-system.md#str) | `必填` | 传给 [Entity.playAnimation](entity.md#playAnimation) 的 animationName 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | `'dict\|PlayAnimationOptions'` | `{}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetCommand`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_playAnimation(instance, animationName):
    return instance.playAnimation(animationName)
```

## remove {#remove}

```python
remove() -> None
```

立即从世界移除实体，不播放死亡动画，也不掉落战利品。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `DestroyEntity`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_remove(instance):
    return instance.remove()
```

## removeEffect {#removeEffect}

```python
removeEffect(effectType: 'str|EffectType') -> bool
```

移除指定 [EffectType](../reference/EffectType.md) 对应的效果；效果不存在时返回 False。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `effectType` | `'str\|EffectType'` | `必填` | 传给 [Entity.removeEffect](entity.md#removeEffect) 的 effectType 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `RemoveEffectFromEntity`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeEffect(instance, effectType):
    return instance.removeEffect(effectType)
```

## removeTag {#removeTag}

```python
removeTag(tag: str) -> bool
```

移除实体上的指定标签。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `tag` | [str](../../common/type-system.md#str) | `必填` | 传给 [Entity.removeTag](entity.md#removeTag) 的 tag 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `RemoveEntityTag`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeTag(instance, tag):
    return instance.removeTag(tag)
```

## resetProperty {#resetProperty}

```python
resetProperty(identifier: str)
```

将实体定义属性恢复为定义中的默认值；更改到下一刻才生效。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Cannot read the default value of property %s' % identifier` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Cannot reset entity property %s' % identifier` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `DestroyEntity`, `GetAllProperties`, `EvalMolangExpression`, `SetPropertyValue`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_resetProperty(instance, identifier):
    return instance.resetProperty(identifier)
```

## runCommand {#runCommand}

```python
runCommand(commandString: str) -> CommandResult
```

以实体为上下文同步执行命令。ModSDK 仅报告成功或失败，因此成功时 successCount 为 1，无法取得原生实际影响的目标数量。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `commandString` | [str](../../common/type-system.md#str) | `必填` | 传给 [Entity.runCommand](entity.md#runCommand) 的 commandString 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [CommandResult](../reference/CommandResult.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Command execution failed: %s' % commandString` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetCommand`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_runCommand(instance, commandString):
    return instance.runCommand(commandString)
```

## setDynamicProperties {#setDynamicProperties}

```python
setDynamicProperties(values: dict) -> None
```

预先校验所有标识并复制值，再批量修改，最后统一保存一次。[None](../../common/type-system.md#none) 表示删除，空字典不调用引擎。原生写入或保存失败时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)；引擎不保证回滚此前已经发生的修改。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `values` | [dict](../../common/type-system.md#dict) | `必填` | 传给 [Entity.setDynamicProperties](entity.md#setDynamicProperties) 的 values 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SaveExtraData`, `CleanExtraData`, `SetExtraData`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setDynamicProperties(instance, values):
    return instance.setDynamicProperties(values)
```

## setDynamicProperty {#setDynamicProperty}

```python
setDynamicProperty(identifier: str, value: Any = None) -> None
```

设置指定动态属性，[None](../../common/type-system.md#none) 表示删除。写入前复制值；原生写入或保存失败时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `value` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SaveExtraData`, `CleanExtraData`, `SetExtraData`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setDynamicProperty(instance, identifier):
    return instance.setDynamicProperty(identifier)
```

## setOnFire {#setOnFire}

```python
setOnFire(seconds: int, useEffects: bool = True) -> bool
```

使实体着火，实体处于水中或雨中时可能无法生效。可通过 getComponent('minecraft:onfire') 检查燃烧组件。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `seconds` | [int](../../common/type-system.md#int) | `必填` | 传给 [Entity.setOnFire](entity.md#setOnFire) 的 seconds 参数；结合上方功能说明和下方调用示例使用。 |
| `useEffects` | [bool](../../common/type-system.md#bool) | `True` | 传给 [Entity.setOnFire](entity.md#setOnFire) 的 useEffects 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetEntityOnFire`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setOnFire(instance, seconds):
    return instance.setOnFire(seconds)
```

## setProperty {#setProperty}

```python
setProperty(identifier: str, value) -> None
```

设置实体定义属性；更改到下一刻才生效。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `value` | 由值/所属选项确定 | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetPropertyValue`, `GetAllProperties`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setProperty(instance, identifier, value):
    return instance.setProperty(identifier, value)
```

## setRotation {#setRotation}

```python
setRotation(rotation: 'Vector2') -> None
```

设置实体的主要旋转角度。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `rotation` | [Vector2](../../common/reference/Vector2.md) | `必填` | 旋转角度，具体分量与单位参见成员说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetRot`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setRotation(instance, rotation):
    return instance.setRotation(rotation)
```

## teleport {#teleport}

```python
teleport(location: 'Vector3', teleportOptions: 'dict|TeleportOptions' = None) -> None
```

将实体传送到新位置。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `teleportOptions` | `'dict\|TeleportOptions'` | [None](../../common/type-system.md#none) | 传给 [Entity.teleport](entity.md#teleport) 的 teleportOptions 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NotImplementedError](../../common/type-system.md#notimplementederror) | `'ModSDK cannot check collision before a cross-dimension teleport'` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to teleport entity'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetCommand`, `SetPlayerMotion`, `SetMotion`, `SetFootPos`, `ChangePlayerDimension`, `ChangeEntityDimension`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_teleport(instance, location):
    return instance.teleport(location)
```

## triggerEvent {#triggerEvent}

```python
triggerEvent(eventName: str) -> None
```

触发实体类型事件。此类事件在实体定义中配置，例如苦力怕的 minecraft:start_exploding。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `eventName` | [str](../../common/type-system.md#str) | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `TriggerCustomEvent`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_triggerEvent(instance, eventName):
    return instance.triggerEvent(eventName)
```

## tryTeleport {#tryTeleport}

```python
tryTeleport(location: 'Vector3', teleportOptions: 'dict|None' = None) -> bool
```

尝试传送实体；目标位置被方块阻挡等情况可能导致传送失败。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `teleportOptions` | `'dict\|None'` | [None](../../common/type-system.md#none) | 传给 [Entity.tryTeleport](entity.md#tryTeleport) 的 teleportOptions 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_tryTeleport(instance, location):
    return instance.tryTeleport(location)
```

## asPlayer {#asPlayer}

```python
asPlayer() -> Player
```

执行 `asPlayer` 操作。原生实现使用 [Player](player.md)，行为受网易运行环境约束。

**返回类型：** [Player](player.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** [Player](player.md)。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_asPlayer(instance):
    return instance.asPlayer()
```

## isAngry {#isAngry}

```python
isAngry: bool
```

原生实体是否处于激怒状态；不支持的实体定义会报告失败。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsAngry`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isAngry
```

## isBaby {#isBaby}

```python
isBaby: bool
```

原生实体是否为幼年状态。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsBaby`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isBaby
```

## isPregnant {#isPregnant}

```python
isPregnant: bool
```

原生怀孕状态是否有效，具体支持取决于实体种类。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsPregnant`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isPregnant
```

## isSheared {#isSheared}

```python
isSheared: bool
```

原生实体是否已被剪毛，需要实体定义支持。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsSheared`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isSheared
```

## isTamed {#isTamed}

```python
isTamed: bool
```

原生实体是否已经驯服。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsTamed`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isTamed
```

## isOutOfControl {#isOutOfControl}

```python
isOutOfControl: bool
```

原生失控状态是否有效，通常用于船。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsOutOfControl`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isOutOfControl
```

## isIllagerCaptain {#isIllagerCaptain}

```python
isIllagerCaptain: bool
```

实体是否为袭击队长，具体支持取决于实体定义。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsIllagerCaptain`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isIllagerCaptain
```

## isChested {#isChested}

```python
isChested: bool
```

支持的羊驼、驴、骡等载体是否背负箱子。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `HasChest`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isChested
```

## isSaddled {#isSaddled}

```python
isSaddled: bool
```

原生实体是否装备了鞍。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `HasSaddle`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isSaddled
```

## variant {#variant}

```python
variant: int
```

非负的原生变种值，具体含义由实体 JSON 定义决定。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetVariant`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.variant
```

## markVariant {#markVariant}

```python
markVariant: int
```

非负的原生标记变种，例如马的花纹或村民服装。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetMarkVariant`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.markVariant
```

## tradeLevel {#tradeLevel}

```python
tradeLevel: int
```

原生村民交易等级；原生失败哨兵不被当成正常等级。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetTradeLevel`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.tradeLevel
```

## strength {#strength}

```python
strength: int
```

原生羊驼携带强度，文档范围为一到五。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetMobStrength`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.strength
```

## maxStrength {#maxStrength}

```python
maxStrength: int
```

原生羊驼最大强度；引擎重新加载时可能恢复 JSON 配置值。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetMobStrengthMax`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.maxStrength
```

## deathTimeTicks {#deathTimeTicks}

```python
deathTimeTicks: int
```

原生死亡动画持续时间，以每秒二十个逻辑刻计量；未死亡时为零。特意允许查询仍被原生引擎保留的死亡实体。凋零死亡动画不受此原生方法支持。

:::note 当前实现说明
特意允许仍被引擎保留的死亡实体。无效原生结果报告错误，不改变实体存活状态；凋零使用特殊死亡动画。
:::

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetDeathTime`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.deathTimeTicks
```

## color {#color}

```python
color: str
```

以标准 [DyeColor](../../common/reference/DyeColor.md) 字符串读取原生羊或鱼的颜色。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetMobColor'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetMobColor`, `GetMinecraftEnum`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.color
```

## setAngry {#setAngry}

```python
setAngry(isAngry: bool, target: Entity | None = None) -> None
```

设置怒气；启用时使用有效的目标包装对象。True 必须提供目标，False 必须省略目标。仍受原生实体定义和感知范围限制。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `isAngry` | [bool](../../common/type-system.md#bool) | `必填` | 传给 [Entity.setAngry](entity.md#setAngry) 的 isAngry 参数；结合上方功能说明和下方调用示例使用。 |
| `target` | [Entity](entity.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Entity.setAngry](entity.md#setAngry) 的 target 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Enabling anger requires a target'` |
| [ValueError](../../common/type-system.md#valueerror) | `'A target is not used when clearing anger'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetAngry`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setAngry(instance, isAngry):
    return instance.setAngry(isAngry)
```

## growUp {#growUp}

```python
growUp() -> None
```

请求原生成长；实体定义需要具有 ageable_grow_up 事件。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetAsAdult`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_growUp(instance):
    return instance.growUp()
```

## setSheared {#setSheared}

```python
setSheared(isSheared: bool) -> None
```

设置受支持实体的原生剪毛状态，例如羊。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `isSheared` | [bool](../../common/type-system.md#bool) | `必填` | 传给 [Entity.setSheared](entity.md#setSheared) 的 isSheared 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetSheared`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setSheared(instance, isSheared):
    return instance.setSheared(isSheared)
```

## setSitting {#setSitting}

```python
setSitting(isSitting: bool) -> None
```

设置原生坐姿；熊猫使用其他原生行为。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `isSitting` | [bool](../../common/type-system.md#bool) | `必填` | 传给 [Entity.setSitting](entity.md#setSitting) 的 isSitting 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetSitting`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setSitting(instance, isSitting):
    return instance.setSitting(isSitting)
```

## setOutOfControl {#setOutOfControl}

```python
setOutOfControl(isOutOfControl: bool) -> None
```

设置受支持实体的原生失控状态，例如船。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `isOutOfControl` | [bool](../../common/type-system.md#bool) | `必填` | 传给 [Entity.setOutOfControl](entity.md#setOutOfControl) 的 isOutOfControl 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetOutOfControl`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setOutOfControl(instance, isOutOfControl):
    return instance.setOutOfControl(isOutOfControl)
```

## setChested {#setChested}

```python
setChested(isChested: bool) -> None
```

设置受支持羊驼、驴、骡的背负箱子状态。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `isChested` | [bool](../../common/type-system.md#bool) | `必填` | 传给 [Entity.setChested](entity.md#setChested) 的 isChested 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetChest`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setChested(instance, isChested):
    return instance.setChested(isChested)
```

## promoteToIllagerCaptain {#promoteToIllagerCaptain}

```python
promoteToIllagerCaptain() -> None
```

将支持的掠夺者或卫道士晋升为袭击队长。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `PromoteToIllagerCaptain`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_promoteToIllagerCaptain(instance):
    return instance.promoteToIllagerCaptain()
```

## setVariant {#setVariant}

```python
setVariant(variant: int) -> None
```

设置实体 JSON 支持的非负变种整数。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `variant` | [int](../../common/type-system.md#int) | `必填` | 传给 [Entity.setVariant](entity.md#setVariant) 的 variant 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetVariant`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setVariant(instance, variant):
    return instance.setVariant(variant)
```

## setMarkVariant {#setMarkVariant}

```python
setMarkVariant(variant: int) -> None
```

设置实体定义支持的非负标记变种整数。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `variant` | [int](../../common/type-system.md#int) | `必填` | 传给 [Entity.setMarkVariant](entity.md#setMarkVariant) 的 variant 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetMarkVariant`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setMarkVariant(instance, variant):
    return instance.setMarkVariant(variant)
```

## setTradeLevel {#setTradeLevel}

```python
setTradeLevel(level: int) -> None
```

设置原生村民交易等级整数；不支持的值会报告原生失败。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `level` | [int](../../common/type-system.md#int) | `必填` | 传给 [Entity.setTradeLevel](entity.md#setTradeLevel) 的 level 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetTradeLevel`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setTradeLevel(instance, level):
    return instance.setTradeLevel(level)
```

## setStrength {#setStrength}

```python
setStrength(strength: int) -> None
```

设置羊驼强度，避免被原生最大值静默截断。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `strength` | [int](../../common/type-system.md#int) | `必填` | 传给 [Entity.setStrength](entity.md#setStrength) 的 strength 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetMobStrengthMax'` |
| [ArgumentOutOfBoundsError](../../common/reference/ArgumentOutOfBoundsError.md) | `'Strength exceeds the current native maximum'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetMobStrengthMax`, `SetMobStrength`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setStrength(instance, strength):
    return instance.setStrength(strength)
```

## setMaxStrength {#setMaxStrength}

```python
setMaxStrength(strength: int) -> None
```

设置原生羊驼强度上限；引擎重新加载时可能重置。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `strength` | [int](../../common/type-system.md#int) | `必填` | 传给 [Entity.setMaxStrength](entity.md#setMaxStrength) 的 strength 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetMobStrengthMax`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setMaxStrength(instance, strength):
    return instance.setMaxStrength(strength)
```

## setColor {#setColor}

```python
setColor(color: str) -> None
```

使用标准 [DyeColor](../../common/reference/DyeColor.md) 字符串设置支持的羊或鱼的颜色。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `color` | [str](../../common/type-system.md#str) | `必填` | 传给 [Entity.setColor](entity.md#setColor) 的 color 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown DyeColor: ' + color` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetMobColor`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setColor(instance, color):
    return instance.setColor(color)
```

## getOwner {#getOwner}

```python
getOwner() -> Entity | None
```

读取实体属主包装对象，包含驯服主人及弹射物发射者等关系。

**返回类型：** [Entity](entity.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'CreateEngineType'` |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetEngineTypeStr'` |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetEntityOwner'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEntityOwner`, `GetEngineTypeStr`, `GetEngineCompFactory`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getOwner(instance):
    return instance.getOwner()
```

## setOwner {#setOwner}

```python
setOwner(owner: Entity | None = None) -> None
```

使用服务端实体包装对象设置属主，传入 [None](../../common/type-system.md#none) 可清除属主。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `owner` | [Entity](entity.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Entity.setOwner](entity.md#setOwner) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetEntityOwner`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setOwner(instance):
    return instance.setOwner()
```

## 使用示例


```python
from ModSAPI.server.beta import world

for entity in world.getDimension("overworld").getEntities():
    if entity.isValid:
        print(entity.id, entity.typeId)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)