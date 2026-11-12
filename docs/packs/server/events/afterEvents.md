---
title: "WorldAfterEvents"
sidebar_label: "WorldAfterEvents"
---

# WorldAfterEvents

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/WorldEvents.py`；声明补充了静态类型信息。

世界范围内可订阅的事件集合。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [dataDrivenEntityTrigger](#dataDrivenEntityTrigger) | 只读属性 |
| [entityDie](#entityDie) | 只读属性 |
| [effectAdd](#effectAdd) | 只读属性 |
| [entityHealthChanged](#entityHealthChanged) | 只读属性 |
| [entityHurt](#entityHurt) | 只读属性 |
| [entityHitEntity](#entityHitEntity) | 只读属性 |
| [entitySpawn](#entitySpawn) | 只读属性 |
| [entityLoad](#entityLoad) | 只读属性 |
| [entityRemove](#entityRemove) | 只读属性 |
| [chatSend](#chatSend) | 只读属性 |
| [itemUse](#itemUse) | 只读属性 |
| [itemCompleteUse](#itemCompleteUse) | 只读属性 |
| [projectileHitBlock](#projectileHitBlock) | 只读属性 |
| [projectileHitEntity](#projectileHitEntity) | 只读属性 |
| [itemStartUseOn](#itemStartUseOn) | 只读属性 |
| [blockExplode](#blockExplode) | 只读属性 |
| [explosion](#explosion) | 只读属性 |
| [playerDimensionChange](#playerDimensionChange) | 只读属性 |
| [playerJoin](#playerJoin) | 只读属性 |
| [playerLeave](#playerLeave) | 只读属性 |
| [playerSpawn](#playerSpawn) | 只读属性 |
| [playerInventoryItemChange](#playerInventoryItemChange) | 只读属性 |
| [playerBreakBlock](#playerBreakBlock) | 只读属性 |
| [playerPlaceBlock](#playerPlaceBlock) | 只读属性 |
| [playerInteractWithEntity](#playerInteractWithEntity) | 只读属性 |
| [achievementComplete](#achievementComplete) | 只读属性 |
| [actorAcquiredItem](#actorAcquiredItem) | 只读属性 |
| [actorHurt](#actorHurt) | 只读属性 |
| [attackAnimBegin](#attackAnimBegin) | 只读属性 |
| [attackAnimEnd](#attackAnimEnd) | 只读属性 |
| [blockDestroyByLiquid](#blockDestroyByLiquid) | 只读属性 |
| [blockEntityTick](#blockEntityTick) | 只读属性 |
| [blockLiquidStateChange](#blockLiquidStateChange) | 只读属性 |
| [blockNeighborChange](#blockNeighborChange) | 只读属性 |
| [blockPattern](#blockPattern) | 只读属性 |
| [blockRandomTick](#blockRandomTick) | 只读属性 |
| [blockRemove](#blockRemove) | 只读属性 |
| [blockSnowStateChange](#blockSnowStateChange) | 只读属性 |
| [blockStrengthChange](#blockStrengthChange) | 只读属性 |
| [changeSwimState](#changeSwimState) | 只读属性 |
| [chunkGenerated](#chunkGenerated) | 只读属性 |
| [chunkLoad](#chunkLoad) | 只读属性 |
| [clientReady](#clientReady) | 只读属性 |
| [commandOutput](#commandOutput) | 只读属性 |
| [containerItemChange](#containerItemChange) | 只读属性 |
| [dirtBlockToGrassBlock](#dirtBlockToGrassBlock) | 只读属性 |
| [entityChangeDimension](#entityChangeDimension) | 只读属性 |
| [entityCollide](#entityCollide) | 只读属性 |
| [entityDroppedItem](#entityDroppedItem) | 只读属性 |
| [entityEffectDamage](#entityEffectDamage) | 只读属性 |
| [entityHitBlock](#entityHitBlock) | 只读属性 |
| [entityKnockback](#entityKnockback) | 只读属性 |
| [entityLand](#entityLand) | 只读属性 |
| [entityLoadScript](#entityLoadScript) | 只读属性 |
| [entityLoot](#entityLoot) | 只读属性 |
| [entityMotionStart](#entityMotionStart) | 只读属性 |
| [entityPickupItem](#entityPickupItem) | 只读属性 |
| [entityPlaceBlock](#entityPlaceBlock) | 只读属性 |
| [entityStartRiding](#entityStartRiding) | 只读属性 |
| [entityTame](#entityTame) | 只读属性 |
| [entityTick](#entityTick) | 只读属性 |
| [fallingBlockReturnHeavyBlock](#fallingBlockReturnHeavyBlock) | 只读属性 |
| [farmBlockToDirtBlock](#farmBlockToDirtBlock) | 只读属性 |
| [furnaceBurnFinish](#furnaceBurnFinish) | 只读属性 |
| [gameTypeChange](#gameTypeChange) | 只读属性 |
| [grassBlockToDirtBlock](#grassBlockToDirtBlock) | 只读属性 |
| [heavyBlockStartFalling](#heavyBlockStartFalling) | 只读属性 |
| [hopperTryPullIn](#hopperTryPullIn) | 只读属性 |
| [hopperTryPullOut](#hopperTryPullOut) | 只读属性 |
| [jumpAnimBegin](#jumpAnimBegin) | 只读属性 |
| [liquidClipped](#liquidClipped) | 只读属性 |
| [lobbyPurchase](#lobbyPurchase) | 只读属性 |
| [placeBlockEntity](#placeBlockEntity) | 只读属性 |
| [playerAdd](#playerAdd) | 只读属性 |
| [playerAddCustomContainerItem](#playerAddCustomContainerItem) | 只读属性 |
| [playerBlockedByShield](#playerBlockedByShield) | 只读属性 |
| [playerCheatSpinAttack](#playerCheatSpinAttack) | 只读属性 |
| [playerDie](#playerDie) | 只读属性 |
| [playerDimensionChangeFinish](#playerDimensionChangeFinish) | 只读属性 |
| [playerDropItem](#playerDropItem) | 只读属性 |
| [playerExperienceAdd](#playerExperienceAdd) | 只读属性 |
| [playerFishing](#playerFishing) | 只读属性 |
| [playerHitBlock](#playerHitBlock) | 只读属性 |
| [playerInventoryOpenScript](#playerInventoryOpenScript) | 只读属性 |
| [playerLevelChange](#playerLevelChange) | 只读属性 |
| [playerRemove](#playerRemove) | 只读属性 |
| [playerRemoveCustomContainerItem](#playerRemoveCustomContainerItem) | 只读属性 |
| [playerRespawn](#playerRespawn) | 只读属性 |
| [playerSleep](#playerSleep) | 只读属性 |
| [playerSpinAttack](#playerSpinAttack) | 只读属性 |
| [playerStopSleep](#playerStopSleep) | 只读属性 |
| [playerTeleport](#playerTeleport) | 只读属性 |
| [projectileCritHit](#projectileCritHit) | 只读属性 |
| [scriptsLoad](#scriptsLoad) | 只读属性 |
| [spawnProjectile](#spawnProjectile) | 只读属性 |
| [stepOffBlock](#stepOffBlock) | 只读属性 |
| [storeBuySucc](#storeBuySucc) | 只读属性 |
| [tick](#tick) | 只读属性 |
| [uiContainerItemChange](#uiContainerItemChange) | 只读属性 |
| [urgeShip](#urgeShip) | 只读属性 |
| [walkAnimBegin](#walkAnimBegin) | 只读属性 |
| [walkAnimEnd](#walkAnimEnd) | 只读属性 |
| [playerStateChange](#playerStateChange) | 只读属性 |
| [playerSneakChange](#playerSneakChange) | 只读属性 |
| [playerSprintChange](#playerSprintChange) | 只读属性 |
| [playerGlideChange](#playerGlideChange) | 只读属性 |
| [playerSwimChange](#playerSwimChange) | 只读属性 |
| [playerCrawlChange](#playerCrawlChange) | 只读属性 |
| [playerFlyChange](#playerFlyChange) | 只读属性 |
| [playerSleepChange](#playerSleepChange) | 只读属性 |
| [playerSpinAttackChange](#playerSpinAttackChange) | 只读属性 |
| [equipmentChange](#equipmentChange) | 只读属性 |
| [physicsContactBegin](#physicsContactBegin) | 只读属性 |
| [physicsContactEnd](#physicsContactEnd) | 只读属性 |
| [physicsTriggerEnter](#physicsTriggerEnter) | 只读属性 |
| [physicsTriggerLeave](#physicsTriggerLeave) | 只读属性 |
| [entityEnterArea](#entityEnterArea) | 只读属性 |
| [entityLeaveArea](#entityLeaveArea) | 只读属性 |
| [effectRefresh](#effectRefresh) | 只读属性 |
| [effectRemove](#effectRemove) | 只读属性 |
| [weatherChange](#weatherChange) | 只读属性 |
| [getSemanticEventNames](#getSemanticEventNames) | 方法 |
| [getEventNames](#getEventNames) | 方法 |
| [getNativeEventNames](#getNativeEventNames) | 方法 |
| [getNativeEvent](#getNativeEvent) | 方法 |

## 构造器 {#constructor}

```python
WorldAfterEvents(owner = None)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `owner` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [WorldAfterEvents.__init__](afterEvents.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## dataDrivenEntityTrigger {#dataDrivenEntityTrigger}

```python
dataDrivenEntityTrigger: DataDrivenEntityTriggerEventSignal
```

触发会更新实体组件定义状态的数据驱动事件时执行。

**访问：** 只读。

**返回类型：** [DataDrivenEntityTriggerEventSignal](../reference/DataDrivenEntityTriggerEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.dataDrivenEntityTrigger
```

## entityDie {#entityDie}

```python
entityDie: EntityDieAfterEventSignal
```

实体死亡后的事件订阅入口。

**访问：** 只读。

**返回类型：** [EntityDieAfterEventSignal](../reference/EntityDieAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entityDie
```

## effectAdd {#effectAdd}

```python
effectAdd: EventSignal[EffectAddAfterEvent]
```

向实体添加状态效果时触发，例如中毒效果。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[EffectAddAfterEvent](../reference/EffectAddAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.effectAdd
```

## entityHealthChanged {#entityHealthChanged}

```python
entityHealthChanged: EntityHealthChangedAfterEventSignal
```

实体生命值发生任何变化时触发。

**访问：** 只读。

**返回类型：** [EntityHealthChangedAfterEventSignal](../reference/EntityHealthChangedAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entityHealthChanged
```

## entityHurt {#entityHurt}

<span id="entityhurt" />

```python
entityHurt: EntityHurtAfterEventSignal
```

实体受到伤害时触发。

**访问：** 只读。

**返回类型：** [EntityHurtAfterEventSignal](../reference/EntityHurtAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entityHurt
```

## entityHitEntity {#entityHitEntity}

```python
entityHitEntity: EntityHitEntityAfterEventSignal
```

实体近战攻击另一实体时触发。

**访问：** 只读。

**返回类型：** [EntityHitEntityAfterEventSignal](../reference/EntityHitEntityAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entityHitEntity
```

## entitySpawn {#entitySpawn}

```python
entitySpawn: EntitySpawnAfterEventSignal
```

实体生成时触发。

**访问：** 只读。

**返回类型：** [EntitySpawnAfterEventSignal](../reference/EntitySpawnAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entitySpawn
```

## entityLoad {#entityLoad}

```python
entityLoad: EntityLoadAfterEventSignal
```

实体加载时触发。

**访问：** 只读。

**返回类型：** [EntityLoadAfterEventSignal](../reference/EntityLoadAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entityLoad
```

## entityRemove {#entityRemove}

```python
entityRemove: EntityRemoveAfterEventSignal
```

实体被移除时触发，例如卸载或死亡后移除。

**访问：** 只读。

**返回类型：** [EntityRemoveAfterEventSignal](../reference/EntityRemoveAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entityRemove
```

## chatSend {#chatSend}

```python
chatSend: ChatSendAfterEventSignal
```

聊天消息广播或发送给玩家后触发。

**访问：** 只读。

**返回类型：** [ChatSendAfterEventSignal](../reference/ChatSendAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.chatSend
```

## itemUse {#itemUse}

```python
itemUse: ItemUseAfterEventSignal
```

玩家成功使用物品时触发。

**访问：** 只读。

**返回类型：** [ItemUseAfterEventSignal](../reference/ItemUseAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.itemUse
```

## itemCompleteUse {#itemCompleteUse}

```python
itemCompleteUse: ItemCompleteUseAfterEventSignal
```

可蓄力物品完成蓄力时触发。

**访问：** 只读。

**返回类型：** [ItemCompleteUseAfterEventSignal](../reference/ItemCompleteUseAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.itemCompleteUse
```

## projectileHitBlock {#projectileHitBlock}

```python
projectileHitBlock: ProjectileHitBlockAfterEventSignal
```

投射物命中方块时触发。

**访问：** 只读。

**返回类型：** [ProjectileHitBlockAfterEventSignal](../reference/ProjectileHitBlockAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.projectileHitBlock
```

## projectileHitEntity {#projectileHitEntity}

```python
projectileHitEntity: ProjectileHitEntityAfterEventSignal
```

投射物命中实体时触发。

**访问：** 只读。

**返回类型：** [ProjectileHitEntityAfterEventSignal](../reference/ProjectileHitEntityAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.projectileHitEntity
```

## itemStartUseOn {#itemStartUseOn}

```python
itemStartUseOn: ItemStartUseOnAfterEventSignal
```

可蓄力物品开始蓄力时触发。

**访问：** 只读。

**返回类型：** [ItemStartUseOnAfterEventSignal](../reference/ItemStartUseOnAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.itemStartUseOn
```

## blockExplode {#blockExplode}

```python
blockExplode: BlockExplodeAfterEventSignal
```

爆炸破坏方块后，针对每个被破坏的位置触发。

**访问：** 只读。

**返回类型：** [BlockExplodeAfterEventSignal](../reference/BlockExplodeAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.blockExplode
```

## explosion {#explosion}

```python
explosion: ExplosionAfterEventSignal
```

爆炸发生后触发。

**访问：** 只读。

**返回类型：** [ExplosionAfterEventSignal](../reference/ExplosionAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.explosion
```

## playerDimensionChange {#playerDimensionChange}

```python
playerDimensionChange: PlayerDimensionChangeAfterEventSignal
```

玩家切换到另一维度时触发。

**访问：** 只读。

**返回类型：** [PlayerDimensionChangeAfterEventSignal](../reference/PlayerDimensionChangeAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.playerDimensionChange
```

## playerJoin {#playerJoin}

```python
playerJoin: PlayerJoinAfterEventSignal
```

玩家加入世界时触发。需要玩家首次生成后的信息时，也可订阅 playerSpawn。

**访问：** 只读。

**返回类型：** [PlayerJoinAfterEventSignal](../reference/PlayerJoinAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.playerJoin
```

## playerLeave {#playerLeave}

```python
playerLeave: PlayerLeaveAfterEventSignal
```

玩家离开世界时触发。

**访问：** 只读。

**返回类型：** [PlayerLeaveAfterEventSignal](../reference/PlayerLeaveAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.playerLeave
```

## playerSpawn {#playerSpawn}

```python
playerSpawn: PlayerSpawnAfterEventSignal
```

玩家生成或重生时触发；事件中的标记可区分加入后的首次生成与后续重生。

**访问：** 只读。

**返回类型：** [PlayerSpawnAfterEventSignal](../reference/PlayerSpawnAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.playerSpawn
```

## playerInventoryItemChange {#playerInventoryItemChange}

```python
playerInventoryItemChange: EventSignal[PlayerInventoryItemChangeAfterEvent]
```

玩家库存中的物品增加或移除时触发。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerInventoryItemChangeAfterEvent](../reference/PlayerInventoryItemChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.playerInventoryItemChange
```

## playerBreakBlock {#playerBreakBlock}

```python
playerBreakBlock: PlayerBreakBlockAfterEventSignal
```

玩家破坏方块时触发。

**访问：** 只读。

**返回类型：** [PlayerBreakBlockAfterEventSignal](../reference/PlayerBreakBlockAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.playerBreakBlock
```

## playerPlaceBlock {#playerPlaceBlock}

```python
playerPlaceBlock: PlayerPlaceBlockAfterEventSignal
```

玩家放置方块时触发。

**访问：** 只读。

**返回类型：** [PlayerPlaceBlockAfterEventSignal](../reference/PlayerPlaceBlockAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.playerPlaceBlock
```

## playerInteractWithEntity {#playerInteractWithEntity}

```python
playerInteractWithEntity: PlayerInteractWithEntityAfterEventSignal
```

玩家与实体交互时触发。

**访问：** 只读。

**返回类型：** [PlayerInteractWithEntityAfterEventSignal](../reference/PlayerInteractWithEntityAfterEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.playerInteractWithEntity
```

## achievementComplete {#achievementComplete}

```python
achievementComplete: NativeEventSignal[WorldAchievementCompleteAfterEvent]
```

原生事件信号：[AchievementCompleteEvent](../native-events.md#achievementcompleteevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldAchievementCompleteAfterEvent](../reference/WorldAchievementCompleteAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## actorAcquiredItem {#actorAcquiredItem}

```python
actorAcquiredItem: NativeEventSignal[WorldActorAcquiredItemAfterEvent]
```

原生事件信号：[ActorAcquiredItemServerEvent](../native-events.md#actoracquireditemserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldActorAcquiredItemAfterEvent](../reference/WorldActorAcquiredItemAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## actorHurt {#actorHurt}

```python
actorHurt: NativeEventSignal[WorldActorHurtAfterEvent]
```

原生事件信号：[ActorHurtServerEvent](../native-events.md#actorhurtserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldActorHurtAfterEvent](../reference/WorldActorHurtAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## attackAnimBegin {#attackAnimBegin}

```python
attackAnimBegin: NativeEventSignal[WorldAttackAnimBeginAfterEvent]
```

原生事件信号：[AttackAnimBeginServerEvent](../native-events.md#attackanimbeginserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldAttackAnimBeginAfterEvent](../reference/WorldAttackAnimBeginAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## attackAnimEnd {#attackAnimEnd}

```python
attackAnimEnd: NativeEventSignal[WorldAttackAnimEndAfterEvent]
```

原生事件信号：[AttackAnimEndServerEvent](../native-events.md#attackanimendserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldAttackAnimEndAfterEvent](../reference/WorldAttackAnimEndAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockDestroyByLiquid {#blockDestroyByLiquid}

```python
blockDestroyByLiquid: NativeEventSignal[WorldBlockDestroyByLiquidAfterEvent]
```

原生事件信号：[BlockDestroyByLiquidServerEvent](../native-events.md#blockdestroybyliquidserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldBlockDestroyByLiquidAfterEvent](../reference/WorldBlockDestroyByLiquidAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockEntityTick {#blockEntityTick}

```python
blockEntityTick: NativeEventSignal[WorldBlockEntityTickAfterEvent]
```

原生事件信号：[ServerBlockEntityTickEvent](../native-events.md#serverblockentitytickevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldBlockEntityTickAfterEvent](../reference/WorldBlockEntityTickAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockLiquidStateChange {#blockLiquidStateChange}

```python
blockLiquidStateChange: NativeEventSignal[WorldBlockLiquidStateChangeAfterEvent]
```

原生事件信号：[BlockLiquidStateChangeAfterServerEvent](../native-events.md#blockliquidstatechangeafterserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldBlockLiquidStateChangeAfterEvent](../reference/WorldBlockLiquidStateChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockNeighborChange {#blockNeighborChange}

```python
blockNeighborChange: NativeEventSignal[WorldBlockNeighborChangeAfterEvent]
```

原生事件信号：[BlockNeighborChangedServerEvent](../native-events.md#blockneighborchangedserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldBlockNeighborChangeAfterEvent](../reference/WorldBlockNeighborChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockPattern {#blockPattern}

```python
blockPattern: NativeEventSignal[WorldBlockPatternAfterEvent]
```

原生事件信号：[ServerPostBlockPatternEvent](../native-events.md#serverpostblockpatternevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldBlockPatternAfterEvent](../reference/WorldBlockPatternAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockRandomTick {#blockRandomTick}

```python
blockRandomTick: NativeEventSignal[WorldBlockRandomTickAfterEvent]
```

原生事件信号：[BlockRandomTickServerEvent](../native-events.md#blockrandomtickserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldBlockRandomTickAfterEvent](../reference/WorldBlockRandomTickAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockRemove {#blockRemove}

```python
blockRemove: NativeEventSignal[WorldBlockRemoveAfterEvent]
```

原生事件信号：[BlockRemoveServerEvent](../native-events.md#blockremoveserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldBlockRemoveAfterEvent](../reference/WorldBlockRemoveAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockSnowStateChange {#blockSnowStateChange}

```python
blockSnowStateChange: NativeEventSignal[WorldBlockSnowStateChangeAfterEvent]
```

原生事件信号：[BlockSnowStateChangeAfterServerEvent](../native-events.md#blocksnowstatechangeafterserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldBlockSnowStateChangeAfterEvent](../reference/WorldBlockSnowStateChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockStrengthChange {#blockStrengthChange}

```python
blockStrengthChange: NativeEventSignal[WorldBlockStrengthChangeAfterEvent]
```

原生事件信号：[BlockStrengthChangedServerEvent](../native-events.md#blockstrengthchangedserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldBlockStrengthChangeAfterEvent](../reference/WorldBlockStrengthChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## changeSwimState {#changeSwimState}

```python
changeSwimState: NativeEventSignal[WorldChangeSwimStateAfterEvent]
```

原生事件信号：[ChangeSwimStateServerEvent](../native-events.md#changeswimstateserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldChangeSwimStateAfterEvent](../reference/WorldChangeSwimStateAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## chunkGenerated {#chunkGenerated}

```python
chunkGenerated: NativeEventSignal[WorldChunkGeneratedAfterEvent]
```

原生事件信号：[ChunkGeneratedServerEvent](../native-events.md#chunkgeneratedserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldChunkGeneratedAfterEvent](../reference/WorldChunkGeneratedAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## chunkLoad {#chunkLoad}

```python
chunkLoad: NativeEventSignal[WorldChunkLoadAfterEvent]
```

原生事件信号：[ChunkLoadedServerEvent](../native-events.md#chunkloadedserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldChunkLoadAfterEvent](../reference/WorldChunkLoadAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## clientReady {#clientReady}

```python
clientReady: NativeEventSignal[WorldClientReadyAfterEvent]
```

原生事件信号：[ClientLoadAddonsFinishServerEvent](../native-events.md#clientloadaddonsfinishserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldClientReadyAfterEvent](../reference/WorldClientReadyAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## commandOutput {#commandOutput}

```python
commandOutput: NativeEventSignal[WorldCommandOutputAfterEvent]
```

原生事件信号：[OnCommandOutputServerEvent](../native-events.md#oncommandoutputserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldCommandOutputAfterEvent](../reference/WorldCommandOutputAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## containerItemChange {#containerItemChange}

```python
containerItemChange: NativeEventSignal[WorldContainerItemChangeAfterEvent]
```

原生事件信号：[ContainerItemChangedServerEvent](../native-events.md#containeritemchangedserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldContainerItemChangeAfterEvent](../reference/WorldContainerItemChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## dirtBlockToGrassBlock {#dirtBlockToGrassBlock}

```python
dirtBlockToGrassBlock: NativeEventSignal[WorldDirtBlockToGrassBlockAfterEvent]
```

原生事件信号：[DirtBlockToGrassBlockServerEvent](../native-events.md#dirtblocktograssblockserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldDirtBlockToGrassBlockAfterEvent](../reference/WorldDirtBlockToGrassBlockAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityChangeDimension {#entityChangeDimension}

```python
entityChangeDimension: NativeEventSignal[WorldEntityChangeDimensionAfterEvent]
```

原生事件信号：[EntityChangeDimensionServerEvent](../native-events.md#entitychangedimensionserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityChangeDimensionAfterEvent](../reference/WorldEntityChangeDimensionAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityCollide {#entityCollide}

```python
entityCollide: NativeEventSignal[WorldEntityCollideAfterEvent]
```

原生事件信号：[OnMobHitMobServerEvent](../native-events.md#onmobhitmobserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityCollideAfterEvent](../reference/WorldEntityCollideAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityDroppedItem {#entityDroppedItem}

```python
entityDroppedItem: NativeEventSignal[WorldEntityDroppedItemAfterEvent]
```

原生事件信号：[EntityDroppedItemServerEvent](../native-events.md#entitydroppeditemserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityDroppedItemAfterEvent](../reference/WorldEntityDroppedItemAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityEffectDamage {#entityEffectDamage}

```python
entityEffectDamage: NativeEventSignal[WorldEntityEffectDamageAfterEvent]
```

原生事件信号：[EntityEffectDamageServerEvent](../native-events.md#entityeffectdamageserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityEffectDamageAfterEvent](../reference/WorldEntityEffectDamageAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityHitBlock {#entityHitBlock}

```python
entityHitBlock: NativeEventSignal[WorldEntityHitBlockAfterEvent]
```

原生事件信号：[OnMobHitBlockServerEvent](../native-events.md#onmobhitblockserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityHitBlockAfterEvent](../reference/WorldEntityHitBlockAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityKnockback {#entityKnockback}

```python
entityKnockback: NativeEventSignal[WorldEntityKnockbackAfterEvent]
```

原生事件信号：[OnKnockBackServerEvent](../native-events.md#onknockbackserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityKnockbackAfterEvent](../reference/WorldEntityKnockbackAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityLand {#entityLand}

```python
entityLand: NativeEventSignal[WorldEntityLandAfterEvent]
```

原生事件信号：[OnGroundServerEvent](../native-events.md#ongroundserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityLandAfterEvent](../reference/WorldEntityLandAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityLoadScript {#entityLoadScript}

```python
entityLoadScript: NativeEventSignal[WorldEntityLoadScriptAfterEvent]
```

原生事件信号：[EntityLoadScriptEvent](../native-events.md#entityloadscriptevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityLoadScriptAfterEvent](../reference/WorldEntityLoadScriptAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityLoot {#entityLoot}

```python
entityLoot: NativeEventSignal[WorldEntityLootAfterEvent]
```

原生事件信号：[EntityDieLoottableAfterServerEvent](../native-events.md#entitydieloottableafterserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityLootAfterEvent](../reference/WorldEntityLootAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityMotionStart {#entityMotionStart}

```python
entityMotionStart: NativeEventSignal[WorldEntityMotionStartAfterEvent]
```

原生事件信号：[EntityMotionStartServerEvent](../native-events.md#entitymotionstartserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityMotionStartAfterEvent](../reference/WorldEntityMotionStartAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityPickupItem {#entityPickupItem}

```python
entityPickupItem: NativeEventSignal[WorldEntityPickupItemAfterEvent]
```

原生事件信号：[EntityPickupItemServerEvent](../native-events.md#entitypickupitemserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityPickupItemAfterEvent](../reference/WorldEntityPickupItemAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityPlaceBlock {#entityPlaceBlock}

```python
entityPlaceBlock: NativeEventSignal[WorldEntityPlaceBlockAfterEvent]
```

原生事件信号：[EntityPlaceBlockAfterServerEvent](../native-events.md#entityplaceblockafterserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityPlaceBlockAfterEvent](../reference/WorldEntityPlaceBlockAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityStartRiding {#entityStartRiding}

```python
entityStartRiding: NativeEventSignal[WorldEntityStartRidingAfterEvent]
```

原生事件信号：[EntityStartRidingEvent](../native-events.md#entitystartridingevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityStartRidingAfterEvent](../reference/WorldEntityStartRidingAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityTame {#entityTame}

```python
entityTame: NativeEventSignal[WorldEntityTameAfterEvent]
```

原生事件信号：[MountTamingEvent](../native-events.md#mounttamingevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityTameAfterEvent](../reference/WorldEntityTameAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityTick {#entityTick}

```python
entityTick: NativeEventSignal[WorldEntityTickAfterEvent]
```

原生事件信号：[EntityTickServerEvent](../native-events.md#entitytickserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldEntityTickAfterEvent](../reference/WorldEntityTickAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fallingBlockReturnHeavyBlock {#fallingBlockReturnHeavyBlock}

```python
fallingBlockReturnHeavyBlock: NativeEventSignal[WorldFallingBlockReturnHeavyBlockAfterEvent]
```

原生事件信号：[FallingBlockReturnHeavyBlockServerEvent](../native-events.md#fallingblockreturnheavyblockserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldFallingBlockReturnHeavyBlockAfterEvent](../reference/WorldFallingBlockReturnHeavyBlockAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## farmBlockToDirtBlock {#farmBlockToDirtBlock}

```python
farmBlockToDirtBlock: NativeEventSignal[WorldFarmBlockToDirtBlockAfterEvent]
```

原生事件信号：[FarmBlockToDirtBlockServerEvent](../native-events.md#farmblocktodirtblockserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldFarmBlockToDirtBlockAfterEvent](../reference/WorldFarmBlockToDirtBlockAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## furnaceBurnFinish {#furnaceBurnFinish}

```python
furnaceBurnFinish: NativeEventSignal[WorldFurnaceBurnFinishAfterEvent]
```

原生事件信号：[FurnaceBurnFinishedServerEvent](../native-events.md#furnaceburnfinishedserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldFurnaceBurnFinishAfterEvent](../reference/WorldFurnaceBurnFinishAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## gameTypeChange {#gameTypeChange}

```python
gameTypeChange: NativeEventSignal[WorldGameTypeChangeAfterEvent]
```

原生事件信号：[GameTypeChangedServerEvent](../native-events.md#gametypechangedserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldGameTypeChangeAfterEvent](../reference/WorldGameTypeChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## grassBlockToDirtBlock {#grassBlockToDirtBlock}

```python
grassBlockToDirtBlock: NativeEventSignal[WorldGrassBlockToDirtBlockAfterEvent]
```

原生事件信号：[GrassBlockToDirtBlockServerEvent](../native-events.md#grassblocktodirtblockserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldGrassBlockToDirtBlockAfterEvent](../reference/WorldGrassBlockToDirtBlockAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## heavyBlockStartFalling {#heavyBlockStartFalling}

```python
heavyBlockStartFalling: NativeEventSignal[WorldHeavyBlockStartFallingAfterEvent]
```

原生事件信号：[HeavyBlockStartFallingServerEvent](../native-events.md#heavyblockstartfallingserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldHeavyBlockStartFallingAfterEvent](../reference/WorldHeavyBlockStartFallingAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## hopperTryPullIn {#hopperTryPullIn}

```python
hopperTryPullIn: NativeEventSignal[WorldHopperTryPullInAfterEvent]
```

原生事件信号：[HopperTryPullInServerEvent](../native-events.md#hoppertrypullinserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldHopperTryPullInAfterEvent](../reference/WorldHopperTryPullInAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## hopperTryPullOut {#hopperTryPullOut}

```python
hopperTryPullOut: NativeEventSignal[WorldHopperTryPullOutAfterEvent]
```

原生事件信号：[HopperTryPullOutServerEvent](../native-events.md#hoppertrypulloutserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldHopperTryPullOutAfterEvent](../reference/WorldHopperTryPullOutAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## jumpAnimBegin {#jumpAnimBegin}

```python
jumpAnimBegin: NativeEventSignal[WorldJumpAnimBeginAfterEvent]
```

原生事件信号：[JumpAnimBeginServerEvent](../native-events.md#jumpanimbeginserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldJumpAnimBeginAfterEvent](../reference/WorldJumpAnimBeginAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## liquidClipped {#liquidClipped}

```python
liquidClipped: NativeEventSignal[WorldLiquidClippedAfterEvent]
```

原生事件信号：[LiquidClippedServerEvent](../native-events.md#liquidclippedserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldLiquidClippedAfterEvent](../reference/WorldLiquidClippedAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## lobbyPurchase {#lobbyPurchase}

```python
lobbyPurchase: NativeEventSignal[WorldLobbyPurchaseAfterEvent]
```

原生事件信号：[lobbyGoodBuySucServerEvent](../native-events.md#lobbygoodbuysucserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldLobbyPurchaseAfterEvent](../reference/WorldLobbyPurchaseAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## placeBlockEntity {#placeBlockEntity}

```python
placeBlockEntity: NativeEventSignal[WorldPlaceBlockEntityAfterEvent]
```

原生事件信号：[ServerPlaceBlockEntityEvent](../native-events.md#serverplaceblockentityevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlaceBlockEntityAfterEvent](../reference/WorldPlaceBlockEntityAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerAdd {#playerAdd}

```python
playerAdd: NativeEventSignal[WorldPlayerAddAfterEvent]
```

原生事件信号：[AddServerPlayerEvent](../native-events.md#addserverplayerevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerAddAfterEvent](../reference/WorldPlayerAddAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerAddCustomContainerItem {#playerAddCustomContainerItem}

```python
playerAddCustomContainerItem: NativeEventSignal[WorldPlayerAddCustomContainerItemAfterEvent]
```

原生事件信号：[PlayerAddCustomContainerItemServerEvent](../native-events.md#playeraddcustomcontaineritemserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerAddCustomContainerItemAfterEvent](../reference/WorldPlayerAddCustomContainerItemAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerBlockedByShield {#playerBlockedByShield}

```python
playerBlockedByShield: NativeEventSignal[WorldPlayerBlockedByShieldAfterEvent]
```

原生事件信号：[OnPlayerBlockedByShieldAfterServerEvent](../native-events.md#onplayerblockedbyshieldafterserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerBlockedByShieldAfterEvent](../reference/WorldPlayerBlockedByShieldAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerCheatSpinAttack {#playerCheatSpinAttack}

```python
playerCheatSpinAttack: NativeEventSignal[WorldPlayerCheatSpinAttackAfterEvent]
```

原生事件信号：[PlayerCheatSpinAttackServerEvent](../native-events.md#playercheatspinattackserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerCheatSpinAttackAfterEvent](../reference/WorldPlayerCheatSpinAttackAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerDie {#playerDie}

```python
playerDie: NativeEventSignal[WorldPlayerDieAfterEvent]
```

原生事件信号：[PlayerDieEvent](../native-events.md#playerdieevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerDieAfterEvent](../reference/WorldPlayerDieAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerDimensionChangeFinish {#playerDimensionChangeFinish}

```python
playerDimensionChangeFinish: NativeEventSignal[WorldPlayerDimensionChangeFinishAfterEvent]
```

原生事件信号：[DimensionChangeFinishServerEvent](../native-events.md#dimensionchangefinishserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerDimensionChangeFinishAfterEvent](../reference/WorldPlayerDimensionChangeFinishAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerDropItem {#playerDropItem}

```python
playerDropItem: NativeEventSignal[WorldPlayerDropItemAfterEvent]
```

原生事件信号：[PlayerDropItemServerEvent](../native-events.md#playerdropitemserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerDropItemAfterEvent](../reference/WorldPlayerDropItemAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerExperienceAdd {#playerExperienceAdd}

```python
playerExperienceAdd: NativeEventSignal[WorldPlayerExperienceAddAfterEvent]
```

原生事件信号：[AddExpEvent](../native-events.md#addexpevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerExperienceAddAfterEvent](../reference/WorldPlayerExperienceAddAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerFishing {#playerFishing}

```python
playerFishing: NativeEventSignal[WorldPlayerFishingAfterEvent]
```

原生事件信号：[PlayerFishingAfterServerEvent](../native-events.md#playerfishingafterserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerFishingAfterEvent](../reference/WorldPlayerFishingAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerHitBlock {#playerHitBlock}

```python
playerHitBlock: NativeEventSignal[WorldPlayerHitBlockAfterEvent]
```

原生事件信号：[OnPlayerHitBlockServerEvent](../native-events.md#onplayerhitblockserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerHitBlockAfterEvent](../reference/WorldPlayerHitBlockAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerInventoryOpenScript {#playerInventoryOpenScript}

```python
playerInventoryOpenScript: NativeEventSignal[WorldPlayerInventoryOpenScriptAfterEvent]
```

原生事件信号：[PlayerInventoryOpenScriptServerEvent](../native-events.md#playerinventoryopenscriptserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerInventoryOpenScriptAfterEvent](../reference/WorldPlayerInventoryOpenScriptAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerLevelChange {#playerLevelChange}

```python
playerLevelChange: NativeEventSignal[WorldPlayerLevelChangeAfterEvent]
```

原生事件信号：[AddLevelEvent](../native-events.md#addlevelevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerLevelChangeAfterEvent](../reference/WorldPlayerLevelChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerRemove {#playerRemove}

```python
playerRemove: NativeEventSignal[WorldPlayerRemoveAfterEvent]
```

原生事件信号：[DelServerPlayerEvent](../native-events.md#delserverplayerevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerRemoveAfterEvent](../reference/WorldPlayerRemoveAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerRemoveCustomContainerItem {#playerRemoveCustomContainerItem}

```python
playerRemoveCustomContainerItem: NativeEventSignal[WorldPlayerRemoveCustomContainerItemAfterEvent]
```

原生事件信号：[PlayerRemoveCustomContainerItemServerEvent](../native-events.md#playerremovecustomcontaineritemserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerRemoveCustomContainerItemAfterEvent](../reference/WorldPlayerRemoveCustomContainerItemAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerRespawn {#playerRespawn}

```python
playerRespawn: NativeEventSignal[WorldPlayerRespawnAfterEvent]
```

原生事件信号：[PlayerRespawnEvent](../native-events.md#playerrespawnevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerRespawnAfterEvent](../reference/WorldPlayerRespawnAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerSleep {#playerSleep}

```python
playerSleep: NativeEventSignal[WorldPlayerSleepAfterEvent]
```

原生事件信号：[PlayerSleepServerEvent](../native-events.md#playersleepserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerSleepAfterEvent](../reference/WorldPlayerSleepAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerSpinAttack {#playerSpinAttack}

```python
playerSpinAttack: NativeEventSignal[WorldPlayerSpinAttackAfterEvent]
```

原生事件信号：[PlayerSpinAttackServerEvent](../native-events.md#playerspinattackserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerSpinAttackAfterEvent](../reference/WorldPlayerSpinAttackAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerStopSleep {#playerStopSleep}

```python
playerStopSleep: NativeEventSignal[WorldPlayerStopSleepAfterEvent]
```

原生事件信号：[PlayerStopSleepServerEvent](../native-events.md#playerstopsleepserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerStopSleepAfterEvent](../reference/WorldPlayerStopSleepAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerTeleport {#playerTeleport}

```python
playerTeleport: NativeEventSignal[WorldPlayerTeleportAfterEvent]
```

原生事件信号：[PlayerTeleportEvent](../native-events.md#playerteleportevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldPlayerTeleportAfterEvent](../reference/WorldPlayerTeleportAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## projectileCritHit {#projectileCritHit}

```python
projectileCritHit: NativeEventSignal[WorldProjectileCritHitAfterEvent]
```

原生事件信号：[ProjectileCritHitEvent](../native-events.md#projectilecrithitevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldProjectileCritHitAfterEvent](../reference/WorldProjectileCritHitAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## scriptsLoad {#scriptsLoad}

```python
scriptsLoad: NativeEventSignal[WorldScriptsLoadAfterEvent]
```

原生事件信号：[LoadServerAddonScriptsAfter](../native-events.md#loadserveraddonscriptsafter)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldScriptsLoadAfterEvent](../reference/WorldScriptsLoadAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## spawnProjectile {#spawnProjectile}

```python
spawnProjectile: NativeEventSignal[WorldSpawnProjectileAfterEvent]
```

原生事件信号：[SpawnProjectileServerEvent](../native-events.md#spawnprojectileserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldSpawnProjectileAfterEvent](../reference/WorldSpawnProjectileAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## stepOffBlock {#stepOffBlock}

```python
stepOffBlock: NativeEventSignal[WorldStepOffBlockAfterEvent]
```

原生事件信号：[StepOffBlockServerEvent](../native-events.md#stepoffblockserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldStepOffBlockAfterEvent](../reference/WorldStepOffBlockAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## storeBuySucc {#storeBuySucc}

```python
storeBuySucc: NativeEventSignal[WorldStoreBuySuccAfterEvent]
```

原生事件信号：[StoreBuySuccServerEvent](../native-events.md#storebuysuccserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldStoreBuySuccAfterEvent](../reference/WorldStoreBuySuccAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## tick {#tick}

```python
tick: NativeEventSignal[WorldTickAfterEvent]
```

原生事件信号：[OnScriptTickServer](../native-events.md#onscripttickserver)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldTickAfterEvent](../reference/WorldTickAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## uiContainerItemChange {#uiContainerItemChange}

```python
uiContainerItemChange: NativeEventSignal[WorldUiContainerItemChangeAfterEvent]
```

原生事件信号：[UIContainerItemChangedServerEvent](../native-events.md#uicontaineritemchangedserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldUiContainerItemChangeAfterEvent](../reference/WorldUiContainerItemChangeAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## urgeShip {#urgeShip}

```python
urgeShip: NativeEventSignal[WorldUrgeShipAfterEvent]
```

原生事件信号：[UrgeShipEvent](../native-events.md#urgeshipevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldUrgeShipAfterEvent](../reference/WorldUrgeShipAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## walkAnimBegin {#walkAnimBegin}

```python
walkAnimBegin: NativeEventSignal[WorldWalkAnimBeginAfterEvent]
```

原生事件信号：[WalkAnimBeginServerEvent](../native-events.md#walkanimbeginserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldWalkAnimBeginAfterEvent](../reference/WorldWalkAnimBeginAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## walkAnimEnd {#walkAnimEnd}

```python
walkAnimEnd: NativeEventSignal[WorldWalkAnimEndAfterEvent]
```

原生事件信号：[WalkAnimEndServerEvent](../native-events.md#walkanimendserverevent)。参数类型及触发前提见对应类型页和原生事件目录。

**访问：** 只读。

**返回类型：** [NativeEventSignal](../../common/reference/NativeEventSignal.md)[[WorldWalkAnimEndAfterEvent](../reference/WorldWalkAnimEndAfterEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerStateChange {#playerStateChange}

```python
playerStateChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnPlayerActionServerEvent](../native-events.md#onplayeractionserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerSneakChange {#playerSneakChange}

```python
playerSneakChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnPlayerActionServerEvent](../native-events.md#onplayeractionserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerSprintChange {#playerSprintChange}

```python
playerSprintChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnPlayerActionServerEvent](../native-events.md#onplayeractionserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerGlideChange {#playerGlideChange}

```python
playerGlideChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnPlayerActionServerEvent](../native-events.md#onplayeractionserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerSwimChange {#playerSwimChange}

```python
playerSwimChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnPlayerActionServerEvent](../native-events.md#onplayeractionserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerCrawlChange {#playerCrawlChange}

```python
playerCrawlChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnPlayerActionServerEvent](../native-events.md#onplayeractionserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerFlyChange {#playerFlyChange}

```python
playerFlyChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnPlayerActionServerEvent](../native-events.md#onplayeractionserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerSleepChange {#playerSleepChange}

```python
playerSleepChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnPlayerActionServerEvent](../native-events.md#onplayeractionserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playerSpinAttackChange {#playerSpinAttackChange}

```python
playerSpinAttackChange: EventSignal[PlayerStateChangeEvent]
```

玩家状态事件，支持订阅筛选。原生来源：[OnPlayerActionServerEvent](../native-events.md#onplayeractionserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PlayerStateChangeEvent](../../common/reference/PlayerStateChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## equipmentChange {#equipmentChange}

```python
equipmentChange: EventSignal[InventoryChangeEvent]
```

库存变化事件，支持订阅筛选。原生来源：[OnCarriedNewItemChangedServerEvent](../native-events.md#oncarriednewitemchangedserverevent), [OnOffhandItemChangedServerEvent](../native-events.md#onoffhanditemchangedserverevent), [OnNewArmorExchangeServerEvent](../native-events.md#onnewarmorexchangeserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[InventoryChangeEvent](../../common/reference/InventoryChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## physicsContactBegin {#physicsContactBegin}

```python
physicsContactBegin: EventSignal[PhysicsContactEvent]
```

物理接触事件，支持订阅筛选。原生来源：[PhysxTouchServerEvent](../native-events.md#physxtouchserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PhysicsContactEvent](../../common/reference/PhysicsContactEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## physicsContactEnd {#physicsContactEnd}

```python
physicsContactEnd: EventSignal[PhysicsContactEvent]
```

物理接触事件，支持订阅筛选。原生来源：[PhysxTouchServerEvent](../native-events.md#physxtouchserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PhysicsContactEvent](../../common/reference/PhysicsContactEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## physicsTriggerEnter {#physicsTriggerEnter}

```python
physicsTriggerEnter: EventSignal[PhysicsContactEvent]
```

物理接触事件，支持订阅筛选。原生来源：[PhysxTriggerServerEvent](../native-events.md#physxtriggerserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PhysicsContactEvent](../../common/reference/PhysicsContactEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## physicsTriggerLeave {#physicsTriggerLeave}

```python
physicsTriggerLeave: EventSignal[PhysicsContactEvent]
```

物理接触事件，支持订阅筛选。原生来源：[PhysxTriggerServerEvent](../native-events.md#physxtriggerserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[PhysicsContactEvent](../../common/reference/PhysicsContactEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityEnterArea {#entityEnterArea}

```python
entityEnterArea: EventSignal[EntityAreaEvent]
```

兴趣区域事件，支持订阅筛选。原生来源：[NewOnEntityAreaEvent](../native-events.md#newonentityareaevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[EntityAreaEvent](../../common/reference/EntityAreaEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entityLeaveArea {#entityLeaveArea}

```python
entityLeaveArea: EventSignal[EntityAreaEvent]
```

兴趣区域事件，支持订阅筛选。原生来源：[NewOnEntityAreaEvent](../native-events.md#newonentityareaevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[EntityAreaEvent](../../common/reference/EntityAreaEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## effectRefresh {#effectRefresh}

```python
effectRefresh: EventSignal[EffectChangeEvent]
```

效果变化事件，支持订阅筛选。原生来源：[RefreshEffectServerEvent](../native-events.md#refresheffectserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[EffectChangeEvent](../../common/reference/EffectChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## effectRemove {#effectRemove}

```python
effectRemove: EventSignal[EffectChangeEvent]
```

效果变化事件，支持订阅筛选。原生来源：[RemoveEffectServerEvent](../native-events.md#removeeffectserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[EffectChangeEvent](../../common/reference/EffectChangeEvent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## weatherChange {#weatherChange}

```python
weatherChange: EventSignal[WeatherLevelChangeEvent]
```

天气强度事件，支持订阅筛选。原生来源：[OnRainLevelChangeServerEvent](../native-events.md#onrainlevelchangeserverevent), [OnLightningLevelChangeServerEvent](../native-events.md#onlightninglevelchangeserverevent), [OnLocalRainLevelChangeServerEvent](../native-events.md#onlocalrainlevelchangeserverevent), [OnLocalLightningLevelChangeServerEvent](../native-events.md#onlocallightninglevelchangeserverevent)。

**访问：** 只读。

**返回类型：** [EventSignal](../../common/reference/EventSignal.md)[[WeatherLevelChangeEvent](../../common/reference/WeatherLevelChangeEvent.md)]。静态声明不替代本页的实现限制。

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
    # value 是上方获取方式取得的 WorldAfterEvents 对象。
    print(value.dataDrivenEntityTrigger)
    print(value.entityDie)
    print(value.effectAdd)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)