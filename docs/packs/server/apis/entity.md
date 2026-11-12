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

实体的当前位置。

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
health
```

读取 `health` 的当前值。底层调用 `GetAttrValue`。

**访问：** 可读写。

写入方式：`instance.health = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAttrValue`。

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
addEffect(effectType: 'str|EffectType', duration: int, options: 'EntityEffectOptions|dict' = None) -> 'Effect'
```

为实体添加或更新状态效果，例如中毒。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `effectType` | `'str\|EffectType'` | `必填` | 传给 [Entity.addEffect](entity.md#addEffect) 的 effectType 参数；结合上方功能说明和下方调用示例使用。 |
| `duration` | [int](../../common/type-system.md#int) | `必填` | 传给 [Entity.addEffect](entity.md#addEffect) 的 duration 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | `'EntityEffectOptions\|dict'` | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

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

清除实体上的全部动态属性。

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
getBlockFromViewDirection(options: 'dict|BlockRaycastOptions' = None) -> 'BlockRaycastHit'
```

读取 `getBlockFromViewDirection` 操作。原生实现使用 [Block](block.md)，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | `'dict\|BlockRaycastOptions'` | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [BlockRaycastHit](../../common/reference/BlockRaycastHit.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'maxDistance must be finite and non-negative'` |

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
getDynamicProperty(identifier: str)
```

读取属性值。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

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
getEffect(effectType: 'str|EffectType') -> 'Effect'
```

读取 `getEffect` 操作。原生实现使用 `GetAllEffects`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `effectType` | `'str\|EffectType'` | `必填` | 传给 [Entity.getEffect](entity.md#getEffect) 的 effectType 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Effect](../reference/Effect.md)。静态声明不替代本页的实现限制。

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
getEntitiesFromViewDirection(options: 'dict' = None) -> 'list[EntityRaycastHit]'
```

读取 `getEntitiesFromViewDirection` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

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
matches(options: 'dict' = None) -> bool
```

检查 `matches` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

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

设置 `setDynamicProperties` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `values` | [dict](../../common/type-system.md#dict) | `必填` | 传给 [Entity.setDynamicProperties](entity.md#setDynamicProperties) 的 values 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'Dynamic properties must be a dictionary'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setDynamicProperties(instance, values):
    return instance.setDynamicProperties(values)
```

## setDynamicProperty {#setDynamicProperty}

```python
setDynamicProperty(identifier: str, value = None) -> None
```

将指定属性设置为给定值。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `value` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 需要写入的值，类型、范围及副本语义见本成员说明。 |

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
tryTeleport(location: 'Vector3', teleportOptions: 'dict' = None) -> bool
```

尝试传送实体；目标位置被方块阻挡等情况可能导致传送失败。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `teleportOptions` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 传给 [Entity.tryTeleport](entity.md#tryTeleport) 的 teleportOptions 参数；结合上方功能说明和下方调用示例使用。 |

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

## 使用示例


```python
from ModSAPI.server.beta import world

for entity in world.getDimension("overworld").getEntities():
    if entity.isValid:
        print(entity.id, entity.typeId)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)