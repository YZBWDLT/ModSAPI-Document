---
title: "Player"
sidebar_label: "Player"
---

# Player

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Player.py`；声明补充了静态类型信息。

世界中的玩家对象。

## 获取方式

通过 `world.getAllPlayers()`、玩家事件或有效玩家 ID 获取。

基类：[Entity](entity.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [name](#name) | 只读属性 |
| [camera](#camera) | 只读属性 |
| [isFlying](#isFlying) | 只读属性 |
| [level](#level) | 只读属性 |
| [xpEarnedAtCurrentLevel](#xpEarnedAtCurrentLevel) | 只读属性 |
| [getTotalXp](#getTotalXp) | 方法 |
| [addExperience](#addExperience) | 方法 |
| [addLevels](#addLevels) | 方法 |
| [resetLevel](#resetLevel) | 方法 |
| [selectedSlotIndex](#selectedSlotIndex) | 可读写属性 |
| [clientSystemInfo](#clientSystemInfo) | 只读属性 |
| [playerPermissionLevel](#playerPermissionLevel) | 只读属性 |
| [container](#container) | 只读属性 |
| [mainHand](#mainHand) | 可读写属性 |
| [applyKnockback](#applyKnockback) | 方法 |
| [playSound](#playSound) | 方法 |
| [sendMessage](#sendMessage) | 方法 |
| [getSpawnPoint](#getSpawnPoint) | 方法 |
| [sendToast](#sendToast) | 方法 |
| [spawnParticle](#spawnParticle) | 方法 |
| [showUI](#showUI) | 方法 |
| [popScreen](#popScreen) | 方法 |
| [getGameMode](#getGameMode) | 方法 |
| [setGameMode](#setGameMode) | 方法 |
| [teleport](#teleport) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [addEffect](entity.md#addEffect) | [Entity](entity.md) |
| [addTag](entity.md#addTag) | [Entity](entity.md) |
| [applyDamage](entity.md#applyDamage) | [Entity](entity.md) |
| [applyImpulse](entity.md#applyImpulse) | [Entity](entity.md) |
| [asPlayer](entity.md#asPlayer) | [Entity](entity.md) |
| [clearDynamicProperties](entity.md#clearDynamicProperties) | [Entity](entity.md) |
| [clearVelocity](entity.md#clearVelocity) | [Entity](entity.md) |
| [dimension](entity.md#dimension) | [Entity](entity.md) |
| [extinguishFire](entity.md#extinguishFire) | [Entity](entity.md) |
| [getBlockFromViewDirection](entity.md#getBlockFromViewDirection) | [Entity](entity.md) |
| [getComponent](entity.md#getComponent) | [Entity](entity.md) |
| [getComponents](entity.md#getComponents) | [Entity](entity.md) |
| [getDynamicProperty](entity.md#getDynamicProperty) | [Entity](entity.md) |
| [getDynamicPropertyIds](entity.md#getDynamicPropertyIds) | [Entity](entity.md) |
| [getDynamicPropertyTotalByteCount](entity.md#getDynamicPropertyTotalByteCount) | [Entity](entity.md) |
| [getEffect](entity.md#getEffect) | [Entity](entity.md) |
| [getEffects](entity.md#getEffects) | [Entity](entity.md) |
| [getEntitiesFromViewDirection](entity.md#getEntitiesFromViewDirection) | [Entity](entity.md) |
| [getFamilies](entity.md#getFamilies) | [Entity](entity.md) |
| [getHeadLocation](entity.md#getHeadLocation) | [Entity](entity.md) |
| [getNbt](entity.md#getNbt) | [Entity](entity.md) |
| [getProperty](entity.md#getProperty) | [Entity](entity.md) |
| [getRotation](entity.md#getRotation) | [Entity](entity.md) |
| [getTags](entity.md#getTags) | [Entity](entity.md) |
| [getTarget](entity.md#getTarget) | [Entity](entity.md) |
| [getVelocity](entity.md#getVelocity) | [Entity](entity.md) |
| [getViewDirection](entity.md#getViewDirection) | [Entity](entity.md) |
| [hasComponent](entity.md#hasComponent) | [Entity](entity.md) |
| [hasFamily](entity.md#hasFamily) | [Entity](entity.md) |
| [hasTag](entity.md#hasTag) | [Entity](entity.md) |
| [hasTarget](entity.md#hasTarget) | [Entity](entity.md) |
| [health](entity.md#health) | [Entity](entity.md) |
| [id](entity.md#id) | [Entity](entity.md) |
| [isClimbing](entity.md#isClimbing) | [Entity](entity.md) |
| [isFalling](entity.md#isFalling) | [Entity](entity.md) |
| [isInWater](entity.md#isInWater) | [Entity](entity.md) |
| [isOnGround](entity.md#isOnGround) | [Entity](entity.md) |
| [isSitting](entity.md#isSitting) | [Entity](entity.md) |
| [isSleeping](entity.md#isSleeping) | [Entity](entity.md) |
| [isSneaking](entity.md#isSneaking) | [Entity](entity.md) |
| [isSprinting](entity.md#isSprinting) | [Entity](entity.md) |
| [isSwimming](entity.md#isSwimming) | [Entity](entity.md) |
| [isValid](entity.md#isValid) | [Entity](entity.md) |
| [kill](entity.md#kill) | [Entity](entity.md) |
| [location](entity.md#location) | [Entity](entity.md) |
| [matches](entity.md#matches) | [Entity](entity.md) |
| [nameTag](entity.md#nameTag) | [Entity](entity.md) |
| [playAnimation](entity.md#playAnimation) | [Entity](entity.md) |
| [remove](entity.md#remove) | [Entity](entity.md) |
| [removeEffect](entity.md#removeEffect) | [Entity](entity.md) |
| [removeTag](entity.md#removeTag) | [Entity](entity.md) |
| [resetProperty](entity.md#resetProperty) | [Entity](entity.md) |
| [runCommand](entity.md#runCommand) | [Entity](entity.md) |
| [scoreboardIdentity](entity.md#scoreboardIdentity) | [Entity](entity.md) |
| [setDynamicProperties](entity.md#setDynamicProperties) | [Entity](entity.md) |
| [setDynamicProperty](entity.md#setDynamicProperty) | [Entity](entity.md) |
| [setOnFire](entity.md#setOnFire) | [Entity](entity.md) |
| [setProperty](entity.md#setProperty) | [Entity](entity.md) |
| [setRotation](entity.md#setRotation) | [Entity](entity.md) |
| [triggerEvent](entity.md#triggerEvent) | [Entity](entity.md) |
| [tryTeleport](entity.md#tryTeleport) | [Entity](entity.md) |
| [typeId](entity.md#typeId) | [Entity](entity.md) |

## 构造器 {#constructor}

```python
Player(playerId: str) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `playerId` | [str](../../common/type-system.md#str) | `必填` | 玩家运行 ID，不是玩家显示名称。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## name {#name}

```python
name
```

玩家名称。

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.name
```

## camera {#camera}

```python
camera: None
```

玩家的 [Camera](../../client/reference/Camera.md) 接口；当前尚无可用实现。

:::note 当前实现说明
当前服务端属性为空返回。使用客户端入口的 [client.camera](../../client/apis/manager.md#camera) 控制本机相机。
:::

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**访问：** 只读。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## isFlying {#isFlying}

```python
isFlying: bool
```

玩家是否正在飞行，例如创造或旁观模式下的飞行。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsPlayerFlying`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isFlying
```

## level {#level}

```python
level: int
```

根据经验值计算的玩家当前等级。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerLevel`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.level
```

## xpEarnedAtCurrentLevel {#xpEarnedAtCurrentLevel}

```python
xpEarnedAtCurrentLevel: int
```

读取 `xpEarnedAtCurrentLevel` 的当前值。底层调用 `GetPlayerExp`。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerExp`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.xpEarnedAtCurrentLevel
```

## getTotalXp {#getTotalXp}

```python
getTotalXp() -> int
```

读取 `getTotalXp` 操作。原生实现使用 `GetPlayerTotalExp`，行为受网易运行环境约束。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to read player experience'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerTotalExp`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getTotalXp(instance):
    return instance.getTotalXp()
```

## addExperience {#addExperience}

```python
addExperience(amount: int) -> int
```

创建或登记 `addExperience` 操作。原生实现使用 `SetPlayerTotalExp`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `amount` | [int](../../common/type-system.md#int) | `必填` | 物品数量；新物品要求 1–255 的整数，并按最大堆叠数限制。 |

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to change player experience'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetPlayerTotalExp`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addExperience(instance, amount):
    return instance.addExperience(amount)
```

## addLevels {#addLevels}

```python
addLevels(amount: int) -> int
```

创建或登记 `addLevels` 操作。原生实现使用 `AddPlayerLevel`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `amount` | [int](../../common/type-system.md#int) | `必填` | 物品数量；新物品要求 1–255 的整数，并按最大堆叠数限制。 |

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to change player level'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `AddPlayerLevel`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addLevels(instance, amount):
    return instance.addLevels(amount)
```

## resetLevel {#resetLevel}

```python
resetLevel() -> None
```

执行 `resetLevel` 操作。原生实现使用 `SetPlayerTotalExp`，行为受网易运行环境约束。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to reset player level'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetPlayerTotalExp`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_resetLevel(instance):
    return instance.resetLevel()
```

## selectedSlotIndex {#selectedSlotIndex}

```python
selectedSlotIndex
```

当前选中槽位的索引。

**访问：** 可读写。

写入方式：`instance.selectedSlotIndex = value`。参数类型线索：`(slotId: int) -> None`。

写入参数 `slotId`：[int](../../common/type-system.md#int)。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetSelectSlotId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.selectedSlotIndex

def write_value(instance, value):
    instance.selectedSlotIndex = value
```

## clientSystemInfo {#clientSystemInfo}

```python
clientSystemInfo: None
```

玩家的设备信息。

:::note 当前实现说明
当前为空返回；没有可靠的服务端同步系统信息缓存。
:::

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**访问：** 只读。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerPermissionLevel {#playerPermissionLevel}

```python
playerPermissionLevel: PlayerPermissionLevel
```

读取 `playerPermissionLevel` 的当前值。底层调用 `GetPlayerOperation`。

**访问：** 只读。

**返回类型：** [PlayerPermissionLevel](../../common/reference/PlayerPermissionLevel.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerOperation`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.playerPermissionLevel
```

## container {#container}

```python
container: con.Container
```

玩家的库存容器。

**访问：** 只读。

**返回类型：** [con.Container](container.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** [Container](container.md)。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.container
```

## mainHand {#mainHand}

```python
mainHand: ItemStack
```

读取主手物品。

**访问：** 可读写。

写入方式：`instance.mainHand = value`。参数类型线索：`(item: ItemStack) -> None`。

写入参数 `item`：[ItemStack](itemStack.md)。

**返回类型：** [ItemStack](itemStack.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.mainHand

def write_value(instance, value):
    instance.mainHand = value
```

## applyKnockback {#applyKnockback}

```python
applyKnockback(horizontalForce, verticalStrength)
```

执行 `applyKnockback` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `horizontalForce` | 由值/所属选项确定 | `必填` | 传给 [Player.applyKnockback](player.md#applyKnockback) 的 horizontalForce 参数；结合上方功能说明和下方调用示例使用。 |
| `verticalStrength` | 由值/所属选项确定 | `必填` | 传给 [Player.applyKnockback](player.md#applyKnockback) 的 verticalStrength 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_applyKnockback(instance, horizontalForce, verticalStrength):
    return instance.applyKnockback(horizontalForce, verticalStrength)
```

## playSound {#playSound}

```python
playSound(soundId: str, soundOptions: dict | PlayerSoundOptions | None = None) -> None
```

通过该在线玩家的原生命令上下文播放一次声音。选项支持位置、音量和音调；loopCount 为非零时明确拒绝。原生命令失败会抛出异常；当前后端不能返回微软的 SoundInstance 声音实例句柄。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `soundId` | [str](../../common/type-system.md#str) | `必填` | 资源包定义的声音标识，不是播放实例句柄的 id。 |
| `soundOptions` | [dict](../../common/type-system.md#dict) \| [PlayerSoundOptions](../../common/reference/PlayerSoundOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Player.playSound](player.md#playSound) 的 soundOptions 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'soundId must be a single sound definition identifier'` |
| [ValueError](../../common/type-system.md#valueerror) | `'loopCount must be an integer greater than or equal to -1'` |
| [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md) | `'The player sound backend does not support repeated playback'` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'The player is no longer connected'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetCommand`, `GetPlayerList`, `GetPos`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_playSound(instance, soundId):
    return instance.playSound(soundId)
```

## sendMessage {#sendMessage}

```python
sendMessage(message: str) -> None
```

向玩家发送消息。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `message` | [str](../../common/type-system.md#str) | `必填` | 传给 [Player.sendMessage](player.md#sendMessage) 的 message 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'Message must contain strings or RawMessage objects'` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to send raw message'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `NotifyOneMessage`, `SetCommand`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_sendMessage(instance, message):
    return instance.sendMessage(message)
```

## getSpawnPoint {#getSpawnPoint}

```python
getSpawnPoint() -> DimensionLocation | None
```

读取配置的重生位置及其维度；原生数据可用时返回。

**返回类型：** [DimensionLocation](../../common/reference/DimensionLocation.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerRespawnPos`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getSpawnPoint(instance):
    return instance.getSpawnPoint()
```

## sendToast {#sendToast}

```python
sendToast(message: str, title: str = '') -> None
```

向玩家发送弹出提示。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `message` | [str](../../common/type-system.md#str) | `必填` | 传给 [Player.sendToast](player.md#sendToast) 的 message 参数；结合上方功能说明和下方调用示例使用。 |
| `title` | [str](../../common/type-system.md#str) | `''` | 标题文本，动态表单也可接受相应 [Observable](../../ui/reference/Observable.md)。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_sendToast(instance, message):
    return instance.sendToast(message)
```

## spawnParticle {#spawnParticle}

```python
spawnParticle(effectName: str, location: Vector3, molangVariables: MolangVariableMap | None = None)
```

在世界指定位置创建粒子发射器。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `effectName` | [str](../../common/type-system.md#str) | `必填` | 资源包内存在的粒子效果标识。 |
| `location` | [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `molangVariables` | [MolangVariableMap](../reference/MolangVariableMap.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Player.spawnParticle](player.md#spawnParticle) 的 molangVariables 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_spawnParticle(instance, effectName, location):
    return instance.spawnParticle(effectName, location)
```

## showUI {#showUI}

```python
showUI(customUI)
```

当前没有功能性实现，不应依赖此成员完成操作。

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `customUI` | 由值/所属选项确定 | `必填` | 传给 [Player.showUI](player.md#showUI) 的 customUI 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## popScreen {#popScreen}

```python
popScreen()
```

当前没有功能性实现，不应依赖此成员完成操作。

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## getGameMode {#getGameMode}

```python
getGameMode() -> GameMode
```

获取玩家当前的游戏模式。

**返回类型：** [GameMode](../../common/reference/GameMode.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerGameType`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getGameMode(instance):
    return instance.getGameMode()
```

## setGameMode {#setGameMode}

```python
setGameMode(gameMode: str) -> None
```

设置 `setGameMode` 操作。原生实现使用 `SetPlayerGameType`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `gameMode` | [str](../../common/type-system.md#str) | `必填` | 传给 [Player.setGameMode](player.md#setGameMode) 的 gameMode 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown game mode: %r' % gameMode` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to set player game mode'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetPlayerGameType`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setGameMode(instance, gameMode):
    return instance.setGameMode(gameMode)
```

## teleport {#teleport}

```python
teleport(location, teleportOptions = None)
```

执行 `teleport` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | 由值/所属选项确定 | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `teleportOptions` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [Player.teleport](player.md#teleport) 的 teleportOptions 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_teleport(instance, location):
    return instance.teleport(location)
```

## 使用示例


```python
from ModSAPI.server.beta import world

for player in world.getAllPlayers():
    player.sendMessage("Hello, " + player.name)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)