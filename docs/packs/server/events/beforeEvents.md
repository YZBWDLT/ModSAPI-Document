---
title: "WorldBeforeEvents"
sidebar_label: "WorldBeforeEvents"
---

# WorldBeforeEvents

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/WorldEvents.py`；声明补充了静态类型信息。

实际操作发生前的事件集合，多数情况下可取消或修改即将发生的操作。原生钩子同步执行，只有文档规定的输出可写，且须在回调内完成。开发包不实行微软的受限执行阶段；原生前置条件仍然适用。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [chatSend](#chatSend) | 只读属性 |
| [entityHurt](#entityHurt) | 只读属性 |
| [explosion](#explosion) | 只读属性 |
| [playerInteractWithEntity](#playerInteractWithEntity) | 只读属性 |
| [playerBreakBlock](#playerBreakBlock) | 只读属性 |
| [actorUseItem](#actorUseItem) | 只读属性 |
| [actuallyHurt](#actuallyHurt) | 只读属性 |
| [blockLiquidStateChange](#blockLiquidStateChange) | 只读属性 |
| [blockPattern](#blockPattern) | 只读属性 |
| [blockSnowStateChange](#blockSnowStateChange) | 只读属性 |
| [changeLevelUpCost](#changeLevelUpCost) | 只读属性 |
| [chestBlockTryPairWith](#chestBlockTryPairWith) | 只读属性 |
| [chunkUnload](#chunkUnload) | 只读属性 |
| [command](#command) | 只读属性 |
| [commandBlockContainerOpen](#commandBlockContainerOpen) | 只读属性 |
| [commandBlockUpdate](#commandBlockUpdate) | 只读属性 |
| [craftItemOutputChange](#craftItemOutputChange) | 只读属性 |
| [customCommandTrigger](#customCommandTrigger) | 只读属性 |
| [effectAdd](#effectAdd) | 只读属性 |
| [entityHealthChanged](#entityHealthChanged) | 只读属性 |
| [entityInsideBlock](#entityInsideBlock) | 只读属性 |
| [entityMotionStop](#entityMotionStop) | 只读属性 |
| [entityPlaceBlock](#entityPlaceBlock) | 只读属性 |
| [entitySpawn](#entitySpawn) | 只读属性 |
| [entityStopRiding](#entityStopRiding) | 只读属性 |
| [extinguishFire](#extinguishFire) | 只读属性 |
| [fallOnBlock](#fallOnBlock) | 只读属性 |
| [fallOnBlockMotion](#fallOnBlockMotion) | 只读属性 |
| [fallingBlockBreak](#fallingBlockBreak) | 只读属性 |
| [fallingBlockCauseDamage](#fallingBlockCauseDamage) | 只读属性 |
| [fireHurt](#fireHurt) | 只读属性 |
| [globalCommand](#globalCommand) | 只读属性 |
| [itemDurabilityChange](#itemDurabilityChange) | 只读属性 |
| [itemPullOutCustomContainer](#itemPullOutCustomContainer) | 只读属性 |
| [itemPushInCustomContainer](#itemPushInCustomContainer) | 只读属性 |
| [itemPutInEnchantingModel](#itemPutInEnchantingModel) | 只读属性 |
| [itemReleaseUsing](#itemReleaseUsing) | 只读属性 |
| [mobGriefingBlock](#mobGriefingBlock) | 只读属性 |
| [pistonAction](#pistonAction) | 只读属性 |
| [placeNeteaseLargeFeature](#placeNeteaseLargeFeature) | 只读属性 |
| [placeNeteaseStructureFeature](#placeNeteaseStructureFeature) | 只读属性 |
| [playerActiveShield](#playerActiveShield) | 只读属性 |
| [playerAttackEntity](#playerAttackEntity) | 只读属性 |
| [playerBlockedByShield](#playerBlockedByShield) | 只读属性 |
| [playerEatFood](#playerEatFood) | 只读属性 |
| [playerFeedEntity](#playerFeedEntity) | 只读属性 |
| [playerGetExperienceOrb](#playerGetExperienceOrb) | 只读属性 |
| [playerHungerChange](#playerHungerChange) | 只读属性 |
| [playerHurt](#playerHurt) | 只读属性 |
| [playerJoinMessage](#playerJoinMessage) | 只读属性 |
| [playerLeave](#playerLeave) | 只读属性 |
| [playerLeftMessage](#playerLeftMessage) | 只读属性 |
| [playerNamedEntity](#playerNamedEntity) | 只读属性 |
| [playerPermissionChange](#playerPermissionChange) | 只读属性 |
| [playerPickupArrow](#playerPickupArrow) | 只读属性 |
| [playerPickupItem](#playerPickupItem) | 只读属性 |
| [playerStartFishing](#playerStartFishing) | 只读属性 |
| [playerTryAddCustomContainerItem](#playerTryAddCustomContainerItem) | 只读属性 |
| [playerTryPutCustomContainerItem](#playerTryPutCustomContainerItem) | 只读属性 |
| [playerTryRemoveCustomContainerItem](#playerTryRemoveCustomContainerItem) | 只读属性 |
| [playerTrySleep](#playerTrySleep) | 只读属性 |
| [projectileDoHitEffect](#projectileDoHitEffect) | 只读属性 |
| [shearsDestroyBlock](#shearsDestroyBlock) | 只读属性 |
| [shearsUseToBlock](#shearsUseToBlock) | 只读属性 |
| [standOnBlock](#standOnBlock) | 只读属性 |
| [startDestroyBlock](#startDestroyBlock) | 只读属性 |
| [startRiding](#startRiding) | 只读属性 |
| [stepOnBlock](#stepOnBlock) | 只读属性 |
| [willTeleportTo](#willTeleportTo) | 只读属性 |
| [itemUse](#itemUse) | 只读属性 |
| [playerUseItemOnBlock](#playerUseItemOnBlock) | 只读属性 |
| [playerInteractWithBlock](#playerInteractWithBlock) | 只读属性 |
| [lootGenerate](#lootGenerate) | 只读属性 |
| [getSemanticEventNames](#getSemanticEventNames) | 方法 |
| [getEventNames](#getEventNames) | 方法 |
| [getNativeEventNames](#getNativeEventNames) | 方法 |
| [getNativeEvent](#getNativeEvent) | 方法 |

## 构造器 {#constructor}

```python
WorldBeforeEvents(owner = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `owner` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [WorldBeforeEvents.__init__](beforeEvents.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## chatSend {#chatSend}

```python
chatSend: ChatSendBeforeEventSignal
```

聊天消息广播或发送给玩家后触发。

**访问：** 只读。

**返回类型：** [ChatSendBeforeEventSignal](../reference/ChatSendBeforeEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.chatSend
```

## entityHurt {#entityHurt}

```python
entityHurt: EntityHurtBeforeEventSignal
```

实体受到伤害时触发。

**访问：** 只读。

**返回类型：** [EntityHurtBeforeEventSignal](../reference/EntityHurtBeforeEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entityHurt
```

## explosion {#explosion}

```python
explosion: ExplosionBeforeEventSignal
```

爆炸发生前触发。

**访问：** 只读。

**返回类型：** [ExplosionBeforeEventSignal](../reference/ExplosionBeforeEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.explosion
```

## playerInteractWithEntity {#playerInteractWithEntity}

```python
playerInteractWithEntity: PlayerInteractWithEntityBeforeEventSignal
```

玩家与实体交互时触发。

**访问：** 只读。

**返回类型：** [PlayerInteractWithEntityBeforeEventSignal](../reference/PlayerInteractWithEntityBeforeEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.playerInteractWithEntity
```

## playerBreakBlock {#playerBreakBlock}

```python
playerBreakBlock: PlayerBreakBlockBeforeEventSignal
```

玩家破坏方块前触发。

**访问：** 只读。

**返回类型：** [PlayerBreakBlockBeforeEventSignal](../reference/PlayerBreakBlockBeforeEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.playerBreakBlock
```

## actorUseItem {#actorUseItem}

```python
actorUseItem: NativeEventSignal[WorldActorUseItemBeforeEvent]
```

原生事件信号：[ActorUseItemServerEvent](../native-events.md#actoruseitemserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldActorUseItemBeforeEvent](../reference/WorldActorUseItemBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## actuallyHurt {#actuallyHurt}

```python
actuallyHurt: NativeEventSignal[WorldActuallyHurtBeforeEvent]
```

原生事件信号：[ActuallyHurtServerEvent](../native-events.md#actuallyhurtserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldActuallyHurtBeforeEvent](../reference/WorldActuallyHurtBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockLiquidStateChange {#blockLiquidStateChange}

```python
blockLiquidStateChange: NativeEventSignal[WorldBlockLiquidStateChangeBeforeEvent]
```

原生事件信号：[BlockLiquidStateChangeServerEvent](../native-events.md#blockliquidstatechangeserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldBlockLiquidStateChangeBeforeEvent](../reference/WorldBlockLiquidStateChangeBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockPattern {#blockPattern}

```python
blockPattern: NativeEventSignal[WorldBlockPatternBeforeEvent]
```

原生事件信号：[ServerPreBlockPatternEvent](../native-events.md#serverpreblockpatternevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldBlockPatternBeforeEvent](../reference/WorldBlockPatternBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockSnowStateChange {#blockSnowStateChange}

```python
blockSnowStateChange: NativeEventSignal[WorldBlockSnowStateChangeBeforeEvent]
```

原生事件信号：[BlockSnowStateChangeServerEvent](../native-events.md#blocksnowstatechangeserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldBlockSnowStateChangeBeforeEvent](../reference/WorldBlockSnowStateChangeBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## changeLevelUpCost {#changeLevelUpCost}

```python
changeLevelUpCost: NativeEventSignal[WorldChangeLevelUpCostBeforeEvent]
```

原生事件信号：[ChangeLevelUpCostServerEvent](../native-events.md#changelevelupcostserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldChangeLevelUpCostBeforeEvent](../reference/WorldChangeLevelUpCostBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## chestBlockTryPairWith {#chestBlockTryPairWith}

```python
chestBlockTryPairWith: NativeEventSignal[WorldChestBlockTryPairWithBeforeEvent]
```

原生事件信号：[ChestBlockTryPairWithServerEvent](../native-events.md#chestblocktrypairwithserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldChestBlockTryPairWithBeforeEvent](../reference/WorldChestBlockTryPairWithBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## chunkUnload {#chunkUnload}

```python
chunkUnload: NativeEventSignal[WorldChunkUnloadBeforeEvent]
```

原生事件信号：[ChunkAcquireDiscardedServerEvent](../native-events.md#chunkacquirediscardedserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldChunkUnloadBeforeEvent](../reference/WorldChunkUnloadBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## command {#command}

```python
command: NativeEventSignal[WorldCommandBeforeEvent]
```

原生事件信号：[CommandEvent](../native-events.md#commandevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldCommandBeforeEvent](../reference/WorldCommandBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## commandBlockContainerOpen {#commandBlockContainerOpen}

```python
commandBlockContainerOpen: NativeEventSignal[WorldCommandBlockContainerOpenBeforeEvent]
```

原生事件信号：[CommandBlockContainerOpenEvent](../native-events.md#commandblockcontaineropenevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldCommandBlockContainerOpenBeforeEvent](../reference/WorldCommandBlockContainerOpenBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## commandBlockUpdate {#commandBlockUpdate}

```python
commandBlockUpdate: NativeEventSignal[WorldCommandBlockUpdateBeforeEvent]
```

原生事件信号：[CommandBlockUpdateEvent](../native-events.md#commandblockupdateevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldCommandBlockUpdateBeforeEvent](../reference/WorldCommandBlockUpdateBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## craftItemOutputChange {#craftItemOutputChange}

```python
craftItemOutputChange: NativeEventSignal[WorldCraftItemOutputChangeBeforeEvent]
```

原生事件信号：[CraftItemOutputChangeServerEvent](../native-events.md#craftitemoutputchangeserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldCraftItemOutputChangeBeforeEvent](../reference/WorldCraftItemOutputChangeBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## customCommandTrigger {#customCommandTrigger}

```python
customCommandTrigger: NativeEventSignal[WorldCustomCommandTriggerBeforeEvent]
```

原生事件信号：[CustomCommandTriggerServerEvent](../native-events.md#customcommandtriggerserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldCustomCommandTriggerBeforeEvent](../reference/WorldCustomCommandTriggerBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## effectAdd {#effectAdd}

```python
effectAdd: NativeEventSignal[WorldEffectAddBeforeEvent]
```

原生事件信号：[WillAddEffectServerEvent](../native-events.md#willaddeffectserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEffectAddBeforeEvent](../reference/WorldEffectAddBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityHealthChanged {#entityHealthChanged}

```python
entityHealthChanged: NativeEventSignal[WorldEntityHealthChangedBeforeEvent]
```

原生事件信号：[HealthChangeBeforeServerEvent](../native-events.md#healthchangebeforeserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityHealthChangedBeforeEvent](../reference/WorldEntityHealthChangedBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityInsideBlock {#entityInsideBlock}

```python
entityInsideBlock: NativeEventSignal[WorldEntityInsideBlockBeforeEvent]
```

原生事件信号：[OnEntityInsideBlockServerEvent](../native-events.md#onentityinsideblockserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityInsideBlockBeforeEvent](../reference/WorldEntityInsideBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityMotionStop {#entityMotionStop}

```python
entityMotionStop: NativeEventSignal[WorldEntityMotionStopBeforeEvent]
```

原生事件信号：[EntityMotionStopServerEvent](../native-events.md#entitymotionstopserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityMotionStopBeforeEvent](../reference/WorldEntityMotionStopBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityPlaceBlock {#entityPlaceBlock}

```python
entityPlaceBlock: NativeEventSignal[WorldEntityPlaceBlockBeforeEvent]
```

原生事件信号：[ServerEntityTryPlaceBlockEvent](../native-events.md#serverentitytryplaceblockevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityPlaceBlockBeforeEvent](../reference/WorldEntityPlaceBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entitySpawn {#entitySpawn}

```python
entitySpawn: NativeEventSignal[WorldEntitySpawnBeforeEvent]
```

原生事件信号：[ServerSpawnMobEvent](../native-events.md#serverspawnmobevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntitySpawnBeforeEvent](../reference/WorldEntitySpawnBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityStopRiding {#entityStopRiding}

```python
entityStopRiding: NativeEventSignal[WorldEntityStopRidingBeforeEvent]
```

原生事件信号：[EntityStopRidingEvent](../native-events.md#entitystopridingevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityStopRidingBeforeEvent](../reference/WorldEntityStopRidingBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## extinguishFire {#extinguishFire}

```python
extinguishFire: NativeEventSignal[WorldExtinguishFireBeforeEvent]
```

原生事件信号：[ExtinguishFireServerEvent](../native-events.md#extinguishfireserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldExtinguishFireBeforeEvent](../reference/WorldExtinguishFireBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fallOnBlock {#fallOnBlock}

```python
fallOnBlock: NativeEventSignal[WorldFallOnBlockBeforeEvent]
```

原生事件信号：[OnBeforeFallOnBlockServerEvent](../native-events.md#onbeforefallonblockserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldFallOnBlockBeforeEvent](../reference/WorldFallOnBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fallOnBlockMotion {#fallOnBlockMotion}

```python
fallOnBlockMotion: NativeEventSignal[WorldFallOnBlockMotionBeforeEvent]
```

原生事件信号：[OnAfterFallOnBlockServerEvent](../native-events.md#onafterfallonblockserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldFallOnBlockMotionBeforeEvent](../reference/WorldFallOnBlockMotionBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fallingBlockBreak {#fallingBlockBreak}

```python
fallingBlockBreak: NativeEventSignal[WorldFallingBlockBreakBeforeEvent]
```

原生事件信号：[FallingBlockBreakServerEvent](../native-events.md#fallingblockbreakserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldFallingBlockBreakBeforeEvent](../reference/WorldFallingBlockBreakBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fallingBlockCauseDamage {#fallingBlockCauseDamage}

```python
fallingBlockCauseDamage: NativeEventSignal[WorldFallingBlockCauseDamageBeforeEvent]
```

原生事件信号：[FallingBlockCauseDamageBeforeServerEvent](../native-events.md#fallingblockcausedamagebeforeserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldFallingBlockCauseDamageBeforeEvent](../reference/WorldFallingBlockCauseDamageBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fireHurt {#fireHurt}

```python
fireHurt: NativeEventSignal[WorldFireHurtBeforeEvent]
```

原生事件信号：[OnFireHurtEvent](../native-events.md#onfirehurtevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldFireHurtBeforeEvent](../reference/WorldFireHurtBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## globalCommand {#globalCommand}

```python
globalCommand: NativeEventSignal[WorldGlobalCommandBeforeEvent]
```

原生事件信号：[GlobalCommandServerEvent](../native-events.md#globalcommandserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldGlobalCommandBeforeEvent](../reference/WorldGlobalCommandBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## itemDurabilityChange {#itemDurabilityChange}

```python
itemDurabilityChange: NativeEventSignal[WorldItemDurabilityChangeBeforeEvent]
```

原生事件信号：[ItemDurabilityChangedServerEvent](../native-events.md#itemdurabilitychangedserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldItemDurabilityChangeBeforeEvent](../reference/WorldItemDurabilityChangeBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## itemPullOutCustomContainer {#itemPullOutCustomContainer}

```python
itemPullOutCustomContainer: NativeEventSignal[WorldItemPullOutCustomContainerBeforeEvent]
```

原生事件信号：[ItemPullOutCustomContainerServerEvent](../native-events.md#itempulloutcustomcontainerserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldItemPullOutCustomContainerBeforeEvent](../reference/WorldItemPullOutCustomContainerBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## itemPushInCustomContainer {#itemPushInCustomContainer}

```python
itemPushInCustomContainer: NativeEventSignal[WorldItemPushInCustomContainerBeforeEvent]
```

原生事件信号：[ItemPushInCustomContainerServerEvent](../native-events.md#itempushincustomcontainerserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldItemPushInCustomContainerBeforeEvent](../reference/WorldItemPushInCustomContainerBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## itemPutInEnchantingModel {#itemPutInEnchantingModel}

```python
itemPutInEnchantingModel: NativeEventSignal[WorldItemPutInEnchantingModelBeforeEvent]
```

原生事件信号：[OnItemPutInEnchantingModelServerEvent](../native-events.md#onitemputinenchantingmodelserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldItemPutInEnchantingModelBeforeEvent](../reference/WorldItemPutInEnchantingModelBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## itemReleaseUsing {#itemReleaseUsing}

```python
itemReleaseUsing: NativeEventSignal[WorldItemReleaseUsingBeforeEvent]
```

原生事件信号：[ItemReleaseUsingServerEvent](../native-events.md#itemreleaseusingserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldItemReleaseUsingBeforeEvent](../reference/WorldItemReleaseUsingBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## mobGriefingBlock {#mobGriefingBlock}

```python
mobGriefingBlock: NativeEventSignal[WorldMobGriefingBlockBeforeEvent]
```

原生事件信号：[MobGriefingBlockServerEvent](../native-events.md#mobgriefingblockserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldMobGriefingBlockBeforeEvent](../reference/WorldMobGriefingBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## pistonAction {#pistonAction}

```python
pistonAction: NativeEventSignal[WorldPistonActionBeforeEvent]
```

原生事件信号：[PistonActionServerEvent](../native-events.md#pistonactionserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPistonActionBeforeEvent](../reference/WorldPistonActionBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## placeNeteaseLargeFeature {#placeNeteaseLargeFeature}

```python
placeNeteaseLargeFeature: NativeEventSignal[WorldPlaceNeteaseLargeFeatureBeforeEvent]
```

原生事件信号：[PlaceNeteaseLargeFeatureServerEvent](../native-events.md#placeneteaselargefeatureserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlaceNeteaseLargeFeatureBeforeEvent](../reference/WorldPlaceNeteaseLargeFeatureBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## placeNeteaseStructureFeature {#placeNeteaseStructureFeature}

```python
placeNeteaseStructureFeature: NativeEventSignal[WorldPlaceNeteaseStructureFeatureBeforeEvent]
```

原生事件信号：[PlaceNeteaseStructureFeatureEvent](../native-events.md#placeneteasestructurefeatureevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlaceNeteaseStructureFeatureBeforeEvent](../reference/WorldPlaceNeteaseStructureFeatureBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerActiveShield {#playerActiveShield}

```python
playerActiveShield: NativeEventSignal[WorldPlayerActiveShieldBeforeEvent]
```

原生事件信号：[OnPlayerActiveShieldServerEvent](../native-events.md#onplayeractiveshieldserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerActiveShieldBeforeEvent](../reference/WorldPlayerActiveShieldBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerAttackEntity {#playerAttackEntity}

```python
playerAttackEntity: NativeEventSignal[WorldPlayerAttackEntityBeforeEvent]
```

原生事件信号：[PlayerAttackEntityEvent](../native-events.md#playerattackentityevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerAttackEntityBeforeEvent](../reference/WorldPlayerAttackEntityBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerBlockedByShield {#playerBlockedByShield}

```python
playerBlockedByShield: NativeEventSignal[WorldPlayerBlockedByShieldBeforeEvent]
```

原生事件信号：[OnPlayerBlockedByShieldBeforeServerEvent](../native-events.md#onplayerblockedbyshieldbeforeserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerBlockedByShieldBeforeEvent](../reference/WorldPlayerBlockedByShieldBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerEatFood {#playerEatFood}

```python
playerEatFood: NativeEventSignal[WorldPlayerEatFoodBeforeEvent]
```

原生事件信号：[PlayerEatFoodServerEvent](../native-events.md#playereatfoodserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerEatFoodBeforeEvent](../reference/WorldPlayerEatFoodBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerFeedEntity {#playerFeedEntity}

```python
playerFeedEntity: NativeEventSignal[WorldPlayerFeedEntityBeforeEvent]
```

原生事件信号：[PlayerFeedEntityServerEvent](../native-events.md#playerfeedentityserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerFeedEntityBeforeEvent](../reference/WorldPlayerFeedEntityBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerGetExperienceOrb {#playerGetExperienceOrb}

```python
playerGetExperienceOrb: NativeEventSignal[WorldPlayerGetExperienceOrbBeforeEvent]
```

原生事件信号：[ServerPlayerGetExperienceOrbEvent](../native-events.md#serverplayergetexperienceorbevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerGetExperienceOrbBeforeEvent](../reference/WorldPlayerGetExperienceOrbBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerHungerChange {#playerHungerChange}

```python
playerHungerChange: NativeEventSignal[WorldPlayerHungerChangeBeforeEvent]
```

原生事件信号：[PlayerHungerChangeServerEvent](../native-events.md#playerhungerchangeserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerHungerChangeBeforeEvent](../reference/WorldPlayerHungerChangeBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerHurt {#playerHurt}

```python
playerHurt: NativeEventSignal[WorldPlayerHurtBeforeEvent]
```

原生事件信号：[PlayerHurtEvent](../native-events.md#playerhurtevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerHurtBeforeEvent](../reference/WorldPlayerHurtBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerJoinMessage {#playerJoinMessage}

```python
playerJoinMessage: NativeEventSignal[WorldPlayerJoinMessageBeforeEvent]
```

原生事件信号：[PlayerJoinMessageEvent](../native-events.md#playerjoinmessageevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerJoinMessageBeforeEvent](../reference/WorldPlayerJoinMessageBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerLeave {#playerLeave}

```python
playerLeave: NativeEventSignal[WorldPlayerLeaveBeforeEvent]
```

原生事件信号：[PlayerIntendLeaveServerEvent](../native-events.md#playerintendleaveserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerLeaveBeforeEvent](../reference/WorldPlayerLeaveBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerLeftMessage {#playerLeftMessage}

```python
playerLeftMessage: NativeEventSignal[WorldPlayerLeftMessageBeforeEvent]
```

原生事件信号：[PlayerLeftMessageServerEvent](../native-events.md#playerleftmessageserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerLeftMessageBeforeEvent](../reference/WorldPlayerLeftMessageBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerNamedEntity {#playerNamedEntity}

```python
playerNamedEntity: NativeEventSignal[WorldPlayerNamedEntityBeforeEvent]
```

原生事件信号：[PlayerNamedEntityServerEvent](../native-events.md#playernamedentityserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerNamedEntityBeforeEvent](../reference/WorldPlayerNamedEntityBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerPermissionChange {#playerPermissionChange}

```python
playerPermissionChange: NativeEventSignal[WorldPlayerPermissionChangeBeforeEvent]
```

原生事件信号：[PlayerPermissionChangeServerEvent](../native-events.md#playerpermissionchangeserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerPermissionChangeBeforeEvent](../reference/WorldPlayerPermissionChangeBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerPickupArrow {#playerPickupArrow}

```python
playerPickupArrow: NativeEventSignal[WorldPlayerPickupArrowBeforeEvent]
```

原生事件信号：[PlayerPickupArrowServerEvent](../native-events.md#playerpickuparrowserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerPickupArrowBeforeEvent](../reference/WorldPlayerPickupArrowBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerPickupItem {#playerPickupItem}

```python
playerPickupItem: NativeEventSignal[WorldPlayerPickupItemBeforeEvent]
```

原生事件信号：[ServerPlayerTryTouchEvent](../native-events.md#serverplayertrytouchevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerPickupItemBeforeEvent](../reference/WorldPlayerPickupItemBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerStartFishing {#playerStartFishing}

```python
playerStartFishing: NativeEventSignal[WorldPlayerStartFishingBeforeEvent]
```

原生事件信号：[PlayerStartFishingServerEvent](../native-events.md#playerstartfishingserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerStartFishingBeforeEvent](../reference/WorldPlayerStartFishingBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerTryAddCustomContainerItem {#playerTryAddCustomContainerItem}

```python
playerTryAddCustomContainerItem: NativeEventSignal[WorldPlayerTryAddCustomContainerItemBeforeEvent]
```

原生事件信号：[PlayerTryAddCustomContainerItemServerEvent](../native-events.md#playertryaddcustomcontaineritemserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerTryAddCustomContainerItemBeforeEvent](../reference/WorldPlayerTryAddCustomContainerItemBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerTryPutCustomContainerItem {#playerTryPutCustomContainerItem}

```python
playerTryPutCustomContainerItem: NativeEventSignal[WorldPlayerTryPutCustomContainerItemBeforeEvent]
```

原生事件信号：[PlayerTryPutCustomContainerItemServerEvent](../native-events.md#playertryputcustomcontaineritemserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerTryPutCustomContainerItemBeforeEvent](../reference/WorldPlayerTryPutCustomContainerItemBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerTryRemoveCustomContainerItem {#playerTryRemoveCustomContainerItem}

```python
playerTryRemoveCustomContainerItem: NativeEventSignal[WorldPlayerTryRemoveCustomContainerItemBeforeEvent]
```

原生事件信号：[PlayerTryRemoveCustomContainerItemServerEvent](../native-events.md#playertryremovecustomcontaineritemserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerTryRemoveCustomContainerItemBeforeEvent](../reference/WorldPlayerTryRemoveCustomContainerItemBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerTrySleep {#playerTrySleep}

```python
playerTrySleep: NativeEventSignal[WorldPlayerTrySleepBeforeEvent]
```

原生事件信号：[PlayerTrySleepServerEvent](../native-events.md#playertrysleepserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerTrySleepBeforeEvent](../reference/WorldPlayerTrySleepBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## projectileDoHitEffect {#projectileDoHitEffect}

```python
projectileDoHitEffect: NativeEventSignal[WorldProjectileDoHitEffectBeforeEvent]
```

原生事件信号：[ProjectileDoHitEffectEvent](../native-events.md#projectiledohiteffectevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldProjectileDoHitEffectBeforeEvent](../reference/WorldProjectileDoHitEffectBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## shearsDestroyBlock {#shearsDestroyBlock}

```python
shearsDestroyBlock: NativeEventSignal[WorldShearsDestroyBlockBeforeEvent]
```

原生事件信号：[ShearsDestoryBlockBeforeServerEvent](../native-events.md#shearsdestoryblockbeforeserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldShearsDestroyBlockBeforeEvent](../reference/WorldShearsDestroyBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## shearsUseToBlock {#shearsUseToBlock}

```python
shearsUseToBlock: NativeEventSignal[WorldShearsUseToBlockBeforeEvent]
```

原生事件信号：[ShearsUseToBlockBeforeServerEvent](../native-events.md#shearsusetoblockbeforeserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldShearsUseToBlockBeforeEvent](../reference/WorldShearsUseToBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## standOnBlock {#standOnBlock}

```python
standOnBlock: NativeEventSignal[WorldStandOnBlockBeforeEvent]
```

原生事件信号：[OnStandOnBlockServerEvent](../native-events.md#onstandonblockserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldStandOnBlockBeforeEvent](../reference/WorldStandOnBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## startDestroyBlock {#startDestroyBlock}

```python
startDestroyBlock: NativeEventSignal[WorldStartDestroyBlockBeforeEvent]
```

原生事件信号：[StartDestroyBlockServerEvent](../native-events.md#startdestroyblockserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldStartDestroyBlockBeforeEvent](../reference/WorldStartDestroyBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## startRiding {#startRiding}

```python
startRiding: NativeEventSignal[WorldStartRidingBeforeEvent]
```

原生事件信号：[StartRidingServerEvent](../native-events.md#startridingserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldStartRidingBeforeEvent](../reference/WorldStartRidingBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## stepOnBlock {#stepOnBlock}

```python
stepOnBlock: NativeEventSignal[WorldStepOnBlockBeforeEvent]
```

原生事件信号：[StepOnBlockServerEvent](../native-events.md#steponblockserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldStepOnBlockBeforeEvent](../reference/WorldStepOnBlockBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## willTeleportTo {#willTeleportTo}

```python
willTeleportTo: NativeEventSignal[WorldWillTeleportToBeforeEvent]
```

原生事件信号：[WillTeleportToServerEvent](../native-events.md#willteleporttoserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldWillTeleportToBeforeEvent](../reference/WorldWillTeleportToBeforeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## itemUse {#itemUse}

```python
itemUse: EventSignal[ItemUseAttemptEvent]
```

物品使用事件，支持订阅筛选。原生来源：[ServerItemTryUseEvent](../native-events.md#serveritemtryuseevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[ItemUseAttemptEvent](../../common/reference/ItemUseAttemptEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerUseItemOnBlock {#playerUseItemOnBlock}

```python
playerUseItemOnBlock: EventSignal[BlockInteractionEvent]
```

对方块使用物品事件，支持订阅筛选。原生来源：[ServerItemUseOnEvent](../native-events.md#serveritemuseonevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[BlockInteractionEvent](../../common/reference/BlockInteractionEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerInteractWithBlock {#playerInteractWithBlock}

```python
playerInteractWithBlock: EventSignal[BlockInteractionEvent]
```

方块交互事件，支持订阅筛选。原生来源：[ServerBlockUseEvent](../native-events.md#serverblockuseevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[BlockInteractionEvent](../../common/reference/BlockInteractionEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## lootGenerate {#lootGenerate}

```python
lootGenerate: EventSignal[LootGenerateBeforeEvent]
```

战利品生成事件，支持订阅筛选。原生来源：[EntityDieLoottableServerEvent](../native-events.md#entitydieloottableserverevent), [OnContainerFillLoottableServerEvent](../native-events.md#oncontainerfillloottableserverevent), [PlayerFishingServerEvent](../native-events.md#playerfishingserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[LootGenerateBeforeEvent](../../common/reference/LootGenerateBeforeEvent.md)]。静态声明不替代本页的实现限制。

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
    # value 是上方获取方式取得的 WorldBeforeEvents 对象。
    print(value.chatSend)
    print(value.entityHurt)
    print(value.explosion)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)