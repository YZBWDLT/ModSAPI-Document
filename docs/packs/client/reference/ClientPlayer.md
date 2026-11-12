---
title: "ClientPlayer"
sidebar_label: "ClientPlayer"
---

# ClientPlayer

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Player.py`；声明补充了静态类型信息。

本地玩家的可读状态及本地显示控制。

## 获取方式

使用 [client.localPlayer](../apis/manager.md#localPlayer)。

基类：[ClientEntity](ClientEntity.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [name](#name) | 只读属性 |
| [dimension](#dimension) | 只读属性 |
| [isGliding](#isGliding) | 只读属性 |
| [isInWater](#isInWater) | 只读属性 |
| [isMoving](#isMoving) | 只读属性 |
| [isRiding](#isRiding) | 只读属性 |
| [isSneaking](#isSneaking) | 只读属性 |
| [isSprinting](#isSprinting) | 只读属性 |
| [isSwimming](#isSwimming) | 只读属性 |
| [isInScaffolding](#isInScaffolding) | 只读属性 |
| [isOnLadder](#isOnLadder) | 只读属性 |
| [isFishing](#isFishing) | 只读属性 |
| [armorValue](#armorValue) | 只读属性 |
| [hunger](#hunger) | 只读属性 |
| [xpEarnedAtCurrentLevel](#xpEarnedAtCurrentLevel) | 只读属性 |
| [totalXpNeededForNextLevel](#totalXpNeededForNextLevel) | 只读属性 |
| [getTotalXp](#getTotalXp) | 方法 |
| [getRidingEntity](#getRidingEntity) | 方法 |
| [setVelocity](#setVelocity) | 方法 |
| [swingArm](#swingArm) | 方法 |
| [setShieldActive](#setShieldActive) | 方法 |
| [sendToast](#sendToast) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [airSupplyTicks](ClientEntity.md#airSupplyTicks) | [ClientEntity](ClientEntity.md) |
| [bodyRotation](ClientEntity.md#bodyRotation) | [ClientEntity](ClientEntity.md) |
| [collisionBoxSize](ClientEntity.md#collisionBoxSize) | [ClientEntity](ClientEntity.md) |
| [getComponent](ClientEntity.md#getComponent) | [ClientEntity](ClientEntity.md) |
| [getComponents](ClientEntity.md#getComponents) | [ClientEntity](ClientEntity.md) |
| [getMolangValue](ClientEntity.md#getMolangValue) | [ClientEntity](ClientEntity.md) |
| [getOwner](ClientEntity.md#getOwner) | [ClientEntity](ClientEntity.md) |
| [getQueryVariable](ClientEntity.md#getQueryVariable) | [ClientEntity](ClientEntity.md) |
| [getRotation](ClientEntity.md#getRotation) | [ClientEntity](ClientEntity.md) |
| [getTarget](ClientEntity.md#getTarget) | [ClientEntity](ClientEntity.md) |
| [getVelocity](ClientEntity.md#getVelocity) | [ClientEntity](ClientEntity.md) |
| [getViewDirection](ClientEntity.md#getViewDirection) | [ClientEntity](ClientEntity.md) |
| [hasComponent](ClientEntity.md#hasComponent) | [ClientEntity](ClientEntity.md) |
| [id](ClientEntity.md#id) | [ClientEntity](ClientEntity.md) |
| [isInLava](ClientEntity.md#isInLava) | [ClientEntity](ClientEntity.md) |
| [isOnGround](ClientEntity.md#isOnGround) | [ClientEntity](ClientEntity.md) |
| [isValid](ClientEntity.md#isValid) | [ClientEntity](ClientEntity.md) |
| [location](ClientEntity.md#location) | [ClientEntity](ClientEntity.md) |
| [maxAirSupplyTicks](ClientEntity.md#maxAirSupplyTicks) | [ClientEntity](ClientEntity.md) |
| [nameTag](ClientEntity.md#nameTag) | [ClientEntity](ClientEntity.md) |
| [remove](ClientEntity.md#remove) | [ClientEntity](ClientEntity.md) |
| [setMolangValue](ClientEntity.md#setMolangValue) | [ClientEntity](ClientEntity.md) |
| [setQueryVariable](ClientEntity.md#setQueryVariable) | [ClientEntity](ClientEntity.md) |
| [setRotation](ClientEntity.md#setRotation) | [ClientEntity](ClientEntity.md) |
| [teleport](ClientEntity.md#teleport) | [ClientEntity](ClientEntity.md) |
| [typeId](ClientEntity.md#typeId) | [ClientEntity](ClientEntity.md) |

## 构造器 {#constructor}

```python
ClientPlayer(owner: Any = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `owner` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 传给 [ClientPlayer.__init__](ClientPlayer.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLocalPlayerId`。

## name {#name}

```python
name: str
```

当前玩家名称，每次读取均从引擎刷新。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.name
```

## dimension {#dimension}

```python
dimension: ClientDimension
```

本地玩家当前显示的维度包装对象。

**访问：** 只读。

**返回类型：** [ClientDimension](ClientDimension.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetCurrentDimension'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetCurrentDimension`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.dimension
```

## isGliding {#isGliding}

```python
isGliding: bool
```

本地玩家是否正在使用鞘翅滑翔。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `isGliding`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isGliding
```

## isInWater {#isInWater}

```python
isInWater: bool
```

本地玩家是否在水中。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `isInWater`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isInWater
```

## isMoving {#isMoving}

```python
isMoving: bool
```

本地玩家的原生行走状态是否有效。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `isMoving`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isMoving
```

## isRiding {#isRiding}

```python
isRiding: bool
```

本地玩家是否正在骑乘实体。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `isRiding`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isRiding
```

## isSneaking {#isSneaking}

```python
isSneaking: bool
```

本地玩家是否正在潜行；此属性只读。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `isSneaking`。

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

本地玩家是否正在疾跑；静止时返回 False。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `isSprinting`。

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

本地玩家是否正在游泳。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `isSwimming`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isSwimming
```

## isInScaffolding {#isInScaffolding}

```python
isInScaffolding: bool
```

本地玩家是否处于脚手架内。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsInScaffolding`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isInScaffolding
```

## isOnLadder {#isOnLadder}

```python
isOnLadder: bool
```

本地玩家是否在梯子或藤蔓上，不推断其他攀爬状态。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsOnLadder`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isOnLadder
```

## isFishing {#isFishing}

```python
isFishing: bool
```

本地玩家当前是否正在钓鱼。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerIsFishing`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isFishing
```

## armorValue {#armorValue}

```python
armorValue: int
```

读取本地玩家的原生护甲显示值。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetArmorValue'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetArmorValue`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.armorValue
```

## hunger {#hunger}

```python
hunger: float
```

从玩家组件读取饥饿点数，不据此推算饱和度。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetPlayerHunger'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerHunger`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.hunger
```

## xpEarnedAtCurrentLevel {#xpEarnedAtCurrentLevel}

```python
xpEarnedAtCurrentLevel: float
```

读取当前等级内的绝对经验值，不是百分比。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetPlayerExp'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerExp`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.xpEarnedAtCurrentLevel
```

## totalXpNeededForNextLevel {#totalXpNeededForNextLevel}

```python
totalXpNeededForNextLevel: int
```

完成当前等级需要的总经验量，不是还差多少经验。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetPlayerCurLevelExp'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerCurLevelExp`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.totalXpNeededForNextLevel
```

## getTotalXp {#getTotalXp}

```python
getTotalXp() -> int
```

读取原生总经验；原生失败哨兵会转换为错误。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetPlayerTotalExp'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerTotalExp`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getTotalXp(instance):
    return instance.getTotalXp()
```

## getRidingEntity {#getRidingEntity}

```python
getRidingEntity() -> ClientEntity | None
```

取得本地玩家直接骑乘的已加载实体对象，没有时返回 [None](../../common/type-system.md#none)，不返回实体标识符。优先使用骑乘组件；旧客户端缺少该方法时使用原生游戏查询。兼容查询不会掩盖原生调用失败。

**返回类型：** [ClientEntity](ClientEntity.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEntityRider`, `GetRiderId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getRidingEntity(instance):
    return instance.getRidingEntity()
```

## setVelocity {#setVelocity}

```python
setVelocity(velocity: VectorLike) -> None
```

使用有限的世界向量替换本地玩家的原生运动，不是叠加冲量。频繁写入可能与服务端模拟不一致；权威移动应在服务端完成。其他客户端实体没有此写入方法。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `velocity` | [VectorLike](../../common/type-aliases.md#vectorlike) | `必填` | 传给 [ClientPlayer.setVelocity](ClientPlayer.md#setVelocity) 的 velocity 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetMotion`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setVelocity(instance, velocity):
    return instance.setVelocity(velocity)
```

## swingArm {#swingArm}

```python
swingArm() -> None
```

播放本地玩家的原版攻击挥手动作，不实际执行攻击。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `Swing`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_swingArm(instance):
    return instance.swingArm()
```

## setShieldActive {#setShieldActive}

```python
setShieldActive(isActive: bool) -> bool
```

请求本地盾牌状态；未手持盾牌时返回 False。原生结果 1、0、-1 分别表示成功、失败、未持盾。失败及未知结果会抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `isActive` | [bool](../../common/type-system.md#bool) | `必填` | 传给 [ClientPlayer.setShieldActive](ClientPlayer.md#setShieldActive) 的 isActive 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'setUsingShield'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `setUsingShield`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setShieldActive(instance, isActive):
    return instance.setShieldActive(isActive)
```

## sendToast {#sendToast}

```python
sendToast(message: str, title: str = '') -> None
```

显示本地提示，参数顺序与服务端扩展一致。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `message` | [str](../../common/type-system.md#str) | `必填` | 传给 [ClientPlayer.sendToast](ClientPlayer.md#sendToast) 的 message 参数；结合上方功能说明和下方调用示例使用。 |
| `title` | [str](../../common/type-system.md#str) | `''` | 标题文本，动态表单也可接受相应 [Observable](../../ui/reference/Observable.md)。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'title must be text without NUL'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetPopupNotice`, `GetEngineCompFactory`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_sendToast(instance, message):
    return instance.sendToast(message)
```

## 使用示例


```python
from ModSAPI.client.beta import client

player = client.localPlayer
print(player.id, player.location.getTuple())
player.sendToast("Ready", "Example")
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)