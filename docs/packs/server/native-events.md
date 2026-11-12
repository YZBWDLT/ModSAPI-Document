---
sidebar_position: 3
title: 服务端原生事件目录
---

# 服务端原生事件目录

本目录逐项对应 ModSDK 文档事件索引，包含 **178 个事件绑定**。

属性名称采用 lowerCamelCase；保留准确的原生事件名用于检索。前置或可写引擎钩子放在 `beforeEvents`，通知放在 `afterEvents`。原生名称带 After 的钩子仍可能在后续力学计算前接收可写输出，按字段契约归入 before。

每项都提供独立类型、订阅示例、字段说明和原生前提。索引覆盖不意味着所有网易引擎版本、平台或资源配置都会触发这些事件。

**常用业务优先使用 [语义化事件与筛选](../guides/semantic-events.md)**：多个原生事件可以合并为统一入口，一个原生事件也可以拆成多个有明确用途的信号。下面保留准确的原生契约用于高级场景。

[原生用法、取消语义与错误处理](../guides/native-events.md)

## 全部事件

| 原生事件 | 信号属性 | 可写输出 | 平台 |
| --- | --- | --- | --- |
| [AchievementCompleteEvent](#achievementcompleteevent) | [world.afterEvents.achievementComplete](events/afterEvents.md#achievementComplete) | 无 | ModSDK |
| [ActorAcquiredItemServerEvent](#actoracquireditemserverevent) | [world.afterEvents.actorAcquiredItem](events/afterEvents.md#actorAcquiredItem) | 无 | ModSDK |
| [ActorHurtServerEvent](#actorhurtserverevent) | [world.afterEvents.actorHurt](events/afterEvents.md#actorHurt) | 无 | ModSDK |
| [AttackAnimBeginServerEvent](#attackanimbeginserverevent) | [world.afterEvents.attackAnimBegin](events/afterEvents.md#attackAnimBegin) | 无 | ModSDK |
| [AttackAnimEndServerEvent](#attackanimendserverevent) | [world.afterEvents.attackAnimEnd](events/afterEvents.md#attackAnimEnd) | 无 | ModSDK |
| [BlockDestroyByLiquidServerEvent](#blockdestroybyliquidserverevent) | [world.afterEvents.blockDestroyByLiquid](events/afterEvents.md#blockDestroyByLiquid) | 无 | ModSDK |
| [ServerBlockEntityTickEvent](#serverblockentitytickevent) | [world.afterEvents.blockEntityTick](events/afterEvents.md#blockEntityTick) | 无 | ModSDK |
| [BlockLiquidStateChangeAfterServerEvent](#blockliquidstatechangeafterserverevent) | [world.afterEvents.blockLiquidStateChange](events/afterEvents.md#blockLiquidStateChange) | 无 | ModSDK |
| [BlockNeighborChangedServerEvent](#blockneighborchangedserverevent) | [world.afterEvents.blockNeighborChange](events/afterEvents.md#blockNeighborChange) | 无 | ModSDK |
| [ServerPostBlockPatternEvent](#serverpostblockpatternevent) | [world.afterEvents.blockPattern](events/afterEvents.md#blockPattern) | 无 | ModSDK |
| [BlockRandomTickServerEvent](#blockrandomtickserverevent) | [world.afterEvents.blockRandomTick](events/afterEvents.md#blockRandomTick) | 无 | ModSDK |
| [BlockRemoveServerEvent](#blockremoveserverevent) | [world.afterEvents.blockRemove](events/afterEvents.md#blockRemove) | 无 | ModSDK |
| [BlockSnowStateChangeAfterServerEvent](#blocksnowstatechangeafterserverevent) | [world.afterEvents.blockSnowStateChange](events/afterEvents.md#blockSnowStateChange) | 无 | ModSDK |
| [BlockStrengthChangedServerEvent](#blockstrengthchangedserverevent) | [world.afterEvents.blockStrengthChange](events/afterEvents.md#blockStrengthChange) | 无 | ModSDK |
| [ChangeSwimStateServerEvent](#changeswimstateserverevent) | [world.afterEvents.changeSwimState](events/afterEvents.md#changeSwimState) | 无 | ModSDK |
| [ChunkGeneratedServerEvent](#chunkgeneratedserverevent) | [world.afterEvents.chunkGenerated](events/afterEvents.md#chunkGenerated) | 无 | ModSDK |
| [ChunkLoadedServerEvent](#chunkloadedserverevent) | [world.afterEvents.chunkLoad](events/afterEvents.md#chunkLoad) | 无 | ModSDK |
| [ClientLoadAddonsFinishServerEvent](#clientloadaddonsfinishserverevent) | [world.afterEvents.clientReady](events/afterEvents.md#clientReady) | 无 | ModSDK |
| [OnCommandOutputServerEvent](#oncommandoutputserverevent) | [world.afterEvents.commandOutput](events/afterEvents.md#commandOutput) | 无 | ModSDK |
| [ContainerItemChangedServerEvent](#containeritemchangedserverevent) | [world.afterEvents.containerItemChange](events/afterEvents.md#containerItemChange) | 无 | ModSDK |
| [DestroyBlockEvent](#destroyblockevent) | `world.afterEvents.getNativeEvent('DestroyBlockEvent')` | 无 | ModSDK |
| [DirtBlockToGrassBlockServerEvent](#dirtblocktograssblockserverevent) | [world.afterEvents.dirtBlockToGrassBlock](events/afterEvents.md#dirtBlockToGrassBlock) | 无 | ModSDK |
| [RefreshEffectServerEvent](#refresheffectserverevent) | `world.afterEvents.getNativeEvent('RefreshEffectServerEvent')` | 无 | ModSDK |
| [RemoveEffectServerEvent](#removeeffectserverevent) | `world.afterEvents.getNativeEvent('RemoveEffectServerEvent')` | 无 | ModSDK |
| [AddEntityServerEvent](#addentityserverevent) | `world.afterEvents.getNativeEvent('AddEntityServerEvent')` | 无 | ModSDK |
| [NewOnEntityAreaEvent](#newonentityareaevent) | `world.afterEvents.getNativeEvent('NewOnEntityAreaEvent')` | 无 | ModSDK |
| [EntityChangeDimensionServerEvent](#entitychangedimensionserverevent) | [world.afterEvents.entityChangeDimension](events/afterEvents.md#entityChangeDimension) | 无 | ModSDK |
| [OnMobHitMobServerEvent](#onmobhitmobserverevent) | [world.afterEvents.entityCollide](events/afterEvents.md#entityCollide) | 无 | ModSDK |
| [EntityDefinitionsEventServerEvent](#entitydefinitionseventserverevent) | `world.afterEvents.getNativeEvent('EntityDefinitionsEventServerEvent')` | 无 | ModSDK |
| [EntityDroppedItemServerEvent](#entitydroppeditemserverevent) | [world.afterEvents.entityDroppedItem](events/afterEvents.md#entityDroppedItem) | 无 | ModSDK |
| [EntityEffectDamageServerEvent](#entityeffectdamageserverevent) | [world.afterEvents.entityEffectDamage](events/afterEvents.md#entityEffectDamage) | 无 | ModSDK |
| [OnMobHitBlockServerEvent](#onmobhitblockserverevent) | [world.afterEvents.entityHitBlock](events/afterEvents.md#entityHitBlock) | 无 | ModSDK |
| [OnKnockBackServerEvent](#onknockbackserverevent) | [world.afterEvents.entityKnockback](events/afterEvents.md#entityKnockback) | 无 | ModSDK |
| [OnGroundServerEvent](#ongroundserverevent) | [world.afterEvents.entityLand](events/afterEvents.md#entityLand) | 无 | ModSDK |
| [EntityLoadScriptEvent](#entityloadscriptevent) | [world.afterEvents.entityLoadScript](events/afterEvents.md#entityLoadScript) | 无 | ModSDK |
| [EntityDieLoottableAfterServerEvent](#entitydieloottableafterserverevent) | [world.afterEvents.entityLoot](events/afterEvents.md#entityLoot) | 无 | ModSDK |
| [EntityMotionStartServerEvent](#entitymotionstartserverevent) | [world.afterEvents.entityMotionStart](events/afterEvents.md#entityMotionStart) | 无 | ModSDK |
| [EntityPickupItemServerEvent](#entitypickupitemserverevent) | [world.afterEvents.entityPickupItem](events/afterEvents.md#entityPickupItem) | 无 | ModSDK |
| [EntityPlaceBlockAfterServerEvent](#entityplaceblockafterserverevent) | [world.afterEvents.entityPlaceBlock](events/afterEvents.md#entityPlaceBlock) | 无 | ModSDK |
| [EntityRemoveEvent](#entityremoveevent) | `world.afterEvents.getNativeEvent('EntityRemoveEvent')` | 无 | ModSDK |
| [EntityStartRidingEvent](#entitystartridingevent) | [world.afterEvents.entityStartRiding](events/afterEvents.md#entityStartRiding) | 无 | ModSDK |
| [MountTamingEvent](#mounttamingevent) | [world.afterEvents.entityTame](events/afterEvents.md#entityTame) | 无 | ModSDK |
| [EntityTickServerEvent](#entitytickserverevent) | [world.afterEvents.entityTick](events/afterEvents.md#entityTick) | 无 | ModSDK |
| [FallingBlockReturnHeavyBlockServerEvent](#fallingblockreturnheavyblockserverevent) | [world.afterEvents.fallingBlockReturnHeavyBlock](events/afterEvents.md#fallingBlockReturnHeavyBlock) | 无 | ModSDK |
| [FarmBlockToDirtBlockServerEvent](#farmblocktodirtblockserverevent) | [world.afterEvents.farmBlockToDirtBlock](events/afterEvents.md#farmBlockToDirtBlock) | 无 | ModSDK |
| [FurnaceBurnFinishedServerEvent](#furnaceburnfinishedserverevent) | [world.afterEvents.furnaceBurnFinish](events/afterEvents.md#furnaceBurnFinish) | 无 | ModSDK |
| [GameTypeChangedServerEvent](#gametypechangedserverevent) | [world.afterEvents.gameTypeChange](events/afterEvents.md#gameTypeChange) | 无 | ModSDK |
| [GrassBlockToDirtBlockServerEvent](#grassblocktodirtblockserverevent) | [world.afterEvents.grassBlockToDirtBlock](events/afterEvents.md#grassBlockToDirtBlock) | 无 | ModSDK |
| [HeavyBlockStartFallingServerEvent](#heavyblockstartfallingserverevent) | [world.afterEvents.heavyBlockStartFalling](events/afterEvents.md#heavyBlockStartFalling) | 无 | ModSDK |
| [HopperTryPullInServerEvent](#hoppertrypullinserverevent) | [world.afterEvents.hopperTryPullIn](events/afterEvents.md#hopperTryPullIn) | 无 | ModSDK |
| [HopperTryPullOutServerEvent](#hoppertrypulloutserverevent) | [world.afterEvents.hopperTryPullOut](events/afterEvents.md#hopperTryPullOut) | 无 | ModSDK |
| [ItemUseAfterServerEvent](#itemuseafterserverevent) | `world.afterEvents.getNativeEvent('ItemUseAfterServerEvent')` | 无 | ModSDK |
| [ItemUseOnAfterServerEvent](#itemuseonafterserverevent) | `world.afterEvents.getNativeEvent('ItemUseOnAfterServerEvent')` | 无 | ModSDK |
| [JumpAnimBeginServerEvent](#jumpanimbeginserverevent) | [world.afterEvents.jumpAnimBegin](events/afterEvents.md#jumpAnimBegin) | 无 | ModSDK |
| [OnLightningLevelChangeServerEvent](#onlightninglevelchangeserverevent) | `world.afterEvents.getNativeEvent('OnLightningLevelChangeServerEvent')` | 无 | ModSDK |
| [LiquidClippedServerEvent](#liquidclippedserverevent) | [world.afterEvents.liquidClipped](events/afterEvents.md#liquidClipped) | 无 | ModSDK |
| [lobbyGoodBuySucServerEvent](#lobbygoodbuysucserverevent) | [world.afterEvents.lobbyPurchase](events/afterEvents.md#lobbyPurchase) | 无 | ModSDK |
| [OnLocalLightningLevelChangeServerEvent](#onlocallightninglevelchangeserverevent) | `world.afterEvents.getNativeEvent('OnLocalLightningLevelChangeServerEvent')` | 无 | ModSDK |
| [OnLocalRainLevelChangeServerEvent](#onlocalrainlevelchangeserverevent) | `world.afterEvents.getNativeEvent('OnLocalRainLevelChangeServerEvent')` | 无 | ModSDK |
| [MobDieEvent](#mobdieevent) | `world.afterEvents.getNativeEvent('MobDieEvent')` | 无 | ModSDK |
| [AddEffectServerEvent](#addeffectserverevent) | `world.afterEvents.getNativeEvent('AddEffectServerEvent')` | 无 | ModSDK |
| [HealthChangeServerEvent](#healthchangeserverevent) | `world.afterEvents.getNativeEvent('HealthChangeServerEvent')` | 无 | ModSDK |
| [InventoryItemChangedServerEvent](#inventoryitemchangedserverevent) | `world.afterEvents.getNativeEvent('InventoryItemChangedServerEvent')` | 无 | ModSDK |
| [PhysxTouchServerEvent](#physxtouchserverevent) | `world.afterEvents.getNativeEvent('PhysxTouchServerEvent')` | 无 | ModSDK |
| [PhysxTriggerServerEvent](#physxtriggerserverevent) | `world.afterEvents.getNativeEvent('PhysxTriggerServerEvent')` | 无 | ModSDK |
| [ServerPlaceBlockEntityEvent](#serverplaceblockentityevent) | [world.afterEvents.placeBlockEntity](events/afterEvents.md#placeBlockEntity) | 无 | ModSDK |
| [OnPlayerActionServerEvent](#onplayeractionserverevent) | `world.afterEvents.getNativeEvent('OnPlayerActionServerEvent')` | 无 | ModSDK |
| [AddServerPlayerEvent](#addserverplayerevent) | [world.afterEvents.playerAdd](events/afterEvents.md#playerAdd) | 无 | ModSDK |
| [PlayerAddCustomContainerItemServerEvent](#playeraddcustomcontaineritemserverevent) | [world.afterEvents.playerAddCustomContainerItem](events/afterEvents.md#playerAddCustomContainerItem) | 无 | ModSDK |
| [OnNewArmorExchangeServerEvent](#onnewarmorexchangeserverevent) | `world.afterEvents.getNativeEvent('OnNewArmorExchangeServerEvent')` | 无 | ModSDK |
| [OnPlayerBlockedByShieldAfterServerEvent](#onplayerblockedbyshieldafterserverevent) | [world.afterEvents.playerBlockedByShield](events/afterEvents.md#playerBlockedByShield) | 无 | ModSDK |
| [PlayerCheatSpinAttackServerEvent](#playercheatspinattackserverevent) | [world.afterEvents.playerCheatSpinAttack](events/afterEvents.md#playerCheatSpinAttack) | 无 | Apollo |
| [PlayerDieEvent](#playerdieevent) | [world.afterEvents.playerDie](events/afterEvents.md#playerDie) | 无 | ModSDK |
| [DimensionChangeFinishServerEvent](#dimensionchangefinishserverevent) | [world.afterEvents.playerDimensionChangeFinish](events/afterEvents.md#playerDimensionChangeFinish) | 无 | ModSDK |
| [DimensionChangeServerEvent](#dimensionchangeserverevent) | `world.afterEvents.getNativeEvent('DimensionChangeServerEvent')` | 无 | ModSDK |
| [PlayerDoInteractServerEvent](#playerdointeractserverevent) | `world.afterEvents.getNativeEvent('PlayerDoInteractServerEvent')` | 无 | ModSDK |
| [PlayerDropItemServerEvent](#playerdropitemserverevent) | [world.afterEvents.playerDropItem](events/afterEvents.md#playerDropItem) | 无 | ModSDK |
| [AddExpEvent](#addexpevent) | [world.afterEvents.playerExperienceAdd](events/afterEvents.md#playerExperienceAdd) | 无 | ModSDK |
| [PlayerFishingAfterServerEvent](#playerfishingafterserverevent) | [world.afterEvents.playerFishing](events/afterEvents.md#playerFishing) | 无 | ModSDK |
| [OnPlayerHitBlockServerEvent](#onplayerhitblockserverevent) | [world.afterEvents.playerHitBlock](events/afterEvents.md#playerHitBlock) | 无 | ModSDK |
| [OnCarriedNewItemChangedServerEvent](#oncarriednewitemchangedserverevent) | `world.afterEvents.getNativeEvent('OnCarriedNewItemChangedServerEvent')` | 无 | ModSDK |
| [PlayerInventoryOpenScriptServerEvent](#playerinventoryopenscriptserverevent) | [world.afterEvents.playerInventoryOpenScript](events/afterEvents.md#playerInventoryOpenScript) | 无 | ModSDK |
| [AddLevelEvent](#addlevelevent) | [world.afterEvents.playerLevelChange](events/afterEvents.md#playerLevelChange) | 无 | ModSDK |
| [OnOffhandItemChangedServerEvent](#onoffhanditemchangedserverevent) | `world.afterEvents.getNativeEvent('OnOffhandItemChangedServerEvent')` | 无 | ModSDK |
| [DelServerPlayerEvent](#delserverplayerevent) | [world.afterEvents.playerRemove](events/afterEvents.md#playerRemove) | 无 | ModSDK |
| [PlayerRemoveCustomContainerItemServerEvent](#playerremovecustomcontaineritemserverevent) | [world.afterEvents.playerRemoveCustomContainerItem](events/afterEvents.md#playerRemoveCustomContainerItem) | 无 | ModSDK |
| [PlayerRespawnEvent](#playerrespawnevent) | [world.afterEvents.playerRespawn](events/afterEvents.md#playerRespawn) | 无 | ModSDK |
| [PlayerRespawnFinishServerEvent](#playerrespawnfinishserverevent) | `world.afterEvents.getNativeEvent('PlayerRespawnFinishServerEvent')` | 无 | ModSDK |
| [PlayerSleepServerEvent](#playersleepserverevent) | [world.afterEvents.playerSleep](events/afterEvents.md#playerSleep) | 无 | ModSDK |
| [PlayerSpinAttackServerEvent](#playerspinattackserverevent) | [world.afterEvents.playerSpinAttack](events/afterEvents.md#playerSpinAttack) | 无 | Apollo |
| [PlayerStopSleepServerEvent](#playerstopsleepserverevent) | [world.afterEvents.playerStopSleep](events/afterEvents.md#playerStopSleep) | 无 | ModSDK |
| [PlayerTeleportEvent](#playerteleportevent) | [world.afterEvents.playerTeleport](events/afterEvents.md#playerTeleport) | 无 | ModSDK |
| [ProjectileCritHitEvent](#projectilecrithitevent) | [world.afterEvents.projectileCritHit](events/afterEvents.md#projectileCritHit) | 无 | ModSDK |
| [OnRainLevelChangeServerEvent](#onrainlevelchangeserverevent) | `world.afterEvents.getNativeEvent('OnRainLevelChangeServerEvent')` | 无 | ModSDK |
| [LoadServerAddonScriptsAfter](#loadserveraddonscriptsafter) | [world.afterEvents.scriptsLoad](events/afterEvents.md#scriptsLoad) | 无 | ModSDK |
| [SpawnProjectileServerEvent](#spawnprojectileserverevent) | [world.afterEvents.spawnProjectile](events/afterEvents.md#spawnProjectile) | 无 | ModSDK |
| [StepOffBlockServerEvent](#stepoffblockserverevent) | [world.afterEvents.stepOffBlock](events/afterEvents.md#stepOffBlock) | 无 | ModSDK |
| [StoreBuySuccServerEvent](#storebuysuccserverevent) | [world.afterEvents.storeBuySucc](events/afterEvents.md#storeBuySucc) | 无 | ModSDK |
| [OnScriptTickServer](#onscripttickserver) | [world.afterEvents.tick](events/afterEvents.md#tick) | 无 | ModSDK |
| [UIContainerItemChangedServerEvent](#uicontaineritemchangedserverevent) | [world.afterEvents.uiContainerItemChange](events/afterEvents.md#uiContainerItemChange) | 无 | ModSDK |
| [UrgeShipEvent](#urgeshipevent) | [world.afterEvents.urgeShip](events/afterEvents.md#urgeShip) | 无 | ModSDK |
| [WalkAnimBeginServerEvent](#walkanimbeginserverevent) | [world.afterEvents.walkAnimBegin](events/afterEvents.md#walkAnimBegin) | 无 | ModSDK |
| [WalkAnimEndServerEvent](#walkanimendserverevent) | [world.afterEvents.walkAnimEnd](events/afterEvents.md#walkAnimEnd) | 无 | ModSDK |
| [ActorUseItemServerEvent](#actoruseitemserverevent) | [world.beforeEvents.actorUseItem](events/beforeEvents.md#actorUseItem) | 无 | ModSDK |
| [ActuallyHurtServerEvent](#actuallyhurtserverevent) | [world.beforeEvents.actuallyHurt](events/beforeEvents.md#actuallyHurt) | damage | ModSDK |
| [BlockLiquidStateChangeServerEvent](#blockliquidstatechangeserverevent) | [world.beforeEvents.blockLiquidStateChange](events/beforeEvents.md#blockLiquidStateChange) | 无 | ModSDK |
| [ServerPreBlockPatternEvent](#serverpreblockpatternevent) | [world.beforeEvents.blockPattern](events/beforeEvents.md#blockPattern) | enable；cancel 映射 反转 enable | ModSDK |
| [BlockSnowStateChangeServerEvent](#blocksnowstatechangeserverevent) | [world.beforeEvents.blockSnowStateChange](events/beforeEvents.md#blockSnowStateChange) | 无 | ModSDK |
| [ServerBlockUseEvent](#serverblockuseevent) | `world.beforeEvents.getNativeEvent('ServerBlockUseEvent')` | cancel | ModSDK |
| [ChangeLevelUpCostServerEvent](#changelevelupcostserverevent) | [world.beforeEvents.changeLevelUpCost](events/beforeEvents.md#changeLevelUpCost) | changed, levelUpCostExp | ModSDK |
| [ChestBlockTryPairWithServerEvent](#chestblocktrypairwithserverevent) | [world.beforeEvents.chestBlockTryPairWith](events/beforeEvents.md#chestBlockTryPairWith) | cancel | ModSDK |
| [ChunkAcquireDiscardedServerEvent](#chunkacquirediscardedserverevent) | [world.beforeEvents.chunkUnload](events/beforeEvents.md#chunkUnload) | 无 | ModSDK |
| [CommandEvent](#commandevent) | [world.beforeEvents.command](events/beforeEvents.md#command) | cancel | ModSDK |
| [CommandBlockContainerOpenEvent](#commandblockcontaineropenevent) | [world.beforeEvents.commandBlockContainerOpen](events/beforeEvents.md#commandBlockContainerOpen) | cancel | ModSDK |
| [CommandBlockUpdateEvent](#commandblockupdateevent) | [world.beforeEvents.commandBlockUpdate](events/beforeEvents.md#commandBlockUpdate) | cancel | ModSDK |
| [OnContainerFillLoottableServerEvent](#oncontainerfillloottableserverevent) | `world.beforeEvents.getNativeEvent('OnContainerFillLoottableServerEvent')` | dirty, itemList | ModSDK |
| [CraftItemOutputChangeServerEvent](#craftitemoutputchangeserverevent) | [world.beforeEvents.craftItemOutputChange](events/beforeEvents.md#craftItemOutputChange) | cancel | ModSDK |
| [CustomCommandTriggerServerEvent](#customcommandtriggerserverevent) | [world.beforeEvents.customCommandTrigger](events/beforeEvents.md#customCommandTrigger) | return_failed, return_msg_key | ModSDK |
| [DamageEvent](#damageevent) | `world.beforeEvents.getNativeEvent('DamageEvent')` | damage, ignite, knock | ModSDK |
| [WillAddEffectServerEvent](#willaddeffectserverevent) | [world.beforeEvents.effectAdd](events/beforeEvents.md#effectAdd) | cancel | ModSDK |
| [HealthChangeBeforeServerEvent](#healthchangebeforeserverevent) | [world.beforeEvents.entityHealthChanged](events/beforeEvents.md#entityHealthChanged) | cancel | ModSDK |
| [OnEntityInsideBlockServerEvent](#onentityinsideblockserverevent) | [world.beforeEvents.entityInsideBlock](events/beforeEvents.md#entityInsideBlock) | cancel, slowdownMultiX, slowdownMultiY, slowdownMultiZ | ModSDK |
| [EntityDieLoottableServerEvent](#entitydieloottableserverevent) | `world.beforeEvents.getNativeEvent('EntityDieLoottableServerEvent')` | dirty, itemList | ModSDK |
| [EntityMotionStopServerEvent](#entitymotionstopserverevent) | [world.beforeEvents.entityMotionStop](events/beforeEvents.md#entityMotionStop) | remove | ModSDK |
| [ServerEntityTryPlaceBlockEvent](#serverentitytryplaceblockevent) | [world.beforeEvents.entityPlaceBlock](events/beforeEvents.md#entityPlaceBlock) | auxData, cancel, fullName, x, y, z | ModSDK |
| [ServerSpawnMobEvent](#serverspawnmobevent) | [world.beforeEvents.entitySpawn](events/beforeEvents.md#entitySpawn) | cancel | ModSDK |
| [EntityStopRidingEvent](#entitystopridingevent) | [world.beforeEvents.entityStopRiding](events/beforeEvents.md#entityStopRiding) | cancel | ModSDK |
| [ExtinguishFireServerEvent](#extinguishfireserverevent) | [world.beforeEvents.extinguishFire](events/beforeEvents.md#extinguishFire) | cancel | ModSDK |
| [OnBeforeFallOnBlockServerEvent](#onbeforefallonblockserverevent) | [world.beforeEvents.fallOnBlock](events/beforeEvents.md#fallOnBlock) | cancel, fallDistance | ModSDK |
| [OnAfterFallOnBlockServerEvent](#onafterfallonblockserverevent) | [world.beforeEvents.fallOnBlockMotion](events/beforeEvents.md#fallOnBlockMotion) | calculate, motionX, motionY, motionZ | ModSDK |
| [FallingBlockBreakServerEvent](#fallingblockbreakserverevent) | [world.beforeEvents.fallingBlockBreak](events/beforeEvents.md#fallingBlockBreak) | cancelDrop | ModSDK |
| [FallingBlockCauseDamageBeforeServerEvent](#fallingblockcausedamagebeforeserverevent) | [world.beforeEvents.fallingBlockCauseDamage](events/beforeEvents.md#fallingBlockCauseDamage) | fallDamage, isHarmful | ModSDK |
| [OnFireHurtEvent](#onfirehurtevent) | [world.beforeEvents.fireHurt](events/beforeEvents.md#fireHurt) | cancel, cancelIgnite | ModSDK |
| [GlobalCommandServerEvent](#globalcommandserverevent) | [world.beforeEvents.globalCommand](events/beforeEvents.md#globalCommand) | cancel | ModSDK |
| [ItemDurabilityChangedServerEvent](#itemdurabilitychangedserverevent) | [world.beforeEvents.itemDurabilityChange](events/beforeEvents.md#itemDurabilityChange) | durability | ModSDK |
| [ItemPullOutCustomContainerServerEvent](#itempulloutcustomcontainerserverevent) | [world.beforeEvents.itemPullOutCustomContainer](events/beforeEvents.md#itemPullOutCustomContainer) | cancel | ModSDK |
| [ItemPushInCustomContainerServerEvent](#itempushincustomcontainerserverevent) | [world.beforeEvents.itemPushInCustomContainer](events/beforeEvents.md#itemPushInCustomContainer) | cancel | ModSDK |
| [OnItemPutInEnchantingModelServerEvent](#onitemputinenchantingmodelserverevent) | [world.beforeEvents.itemPutInEnchantingModel](events/beforeEvents.md#itemPutInEnchantingModel) | change, options | ModSDK |
| [ItemReleaseUsingServerEvent](#itemreleaseusingserverevent) | [world.beforeEvents.itemReleaseUsing](events/beforeEvents.md#itemReleaseUsing) | cancel, changeItem | ModSDK |
| [ServerItemTryUseEvent](#serveritemtryuseevent) | `world.beforeEvents.getNativeEvent('ServerItemTryUseEvent')` | cancel | ModSDK |
| [ServerItemUseOnEvent](#serveritemuseonevent) | `world.beforeEvents.getNativeEvent('ServerItemUseOnEvent')` | ret；cancel 映射 ret | ModSDK |
| [MobGriefingBlockServerEvent](#mobgriefingblockserverevent) | [world.beforeEvents.mobGriefingBlock](events/beforeEvents.md#mobGriefingBlock) | cancel | ModSDK |
| [ServerChatEvent](#serverchatevent) | `world.beforeEvents.getNativeEvent('ServerChatEvent')` | bChatById, bForbid, cancel, gameChatPrefix, gameChatPrefixColorB, gameChatPrefixColorG, gameChatPrefixColorR, message, toPlayerIds, username | ModSDK |
| [ExplosionServerEvent](#explosionserverevent) | `world.beforeEvents.getNativeEvent('ExplosionServerEvent')` | blocks | ModSDK |
| [PistonActionServerEvent](#pistonactionserverevent) | [world.beforeEvents.pistonAction](events/beforeEvents.md#pistonAction) | cancel | ModSDK |
| [PlaceNeteaseLargeFeatureServerEvent](#placeneteaselargefeatureserverevent) | [world.beforeEvents.placeNeteaseLargeFeature](events/beforeEvents.md#placeNeteaseLargeFeature) | cancel | ModSDK |
| [PlaceNeteaseStructureFeatureEvent](#placeneteasestructurefeatureevent) | [world.beforeEvents.placeNeteaseStructureFeature](events/beforeEvents.md#placeNeteaseStructureFeature) | cancel, structureName | ModSDK |
| [OnPlayerActiveShieldServerEvent](#onplayeractiveshieldserverevent) | [world.beforeEvents.playerActiveShield](events/beforeEvents.md#playerActiveShield) | cancel | ModSDK |
| [PlayerAttackEntityEvent](#playerattackentityevent) | [world.beforeEvents.playerAttackEntity](events/beforeEvents.md#playerAttackEntity) | cancel, damage, isKnockBack, isValid | ModSDK |
| [OnPlayerBlockedByShieldBeforeServerEvent](#onplayerblockedbyshieldbeforeserverevent) | [world.beforeEvents.playerBlockedByShield](events/beforeEvents.md#playerBlockedByShield) | 无 | ModSDK |
| [PlayerEatFoodServerEvent](#playereatfoodserverevent) | [world.beforeEvents.playerEatFood](events/beforeEvents.md#playerEatFood) | hunger, nutrition | ModSDK |
| [PlayerFeedEntityServerEvent](#playerfeedentityserverevent) | [world.beforeEvents.playerFeedEntity](events/beforeEvents.md#playerFeedEntity) | cancel | ModSDK |
| [PlayerFishingServerEvent](#playerfishingserverevent) | `world.beforeEvents.getNativeEvent('PlayerFishingServerEvent')` | cancel, itemChange, itemList | ModSDK |
| [ServerPlayerGetExperienceOrbEvent](#serverplayergetexperienceorbevent) | [world.beforeEvents.playerGetExperienceOrb](events/beforeEvents.md#playerGetExperienceOrb) | cancel | ModSDK |
| [PlayerHungerChangeServerEvent](#playerhungerchangeserverevent) | [world.beforeEvents.playerHungerChange](events/beforeEvents.md#playerHungerChange) | cancel | ModSDK |
| [PlayerHurtEvent](#playerhurtevent) | [world.beforeEvents.playerHurt](events/beforeEvents.md#playerHurt) | 无 | ModSDK |
| [PlayerInteractServerEvent](#playerinteractserverevent) | `world.beforeEvents.getNativeEvent('PlayerInteractServerEvent')` | cancel | ModSDK |
| [PlayerJoinMessageEvent](#playerjoinmessageevent) | [world.beforeEvents.playerJoinMessage](events/beforeEvents.md#playerJoinMessage) | cancel, message | ModSDK |
| [PlayerIntendLeaveServerEvent](#playerintendleaveserverevent) | [world.beforeEvents.playerLeave](events/beforeEvents.md#playerLeave) | 无 | ModSDK |
| [PlayerLeftMessageServerEvent](#playerleftmessageserverevent) | [world.beforeEvents.playerLeftMessage](events/beforeEvents.md#playerLeftMessage) | cancel, message | ModSDK |
| [PlayerNamedEntityServerEvent](#playernamedentityserverevent) | [world.beforeEvents.playerNamedEntity](events/beforeEvents.md#playerNamedEntity) | cancel | ModSDK |
| [PlayerPermissionChangeServerEvent](#playerpermissionchangeserverevent) | [world.beforeEvents.playerPermissionChange](events/beforeEvents.md#playerPermissionChange) | cancel | ModSDK |
| [PlayerPickupArrowServerEvent](#playerpickuparrowserverevent) | [world.beforeEvents.playerPickupArrow](events/beforeEvents.md#playerPickupArrow) | cancel, pickupDelay | ModSDK |
| [ServerPlayerTryTouchEvent](#serverplayertrytouchevent) | [world.beforeEvents.playerPickupItem](events/beforeEvents.md#playerPickupItem) | cancel, pickupDelay | ModSDK |
| [PlayerStartFishingServerEvent](#playerstartfishingserverevent) | [world.beforeEvents.playerStartFishing](events/beforeEvents.md#playerStartFishing) | cancel | ModSDK |
| [PlayerTryAddCustomContainerItemServerEvent](#playertryaddcustomcontaineritemserverevent) | [world.beforeEvents.playerTryAddCustomContainerItem](events/beforeEvents.md#playerTryAddCustomContainerItem) | 无 | ModSDK |
| [ServerPlayerTryDestroyBlockEvent](#serverplayertrydestroyblockevent) | `world.beforeEvents.getNativeEvent('ServerPlayerTryDestroyBlockEvent')` | cancel, spawnResources | ModSDK |
| [PlayerTryPutCustomContainerItemServerEvent](#playertryputcustomcontaineritemserverevent) | [world.beforeEvents.playerTryPutCustomContainerItem](events/beforeEvents.md#playerTryPutCustomContainerItem) | cancel | ModSDK |
| [PlayerTryRemoveCustomContainerItemServerEvent](#playertryremovecustomcontaineritemserverevent) | [world.beforeEvents.playerTryRemoveCustomContainerItem](events/beforeEvents.md#playerTryRemoveCustomContainerItem) | 无 | ModSDK |
| [PlayerTrySleepServerEvent](#playertrysleepserverevent) | [world.beforeEvents.playerTrySleep](events/beforeEvents.md#playerTrySleep) | cancel | ModSDK |
| [ProjectileDoHitEffectEvent](#projectiledohiteffectevent) | [world.beforeEvents.projectileDoHitEffect](events/beforeEvents.md#projectileDoHitEffect) | cancel | ModSDK |
| [ShearsDestoryBlockBeforeServerEvent](#shearsdestoryblockbeforeserverevent) | [world.beforeEvents.shearsDestroyBlock](events/beforeEvents.md#shearsDestroyBlock) | cancelShears | ModSDK |
| [ShearsUseToBlockBeforeServerEvent](#shearsusetoblockbeforeserverevent) | [world.beforeEvents.shearsUseToBlock](events/beforeEvents.md#shearsUseToBlock) | cancelShears | ModSDK |
| [OnStandOnBlockServerEvent](#onstandonblockserverevent) | [world.beforeEvents.standOnBlock](events/beforeEvents.md#standOnBlock) | cancel, motionX, motionY, motionZ | ModSDK |
| [StartDestroyBlockServerEvent](#startdestroyblockserverevent) | [world.beforeEvents.startDestroyBlock](events/beforeEvents.md#startDestroyBlock) | cancel | ModSDK |
| [StartRidingServerEvent](#startridingserverevent) | [world.beforeEvents.startRiding](events/beforeEvents.md#startRiding) | cancel | ModSDK |
| [StepOnBlockServerEvent](#steponblockserverevent) | [world.beforeEvents.stepOnBlock](events/beforeEvents.md#stepOnBlock) | cancel | ModSDK |
| [WillTeleportToServerEvent](#willteleporttoserverevent) | [world.beforeEvents.willTeleportTo](events/beforeEvents.md#willTeleportTo) | cancel | ModSDK |

## 逐项契约

### AchievementCompleteEvent {#achievementcompleteevent}

玩家完成自定义成就时触发该事件

信号：[world.afterEvents.achievementComplete](events/afterEvents.md#achievementComplete)。分类：世界。

参数类型：[WorldAchievementCompleteAfterEvent](reference/WorldAchievementCompleteAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("AchievementCompleteEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `rootNodeId` | `rootNodeId` | [str](../common/type-system.md#str) | 只读 | 所属的页面的根节点成就id |
| `achievementId` | `achievementId` | [str](../common/type-system.md#str) | 只读 | 达成的成就id |
| `title` | `title` | [str](../common/type-system.md#str) | 只读 | 成就标题 |
| `description` | `description` | [str](../common/type-system.md#str) | 只读 | 成就描述 |

### ActorAcquiredItemServerEvent {#actoracquireditemserverevent}

触发时机：玩家获得物品时服务端抛出的事件（有些获取物品方式只会触发客户端事件，有些获取物品方式只会触发服务端事件，在使用时注意一点。）

信号：[world.afterEvents.actorAcquiredItem](events/afterEvents.md#actorAcquiredItem)。分类：物品。

参数类型：[WorldActorAcquiredItemAfterEvent](reference/WorldActorAcquiredItemAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("ActorAcquiredItemServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `actor` | `actor` | [str](../common/type-system.md#str) | 只读 | 获得物品玩家实体id |
| `secondaryActor` | `secondaryActor` | [str](../common/type-system.md#str) | 只读 | 物品给予者玩家实体id，如果不存在给予者的话，这里为空字符串 |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 获得的物品的物品信息字典 |
| `acquireMethod` | `acquireMethod` | [int](../common/type-system.md#int) | 只读 | 获得物品的方法，详见ItemAcquisitionMethod枚举 |

### ActorHurtServerEvent {#actorhurtserverevent}

触发时机：生物（包括玩家）受伤时触发

信号：[world.afterEvents.actorHurt](events/afterEvents.md#actorHurt)。分类：实体。

参数类型：[WorldActorHurtAfterEvent](reference/WorldActorHurtAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("ActorHurtServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 生物Id |
| `cause` | `cause` | [str](../common/type-system.md#str) | 只读 | 伤害来源，详见Minecraft枚举值文档的ActorDamageCause |
| `damage` | `damage` | [float](../common/type-system.md#float) | 只读 | 伤害值（被伤害吸收后的值），不可修改 |
| `absorbedDamage` | `absorbedDamage` | [int](../common/type-system.md#int) | 只读 | 被伤害吸收效果吸收的伤害值 |
| `customTag` | `customTag` | [str](../common/type-system.md#str) | 只读 | 使用Hurt接口传入的自定义伤害类型 |

### AttackAnimBeginServerEvent {#attackanimbeginserverevent}

当攻击动作开始时触发

信号：[world.afterEvents.attackAnimBegin](events/afterEvents.md#attackAnimBegin)。分类：模型。

参数类型：[WorldAttackAnimBeginAfterEvent](reference/WorldAttackAnimBeginAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("AttackAnimBeginServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |

**原生前提与限制：**

- 使用SetModel替换骨骼模型后，该事件才生效

### AttackAnimEndServerEvent {#attackanimendserverevent}

当攻击动作结束时触发

信号：[world.afterEvents.attackAnimEnd](events/afterEvents.md#attackAnimEnd)。分类：模型。

参数类型：[WorldAttackAnimEndAfterEvent](reference/WorldAttackAnimEndAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("AttackAnimEndServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |

**原生前提与限制：**

- 使用SetModel替换骨骼模型后，该事件才生效

### BlockDestroyByLiquidServerEvent {#blockdestroybyliquidserverevent}

触发时机：方块被水流破坏的事件

信号：[world.afterEvents.blockDestroyByLiquid](events/afterEvents.md#blockDestroyByLiquid)。分类：方块。

参数类型：[WorldBlockDestroyByLiquidAfterEvent](reference/WorldBlockDestroyByLiquidAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("BlockDestroyByLiquidServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `liquidName` | `liquidName` | [str](../common/type-system.md#str) | 只读 | 流体方块id |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块id |
| `auxValue` | `auxValue` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 方块所在维度id |

**原生前提与限制：**

- 指令或者接口的设置不会触发该事件

### ServerBlockEntityTickEvent {#serverblockentitytickevent}

触发时机：自定义方块配置了netease:block_entity组件并设tick为true，方块在玩家的模拟距离（新建存档时可以设置，默认为4个区块）内，或者在tickingarea内的时候触发

信号：[world.afterEvents.blockEntityTick](events/afterEvents.md#blockEntityTick)。分类：方块。

参数类型：[WorldBlockEntityTickAfterEvent](reference/WorldBlockEntityTickAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("ServerBlockEntityTickEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 该方块名称 |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 该方块所在的维度 |
| `posX` | `posX` | [int](../common/type-system.md#int) | 只读 | 该方块的x坐标 |
| `posY` | `posY` | [int](../common/type-system.md#int) | 只读 | 该方块的y坐标 |
| `posZ` | `posZ` | [int](../common/type-system.md#int) | 只读 | 该方块的z坐标 |

**原生前提与限制：**

- **方块实体的tick事件频率为每秒钟20次**
  - 触发本事件时，若正在退出游戏，将无法获取到抛出本事件的方块实体数据（GetBlockEntityData函数返回None），也无法对其进行操作

### BlockLiquidStateChangeAfterServerEvent {#blockliquidstatechangeafterserverevent}

触发时机：方块转为含水或者脱离含水(流体)后触发

信号：[world.afterEvents.blockLiquidStateChange](events/afterEvents.md#blockLiquidStateChange)。分类：方块。

参数类型：[WorldBlockLiquidStateChangeAfterEvent](reference/WorldBlockLiquidStateChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("BlockLiquidStateChangeAfterServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxValue` | `auxValue` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 方块维度 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `turnLiquid` | `turnLiquid` | [bool](../common/type-system.md#bool) | 只读 | 是否转为含水，true则转为含水，false则脱离含水 |

### BlockNeighborChangedServerEvent {#blockneighborchangedserverevent}

触发时机：自定义方块周围的方块发生变化时，需要配置netease:neighborchanged_sendto_script，详情请查阅《自定义农作物》文档

信号：[world.afterEvents.blockNeighborChange](events/afterEvents.md#blockNeighborChange)。分类：方块。

参数类型：[WorldBlockNeighborChangeAfterEvent](reference/WorldBlockNeighborChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("BlockNeighborChangedServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度 |
| `posX` | `posX` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `posY` | `posY` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `posZ` | `posZ` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxValue` | `auxValue` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |
| `neighborPosX` | `neighborPosX` | [int](../common/type-system.md#int) | 只读 | 变化方块x坐标 |
| `neighborPosY` | `neighborPosY` | [int](../common/type-system.md#int) | 只读 | 变化方块y坐标 |
| `neighborPosZ` | `neighborPosZ` | [int](../common/type-system.md#int) | 只读 | 变化方块z坐标 |
| `fromBlockName` | `fromBlockName` | [str](../common/type-system.md#str) | 只读 | 方块变化前的identifier，包含命名空间及名称 |
| `fromBlockAuxValue` | `fromBlockAuxValue` | [int](../common/type-system.md#int) | 只读 | 方块变化前附加值 |
| `toBlockName` | `toBlockName` | [str](../common/type-system.md#str) | 只读 | 方块变化后的identifier，包含命名空间及名称 |
| `toAuxValue` | `toAuxValue` | [int](../common/type-system.md#int) | 只读 | 方块变化后附加值 |

### ServerPostBlockPatternEvent {#serverpostblockpatternevent}

触发时机：用方块组合生成生物，生成生物之后触发该事件。

信号：[world.afterEvents.blockPattern](events/afterEvents.md#blockPattern)。分类：世界。

参数类型：[WorldBlockPatternAfterEvent](reference/WorldBlockPatternAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("ServerPostBlockPatternEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 生成生物的id |
| `entityGenerated` | `entityGenerated` | [str](../common/type-system.md#str) | 只读 | 生成生物的名字，如"minecraft:pig" |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |

### BlockRandomTickServerEvent {#blockrandomtickserverevent}

触发时机：自定义方块配置netease:random_tick随机tick时

信号：[world.afterEvents.blockRandomTick](events/afterEvents.md#blockRandomTick)。分类：方块。

参数类型：[WorldBlockRandomTickAfterEvent](reference/WorldBlockRandomTickAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("BlockRandomTickServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `posX` | `posX` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `posY` | `posY` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `posZ` | `posZ` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块名称 |
| `fullName` | `fullName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxValue` | `auxValue` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |
| `brightness` | `brightness` | [int](../common/type-system.md#int) | 只读 | 方块亮度 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 方块所在维度 |

### BlockRemoveServerEvent {#blockremoveserverevent}

触发时机：监听该事件的方块在销毁时触发，可以通过ListenOnBlockRemoveEvent方法进行监听，或者通过json组件netease:listen_block_remove进行配置

信号：[world.afterEvents.blockRemove](events/afterEvents.md#blockRemove)。分类：方块。

参数类型：[WorldBlockRemoveAfterEvent](reference/WorldBlockRemoveAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("BlockRemoveServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块位置x |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块位置y |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块位置z |
| `fullName` | `fullName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxValue` | `auxValue` | [int](../common/type-system.md#int) | 只读 | 方块的附加值 |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 该方块所在的维度 |

**原生前提与限制：**

- 对于一些特殊的方块，注意要使用对应的方块Id参数（如砖块楼梯，监听的方块Id应该为minecraft:brick_block）
  - 如果用骨粉改变了发光浆果，也会触发一次事件，它实际是从cave_vines变成了cave_vines_head_with_berries

### BlockSnowStateChangeAfterServerEvent {#blocksnowstatechangeafterserverevent}

触发时机：方块转为含雪或者脱离含雪后触发

信号：[world.afterEvents.blockSnowStateChange](events/afterEvents.md#blockSnowStateChange)。分类：方块。

参数类型：[WorldBlockSnowStateChangeAfterEvent](reference/WorldBlockSnowStateChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("BlockSnowStateChangeAfterServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 方块维度 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `turnSnow` | `turnSnow` | [bool](../common/type-system.md#bool) | 只读 | 是否转为含雪，true则转为含雪，false则脱离含雪 |
| `setBlockType` | `setBlockType` | [int](../common/type-system.md#int) | 只读 | 方块进入脱离含雪的原因，参考SetBlockType |

### BlockStrengthChangedServerEvent {#blockstrengthchangedserverevent}

触发时机：自定义机械元件方块红石信号量发生变化时触发

信号：[world.afterEvents.blockStrengthChange](events/afterEvents.md#blockStrengthChange)。分类：方块。

参数类型：[WorldBlockStrengthChangeAfterEvent](reference/WorldBlockStrengthChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("BlockStrengthChangedServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `posX` | `posX` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `posY` | `posY` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `posZ` | `posZ` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxValue` | `auxValue` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |
| `newStrength` | `newStrength` | [int](../common/type-system.md#int) | 只读 | 变化后的红石信号量 |
| `oldStrength` | `oldStrength` | [int](../common/type-system.md#int) | 只读 | 变化前的红石信号量 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度 |

### ChangeSwimStateServerEvent {#changeswimstateserverevent}

触发时机：实体开始或者结束游泳时

信号：[world.afterEvents.changeSwimState](events/afterEvents.md#changeSwimState)。分类：实体。

参数类型：[WorldChangeSwimStateAfterEvent](reference/WorldChangeSwimStateAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("ChangeSwimStateServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体的唯一ID |
| `formState` | `formState` | [bool](../common/type-system.md#bool) | 只读 | 事件触发前，实体是否在游泳状态 |
| `toState` | `toState` | [bool](../common/type-system.md#bool) | 只读 | 事件触发后，实体是否在游泳状态 |

**原生前提与限制：**

- 当实体的状态没有变化时，不会触发此事件，即formState和toState必定一真一假

### ChunkGeneratedServerEvent {#chunkgeneratedserverevent}

触发时机：区块创建完成时触发

信号：[world.afterEvents.chunkGenerated](events/afterEvents.md#chunkGenerated)。分类：世界。

参数类型：[WorldChunkGeneratedAfterEvent](reference/WorldChunkGeneratedAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("ChunkGeneratedServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 该区块所在的维度 |
| `chunkPosX` | `chunkPosX` | [int](../common/type-system.md#int) | 只读 | 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15] |
| `chunkPosZ` | `chunkPosZ` | [int](../common/type-system.md#int) | 只读 | 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15] |
| `blockEntityData` | `blockEntityData` | [&#123;"blockName":[str](../common/type-system.md#str),"posX":[int](../common/type-system.md#int),"posY":[int](../common/type-system.md#int),"posZ":[int](../common/type-system.md#int)&#125;...]/[None](../common/type-system.md#none) | 只读 | 该区块中的自定义方块实体列表，通常是由自定义特征生成的自定义方块，没有自定义方块实体时该值为[None](../common/type-system.md#none) |

### ChunkLoadedServerEvent {#chunkloadedserverevent}

触发时机：服务端区块加载完成时

信号：[world.afterEvents.chunkLoad](events/afterEvents.md#chunkLoad)。分类：世界。

参数类型：[WorldChunkLoadAfterEvent](reference/WorldChunkLoadAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("ChunkLoadedServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 区块所在维度 |
| `chunkPosX` | `chunkPosX` | [int](../common/type-system.md#int) | 只读 | 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15] |
| `chunkPosZ` | `chunkPosZ` | [int](../common/type-system.md#int) | 只读 | 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15] |
| `blockEntities` | `blockEntities` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 只读 | 随区块加载而加载进世界的自定义方块实体的坐标的列表，列表元素dict包含posX，posY，posZ三个int表示自定义方块实体的坐标，blockName表示方块的identifier，包含命名空间及名称 |

**原生前提与限制：**

- 注意：服务端的自定义方块实体加载完成时对应的客户端的自定义方块实体并没有初始化完成，无法使用该事件对客户端的自定义方块实体进行相关操作。

### ClientLoadAddonsFinishServerEvent {#clientloadaddonsfinishserverevent}

触发时机：客户端mod加载完成时，服务端触发此事件。服务器可以使用此事件，往客户端发送数据给其初始化。

信号：[world.afterEvents.clientReady](events/afterEvents.md#clientReady)。分类：世界。

参数类型：[WorldClientReadyAfterEvent](reference/WorldClientReadyAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("ClientLoadAddonsFinishServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |

### OnCommandOutputServerEvent {#oncommandoutputserverevent}

Command命令执行成功事件

信号：[world.afterEvents.commandOutput](events/afterEvents.md#commandOutput)。分类：世界。

参数类型：[WorldCommandOutputAfterEvent](reference/WorldCommandOutputAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnCommandOutputServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `command` | `command` | [str](../common/type-system.md#str) | 只读 | 命令名称 |
| `message` | `message` | [str](../common/type-system.md#str) | 只读 | 命令返回的消息 |

**原生前提与限制：**

- 部分命令在返回的时候没有命令名称，SetCommand接口需要showOutput参数为True时才会有返回

### ContainerItemChangedServerEvent {#containeritemchangedserverevent}

容器物品变化事件

信号：[world.afterEvents.containerItemChange](events/afterEvents.md#containerItemChange)。分类：物品。

参数类型：[WorldContainerItemChangeAfterEvent](reference/WorldContainerItemChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("ContainerItemChangedServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `pos` | `pos` | [tuple](../common/type-system.md#tuple)([int](../common/type-system.md#int),[int](../common/type-system.md#int),[int](../common/type-system.md#int))`/[None](../common/type-system.md#none) | 只读 | 容器坐标 |
| `containerType` | `containerType` | [int](../common/type-system.md#int) | 只读 | 容器类型，类型含义见：容器类型枚举 |
| `slot` | `slot` | [int](../common/type-system.md#int) | 只读 | 容器槽位 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `oldItemDict` | `oldItemDict` | [dict](../common/type-system.md#dict) | 只读 | 旧物品，格式参考物品信息字典 |
| `newItemDict` | `newItemDict` | [dict](../common/type-system.md#dict) | 只读 | 新物品，格式参考物品信息字典 |

**原生前提与限制：**

- 储物容器(箱子，潜影箱)，熔炉，酿造台，发射器，投掷器，漏斗，炼药锅，唱片机，高炉，烟熏炉中物品发生变化会触发此事件
  - 工作台、铁砧、附魔台、织布机、砂轮、切石机、制图台、锻造台为合成容器，不会触发此事件，此类容器可通过UIContainerItemChangedServerEvent监听具体生成容器物品变化
  - 炼药锅只在使用染料时触发本事件，且slot为2
  - 唱片机只在从漏斗放入唱片触发此事件

### DestroyBlockEvent {#destroyblockevent}

触发时机：当方块已经被玩家破坏时触发该事件。

信号：`world.afterEvents.getNativeEvent('DestroyBlockEvent')`。分类：方块。

参数类型：[WorldDestroyBlockAfterEvent](reference/WorldDestroyBlockAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("DestroyBlockEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `face` | `face` | [int](../common/type-system.md#int) | 只读 | 方块被敲击的面向id，参考Facing枚举 |
| `fullName` | `fullName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxData` | `auxData` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 破坏方块的玩家ID |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `dropEntities` | `dropEntityIds` | [list](../common/type-system.md#list)([str](../common/type-system.md#str)) | 只读 | 掉落物实体id列表 |

**原生前提与限制：**

- 在生存模式或创造模式下都会触发

### DirtBlockToGrassBlockServerEvent {#dirtblocktograssblockserverevent}

触发时机：泥土方块变成草方块时触发

信号：[world.afterEvents.dirtBlockToGrassBlock](events/afterEvents.md#dirtBlockToGrassBlock)。分类：方块。

参数类型：[WorldDirtBlockToGrassBlockAfterEvent](reference/WorldDirtBlockToGrassBlockAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("DirtBlockToGrassBlockServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 方块维度 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |

**原生前提与限制：**

- 指令或者接口的设置不会触发该事件

### RefreshEffectServerEvent {#refresheffectserverevent}

触发时机：实体身上状态效果更新时触发，更新条件1、新增状态等级较高，更新状态等级及时间；2、新增状态等级不变，时间较长，更新状态持续时间

信号：`world.afterEvents.getNativeEvent('RefreshEffectServerEvent')`。分类：实体。

参数类型：[WorldEffectRefreshAfterEvent](reference/WorldEffectRefreshAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("RefreshEffectServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `effectName` | `effectName` | [str](../common/type-system.md#str) | 只读 | 更新状态效果的名字 |
| `effectDuration` | `effectDuration` | [int](../common/type-system.md#int) | 只读 | 更新后状态效果剩余持续时间，单位秒 |
| `effectAmplifier` | `effectAmplifier` | [int](../common/type-system.md#int) | 只读 | 更新后的状态效果放大倍数 |
| `damage` | `damage` | [float](../common/type-system.md#float) | 只读 | 状态造成的伤害值，如药水 |

### RemoveEffectServerEvent {#removeeffectserverevent}

触发时机：实体身上状态效果被移除时

信号：`world.afterEvents.getNativeEvent('RemoveEffectServerEvent')`。分类：实体。

参数类型：[WorldEffectRemoveAfterEvent](reference/WorldEffectRemoveAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("RemoveEffectServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `effectName` | `effectName` | [str](../common/type-system.md#str) | 只读 | 被移除状态效果的名字 |
| `effectDuration` | `effectDuration` | [int](../common/type-system.md#int) | 只读 | 被移除状态效果的剩余持续时间，单位秒 |
| `effectAmplifier` | `effectAmplifier` | [int](../common/type-system.md#int) | 只读 | 被移除状态效果的放大倍数 |

### AddEntityServerEvent {#addentityserverevent}

服务端侧创建新实体，或实体从存档加载时触发

信号：`world.afterEvents.getNativeEvent('AddEntityServerEvent')`。分类：世界。

参数类型：[WorldEntityAddAfterEvent](reference/WorldEntityAddAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("AddEntityServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `posX` | `posX` | [float](../common/type-system.md#float) | 只读 | 位置x |
| `posY` | `posY` | [float](../common/type-system.md#float) | 只读 | 位置y |
| `posZ` | `posZ` | [float](../common/type-system.md#float) | 只读 | 位置z |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 实体维度 |
| `isBaby` | `isBaby` | [bool](../common/type-system.md#bool) | 只读 | 是否为幼儿 |
| `engineTypeStr` | `engineTypeStr` | [str](../common/type-system.md#str) | 只读 | 实体类型，即实体identifier |
| `itemName` | `itemName` | [str](../common/type-system.md#str) | 只读 | 物品identifier（仅当物品实体时存在该字段） |
| `auxValue` | `auxValue` | [int](../common/type-system.md#int) | 只读 | 物品附加值（仅当物品实体时存在该字段） |

**原生前提与限制：**

- 创建玩家时不会触发该事件

### NewOnEntityAreaEvent {#newonentityareaevent}

触发时机：通过RegisterEntityAOIEvent注册过AOI事件后，当有实体进入或离开注册感应区域时触发该事件。

信号：`world.afterEvents.getNativeEvent('NewOnEntityAreaEvent')`。分类：世界。

参数类型：[WorldEntityAreaChangeAfterEvent](reference/WorldEntityAreaChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("NewOnEntityAreaEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `name` | `name` | [str](../common/type-system.md#str) | 只读 | 注册感应区域名称 |
| `enteredEntities` | `enteredEntities` | [list](../common/type-system.md#list)[[str](../common/type-system.md#str)] | 只读 | 进入该感应区域的实体id列表 |
| `leftEntities` | `leftEntities` | [list](../common/type-system.md#list)[[str](../common/type-system.md#str)] | 只读 | 离开该感应区域的实体id列表 |

**原生前提与限制：**

- 本事件代替原有的OnEntityAreaEvent事件

### EntityChangeDimensionServerEvent {#entitychangedimensionserverevent}

实体维度改变时服务端抛出

信号：[world.afterEvents.entityChangeDimension](events/afterEvents.md#entityChangeDimension)。分类：实体。

参数类型：[WorldEntityChangeDimensionAfterEvent](reference/WorldEntityChangeDimensionAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("EntityChangeDimensionServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `fromDimension` | `fromDimensionId` | [int](../common/type-system.md#int) | 只读 | 维度改变前的维度 |
| `toDimension` | `toDimensionId` | [int](../common/type-system.md#int) | 只读 | 维度改变后的维度 |
| `fromX` | `fromX` | [float](../common/type-system.md#float) | 只读 | 改变前的位置x |
| `fromY` | `fromY` | [float](../common/type-system.md#float) | 只读 | 改变前的位置Y |
| `fromZ` | `fromZ` | [float](../common/type-system.md#float) | 只读 | 改变前的位置Z |
| `toX` | `toX` | [float](../common/type-system.md#float) | 只读 | 改变后的位置x |
| `toY` | `toY` | [float](../common/type-system.md#float) | 只读 | 改变后的位置Y |
| `toZ` | `toZ` | [float](../common/type-system.md#float) | 只读 | 改变后的位置Z |

**原生前提与限制：**

- 实体转移维度时，如果对应维度的对应位置的区块尚未加载，实体会缓存在维度自身的缓冲区中，直到对应区块被加载时才会创建对应的实体，此事件的抛出只代表实体从原维度消失，不代表必定会在对应维度出现
  - 注意，玩家维度改变时不触发该事件，而是会触发DimensionChangeServerEvent事件

### OnMobHitMobServerEvent {#onmobhitmobserverevent}

触发时机：通过OpenPlayerHitMobDetection打开生物碰撞检测后，当生物间（包含玩家）碰撞时触发该事件。注：客户端和服务端分别作碰撞检测，可能两个事件返回的略有差异。

信号：[world.afterEvents.entityCollide](events/afterEvents.md#entityCollide)。分类：实体。

参数类型：[WorldEntityCollideAfterEvent](reference/WorldEntityCollideAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnMobHitMobServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `mobId` | [str](../common/type-system.md#str) | 只读 | 当前生物的id |
| `hittedMobList` | `hittedMobList` | [list](../common/type-system.md#list)[[str](../common/type-system.md#str)] | 只读 | 当前生物碰撞到的其他所有生物id的list |

**原生前提与限制：**

- 本事件代替原有的OnPlayerHitMobServerEvent事件

### EntityDefinitionsEventServerEvent {#entitydefinitionseventserverevent}

触发时机：生物定义json文件中设置的event触发时同时触发。生物行为变更事件

信号：`world.afterEvents.getNativeEvent('EntityDefinitionsEventServerEvent')`。分类：实体。

参数类型：[WorldEntityDefinitionTriggerAfterEvent](reference/WorldEntityDefinitionTriggerAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("EntityDefinitionsEventServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 生物id |
| `eventName` | `eventName` | [str](../common/type-system.md#str) | 只读 | 触发的事件名称 |

### EntityDroppedItemServerEvent {#entitydroppeditemserverevent}

触发时机：生物扔出物品时触发

信号：[world.afterEvents.entityDroppedItem](events/afterEvents.md#entityDroppedItem)。分类：实体。

参数类型：[WorldEntityDroppedItemAfterEvent](reference/WorldEntityDroppedItemAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("EntityDroppedItemServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 生物Id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 扔出的物品的物品信息字典 |
| `itemEntity` | `itemEntityId` | [str](../common/type-system.md#str) | 只读 | 物品实体Id |

### EntityEffectDamageServerEvent {#entityeffectdamageserverevent}

生物受到状态伤害/回复事件。

信号：[world.afterEvents.entityEffectDamage](events/afterEvents.md#entityEffectDamage)。分类：实体。

参数类型：[WorldEntityEffectDamageAfterEvent](reference/WorldEntityEffectDamageAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("EntityEffectDamageServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `damage` | `damage` | [float](../common/type-system.md#float) | 只读 | 伤害值（伤害吸收后实际扣血量），负数表示生命回复量 |
| `attributeBuffType` | `attributeBuffType` | [int](../common/type-system.md#int) | 只读 | 状态类型，参考AttributeBuffType |
| `duration` | `duration` | [float](../common/type-system.md#float) | 只读 | 状态持续时间，单位秒（s） |
| `lifeTimer` | `lifeTimer` | [float](../common/type-system.md#float) | 只读 | 状态生命时间，单位秒（s） |
| `isInstantaneous` | `isInstantaneous` | [bool](../common/type-system.md#bool) | 只读 | 是否为立即生效状态 |
| `cause` | `cause` | [str](../common/type-system.md#str) | 只读 | 伤害来源，详见Minecraft枚举值文档的ActorDamageCause |

### OnMobHitBlockServerEvent {#onmobhitblockserverevent}

触发时机：通过OpenMobHitBlockDetection打开方块碰撞检测后，当生物（不包括玩家）碰撞到方块时触发该事件。

信号：[world.afterEvents.entityHitBlock](events/afterEvents.md#entityHitBlock)。分类：实体。

参数类型：[WorldEntityHitBlockAfterEvent](reference/WorldEntityHitBlockAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnMobHitBlockServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 碰撞到方块的生物Id |
| `posX` | `posX` | [int](../common/type-system.md#int) | 只读 | 碰撞方块x坐标 |
| `posY` | `posY` | [int](../common/type-system.md#int) | 只读 | 碰撞方块y坐标 |
| `posZ` | `posZ` | [int](../common/type-system.md#int) | 只读 | 碰撞方块z坐标 |
| `blockId` | `blockId` | [str](../common/type-system.md#str) | 只读 | 碰撞方块的identifier |
| `auxValue` | `auxValue` | [int](../common/type-system.md#int) | 只读 | 碰撞方块的附加值 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |

**原生前提与限制：**

- 注：该碰撞检测会屏蔽草、空气、火、高草四种方块

### OnKnockBackServerEvent {#onknockbackserverevent}

实体被击退时触发

信号：[world.afterEvents.entityKnockback](events/afterEvents.md#entityKnockback)。分类：实体。

参数类型：[WorldEntityKnockbackAfterEvent](reference/WorldEntityKnockbackAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnKnockBackServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |

### OnGroundServerEvent {#ongroundserverevent}

实体着地事件。实体，掉落的物品，点燃的TNT掉落地面时触发

信号：[world.afterEvents.entityLand](events/afterEvents.md#entityLand)。分类：实体。

参数类型：[WorldEntityLandAfterEvent](reference/WorldEntityLandAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnGroundServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |

**原生前提与限制：**

- 不支持抛射物实体

### EntityLoadScriptEvent {#entityloadscriptevent}

数据库加载实体自定义数据时触发

信号：[world.afterEvents.entityLoadScript](events/afterEvents.md#entityLoadScript)。分类：实体。

参数类型：[WorldEntityLoadScriptAfterEvent](reference/WorldEntityLoadScriptAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("EntityLoadScriptEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `args` | `args` | [list](../common/type-system.md#list) | 只读 | 该事件的参数为长度为2的[list](../common/type-system.md#list)，而非[dict](../common/type-system.md#dict)，其中list的第一个元素为实体id |

**原生前提与限制：**

- 只有使用过extraData组件的SetExtraData接口的实体才有此事件，触发时可以通过extraData组件的GetExtraData或GetWholeExtraData接口获取该实体的自定义数据

### EntityDieLoottableAfterServerEvent {#entitydieloottableafterserverevent}

触发时机：生物死亡掉落物品之后

信号：[world.afterEvents.entityLoot](events/afterEvents.md#entityLoot)。分类：实体。

参数类型：[WorldEntityLootAfterEvent](reference/WorldEntityLootAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("EntityDieLoottableAfterServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `deadEntity` | `dieEntityId` | [str](../common/type-system.md#str) | 只读 | 死亡实体的entityId |
| `attacker` | `attacker` | [str](../common/type-system.md#str) | 只读 | 伤害来源的entityId |
| `itemList` | `itemList` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 只读 | 掉落物品列表，每个元素为一个itemDict，格式可参考物品信息字典 |
| `itemEntities` | `itemEntityIdList` | [list](../common/type-system.md#list)([str](../common/type-system.md#str)) | 只读 | 掉落物品entityId列表 |

**原生前提与限制：**

- 该事件为生物死亡掉落物品生成后触发，可以得到掉落物的id列表，如果需要更改掉落物，请使用[EntityDieLoottableServerEvent](native-events.md#entitydieloottableserverevent)
  - 该事件在生物死亡后会触发，无论是否掉落物品，因此掉落物品列表可能存在为空的情况
  - 掉落物不包含玩家或生物携带以及背包内的物品，若要获取死亡后由背包扔出的物品请参考EntityDroppedItemServerEvent事件

### EntityMotionStartServerEvent {#entitymotionstartserverevent}

实体运动器开始事件。实体（包含玩家）添加运动器后，运动器开始运行时触发

信号：[world.afterEvents.entityMotionStart](events/afterEvents.md#entityMotionStart)。分类：实体。

参数类型：[WorldEntityMotionStartAfterEvent](reference/WorldEntityMotionStartAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("EntityMotionStartServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `motionId` | `motionId` | [int](../common/type-system.md#int) | 只读 | 运动器id |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |

### EntityPickupItemServerEvent {#entitypickupitemserverevent}

有minecraft:behavior.pickup_items行为的生物拾取物品时触发该事件，例如村民拾取面包、猪灵拾取金锭

信号：[world.afterEvents.entityPickupItem](events/afterEvents.md#entityPickupItem)。分类：实体。

参数类型：[WorldEntityPickupItemAfterEvent](reference/WorldEntityPickupItemAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("EntityPickupItemServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 生物Id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 拾取的物品的物品信息字典 |
| `secondaryActor` | `secondaryActor` | [str](../common/type-system.md#str) | 只读 | 物品给予者id（一般是玩家），如果不存在给予者的话，这里为空字符串 |

### EntityPlaceBlockAfterServerEvent {#entityplaceblockafterserverevent}

触发时机：当生物成功放置方块后触发

信号：[world.afterEvents.entityPlaceBlock](events/afterEvents.md#entityPlaceBlock)。分类：方块。

参数类型：[WorldEntityPlaceBlockAfterEvent](reference/WorldEntityPlaceBlockAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("EntityPlaceBlockAfterServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `fullName` | `fullName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxData` | `auxData` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 试图放置方块的生物ID |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `face` | `face` | [int](../common/type-system.md#int) | 只读 | 点击方块的面，参考Facing枚举 |

**原生前提与限制：**

- 部分放置后会产生实体的方块、可操作的方块、带有特殊逻辑的方块，不会触发该事件，包括但不限于床、门、告示牌、花盆、红石中继器、船、炼药锅、头部模型、蛋糕、酿造台、盔甲架等。

### EntityRemoveEvent {#entityremoveevent}

实体被删除时触发

信号：`world.afterEvents.getNativeEvent('EntityRemoveEvent')`。分类：世界。

参数类型：[WorldEntityRemoveAfterEvent](reference/WorldEntityRemoveAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("EntityRemoveEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |

**原生前提与限制：**

- 触发情景：实体从场景中被删除，例如：生物死亡，生物被[清除 （在新窗口打开）](https://zh.minecraft.wiki/w/%E7%94%9F%E6%88%90#%E6%B8%85%E9%99%A4)，玩家退出游戏，船/盔甲架被破坏，掉落物/经验球被捡起或清除
  - 当生物随区块卸载时，不会触发该事件，而是ChunkAcquireDiscardedServerEvent事件
  - 关于生物的清除：当生物离玩家大于wiki所说的距离，并且还在玩家的模拟距离内时，会被清除。也就是说，如果玩家瞬间传送到远处，原处的生物马上离开了模拟距离，并不会被清除
  - 玩家退出游戏时，[EntityRemoveEvent](native-events.md#entityremoveevent)，DelServerPlayerEvent按顺序依次触发

### EntityStartRidingEvent {#entitystartridingevent}

当实体骑乘上另一个实体时触发

信号：[world.afterEvents.entityStartRiding](events/afterEvents.md#entityStartRiding)。分类：实体。

参数类型：[WorldEntityStartRidingAfterEvent](reference/WorldEntityStartRidingAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("EntityStartRidingEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 乘骑者实体id |
| `mount` | `rideId` | [str](../common/type-system.md#str) | 只读 | 被乘骑者实体id |

### MountTamingEvent {#mounttamingevent}

玩家通过骑乘驯服生物后触发该事件

信号：[world.afterEvents.entityTame](events/afterEvents.md#entityTame)。分类：玩家。

参数类型：[WorldEntityTameAfterEvent](reference/WorldEntityTameAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("MountTamingEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `eid` | [str](../common/type-system.md#str) | 只读 | 生物id |
| `player` | `pid` | [str](../common/type-system.md#str) | 只读 | 玩家id |

**原生前提与限制：**

- 该事件是检测minecraft:tamemount行为包组件，即玩家通过不断骑乘生物，使其冒出爱心时触发

### EntityTickServerEvent {#entitytickserverevent}

实体tick时触发。该事件为20帧每秒。需要使用AddEntityTickEventWhiteList添加触发该事件的实体类型白名单。

信号：[world.afterEvents.entityTick](events/afterEvents.md#entityTick)。分类：实体。

参数类型：[WorldEntityTickAfterEvent](reference/WorldEntityTickAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("EntityTickServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `identifier` | `identifier` | [str](../common/type-system.md#str) | 只读 | 实体identifier |

### FallingBlockReturnHeavyBlockServerEvent {#fallingblockreturnheavyblockserverevent}

触发时机：当下落的方块实体变回普通重力方块时，服务端触发该事件

信号：[world.afterEvents.fallingBlockReturnHeavyBlock](events/afterEvents.md#fallingBlockReturnHeavyBlock)。分类：方块。

参数类型：[WorldFallingBlockReturnHeavyBlockAfterEvent](reference/WorldFallingBlockReturnHeavyBlockAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("FallingBlockReturnHeavyBlockServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `fallingBlock` | `fallingBlockId` | [int](../common/type-system.md#int) | 只读 | 下落的方块实体id |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 方块位置x |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 方块位置y |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 方块位置z |
| `heavyBlockName` | `heavyBlockName` | [str](../common/type-system.md#str) | 只读 | 重力方块的identifier，包含命名空间及名称 |
| `prevHereBlockName` | `prevHereBlockName` | [str](../common/type-system.md#str) | 只读 | 变回重力方块时，原本方块位置的identifier，包含命名空间及名称 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 下落的方块实体维度id |
| `fallTickAmount` | `fallTickAmount` | [int](../common/type-system.md#int) | 只读 | 下落的方块实体持续下落了多少tick |

**原生前提与限制：**

- 不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义重力方块）

### FarmBlockToDirtBlockServerEvent {#farmblocktodirtblockserverevent}

触发时机：耕地退化为泥土时触发

信号：[world.afterEvents.farmBlockToDirtBlock](events/afterEvents.md#farmBlockToDirtBlock)。分类：方块。

参数类型：[WorldFarmBlockToDirtBlockAfterEvent](reference/WorldFarmBlockToDirtBlockAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("FarmBlockToDirtBlockServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 方块维度 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `setBlockType` | `setBlockType` | [int](../common/type-system.md#int) | 只读 | 耕地退化为泥土的原因，参考SetBlockType |

**原生前提与限制：**

- 指令或者接口的设置不会触发该事件

### FurnaceBurnFinishedServerEvent {#furnaceburnfinishedserverevent}

服务端熔炉烧制触发事件。熔炉, 高炉，烟熏炉烧出物品时触发

信号：[world.afterEvents.furnaceBurnFinish](events/afterEvents.md#furnaceBurnFinish)。分类：物品。

参数类型：[WorldFurnaceBurnFinishAfterEvent](reference/WorldFurnaceBurnFinishAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("FurnaceBurnFinishedServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `posX` | `posX` | [float](../common/type-system.md#float) | 只读 | 位置x |
| `posY` | `posY` | [float](../common/type-system.md#float) | 只读 | 位置y |
| `posZ` | `posZ` | [float](../common/type-system.md#float) | 只读 | 位置z |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 物品的物品信息字典，当新物品为空时，此项属性为[None](../common/type-system.md#none) |

### GameTypeChangedServerEvent {#gametypechangedserverevent}

当默认游戏模式或个人游戏模式发生变化时服务端触发，如果个人游戏模式不为默认时，修改默认游戏模式也会同时修改个人游戏模式，此时会触发两次该事件

信号：[world.afterEvents.gameTypeChange](events/afterEvents.md#gameTypeChange)。分类：玩家。

参数类型：[WorldGameTypeChangeAfterEvent](reference/WorldGameTypeChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("GameTypeChangedServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家Id，SetDefaultGameType接口改变游戏模式时该参数为空字符串 |
| `oldGameType` | `oldGameType` | [int](../common/type-system.md#int) | 只读 | 切换前的游戏模式 |
| `newGameType` | `newGameType` | [int](../common/type-system.md#int) | 只读 | 切换后的游戏模式 |

**原生前提与限制：**

- 游戏模式：GetMinecraftEnum().GameType.\*:Survival，Creative，Adventure分别为0~2，Spectator为6
    默认游戏模式发生变化时最后反映在个人游戏模式之上。
    注意：避免在该事件中调用修改ability相关的接口，比如ChangePlayerFlyState等接口，如确实需要，可加定时器延后调用

### GrassBlockToDirtBlockServerEvent {#grassblocktodirtblockserverevent}

触发时机：草方块变成泥土方块时触发

信号：[world.afterEvents.grassBlockToDirtBlock](events/afterEvents.md#grassBlockToDirtBlock)。分类：方块。

参数类型：[WorldGrassBlockToDirtBlockAfterEvent](reference/WorldGrassBlockToDirtBlockAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("GrassBlockToDirtBlockServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 方块维度 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |

**原生前提与限制：**

- 指令或者接口的设置不会触发该事件

### HeavyBlockStartFallingServerEvent {#heavyblockstartfallingserverevent}

触发时机：当重力方块变为下落的方块实体后，服务端触发该事件

信号：[world.afterEvents.heavyBlockStartFalling](events/afterEvents.md#heavyBlockStartFalling)。分类：方块。

参数类型：[WorldHeavyBlockStartFallingAfterEvent](reference/WorldHeavyBlockStartFallingAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("HeavyBlockStartFallingServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `fallingBlock` | `fallingBlockId` | [str](../common/type-system.md#str) | 只读 | 下落的方块实体id |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 方块位置x |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 方块位置y |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 方块位置z |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 重力方块的identifier，包含命名空间及名称 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 下落的方块实体维度id |

**原生前提与限制：**

- 不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义重力方块）

### HopperTryPullInServerEvent {#hoppertrypullinserverevent}

触发时机：当漏斗上方连接容器后，容器往漏斗开始输入物品时触发，事件仅触发一次

信号：[world.afterEvents.hopperTryPullIn](events/afterEvents.md#hopperTryPullIn)。分类：方块。

参数类型：[WorldHopperTryPullInAfterEvent](reference/WorldHopperTryPullInAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("HopperTryPullInServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 漏斗位置x |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 漏斗位置y |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 漏斗位置z |
| `abovePosX` | `abovePosX` | [int](../common/type-system.md#int) | 只读 | 交互的容器位置x |
| `abovePosY` | `abovePosY` | [int](../common/type-system.md#int) | 只读 | 交互的容器位置y |
| `abovePosZ` | `abovePosZ` | [int](../common/type-system.md#int) | 只读 | 交互的容器位置z |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `canHopper` | `canHopper` | [bool](../common/type-system.md#bool) | 只读 | 是否允许容器往漏斗加东西(要关闭此交互，需先监听此事件再放置容器) |

### HopperTryPullOutServerEvent {#hoppertrypulloutserverevent}

触发时机：当漏斗以毗邻的方式连接容器时，即从旁边连接容器时，漏斗向容器开始输出物品时触发，事件仅触发一次

信号：[world.afterEvents.hopperTryPullOut](events/afterEvents.md#hopperTryPullOut)。分类：方块。

参数类型：[WorldHopperTryPullOutAfterEvent](reference/WorldHopperTryPullOutAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("HopperTryPullOutServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 漏斗位置x |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 漏斗位置y |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 漏斗位置z |
| `attachedPosX` | `attachedPosX` | [int](../common/type-system.md#int) | 只读 | 交互的容器位置x |
| `attachedPosY` | `attachedPosY` | [int](../common/type-system.md#int) | 只读 | 交互的容器位置y |
| `attachedPosZ` | `attachedPosZ` | [int](../common/type-system.md#int) | 只读 | 交互的容器位置z |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `canHopper` | `canHopper` | [bool](../common/type-system.md#bool) | 只读 | 是否允许漏斗往容器加东西(要关闭此交互，需先监听此事件再放置容器) |

### ItemUseAfterServerEvent {#itemuseafterserverevent}

玩家在使用物品之后服务端抛出的事件。

信号：`world.afterEvents.getNativeEvent('ItemUseAfterServerEvent')`。分类：物品。

参数类型：[WorldItemUseAfterEvent](reference/WorldItemUseAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("ItemUseAfterServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 使用的物品的物品信息字典 |

**原生前提与限制：**

- 做出使用物品这个动作之后触发，一些需要蓄力的物品使用事件([ActorUseItemServerEvent](native-events.md#actoruseitemserverevent))会在之后触发。如投掷三叉戟，先触发本事件，投出去之后再触发[ActorUseItemServerEvent](native-events.md#actoruseitemserverevent)

### ItemUseOnAfterServerEvent {#itemuseonafterserverevent}

玩家在对方块使用物品之后服务端抛出的事件。

信号：`world.afterEvents.getNativeEvent('ItemUseOnAfterServerEvent')`。分类：物品。

参数类型：[WorldItemUseOnAfterEvent](reference/WorldItemUseOnAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("ItemUseOnAfterServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 使用的物品的物品信息字典 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块 x 坐标值 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块 y 坐标值 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块 z 坐标值 |
| `face` | `face` | [int](../common/type-system.md#int) | 只读 | 点击方块的面，参考Facing枚举 |
| `clickX` | `clickX` | [float](../common/type-system.md#float) | 只读 | 点击点的x比例位置 |
| `clickY` | `clickY` | [float](../common/type-system.md#float) | 只读 | 点击点的y比例位置 |
| `clickZ` | `clickZ` | [float](../common/type-system.md#float) | 只读 | 点击点的z比例位置 |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier |
| `blockAuxValue` | `blockAuxValue` | [int](../common/type-system.md#int) | 只读 | 方块的附加值 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |

**原生前提与限制：**

- 在ServerItemUseOnEvent和原版物品使用事件（例如[StartUsingItemClientEvent](../client/events.md#startusingitemclientevent)）之后触发

### JumpAnimBeginServerEvent {#jumpanimbeginserverevent}

当跳跃动作开始时触发

信号：[world.afterEvents.jumpAnimBegin](events/afterEvents.md#jumpAnimBegin)。分类：模型。

参数类型：[WorldJumpAnimBeginAfterEvent](reference/WorldJumpAnimBeginAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("JumpAnimBeginServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |

**原生前提与限制：**

- 使用SetModel替换骨骼模型后，该事件才生效

### OnLightningLevelChangeServerEvent {#onlightninglevelchangeserverevent}

打雷强度发生改变

信号：`world.afterEvents.getNativeEvent('OnLightningLevelChangeServerEvent')`。分类：世界。

参数类型：[WorldLightningLevelChangeAfterEvent](reference/WorldLightningLevelChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnLightningLevelChangeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `oldLevel` | `oldLevel` | [float](../common/type-system.md#float) | 只读 | 改变前的打雷强度 |
| `newLevel` | `newLevel` | [float](../common/type-system.md#float) | 只读 | 改变后的打雷强度 |

### LiquidClippedServerEvent {#liquidclippedserverevent}

玩家服务端点击流体时触发（支持原版流体与自定义流体）

信号：[world.afterEvents.liquidClipped](events/afterEvents.md#liquidClipped)。分类：物品。

参数类型：[WorldLiquidClippedAfterEvent](reference/WorldLiquidClippedAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("LiquidClippedServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家Id |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `aux` | `aux` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |
| `blockPos` | `blockPos` | [tuple](../common/type-system.md#tuple)([int](../common/type-system.md#int),[int](../common/type-system.md#int),[int](../common/type-system.md#int)) | 只读 | 方块坐标(x,y,z) |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `floatPos` | `floatPos` | [tuple](../common/type-system.md#tuple)([float](../common/type-system.md#float),[float](../common/type-system.md#float),[float](../common/type-system.md#float)) | 只读 | 点击的精准坐标(x,y,z) |

**原生前提与限制：**

- 需要在物品中添加netease:liquid_clipped: True组件才能触发

### lobbyGoodBuySucServerEvent {#lobbygoodbuysucserverevent}

玩家登录联机大厅服务器，或者联机大厅游戏内购买商品时触发。如果是玩家登录，触发时玩家客户端已经触发了UiInitFinished事件

信号：[world.afterEvents.lobbyPurchase](events/afterEvents.md#lobbyPurchase)。分类：联机大厅。

参数类型：[WorldLobbyPurchaseAfterEvent](reference/WorldLobbyPurchaseAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("lobbyGoodBuySucServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `eid` | [str](../common/type-system.md#str) | 只读 | 购买商品的玩家实体id |
| `buyItem` | `buyItem` | [bool](../common/type-system.md#bool) | 只读 | 玩家登录时为False，玩家购买了商品时为True |

### OnLocalLightningLevelChangeServerEvent {#onlocallightninglevelchangeserverevent}

独立维度天气打雷强度发生改变时触发

信号：`world.afterEvents.getNativeEvent('OnLocalLightningLevelChangeServerEvent')`。分类：世界。

参数类型：[WorldLocalLightningLevelChangeAfterEvent](reference/WorldLocalLightningLevelChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnLocalLightningLevelChangeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `oldLevel` | `oldLevel` | [float](../common/type-system.md#float) | 只读 | 改变前的打雷强度 |
| `newLevel` | `newLevel` | [float](../common/type-system.md#float) | 只读 | 改变后的打雷强度 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 独立天气维度id |

### OnLocalRainLevelChangeServerEvent {#onlocalrainlevelchangeserverevent}

独立维度天气下雨强度发生改变时触发

信号：`world.afterEvents.getNativeEvent('OnLocalRainLevelChangeServerEvent')`。分类：世界。

参数类型：[WorldLocalRainLevelChangeAfterEvent](reference/WorldLocalRainLevelChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnLocalRainLevelChangeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `oldLevel` | `oldLevel` | [float](../common/type-system.md#float) | 只读 | 改变前的下雨强度 |
| `newLevel` | `newLevel` | [float](../common/type-system.md#float) | 只读 | 改变后的下雨强度 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 独立天气维度id |

### MobDieEvent {#mobdieevent}

实体死亡时触发

信号：`world.afterEvents.getNativeEvent('MobDieEvent')`。分类：实体。

参数类型：[WorldMobDieAfterEvent](reference/WorldMobDieAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("MobDieEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `attacker` | `attacker` | [str](../common/type-system.md#str) | 只读 | 伤害来源id |
| `cause` | `cause` | [str](../common/type-system.md#str) | 只读 | 伤害来源，详见Minecraft枚举值文档的ActorDamageCause |
| `customTag` | `customTag` | [str](../common/type-system.md#str) | 只读 | 使用Hurt接口传入的自定义伤害类型 |

**原生前提与限制：**

- 注意：不能在该事件回调中对此玩家手持物品进行修改，如SpawnItemToPlayerCarried、ChangePlayerItemTipsAndExtraId等接口

### AddEffectServerEvent {#addeffectserverevent}

触发时机：实体获得状态效果时

信号：`world.afterEvents.getNativeEvent('AddEffectServerEvent')`。分类：实体。

参数类型：[WorldNativeEffectAddAfterEvent](reference/WorldNativeEffectAddAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("AddEffectServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `effectName` | `effectName` | [str](../common/type-system.md#str) | 只读 | 实体获得状态效果的名字 |
| `effectDuration` | `effectDuration` | [int](../common/type-system.md#int) | 只读 | 状态效果的持续时间，单位秒 |
| `effectAmplifier` | `effectAmplifier` | [int](../common/type-system.md#int) | 只读 | 状态效果的放大倍数 |
| `damage` | `damage` | [float](../common/type-system.md#float) | 只读 | 状态造成的伤害值（真实扣除生命值的量）。只有持续时间为0时有用 |

### HealthChangeServerEvent {#healthchangeserverevent}

生物生命值发生变化时触发

信号：`world.afterEvents.getNativeEvent('HealthChangeServerEvent')`。分类：实体。

参数类型：[WorldNativeEntityHealthChangeAfterEvent](reference/WorldNativeEntityHealthChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("HealthChangeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `fromValue` | `from` | [float](../common/type-system.md#float) | 只读 | 变化前的生命值 |
| `to` | `to` | [float](../common/type-system.md#float) | 只读 | 变化后的生命值 |
| `byScript` | `byScript` | [bool](../common/type-system.md#bool) | 只读 | 是否通过SetAttrValue或SetAttrMaxValue调用产生的变化 |

### InventoryItemChangedServerEvent {#inventoryitemchangedserverevent}

玩家背包物品变化时服务端抛出的事件。

信号：`world.afterEvents.getNativeEvent('InventoryItemChangedServerEvent')`。分类：物品。

参数类型：[WorldNativePlayerInventoryItemChangeAfterEvent](reference/WorldNativePlayerInventoryItemChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("InventoryItemChangedServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `slot` | `slot` | [int](../common/type-system.md#int) | 只读 | 背包槽位 |
| `oldItemDict` | `oldItemDict` | [dict](../common/type-system.md#dict) | 只读 | 变化前槽位中的物品，格式参考物品信息字典 |
| `newItemDict` | `newItemDict` | [dict](../common/type-system.md#dict) | 只读 | 变化后槽位中的物品，格式参考物品信息字典 |

**原生前提与限制：**

- 如果槽位变空，变化后槽位中物品为空气
  - 触发时槽位物品仍为变化前物品
  - 玩家进入游戏时，身上的物品会触发该事件
  - 背包内物品移动，合堆，分堆的操作会分多次事件触发并且顺序不定，编写逻辑时请勿依赖事件触发顺序

### PhysxTouchServerEvent {#physxtouchserverevent}

给自定义刚体添加的碰撞体，与其他碰撞体或原版实体发生碰撞/结束碰撞时触发。需要在碰撞体创建时使用PxEventMask.Server才会触发

信号：`world.afterEvents.getNativeEvent('PhysxTouchServerEvent')`。分类：物理。

参数类型：[WorldPhysicsTouchAfterEvent](reference/WorldPhysicsTouchAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PhysxTouchServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `touch` | `touch` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 只读 | 开始接触的碰撞体对的信息。一个碰撞体在创建时使用了PxEventMask.Found，他与其他碰撞体/原版实体开始接触时，会出现在列表中 |
| `lost` | `lost` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 只读 | 结束接触的碰撞体对的信息。一个碰撞体在创建时使用了PxEventMask.Lost，他与其他碰撞体/原版实体结束接触时，会出现在列表中 |

**原生前提与限制：**

- touch列表每个元素的内容：

    

    lost列表每个元素的内容：

    

  - 列表中的碰撞对不分先后，每个碰撞对中的碰撞体0与碰撞体1也不分先后

### PhysxTriggerServerEvent {#physxtriggerserverevent}

给自定义刚体添加的触发器，与其他碰撞体或原版实体发生进入触发器/离开触发器时触发。需要在触发器创建时使用PxEventMask.Server才会触发

信号：`world.afterEvents.getNativeEvent('PhysxTriggerServerEvent')`。分类：物理。

参数类型：[WorldPhysicsTriggerAfterEvent](reference/WorldPhysicsTriggerAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PhysxTriggerServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `found` | `found` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 只读 | 进入触发器的碰撞体对的信息。一个碰撞体在创建时使用了PxEventMask.Found，它与其他碰撞体/原版实体进入触发器时，会出现在列表中 |
| `lost` | `lost` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 只读 | 离开触发器的碰撞体对的信息。一个碰撞体在创建时使用了PxEventMask.Lost，它与其他碰撞体/原版实体离开触发器时，会出现在列表中 |

**原生前提与限制：**

- found列表每个元素的内容：

    

    lost列表每个元素的内容：

    

  - 列表中的碰撞对不分先后，每个碰撞对中的碰撞体0与碰撞体1的具体角色取决于底层触发逻辑。

### ServerPlaceBlockEntityEvent {#serverplaceblockentityevent}

触发时机：手动放置或通过接口创建含自定义方块实体的方块时触发，此时可向该方块实体中存放数据

信号：[world.afterEvents.placeBlockEntity](events/afterEvents.md#placeBlockEntity)。分类：方块。

参数类型：[WorldPlaceBlockEntityAfterEvent](reference/WorldPlaceBlockEntityAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("ServerPlaceBlockEntityEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 该方块名称 |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 该方块所在的维度 |
| `posX` | `posX` | [int](../common/type-system.md#int) | 只读 | 该方块的x坐标 |
| `posY` | `posY` | [int](../common/type-system.md#int) | 只读 | 该方块的y坐标 |
| `posZ` | `posZ` | [int](../common/type-system.md#int) | 只读 | 该方块的z坐标 |

### OnPlayerActionServerEvent {#onplayeractionserverevent}

玩家动作事件，当玩家开始/停止某些动作时触发该事件

信号：`world.afterEvents.getNativeEvent('OnPlayerActionServerEvent')`。分类：玩家。

参数类型：[WorldPlayerActionAfterEvent](reference/WorldPlayerActionAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnPlayerActionServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `actionType` | `actionType` | [int](../common/type-system.md#int) | 只读 | 动作事件枚举，详见Minecraft枚举值文档的PlayerActionType |

### AddServerPlayerEvent {#addserverplayerevent}

触发时机：玩家加入时触发该事件。

信号：[world.afterEvents.playerAdd](events/afterEvents.md#playerAdd)。分类：世界。

参数类型：[WorldPlayerAddAfterEvent](reference/WorldPlayerAddAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("AddServerPlayerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `id` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `isTransfer` | `isTransfer` | [bool](../common/type-system.md#bool) | 只读 | 是否是切服时进入服务器，仅用于Apollo。如果是True，则表示切服时加入服务器，若是False，则表示登录进入网络游戏 |
| `isReconnect` | `isReconnect` | [bool](../common/type-system.md#bool) | 只读 | 是否是断线重连，仅用于Apollo。如果是True，则表示本次登录是断线重连，若是False，则表示本次是正常登录或者转服 |
| `isPeUser` | `isPeUser` | [bool](../common/type-system.md#bool) | 只读 | 是否从手机端登录，仅用于Apollo。如果是True，则表示本次登录是从手机端登录，若是False，则表示本次登录是从PC端登录 |
| `transferParam` | `transferParam` | [str](../common/type-system.md#str) | 只读 | 切服传入参数，仅用于Apollo。调用【TransferToOtherServer】或【TransferToOtherServerById】传入的切服参数 |
| `uid` | `uid` | [int](../common/type-system.md#int)/[long](../common/type-system.md#long) | 只读 | 仅用于Apollo，玩家的netease uid，玩家的唯一标识 |
| `proxyId` | `proxyId` | [int](../common/type-system.md#int) | 只读 | 仅用于Apollo，当前客户端连接的proxy服务器id |

**原生前提与限制：**

- 触发此事件时，客户端mod未加载完毕，因此响应本事件时不能客户端发送事件。若需要在玩家进入世界时，服务器往客户端发送事件，请使用[ClientLoadAddonsFinishServerEvent](native-events.md#clientloadaddonsfinishserverevent)
  - 触发此事件时，玩家的实体还未加载完毕，请勿在这时切换维度。请在客户端监听OnLocalPlayerStopLoading事件并发送事件到server端再进行维度切换。

### PlayerAddCustomContainerItemServerEvent {#playeraddcustomcontaineritemserverevent}

玩家向自定义容器中添加物品成功后触发该事件。该事件不可取消，仅用于通知物品添加操作已完成。

信号：[world.afterEvents.playerAddCustomContainerItem](events/afterEvents.md#playerAddCustomContainerItem)。分类：物品。

参数类型：[WorldPlayerAddCustomContainerItemAfterEvent](reference/WorldPlayerAddCustomContainerItemAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PlayerAddCustomContainerItemServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `beforeItemDict` | `beforeItemDict` | [dict](../common/type-system.md#dict) | 只读 | 操作前目标槽位的物品信息字典 |
| `changedItemDict` | `changedItemDict` | [dict](../common/type-system.md#dict) | 只读 | 实际添加的物品的物品信息字典 |
| `afterItemDict` | `afterItemDict` | [dict](../common/type-system.md#dict) | 只读 | 操作后目标槽位的物品信息字典 |
| `collectionName` | `collectionName` | [str](../common/type-system.md#str) | 只读 | 容器名称，对应容器json中"custom_description"字段 |
| `collectionType` | `collectionType` | [str](../common/type-system.md#str) | 只读 | 容器类型，目前仅支持netease_container和netease_ui_container |
| `collectionIndex` | `collectionIndex` | [int](../common/type-system.md#int) | 只读 | 目标容器索引 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 容器方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 容器方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 容器方块z坐标 |

**原生前提与限制：**

- 该事件仅在操作成功后触发，且不可取消。事件提供三个物品字典：操作前状态、实际变化的物品、操作后状态，便于精确追踪物品变化。
  - 当目标槽位接近满仓时，实际添加的数量可能小于请求添加的数量，changedItemDict反映实际添加的物品信息。

### OnNewArmorExchangeServerEvent {#onnewarmorexchangeserverevent}

触发时机：玩家切换盔甲时触发该事件

信号：`world.afterEvents.getNativeEvent('OnNewArmorExchangeServerEvent')`。分类：物品。

参数类型：[WorldPlayerArmorChangeAfterEvent](reference/WorldPlayerArmorChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnNewArmorExchangeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `slot` | `slot` | [int](../common/type-system.md#int) | 只读 | 槽位id |
| `oldArmorDict` | `oldArmorDict` | [dict](../common/type-system.md#dict)/[None](../common/type-system.md#none) | 只读 | 旧装备的物品信息字典，当旧物品为空时，此项属性为[None](../common/type-system.md#none) |
| `newArmorDict` | `newArmorDict` | [dict](../common/type-system.md#dict)/[None](../common/type-system.md#none) | 只读 | 新装备的物品信息字典，当新物品为空时，此项属性为[None](../common/type-system.md#none) |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家 entityId |

**原生前提与限制：**

- 当玩家登录时，每个盔甲槽位会触发两次该事件，第一次为None切换到身上的装备，第二次的old和new都为身上装备。如果槽位为空，则是触发两次从None切换到None的事件。
  - 注意：避免在该事件回调中对玩家修改盔甲栏装备，如SetEntityItem接口，会导致事件循环触发造成堆栈溢出。

### OnPlayerBlockedByShieldAfterServerEvent {#onplayerblockedbyshieldafterserverevent}

触发时机：玩家使用盾牌抵挡伤害之后触发

信号：[world.afterEvents.playerBlockedByShield](events/afterEvents.md#playerBlockedByShield)。分类：物品。

参数类型：[WorldPlayerBlockedByShieldAfterEvent](reference/WorldPlayerBlockedByShieldAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnPlayerBlockedByShieldAfterServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家Id |
| `source` | `sourceId` | [str](../common/type-system.md#str) | 只读 | 伤害来源实体Id，没有实体返回"-1" |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 盾牌物品字典物品信息字典 |
| `damage` | `damage` | [float](../common/type-system.md#float) | 只读 | 抵挡的伤害数值 |

### PlayerCheatSpinAttackServerEvent {#playercheatspinattackserverevent}

触发时机：玩家开始/结束快速旋转攻击并且不符合发送快速旋转攻击条件时触发（装备激流附魔的三叉戟、在水中或雨中，且未骑乘）

信号：[world.afterEvents.playerCheatSpinAttack](events/afterEvents.md#playerCheatSpinAttack)。分类：玩家。

参数类型：[WorldPlayerCheatSpinAttackAfterEvent](reference/WorldPlayerCheatSpinAttackAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PlayerCheatSpinAttackServerEvent")`。

:::warning 平台条件
此事件仅在 Apollo 环境中提供；普通联机/单机不会因此得到同等能力。
:::

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家的entityId |
| `isStart` | `isStart` | [bool](../common/type-system.md#bool) | 只读 | True时代表开始快速旋转攻击；False时代表结束快速旋转攻击 |

**原生前提与限制：**

- 假如没有自定义类似三叉戟/激流附魔的物品，那么触发此事件说明此有很大可能此玩家使用了【杀戮光环】外挂

### PlayerDieEvent {#playerdieevent}

触发时机：当玩家死亡时触发该事件。

信号：[world.afterEvents.playerDie](events/afterEvents.md#playerDie)。分类：玩家。

参数类型：[WorldPlayerDieAfterEvent](reference/WorldPlayerDieAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PlayerDieEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `id` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `attacker` | `attacker` | [str](../common/type-system.md#str) | 只读 | 伤害来源id |
| `customTag` | `customTag` | [str](../common/type-system.md#str) | 只读 | 使用Hurt接口传入的自定义伤害类型 |
| `cause` | `cause` | [str](../common/type-system.md#str) | 只读 | 伤害来源，详见Minecraft枚举值文档的ActorDamageCause |

### DimensionChangeFinishServerEvent {#dimensionchangefinishserverevent}

玩家维度改变完成后服务端抛出

信号：[world.afterEvents.playerDimensionChangeFinish](events/afterEvents.md#playerDimensionChangeFinish)。分类：玩家。

参数类型：[WorldPlayerDimensionChangeFinishAfterEvent](reference/WorldPlayerDimensionChangeFinishAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("DimensionChangeFinishServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `fromDimension` | `fromDimensionId` | [int](../common/type-system.md#int) | 只读 | 维度改变前的维度 |
| `toDimension` | `toDimensionId` | [int](../common/type-system.md#int) | 只读 | 维度改变后的维度 |
| `toPos` | `toPos` | [tuple](../common/type-system.md#tuple)([float](../common/type-system.md#float),[float](../common/type-system.md#float),[float](../common/type-system.md#float)) | 只读 | 改变后的位置x,y,z,其中y值为脚底加上角色的身高值 |

**原生前提与限制：**

- 当通过传送门从末地回到主世界时，toPos的y值为32767，其他情况一般会比设置值高1.62

### DimensionChangeServerEvent {#dimensionchangeserverevent}

玩家维度改变时服务端抛出

信号：`world.afterEvents.getNativeEvent('DimensionChangeServerEvent')`。分类：玩家。

参数类型：[WorldPlayerDimensionChangeStartAfterEvent](reference/WorldPlayerDimensionChangeStartAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("DimensionChangeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `fromDimension` | `fromDimensionId` | [int](../common/type-system.md#int) | 只读 | 维度改变前的维度 |
| `toDimension` | `toDimensionId` | [int](../common/type-system.md#int) | 只读 | 维度改变后的维度 |
| `fromX` | `fromX` | [float](../common/type-system.md#float) | 只读 | 改变前的位置x |
| `fromY` | `fromY` | [float](../common/type-system.md#float) | 只读 | 改变前的位置Y |
| `fromZ` | `fromZ` | [float](../common/type-system.md#float) | 只读 | 改变前的位置Z |
| `toX` | `toX` | [float](../common/type-system.md#float) | 只读 | 改变后的位置x |
| `toY` | `toY` | [float](../common/type-system.md#float) | 只读 | 改变后的位置Y |
| `toZ` | `toZ` | [float](../common/type-system.md#float) | 只读 | 改变后的位置Z |

**原生前提与限制：**

- 当通过传送门从末地回到主世界时，toY值为32767，其他情况一般会比设置值高1.62

### PlayerDoInteractServerEvent {#playerdointeractserverevent}

玩家与有minecraft:interact组件的生物交互时触发该事件，例如玩家手持空桶对牛挤奶、玩家手持打火石点燃苦力怕

信号：`world.afterEvents.getNativeEvent('PlayerDoInteractServerEvent')`。分类：玩家。

参数类型：[WorldPlayerDoInteractAfterEvent](reference/WorldPlayerDoInteractAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PlayerDoInteractServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 交互时使用物品的物品信息字典 |
| `target` | `interactEntityId` | [str](../common/type-system.md#str) | 只读 | 交互的生物entityId |

### PlayerDropItemServerEvent {#playerdropitemserverevent}

触发时机：玩家丢弃物品时触发

信号：[world.afterEvents.playerDropItem](events/afterEvents.md#playerDropItem)。分类：物品。

参数类型：[WorldPlayerDropItemAfterEvent](reference/WorldPlayerDropItemAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PlayerDropItemServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `itemEntity` | `itemEntityId` | [str](../common/type-system.md#str) | 只读 | 物品entityId |

### AddExpEvent {#addexpevent}

触发时机：当玩家增加经验时触发该事件。

信号：[world.afterEvents.playerExperienceAdd](events/afterEvents.md#playerExperienceAdd)。分类：玩家。

参数类型：[WorldPlayerExperienceAddAfterEvent](reference/WorldPlayerExperienceAddAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("AddExpEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `id` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `addExp` | `addExp` | [int](../common/type-system.md#int) | 只读 | 增加的经验值 |

### PlayerFishingAfterServerEvent {#playerfishingafterserverevent}

玩家钓鱼成功收杆后触发，在钓鱼掉落物生成后触发

信号：[world.afterEvents.playerFishing](events/afterEvents.md#playerFishing)。分类：玩家。

参数类型：[WorldPlayerFishingAfterEvent](reference/WorldPlayerFishingAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PlayerFishingAfterServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 钓鱼的玩家id |
| `hook` | `hookEntity` | [str](../common/type-system.md#str) | 只读 | 鱼钩实体id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 玩家手持鱼竿的物品信息字典 |
| `itemList` | `itemList` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 只读 | 钓鱼获得的物品信息字典列表（只读） |
| `itemEntities` | `itemEntityIdList` | [list](../common/type-system.md#list)([str](../common/type-system.md#str)) | 只读 | 钓鱼生成的掉落物实体id列表，与itemList一一对应 |

**原生前提与限制：**

- 此事件在掉落物实体生成后触发，可通过itemEntityIdList获取生成的掉落物实体id进行后续操作

### OnPlayerHitBlockServerEvent {#onplayerhitblockserverevent}

触发时机：通过OpenPlayerHitBlockDetection打开方块碰撞检测后，当玩家碰撞到方块时触发该事件。监听玩家着地请使用客户端的[OnGroundClientEvent](../client/events.md#ongroundclientevent)。客户端和服务端分别作碰撞检测，可能两个事件返回的略有差异。

信号：[world.afterEvents.playerHitBlock](events/afterEvents.md#playerHitBlock)。分类：玩家。

参数类型：[WorldPlayerHitBlockAfterEvent](reference/WorldPlayerHitBlockAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnPlayerHitBlockServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 碰撞到方块的玩家Id |
| `posX` | `posX` | [int](../common/type-system.md#int) | 只读 | 碰撞方块x坐标 |
| `posY` | `posY` | [int](../common/type-system.md#int) | 只读 | 碰撞方块y坐标 |
| `posZ` | `posZ` | [int](../common/type-system.md#int) | 只读 | 碰撞方块z坐标 |
| `blockId` | `blockId` | [str](../common/type-system.md#str) | 只读 | 碰撞方块的identifier |
| `auxValue` | `auxValue` | [int](../common/type-system.md#int) | 只读 | 碰撞方块的附加值 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |

**原生前提与限制：**

- 注：该碰撞检测会屏蔽草、空气、火、高草四种方块

### OnCarriedNewItemChangedServerEvent {#oncarriednewitemchangedserverevent}

触发时机：玩家切换主手物品时触发该事件

信号：`world.afterEvents.getNativeEvent('OnCarriedNewItemChangedServerEvent')`。分类：物品。

参数类型：[WorldPlayerHotbarItemChangeAfterEvent](reference/WorldPlayerHotbarItemChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnCarriedNewItemChangedServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `oldItemDict` | `oldItemDict` | [dict](../common/type-system.md#dict)/[None](../common/type-system.md#none) | 只读 | 旧物品的物品信息字典，当旧物品为空时，此项属性为[None](../common/type-system.md#none) |
| `newItemDict` | `newItemDict` | [dict](../common/type-system.md#dict)/[None](../common/type-system.md#none) | 只读 | 新物品的物品信息字典，当新物品为空时，此项属性为[None](../common/type-system.md#none) |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家 entityId |

**原生前提与限制：**

- 切换耐久度不同的相同物品，不会触发该事件

### PlayerInventoryOpenScriptServerEvent {#playerinventoryopenscriptserverevent}

某个客户端打开物品背包界面时触发

信号：[world.afterEvents.playerInventoryOpenScript](events/afterEvents.md#playerInventoryOpenScript)。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[WorldPlayerInventoryOpenScriptAfterEvent](reference/WorldPlayerInventoryOpenScriptAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PlayerInventoryOpenScriptServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 客户端对应的玩家entity的唯一ID |
| `isCreative` | `isCreative` | [bool](../common/type-system.md#bool) | 只读 | 是否是创造模式背包界面 |

**原生前提与限制：**

- 可以监听此事件判定客户端是否打开了创造背包

### AddLevelEvent {#addlevelevent}

触发时机：当玩家升级时触发该事件。

信号：[world.afterEvents.playerLevelChange](events/afterEvents.md#playerLevelChange)。分类：玩家。

参数类型：[WorldPlayerLevelChangeAfterEvent](reference/WorldPlayerLevelChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("AddLevelEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `id` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `addLevel` | `addLevel` | [int](../common/type-system.md#int) | 只读 | 增加的等级值 |
| `newLevel` | `newLevel` | [int](../common/type-system.md#int) | 只读 | 新的等级 |

### OnOffhandItemChangedServerEvent {#onoffhanditemchangedserverevent}

触发时机：玩家切换副手物品时触发该事件

信号：`world.afterEvents.getNativeEvent('OnOffhandItemChangedServerEvent')`。分类：物品。

参数类型：[WorldPlayerOffhandItemChangeAfterEvent](reference/WorldPlayerOffhandItemChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnOffhandItemChangedServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `oldItemDict` | `oldItemDict` | [dict](../common/type-system.md#dict)/[None](../common/type-system.md#none) | 只读 | 旧物品的物品信息字典，当旧物品为空时，此项属性为[None](../common/type-system.md#none) |
| `newItemDict` | `newItemDict` | [dict](../common/type-system.md#dict)/[None](../common/type-system.md#none) | 只读 | 新物品的物品信息字典，当新物品为空时，此项属性为[None](../common/type-system.md#none) |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家 entityId |

**原生前提与限制：**

- 当原有的物品槽内容为空时，`oldItemName`值为'minecraft:air'，且`oldItem`其余字段不存在
    当切换原有物品，且新物品为空时，参数值同理

### DelServerPlayerEvent {#delserverplayerevent}

触发时机：删除玩家时触发该事件。

信号：[world.afterEvents.playerRemove](events/afterEvents.md#playerRemove)。分类：世界。

参数类型：[WorldPlayerRemoveAfterEvent](reference/WorldPlayerRemoveAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("DelServerPlayerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `id` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `isTransfer` | `isTransfer` | [bool](../common/type-system.md#bool) | 只读 | 是否是切服时退出服务器，仅用于Apollo。如果是True，则表示切服时退出服务器；若是False，则表示退出网络游戏 |
| `uid` | `uid` | [int](../common/type-system.md#int)/[long](../common/type-system.md#long) | 只读 | 玩家的netease uid，玩家的唯一标识 |

### PlayerRemoveCustomContainerItemServerEvent {#playerremovecustomcontaineritemserverevent}

玩家从自定义容器中移除物品成功后触发该事件。该事件不可取消，仅用于通知物品移除操作已完成。

信号：[world.afterEvents.playerRemoveCustomContainerItem](events/afterEvents.md#playerRemoveCustomContainerItem)。分类：物品。

参数类型：[WorldPlayerRemoveCustomContainerItemAfterEvent](reference/WorldPlayerRemoveCustomContainerItemAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PlayerRemoveCustomContainerItemServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `beforeItemDict` | `beforeItemDict` | [dict](../common/type-system.md#dict) | 只读 | 操作前目标槽位的物品信息字典 |
| `changedItemDict` | `changedItemDict` | [dict](../common/type-system.md#dict) | 只读 | 实际移除的物品的物品信息字典 |
| `afterItemDict` | `afterItemDict` | [dict](../common/type-system.md#dict) | 只读 | 操作后目标槽位的物品信息字典 |
| `collectionName` | `collectionName` | [str](../common/type-system.md#str) | 只读 | 容器名称，对应容器json中"custom_description"字段 |
| `collectionType` | `collectionType` | [str](../common/type-system.md#str) | 只读 | 容器类型，目前仅支持netease_container和netease_ui_container |
| `collectionIndex` | `collectionIndex` | [int](../common/type-system.md#int) | 只读 | 目标容器索引 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 容器方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 容器方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 容器方块z坐标 |

**原生前提与限制：**

- 该事件仅在操作成功后触发，且不可取消。事件提供三个物品字典：操作前状态、实际变化的物品、操作后状态，便于精确追踪物品变化。

### PlayerRespawnEvent {#playerrespawnevent}

触发时机：玩家复活时触发该事件。

信号：[world.afterEvents.playerRespawn](events/afterEvents.md#playerRespawn)。分类：玩家。

参数类型：[WorldPlayerRespawnAfterEvent](reference/WorldPlayerRespawnAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PlayerRespawnEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `id` | [str](../common/type-system.md#str) | 只读 | 玩家id |

**原生前提与限制：**

- 该事件为玩家点击重生按钮时触发，但是触发时玩家可能尚未完成复活，此时请勿对玩家进行切维度或设置生命值等操作
    一般情况下推荐使用[PlayerRespawnFinishServerEvent](native-events.md#playerrespawnfinishserverevent)

### PlayerRespawnFinishServerEvent {#playerrespawnfinishserverevent}

触发时机：玩家复活完毕时触发

信号：`world.afterEvents.getNativeEvent('PlayerRespawnFinishServerEvent')`。分类：玩家。

参数类型：[WorldPlayerRespawnFinishAfterEvent](reference/WorldPlayerRespawnFinishAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PlayerRespawnFinishServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |

**原生前提与限制：**

- 该事件触发时玩家已重生完毕，可以安全使用切维度等操作
  - 通过末地传送门回到主世界时也算重生，同样也会触发该事件

### PlayerSleepServerEvent {#playersleepserverevent}

玩家使用床睡觉成功

信号：[world.afterEvents.playerSleep](events/afterEvents.md#playerSleep)。分类：玩家。

参数类型：[WorldPlayerSleepAfterEvent](reference/WorldPlayerSleepAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PlayerSleepServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |

### PlayerSpinAttackServerEvent {#playerspinattackserverevent}

触发时机：玩家开始/结束快速旋转攻击时触发

信号：[world.afterEvents.playerSpinAttack](events/afterEvents.md#playerSpinAttack)。分类：玩家。

参数类型：[WorldPlayerSpinAttackAfterEvent](reference/WorldPlayerSpinAttackAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PlayerSpinAttackServerEvent")`。

:::warning 平台条件
此事件仅在 Apollo 环境中提供；普通联机/单机不会因此得到同等能力。
:::

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家的entityId |
| `isInWaterOrRain` | `isInWaterOrRain` | [bool](../common/type-system.md#bool) | 只读 | 是否在水中或雨中 |
| `isRiding` | `isRiding` | [bool](../common/type-system.md#bool) | 只读 | 是否骑乘状态 |
| `isStart` | `isStart` | [bool](../common/type-system.md#bool) | 只读 | True时代表开始快速旋转攻击；False时代表结束快速旋转攻击 |

### PlayerStopSleepServerEvent {#playerstopsleepserverevent}

玩家停止睡觉

信号：[world.afterEvents.playerStopSleep](events/afterEvents.md#playerStopSleep)。分类：玩家。

参数类型：[WorldPlayerStopSleepAfterEvent](reference/WorldPlayerStopSleepAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PlayerStopSleepServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |

### PlayerTeleportEvent {#playerteleportevent}

触发时机：当玩家传送时触发该事件，如：玩家使用末影珍珠或tp指令时。

信号：[world.afterEvents.playerTeleport](events/afterEvents.md#playerTeleport)。分类：玩家。

参数类型：[WorldPlayerTeleportAfterEvent](reference/WorldPlayerTeleportAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("PlayerTeleportEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `id` | [str](../common/type-system.md#str) | 只读 | 玩家id |

### ProjectileCritHitEvent {#projectilecrithitevent}

触发时机：当抛射物与头部碰撞时触发该事件。注：需调用OpenPlayerCritBox开启玩家爆头后才能触发。

信号：[world.afterEvents.projectileCritHit](events/afterEvents.md#projectileCritHit)。分类：实体。

参数类型：[WorldProjectileCritHitAfterEvent](reference/WorldProjectileCritHitAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("ProjectileCritHitEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 抛射物id |
| `target` | `targetId` | [str](../common/type-system.md#str) | 只读 | 碰撞目标id |

### OnRainLevelChangeServerEvent {#onrainlevelchangeserverevent}

下雨强度发生改变

信号：`world.afterEvents.getNativeEvent('OnRainLevelChangeServerEvent')`。分类：世界。

参数类型：[WorldRainLevelChangeAfterEvent](reference/WorldRainLevelChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnRainLevelChangeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `oldLevel` | `oldLevel` | [float](../common/type-system.md#float) | 只读 | 改变前的下雨强度 |
| `newLevel` | `newLevel` | [float](../common/type-system.md#float) | 只读 | 改变后的下雨强度 |

### LoadServerAddonScriptsAfter {#loadserveraddonscriptsafter}

服务器加载完mod时触发

信号：[world.afterEvents.scriptsLoad](events/afterEvents.md#scriptsLoad)。分类：世界。

参数类型：[WorldScriptsLoadAfterEvent](reference/WorldScriptsLoadAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("LoadServerAddonScriptsAfter")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### SpawnProjectileServerEvent {#spawnprojectileserverevent}

触发时机：抛射物生成时触发

信号：[world.afterEvents.spawnProjectile](events/afterEvents.md#spawnProjectile)。分类：实体。

参数类型：[WorldSpawnProjectileAfterEvent](reference/WorldSpawnProjectileAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("SpawnProjectileServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `projectile` | `projectileId` | [str](../common/type-system.md#str) | 只读 | 抛射物的实体id |
| `projectileIdentifier` | `projectileIdentifier` | [str](../common/type-system.md#str) | 只读 | 抛射物的identifier |
| `source` | `spawnerId` | [str](../common/type-system.md#str) | 只读 | 发射者的实体id，没有发射者时为-1 |

**原生前提与限制：**

- 该事件里无法获取弹射物实体的auxvalue。如有需要可以延迟一帧获取，或者在ProjectileDoHitEffectEvent获取

### StepOffBlockServerEvent {#stepoffblockserverevent}

触发时机：实体移动离开一个实心方块时触发

信号：[world.afterEvents.stepOffBlock](events/afterEvents.md#stepOffBlock)。分类：方块。

参数类型：[WorldStepOffBlockAfterEvent](reference/WorldStepOffBlockAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("StepOffBlockServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 触发的entity的唯一ID |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |

**原生前提与限制：**

- 不是所有方块都会触发该事件，自定义方块需要在json中先配置触发开关（详情参考：自定义方块JSON组件），
    原版方块需要先通过RegisterOnStepOff接口注册才能触发
  - 压力板与绊线钩这种非实心方块不会触发

### StoreBuySuccServerEvent {#storebuysuccserverevent}

触发时机:玩家游戏内购买商品时服务端抛出的事件

信号：[world.afterEvents.storeBuySucc](events/afterEvents.md#storeBuySucc)。分类：玩家。

参数类型：[WorldStoreBuySuccAfterEvent](reference/WorldStoreBuySuccAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("StoreBuySuccServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 购买商品的玩家实体id |

### OnScriptTickServer {#onscripttickserver}

服务器tick时触发,1秒有30个tick

信号：[world.afterEvents.tick](events/afterEvents.md#tick)。分类：世界。

参数类型：[WorldTickAfterEvent](reference/WorldTickAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("OnScriptTickServer")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### UIContainerItemChangedServerEvent {#uicontaineritemchangedserverevent}

合成容器物品发生变化时触发

信号：[world.afterEvents.uiContainerItemChange](events/afterEvents.md#uiContainerItemChange)。分类：物品。

参数类型：[WorldUiContainerItemChangeAfterEvent](reference/WorldUiContainerItemChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("UIContainerItemChangedServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `slot` | `slot` | [int](../common/type-system.md#int) | 只读 | 容器槽位，含义见：容器类型枚举 |
| `oldItemDict` | `oldItemDict` | [dict](../common/type-system.md#dict) | 只读 | 旧物品，格式参考物品信息字典 |
| `newItemDict` | `newItemDict` | [dict](../common/type-system.md#dict) | 只读 | 生成的物品，格式参考物品信息字典 |

**原生前提与限制：**

- 合成容器包括工作台、铁砧、附魔台、织布机、砂轮、切石机、制图台、锻造台，输入物品发生变化时会触发本事件
  - 可通过容器槽位区分不同的生成容器类型
  - 合成容器的生成槽位生成物品时不触发本事件，生成物品可通过CraftItemOutputChangeServerEvent监听
  - 储物容器(箱子，潜影箱)，熔炉，酿造台，发射器，投掷器，漏斗，炼药锅，唱片机，高炉，烟熏炉中物品发生变化不会触发此事件，此类容器可通过ContainerItemChangedServerEvent监听

### UrgeShipEvent {#urgeshipevent}

玩家点击商城催促发货按钮时触发该事件

信号：[world.afterEvents.urgeShip](events/afterEvents.md#urgeShip)。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[WorldUrgeShipAfterEvent](reference/WorldUrgeShipAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("UrgeShipEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |

### WalkAnimBeginServerEvent {#walkanimbeginserverevent}

当走路动作开始时触发

信号：[world.afterEvents.walkAnimBegin](events/afterEvents.md#walkAnimBegin)。分类：模型。

参数类型：[WorldWalkAnimBeginAfterEvent](reference/WorldWalkAnimBeginAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("WalkAnimBeginServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |

**原生前提与限制：**

- 使用SetModel替换骨骼模型后，该事件才生效

### WalkAnimEndServerEvent {#walkanimendserverevent}

当走路动作结束时触发

信号：[world.afterEvents.walkAnimEnd](events/afterEvents.md#walkAnimEnd)。分类：模型。

参数类型：[WorldWalkAnimEndAfterEvent](reference/WorldWalkAnimEndAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.afterEvents.getNativeEvent("WalkAnimEndServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |

**原生前提与限制：**

- 使用SetModel替换骨骼模型后，该事件才生效

### ActorUseItemServerEvent {#actoruseitemserverevent}

触发时机：玩家使用物品生效之前服务端抛出的事件（比较特殊不走该事件的例子：1）染料对有水的炼药锅使用；2）盔甲架装备盔甲）

信号：[world.beforeEvents.actorUseItem](events/beforeEvents.md#actorUseItem)。分类：物品。

参数类型：[WorldActorUseItemBeforeEvent](reference/WorldActorUseItemBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ActorUseItemServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 使用的物品的物品信息字典 |
| `useMethod` | `useMethod` | [int](../common/type-system.md#int) | 只读 | 使用物品的方法，详见ItemUseMethodEnum枚举 |

**原生前提与限制：**

- 注意，喝牛奶会触发该事件，但是不会触发[ActorUseItemClientEvent](../client/events.md#actoruseitemclientevent)

### ActuallyHurtServerEvent {#actuallyhurtserverevent}

实体实际受到伤害时触发，相比于[DamageEvent](native-events.md#damageevent)，该伤害为经过护甲及buff计算后，实际的扣血量

信号：[world.beforeEvents.actuallyHurt](events/beforeEvents.md#actuallyHurt)。分类：实体。

参数类型：[WorldActuallyHurtBeforeEvent](reference/WorldActuallyHurtBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ActuallyHurtServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `source` | `srcId` | [str](../common/type-system.md#str) | 只读 | 伤害源id |
| `projectile` | `projectileId` | [str](../common/type-system.md#str) | 只读 | 投射物id |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 被伤害id |
| `damage` | `damage` | [float](../common/type-system.md#float) | 同步回调中 | 伤害值（被伤害吸收后的值），允许修改，设置为0则此次造成的伤害为0，若设置数值和原来一样则视为没有修改 |
| `invulnerableTime` | `invulnerableTime` | [int](../common/type-system.md#int) | 只读 | 实体受击后，剩余的无懈可击帧数，在无懈可击时间内，damage和damage_f为超过上次伤害的部分 |
| `lastHurt` | `lastHurt` | [float](../common/type-system.md#float) | 只读 | 实体上次受到的伤害 |
| `cause` | `cause` | [str](../common/type-system.md#str) | 只读 | 伤害来源，详见Minecraft枚举值文档的ActorDamageCause |
| `customTag` | `customTag` | [str](../common/type-system.md#str) | 只读 | 使用Hurt接口传入的自定义伤害类型 |

**原生前提与限制：**

- 药水与状态效果造成的伤害不触发，可以使用[ActorHurtServerEvent](native-events.md#actorhurtserverevent)
  - 为了游戏运行效率请尽可能避免将火的伤害设置为0，因为这样会导致大量触发该事件。
  - 若要修改damage的值，请确保修改后的值与原值不同，且支持转换为浮点型，否则引擎会忽略这次修改。
  - 青蛙、山羊跳跃落地时也会触发此伤害事件，但它们的掉落伤害实际会有减免，青蛙减少5，山羊减少10
  - 在无懈可击时间内，只要实体受到高于上次受击的伤害，可以连续触发不受SetHurtCD影响，如实体连续受到1伤害，如果在本事件中修改damage为0.5，则引擎会认为每次都有0.5的溢出伤害，可以通过invulnerableTime和lastHurt来判断是否取消这次伤害

### BlockLiquidStateChangeServerEvent {#blockliquidstatechangeserverevent}

触发时机：方块转为含水或者脱离含水(流体)前触发

信号：[world.beforeEvents.blockLiquidStateChange](events/beforeEvents.md#blockLiquidStateChange)。分类：方块。

参数类型：[WorldBlockLiquidStateChangeBeforeEvent](reference/WorldBlockLiquidStateChangeBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("BlockLiquidStateChangeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxValue` | `auxValue` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 方块维度 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `turnLiquid` | `turnLiquid` | [bool](../common/type-system.md#bool) | 只读 | 是否转为含水，true则转为含水，false则脱离含水 |

### ServerPreBlockPatternEvent {#serverpreblockpatternevent}

触发时机：用方块组合生成生物，在放置最后一个组成方块时触发该事件。

信号：[world.beforeEvents.blockPattern](events/beforeEvents.md#blockPattern)。分类：世界。

参数类型：[WorldBlockPatternBeforeEvent](reference/WorldBlockPatternBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ServerPreBlockPatternEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `enable` | `enable` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否允许继续生成。若设为False，可阻止生成生物 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `entityWillBeGenerated` | `entityWillBeGenerated` | [str](../common/type-system.md#str) | 只读 | 即将生成生物的名字，如"minecraft:pig" |

取消映射：`event.cancel = True` 等价于 `event.enable = False`。只影响该原生动作。

### BlockSnowStateChangeServerEvent {#blocksnowstatechangeserverevent}

触发时机：方块转为含雪或者脱离含雪前触发

信号：[world.beforeEvents.blockSnowStateChange](events/beforeEvents.md#blockSnowStateChange)。分类：方块。

参数类型：[WorldBlockSnowStateChangeBeforeEvent](reference/WorldBlockSnowStateChangeBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("BlockSnowStateChangeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 方块维度 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `turnSnow` | `turnSnow` | [bool](../common/type-system.md#bool) | 只读 | 是否转为含雪，true则转为含雪，false则脱离含雪 |
| `setBlockType` | `setBlockType` | [int](../common/type-system.md#int) | 只读 | 方块进入脱离含雪的原因，参考SetBlockType |

### ServerBlockUseEvent {#serverblockuseevent}

触发时机：玩家右键点击新版自定义方块（或者通过接口AddBlockItemListenForUseEvent增加监听的MC原生游戏方块）时服务端抛出该事件（该事件tick执行，需要注意效率问题）。

信号：`world.beforeEvents.getNativeEvent('ServerBlockUseEvent')`。分类：方块。

参数类型：[WorldBlockUseBeforeEvent](reference/WorldBlockUseBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ServerBlockUseEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家Id |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `aux` | `aux` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True可拦截与方块交互的逻辑。 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `clickX` | `clickX` | [float](../common/type-system.md#float) | 只读 | 点击点的x比例位置 |
| `clickY` | `clickY` | [float](../common/type-system.md#float) | 只读 | 点击点的y比例位置 |
| `clickZ` | `clickZ` | [float](../common/type-system.md#float) | 只读 | 点击点的z比例位置 |
| `face` | `face` | [int](../common/type-system.md#int) | 只读 | 点击方块的面，参考Facing枚举 |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 使用的物品的物品信息字典 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |

**原生前提与限制：**

- 客户端对应事件ClientBlockUseEvent如果开启拦截开关，则服务端也不会收到对应事件，即ServerBlockUseEvent不会触发。
  - 当对原生方块进行使用时，如堆肥桶等类似有 使用 功能的方块使用物品时，会触发该事件，而ServerItemUseOnEvent则不会被触发。对应的客户端事件同理。
  - 部分工具对方块的使用效果，如锹犁地，不一定能通过该事件cancel，还需同时使用ItemUseOnServerEvent进行取消
    目前已知有：
    锹犁地相关的方块：草地、泥土、砂土、菌丝体、灰化土、缠根泥土，均需同时通过ServerBlockUseEvent和ItemUseOnServerEvent进行取消

### ChangeLevelUpCostServerEvent {#changelevelupcostserverevent}

触发时机：获取玩家下一个等级升级经验时，用于重载玩家的升级经验，每个等级在重置之前都只会触发一次

信号：[world.beforeEvents.changeLevelUpCost](events/beforeEvents.md#changeLevelUpCost)。分类：玩家。

参数类型：[WorldChangeLevelUpCostBeforeEvent](reference/WorldChangeLevelUpCostBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ChangeLevelUpCostServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `level` | `level` | [int](../common/type-system.md#int) | 只读 | 玩家当前等级 |
| `levelUpCostExp` | `levelUpCostExp` | [int](../common/type-system.md#int) | 同步回调中 | 当前等级升级到下个等级需要的经验值，当设置升级经验小于1时会被强制调整到1 |
| `changed` | `changed` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True，重载玩家升级经验才会生效 |

### ChestBlockTryPairWithServerEvent {#chestblocktrypairwithserverevent}

触发时机：两个并排的小箱子方块准备组合为一个大箱子方块时

信号：[world.beforeEvents.chestBlockTryPairWith](events/beforeEvents.md#chestBlockTryPairWith)。分类：方块。

参数类型：[WorldChestBlockTryPairWithBeforeEvent](reference/WorldChestBlockTryPairWithBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ChestBlockTryPairWithServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否允许触发，默认为False，若设为True，可阻止小箱子组合成为一个大箱子 |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 小箱子方块x坐标 |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 小箱子方块y坐标 |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 小箱子方块z坐标 |
| `otherBlockX` | `otherBlockX` | [int](../common/type-system.md#int) | 只读 | 将要与之组合的另外一个小箱子方块x坐标 |
| `otherBlockY` | `otherBlockY` | [int](../common/type-system.md#int) | 只读 | 将要与之组合的另外一个小箱子方块y坐标 |
| `otherBlockZ` | `otherBlockZ` | [int](../common/type-system.md#int) | 只读 | 将要与之组合的另外一个小箱子方块z坐标 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |

### ChunkAcquireDiscardedServerEvent {#chunkacquirediscardedserverevent}

服务端区块即将被卸载时触发

信号：[world.beforeEvents.chunkUnload](events/beforeEvents.md#chunkUnload)。分类：世界。

参数类型：[WorldChunkUnloadBeforeEvent](reference/WorldChunkUnloadBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ChunkAcquireDiscardedServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 区块所在维度 |
| `chunkPosX` | `chunkPosX` | [int](../common/type-system.md#int) | 只读 | 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15] |
| `chunkPosZ` | `chunkPosZ` | [int](../common/type-system.md#int) | 只读 | 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15] |
| `entities` | `entities` | [list](../common/type-system.md#list)([str](../common/type-system.md#str)) | 只读 | 随区块卸载而从世界移除的实体id的列表。注意事件触发时已经无法获取到这些实体的信息，仅供脚本资源回收用。 |
| `blockEntities` | `blockEntities` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 只读 | 随区块卸载而从世界移除的自定义方块实体的坐标的列表，列表元素dict包含posX，posY，posZ三个int表示自定义方块实体的坐标，blockName表示方块的identifier，包含命名空间及名称。注意事件触发时已经无法获取到这些方块实体的信息，仅供脚本资源回收用。 |

**原生前提与限制：**

- 区块卸载：游戏只会加载玩家周围的区块，玩家移动到别的区域时，原来所在区域的区块会被卸载，参考[区块介绍 （在新窗口打开）](https://zh.minecraft.wiki/w/%E5%8C%BA%E5%9D%97)

### CommandEvent {#commandevent}

玩家请求执行指令时触发

信号：[world.beforeEvents.command](events/beforeEvents.md#command)。分类：世界。

参数类型：[WorldCommandBeforeEvent](reference/WorldCommandBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("CommandEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 玩家ID |
| `command` | `command` | [str](../common/type-system.md#str) | 只读 | 指令字符串 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消 |

**原生前提与限制：**

- 该事件是玩家请求执行指令时触发的Hook，该事件不响应命令方块的指令和通过modSDK调用的指令，阻止玩家的该条指令只需要将cancel设置为True

### CommandBlockContainerOpenEvent {#commandblockcontaineropenevent}

触发时机：玩家点击命令方块，尝试打开命令方块的设置界面

信号：[world.beforeEvents.commandBlockContainerOpen](events/beforeEvents.md#commandBlockContainerOpen)。分类：方块。

参数类型：[WorldCommandBlockContainerOpenBeforeEvent](reference/WorldCommandBlockContainerOpenBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("CommandBlockContainerOpenEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `isBlock` | `isBlock` | [bool](../common/type-system.md#bool) | 只读 | 是否以方块坐标的形式定位命令方块，当为True时下述的blockX/blockY/blockZ有意义，当为False时，下述的victimId有意义 |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 命令方块位置x，当isBlock为True时有效 |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 命令方块位置y，当isBlock为True时有效 |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 命令方块位置z，当isBlock为True时有效 |
| `target` | `victimId` | [str](../common/type-system.md#str) | 只读 | 命令方块对应的逻辑实体的唯一id，当isBlock为False时有效 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 修改为True时，可以阻止玩家打开命令方块的设置界面 |

### CommandBlockUpdateEvent {#commandblockupdateevent}

触发时机：玩家尝试修改命令方块的内置命令时

信号：[world.beforeEvents.commandBlockUpdate](events/beforeEvents.md#commandBlockUpdate)。分类：方块。

参数类型：[WorldCommandBlockUpdateBeforeEvent](reference/WorldCommandBlockUpdateBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("CommandBlockUpdateEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `playerUid` | `playerUid` | [int](../common/type-system.md#int)/[long](../common/type-system.md#long) | 只读 | 玩家的uid |
| `command` | `command` | [str](../common/type-system.md#str) | 只读 | 企图修改的命令方块中的命令内容字符串 |
| `isBlock` | `isBlock` | [bool](../common/type-system.md#bool) | 只读 | 是否以方块坐标的形式定位命令方块，当为True时下述的blockX/blockY/blockZ有意义，当为False时，下述的victimId有意义 |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 命令方块位置x，当isBlock为True时有效 |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 命令方块位置y，当isBlock为True时有效 |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 命令方块位置z，当isBlock为True时有效 |
| `target` | `victimId` | [str](../common/type-system.md#str) | 只读 | 命令方块对应的逻辑实体的唯一id，当isBlock为False时有效 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 修改为True时，可以阻止玩家修改命令方块的内置命令 |

**原生前提与限制：**

- 当修改的目标为命令方块矿车时（此时isBlock为False），设置cancel为True，依旧可以阻止修改命令方块矿车的内部指令，但是从客户端能够看到命令方块矿车的内部指令变化了，不过这仅仅是假象，重新登录或者其他客户端打开命令方块矿车的设置界面，就会发现其实内部指令没有变化

### OnContainerFillLoottableServerEvent {#oncontainerfillloottableserverevent}

触发时机：随机奖励箱第一次打开根据loottable生成物品时

信号：`world.beforeEvents.getNativeEvent('OnContainerFillLoottableServerEvent')`。分类：世界。

参数类型：[WorldContainerLootBeforeEvent](reference/WorldContainerLootBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("OnContainerFillLoottableServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `loottable` | `loottable` | [str](../common/type-system.md#str) | 只读 | 奖励箱子所读取的loottable的json路径 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 打开奖励箱子的玩家的playerId |
| `itemList` | `itemList` | [list](../common/type-system.md#list) | 同步回调中 | 掉落物品列表，每个元素为一个itemDict，格式可参考物品信息字典 |
| `dirty` | `dirty` | [bool](../common/type-system.md#bool) | 同步回调中 | 默认为False，如果需要修改掉落列表需将该值设为True |

**原生前提与限制：**

- 只有当dirty为True时才会重新读取item列表并生成对应的掉落物，如果不需要修改掉落结果的话请勿随意修改dirty值
  - 可疑的沙子也具有奖励箱性质，使用刷子刷可疑的沙子也会触发该事件

### CraftItemOutputChangeServerEvent {#craftitemoutputchangeserverevent}

玩家从容器拿出生成物品时触发

信号：[world.beforeEvents.craftItemOutputChange](events/beforeEvents.md#craftItemOutputChange)。分类：物品。

参数类型：[WorldCraftItemOutputChangeBeforeEvent](reference/WorldCraftItemOutputChangeBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("CraftItemOutputChangeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 生成的物品，格式参考物品信息字典 |
| `screenContainerType` | `screenContainerType` | [int](../common/type-system.md#int) | 只读 | 当前界面类型,类型含义见：容器类型枚举 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消生成物品 |

**原生前提与限制：**

- 支持工作台，铁砧，砂轮等工作方块
  - screenContainerType = serverApi.GetMinecraftEnum().ContainerType.INVENTORY时，表示从创造模式物品栏中拿出物品，或者从合成栏中拿出合成物品
  - 通过cancel参数取消生成物品，可用于禁止外挂刷物品
  - cancel=True时无法从创造模式物品栏拿物品
  - cancel=True时铁砧无法修复或重命名物品，但仍会扣除经验值

### CustomCommandTriggerServerEvent {#customcommandtriggerserverevent}

自定义命令触发事件

信号：[world.beforeEvents.customCommandTrigger](events/beforeEvents.md#customCommandTrigger)。分类：世界。

参数类型：[WorldCustomCommandTriggerBeforeEvent](reference/WorldCustomCommandTriggerBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("CustomCommandTriggerServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `command` | `command` | [str](../common/type-system.md#str) | 只读 | 自定义命令名称，对应json中的name字段 |
| `args` | `args` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 只读 | 自定义命令参数，详情见下方 |
| `variant` | `variant` | [int](../common/type-system.md#int) | 只读 | 表示是哪条变体，范围`[0, 9]`，对应json中args键中的数字，未配置变体则为0 |
| `origin` | `origin` | [dict](../common/type-system.md#dict) | 只读 | 触发源的信息，详情见下方 |
| `return_failed` | `return_failed` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置自定义命令是否执行失败，默认为False，如果执行失败，返回信息以红色字体显示 |
| `return_msg_key` | `return_msg_key` | [str](../common/type-system.md#str) | 同步回调中 | 设置返回给玩家或命令方块的信息，也支持通过语言文件(.lang)定义，默认值为commands.custom.success(自定义命令执行成功) |

**原生前提与限制：**

- origin参数说明如下

| 键 | 类型 | 解释 |
| --- | --- | --- |
| entityId | [str](../common/type-system.md#str) | 触发指令的实体id，**若由命令方块触发，则不会含有此字段** |
| dimension | [int](../common/type-system.md#int) | 指令触发的维度id，0-主世界; 1-下界; 2-末地; 或其他自定义维度 |
| blockPos | [tuple](../common/type-system.md#tuple) | 触发指令的实体或命令方块的整数坐标 |

- 自定义命令参数中的dict说明如下

| 键 | 类型 | 解释 |
| --- | --- | --- |
| name | [str](../common/type-system.md#str) | 参数名称，对应json中的name字段 |
| [type](../common/type-system.md#type) | [str](../common/type-system.md#str) | 参数类型，对应json中的type字段 |
| value | [any](../common/type-system.md#any) | 参数的值，若玩家没传，则采用json中填写的default的值，但会转为python变量格式。如null转为None，array转为tuple |

- 对于玩家传入的参数，type不同则对应的value也不同，type对应value的类型和具体数据格式如下

| [type](../common/type-system.md#type) | value类型 | 解释 |
| --- | --- | --- |
| [int](../common/type-system.md#int) | [int](../common/type-system.md#int) | 整数，如114 |
| [float](../common/type-system.md#float) | [float](../common/type-system.md#float) | 浮点数，如5.14 |
| [bool](../common/type-system.md#bool) | [bool](../common/type-system.md#bool) | 布尔值，如True |
| [str](../common/type-system.md#str) | [str](../common/type-system.md#str) | 字符串，如'niganma' |
| enum | [str](../common/type-system.md#str) | 开发者在json中指定的某个字符串 |
| enum_short | [str](../common/type-system.md#str) | 开发者在json中指定的某个字符串 |
| block | [str](../common/type-system.md#str) | 方块的identifier，如'minecraft:grass' |
| item | [dict](../common/type-system.md#dict) | 含有物品名称，如&#123;'itemName': 'minecraft:apple'&#125; |
| pos | [tuple](../common/type-system.md#tuple) | 含有三个float的坐标，如(-0.93, 81.25, -5.67) |
| target | [tuple](../common/type-system.md#tuple) | 含有对应的所有目标entityId，如('-139816907912', '-263852559602') |
| entity | [dict](../common/type-system.md#dict) | 含有实体名称，如&#123;'entityType': 'minecraft:cow'&#125; |
| effect | [dict](../common/type-system.md#dict) | 含有状态效果名称和对应的EffectType枚举，如&#123;'name': 'absorption', 'id': 22&#125; |
| dimension | [dict](../common/type-system.md#dict) | 含有维度名称和对应数字id，如&#123;'name': 'nether', 'id': 1&#125; |
| biome | [dict](../common/type-system.md#dict) | 含有生物群系名称和对应的BiomeType枚举，如&#123;'name': 'bamboo_jungle', 'biomeType': 48&#125; |
| structure | [dict](../common/type-system.md#dict) | 含有结构名称和对应的StructureFeatureType枚举，如&#123;'name': 'ancient_city', 'structureType': 15&#125; |
| enchant | [dict](../common/type-system.md#dict) | 含有附魔名称和对应的EnchantType枚举，如&#123;'identifier': 'knockback', '[type](../common/type-system.md#type)': 12&#125; |

### DamageEvent {#damageevent}

实体受到伤害时触发

信号：`world.beforeEvents.getNativeEvent('DamageEvent')`。分类：实体。

参数类型：[WorldDamageBeforeEvent](reference/WorldDamageBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("DamageEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `source` | `srcId` | [str](../common/type-system.md#str) | 只读 | 伤害源id |
| `projectile` | `projectileId` | [str](../common/type-system.md#str) | 只读 | 投射物id |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 被伤害id |
| `damage` | `damage` | [float](../common/type-system.md#float) | 同步回调中 | 伤害值（被伤害吸收前的值），允许修改，设置为0则此次造成的伤害为0 |
| `absorption` | `absorption` | [int](../common/type-system.md#int) | 只读 | 受到伤害时，扣除黄心前，实体拥有的黄心血量（见AttrType枚举的ABSORPTION） |
| `cause` | `cause` | [str](../common/type-system.md#str) | 只读 | 伤害来源，详见Minecraft枚举值文档的ActorDamageCause |
| `knock` | `knock` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否击退被攻击者，允许修改，设置该值为False则不产生击退 |
| `ignite` | `ignite` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否点燃被伤害者，允许修改，设置该值为True产生点燃效果 |
| `customTag` | `customTag` | [str](../common/type-system.md#str) | 只读 | 使用Hurt接口传入的自定义伤害类型 |

**原生前提与限制：**

- damage值会被护甲和absorption等吸收，不一定是最终扣血量。通过设置这个伤害值可以取消伤害，但不会取消由击退效果或者点燃效果带来的伤害
  - 该事件在实体受伤之前触发，由于部分伤害是在tick中处理，因此持续触发受伤时（如站在火中）会每帧触发事件（可以使用ActorHurtServerEvent来避免）。
  - 这里的damage是伤害源具有的攻击伤害值，并非实体真实的扣血量，如果需要获取真实伤害，可以使用ActuallyHurtServerEvent事件。
  - 当目标无法被击退时，knock值无效
  - 药水与状态效果造成的伤害不触发，可以使用[ActorHurtServerEvent](native-events.md#actorhurtserverevent)
  - 由于点燃的实现原因，此处ignite设置为false并不能取消实体的点燃效果（如果需要取消点燃效果，请通过OnFireHurtEvent事件实现）
  - 青蛙、山羊跳跃落地时也会触发此伤害事件，但它们的掉落伤害实际会有减免，青蛙减少5，山羊减少10

### WillAddEffectServerEvent {#willaddeffectserverevent}

触发时机：实体即将获得状态效果前

信号：[world.beforeEvents.effectAdd](events/beforeEvents.md#effectAdd)。分类：实体。

参数类型：[WorldEffectAddBeforeEvent](reference/WorldEffectAddBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("WillAddEffectServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `effectName` | `effectName` | [str](../common/type-system.md#str) | 只读 | 实体获得状态效果的名字 |
| `effectDuration` | `effectDuration` | [int](../common/type-system.md#int) | 只读 | 状态效果的持续时间，单位秒 |
| `effectAmplifier` | `effectAmplifier` | [int](../common/type-system.md#int) | 只读 | 状态效果的放大倍数 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True可以取消 |
| `damage` | `damage` | [float](../common/type-system.md#float) | 只读 | 状态将会造成的伤害值，如药水；需要注意，该值不一定是最终的伤害值，例如被伤害吸收效果扣除。只有持续时间为0时有用 |

### HealthChangeBeforeServerEvent {#healthchangebeforeserverevent}

生物生命值或最大生命值发生变化之前触发

信号：[world.beforeEvents.entityHealthChanged](events/beforeEvents.md#entityHealthChanged)。分类：实体。

参数类型：[WorldEntityHealthChangedBeforeEvent](reference/WorldEntityHealthChangedBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("HealthChangeBeforeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `fromValue` | `from` | [float](../common/type-system.md#float) | 只读 | 变化前的生命值 |
| `to` | `to` | [float](../common/type-system.md#float) | 只读 | 将要变化到的生命值，cancel设置为True时可以取消该变化，但是此参数不变 |
| `byScript` | `byScript` | [bool](../common/type-system.md#bool) | 只读 | 是否通过SetAttrValue或SetAttrMaxValue调用产生的变化 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消该变化 |

### OnEntityInsideBlockServerEvent {#onentityinsideblockserverevent}

触发时机：当实体碰撞盒所在区域有方块时，服务端持续触发

信号：[world.beforeEvents.entityInsideBlock](events/beforeEvents.md#entityInsideBlock)。分类：方块。

参数类型：[WorldEntityInsideBlockBeforeEvent](reference/WorldEntityInsideBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("OnEntityInsideBlockServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `slowdownMultiX` | `slowdownMultiX` | [float](../common/type-system.md#float) | 同步回调中 | 实体移速X方向的减速比例，可在脚本层被修改 |
| `slowdownMultiY` | `slowdownMultiY` | [float](../common/type-system.md#float) | 同步回调中 | 实体移速Y方向的减速比例，可在脚本层被修改 |
| `slowdownMultiZ` | `slowdownMultiZ` | [float](../common/type-system.md#float) | 同步回调中 | 实体移速Z方向的减速比例，可在脚本层被修改 |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 方块位置x |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 方块位置y |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 方块位置z |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 可由脚本层回传True给引擎，阻止触发后续原版逻辑 |

**原生前提与限制：**

- 不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义方块JSON组件）
    ，原版方块需要先通过RegisterOnEntityInside接口注册才能触发
  - 如果需要修改slowdownMulti/cancel，强烈建议与客户端事件同步修改，避免出现客户端表现不一致等非预期现象。
  - 如果要在脚本层修改slowdownMulti，回传的一定要是浮点型，例如需要赋值1.0而不是1
  - 有任意slowdownMulti参数被传回非0值时生效减速比例
  - slowdownMulti参数更像是一个Buff，例如并不是立刻计算，而是先保存在实体属性里延后计算、在已经有slowdownMulti属性的情况下会取最低的值、免疫掉落伤害等，与原版蜘蛛网逻辑基本一致。

### EntityDieLoottableServerEvent {#entitydieloottableserverevent}

触发时机：生物死亡掉落物品时

信号：`world.beforeEvents.getNativeEvent('EntityDieLoottableServerEvent')`。分类：实体。

参数类型：[WorldEntityLootBeforeEvent](reference/WorldEntityLootBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("EntityDieLoottableServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `deadEntity` | `dieEntityId` | [str](../common/type-system.md#str) | 只读 | 死亡实体的entityId |
| `attacker` | `attacker` | [str](../common/type-system.md#str) | 只读 | 伤害来源的entityId |
| `itemList` | `itemList` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 同步回调中 | 掉落物品列表，每个元素为一个itemDict，格式可参考物品信息字典 |
| `dirty` | `dirty` | [bool](../common/type-system.md#bool) | 同步回调中 | 默认为False，如果需要修改掉落列表需将该值设为True |

**原生前提与限制：**

- 只有当dirty为True时才会重新读取item列表并生成对应的掉落物，如果不需要修改掉落结果的话请勿随意修改dirty值
  - 该事件在生物死亡后会触发，无论是否掉落物品，因此掉落物品列表可能存在为空的情况
  - 掉落物不包含玩家或生物携带以及背包内的物品，若要获取死亡后由背包扔出的物品请参考EntityDroppedItemServerEvent事件

### EntityMotionStopServerEvent {#entitymotionstopserverevent}

实体运动器停止事件。实体（包含玩家）添加运动器并开始运行后，运动器自动停止时触发

信号：[world.beforeEvents.entityMotionStop](events/beforeEvents.md#entityMotionStop)。分类：实体。

参数类型：[WorldEntityMotionStopBeforeEvent](reference/WorldEntityMotionStopBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("EntityMotionStopServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `motionId` | `motionId` | [int](../common/type-system.md#int) | 只读 | 运动器id |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `remove` | `remove` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否移除该运动器，设置为False则保留，默认为True，即运动器停止后自动移除，该参数设置只对非玩家实体有效 |

**原生前提与限制：**

- 注意：该事件触发表示运动器播放顺利完成，手动调用的StopEntityMotion、RemoveEntityMotion以及实体被销毁导致的运动器停止不会触发该事件。

### ServerEntityTryPlaceBlockEvent {#serverentitytryplaceblockevent}

触发时机：当生物试图放置方块时触发该事件。

信号：[world.beforeEvents.entityPlaceBlock](events/beforeEvents.md#entityPlaceBlock)。分类：方块。

参数类型：[WorldEntityPlaceBlockBeforeEvent](reference/WorldEntityPlaceBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ServerEntityTryPlaceBlockEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `x` | `x` | [int](../common/type-system.md#int) | 同步回调中 | 方块x坐标,支持修改 |
| `y` | `y` | [int](../common/type-system.md#int) | 同步回调中 | 方块y坐标,支持修改 |
| `z` | `z` | [int](../common/type-system.md#int) | 同步回调中 | 方块z坐标,支持修改 |
| `fullName` | `fullName` | [str](../common/type-system.md#str) | 同步回调中 | 方块的identifier，包含命名空间及名称,支持修改 |
| `auxData` | `auxData` | [int](../common/type-system.md#int) | 同步回调中 | 方块附加值,支持修改 |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 试图放置方块的生物ID |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `face` | `face` | [int](../common/type-system.md#int) | 只读 | 点击方块的面，参考Facing枚举 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 默认为False，在脚本层设置为True就能取消该方块的放置 |
| `clickX` | `clickX` | [float](../common/type-system.md#float) | 只读 | 点击点的x比例位置 |
| `clickY` | `clickY` | [float](../common/type-system.md#float) | 只读 | 点击点的y比例位置 |
| `clickZ` | `clickZ` | [float](../common/type-system.md#float) | 只读 | 点击点的z比例位置 |

**原生前提与限制：**

- 部分放置后会产生实体的方块、可操作的方块、带有特殊逻辑的方块，不会触发该事件，包括但不限于床、门、告示牌、船、头部模型、盔甲架，半台阶方块叠加时等。
  - 修改放置方块信息只对一般方块有效，对一些特殊方块无效，会导致放置取消，特殊方块包括：钟、蜡烛、管珊瑚扇、台阶、青蛙卵、脚手架、海泡菜、顶层雪、睡莲

### ServerSpawnMobEvent {#serverspawnmobevent}

游戏内自动生成生物，以及使用api生成生物时触发

信号：[world.beforeEvents.entitySpawn](events/beforeEvents.md#entitySpawn)。分类：世界。

参数类型：[WorldEntitySpawnBeforeEvent](reference/WorldEntitySpawnBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ServerSpawnMobEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `identifier` | `identifier` | [str](../common/type-system.md#str) | 只读 | 生成实体的命名空间 |
| [type](../common/type-system.md#type) | [type](../common/type-system.md#type) | [int](../common/type-system.md#int) | 只读 | 生成实体的类型，参考EntityType |
| `baby` | `baby` | [bool](../common/type-system.md#bool) | 只读 | 生成怪物是否是幼年怪 |
| `x` | `x` | [float](../common/type-system.md#float) | 只读 | 生成实体坐标x |
| `y` | `y` | [float](../common/type-system.md#float) | 只读 | 生成实体坐标y |
| `z` | `z` | [float](../common/type-system.md#float) | 只读 | 生成实体坐标z |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 生成实体的维度，默认值为0（0为主世界，1为地狱，2为末地） |
| `realIdentifier` | `realIdentifier` | [str](../common/type-system.md#str) | 只读 | 生成实体的命名空间，通过MOD API生成的生物在这个参数也能获取到真正的命名空间，而不是以custom开头的 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消生成该实体 |

**原生前提与限制：**

- 如果通过MOD API生成，identifier命名空间为custom。如果需要屏蔽原版的生物生成，可以判断identifier命名空间不为custom时设置cancel为True

### EntityStopRidingEvent {#entitystopridingevent}

触发时机：当实体停止骑乘时

信号：[world.beforeEvents.entityStopRiding](events/beforeEvents.md#entityStopRiding)。分类：实体。

参数类型：[WorldEntityStopRidingBeforeEvent](reference/WorldEntityStopRidingBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("EntityStopRidingEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `mount` | `rideId` | [str](../common/type-system.md#str) | 只读 | 坐骑id |
| `exitFromRider` | `exitFromRider` | [bool](../common/type-system.md#bool) | 只读 | 是否下坐骑 |
| `entityIsBeingDestroyed` | `entityIsBeingDestroyed` | [bool](../common/type-system.md#bool) | 只读 | 坐骑是否将要销毁 |
| `switchingRides` | `switchingRides` | [bool](../common/type-system.md#bool) | 只读 | 是否换乘坐骑 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True可以取消（需要与客户端事件一同取消） |

**原生前提与限制：**

- 以下情况不允许取消
    1. ride组件StopEntityRiding接口
    1. 玩家传送时
    1. 坐骑死亡时
    1. 玩家睡觉时
    1. 玩家死亡时
    1. 未驯服的马
    1. 怕水的生物坐骑进入水里
    1. 切换维度

### ExtinguishFireServerEvent {#extinguishfireserverevent}

玩家扑灭火焰时触发。下雨，倒水等方式熄灭火焰不会触发。

信号：[world.beforeEvents.extinguishFire](events/beforeEvents.md#extinguishFire)。分类：玩家。

参数类型：[WorldExtinguishFireBeforeEvent](reference/WorldExtinguishFireBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ExtinguishFireServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `pos` | `pos` | [tuple](../common/type-system.md#tuple)([float](../common/type-system.md#float),[float](../common/type-system.md#float),[float](../common/type-system.md#float)) | 只读 | 火焰方块的坐标 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 修改为True时，可阻止玩家扑灭火焰。需要与ExtinguishFireClientEvent一起修改。 |

### OnBeforeFallOnBlockServerEvent {#onbeforefallonblockserverevent}

触发时机：当实体刚降落到方块上时服务端触发，主要用于伤害计算

信号：[world.beforeEvents.fallOnBlock](events/beforeEvents.md#fallOnBlock)。分类：方块。

参数类型：[WorldFallOnBlockBeforeEvent](reference/WorldFallOnBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("OnBeforeFallOnBlockServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 方块位置x |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 方块位置y |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 方块位置z |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `fallDistance` | `fallDistance` | [float](../common/type-system.md#float) | 同步回调中 | 实体下降距离，可在脚本层传给引擎 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消引擎对实体下降伤害的计算 |

**原生前提与限制：**

- 不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义方块JSON组件）
  - 如果要在脚本层修改fallDistance，回传的一定要是浮点型，例如需要赋值0.0而不是0
  - 可能会因为轻微的反弹触发多次，可在脚本层针对fallDistance的值进行判断

### OnAfterFallOnBlockServerEvent {#onafterfallonblockserverevent}

触发时机：当实体降落到方块后服务端触发，主要用于力的计算

信号：[world.beforeEvents.fallOnBlockMotion](events/beforeEvents.md#fallOnBlockMotion)。分类：方块。

参数类型：[WorldFallOnBlockMotionBeforeEvent](reference/WorldFallOnBlockMotionBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("OnAfterFallOnBlockServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `posX` | `posX` | [float](../common/type-system.md#float) | 只读 | 实体位置x |
| `posY` | `posY` | [float](../common/type-system.md#float) | 只读 | 实体位置y |
| `posZ` | `posZ` | [float](../common/type-system.md#float) | 只读 | 实体位置z |
| `motionX` | `motionX` | [float](../common/type-system.md#float) | 同步回调中 | 瞬时移动X方向的力 |
| `motionY` | `motionY` | [float](../common/type-system.md#float) | 同步回调中 | 瞬时移动Y方向的力 |
| `motionZ` | `motionZ` | [float](../common/type-system.md#float) | 同步回调中 | 瞬时移动Z方向的力 |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `calculate` | `calculate` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否按脚本层传值计算力 |

**原生前提与限制：**

- 不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义方块JSON组件）
  - 如果要在脚本层修改motion，回传的需要是浮点型，例如需要赋值0.0而不是0
  - 如果需要修改实体的力，最好配合客户端事件同步修改，避免产生非预期现象
  - 因为引擎最后一定会按照原版方块规则计算力（普通方块置0，床、粘液块等反弹），所以脚本层如果想直接修改当前力需要将calculate设为true取消原版计算，按照传回值计算
  - 引擎在落地之后，OnAfterFallOnBlockServerEvent会一直触发，因此请在脚本层中做对应的逻辑判断

### FallingBlockBreakServerEvent {#fallingblockbreakserverevent}

触发时机：当下落的方块实体被破坏时，服务端触发该事件

信号：[world.beforeEvents.fallingBlockBreak](events/beforeEvents.md#fallingBlockBreak)。分类：方块。

参数类型：[WorldFallingBlockBreakBeforeEvent](reference/WorldFallingBlockBreakBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("FallingBlockBreakServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `fallingBlock` | `fallingBlockId` | [str](../common/type-system.md#str) | 只读 | 下落的方块实体id |
| `fallingBlockX` | `fallingBlockX` | [float](../common/type-system.md#float) | 只读 | 下落的方块实体位置x |
| `fallingBlockY` | `fallingBlockY` | [float](../common/type-system.md#float) | 只读 | 下落的方块实体位置y |
| `fallingBlockZ` | `fallingBlockZ` | [float](../common/type-system.md#float) | 只读 | 下落的方块实体位置z |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 重力方块的identifier，包含命名空间及名称 |
| `fallTickAmount` | `fallTickAmount` | [int](../common/type-system.md#int) | 只读 | 下落的方块实体持续下落了多少tick |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 下落的方块实体维度id |
| `cancelDrop` | `cancelDrop` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消方块物品掉落，可以在脚本层中设置 |

**原生前提与限制：**

- 不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义重力方块）

### FallingBlockCauseDamageBeforeServerEvent {#fallingblockcausedamagebeforeserverevent}

触发时机：当下落的方块开始计算砸到实体的伤害时，服务端触发该事件

信号：[world.beforeEvents.fallingBlockCauseDamage](events/beforeEvents.md#fallingBlockCauseDamage)。分类：方块。

参数类型：[WorldFallingBlockCauseDamageBeforeEvent](reference/WorldFallingBlockCauseDamageBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("FallingBlockCauseDamageBeforeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `fallingBlock` | `fallingBlockId` | [str](../common/type-system.md#str) | 只读 | 下落的方块实体id |
| `fallingBlockX` | `fallingBlockX` | [float](../common/type-system.md#float) | 只读 | 下落的方块实体位置x |
| `fallingBlockY` | `fallingBlockY` | [float](../common/type-system.md#float) | 只读 | 下落的方块实体位置y |
| `fallingBlockZ` | `fallingBlockZ` | [float](../common/type-system.md#float) | 只读 | 下落的方块实体位置z |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 重力方块的identifier，包含命名空间及名称 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 下落的方块实体维度id |
| `collidingEntities` | `collidingEntitys` | [list](../common/type-system.md#list)([str](../common/type-system.md#str)) | 只读 | 当前碰撞到的实体列表id，如果没有的话是[None](../common/type-system.md#none) |
| `fallTickAmount` | `fallTickAmount` | [int](../common/type-system.md#int) | 只读 | 下落的方块实体持续下落了多少tick |
| `fallDistance` | `fallDistance` | [float](../common/type-system.md#float) | 只读 | 下落的方块实体持续下落了多少距离 |
| `isHarmful` | `isHarmful` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否计算对实体的伤害，引擎传来的值由json配置和伤害是否大于0决定，可在脚本层修改传回引擎 |
| `fallDamage` | `fallDamage` | [int](../common/type-system.md#int) | 同步回调中 | 对实体的伤害，引擎传来的值距离和json配置决定，可在脚本层修改传回引擎 |

**原生前提与限制：**

- 不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义重力方块）
  - 服务端通常触发在客户端之后，而且有时会相差一个tick，这就意味着可能发生以下现象:服务端fallTickAmount比配置强制破坏时间多1tick，下落的距离、下落的伤害计算出来比客户端时间多1tick的误差。

### OnFireHurtEvent {#onfirehurtevent}

生物受到火焰伤害时触发

信号：[world.beforeEvents.fireHurt](events/beforeEvents.md#fireHurt)。分类：实体。

参数类型：[WorldFireHurtBeforeEvent](reference/WorldFireHurtBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("OnFireHurtEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `victim` | `victim` | [str](../common/type-system.md#str) | 只读 | 受伤实体id |
| `src` | `src` | [str](../common/type-system.md#str) | 只读 | 火焰创建者id |
| `fireTime` | `fireTime` | [float](../common/type-system.md#float) | 只读 | 着火时间，单位秒, 不支持修改 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消此处火焰伤害 |
| `cancelIgnite` | `cancelIgnite` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消点燃效果 |

### GlobalCommandServerEvent {#globalcommandserverevent}

服务端全局命令事件，包括聊天栏发送、SetCommand接口、命令方块（矿车）、行为包动画执行命令

信号：[world.beforeEvents.globalCommand](events/beforeEvents.md#globalCommand)。分类：世界。

参数类型：[WorldGlobalCommandBeforeEvent](reference/WorldGlobalCommandBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("GlobalCommandServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 执行命令的实体id, 如果没有此键，则是命令方块执行的命令 |
| `command` | `command` | [str](../common/type-system.md#str) | 只读 | 将要被执行的命令 |
| `blockPos` | `blockPos` | [tuple](../common/type-system.md#tuple)([int](../common/type-system.md#int),[int](../common/type-system.md#int),[int](../common/type-system.md#int)) | 只读 | 执行命令的实体或方块的方块坐标 |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 执行命令的实体或方块所在维度id |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True可以取消命令执行 |

**原生前提与限制：**

- 有实体的事件参数例子：

    

  - 命令方块(无实体)的事件参数例子：

### ItemDurabilityChangedServerEvent {#itemdurabilitychangedserverevent}

物品耐久度变化事件

信号：[world.beforeEvents.itemDurabilityChange](events/beforeEvents.md#itemDurabilityChange)。分类：物品。

参数类型：[WorldItemDurabilityChangeBeforeEvent](reference/WorldItemDurabilityChangeBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ItemDurabilityChangedServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 物品拥有者的实体id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 物品的物品信息字典 |
| `durabilityBefore` | `durabilityBefore` | [int](../common/type-system.md#int) | 只读 | 变化前耐久度 |
| `durability` | `durability` | [int](../common/type-system.md#int) | 同步回调中 | 变化后耐久度,支持修改。但是请注意修改范围，支持范围为-32768,32767) |
| `canChange` | `canChange` | [bool](../common/type-system.md#bool) | 只读 | 是否支持修改，为true时支持通过durability修改，为false时不支持 |

**原生前提与限制：**

- 目前只有存在耐久的物品，并且有物主的物品才会触发该事件，存在发射器中发射导致的物品耐久变化不会触发该事件
  - 目前铁砧修复、经验修补魔咒、SetItemDurability接口触发的耐久度变化中canChange为false，并且不支持修改变化后耐久度

### ItemPullOutCustomContainerServerEvent {#itempulloutcustomcontainerserverevent}

漏出物品到漏斗时触发该事件

信号：[world.beforeEvents.itemPullOutCustomContainer](events/beforeEvents.md#itemPullOutCustomContainer)。分类：物品。

参数类型：[WorldItemPullOutCustomContainerBeforeEvent](reference/WorldItemPullOutCustomContainerBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ItemPullOutCustomContainerServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 漏斗漏出物品的物品信息字典 |
| `collectionName` | `collectionName` | [str](../common/type-system.md#str) | 只读 | 漏出物品的容器名称，目前仅支持netease_container |
| `collectionIndex` | `collectionIndex` | [int](../common/type-system.md#int) | 只读 | 漏出物品的容器索引 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 容器方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 容器方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 容器方块z坐标 |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 容器方块所在的维度id |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消该操作，默认为false，事件中改为true时拒绝此次漏出物品的操作 |

### ItemPushInCustomContainerServerEvent {#itempushincustomcontainerserverevent}

漏斗漏入物品时触发该事件

信号：[world.beforeEvents.itemPushInCustomContainer](events/beforeEvents.md#itemPushInCustomContainer)。分类：物品。

参数类型：[WorldItemPushInCustomContainerBeforeEvent](reference/WorldItemPushInCustomContainerBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ItemPushInCustomContainerServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 漏斗漏入物品的物品信息字典 |
| `collectionName` | `collectionName` | [str](../common/type-system.md#str) | 只读 | 目标容器名称，目前仅支持netease_container |
| `collectionIndex` | `collectionIndex` | [int](../common/type-system.md#int) | 只读 | 目标容器索引 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 容器方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 容器方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 容器方块z坐标 |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 容器方块所在的维度id |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消该操作，默认为false，事件中改为true时拒绝此次漏入物品的操作 |

### OnItemPutInEnchantingModelServerEvent {#onitemputinenchantingmodelserverevent}

触发时机：玩家将可附魔物品放到附魔台上时

信号：[world.beforeEvents.itemPutInEnchantingModel](events/beforeEvents.md#itemPutInEnchantingModel)。分类：物品。

参数类型：[WorldItemPutInEnchantingModelBeforeEvent](reference/WorldItemPutInEnchantingModelBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("OnItemPutInEnchantingModelServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id，参数类型为[str](../common/type-system.md#str) |
| `slotType` | `slotType` | [int](../common/type-system.md#int) | 只读 | 玩家放入物品的EnchantSlotType |
| `options` | `options` | [list](../common/type-system.md#list) | 同步回调中 | 附魔台选项 |
| `change` | `change` | [bool](../common/type-system.md#bool) | 同步回调中 | 传入True时，附魔台选项会被新传入的options覆盖 |

**原生前提与限制：**

- options为包含三个dict的list，单个dict的格式形如&#123;'cost': 1, 'enchantData': [(1,1)], 'modEnchantData': [('custom_enchant, 1')]&#125;，cost为解锁该选项所需的玩家等级，enchantData为该附魔选项包含的原版附魔数据，modEnchantData为该选项包含的自定义附魔数据

### ItemReleaseUsingServerEvent {#itemreleaseusingserverevent}

触发时机：释放正在使用的物品时

信号：[world.beforeEvents.itemReleaseUsing](events/beforeEvents.md#itemReleaseUsing)。分类：物品。

参数类型：[WorldItemReleaseUsingBeforeEvent](reference/WorldItemReleaseUsingBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ItemReleaseUsingServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `durationLeft` | `durationLeft` | [float](../common/type-system.md#float) | 只读 | 蓄力剩余时间(当物品缺少"minecraft:maxduration"组件时,蓄力剩余时间为负数) |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 使用的物品的物品信息字典 |
| `maxUseDuration` | `maxUseDuration` | [int](../common/type-system.md#int) | 只读 | 最大蓄力时长 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True可以取消，需要同时取消客户端事件[ItemReleaseUsingClientEvent](../client/events.md#itemreleaseusingclientevent) |
| `changeItem` | `changeItem` | [bool](../common/type-system.md#bool) | 同步回调中 | 如果要在该事件的回调中修改当前使用槽位的物品，需设置这个参数为True，否则将修改物品失败，例如修改耐久度或者替换成新物品 |

### ServerItemTryUseEvent {#serveritemtryuseevent}

玩家点击右键尝试使用物品时服务端抛出的事件。

信号：`world.beforeEvents.getNativeEvent('ServerItemTryUseEvent')`。分类：物品。

参数类型：[WorldItemUseBeforeEvent](reference/WorldItemUseBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ServerItemTryUseEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 使用的物品的物品信息字典 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设为True可取消物品的使用 |

**原生前提与限制：**

- ClientItemTryUseEvent的cancel设置为True时，服务端事件不会被触发了。
  - [ServerItemTryUseEvent](native-events.md#serveritemtryuseevent)/ClientItemTryUseEvent不能取消对方块使用物品的行为，如使用生物蛋，使用桶倒出/收集，使用打火石点燃草等；如果想要取消这种行为，请使用ClientItemUseOnEvent和ServerItemUseOnEvent

### ServerItemUseOnEvent {#serveritemuseonevent}

玩家在对方块使用物品之前服务端抛出的事件。

信号：`world.beforeEvents.getNativeEvent('ServerItemUseOnEvent')`。分类：物品。

参数类型：[WorldItemUseOnBeforeEvent](reference/WorldItemUseOnBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ServerItemUseOnEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 使用的物品的物品信息字典 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块 x 坐标值 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块 y 坐标值 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块 z 坐标值 |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier |
| `blockAuxValue` | `blockAuxValue` | [int](../common/type-system.md#int) | 只读 | 方块的附加值 |
| `face` | `face` | [int](../common/type-system.md#int) | 只读 | 点击方块的面，参考Facing枚举 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `clickX` | `clickX` | [float](../common/type-system.md#float) | 只读 | 点击点的x比例位置 |
| `clickY` | `clickY` | [float](../common/type-system.md#float) | 只读 | 点击点的y比例位置 |
| `clickZ` | `clickZ` | [float](../common/type-system.md#float) | 只读 | 点击点的z比例位置 |
| `ret` | `ret` | [bool](../common/type-system.md#bool) | 同步回调中 | 设为True可取消物品的使用 |

取消映射：`event.cancel = True` 等价于 `event.ret = True`。只影响该原生动作。

**原生前提与限制：**

- 客户端事件ClientItemUseOnEvent设置ret设置为True时，服务端不再会接受到这个事件。
  - 当对原生方块进行使用时，如堆肥桶等类似有 使用 功能的方块使用物品时，不会触发该事件。而当原生方块加入监听后，ServerBlockUseEvent会触发。当需要获取触发时使用的物品时，可以通过item组件（例如GetPlayerItem接口）获取手中持有的物品，对应的客户端事件同理。

### MobGriefingBlockServerEvent {#mobgriefingblockserverevent}

环境生物改变方块时触发，触发的时机与mobgriefing游戏规则影响的行为相同

信号：[world.beforeEvents.mobGriefingBlock](events/beforeEvents.md#mobGriefingBlock)。分类：实体。

参数类型：[WorldMobGriefingBlockBeforeEvent](reference/WorldMobGriefingBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("MobGriefingBlockServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否允许触发，默认为False，若设为True，可阻止触发后续物理交互事件 |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 触发的entity的唯一ID |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |

**原生前提与限制：**

- 触发的时机包括：生物踩踏耕地、破坏单个方块、破门、火矢点燃方块、凋灵boss破坏方块、末影龙破坏方块、末影人捡起方块、蠹虫破坏被虫蚀的方块、蠹虫把方块变成被虫蚀的方块、凋零杀死生物生成凋零玫瑰、生物踩坏海龟蛋。

### ServerChatEvent {#serverchatevent}

玩家发送聊天信息时触发

信号：`world.beforeEvents.getNativeEvent('ServerChatEvent')`。分类：世界。

参数类型：[WorldNativeChatSendBeforeEvent](reference/WorldNativeChatSendBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ServerChatEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `username` | `username` | [str](../common/type-system.md#str) | 同步回调中 | 玩家名称 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `message` | `message` | [str](../common/type-system.md#str) | 同步回调中 | 玩家发送的聊天消息内容 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消这个聊天事件，若取消可以设置为True |
| `bChatById` | `bChatById` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否把聊天消息发送给指定在线玩家，而不是广播给所有在线玩家，若只发送某些玩家可以设置为True |
| `bForbid` | `bForbid` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否禁言，仅apollo可用。true：被禁言，玩家聊天会提示“你已被管理员禁言”。 |
| `targets` | `toPlayerIds` | [list](../common/type-system.md#list)([str](../common/type-system.md#str)) | 同步回调中 | 接收聊天消息的玩家id列表，bChatById为True时生效 |
| `gameChatPrefix` | `gameChatPrefix` | [str](../common/type-system.md#str) | 同步回调中 | 设置当前玩家在网易聊天界面中的前缀，字数限制4，从字符串头部开始取。前缀文本输入非字符串格式时会被置为空。若cancel为True，会取消掉本次的前缀修改 |
| `gameChatPrefixColorR` | `gameChatPrefixColorR` | [float](../common/type-system.md#float) | 同步回调中 | 设置当前玩家在网易聊天界面中前缀颜色rgb的r值，范围为`[0,1]`。颜色数值输入其他格式时会被置为0。若cancel为True，会取消掉本次的颜色修改 |
| `gameChatPrefixColorG` | `gameChatPrefixColorG` | [float](../common/type-system.md#float) | 同步回调中 | 设置当前玩家在网易聊天界面中前缀颜色rgb的g值，范围为`[0,1]`。颜色数值输入其他格式时会被置为0。若cancel为True，会取消掉本次的颜色修改 |
| `gameChatPrefixColorB` | `gameChatPrefixColorB` | [float](../common/type-system.md#float) | 同步回调中 | 设置当前玩家在网易聊天界面中前缀颜色rgb的b值，范围为`[0,1]`。颜色数值输入其他格式时会被置为0。若cancel为True，会取消掉本次的颜色修改 |

### ExplosionServerEvent {#explosionserverevent}

当发生爆炸时触发。

信号：`world.beforeEvents.getNativeEvent('ExplosionServerEvent')`。分类：世界。

参数类型：[WorldNativeExplosionBeforeEvent](reference/WorldNativeExplosionBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ExplosionServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `blocks` | `blocks` | [list](../common/type-system.md#list)[[x,y,z,cancel]`,...\] | 同步回调中 | 爆炸导致的被破坏方块坐标(x,y,z)，cancel是一个bool值 |
| `victims` | `victims` | [list](../common/type-system.md#list)/[None](../common/type-system.md#none) | 只读 | 受伤实体id列表，当该爆炸创建者id为None时，victims也为None |
| `source` | `sourceId` | [str](../common/type-system.md#str)/[None](../common/type-system.md#none) | 只读 | 爆炸创建者id |
| `explodePos` | `explodePos` | [list](../common/type-system.md#list) | 只读 | 爆炸位置[x,y,z] |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |

**原生前提与限制：**

- 通过设置blocks中cancel的bool值为True可以将该方块的爆炸取消，例如(x,y,z,True)
  - 某些情况下爆炸创建者id为None，此时受伤实体id列表也为None，比如爬行者所造成的爆炸。

### PistonActionServerEvent {#pistonactionserverevent}

触发时机：活塞或者粘性活塞推送/缩回影响附近方块时

信号：[world.beforeEvents.pistonAction](events/beforeEvents.md#pistonAction)。分类：方块。

参数类型：[WorldPistonActionBeforeEvent](reference/WorldPistonActionBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PistonActionServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否允许触发，默认为False，若设为True，可阻止触发后续的事件 |
| `action` | `action` | [str](../common/type-system.md#str) | 只读 | 推送时=expanding；缩回时=retracting |
| `pistonFacing` | `pistonFacing` | [int](../common/type-system.md#int) | 只读 | 活塞的朝向，参考Facing枚举 |
| `pistonMoveFacing` | `pistonMoveFacing` | [int](../common/type-system.md#int) | 只读 | 活塞的运动方向，参考Facing枚举 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 活塞方块所在的维度 |
| `pistonX` | `pistonX` | [int](../common/type-system.md#int) | 只读 | 活塞方块的x坐标 |
| `pistonY` | `pistonY` | [int](../common/type-system.md#int) | 只读 | 活塞方块的y坐标 |
| `pistonZ` | `pistonZ` | [int](../common/type-system.md#int) | 只读 | 活塞方块的z坐标 |
| `blockList` | `blockList` | [list](../common/type-system.md#list)[[x,y,z]`,...\] | 只读 | 活塞运动影响到产生被移动效果的方块坐标[x,y,z]，均为int类型 |
| `breakBlockList` | `breakBlockList` | [list](../common/type-system.md#list)[[x,y,z]`,...\] | 只读 | 活塞运动影响到产生被破坏效果的方块坐标[x,y,z]，均为int类型 |
| `entities` | `entityList` | [list](../common/type-system.md#list)[[string](../common/type-system.md#str),...] | 只读 | 活塞运动影响到产生被移动或被破坏效果的实体的ID列表 |

### PlaceNeteaseLargeFeatureServerEvent {#placeneteaselargefeatureserverevent}

触发时机：网易版大型结构即将生成时服务端抛出该事件。

信号：[world.beforeEvents.placeNeteaseLargeFeature](events/beforeEvents.md#placeNeteaseLargeFeature)。分类：世界。

参数类型：[WorldPlaceNeteaseLargeFeatureBeforeEvent](reference/WorldPlaceNeteaseLargeFeatureBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlaceNeteaseLargeFeatureServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `pos` | `pos` | [tuple](../common/type-system.md#tuple) | 只读 | 中心结构放置坐标(x, z) |
| `rot` | `rot` | [int](../common/type-system.md#int) | 只读 | 中心结构顺时针旋转角度 |
| `depth` | `depth` | [int](../common/type-system.md#int) | 只读 | 大型结构递归深度 |
| `centerPool` | `centerPool` | [str](../common/type-system.md#str) | 只读 | 中心池的identifier |
| `ignoreFitInContext` | `ignoreFitInContext` | [bool](../common/type-system.md#bool) | 只读 | 是否允许生成过结构的地方是否可以继续生成结构 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True时可阻止该大型结构的放置 |

**原生前提与限制：**

- 1.使用PlaceNeteaseLargeFeature接口触发此事件时，可正常调用其他Mod SDK接口
    2.使用自定义大型特征功能，配置Json的方式触发此事件时，调用其他Mod SDK接口将无法生效，强烈建议仅用于设置结构放置与否

### PlaceNeteaseStructureFeatureEvent {#placeneteasestructurefeatureevent}

触发时机：首次生成地形时，结构特征即将生成时服务端抛出该事件。

信号：[world.beforeEvents.placeNeteaseStructureFeature](events/beforeEvents.md#placeNeteaseStructureFeature)。分类：世界。

参数类型：[WorldPlaceNeteaseStructureFeatureBeforeEvent](reference/WorldPlaceNeteaseStructureFeatureBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlaceNeteaseStructureFeatureEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `structureName` | `structureName` | [str](../common/type-system.md#str) | 同步回调中 | 结构名称，可修改 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 结构坐标最小方块所在的x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 结构坐标最小方块所在的y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 结构坐标最小方块所在的z坐标 |
| `biomeType` | `biomeType` | [int](../common/type-system.md#int) | 只读 | 该feature所放置区块的生物群系类型 |
| `biomeName` | `biomeName` | [str](../common/type-system.md#str) | 只读 | 该feature所放置区块的生物群系名称 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True时可阻止该结构的放置 |

**原生前提与限制：**

- **需要配合AddNeteaseFeatureWhiteList接口一同使用**
    若在本监听事件中调用其他mod SDK接口将无法生效，强烈建议本事件仅用于设置结构放置与否
    该事件只会在网易版结构放置时抛出
    structureName参数修改为不存在结构或者原生结构时，开发包会出现断言。

### OnPlayerActiveShieldServerEvent {#onplayeractiveshieldserverevent}

触发时机：玩家激活/取消激活盾牌触发的事件。包括玩家持盾进入潜行状态，以及在潜行状态切换盾牌（切换耐久度不同的相同盾牌不会触发）

信号：[world.beforeEvents.playerActiveShield](events/beforeEvents.md#playerActiveShield)。分类：物品。

参数类型：[WorldPlayerActiveShieldBeforeEvent](reference/WorldPlayerActiveShieldBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("OnPlayerActiveShieldServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家Id |
| `isActive` | `isActive` | [bool](../common/type-system.md#bool) | 只读 | True:尝试激活,False:尝试取消激活 |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 盾牌物品的物品信息字典 |
| `cancelable` | `cancelable` | [bool](../common/type-system.md#bool) | 只读 | 是否可以取消。如果玩家在潜行状态切换盾牌，则无法取消 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消这次激活 |

### PlayerAttackEntityEvent {#playerattackentityevent}

触发时机：当玩家攻击时触发该事件。

信号：[world.beforeEvents.playerAttackEntity](events/beforeEvents.md#playerAttackEntity)。分类：玩家。

参数类型：[WorldPlayerAttackEntityBeforeEvent](reference/WorldPlayerAttackEntityBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerAttackEntityEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `target` | `victimId` | [str](../common/type-system.md#str) | 只读 | 受击者id |
| `damage` | `damage` | [float](../common/type-system.md#float) | 同步回调中 | 伤害值：引擎传过来的值是0 允许脚本层修改为其他数 |
| `isValid` | `isValid` | [int](../common/type-system.md#int) | 同步回调中 | 脚本是否设置伤害值：1表示是；0 表示否 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消该次攻击，默认不取消 |
| `isKnockBack` | `isKnockBack` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否支持击退效果，默认支持，当不支持时将屏蔽武器击退附魔效果 |
| `isCrit` | `isCrit` | [bool](../common/type-system.md#bool) | 只读 | 本次攻击是否产生暴击,不支持修改 |

### OnPlayerBlockedByShieldBeforeServerEvent {#onplayerblockedbyshieldbeforeserverevent}

触发时机：玩家使用盾牌抵挡伤害之前触发

信号：[world.beforeEvents.playerBlockedByShield](events/beforeEvents.md#playerBlockedByShield)。分类：物品。

参数类型：[WorldPlayerBlockedByShieldBeforeEvent](reference/WorldPlayerBlockedByShieldBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("OnPlayerBlockedByShieldBeforeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家Id |
| `source` | `sourceId` | [str](../common/type-system.md#str) | 只读 | 伤害来源实体Id，没有实体返回"-1" |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 盾牌物品字典物品信息字典 |
| `damage` | `damage` | [float](../common/type-system.md#float) | 只读 | 抵挡的伤害数值 |

**原生前提与限制：**

- 盾牌抵挡了所有伤害时，才会触发事件；部分抛射物造成的伤害无法全部抵挡，无法触发事件，例如带有穿透魔咒的弩。

### PlayerEatFoodServerEvent {#playereatfoodserverevent}

触发时机：玩家吃下食物时触发

信号：[world.beforeEvents.playerEatFood](events/beforeEvents.md#playerEatFood)。分类：玩家。

参数类型：[WorldPlayerEatFoodBeforeEvent](reference/WorldPlayerEatFoodBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerEatFoodServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家Id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 食物物品的物品信息字典 |
| `hunger` | `hunger` | [int](../common/type-system.md#int) | 同步回调中 | 食物增加的饥饿值，可修改 |
| `nutrition` | `nutrition` | [float](../common/type-system.md#float) | 同步回调中 | 食物的营养价值，回复饱和度 = 食物增加的饥饿值 * 食物的营养价值 * 2，饱和度最大不超过当前饥饿值，可修改 |

**原生前提与限制：**

- 由于牛奶本身并没有饱食度的概念，因此，当喝牛奶触发该事件时，饥饿度、营养价值字段无效并始终为0

### PlayerFeedEntityServerEvent {#playerfeedentityserverevent}

玩家喂养生物时触发，例如玩家手持小麦喂养牛、玩家手持胡萝卜喂养幼年猪。

信号：[world.beforeEvents.playerFeedEntity](events/beforeEvents.md#playerFeedEntity)。分类：玩家。

参数类型：[WorldPlayerFeedEntityBeforeEvent](reference/WorldPlayerFeedEntityBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerFeedEntityServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 主动喂养生物的玩家的唯一ID |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 被喂养生物的唯一ID |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 当前玩家手持物品的物品信息字典 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消触发，默认为False，若设为True，可阻止触发后续的生物喂养逻辑 |

**原生前提与限制：**

- 1.对于幼年生物，用对应的物品喂养后就可以触发事件，例如用小麦喂养幼年牛、用生鲑鱼喂养幼年猫；
    2.对于成年生物，用对应的物品喂养后，该生物要进入“求爱模式”（持续散发红心粒子），才可以触发事件。特殊的成年生物列举如下：
    a.可骑乘生物，例如马，玩家要驯服马后，再给它喂养食物（例如金苹果、金萝卜），才可以触发事件；已驯服的马受伤后，用金苹果喂养时会治疗马，不触发事件，马的血量回满时，再喂养金苹果，才会触发事件；
    b.可驯服生物，例如狼，玩家要用骨头驯服狼后，再给它喂养肉类物品（例如熟猪排），才可以触发事件；
    c.需要在特定环境下才能繁殖的生物，例如熊猫，玩家用竹子喂养熊猫时，熊猫的5格内至少要有8根竹子，喂养后才可以触发事件。
    3.该事件中如需调用使用手持物相关的接口，如PlayerUseItemToEntity或其他设置物品数量的接口，会导致接口正常调用但是物品数量计算异常，建议通过timer延迟调用。

### PlayerFishingServerEvent {#playerfishingserverevent}

玩家钓鱼成功收杆时触发，在钓鱼掉落物生成前触发

信号：`world.beforeEvents.getNativeEvent('PlayerFishingServerEvent')`。分类：玩家。

参数类型：[WorldPlayerFishingBeforeEvent](reference/WorldPlayerFishingBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerFishingServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 钓鱼的玩家id |
| `hook` | `hookEntity` | [str](../common/type-system.md#str) | 只读 | 鱼钩实体id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 玩家手持鱼竿的物品信息字典 |
| `itemList` | `itemList` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 同步回调中 | 钓鱼获得的物品信息字典列表，支持修改。修改后需将itemChange设置为True |
| `itemChange` | `itemChange` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否修改了itemList，默认为False。当修改了itemList时需要设置为True才能生效 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消钓鱼成功，设置为True时不会生成掉落物 |

**原生前提与限制：**

- 设置cancel为True时，不会生成掉落物，也不会触发PlayerFishingAfterServerEvent事件
  - 修改itemList后必须设置itemChange为True，否则修改不会生效

### ServerPlayerGetExperienceOrbEvent {#serverplayergetexperienceorbevent}

触发时机：玩家获取经验球时触发的事件

信号：[world.beforeEvents.playerGetExperienceOrb](events/beforeEvents.md#playerGetExperienceOrb)。分类：玩家。

参数类型：[WorldPlayerGetExperienceOrbBeforeEvent](reference/WorldPlayerGetExperienceOrbBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ServerPlayerGetExperienceOrbEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `experienceValue` | `experienceValue` | [int](../common/type-system.md#int) | 只读 | 经验球经验值 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消（开发者传入） |

**原生前提与限制：**

- `cancel`值设为True时，捡起的经验球不会增加经验值，但是经验球一样会消失。

### PlayerHungerChangeServerEvent {#playerhungerchangeserverevent}

玩家饥饿度变化时触发该事件

信号：[world.beforeEvents.playerHungerChange](events/beforeEvents.md#playerHungerChange)。分类：玩家。

参数类型：[WorldPlayerHungerChangeBeforeEvent](reference/WorldPlayerHungerChangeBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerHungerChangeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `hungerBefore` | `hungerBefore` | [float](../common/type-system.md#float) | 只读 | 变化前的饥饿度 |
| `hunger` | `hunger` | [float](../common/type-system.md#float) | 只读 | 变化后的饥饿度 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消饥饿度变化 |

**原生前提与限制：**

- 当通过setplayerhunger接口设置饥饿度时，不会触发服务端对应的事件
  - 当通过/hunger等指令设置饥饿度设置时，hunger字段值可能会超过最大饥饿度

### PlayerHurtEvent {#playerhurtevent}

触发时机：当玩家受伤害前触发该事件。

信号：[world.beforeEvents.playerHurt](events/beforeEvents.md#playerHurt)。分类：玩家。

参数类型：[WorldPlayerHurtBeforeEvent](reference/WorldPlayerHurtBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerHurtEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `id` | [str](../common/type-system.md#str) | 只读 | 受击玩家id |
| `attacker` | `attacker` | [str](../common/type-system.md#str) | 只读 | 伤害来源实体id，若没有实体攻击，例如高空坠落，id为-1 |
| `customTag` | `customTag` | [str](../common/type-system.md#str) | 只读 | 使用Hurt接口传入的自定义伤害类型 |
| `cause` | `cause` | [str](../common/type-system.md#str) | 只读 | 伤害来源，详见Minecraft枚举值文档的ActorDamageCause |

### PlayerInteractServerEvent {#playerinteractserverevent}

触发时机：玩家可以与实体交互时。如果是鼠标控制模式，则当准心对着实体时触发。如果是触屏模式，则触发时机与屏幕下方的交互按钮显示的时机相同。玩家真正与实体发生交互的事件见[PlayerDoInteractServerEvent](native-events.md#playerdointeractserverevent)

信号：`world.beforeEvents.getNativeEvent('PlayerInteractServerEvent')`。分类：玩家。

参数类型：[WorldPlayerInteractBeforeEvent](reference/WorldPlayerInteractBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerInteractServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消触发，默认为False，若设为True，可阻止触发后续的实体交互事件 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 主动与实体互动的玩家的唯一ID |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 当前玩家手持物品的物品信息字典 |
| `target` | `victimId` | [str](../common/type-system.md#str) | 只读 | 被动的实体的唯一ID |

### PlayerJoinMessageEvent {#playerjoinmessageevent}

触发时机：准备显示“xxx加入游戏”的玩家登录提示文字时服务端抛出的事件。

信号：[world.beforeEvents.playerJoinMessage](events/beforeEvents.md#playerJoinMessage)。分类：世界。

参数类型：[WorldPlayerJoinMessageBeforeEvent](reference/WorldPlayerJoinMessageBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerJoinMessageEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `id` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `name` | `name` | [str](../common/type-system.md#str) | 只读 | 玩家昵称 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否显示提示文字，允许修改。True：不显示提示 |
| `message` | `message` | [str](../common/type-system.md#str) | 同步回调中 | 玩家加入游戏的提示文字，允许修改 |

**原生前提与限制：**

- 对于联机类游戏（如联机大厅、网络游戏等），请勿在此事件的回调函数中使用SetFootPos接口修改玩家的位置，否则可能会因为触发服务端反作弊机制而传送失败。如需要在进入游戏时使用SetFootPos接口，建议监听AddServerPlayerEvent并设置位置。

### PlayerIntendLeaveServerEvent {#playerintendleaveserverevent}

触发时机：即将删除玩家时触发该事件，此时可以通过各种API获取玩家的当前状态。

信号：[world.beforeEvents.playerLeave](events/beforeEvents.md#playerLeave)。分类：世界。

参数类型：[WorldPlayerLeaveBeforeEvent](reference/WorldPlayerLeaveBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerIntendLeaveServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |

**原生前提与限制：**

- 与【[DelServerPlayerEvent](native-events.md#delserverplayerevent)】事件不同，此时可以通过各种API获取玩家的当前状态。

### PlayerLeftMessageServerEvent {#playerleftmessageserverevent}

触发时机：准备显示“xxx离开游戏”的玩家离开提示文字时服务端抛出的事件。

信号：[world.beforeEvents.playerLeftMessage](events/beforeEvents.md#playerLeftMessage)。分类：世界。

参数类型：[WorldPlayerLeftMessageBeforeEvent](reference/WorldPlayerLeftMessageBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerLeftMessageServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `id` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `name` | `name` | [str](../common/type-system.md#str) | 只读 | 玩家昵称 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否显示提示文字，允许修改。True：不显示提示 |
| `message` | `message` | [str](../common/type-system.md#str) | 同步回调中 | 玩家离开游戏的提示文字，允许修改 |

### PlayerNamedEntityServerEvent {#playernamedentityserverevent}

玩家用命名牌重命名实体时触发，例如玩家手持命名牌对羊修改名字、玩家手持命名牌对盔甲架修改名字。

信号：[world.beforeEvents.playerNamedEntity](events/beforeEvents.md#playerNamedEntity)。分类：玩家。

参数类型：[WorldPlayerNamedEntityBeforeEvent](reference/WorldPlayerNamedEntityBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerNamedEntityServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 主动命名实体的玩家的唯一ID |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 被命名实体的唯一ID |
| `preName` | `preName` | [str](../common/type-system.md#str) | 只读 | 实体当前的名字 |
| `afterName` | `afterName` | [str](../common/type-system.md#str) | 只读 | 实体重命名后的名字 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消触发，默认为False，若设为True，可阻止触发后续的实体命名逻辑 |

### PlayerPermissionChangeServerEvent {#playerpermissionchangeserverevent}

玩家权限变更事件

信号：[world.beforeEvents.playerPermissionChange](events/beforeEvents.md#playerPermissionChange)。分类：玩家。

参数类型：[WorldPlayerPermissionChangeBeforeEvent](reference/WorldPlayerPermissionChangeBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerPermissionChangeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `causePlayer` | `causePlayerId` | [str](../common/type-system.md#str) | 只读 | 发起者id |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `oldPermission` | `oldPermission` | [dict](../common/type-system.md#dict) | 只读 | 变化前的权限字典 |
| `newPermission` | `newPermission` | [dict](../common/type-system.md#dict) | 只读 | 变化后的权限字典 |
| `changeCause` | `changeCause` | [int](../common/type-system.md#int) | 只读 | 变化原因，详见Minecraft枚举值文档的PermissionChangeCause |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 为true时，取消本次权限变更 |

**原生前提与限制：**

- 具体权限说明：

| 权限字段 | 类型 | 说明 |
| --- | --- | --- |
| build | [bool](../common/type-system.md#bool) | 放置方块 |
| mine | [bool](../common/type-system.md#bool) | 采集方块 |
| doorsandswitches | [bool](../common/type-system.md#bool) | 使用门和开关 |
| opencontainers | [bool](../common/type-system.md#bool) | 打开容器 |
| attackplayers | [bool](../common/type-system.md#bool) | 攻击玩家 |
| attackmobs | [bool](../common/type-system.md#bool) | 攻击生物 |
| op | [bool](../common/type-system.md#bool) | 操作员命令 |
| teleport | [bool](../common/type-system.md#bool) | 使用传送 |

### PlayerPickupArrowServerEvent {#playerpickuparrowserverevent}

玩家即将捡起抛射物时触发，包括使用"netease:pick_up"的自定义抛射物

信号：[world.beforeEvents.playerPickupArrow](events/beforeEvents.md#playerPickupArrow)。分类：物品。

参数类型：[WorldPlayerPickupArrowBeforeEvent](reference/WorldPlayerPickupArrowBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerPickupArrowServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家Id |
| `arrow` | `arrowId` | [str](../common/type-system.md#str) | 只读 | 抛射物Id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 触碰的物品的物品信息字典 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True时将取消本次拾取 |
| `pickupDelay` | `pickupDelay` | [int](../common/type-system.md#int) | 同步回调中 | 取消拾取后重新设置该物品的拾取cd，小于15帧将视作15帧，大于等于97813帧将视作无法拾取，每秒30帧 |

### ServerPlayerTryTouchEvent {#serverplayertrytouchevent}

玩家即将捡起物品时触发

信号：[world.beforeEvents.playerPickupItem](events/beforeEvents.md#playerPickupItem)。分类：物品。

参数类型：[WorldPlayerPickupItemBeforeEvent](reference/WorldPlayerPickupItemBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ServerPlayerTryTouchEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家Id |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 物品实体的Id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 触碰的物品的物品信息字典 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True时将取消本次拾取 |
| `pickupDelay` | `pickupDelay` | [int](../common/type-system.md#int) | 同步回调中 | 取消拾取后重新设置该物品的拾取cd，小于15帧将视作15帧，大于等于97813帧将视作无法拾取 |

### PlayerStartFishingServerEvent {#playerstartfishingserverevent}

玩家开始钓鱼，生成鱼钩时在服务端触发

信号：[world.beforeEvents.playerStartFishing](events/beforeEvents.md#playerStartFishing)。分类：玩家。

参数类型：[WorldPlayerStartFishingBeforeEvent](reference/WorldPlayerStartFishingBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerStartFishingServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 钓鱼成功的玩家id |
| `hook` | `hookEntity` | [str](../common/type-system.md#str) | 只读 | 鱼钩实体id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 玩家手持鱼竿的物品信息字典 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消，设置为True时会取消生成鱼漂 |

**原生前提与限制：**

- 此事件在鱼钩实体生成后触发，设置cancel为True可取消本次抛竿操作

### PlayerTryAddCustomContainerItemServerEvent {#playertryaddcustomcontaineritemserverevent}

玩家尝试将物品添加到自定义容器时触发该事件

信号：[world.beforeEvents.playerTryAddCustomContainerItem](events/beforeEvents.md#playerTryAddCustomContainerItem)。分类：物品。

参数类型：[WorldPlayerTryAddCustomContainerItemBeforeEvent](reference/WorldPlayerTryAddCustomContainerItemBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerTryAddCustomContainerItemServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 尝试添加物品的物品信息字典 |
| `collectionName` | `collectionName` | [str](../common/type-system.md#str) | 只读 | 放入容器名称，对应容器json中"custom_description"字段 |
| `collectionType` | `collectionType` | [str](../common/type-system.md#str) | 只读 | 放入容器类型，目前仅支持netease_container和netease_ui_container |
| `collectionIndex` | `collectionIndex` | [int](../common/type-system.md#int) | 只读 | 放入容器索引 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 容器方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 容器方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 容器方块z坐标 |

**原生前提与限制：**

- 容器内物品移动，合堆，分堆的操作会分多次事件触发并且顺序不定，编写逻辑时请勿依赖事件触发顺序

### ServerPlayerTryDestroyBlockEvent {#serverplayertrydestroyblockevent}

当玩家即将破坏方块时，服务端线程触发该事件。

信号：`world.beforeEvents.getNativeEvent('ServerPlayerTryDestroyBlockEvent')`。分类：方块。

参数类型：[WorldPlayerTryBreakBlockBeforeEvent](reference/WorldPlayerTryBreakBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ServerPlayerTryDestroyBlockEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `face` | `face` | [int](../common/type-system.md#int) | 只读 | 方块被敲击的面向id，参考Facing枚举 |
| `fullName` | `fullName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxData` | `auxData` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 试图破坏方块的玩家ID |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 默认为False，在脚本层设置为True就能取消该方块的破坏 |
| `spawnResources` | `spawnResources` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否生成掉落物，默认为True，在脚本层设置为False就能取消生成掉落物 |

**原生前提与限制：**

- 若需要禁止某些特殊方块的破坏，需要配合PlayerTryDestroyBlockClientEvent一起使用，例如床，旗帜，箱子这些根据方块实体数据进行渲染的方块
  - 该服务端事件触发于玩家破坏方块时，当方块为秒破方块时（破坏方块所需时间为0或未设置破坏时间），本事件触发在StartDestroyBlockServerEvent事件之前;当方块为非秒破方块时，本事件触发在StartDestroyBlockServerEvent事件之后。
  - 可通过minecraft:destroy_time方块组件来修改方块的破坏时间

### PlayerTryPutCustomContainerItemServerEvent {#playertryputcustomcontaineritemserverevent}

玩家尝试将物品放入自定义容器时触发该事件

信号：[world.beforeEvents.playerTryPutCustomContainerItem](events/beforeEvents.md#playerTryPutCustomContainerItem)。分类：物品。

参数类型：[WorldPlayerTryPutCustomContainerItemBeforeEvent](reference/WorldPlayerTryPutCustomContainerItemBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerTryPutCustomContainerItemServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 尝试放入物品的物品信息字典 |
| `collectionName` | `collectionName` | [str](../common/type-system.md#str) | 只读 | 放入容器名称，对应容器json中"custom_description"字段 |
| `collectionType` | `collectionType` | [str](../common/type-system.md#str) | 只读 | 放入容器类型，目前仅支持netease_container和netease_ui_container |
| `collectionIndex` | `collectionIndex` | [int](../common/type-system.md#int) | 只读 | 放入容器索引 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 容器方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 容器方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 容器方块z坐标 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消该操作，默认为false，事件中改为true时拒绝此次放入自定义容器的操作 |

**原生前提与限制：**

- 该事件只有目标槽位为空时触发，如果目标槽位有相同物品时只会触发PlayerTryAddCustomContainerItemServerEvent事件
  - PC存在shift键移动全部物品，放入同种物品时，可能会触发tryadd和tryput，请开发者注意适配
  - 容器内物品移动，合堆，分堆的操作会分多次事件触发并且顺序不定，编写逻辑时请勿依赖事件触发顺序

### PlayerTryRemoveCustomContainerItemServerEvent {#playertryremovecustomcontaineritemserverevent}

玩家尝试从自定义容器中移除物品时触发该事件

信号：[world.beforeEvents.playerTryRemoveCustomContainerItem](events/beforeEvents.md#playerTryRemoveCustomContainerItem)。分类：物品。

参数类型：[WorldPlayerTryRemoveCustomContainerItemBeforeEvent](reference/WorldPlayerTryRemoveCustomContainerItemBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerTryRemoveCustomContainerItemServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 尝试移除物品的物品信息字典 |
| `collectionName` | `collectionName` | [str](../common/type-system.md#str) | 只读 | 放入容器名称，对应容器json中"custom_description"字段 |
| `collectionType` | `collectionType` | [str](../common/type-system.md#str) | 只读 | 放入容器类型，目前仅支持netease_container和netease_ui_container |
| `collectionIndex` | `collectionIndex` | [int](../common/type-system.md#int) | 只读 | 目标容器索引 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 容器方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 容器方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 容器方块z坐标 |

**原生前提与限制：**

- 容器内物品移动，合堆，分堆的操作会分多次事件触发并且顺序不定，编写逻辑时请勿依赖事件触发顺序

### PlayerTrySleepServerEvent {#playertrysleepserverevent}

玩家尝试使用床睡觉

信号：[world.beforeEvents.playerTrySleep](events/beforeEvents.md#playerTrySleep)。分类：玩家。

参数类型：[WorldPlayerTrySleepBeforeEvent](reference/WorldPlayerTrySleepBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("PlayerTrySleepServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消（开发者传入） |

### ProjectileDoHitEffectEvent {#projectiledohiteffectevent}

触发时机：当抛射物碰撞时触发该事件

信号：[world.beforeEvents.projectileDoHitEffect](events/beforeEvents.md#projectileDoHitEffect)。分类：实体。

参数类型：[WorldProjectileDoHitEffectBeforeEvent](reference/WorldProjectileDoHitEffectBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ProjectileDoHitEffectEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 抛射物id |
| `hitTargetType` | `hitTargetType` | [str](../common/type-system.md#str) | 只读 | 碰撞目标类型,'ENTITY'或是'BLOCK' |
| `target` | `targetId` | [str](../common/type-system.md#str) | 只读 | 碰撞目标id |
| `hitFace` | `hitFace` | [int](../common/type-system.md#int) | 只读 | 撞击在方块上的面id，参考Facing枚举 |
| `x` | `x` | [float](../common/type-system.md#float) | 只读 | 碰撞x坐标 |
| `y` | `y` | [float](../common/type-system.md#float) | 只读 | 碰撞y坐标 |
| `z` | `z` | [float](../common/type-system.md#float) | 只读 | 碰撞z坐标 |
| `blockPosX` | `blockPosX` | [int](../common/type-system.md#int) | 只读 | 碰撞是方块时，方块x坐标 |
| `blockPosY` | `blockPosY` | [int](../common/type-system.md#int) | 只读 | 碰撞是方块时，方块y坐标 |
| `blockPosZ` | `blockPosZ` | [int](../common/type-system.md#int) | 只读 | 碰撞是方块时，方块z坐标 |
| `source` | `srcId` | [str](../common/type-system.md#str) | 只读 | 创建者id |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消这个碰撞事件，若取消可以设置为True |

### ShearsDestoryBlockBeforeServerEvent {#shearsdestoryblockbeforeserverevent}

触发时机：玩家手持剪刀破坏方块时，有剪刀特殊效果的方块会在服务端线程触发该事件

信号：[world.beforeEvents.shearsDestroyBlock](events/beforeEvents.md#shearsDestroyBlock)。分类：方块。

参数类型：[WorldShearsDestroyBlockBeforeEvent](reference/WorldShearsDestroyBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ShearsDestoryBlockBeforeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 方块位置x |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 方块位置y |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 方块位置z |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxData` | `auxData` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |
| `dropName` | `dropName` | [str](../common/type-system.md#str) | 只读 | 触发剪刀效果的掉落物identifier，包含命名空间及名称 |
| `dropCount` | `dropCount` | [int](../common/type-system.md#int) | 只读 | 触发剪刀效果的掉落物数量 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 触发剪刀效果的玩家id |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 玩家触发时的维度id |
| `cancelShears` | `cancelShears` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消剪刀效果 |

**原生前提与限制：**

- 该事件触发在ServerPlayerTryDestroyBlockEvent之后，如果在ServerPlayerTryDestroyBlockEvent事件中设置了取消Destory或取消掉落物会导致该事件不触发
  - 取消剪刀效果后不掉落任何东西的方块类型：蜘蛛网、枯萎的灌木、草丛、下界苗、树叶、海草、藤蔓
  - 绊线取消剪刀效果需要配合ShearsDestoryBlockBeforeClientEvent同时使用，否则在表现上可能展现出来的还是剪刀剪断后的效果。绊线取消剪刀效果后依然会掉落成线。

### ShearsUseToBlockBeforeServerEvent {#shearsusetoblockbeforeserverevent}

触发时机：实体手持剪刀对方块使用时，有剪刀特殊效果的方块会在服务端线程触发该事件

信号：[world.beforeEvents.shearsUseToBlock](events/beforeEvents.md#shearsUseToBlock)。分类：物品。

参数类型：[WorldShearsUseToBlockBeforeEvent](reference/WorldShearsUseToBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("ShearsUseToBlockBeforeServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 方块位置x |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 方块位置y |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 方块位置z |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxData` | `auxData` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |
| `dropName` | `dropName` | [str](../common/type-system.md#str) | 只读 | 触发剪刀效果的掉落物identifier，包含命名空间及名称 |
| `dropCount` | `dropCount` | [int](../common/type-system.md#int) | 只读 | 触发剪刀效果的掉落物数量 |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 触发剪刀效果的实体id，目前仅玩家会触发 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 玩家触发时的维度id |
| `cancelShears` | `cancelShears` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消剪刀效果 |

**原生前提与限制：**

- 目前会触发该事件的方块：南瓜、蜂巢
  - 该事件触发在ServerItemUseOnEvent之后，如果ServerItemUseOnEvent中取消了物品使用，该事件无法被触发
  - 和ServerItemUseOnEvent一样该事件判定在tick执行，意味着如果取消剪刀效果该事件可能会多次触发（取决于玩家按下使用键时长）

### OnStandOnBlockServerEvent {#onstandonblockserverevent}

触发时机：当实体站立到方块上时服务端持续触发

信号：[world.beforeEvents.standOnBlock](events/beforeEvents.md#standOnBlock)。分类：方块。

参数类型：[WorldStandOnBlockBeforeEvent](reference/WorldStandOnBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("OnStandOnBlockServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 实体所在维度id |
| `posX` | `posX` | [float](../common/type-system.md#float) | 只读 | 实体位置x |
| `posY` | `posY` | [float](../common/type-system.md#float) | 只读 | 实体位置y |
| `posZ` | `posZ` | [float](../common/type-system.md#float) | 只读 | 实体位置z |
| `motionX` | `motionX` | [float](../common/type-system.md#float) | 同步回调中 | 瞬时移动X方向的力 |
| `motionY` | `motionY` | [float](../common/type-system.md#float) | 同步回调中 | 瞬时移动Y方向的力 |
| `motionZ` | `motionZ` | [float](../common/type-system.md#float) | 同步回调中 | 瞬时移动Z方向的力 |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 方块位置x |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 方块位置y |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 方块位置z |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 可由脚本层回传True给引擎，阻止触发后续原版逻辑 |

**原生前提与限制：**

- 不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义方块JSON组件）
    ，原版方块需要先通过RegisterOnStandOn接口注册才能触发
  - 如果需要修改motion/cancel，强烈建议配合客户端事件同步修改，避免出现客户端表现不一致等现象
  - 如果要在脚本层修改motion，回传的一定要是浮点型，例如需要赋值0.0而不是0

### StartDestroyBlockServerEvent {#startdestroyblockserverevent}

玩家开始挖方块时触发。创造模式下不触发。

信号：[world.beforeEvents.startDestroyBlock](events/beforeEvents.md#startDestroyBlock)。分类：方块。

参数类型：[WorldStartDestroyBlockBeforeEvent](reference/WorldStartDestroyBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("StartDestroyBlockServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `pos` | `pos` | [tuple](../common/type-system.md#tuple)([float](../common/type-system.md#float),[float](../common/type-system.md#float),[float](../common/type-system.md#float)) | 只读 | 方块的坐标 |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxValue` | `auxValue` | [int](../common/type-system.md#int) | 只读 | 方块的附加值 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 修改为True时，可阻止玩家进入挖方块的状态。需要与StartDestroyBlockClientEvent一起修改。 |
| `face` | `face` | [int](../common/type-system.md#int) | 只读 | 方块被敲击面,参考Facing枚举 |

**原生前提与限制：**

- 如果是隔着火焰挖方块，即使将该事件cancel掉，火焰也会被扑灭。如果要阻止火焰扑灭，需要配合ExtinguishFireServerEvent使用
  - 该服务端事件触发于服务端收到玩家破坏操作时，当方块为秒破方块时（破坏方块所需时间为0或未设置破坏时间），ServerPlayerTryDestroyBlockEvent事件触发在本事件之前;当方块为非秒破方块时，ServerPlayerTryDestroyBlockEvent事件触发在本事件之后。
  - 秒破方块在本事件触发前已经被服务端删除，此时本事件获取到的blockName为minecraft:air，且无法通过本事件进行取消操作,以下是两个解决方法：
    （1）用ServerPlayerTryDestroyBlockEvent获取到正确的方块信息或取消操作。
    （2）通过minecraft:destroy_time方块组件来修改方块的破坏时间。

### StartRidingServerEvent {#startridingserverevent}

触发时机：一个实体即将骑乘另外一个实体

信号：[world.beforeEvents.startRiding](events/beforeEvents.md#startRiding)。分类：实体。

参数类型：[WorldStartRidingBeforeEvent](reference/WorldStartRidingBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("StartRidingServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否允许触发，默认为False，若设为True，可阻止触发后续的实体交互事件 |
| `rider` | `actorId` | [str](../common/type-system.md#str) | 只读 | 骑乘者的唯一ID |
| `target` | `victimId` | [str](../common/type-system.md#str) | 只读 | 被骑乘实体的唯一ID |

### StepOnBlockServerEvent {#steponblockserverevent}

触发时机：实体刚移动至一个新实心方块时触发。

信号：[world.beforeEvents.stepOnBlock](events/beforeEvents.md#stepOnBlock)。分类：方块。

参数类型：[WorldStepOnBlockBeforeEvent](reference/WorldStepOnBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("StepOnBlockServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否允许触发，默认为False，若设为True，可阻止触发后续物理交互事件 |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 触发的entity的唯一ID |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |

**原生前提与限制：**

- 在合并微软更新之后，本事件触发时机与微软molang实验性玩法组件"minecraft:on_step_on"一致
  - 压力板与绊线钩在过去的版本的事件是可以触发的，但在更新后这种非实心方块并不会触发，有需要的可以使用OnEntityInsideBlockServerEvent事件。
  - 不是所有方块都会触发该事件，自定义方块需要在json中先配置触发开关（详情参考：自定义方块JSON组件），
    原版方块需要先通过RegisterOnStepOn接口注册才能触发。原版的红石矿默认注册了，但深层红石矿没有默认注册。
  - 如果需要修改cancel，强烈建议配合客户端事件同步修改，避免出现客户端表现不一致等非预期现象。

### WillTeleportToServerEvent {#willteleporttoserverevent}

实体即将传送或切换维度

信号：[world.beforeEvents.willTeleportTo](events/beforeEvents.md#willTeleportTo)。分类：实体。

参数类型：[WorldWillTeleportToBeforeEvent](reference/WorldWillTeleportToBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`world.beforeEvents.getNativeEvent("WillTeleportToServerEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否允许触发，默认为False，若设为True，可阻止触发后续的传送 |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体的唯一ID |
| `fromDimension` | `fromDimensionId` | [int](../common/type-system.md#int) | 只读 | 传送前所在的维度 |
| `toDimension` | `toDimensionId` | [int](../common/type-system.md#int) | 只读 | 传送后的目标维度 |
| `fromX` | `fromX` | [int](../common/type-system.md#int) | 只读 | 传送前所在的x坐标 |
| `fromY` | `fromY` | [int](../common/type-system.md#int) | 只读 | 传送前所在的y坐标 |
| `fromZ` | `fromZ` | [int](../common/type-system.md#int) | 只读 | 传送前所在的z坐标 |
| `toX` | `toX` | [int](../common/type-system.md#int) | 只读 | 传送目标地点的x坐标 |
| `toY` | `toY` | [int](../common/type-system.md#int) | 只读 | 传送目标地点的y坐标 |
| `toZ` | `toZ` | [int](../common/type-system.md#int) | 只读 | 传送目标地点的z坐标 |
| `cause` | `cause` | [str](../common/type-system.md#str) | 只读 | 传送理由，详情见MinecraftEnum.EntityTeleportCause |

**原生前提与限制：**

- 假如目标维度尚未在内存中创建（即服务器启动之后，到传送之前，没有玩家进入过这个维度），那么此时事件中返回的目标地点坐标是算法生成的，不能保证正确。