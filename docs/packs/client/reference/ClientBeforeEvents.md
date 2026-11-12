---
title: "ClientBeforeEvents"
sidebar_label: "ClientBeforeEvents"
---

# ClientBeforeEvents

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/ClientEvents.py`；声明补充了静态类型信息。

待执行操作和原生输出变化的客户端同步钩子。只能修改开发包明确标记为可写的字段，且必须在回调内完成。部分操作需要客户端和服务端共同取消，具体见事件目录。此处不实现微软的受限执行阶段。

## 获取方式

从 [client.beforeEvents](../apis/manager.md#beforeEvents) 获取。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [cameraMotionStop](#cameraMotionStop) | 只读属性 |
| [chunkUnload](#chunkUnload) | 只读属性 |
| [entityInsideBlock](#entityInsideBlock) | 只读属性 |
| [entityStopRiding](#entityStopRiding) | 只读属性 |
| [extinguishFire](#extinguishFire) | 只读属性 |
| [fallOnBlockMotion](#fallOnBlockMotion) | 只读属性 |
| [fallingBlockCauseDamage](#fallingBlockCauseDamage) | 只读属性 |
| [inventoryOpen](#inventoryOpen) | 只读属性 |
| [itemReleaseUsing](#itemReleaseUsing) | 只读属性 |
| [jumpButtonPress](#jumpButtonPress) | 只读属性 |
| [playMusic](#playMusic) | 只读属性 |
| [playSound](#playSound) | 只读属性 |
| [playerBreakBlock](#playerBreakBlock) | 只读属性 |
| [playerTryAddCustomContainerItem](#playerTryAddCustomContainerItem) | 只读属性 |
| [playerTryDropItem](#playerTryDropItem) | 只读属性 |
| [playerTryPutCustomContainerItem](#playerTryPutCustomContainerItem) | 只读属性 |
| [playerTryRemoveCustomContainerItem](#playerTryRemoveCustomContainerItem) | 只读属性 |
| [scriptsUnload](#scriptsUnload) | 只读属性 |
| [shearsDestroyBlock](#shearsDestroyBlock) | 只读属性 |
| [standOnBlock](#standOnBlock) | 只读属性 |
| [startDestroyBlock](#startDestroyBlock) | 只读属性 |
| [stepOnBlock](#stepOnBlock) | 只读属性 |
| [pointerAction](#pointerAction) | 只读属性 |
| [screenClose](#screenClose) | 只读属性 |
| [itemUse](#itemUse) | 只读属性 |
| [playerUseItemOnBlock](#playerUseItemOnBlock) | 只读属性 |
| [playerInteractWithBlock](#playerInteractWithBlock) | 只读属性 |
| [getSemanticEventNames](#getSemanticEventNames) | 方法 |
| [getEventNames](#getEventNames) | 方法 |
| [getNativeEventNames](#getNativeEventNames) | 方法 |
| [getNativeEvent](#getNativeEvent) | 方法 |

## 构造器 {#constructor}

```python
ClientBeforeEvents(clientSystem)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `clientSystem` | 由值/所属选项确定 | `必填` | 传给 [ClientBeforeEvents.__init__](ClientBeforeEvents.md#constructor) 的 clientSystem 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## cameraMotionStop {#cameraMotionStop}

```python
cameraMotionStop: NativeEventSignal[ClientCameraMotionStopBeforeEvent]
```

原生事件信号：[CameraMotionStopClientEvent](../events.md#cameramotionstopclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientCameraMotionStopBeforeEvent](ClientCameraMotionStopBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## chunkUnload {#chunkUnload}

```python
chunkUnload: NativeEventSignal[ClientChunkUnloadBeforeEvent]
```

原生事件信号：[ChunkAcquireDiscardedClientEvent](../events.md#chunkacquirediscardedclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientChunkUnloadBeforeEvent](ClientChunkUnloadBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityInsideBlock {#entityInsideBlock}

```python
entityInsideBlock: NativeEventSignal[ClientEntityInsideBlockBeforeEvent]
```

原生事件信号：[OnEntityInsideBlockClientEvent](../events.md#onentityinsideblockclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientEntityInsideBlockBeforeEvent](ClientEntityInsideBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityStopRiding {#entityStopRiding}

```python
entityStopRiding: NativeEventSignal[ClientEntityStopRidingBeforeEvent]
```

原生事件信号：[EntityStopRidingEvent](../events.md#entitystopridingevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientEntityStopRidingBeforeEvent](ClientEntityStopRidingBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## extinguishFire {#extinguishFire}

```python
extinguishFire: NativeEventSignal[ClientExtinguishFireBeforeEvent]
```

原生事件信号：[ExtinguishFireClientEvent](../events.md#extinguishfireclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientExtinguishFireBeforeEvent](ClientExtinguishFireBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fallOnBlockMotion {#fallOnBlockMotion}

```python
fallOnBlockMotion: NativeEventSignal[ClientFallOnBlockMotionBeforeEvent]
```

原生事件信号：[OnAfterFallOnBlockClientEvent](../events.md#onafterfallonblockclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientFallOnBlockMotionBeforeEvent](ClientFallOnBlockMotionBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fallingBlockCauseDamage {#fallingBlockCauseDamage}

```python
fallingBlockCauseDamage: NativeEventSignal[ClientFallingBlockCauseDamageBeforeEvent]
```

原生事件信号：[FallingBlockCauseDamageBeforeClientEvent](../events.md#fallingblockcausedamagebeforeclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientFallingBlockCauseDamageBeforeEvent](ClientFallingBlockCauseDamageBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## inventoryOpen {#inventoryOpen}

```python
inventoryOpen: NativeEventSignal[ClientInventoryOpenBeforeEvent]
```

原生事件信号：[ClientPlayerInventoryOpenEvent](../events.md#clientplayerinventoryopenevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientInventoryOpenBeforeEvent](ClientInventoryOpenBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## itemReleaseUsing {#itemReleaseUsing}

```python
itemReleaseUsing: NativeEventSignal[ClientItemReleaseUsingBeforeEvent]
```

原生事件信号：[ItemReleaseUsingClientEvent](../events.md#itemreleaseusingclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientItemReleaseUsingBeforeEvent](ClientItemReleaseUsingBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## jumpButtonPress {#jumpButtonPress}

```python
jumpButtonPress: NativeEventSignal[ClientJumpButtonPressBeforeEvent]
```

原生事件信号：[ClientJumpButtonPressDownEvent](../events.md#clientjumpbuttonpressdownevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientJumpButtonPressBeforeEvent](ClientJumpButtonPressBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playMusic {#playMusic}

```python
playMusic: NativeEventSignal[ClientPlayMusicBeforeEvent]
```

原生事件信号：[PlayMusicClientEvent](../events.md#playmusicclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayMusicBeforeEvent](ClientPlayMusicBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playSound {#playSound}

```python
playSound: NativeEventSignal[ClientPlaySoundBeforeEvent]
```

原生事件信号：[PlaySoundClientEvent](../events.md#playsoundclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlaySoundBeforeEvent](ClientPlaySoundBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerBreakBlock {#playerBreakBlock}

```python
playerBreakBlock: NativeEventSignal[ClientPlayerBreakBlockBeforeEvent]
```

原生事件信号：[PlayerTryDestroyBlockClientEvent](../events.md#playertrydestroyblockclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerBreakBlockBeforeEvent](ClientPlayerBreakBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerTryAddCustomContainerItem {#playerTryAddCustomContainerItem}

```python
playerTryAddCustomContainerItem: NativeEventSignal[ClientPlayerTryAddCustomContainerItemBeforeEvent]
```

原生事件信号：[PlayerTryAddCustomContainerItemClientEvent](../events.md#playertryaddcustomcontaineritemclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerTryAddCustomContainerItemBeforeEvent](ClientPlayerTryAddCustomContainerItemBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerTryDropItem {#playerTryDropItem}

```python
playerTryDropItem: NativeEventSignal[ClientPlayerTryDropItemBeforeEvent]
```

原生事件信号：[PlayerTryDropItemClientEvent](../events.md#playertrydropitemclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerTryDropItemBeforeEvent](ClientPlayerTryDropItemBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerTryPutCustomContainerItem {#playerTryPutCustomContainerItem}

```python
playerTryPutCustomContainerItem: NativeEventSignal[ClientPlayerTryPutCustomContainerItemBeforeEvent]
```

原生事件信号：[PlayerTryPutCustomContainerItemClientEvent](../events.md#playertryputcustomcontaineritemclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerTryPutCustomContainerItemBeforeEvent](ClientPlayerTryPutCustomContainerItemBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerTryRemoveCustomContainerItem {#playerTryRemoveCustomContainerItem}

```python
playerTryRemoveCustomContainerItem: NativeEventSignal[ClientPlayerTryRemoveCustomContainerItemBeforeEvent]
```

原生事件信号：[PlayerTryRemoveCustomContainerItemClientEvent](../events.md#playertryremovecustomcontaineritemclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientPlayerTryRemoveCustomContainerItemBeforeEvent](ClientPlayerTryRemoveCustomContainerItemBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## scriptsUnload {#scriptsUnload}

```python
scriptsUnload: NativeEventSignal[ClientScriptsUnloadBeforeEvent]
```

原生事件信号：[UnLoadClientAddonScriptsBefore](../events.md#unloadclientaddonscriptsbefore)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientScriptsUnloadBeforeEvent](ClientScriptsUnloadBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## shearsDestroyBlock {#shearsDestroyBlock}

```python
shearsDestroyBlock: NativeEventSignal[ClientShearsDestroyBlockBeforeEvent]
```

原生事件信号：[ShearsDestoryBlockBeforeClientEvent](../events.md#shearsdestoryblockbeforeclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientShearsDestroyBlockBeforeEvent](ClientShearsDestroyBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## standOnBlock {#standOnBlock}

```python
standOnBlock: NativeEventSignal[ClientStandOnBlockBeforeEvent]
```

原生事件信号：[OnStandOnBlockClientEvent](../events.md#onstandonblockclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientStandOnBlockBeforeEvent](ClientStandOnBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## startDestroyBlock {#startDestroyBlock}

```python
startDestroyBlock: NativeEventSignal[ClientStartDestroyBlockBeforeEvent]
```

原生事件信号：[StartDestroyBlockClientEvent](../events.md#startdestroyblockclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientStartDestroyBlockBeforeEvent](ClientStartDestroyBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## stepOnBlock {#stepOnBlock}

```python
stepOnBlock: NativeEventSignal[ClientStepOnBlockBeforeEvent]
```

原生事件信号：[StepOnBlockClientEvent](../events.md#steponblockclientevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[ClientStepOnBlockBeforeEvent](ClientStepOnBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## pointerAction {#pointerAction}

```python
pointerAction: EventSignal[PointerActionBeforeEvent]
```

指针交互事件，支持订阅筛选。原生来源：[LeftClickBeforeClientEvent](../events.md#leftclickbeforeclientevent), [RightClickBeforeClientEvent](../events.md#rightclickbeforeclientevent), [TapBeforeClientEvent](../events.md#tapbeforeclientevent), [HoldBeforeClientEvent](../events.md#holdbeforeclientevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PointerActionBeforeEvent](../../common/reference/PointerActionBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## screenClose {#screenClose}

```python
screenClose: EventSignal[ScreenClosingEvent]
```

界面关闭事件，支持订阅筛选。原生来源：[PopScreenEvent](../events.md#popscreenevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[ScreenClosingEvent](../../common/reference/ScreenClosingEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## itemUse {#itemUse}

```python
itemUse: EventSignal[ItemUseAttemptEvent]
```

物品使用事件，支持订阅筛选。原生来源：[ClientItemTryUseEvent](../events.md#clientitemtryuseevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[ItemUseAttemptEvent](../../common/reference/ItemUseAttemptEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerUseItemOnBlock {#playerUseItemOnBlock}

```python
playerUseItemOnBlock: EventSignal[BlockInteractionEvent]
```

对方块使用物品事件，支持订阅筛选。原生来源：[ClientItemUseOnEvent](../events.md#clientitemuseonevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[BlockInteractionEvent](../../common/reference/BlockInteractionEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerInteractWithBlock {#playerInteractWithBlock}

```python
playerInteractWithBlock: EventSignal[BlockInteractionEvent]
```

方块交互事件，支持订阅筛选。原生来源：[ClientBlockUseEvent](../events.md#clientblockuseevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[BlockInteractionEvent](../../common/reference/BlockInteractionEvent.md)]。静态声明不替代本页的实现限制。

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
    # value 是上方获取方式取得的 ClientBeforeEvents 对象。
    print(value.cameraMotionStop)
    print(value.chunkUnload)
    print(value.entityInsideBlock)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)