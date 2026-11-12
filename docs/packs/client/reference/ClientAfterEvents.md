---
title: "ClientAfterEvents"
sidebar_label: "ClientAfterEvents"
---

# ClientAfterEvents

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/ClientEvents.py`；声明补充了静态类型信息。

客户端通知集合，包括有文档说明的原生后置钩子。

## 获取方式

从 [client.afterEvents](../apis/manager.md#afterEvents) 获取。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [keyPress](#keyPress) | 只读属性 |
| [mouseWheel](#mouseWheel) | 只读属性 |
| [musicStop](#musicStop) | 只读属性 |
| [uiReady](#uiReady) | 只读属性 |
| [serverEventReceive](#serverEventReceive) | 只读属性 |
| [serverRequestData](#serverRequestData) | 只读属性 |
| [achievementButtonMoved](#achievementButtonMoved) | 只读属性 |
| [actorAcquiredItem](#actorAcquiredItem) | 只读属性 |
| [actorUseItem](#actorUseItem) | 只读属性 |
| [anvilCreateResultItem](#anvilCreateResultItem) | 只读属性 |
| [approachEntity](#approachEntity) | 只读属性 |
| [attackAnimBegin](#attackAnimBegin) | 只读属性 |
| [attackAnimEnd](#attackAnimEnd) | 只读属性 |
| [backButtonRelease](#backButtonRelease) | 只读属性 |
| [blockAnimateRandomTick](#blockAnimateRandomTick) | 只读属性 |
| [cameraMotionStart](#cameraMotionStart) | 只读属性 |
| [chestClose](#chestClose) | 只读属性 |
| [chestOpen](#chestOpen) | 只读属性 |
| [chunkLoad](#chunkLoad) | 只读属性 |
| [closeNeteaseShop](#closeNeteaseShop) | 只读属性 |
| [commandOutput](#commandOutput) | 只读属性 |
| [craftUpdateResultItem](#craftUpdateResultItem) | 只读属性 |
| [customGamepadChange](#customGamepadChange) | 只读属性 |
| [customKeyChange](#customKeyChange) | 只读属性 |
| [entityCollide](#entityCollide) | 只读属性 |
| [entityHealthChanged](#entityHealthChanged) | 只读属性 |
| [entityLand](#entityLand) | 只读属性 |
| [entityModelChange](#entityModelChange) | 只读属性 |
| [gameTypeChange](#gameTypeChange) | 只读属性 |
| [gamepadControllerLayoutChange](#gamepadControllerLayoutChange) | 只读属性 |
| [getEntityByCoord](#getEntityByCoord) | 只读属性 |
| [getEntityByCoordRelease](#getEntityByCoordRelease) | 只读属性 |
| [gridComponentSizeChange](#gridComponentSizeChange) | 只读属性 |
| [grindStoneRemoveEnchant](#grindStoneRemoveEnchant) | 只读属性 |
| [gyroSensorChange](#gyroSensorChange) | 只读属性 |
| [hudButtonChange](#hudButtonChange) | 只读属性 |
| [inventoryClose](#inventoryClose) | 只读属性 |
| [itemSlotButtonClicked](#itemSlotButtonClicked) | 只读属性 |
| [jumpButtonRelease](#jumpButtonRelease) | 只读属性 |
| [keyboardControllerLayoutChange](#keyboardControllerLayoutChange) | 只读属性 |
| [leaveEntity](#leaveEntity) | 只读属性 |
| [liquidClipped](#liquidClipped) | 只读属性 |
| [localPlayerLoad](#localPlayerLoad) | 只读属性 |
| [modBlockEntityLoad](#modBlockEntityLoad) | 只读属性 |
| [modBlockEntityRemove](#modBlockEntityRemove) | 只读属性 |
| [modBlockEntityTick](#modBlockEntityTick) | 只读属性 |
| [modBlockNeteaseEffectCreate](#modBlockNeteaseEffectCreate) | 只读属性 |
| [perspectiveChange](#perspectiveChange) | 只读属性 |
| [playerAddCustomContainerItem](#playerAddCustomContainerItem) | 只读属性 |
| [playerAttackEntity](#playerAttackEntity) | 只读属性 |
| [playerChatButtonClick](#playerChatButtonClick) | 只读属性 |
| [playerDimensionChange](#playerDimensionChange) | 只读属性 |
| [playerDimensionChangeFinish](#playerDimensionChangeFinish) | 只读属性 |
| [playerEnteredView](#playerEnteredView) | 只读属性 |
| [playerHitBlock](#playerHitBlock) | 只读属性 |
| [playerJump](#playerJump) | 只读属性 |
| [playerPermissionChange](#playerPermissionChange) | 只读属性 |
| [playerRemoveCustomContainerItem](#playerRemoveCustomContainerItem) | 只读属性 |
| [playerStartMove](#playerStartMove) | 只读属性 |
| [playerStopMove](#playerStopMove) | 只读属性 |
| [recipeTrigger](#recipeTrigger) | 只读属性 |
| [render](#render) | 只读属性 |
| [screenSizeChange](#screenSizeChange) | 只读属性 |
| [scriptsLoad](#scriptsLoad) | 只读属性 |
| [startRiding](#startRiding) | 只读属性 |
| [startUsingItem](#startUsingItem) | 只读属性 |
| [stepOffBlock](#stepOffBlock) | 只读属性 |
| [stopUsingItem](#stopUsingItem) | 只读属性 |
| [tick](#tick) | 只读属性 |
| [updatePlayerSkin](#updatePlayerSkin) | 只读属性 |
| [walkAnimBegin](#walkAnimBegin) | 只读属性 |
| [walkAnimEnd](#walkAnimEnd) | 只读属性 |
| [inputButton](#inputButton) | 只读属性 |
| [inputButtonDown](#inputButtonDown) | 只读属性 |
| [inputButtonUp](#inputButtonUp) | 只读属性 |
| [customButtonInput](#customButtonInput) | 只读属性 |
| [pointerRelease](#pointerRelease) | 只读属性 |
| [inputAxis](#inputAxis) | 只读属性 |
| [inputStick](#inputStick) | 只读属性 |
| [inputTrigger](#inputTrigger) | 只读属性 |
| [playerStateChange](#playerStateChange) | 只读属性 |
| [playerSneakChange](#playerSneakChange) | 只读属性 |
| [playerSprintChange](#playerSprintChange) | 只读属性 |
| [playerGlideChange](#playerGlideChange) | 只读属性 |
| [playerSwimChange](#playerSwimChange) | 只读属性 |
| [playerCrawlChange](#playerCrawlChange) | 只读属性 |
| [playerFlyChange](#playerFlyChange) | 只读属性 |
| [playerSleepChange](#playerSleepChange) | 只读属性 |
| [playerSpinAttackChange](#playerSpinAttackChange) | 只读属性 |
| [entityLoad](#entityLoad) | 只读属性 |
| [entityRemove](#entityRemove) | 只读属性 |
| [screenStackChange](#screenStackChange) | 只读属性 |
| [playerInventoryItemChange](#playerInventoryItemChange) | 只读属性 |
| [physicsContactBegin](#physicsContactBegin) | 只读属性 |
| [physicsContactEnd](#physicsContactEnd) | 只读属性 |
| [physicsTriggerEnter](#physicsTriggerEnter) | 只读属性 |
| [physicsTriggerLeave](#physicsTriggerLeave) | 只读属性 |
| [getSemanticEventNames](#getSemanticEventNames) | 方法 |
| [getEventNames](#getEventNames) | 方法 |
| [getNativeEventNames](#getNativeEventNames) | 方法 |
| [getNativeEvent](#getNativeEvent) | 方法 |

## 构造器 {#constructor}

```python
ClientAfterEvents(clientSystem)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `clientSystem` | 由值/所属选项确定 | `必填` | 传给 [ClientAfterEvents.__init__](ClientAfterEvents.md#constructor) 的 clientSystem 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## keyPress {#keyPress}

```python
keyPress: ClientEventSignal[ClientKeyPressAfterEvent]
```

键盘按下和释放快照；原生键码为整数。

**访问：** 只读。

**返回类型：** [ClientEventSignal](ClientEventSignal.md)[[ClientKeyPressAfterEvent](ClientKeyPressAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.keyPress
```

## mouseWheel {#mouseWheel}

```python
mouseWheel: ClientEventSignal[ClientMouseWheelAfterEvent]
```

鼠标滚轮通知，方向为 +1 或 -1。

**访问：** 只读。

**返回类型：** [ClientEventSignal](ClientEventSignal.md)[[ClientMouseWheelAfterEvent](ClientMouseWheelAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.mouseWheel
```

## musicStop {#musicStop}

```python
musicStop: ClientEventSignal[ClientMusicStopAfterEvent]
```

原生音乐停止通知，携带声音资源标识。

**访问：** 只读。

**返回类型：** [ClientEventSignal](ClientEventSignal.md)[[ClientMusicStopAfterEvent](ClientMusicStopAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.musicStop
```

## uiReady {#uiReady}

```python
uiReady: ClientEventSignal[ClientUiReadyAfterEvent]
```

界面就绪通知，包括维度切换后的重新初始化。

:::note 当前实现说明
可能在维度切换后再次触发，不是只触发一次的事件。
:::

**访问：** 只读。

**返回类型：** [ClientEventSignal](ClientEventSignal.md)[[ClientUiReadyAfterEvent](ClientUiReadyAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.uiReady
```

## serverEventReceive {#serverEventReceive}

```python
serverEventReceive: ServerEventReceiveAfterEventSignal
```

服务端向客户端发送数据时触发。

**访问：** 只读。

**返回类型：** [ServerEventReceiveAfterEventSignal](ServerEventReceiveAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.serverEventReceive
```

## serverRequestData {#serverRequestData}

```python
serverRequestData: ServerRequestDataAfterEventSignal
```

服务端向客户端发送数据并请求响应时触发。

**访问：** 只读。

**返回类型：** [ServerRequestDataAfterEventSignal](ServerRequestDataAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.serverRequestData
```

## achievementButtonMoved {#achievementButtonMoved}

```python
achievementButtonMoved: NativeEventSignal[ClientAchievementButtonMovedAfterEvent]
```

原生事件信号：[AchievementButtonMovedClientEvent](../events.md#achievementbuttonmovedclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientAchievementButtonMovedAfterEvent](ClientAchievementButtonMovedAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## actorAcquiredItem {#actorAcquiredItem}

```python
actorAcquiredItem: NativeEventSignal[ClientActorAcquiredItemAfterEvent]
```

原生事件信号：[ActorAcquiredItemClientEvent](../events.md#actoracquireditemclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientActorAcquiredItemAfterEvent](ClientActorAcquiredItemAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## actorUseItem {#actorUseItem}

```python
actorUseItem: NativeEventSignal[ClientActorUseItemAfterEvent]
```

原生事件信号：[ActorUseItemClientEvent](../events.md#actoruseitemclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientActorUseItemAfterEvent](ClientActorUseItemAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## anvilCreateResultItem {#anvilCreateResultItem}

```python
anvilCreateResultItem: NativeEventSignal[ClientAnvilCreateResultItemAfterEvent]
```

原生事件信号：[AnvilCreateResultItemAfterClientEvent](../events.md#anvilcreateresultitemafterclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientAnvilCreateResultItemAfterEvent](ClientAnvilCreateResultItemAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## approachEntity {#approachEntity}

```python
approachEntity: NativeEventSignal[ClientApproachEntityAfterEvent]
```

原生事件信号：[ApproachEntityClientEvent](../events.md#approachentityclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientApproachEntityAfterEvent](ClientApproachEntityAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## attackAnimBegin {#attackAnimBegin}

```python
attackAnimBegin: NativeEventSignal[ClientAttackAnimBeginAfterEvent]
```

原生事件信号：[AttackAnimBeginClientEvent](../events.md#attackanimbeginclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientAttackAnimBeginAfterEvent](ClientAttackAnimBeginAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## attackAnimEnd {#attackAnimEnd}

```python
attackAnimEnd: NativeEventSignal[ClientAttackAnimEndAfterEvent]
```

原生事件信号：[AttackAnimEndClientEvent](../events.md#attackanimendclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientAttackAnimEndAfterEvent](ClientAttackAnimEndAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## backButtonRelease {#backButtonRelease}

```python
backButtonRelease: NativeEventSignal[ClientBackButtonReleaseAfterEvent]
```

原生事件信号：[OnBackButtonReleaseClientEvent](../events.md#onbackbuttonreleaseclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientBackButtonReleaseAfterEvent](ClientBackButtonReleaseAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockAnimateRandomTick {#blockAnimateRandomTick}

```python
blockAnimateRandomTick: NativeEventSignal[ClientBlockAnimateRandomTickAfterEvent]
```

原生事件信号：[BlockAnimateRandomTickEvent](../events.md#blockanimaterandomtickevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientBlockAnimateRandomTickAfterEvent](ClientBlockAnimateRandomTickAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## cameraMotionStart {#cameraMotionStart}

```python
cameraMotionStart: NativeEventSignal[ClientCameraMotionStartAfterEvent]
```

原生事件信号：[CameraMotionStartClientEvent](../events.md#cameramotionstartclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientCameraMotionStartAfterEvent](ClientCameraMotionStartAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## chestClose {#chestClose}

```python
chestClose: NativeEventSignal[ClientChestCloseAfterEvent]
```

原生事件信号：[ClientChestCloseEvent](../events.md#clientchestcloseevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientChestCloseAfterEvent](ClientChestCloseAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## chestOpen {#chestOpen}

```python
chestOpen: NativeEventSignal[ClientChestOpenAfterEvent]
```

原生事件信号：[ClientChestOpenEvent](../events.md#clientchestopenevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientChestOpenAfterEvent](ClientChestOpenAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## chunkLoad {#chunkLoad}

```python
chunkLoad: NativeEventSignal[ClientChunkLoadAfterEvent]
```

原生事件信号：[ChunkLoadedClientEvent](../events.md#chunkloadedclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientChunkLoadAfterEvent](ClientChunkLoadAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## closeNeteaseShop {#closeNeteaseShop}

```python
closeNeteaseShop: NativeEventSignal[ClientCloseNeteaseShopAfterEvent]
```

原生事件信号：[CloseNeteaseShopEvent](../events.md#closeneteaseshopevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientCloseNeteaseShopAfterEvent](ClientCloseNeteaseShopAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## commandOutput {#commandOutput}

```python
commandOutput: NativeEventSignal[ClientCommandOutputAfterEvent]
```

原生事件信号：[OnCommandOutputClientEvent](../events.md#oncommandoutputclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientCommandOutputAfterEvent](ClientCommandOutputAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## craftUpdateResultItem {#craftUpdateResultItem}

```python
craftUpdateResultItem: NativeEventSignal[ClientCraftUpdateResultItemAfterEvent]
```

原生事件信号：[CraftUpdateResultItemClientEvent](../events.md#craftupdateresultitemclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientCraftUpdateResultItemAfterEvent](ClientCraftUpdateResultItemAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## customGamepadChange {#customGamepadChange}

```python
customGamepadChange: NativeEventSignal[ClientCustomGamepadChangeAfterEvent]
```

原生事件信号：[OnCustomGamepadChangedEvent](../events.md#oncustomgamepadchangedevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientCustomGamepadChangeAfterEvent](ClientCustomGamepadChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## customKeyChange {#customKeyChange}

```python
customKeyChange: NativeEventSignal[ClientCustomKeyChangeAfterEvent]
```

原生事件信号：[OnCustomKeyChangedEvent](../events.md#oncustomkeychangedevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientCustomKeyChangeAfterEvent](ClientCustomKeyChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityCollide {#entityCollide}

```python
entityCollide: NativeEventSignal[ClientEntityCollideAfterEvent]
```

原生事件信号：[OnMobHitMobClientEvent](../events.md#onmobhitmobclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientEntityCollideAfterEvent](ClientEntityCollideAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityHealthChanged {#entityHealthChanged}

```python
entityHealthChanged: NativeEventSignal[ClientEntityHealthChangedAfterEvent]
```

原生事件信号：[HealthChangeClientEvent](../events.md#healthchangeclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientEntityHealthChangedAfterEvent](ClientEntityHealthChangedAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityLand {#entityLand}

```python
entityLand: NativeEventSignal[ClientEntityLandAfterEvent]
```

原生事件信号：[OnGroundClientEvent](../events.md#ongroundclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientEntityLandAfterEvent](ClientEntityLandAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityModelChange {#entityModelChange}

```python
entityModelChange: NativeEventSignal[ClientEntityModelChangeAfterEvent]
```

原生事件信号：[EntityModelChangedClientEvent](../events.md#entitymodelchangedclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientEntityModelChangeAfterEvent](ClientEntityModelChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## gameTypeChange {#gameTypeChange}

```python
gameTypeChange: NativeEventSignal[ClientGameTypeChangeAfterEvent]
```

原生事件信号：[GameTypeChangedClientEvent](../events.md#gametypechangedclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientGameTypeChangeAfterEvent](ClientGameTypeChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## gamepadControllerLayoutChange {#gamepadControllerLayoutChange}

```python
gamepadControllerLayoutChange: NativeEventSignal[ClientGamepadControllerLayoutChangeAfterEvent]
```

原生事件信号：[OnGamepadControllerLayoutChangeClientEvent](../events.md#ongamepadcontrollerlayoutchangeclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientGamepadControllerLayoutChangeAfterEvent](ClientGamepadControllerLayoutChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## getEntityByCoord {#getEntityByCoord}

```python
getEntityByCoord: NativeEventSignal[ClientGetEntityByCoordAfterEvent]
```

原生事件信号：[GetEntityByCoordEvent](../events.md#getentitybycoordevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientGetEntityByCoordAfterEvent](ClientGetEntityByCoordAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## getEntityByCoordRelease {#getEntityByCoordRelease}

```python
getEntityByCoordRelease: NativeEventSignal[ClientGetEntityByCoordReleaseAfterEvent]
```

原生事件信号：[GetEntityByCoordReleaseClientEvent](../events.md#getentitybycoordreleaseclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientGetEntityByCoordReleaseAfterEvent](ClientGetEntityByCoordReleaseAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## gridComponentSizeChange {#gridComponentSizeChange}

```python
gridComponentSizeChange: NativeEventSignal[ClientGridComponentSizeChangeAfterEvent]
```

原生事件信号：[GridComponentSizeChangedClientEvent](../events.md#gridcomponentsizechangedclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientGridComponentSizeChangeAfterEvent](ClientGridComponentSizeChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## grindStoneRemoveEnchant {#grindStoneRemoveEnchant}

```python
grindStoneRemoveEnchant: NativeEventSignal[ClientGrindStoneRemoveEnchantAfterEvent]
```

原生事件信号：[GrindStoneRemovedEnchantClientEvent](../events.md#grindstoneremovedenchantclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientGrindStoneRemoveEnchantAfterEvent](ClientGrindStoneRemoveEnchantAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## gyroSensorChange {#gyroSensorChange}

```python
gyroSensorChange: NativeEventSignal[ClientGyroSensorChangeAfterEvent]
```

原生事件信号：[GyroSensorChangedClientEvent](../events.md#gyrosensorchangedclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientGyroSensorChangeAfterEvent](ClientGyroSensorChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## hudButtonChange {#hudButtonChange}

```python
hudButtonChange: NativeEventSignal[ClientHudButtonChangeAfterEvent]
```

原生事件信号：[HudButtonChangedClientEvent](../events.md#hudbuttonchangedclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientHudButtonChangeAfterEvent](ClientHudButtonChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## inventoryClose {#inventoryClose}

```python
inventoryClose: NativeEventSignal[ClientInventoryCloseAfterEvent]
```

原生事件信号：[ClientPlayerInventoryCloseEvent](../events.md#clientplayerinventorycloseevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientInventoryCloseAfterEvent](ClientInventoryCloseAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## itemSlotButtonClicked {#itemSlotButtonClicked}

```python
itemSlotButtonClicked: NativeEventSignal[ClientItemSlotButtonClickedAfterEvent]
```

原生事件信号：[OnItemSlotButtonClickedEvent](../events.md#onitemslotbuttonclickedevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientItemSlotButtonClickedAfterEvent](ClientItemSlotButtonClickedAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## jumpButtonRelease {#jumpButtonRelease}

```python
jumpButtonRelease: NativeEventSignal[ClientJumpButtonReleaseAfterEvent]
```

原生事件信号：[ClientJumpButtonReleaseEvent](../events.md#clientjumpbuttonreleaseevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientJumpButtonReleaseAfterEvent](ClientJumpButtonReleaseAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## keyboardControllerLayoutChange {#keyboardControllerLayoutChange}

```python
keyboardControllerLayoutChange: NativeEventSignal[ClientKeyboardControllerLayoutChangeAfterEvent]
```

原生事件信号：[OnKeyboardControllerLayoutChangeClientEvent](../events.md#onkeyboardcontrollerlayoutchangeclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientKeyboardControllerLayoutChangeAfterEvent](ClientKeyboardControllerLayoutChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## leaveEntity {#leaveEntity}

```python
leaveEntity: NativeEventSignal[ClientLeaveEntityAfterEvent]
```

原生事件信号：[LeaveEntityClientEvent](../events.md#leaveentityclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientLeaveEntityAfterEvent](ClientLeaveEntityAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## liquidClipped {#liquidClipped}

```python
liquidClipped: NativeEventSignal[ClientLiquidClippedAfterEvent]
```

原生事件信号：[LiquidClippedClientEvent](../events.md#liquidclippedclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientLiquidClippedAfterEvent](ClientLiquidClippedAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## localPlayerLoad {#localPlayerLoad}

```python
localPlayerLoad: NativeEventSignal[ClientLocalPlayerLoadAfterEvent]
```

原生事件信号：[OnLocalPlayerStopLoading](../events.md#onlocalplayerstoploading)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientLocalPlayerLoadAfterEvent](ClientLocalPlayerLoadAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## modBlockEntityLoad {#modBlockEntityLoad}

```python
modBlockEntityLoad: NativeEventSignal[ClientModBlockEntityLoadAfterEvent]
```

原生事件信号：[ModBlockEntityLoadedClientEvent](../events.md#modblockentityloadedclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientModBlockEntityLoadAfterEvent](ClientModBlockEntityLoadAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## modBlockEntityRemove {#modBlockEntityRemove}

```python
modBlockEntityRemove: NativeEventSignal[ClientModBlockEntityRemoveAfterEvent]
```

原生事件信号：[ModBlockEntityRemoveClientEvent](../events.md#modblockentityremoveclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientModBlockEntityRemoveAfterEvent](ClientModBlockEntityRemoveAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## modBlockEntityTick {#modBlockEntityTick}

```python
modBlockEntityTick: NativeEventSignal[ClientModBlockEntityTickAfterEvent]
```

原生事件信号：[ModBlockEntityTickClientEvent](../events.md#modblockentitytickclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientModBlockEntityTickAfterEvent](ClientModBlockEntityTickAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## modBlockNeteaseEffectCreate {#modBlockNeteaseEffectCreate}

```python
modBlockNeteaseEffectCreate: NativeEventSignal[ClientModBlockNeteaseEffectCreateAfterEvent]
```

原生事件信号：[OnModBlockNeteaseEffectCreatedClientEvent](../events.md#onmodblockneteaseeffectcreatedclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientModBlockNeteaseEffectCreateAfterEvent](ClientModBlockNeteaseEffectCreateAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## perspectiveChange {#perspectiveChange}

```python
perspectiveChange: NativeEventSignal[ClientPerspectiveChangeAfterEvent]
```

原生事件信号：[PerspChangeClientEvent](../events.md#perspchangeclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPerspectiveChangeAfterEvent](ClientPerspectiveChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerAddCustomContainerItem {#playerAddCustomContainerItem}

```python
playerAddCustomContainerItem: NativeEventSignal[ClientPlayerAddCustomContainerItemAfterEvent]
```

原生事件信号：[PlayerAddCustomContainerItemClientEvent](../events.md#playeraddcustomcontaineritemclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerAddCustomContainerItemAfterEvent](ClientPlayerAddCustomContainerItemAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerAttackEntity {#playerAttackEntity}

```python
playerAttackEntity: NativeEventSignal[ClientPlayerAttackEntityAfterEvent]
```

原生事件信号：[PlayerAttackEntityEvent](../events.md#playerattackentityevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerAttackEntityAfterEvent](ClientPlayerAttackEntityAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerChatButtonClick {#playerChatButtonClick}

```python
playerChatButtonClick: NativeEventSignal[ClientPlayerChatButtonClickAfterEvent]
```

原生事件信号：[PlayerChatButtonClickClientEvent](../events.md#playerchatbuttonclickclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerChatButtonClickAfterEvent](ClientPlayerChatButtonClickAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerDimensionChange {#playerDimensionChange}

```python
playerDimensionChange: NativeEventSignal[ClientPlayerDimensionChangeAfterEvent]
```

原生事件信号：[DimensionChangeClientEvent](../events.md#dimensionchangeclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerDimensionChangeAfterEvent](ClientPlayerDimensionChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerDimensionChangeFinish {#playerDimensionChangeFinish}

```python
playerDimensionChangeFinish: NativeEventSignal[ClientPlayerDimensionChangeFinishAfterEvent]
```

原生事件信号：[DimensionChangeFinishClientEvent](../events.md#dimensionchangefinishclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerDimensionChangeFinishAfterEvent](ClientPlayerDimensionChangeFinishAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerEnteredView {#playerEnteredView}

```python
playerEnteredView: NativeEventSignal[ClientPlayerEnteredViewAfterEvent]
```

原生事件信号：[AddPlayerAOIClientEvent](../events.md#addplayeraoiclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerEnteredViewAfterEvent](ClientPlayerEnteredViewAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerHitBlock {#playerHitBlock}

```python
playerHitBlock: NativeEventSignal[ClientPlayerHitBlockAfterEvent]
```

原生事件信号：[OnPlayerHitBlockClientEvent](../events.md#onplayerhitblockclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerHitBlockAfterEvent](ClientPlayerHitBlockAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerJump {#playerJump}

```python
playerJump: NativeEventSignal[ClientPlayerJumpAfterEvent]
```

原生事件信号：[OnLocalPlayerStartJumpClientEvent](../events.md#onlocalplayerstartjumpclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerJumpAfterEvent](ClientPlayerJumpAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerPermissionChange {#playerPermissionChange}

```python
playerPermissionChange: NativeEventSignal[ClientPlayerPermissionChangeAfterEvent]
```

原生事件信号：[PlayerPermissionChangeClientEvent](../events.md#playerpermissionchangeclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerPermissionChangeAfterEvent](ClientPlayerPermissionChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerRemoveCustomContainerItem {#playerRemoveCustomContainerItem}

```python
playerRemoveCustomContainerItem: NativeEventSignal[ClientPlayerRemoveCustomContainerItemAfterEvent]
```

原生事件信号：[PlayerRemoveCustomContainerItemClientEvent](../events.md#playerremovecustomcontaineritemclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerRemoveCustomContainerItemAfterEvent](ClientPlayerRemoveCustomContainerItemAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerStartMove {#playerStartMove}

```python
playerStartMove: NativeEventSignal[ClientPlayerStartMoveAfterEvent]
```

原生事件信号：[OnClientPlayerStartMove](../events.md#onclientplayerstartmove)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerStartMoveAfterEvent](ClientPlayerStartMoveAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerStopMove {#playerStopMove}

```python
playerStopMove: NativeEventSignal[ClientPlayerStopMoveAfterEvent]
```

原生事件信号：[OnClientPlayerStopMove](../events.md#onclientplayerstopmove)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerStopMoveAfterEvent](ClientPlayerStopMoveAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## recipeTrigger {#recipeTrigger}

```python
recipeTrigger: NativeEventSignal[ClientRecipeTriggerAfterEvent]
```

原生事件信号：[ClientShapedRecipeTriggeredEvent](../events.md#clientshapedrecipetriggeredevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientRecipeTriggerAfterEvent](ClientRecipeTriggerAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## render {#render}

```python
render: NativeEventSignal[ClientRenderAfterEvent]
```

原生事件信号：[GameRenderTickEvent](../events.md#gamerendertickevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientRenderAfterEvent](ClientRenderAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## screenSizeChange {#screenSizeChange}

```python
screenSizeChange: NativeEventSignal[ClientScreenSizeChangeAfterEvent]
```

原生事件信号：[ScreenSizeChangedClientEvent](../events.md#screensizechangedclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientScreenSizeChangeAfterEvent](ClientScreenSizeChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## scriptsLoad {#scriptsLoad}

```python
scriptsLoad: NativeEventSignal[ClientScriptsLoadAfterEvent]
```

原生事件信号：[LoadClientAddonScriptsAfter](../events.md#loadclientaddonscriptsafter)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientScriptsLoadAfterEvent](ClientScriptsLoadAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## startRiding {#startRiding}

```python
startRiding: NativeEventSignal[ClientStartRidingAfterEvent]
```

原生事件信号：[StartRidingClientEvent](../events.md#startridingclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientStartRidingAfterEvent](ClientStartRidingAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## startUsingItem {#startUsingItem}

```python
startUsingItem: NativeEventSignal[ClientStartUsingItemAfterEvent]
```

原生事件信号：[StartUsingItemClientEvent](../events.md#startusingitemclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientStartUsingItemAfterEvent](ClientStartUsingItemAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## stepOffBlock {#stepOffBlock}

```python
stepOffBlock: NativeEventSignal[ClientStepOffBlockAfterEvent]
```

原生事件信号：[StepOffBlockClientEvent](../events.md#stepoffblockclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientStepOffBlockAfterEvent](ClientStepOffBlockAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## stopUsingItem {#stopUsingItem}

```python
stopUsingItem: NativeEventSignal[ClientStopUsingItemAfterEvent]
```

原生事件信号：[StopUsingItemClientEvent](../events.md#stopusingitemclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientStopUsingItemAfterEvent](ClientStopUsingItemAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## tick {#tick}

```python
tick: NativeEventSignal[ClientTickAfterEvent]
```

原生事件信号：[OnScriptTickClient](../events.md#onscripttickclient)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientTickAfterEvent](ClientTickAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## updatePlayerSkin {#updatePlayerSkin}

```python
updatePlayerSkin: NativeEventSignal[ClientUpdatePlayerSkinAfterEvent]
```

原生事件信号：[UpdatePlayerSkinClientEvent](../events.md#updateplayerskinclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientUpdatePlayerSkinAfterEvent](ClientUpdatePlayerSkinAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## walkAnimBegin {#walkAnimBegin}

```python
walkAnimBegin: NativeEventSignal[ClientWalkAnimBeginAfterEvent]
```

原生事件信号：[WalkAnimBeginClientEvent](../events.md#walkanimbeginclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientWalkAnimBeginAfterEvent](ClientWalkAnimBeginAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## walkAnimEnd {#walkAnimEnd}

```python
walkAnimEnd: NativeEventSignal[ClientWalkAnimEndAfterEvent]
```

原生事件信号：[WalkAnimEndClientEvent](../events.md#walkanimendclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientWalkAnimEndAfterEvent](ClientWalkAnimEndAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## inputButton {#inputButton}

```python
inputButton: EventSignal[InputButtonEvent]
```

按键输入事件，支持订阅筛选。原生来源：[OnKeyPressInGame](../events.md#onkeypressingame), [OnGamepadKeyPressClientEvent](../events.md#ongamepadkeypressclientevent), [OnCustomKeyPressInGame](../events.md#oncustomkeypressingame), [OnCustomGamepadPressInGame](../events.md#oncustomgamepadpressingame), [OnMouseMiddleDownClientEvent](../events.md#onmousemiddledownclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[InputButtonEvent](../../common/reference/InputButtonEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## inputButtonDown {#inputButtonDown}

```python
inputButtonDown: EventSignal[InputButtonEvent]
```

按键输入事件，支持订阅筛选。原生来源：[OnKeyPressInGame](../events.md#onkeypressingame), [OnGamepadKeyPressClientEvent](../events.md#ongamepadkeypressclientevent), [OnCustomKeyPressInGame](../events.md#oncustomkeypressingame), [OnCustomGamepadPressInGame](../events.md#oncustomgamepadpressingame), [OnMouseMiddleDownClientEvent](../events.md#onmousemiddledownclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[InputButtonEvent](../../common/reference/InputButtonEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## inputButtonUp {#inputButtonUp}

```python
inputButtonUp: EventSignal[InputButtonEvent]
```

按键输入事件，支持订阅筛选。原生来源：[OnKeyPressInGame](../events.md#onkeypressingame), [OnGamepadKeyPressClientEvent](../events.md#ongamepadkeypressclientevent), [OnCustomKeyPressInGame](../events.md#oncustomkeypressingame), [OnCustomGamepadPressInGame](../events.md#oncustomgamepadpressingame), [OnMouseMiddleDownClientEvent](../events.md#onmousemiddledownclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[InputButtonEvent](../../common/reference/InputButtonEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## customButtonInput {#customButtonInput}

```python
customButtonInput: EventSignal[InputButtonEvent]
```

按键输入事件，支持订阅筛选。原生来源：[OnCustomKeyPressInGame](../events.md#oncustomkeypressingame), [OnCustomGamepadPressInGame](../events.md#oncustomgamepadpressingame)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[InputButtonEvent](../../common/reference/InputButtonEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## pointerRelease {#pointerRelease}

```python
pointerRelease: EventSignal[PointerReleaseEvent]
```

指针交互事件，支持订阅筛选。原生来源：[LeftClickReleaseClientEvent](../events.md#leftclickreleaseclientevent), [RightClickReleaseClientEvent](../events.md#rightclickreleaseclientevent), [TapOrHoldReleaseClientEvent](../events.md#taporholdreleaseclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PointerReleaseEvent](../../common/reference/PointerReleaseEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## inputAxis {#inputAxis}

```python
inputAxis: EventSignal[InputAxisEvent]
```

手柄轴输入事件，支持订阅筛选。原生来源：[OnGamepadStickClientEvent](../events.md#ongamepadstickclientevent), [OnGamepadTriggerClientEvent](../events.md#ongamepadtriggerclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[InputAxisEvent](../../common/reference/InputAxisEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## inputStick {#inputStick}

```python
inputStick: EventSignal[InputAxisEvent]
```

手柄轴输入事件，支持订阅筛选。原生来源：[OnGamepadStickClientEvent](../events.md#ongamepadstickclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[InputAxisEvent](../../common/reference/InputAxisEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## inputTrigger {#inputTrigger}

```python
inputTrigger: EventSignal[InputAxisEvent]
```

手柄轴输入事件，支持订阅筛选。原生来源：[OnGamepadTriggerClientEvent](../events.md#ongamepadtriggerclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[InputAxisEvent](../../common/reference/InputAxisEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerStateChange {#playerStateChange}

```python
playerStateChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnLocalPlayerActionClientEvent](../events.md#onlocalplayeractionclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerSneakChange {#playerSneakChange}

```python
playerSneakChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnLocalPlayerActionClientEvent](../events.md#onlocalplayeractionclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerSprintChange {#playerSprintChange}

```python
playerSprintChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnLocalPlayerActionClientEvent](../events.md#onlocalplayeractionclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerGlideChange {#playerGlideChange}

```python
playerGlideChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnLocalPlayerActionClientEvent](../events.md#onlocalplayeractionclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerSwimChange {#playerSwimChange}

```python
playerSwimChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnLocalPlayerActionClientEvent](../events.md#onlocalplayeractionclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerCrawlChange {#playerCrawlChange}

```python
playerCrawlChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnLocalPlayerActionClientEvent](../events.md#onlocalplayeractionclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerFlyChange {#playerFlyChange}

```python
playerFlyChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnLocalPlayerActionClientEvent](../events.md#onlocalplayeractionclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerSleepChange {#playerSleepChange}

```python
playerSleepChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnLocalPlayerActionClientEvent](../events.md#onlocalplayeractionclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerSpinAttackChange {#playerSpinAttackChange}

```python
playerSpinAttackChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnLocalPlayerActionClientEvent](../events.md#onlocalplayeractionclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityLoad {#entityLoad}

```python
entityLoad: EventSignal[EntityPresenceEvent]
```

实体可见性事件，支持订阅筛选。原生来源：[AddEntityClientEvent](../events.md#addentityclientevent), [AddPlayerCreatedClientEvent](../events.md#addplayercreatedclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[EntityPresenceEvent](../../common/reference/EntityPresenceEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityRemove {#entityRemove}

```python
entityRemove: EventSignal[EntityPresenceEvent]
```

实体可见性事件，支持订阅筛选。原生来源：[RemoveEntityClientEvent](../events.md#removeentityclientevent), [RemovePlayerAOIClientEvent](../events.md#removeplayeraoiclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[EntityPresenceEvent](../../common/reference/EntityPresenceEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## screenStackChange {#screenStackChange}

```python
screenStackChange: EventSignal[ScreenStackChangeEvent]
```

界面栈变化事件，支持订阅筛选。原生来源：[PushScreenEvent](../events.md#pushscreenevent), [PopScreenAfterClientEvent](../events.md#popscreenafterclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[ScreenStackChangeEvent](../../common/reference/ScreenStackChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerInventoryItemChange {#playerInventoryItemChange}

```python
playerInventoryItemChange: EventSignal[InventoryChangeEvent]
```

库存变化事件，支持订阅筛选。原生来源：[InventoryItemChangedClientEvent](../events.md#inventoryitemchangedclientevent), [OnCarriedNewItemChangedClientEvent](../events.md#oncarriednewitemchangedclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[InventoryChangeEvent](../../common/reference/InventoryChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## physicsContactBegin {#physicsContactBegin}

```python
physicsContactBegin: EventSignal[PhysicsContactEvent]
```

物理接触事件，支持订阅筛选。原生来源：[PhysxTouchClientEvent](../events.md#physxtouchclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PhysicsContactEvent](../../common/reference/PhysicsContactEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## physicsContactEnd {#physicsContactEnd}

```python
physicsContactEnd: EventSignal[PhysicsContactEvent]
```

物理接触事件，支持订阅筛选。原生来源：[PhysxTouchClientEvent](../events.md#physxtouchclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PhysicsContactEvent](../../common/reference/PhysicsContactEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## physicsTriggerEnter {#physicsTriggerEnter}

```python
physicsTriggerEnter: EventSignal[PhysicsContactEvent]
```

物理接触事件，支持订阅筛选。原生来源：[PhysxTriggerClientEvent](../events.md#physxtriggerclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PhysicsContactEvent](../../common/reference/PhysicsContactEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## physicsTriggerLeave {#physicsTriggerLeave}

```python
physicsTriggerLeave: EventSignal[PhysicsContactEvent]
```

物理接触事件，支持订阅筛选。原生来源：[PhysxTriggerClientEvent](../events.md#physxtriggerclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PhysicsContactEvent](../../common/reference/PhysicsContactEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## getSemanticEventNames {#getSemanticEventNames}

```python
getSemanticEventNames() -> tuple[str, ...]
```

列出便捷的合并或拆分事件名称，不分配监听器。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[str](../../common/type-system.md#str), ...]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getSemanticEventNames(instance):
    return instance.getSemanticEventNames()
```

## getEventNames {#getEventNames}

```python
getEventNames() -> tuple[str, ...]
```

返回排序后的原生事件属性名称，不创建监听器。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[str](../../common/type-system.md#str), ...]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEventNames(instance):
    return instance.getEventNames()
```

## getNativeEventNames {#getNativeEventNames}

```python
getNativeEventNames() -> tuple[str, ...]
```

返回当前执行端和钩子集合支持的准确原生事件名。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[str](../../common/type-system.md#str), ...]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getNativeEventNames(instance):
    return instance.getNativeEventNames()
```

## getNativeEvent {#getNativeEvent}

```python
getNativeEvent(eventName: str) -> NativeEventSignal[NativeEventData]
```

按准确原生名称返回缓存的信号。名称未知、执行端或钩子阶段不符时抛出 [KeyError](../../common/type-system.md#keyerror)；名称参数不合法时抛出 [TypeError](../../common/type-system.md#typeerror) 或 [ValueError](../../common/type-system.md#valueerror)；对象已释放时抛出 [InvalidClientObjectError](../../common/reference/InvalidClientObjectError.md)。引擎和平台的前置条件仍然适用。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `eventName` | [str](../../common/type-system.md#str) | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[NativeEventData](../../common/reference/NativeEventData.md)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [KeyError](../../common/type-system.md#keyerror) | `eventName` |
| [InvalidClientObjectError](../../common/reference/InvalidClientObjectError.md) | `'Native event collection has been disposed'` |
| [InvalidClientObjectError](../../common/reference/InvalidClientObjectError.md) | `'The world event owner is unavailable'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getNativeEvent(instance, eventName):
    return instance.getNativeEvent(eventName)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientAfterEvents 对象。
    print(value.keyPress)
    print(value.mouseWheel)
    print(value.musicStop)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)