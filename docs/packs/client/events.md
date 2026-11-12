---
sidebar_position: 3
title: 客户端原生事件目录
---

# 客户端原生事件目录

本目录逐项对应 ModSDK 文档事件索引，包含 **120 个事件绑定**。

属性名称采用 lowerCamelCase；保留准确的原生事件名用于检索。前置或可写引擎钩子放在 `beforeEvents`，通知放在 `afterEvents`。原生名称带 After 的钩子仍可能在后续力学计算前接收可写输出，按字段契约归入 before。

每项都提供独立类型、订阅示例、字段说明和原生前提。索引覆盖不意味着所有网易引擎版本、平台或资源配置都会触发这些事件。

**常用业务优先使用 [语义化事件与筛选](../guides/semantic-events.md)**：多个原生事件可以合并为统一入口，一个原生事件也可以拆成多个有明确用途的信号。下面保留准确的原生契约用于高级场景。

[原生用法、取消语义与错误处理](../guides/native-events.md)

## 全部事件

| 原生事件 | 信号属性 | 可写输出 | 平台 |
| --- | --- | --- | --- |
| [AchievementButtonMovedClientEvent](#achievementbuttonmovedclientevent) | [client.afterEvents.achievementButtonMoved](reference/ClientAfterEvents.md#achievementButtonMoved) | 无 | ModSDK |
| [ActorAcquiredItemClientEvent](#actoracquireditemclientevent) | [client.afterEvents.actorAcquiredItem](reference/ClientAfterEvents.md#actorAcquiredItem) | 无 | ModSDK |
| [ActorUseItemClientEvent](#actoruseitemclientevent) | [client.afterEvents.actorUseItem](reference/ClientAfterEvents.md#actorUseItem) | 无 | ModSDK |
| [AnvilCreateResultItemAfterClientEvent](#anvilcreateresultitemafterclientevent) | [client.afterEvents.anvilCreateResultItem](reference/ClientAfterEvents.md#anvilCreateResultItem) | 无 | ModSDK |
| [ApproachEntityClientEvent](#approachentityclientevent) | [client.afterEvents.approachEntity](reference/ClientAfterEvents.md#approachEntity) | 无 | ModSDK |
| [AttackAnimBeginClientEvent](#attackanimbeginclientevent) | [client.afterEvents.attackAnimBegin](reference/ClientAfterEvents.md#attackAnimBegin) | 无 | ModSDK |
| [AttackAnimEndClientEvent](#attackanimendclientevent) | [client.afterEvents.attackAnimEnd](reference/ClientAfterEvents.md#attackAnimEnd) | 无 | ModSDK |
| [OnBackButtonReleaseClientEvent](#onbackbuttonreleaseclientevent) | [client.afterEvents.backButtonRelease](reference/ClientAfterEvents.md#backButtonRelease) | 无 | ModSDK |
| [BlockAnimateRandomTickEvent](#blockanimaterandomtickevent) | [client.afterEvents.blockAnimateRandomTick](reference/ClientAfterEvents.md#blockAnimateRandomTick) | 无 | ModSDK |
| [CameraMotionStartClientEvent](#cameramotionstartclientevent) | [client.afterEvents.cameraMotionStart](reference/ClientAfterEvents.md#cameraMotionStart) | 无 | ModSDK |
| [ClientChestCloseEvent](#clientchestcloseevent) | [client.afterEvents.chestClose](reference/ClientAfterEvents.md#chestClose) | 无 | ModSDK |
| [ClientChestOpenEvent](#clientchestopenevent) | [client.afterEvents.chestOpen](reference/ClientAfterEvents.md#chestOpen) | 无 | ModSDK |
| [ChunkLoadedClientEvent](#chunkloadedclientevent) | [client.afterEvents.chunkLoad](reference/ClientAfterEvents.md#chunkLoad) | 无 | ModSDK |
| [CloseNeteaseShopEvent](#closeneteaseshopevent) | [client.afterEvents.closeNeteaseShop](reference/ClientAfterEvents.md#closeNeteaseShop) | 无 | ModSDK |
| [OnCommandOutputClientEvent](#oncommandoutputclientevent) | [client.afterEvents.commandOutput](reference/ClientAfterEvents.md#commandOutput) | 无 | ModSDK |
| [CraftUpdateResultItemClientEvent](#craftupdateresultitemclientevent) | [client.afterEvents.craftUpdateResultItem](reference/ClientAfterEvents.md#craftUpdateResultItem) | 无 | ModSDK |
| [OnCustomGamepadChangedEvent](#oncustomgamepadchangedevent) | [client.afterEvents.customGamepadChange](reference/ClientAfterEvents.md#customGamepadChange) | 无 | ModSDK |
| [OnCustomGamepadPressInGame](#oncustomgamepadpressingame) | `client.afterEvents.getNativeEvent('OnCustomGamepadPressInGame')` | 无 | ModSDK |
| [OnCustomKeyChangedEvent](#oncustomkeychangedevent) | [client.afterEvents.customKeyChange](reference/ClientAfterEvents.md#customKeyChange) | 无 | ModSDK |
| [OnCustomKeyPressInGame](#oncustomkeypressingame) | `client.afterEvents.getNativeEvent('OnCustomKeyPressInGame')` | 无 | ModSDK |
| [AddEntityClientEvent](#addentityclientevent) | `client.afterEvents.getNativeEvent('AddEntityClientEvent')` | 无 | ModSDK |
| [OnMobHitMobClientEvent](#onmobhitmobclientevent) | [client.afterEvents.entityCollide](reference/ClientAfterEvents.md#entityCollide) | 无 | ModSDK |
| [HealthChangeClientEvent](#healthchangeclientevent) | [client.afterEvents.entityHealthChanged](reference/ClientAfterEvents.md#entityHealthChanged) | 无 | ModSDK |
| [OnGroundClientEvent](#ongroundclientevent) | [client.afterEvents.entityLand](reference/ClientAfterEvents.md#entityLand) | 无 | ModSDK |
| [EntityModelChangedClientEvent](#entitymodelchangedclientevent) | [client.afterEvents.entityModelChange](reference/ClientAfterEvents.md#entityModelChange) | 无 | ModSDK |
| [RemoveEntityClientEvent](#removeentityclientevent) | `client.afterEvents.getNativeEvent('RemoveEntityClientEvent')` | 无 | ModSDK |
| [GameTypeChangedClientEvent](#gametypechangedclientevent) | [client.afterEvents.gameTypeChange](reference/ClientAfterEvents.md#gameTypeChange) | 无 | ModSDK |
| [OnGamepadControllerLayoutChangeClientEvent](#ongamepadcontrollerlayoutchangeclientevent) | [client.afterEvents.gamepadControllerLayoutChange](reference/ClientAfterEvents.md#gamepadControllerLayoutChange) | 无 | ModSDK |
| [OnGamepadKeyPressClientEvent](#ongamepadkeypressclientevent) | `client.afterEvents.getNativeEvent('OnGamepadKeyPressClientEvent')` | 无 | ModSDK |
| [OnGamepadStickClientEvent](#ongamepadstickclientevent) | `client.afterEvents.getNativeEvent('OnGamepadStickClientEvent')` | 无 | ModSDK |
| [OnGamepadTriggerClientEvent](#ongamepadtriggerclientevent) | `client.afterEvents.getNativeEvent('OnGamepadTriggerClientEvent')` | 无 | ModSDK |
| [GetEntityByCoordEvent](#getentitybycoordevent) | [client.afterEvents.getEntityByCoord](reference/ClientAfterEvents.md#getEntityByCoord) | 无 | ModSDK |
| [GetEntityByCoordReleaseClientEvent](#getentitybycoordreleaseclientevent) | [client.afterEvents.getEntityByCoordRelease](reference/ClientAfterEvents.md#getEntityByCoordRelease) | 无 | ModSDK |
| [GridComponentSizeChangedClientEvent](#gridcomponentsizechangedclientevent) | [client.afterEvents.gridComponentSizeChange](reference/ClientAfterEvents.md#gridComponentSizeChange) | 无 | ModSDK |
| [GrindStoneRemovedEnchantClientEvent](#grindstoneremovedenchantclientevent) | [client.afterEvents.grindStoneRemoveEnchant](reference/ClientAfterEvents.md#grindStoneRemoveEnchant) | 无 | ModSDK |
| [GyroSensorChangedClientEvent](#gyrosensorchangedclientevent) | [client.afterEvents.gyroSensorChange](reference/ClientAfterEvents.md#gyroSensorChange) | 无 | ModSDK |
| [HudButtonChangedClientEvent](#hudbuttonchangedclientevent) | [client.afterEvents.hudButtonChange](reference/ClientAfterEvents.md#hudButtonChange) | 无 | ModSDK |
| [ClientPlayerInventoryCloseEvent](#clientplayerinventorycloseevent) | [client.afterEvents.inventoryClose](reference/ClientAfterEvents.md#inventoryClose) | 无 | ModSDK |
| [OnItemSlotButtonClickedEvent](#onitemslotbuttonclickedevent) | [client.afterEvents.itemSlotButtonClicked](reference/ClientAfterEvents.md#itemSlotButtonClicked) | 无 | ModSDK |
| [ClientJumpButtonReleaseEvent](#clientjumpbuttonreleaseevent) | [client.afterEvents.jumpButtonRelease](reference/ClientAfterEvents.md#jumpButtonRelease) | 无 | ModSDK |
| [OnKeyboardControllerLayoutChangeClientEvent](#onkeyboardcontrollerlayoutchangeclientevent) | [client.afterEvents.keyboardControllerLayoutChange](reference/ClientAfterEvents.md#keyboardControllerLayoutChange) | 无 | ModSDK |
| [LeaveEntityClientEvent](#leaveentityclientevent) | [client.afterEvents.leaveEntity](reference/ClientAfterEvents.md#leaveEntity) | 无 | ModSDK |
| [LeftClickReleaseClientEvent](#leftclickreleaseclientevent) | `client.afterEvents.getNativeEvent('LeftClickReleaseClientEvent')` | 无 | ModSDK |
| [LiquidClippedClientEvent](#liquidclippedclientevent) | [client.afterEvents.liquidClipped](reference/ClientAfterEvents.md#liquidClipped) | 无 | ModSDK |
| [OnLocalPlayerStopLoading](#onlocalplayerstoploading) | [client.afterEvents.localPlayerLoad](reference/ClientAfterEvents.md#localPlayerLoad) | 无 | ModSDK |
| [ModBlockEntityLoadedClientEvent](#modblockentityloadedclientevent) | [client.afterEvents.modBlockEntityLoad](reference/ClientAfterEvents.md#modBlockEntityLoad) | 无 | ModSDK |
| [ModBlockEntityRemoveClientEvent](#modblockentityremoveclientevent) | [client.afterEvents.modBlockEntityRemove](reference/ClientAfterEvents.md#modBlockEntityRemove) | 无 | ModSDK |
| [ModBlockEntityTickClientEvent](#modblockentitytickclientevent) | [client.afterEvents.modBlockEntityTick](reference/ClientAfterEvents.md#modBlockEntityTick) | 无 | ModSDK |
| [OnModBlockNeteaseEffectCreatedClientEvent](#onmodblockneteaseeffectcreatedclientevent) | [client.afterEvents.modBlockNeteaseEffectCreate](reference/ClientAfterEvents.md#modBlockNeteaseEffectCreate) | 无 | ModSDK |
| [OnMouseMiddleDownClientEvent](#onmousemiddledownclientevent) | `client.afterEvents.getNativeEvent('OnMouseMiddleDownClientEvent')` | 无 | ModSDK |
| [OnKeyPressInGame](#onkeypressingame) | `client.afterEvents.getNativeEvent('OnKeyPressInGame')` | 无 | ModSDK |
| [MouseWheelClientEvent](#mousewheelclientevent) | `client.afterEvents.getNativeEvent('MouseWheelClientEvent')` | 无 | ModSDK |
| [OnMusicStopClientEvent](#onmusicstopclientevent) | `client.afterEvents.getNativeEvent('OnMusicStopClientEvent')` | 无 | ModSDK |
| [PerspChangeClientEvent](#perspchangeclientevent) | [client.afterEvents.perspectiveChange](reference/ClientAfterEvents.md#perspectiveChange) | 无 | ModSDK |
| [PhysxTouchClientEvent](#physxtouchclientevent) | `client.afterEvents.getNativeEvent('PhysxTouchClientEvent')` | 无 | ModSDK |
| [PhysxTriggerClientEvent](#physxtriggerclientevent) | `client.afterEvents.getNativeEvent('PhysxTriggerClientEvent')` | 无 | ModSDK |
| [OnLocalPlayerActionClientEvent](#onlocalplayeractionclientevent) | `client.afterEvents.getNativeEvent('OnLocalPlayerActionClientEvent')` | 无 | ModSDK |
| [PlayerAddCustomContainerItemClientEvent](#playeraddcustomcontaineritemclientevent) | [client.afterEvents.playerAddCustomContainerItem](reference/ClientAfterEvents.md#playerAddCustomContainerItem) | 无 | ModSDK |
| [PlayerAttackEntityEvent](#playerattackentityevent) | [client.afterEvents.playerAttackEntity](reference/ClientAfterEvents.md#playerAttackEntity) | 无 | ModSDK |
| [PlayerChatButtonClickClientEvent](#playerchatbuttonclickclientevent) | [client.afterEvents.playerChatButtonClick](reference/ClientAfterEvents.md#playerChatButtonClick) | 无 | ModSDK |
| [DimensionChangeClientEvent](#dimensionchangeclientevent) | [client.afterEvents.playerDimensionChange](reference/ClientAfterEvents.md#playerDimensionChange) | 无 | ModSDK |
| [DimensionChangeFinishClientEvent](#dimensionchangefinishclientevent) | [client.afterEvents.playerDimensionChangeFinish](reference/ClientAfterEvents.md#playerDimensionChangeFinish) | 无 | ModSDK |
| [AddPlayerAOIClientEvent](#addplayeraoiclientevent) | [client.afterEvents.playerEnteredView](reference/ClientAfterEvents.md#playerEnteredView) | 无 | ModSDK |
| [OnPlayerHitBlockClientEvent](#onplayerhitblockclientevent) | [client.afterEvents.playerHitBlock](reference/ClientAfterEvents.md#playerHitBlock) | 无 | ModSDK |
| [OnCarriedNewItemChangedClientEvent](#oncarriednewitemchangedclientevent) | `client.afterEvents.getNativeEvent('OnCarriedNewItemChangedClientEvent')` | 无 | ModSDK |
| [InventoryItemChangedClientEvent](#inventoryitemchangedclientevent) | `client.afterEvents.getNativeEvent('InventoryItemChangedClientEvent')` | 无 | ModSDK |
| [OnLocalPlayerStartJumpClientEvent](#onlocalplayerstartjumpclientevent) | [client.afterEvents.playerJump](reference/ClientAfterEvents.md#playerJump) | 无 | ModSDK |
| [RemovePlayerAOIClientEvent](#removeplayeraoiclientevent) | `client.afterEvents.getNativeEvent('RemovePlayerAOIClientEvent')` | 无 | ModSDK |
| [PlayerPermissionChangeClientEvent](#playerpermissionchangeclientevent) | [client.afterEvents.playerPermissionChange](reference/ClientAfterEvents.md#playerPermissionChange) | 无 | ModSDK |
| [PlayerRemoveCustomContainerItemClientEvent](#playerremovecustomcontaineritemclientevent) | [client.afterEvents.playerRemoveCustomContainerItem](reference/ClientAfterEvents.md#playerRemoveCustomContainerItem) | 无 | ModSDK |
| [AddPlayerCreatedClientEvent](#addplayercreatedclientevent) | `client.afterEvents.getNativeEvent('AddPlayerCreatedClientEvent')` | 无 | ModSDK |
| [OnClientPlayerStartMove](#onclientplayerstartmove) | [client.afterEvents.playerStartMove](reference/ClientAfterEvents.md#playerStartMove) | 无 | ModSDK |
| [OnClientPlayerStopMove](#onclientplayerstopmove) | [client.afterEvents.playerStopMove](reference/ClientAfterEvents.md#playerStopMove) | 无 | ModSDK |
| [PopScreenAfterClientEvent](#popscreenafterclientevent) | `client.afterEvents.getNativeEvent('PopScreenAfterClientEvent')` | 无 | ModSDK |
| [PushScreenEvent](#pushscreenevent) | `client.afterEvents.getNativeEvent('PushScreenEvent')` | 无 | ModSDK |
| [ClientShapedRecipeTriggeredEvent](#clientshapedrecipetriggeredevent) | [client.afterEvents.recipeTrigger](reference/ClientAfterEvents.md#recipeTrigger) | 无 | ModSDK |
| [GameRenderTickEvent](#gamerendertickevent) | [client.afterEvents.render](reference/ClientAfterEvents.md#render) | 无 | ModSDK |
| [RightClickReleaseClientEvent](#rightclickreleaseclientevent) | `client.afterEvents.getNativeEvent('RightClickReleaseClientEvent')` | 无 | ModSDK |
| [ScreenSizeChangedClientEvent](#screensizechangedclientevent) | [client.afterEvents.screenSizeChange](reference/ClientAfterEvents.md#screenSizeChange) | 无 | ModSDK |
| [LoadClientAddonScriptsAfter](#loadclientaddonscriptsafter) | [client.afterEvents.scriptsLoad](reference/ClientAfterEvents.md#scriptsLoad) | 无 | ModSDK |
| [StartRidingClientEvent](#startridingclientevent) | [client.afterEvents.startRiding](reference/ClientAfterEvents.md#startRiding) | 无 | ModSDK |
| [StartUsingItemClientEvent](#startusingitemclientevent) | [client.afterEvents.startUsingItem](reference/ClientAfterEvents.md#startUsingItem) | 无 | ModSDK |
| [StepOffBlockClientEvent](#stepoffblockclientevent) | [client.afterEvents.stepOffBlock](reference/ClientAfterEvents.md#stepOffBlock) | 无 | ModSDK |
| [StopUsingItemClientEvent](#stopusingitemclientevent) | [client.afterEvents.stopUsingItem](reference/ClientAfterEvents.md#stopUsingItem) | 无 | ModSDK |
| [TapOrHoldReleaseClientEvent](#taporholdreleaseclientevent) | `client.afterEvents.getNativeEvent('TapOrHoldReleaseClientEvent')` | 无 | ModSDK |
| [OnScriptTickClient](#onscripttickclient) | [client.afterEvents.tick](reference/ClientAfterEvents.md#tick) | 无 | ModSDK |
| [UiInitFinished](#uiinitfinished) | `client.afterEvents.getNativeEvent('UiInitFinished')` | 无 | ModSDK |
| [UpdatePlayerSkinClientEvent](#updateplayerskinclientevent) | [client.afterEvents.updatePlayerSkin](reference/ClientAfterEvents.md#updatePlayerSkin) | 无 | ModSDK |
| [WalkAnimBeginClientEvent](#walkanimbeginclientevent) | [client.afterEvents.walkAnimBegin](reference/ClientAfterEvents.md#walkAnimBegin) | 无 | ModSDK |
| [WalkAnimEndClientEvent](#walkanimendclientevent) | [client.afterEvents.walkAnimEnd](reference/ClientAfterEvents.md#walkAnimEnd) | 无 | ModSDK |
| [ClientBlockUseEvent](#clientblockuseevent) | `client.beforeEvents.getNativeEvent('ClientBlockUseEvent')` | cancel | ModSDK |
| [CameraMotionStopClientEvent](#cameramotionstopclientevent) | [client.beforeEvents.cameraMotionStop](reference/ClientBeforeEvents.md#cameraMotionStop) | remove | ModSDK |
| [ChunkAcquireDiscardedClientEvent](#chunkacquirediscardedclientevent) | [client.beforeEvents.chunkUnload](reference/ClientBeforeEvents.md#chunkUnload) | 无 | ModSDK |
| [OnEntityInsideBlockClientEvent](#onentityinsideblockclientevent) | [client.beforeEvents.entityInsideBlock](reference/ClientBeforeEvents.md#entityInsideBlock) | cancel, slowdownMultiX, slowdownMultiY, slowdownMultiZ | ModSDK |
| [EntityStopRidingEvent](#entitystopridingevent) | [client.beforeEvents.entityStopRiding](reference/ClientBeforeEvents.md#entityStopRiding) | cancel | ModSDK |
| [ExtinguishFireClientEvent](#extinguishfireclientevent) | [client.beforeEvents.extinguishFire](reference/ClientBeforeEvents.md#extinguishFire) | cancel | ModSDK |
| [OnAfterFallOnBlockClientEvent](#onafterfallonblockclientevent) | [client.beforeEvents.fallOnBlockMotion](reference/ClientBeforeEvents.md#fallOnBlockMotion) | calculate, motionX, motionY, motionZ | ModSDK |
| [FallingBlockCauseDamageBeforeClientEvent](#fallingblockcausedamagebeforeclientevent) | [client.beforeEvents.fallingBlockCauseDamage](reference/ClientBeforeEvents.md#fallingBlockCauseDamage) | 无 | ModSDK |
| [HoldBeforeClientEvent](#holdbeforeclientevent) | `client.beforeEvents.getNativeEvent('HoldBeforeClientEvent')` | cancel | ModSDK |
| [ClientPlayerInventoryOpenEvent](#clientplayerinventoryopenevent) | [client.beforeEvents.inventoryOpen](reference/ClientBeforeEvents.md#inventoryOpen) | cancel | ModSDK |
| [ItemReleaseUsingClientEvent](#itemreleaseusingclientevent) | [client.beforeEvents.itemReleaseUsing](reference/ClientBeforeEvents.md#itemReleaseUsing) | cancel | ModSDK |
| [ClientItemTryUseEvent](#clientitemtryuseevent) | `client.beforeEvents.getNativeEvent('ClientItemTryUseEvent')` | cancel | ModSDK |
| [ClientItemUseOnEvent](#clientitemuseonevent) | `client.beforeEvents.getNativeEvent('ClientItemUseOnEvent')` | ret；cancel 映射 ret | ModSDK |
| [ClientJumpButtonPressDownEvent](#clientjumpbuttonpressdownevent) | [client.beforeEvents.jumpButtonPress](reference/ClientBeforeEvents.md#jumpButtonPress) | continueJump；cancel 映射 反转 continueJump | ModSDK |
| [LeftClickBeforeClientEvent](#leftclickbeforeclientevent) | `client.beforeEvents.getNativeEvent('LeftClickBeforeClientEvent')` | cancel | ModSDK |
| [PlayMusicClientEvent](#playmusicclientevent) | [client.beforeEvents.playMusic](reference/ClientBeforeEvents.md#playMusic) | cancel | ModSDK |
| [PlaySoundClientEvent](#playsoundclientevent) | [client.beforeEvents.playSound](reference/ClientBeforeEvents.md#playSound) | cancel | ModSDK |
| [PlayerTryDestroyBlockClientEvent](#playertrydestroyblockclientevent) | [client.beforeEvents.playerBreakBlock](reference/ClientBeforeEvents.md#playerBreakBlock) | cancel | ModSDK |
| [PlayerTryAddCustomContainerItemClientEvent](#playertryaddcustomcontaineritemclientevent) | [client.beforeEvents.playerTryAddCustomContainerItem](reference/ClientBeforeEvents.md#playerTryAddCustomContainerItem) | cancel | ModSDK |
| [PlayerTryDropItemClientEvent](#playertrydropitemclientevent) | [client.beforeEvents.playerTryDropItem](reference/ClientBeforeEvents.md#playerTryDropItem) | cancel | ModSDK |
| [PlayerTryPutCustomContainerItemClientEvent](#playertryputcustomcontaineritemclientevent) | [client.beforeEvents.playerTryPutCustomContainerItem](reference/ClientBeforeEvents.md#playerTryPutCustomContainerItem) | cancel | ModSDK |
| [PlayerTryRemoveCustomContainerItemClientEvent](#playertryremovecustomcontaineritemclientevent) | [client.beforeEvents.playerTryRemoveCustomContainerItem](reference/ClientBeforeEvents.md#playerTryRemoveCustomContainerItem) | cancel | ModSDK |
| [PopScreenEvent](#popscreenevent) | `client.beforeEvents.getNativeEvent('PopScreenEvent')` | 无 | ModSDK |
| [RightClickBeforeClientEvent](#rightclickbeforeclientevent) | `client.beforeEvents.getNativeEvent('RightClickBeforeClientEvent')` | cancel | ModSDK |
| [UnLoadClientAddonScriptsBefore](#unloadclientaddonscriptsbefore) | [client.beforeEvents.scriptsUnload](reference/ClientBeforeEvents.md#scriptsUnload) | 无 | ModSDK |
| [ShearsDestoryBlockBeforeClientEvent](#shearsdestoryblockbeforeclientevent) | [client.beforeEvents.shearsDestroyBlock](reference/ClientBeforeEvents.md#shearsDestroyBlock) | cancelShears | ModSDK |
| [OnStandOnBlockClientEvent](#onstandonblockclientevent) | [client.beforeEvents.standOnBlock](reference/ClientBeforeEvents.md#standOnBlock) | cancel, motionX, motionY, motionZ | ModSDK |
| [StartDestroyBlockClientEvent](#startdestroyblockclientevent) | [client.beforeEvents.startDestroyBlock](reference/ClientBeforeEvents.md#startDestroyBlock) | cancel | ModSDK |
| [StepOnBlockClientEvent](#steponblockclientevent) | [client.beforeEvents.stepOnBlock](reference/ClientBeforeEvents.md#stepOnBlock) | cancel | ModSDK |
| [TapBeforeClientEvent](#tapbeforeclientevent) | `client.beforeEvents.getNativeEvent('TapBeforeClientEvent')` | cancel | ModSDK |

## 逐项契约

### AchievementButtonMovedClientEvent {#achievementbuttonmovedclientevent}

触发时机：使用自定义成就系统的时，拖动成就入口结束时触发

信号：[client.afterEvents.achievementButtonMoved](reference/ClientAfterEvents.md#achievementButtonMoved)。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientAchievementButtonMovedAfterEvent](reference/ClientAchievementButtonMovedAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("AchievementButtonMovedClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `oldPosition` | `oldPosition` | [tuple](../common/type-system.md#tuple)([float](../common/type-system.md#float),[float](../common/type-system.md#float)) | 只读 | 移动前该控件相对父节点的坐标信息，第一项为横轴，第二项为纵轴 |
| `newPosition` | `newPosition` | [tuple](../common/type-system.md#tuple)([float](../common/type-system.md#float),[float](../common/type-system.md#float)) | 只读 | 移动后该控件相对父节点的坐标信息，第一项为横轴，第二项为纵轴 |

### ActorAcquiredItemClientEvent {#actoracquireditemclientevent}

触发时机：玩家获得物品时客户端抛出的事件（有些获取物品方式只会触发客户端事件，有些获取物品方式只会触发服务端事件，在使用时注意一点。）

信号：[client.afterEvents.actorAcquiredItem](reference/ClientAfterEvents.md#actorAcquiredItem)。分类：物品。

参数类型：[ClientActorAcquiredItemAfterEvent](reference/ClientActorAcquiredItemAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("ActorAcquiredItemClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `actor` | `actor` | [str](../common/type-system.md#str) | 只读 | 获得物品玩家实体id |
| `secondaryActor` | `secondaryActor` | [str](../common/type-system.md#str) | 只读 | 物品给予者玩家实体id，如果不存在给予者的话，这里为空字符串 |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 获取到的物品的物品信息字典 |
| `acquireMethod` | `acquireMethod` | [int](../common/type-system.md#int) | 只读 | 获得物品的方法，详见ItemAcquisitionMethod |

### ActorUseItemClientEvent {#actoruseitemclientevent}

触发时机：玩家使用物品时客户端抛出的事件（比较特殊不走该事件的例子：1）染料对有水的炼药锅使用；2）盔甲架装备盔甲）;3)喝牛奶

信号：[client.afterEvents.actorUseItem](reference/ClientAfterEvents.md#actorUseItem)。分类：物品。

参数类型：[ClientActorUseItemAfterEvent](reference/ClientActorUseItemAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("ActorUseItemClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 使用的物品的物品信息字典 |
| `useMethod` | `useMethod` | [int](../common/type-system.md#int) | 只读 | 使用物品的方法，详见ItemUseMethodEnum枚举 |

**原生前提与限制：**

- 注意，喝牛奶不会触发该事件，但是会触发[ActorUseItemServerEvent](../server/native-events.md#actoruseitemserverevent)

### AnvilCreateResultItemAfterClientEvent {#anvilcreateresultitemafterclientevent}

玩家点击铁砧合成得到的物品时抛出的事件。

信号：[client.afterEvents.anvilCreateResultItem](reference/ClientAfterEvents.md#anvilCreateResultItem)。分类：物品。

参数类型：[ClientAnvilCreateResultItemAfterEvent](reference/ClientAnvilCreateResultItemAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("AnvilCreateResultItemAfterClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `itemShowName` | `itemShowName` | [str](../common/type-system.md#str) | 只读 | 合成后的物品显示名称 |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 合成后的物品的物品信息字典 |
| `oldItemDict` | `oldItemDict` | [dict](../common/type-system.md#dict) | 只读 | 合成前的物品的物品信息字典（铁砧内第一个物品） |
| `materialItemDict` | `materialItemDict` | [dict](../common/type-system.md#dict) | 只读 | 合成所使用材料的物品信息字典（铁砧内第二个物品） |

### ApproachEntityClientEvent {#approachentityclientevent}

玩家靠近生物时触发

信号：[client.afterEvents.approachEntity](reference/ClientAfterEvents.md#approachEntity)。分类：实体。

参数类型：[ClientApproachEntityAfterEvent](reference/ClientApproachEntityAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("ApproachEntityClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 靠近的生物实体id |

### AttackAnimBeginClientEvent {#attackanimbeginclientevent}

攻击动作开始时触发

信号：[client.afterEvents.attackAnimBegin](reference/ClientAfterEvents.md#attackAnimBegin)。分类：模型。

参数类型：[ClientAttackAnimBeginAfterEvent](reference/ClientAttackAnimBeginAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("AttackAnimBeginClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |

**原生前提与限制：**

- 使用SetModel替换骨骼模型后，该事件才生效

### AttackAnimEndClientEvent {#attackanimendclientevent}

攻击动作结束时触发

信号：[client.afterEvents.attackAnimEnd](reference/ClientAfterEvents.md#attackAnimEnd)。分类：模型。

参数类型：[ClientAttackAnimEndAfterEvent](reference/ClientAttackAnimEndAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("AttackAnimEndClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |

**原生前提与限制：**

- 使用SetModel替换骨骼模型后，该事件才生效

### OnBackButtonReleaseClientEvent {#onbackbuttonreleaseclientevent}

返回按钮（目前特指安卓系统导航中的返回按钮）松开时触发

信号：[client.afterEvents.backButtonRelease](reference/ClientAfterEvents.md#backButtonRelease)。分类：控制。

参数类型：[ClientBackButtonReleaseAfterEvent](reference/ClientBackButtonReleaseAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnBackButtonReleaseClientEvent")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

**原生前提与限制：**

- 目前仅安卓平台可用

### BlockAnimateRandomTickEvent {#blockanimaterandomtickevent}

触发时机：以摄像机为中心，随机选取周围的方块触发Tick，触发的数量取决于设备性能。只有添加了netease:block_animate_random_tick的自定义方块才会触发此事件

信号：[client.afterEvents.blockAnimateRandomTick](reference/ClientAfterEvents.md#blockAnimateRandomTick)。分类：方块。

参数类型：[ClientBlockAnimateRandomTickAfterEvent](reference/ClientBlockAnimateRandomTickAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("BlockAnimateRandomTickEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `blockPos` | `blockPos` | [tuple](../common/type-system.md#tuple)([float](../common/type-system.md#float),[float](../common/type-system.md#float),[float](../common/type-system.md#float)) | 只读 | 方块坐标 |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxData` | `auxData` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |

### CameraMotionStartClientEvent {#cameramotionstartclientevent}

相机运动器开始事件。相机添加运动器后，运动器开始运行时触发

信号：[client.afterEvents.cameraMotionStart](reference/ClientAfterEvents.md#cameraMotionStart)。分类：玩家。

参数类型：[ClientCameraMotionStartAfterEvent](reference/ClientCameraMotionStartAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("CameraMotionStartClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `motionId` | `motionId` | [int](../common/type-system.md#int) | 只读 | 运动器id |

### ClientChestCloseEvent {#clientchestcloseevent}

关闭箱子界面时触发，包括小箱子，合并后大箱子和末影箱(实体容器不属于方块，不会触发该事件)

信号：[client.afterEvents.chestClose](reference/ClientAfterEvents.md#chestClose)。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientChestCloseAfterEvent](reference/ClientChestCloseAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("ClientChestCloseEvent")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### ClientChestOpenEvent {#clientchestopenevent}

打开箱子界面时触发，包括小箱子，合并后大箱子和末影箱(实体容器不属于方块，不会触发该事件)

信号：[client.afterEvents.chestOpen](reference/ClientAfterEvents.md#chestOpen)。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientChestOpenAfterEvent](reference/ClientChestOpenAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("ClientChestOpenEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 箱子位置x值 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 箱子位置y值 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 箱子位置z值 |

### ChunkLoadedClientEvent {#chunkloadedclientevent}

触发时机：客户端区块加载完成时

信号：[client.afterEvents.chunkLoad](reference/ClientAfterEvents.md#chunkLoad)。分类：世界。

参数类型：[ClientChunkLoadAfterEvent](reference/ClientChunkLoadAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("ChunkLoadedClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 区块所在维度 |
| `chunkPosX` | `chunkPosX` | [int](../common/type-system.md#int) | 只读 | 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15] |
| `chunkPosZ` | `chunkPosZ` | [int](../common/type-system.md#int) | 只读 | 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15] |

### CloseNeteaseShopEvent {#closeneteaseshopevent}

关闭商城界面时触发，包括脚本商城和Apollo插件商城

信号：[client.afterEvents.closeNeteaseShop](reference/ClientAfterEvents.md#closeNeteaseShop)。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientCloseNeteaseShopAfterEvent](reference/ClientCloseNeteaseShopAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("CloseNeteaseShopEvent")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### OnCommandOutputClientEvent {#oncommandoutputclientevent}

当command命令有成功消息输出时触发

信号：[client.afterEvents.commandOutput](reference/ClientAfterEvents.md#commandOutput)。分类：世界。

参数类型：[ClientCommandOutputAfterEvent](reference/ClientCommandOutputAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnCommandOutputClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `command` | `command` | [str](../common/type-system.md#str) | 只读 | 命令名称 |
| `message` | `message` | [str](../common/type-system.md#str) | 只读 | 命令返回的消息 |

**原生前提与限制：**

- 部分命令在返回的时候没有命令名称，SetCommand接口需要showOutput参数为True时才会有返回

### CraftUpdateResultItemClientEvent {#craftupdateresultitemclientevent}

玩家工作台界面更新显示可合成物品时抛出的事件。

信号：[client.afterEvents.craftUpdateResultItem](reference/ClientAfterEvents.md#craftUpdateResultItem)。分类：物品。

参数类型：[ClientCraftUpdateResultItemAfterEvent](reference/ClientCraftUpdateResultItemAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("CraftUpdateResultItemClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 合成后的物品的[物品信息字典] |

**原生前提与限制：**

- 该事件在打开3×3工作台界面，2×2工作台界面，向工作台放入物品，预览配方时触发。
  - 如果无可合成的物品，或预览的配方因材料不足而无法合成，则传递的物品参数为 minecraft:air。

### OnCustomGamepadChangedEvent {#oncustomgamepadchangedevent}

当自定义手柄按键绑定发生改变时触发

信号：[client.afterEvents.customGamepadChange](reference/ClientAfterEvents.md#customGamepadChange)。分类：游戏设置。

参数类型：[ClientCustomGamepadChangeAfterEvent](reference/ClientCustomGamepadChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnCustomGamepadChangedEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `name` | `name` | [str](../common/type-system.md#str) | 只读 | 按键名称 |
| `oldKey` | `oldKey` | [str](../common/type-system.md#str) | 只读 | 旧的键码 |
| `newKey` | `newKey` | [str](../common/type-system.md#str) | 只读 | 新的键码 |

### OnCustomGamepadPressInGame {#oncustomgamepadpressingame}

当玩家按下自定义手柄按键时触发

信号：`client.afterEvents.getNativeEvent('OnCustomGamepadPressInGame')`。分类：游戏设置。

参数类型：[ClientCustomGamepadPressInGameAfterEvent](reference/ClientCustomGamepadPressInGameAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnCustomGamepadPressInGame")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `name` | `name` | [str](../common/type-system.md#str) | 只读 | 按键名称 |
| `key` | `key` | [str](../common/type-system.md#str) | 只读 | 键码 |
| `category` | `category` | [str](../common/type-system.md#str) | 只读 | 按键分类 |
| `isDown` | `isDown` | [str](../common/type-system.md#str) | 只读 | 按下状态 ("1"为按下, "0"为抬起)，仅普通按键有效 |
| `magnitude` | `magnitude` | [float](../common/type-system.md#float) | 只读 | 扳机力度 (0.0-1.0)，仅扳机键有效 |
| `x` | `x` | [float](../common/type-system.md#float) | 只读 | 摇杆X轴偏移 (-1.0-1.0)，仅摇杆键有效 |
| `y` | `y` | [float](../common/type-system.md#float) | 只读 | 摇杆Y轴偏移 (-1.0-1.0)，仅摇杆键有效 |
| `screenName` | `screenName` | [str](../common/type-system.md#str) | 只读 | 当前屏幕名称 |

### OnCustomKeyChangedEvent {#oncustomkeychangedevent}

当自定义按键绑定发生改变时触发

信号：[client.afterEvents.customKeyChange](reference/ClientAfterEvents.md#customKeyChange)。分类：游戏设置。

参数类型：[ClientCustomKeyChangeAfterEvent](reference/ClientCustomKeyChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnCustomKeyChangedEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `name` | `name` | [str](../common/type-system.md#str) | 只读 | 按键名称 |
| `oldKey` | `oldKey` | [str](../common/type-system.md#str) | 只读 | 旧的键码 |
| `newKey` | `newKey` | [str](../common/type-system.md#str) | 只读 | 新的键码 |

### OnCustomKeyPressInGame {#oncustomkeypressingame}

当玩家按下自定义按键时触发

信号：`client.afterEvents.getNativeEvent('OnCustomKeyPressInGame')`。分类：游戏设置。

参数类型：[ClientCustomKeyPressInGameAfterEvent](reference/ClientCustomKeyPressInGameAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnCustomKeyPressInGame")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `name` | `name` | [str](../common/type-system.md#str) | 只读 | 按键名称 |
| `key` | `key` | [str](../common/type-system.md#str) | 只读 | 键码 |
| `category` | `category` | [str](../common/type-system.md#str) | 只读 | 按键分类 |
| `isDown` | `isDown` | [str](../common/type-system.md#str) | 只读 | 按下状态 ("1"为按下, "0"为抬起) |
| `screenName` | `screenName` | [str](../common/type-system.md#str) | 只读 | 当前屏幕名称 |

### AddEntityClientEvent {#addentityclientevent}

客户端侧创建新实体时触发

信号：`client.afterEvents.getNativeEvent('AddEntityClientEvent')`。分类：世界。

参数类型：[ClientEntityAddAfterEvent](reference/ClientEntityAddAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("AddEntityClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `posX` | `posX` | [float](../common/type-system.md#float) | 只读 | 位置x |
| `posY` | `posY` | [float](../common/type-system.md#float) | 只读 | 位置y |
| `posZ` | `posZ` | [float](../common/type-system.md#float) | 只读 | 位置z |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 实体维度 |
| `isBaby` | `isBaby` | [bool](../common/type-system.md#bool) | 只读 | 是否为幼儿 |
| `engineTypeStr` | `engineTypeStr` | [str](../common/type-system.md#str) | 只读 | 实体类型 |
| `itemName` | `itemName` | [str](../common/type-system.md#str) | 只读 | 物品identifier（仅当物品实体时存在该字段） |
| `auxValue` | `auxValue` | [int](../common/type-system.md#int) | 只读 | 物品附加值（仅当物品实体时存在该字段） |

**原生前提与限制：**

- 创建玩家时不会触发该事件

### OnMobHitMobClientEvent {#onmobhitmobclientevent}

触发时机：通过OpenPlayerHitMobDetection打开生物碰撞检测后，当生物间（包含玩家）碰撞时触发该事件。注：客户端和服务端分别作碰撞检测，可能两个事件返回的略有差异。

信号：[client.afterEvents.entityCollide](reference/ClientAfterEvents.md#entityCollide)。分类：实体。

参数类型：[ClientEntityCollideAfterEvent](reference/ClientEntityCollideAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnMobHitMobClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `mobId` | [str](../common/type-system.md#str) | 只读 | 当前生物的id |
| `hittedMobList` | `hittedMobList` | [list](../common/type-system.md#list)[[str](../common/type-system.md#str)] | 只读 | 当前生物碰撞到的其他所有生物id的list |

**原生前提与限制：**

- 本事件代替原有的OnPlayerHitMobClientEvent事件
  - 监听本事件会导致客户端在实体较多时严重掉帧，建议监听服务端版本事件[OnMobHitMobServerEvent](../server/native-events.md#onmobhitmobserverevent)

### HealthChangeClientEvent {#healthchangeclientevent}

生物生命值发生变化时触发

信号：[client.afterEvents.entityHealthChanged](reference/ClientAfterEvents.md#entityHealthChanged)。分类：实体。

参数类型：[ClientEntityHealthChangedAfterEvent](reference/ClientEntityHealthChangedAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("HealthChangeClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `fromValue` | `from` | [float](../common/type-system.md#float) | 只读 | 变化前的生命值 |
| `to` | `to` | [float](../common/type-system.md#float) | 只读 | 变化后的生命值 |

### OnGroundClientEvent {#ongroundclientevent}

实体着地事件。玩家，沙子，铁砧，掉落的物品，点燃的TNT掉落地面时触发，其余实体着地不触发。

信号：[client.afterEvents.entityLand](reference/ClientAfterEvents.md#entityLand)。分类：实体。

参数类型：[ClientEntityLandAfterEvent](reference/ClientEntityLandAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnGroundClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |

**原生前提与限制：**

- 因为掉落是服务端与客户端各自计算的，对于掉落的方块，有时会出现服务端先着地，然后把FallingBlock实体移除掉了，导致客户端没触发着地事件的情况。

### EntityModelChangedClientEvent {#entitymodelchangedclientevent}

触发时机：实体模型切换时触发

信号：[client.afterEvents.entityModelChange](reference/ClientAfterEvents.md#entityModelChange)。分类：实体。

参数类型：[ClientEntityModelChangeAfterEvent](reference/ClientEntityModelChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("EntityModelChangedClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `newModel` | `newModel` | [str](../common/type-system.md#str) | 只读 | 新的模型名字 |
| `oldModel` | `oldModel` | [str](../common/type-system.md#str) | 只读 | 原来的模型名字 |

### RemoveEntityClientEvent {#removeentityclientevent}

客户端侧实体被移除时触发

信号：`client.afterEvents.getNativeEvent('RemoveEntityClientEvent')`。分类：世界。

参数类型：[ClientEntityRemoveAfterEvent](reference/ClientEntityRemoveAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("RemoveEntityClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 移除的实体id |

**原生前提与限制：**

- 客户端接收到了服务端监测实体离开玩家视野时触发，原事件名 RemoveEntityPacketEvent

### GameTypeChangedClientEvent {#gametypechangedclientevent}

个人游戏模式发生变化时客户端触发。

信号：[client.afterEvents.gameTypeChange](reference/ClientAfterEvents.md#gameTypeChange)。分类：玩家。

参数类型：[ClientGameTypeChangeAfterEvent](reference/ClientGameTypeChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("GameTypeChangedClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家Id |
| `oldGameType` | `oldGameType` | [int](../common/type-system.md#int) | 只读 | 切换前的游戏模式 |
| `newGameType` | `newGameType` | [int](../common/type-system.md#int) | 只读 | 切换后的游戏模式 |

**原生前提与限制：**

- 游戏模式：GetMinecraftEnum().GameType.\*:Survival，Creative，Adventure分别为0~2
    默认游戏模式发生变化时最后反映在个人游戏模式之上。

### OnGamepadControllerLayoutChangeClientEvent {#ongamepadcontrollerlayoutchangeclientevent}

游戏手柄按键映射改变事件

信号：[client.afterEvents.gamepadControllerLayoutChange](reference/ClientAfterEvents.md#gamepadControllerLayoutChange)。分类：控制。

参数类型：[ClientGamepadControllerLayoutChangeAfterEvent](reference/ClientGamepadControllerLayoutChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnGamepadControllerLayoutChangeClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `action` | `action` | [str](../common/type-system.md#str) | 只读 | 行为 |
| `newKey` | `newKey` | [int](../common/type-system.md#int) | 只读 | 修改后的键码，详见GamepadKeyType枚举 |
| `oldKey` | `oldKey` | [int](../common/type-system.md#int) | 只读 | 修改前的键码，详见GamepadKeyType枚举 |

### OnGamepadKeyPressClientEvent {#ongamepadkeypressclientevent}

游戏手柄按键事件

信号：`client.afterEvents.getNativeEvent('OnGamepadKeyPressClientEvent')`。分类：控制。

参数类型：[ClientGamepadKeyPressAfterEvent](reference/ClientGamepadKeyPressAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnGamepadKeyPressClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `screenName` | `screenName` | [str](../common/type-system.md#str) | 只读 | 当前screenName |
| `key` | `key` | [int](../common/type-system.md#int) | 只读 | 键码，详见GamepadKeyType枚举 |
| `isDown` | `isDown` | [str](../common/type-system.md#str) | 只读 | 是否按下，按下为1，弹起为0 |

### OnGamepadStickClientEvent {#ongamepadstickclientevent}

游戏手柄摇杆事件

信号：`client.afterEvents.getNativeEvent('OnGamepadStickClientEvent')`。分类：控制。

参数类型：[ClientGamepadStickAfterEvent](reference/ClientGamepadStickAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnGamepadStickClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `key` | `key` | [int](../common/type-system.md#int) | 只读 | 键码，详见GamepadKeyType枚举 |
| `x` | `x` | [float](../common/type-system.md#float) | 只读 | 摇杆水平方向的值，从左到右取值为 -1.0 ~ 1.0 |
| `y` | `y` | [float](../common/type-system.md#float) | 只读 | 摇杆竖直方向的值，从下到上取值为 -1.0 ~ 1.0 |

**原生前提与限制：**

- 触发时机：当摇杆摇动位置发生改变时

### OnGamepadTriggerClientEvent {#ongamepadtriggerclientevent}

游戏手柄扳机事件

信号：`client.afterEvents.getNativeEvent('OnGamepadTriggerClientEvent')`。分类：控制。

参数类型：[ClientGamepadTriggerAfterEvent](reference/ClientGamepadTriggerAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnGamepadTriggerClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `key` | `key` | [int](../common/type-system.md#int) | 只读 | 键码，详见GamepadKeyType枚举 |
| `magnitude` | `magnitude` | [float](../common/type-system.md#float) | 只读 | 扣动扳机的力度，取值为 0 ~ 1.0 |

**原生前提与限制：**

- 触发时机：当扣动扳机的力度发生改变时

### GetEntityByCoordEvent {#getentitybycoordevent}

玩家点击屏幕时触发，多个手指点在屏幕上时，只有第一个会触发。

信号：[client.afterEvents.getEntityByCoord](reference/ClientAfterEvents.md#getEntityByCoord)。分类：控制。

参数类型：[ClientGetEntityByCoordAfterEvent](reference/ClientGetEntityByCoordAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("GetEntityByCoordEvent")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### GetEntityByCoordReleaseClientEvent {#getentitybycoordreleaseclientevent}

玩家点击屏幕后松开时触发，多个手指点在屏幕上时，只有最后一个手指松开时触发。

信号：[client.afterEvents.getEntityByCoordRelease](reference/ClientAfterEvents.md#getEntityByCoordRelease)。分类：控制。

参数类型：[ClientGetEntityByCoordReleaseAfterEvent](reference/ClientGetEntityByCoordReleaseAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("GetEntityByCoordReleaseClientEvent")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### GridComponentSizeChangedClientEvent {#gridcomponentsizechangedclientevent}

[UI](../server_ui/reference/UI.md) grid控件里格子重新排列时触发

信号：[client.afterEvents.gridComponentSizeChange](reference/ClientAfterEvents.md#gridComponentSizeChange)。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientGridComponentSizeChangeAfterEvent](reference/ClientGridComponentSizeChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("GridComponentSizeChangedClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `path` | `path` | [str](../common/type-system.md#str) | 只读 | grid网格所在的路径（从UI根节点算起） |

### GrindStoneRemovedEnchantClientEvent {#grindstoneremovedenchantclientevent}

玩家点击砂轮合成得到的物品时抛出的事件

信号：[client.afterEvents.grindStoneRemoveEnchant](reference/ClientAfterEvents.md#grindStoneRemoveEnchant)。分类：物品。

参数类型：[ClientGrindStoneRemoveEnchantAfterEvent](reference/ClientGrindStoneRemoveEnchantAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("GrindStoneRemovedEnchantClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `oldItemDict` | `oldItemDict` | [dict](../common/type-system.md#dict) | 只读 | 合成前的物品物品信息字典（砂轮内第一个物品） |
| `additionalItemDict` | `additionalItemDict` | [dict](../common/type-system.md#dict) | 只读 | 作为合成材料的物品物品信息字典（砂轮内第二个物品） |
| `newItemDict` | `newItemDict` | [dict](../common/type-system.md#dict) | 只读 | 合成后的物品物品信息字典 |
| `exp` | `exp` | [int](../common/type-system.md#int) | 只读 | 本次合成返还的经验 |

### GyroSensorChangedClientEvent {#gyrosensorchangedclientevent}

触发时机：陀螺仪传感器姿态发生变化时

信号：[client.afterEvents.gyroSensorChange](reference/ClientAfterEvents.md#gyroSensorChange)。分类：控制。

参数类型：[ClientGyroSensorChangeAfterEvent](reference/ClientGyroSensorChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("GyroSensorChangedClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `xDiff` | `xDiff` | [float](../common/type-system.md#float) | 只读 | x轴角速度，单位为弧度/s |
| `yDiff` | `yDiff` | [float](../common/type-system.md#float) | 只读 | y轴角速度，单位为弧度/s |
| `zDiff` | `zDiff` | [float](../common/type-system.md#float) | 只读 | z轴角速度，单位为弧度/s |
| `orientation` | `orientation` | [int](../common/type-system.md#int) | 只读 | 当前屏幕朝向,0竖屏正向 1横屏向左 2竖屏倒置 3横屏向右 |
| `timestamp` | `timestamp` | [float](../common/type-system.md#float) | 只读 | 触发时间戳,秒 |

**原生前提与限制：**

- 该事件只适用于移动端

### HudButtonChangedClientEvent {#hudbuttonchangedclientevent}

当原生HUD按钮位置或大小发生改变时触发，例如玩家使用了自定义控件功能会触发，可在该事件中修改mod按钮的位置防止重叠

信号：[client.afterEvents.hudButtonChange](reference/ClientAfterEvents.md#hudButtonChange)。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientHudButtonChangeAfterEvent](reference/ClientHudButtonChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("HudButtonChangedClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `changedList` | `changedList` | [tuple](../common/type-system.md#tuple)([dict](../common/type-system.md#dict)) | 只读 | 修改后的按钮列表 |

**原生前提与限制：**

- 修改后的按钮列表中，每个按钮的字段如下：

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| areaEnum | [str](../common/type-system.md#str) | HUD原生UI枚举值 |
| beforeSize | `tuple(float,float,float,float)` | (xMin, yMin, xMax, yMax)修改前原生UI的Area |
| afterSize | `tuple(float,float,float,float)` | (xMin, yMin, xMax, yMax)修改后原生UI的Area |

### ClientPlayerInventoryCloseEvent {#clientplayerinventorycloseevent}

关闭物品背包界面时触发

信号：[client.afterEvents.inventoryClose](reference/ClientAfterEvents.md#inventoryClose)。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientInventoryCloseAfterEvent](reference/ClientInventoryCloseAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("ClientPlayerInventoryCloseEvent")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### OnItemSlotButtonClickedEvent {#onitemslotbuttonclickedevent}

点击快捷栏、背包栏、盔甲栏、副手栏的物品槽时触发

信号：[client.afterEvents.itemSlotButtonClicked](reference/ClientAfterEvents.md#itemSlotButtonClicked)。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientItemSlotButtonClickedAfterEvent](reference/ClientItemSlotButtonClickedAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnItemSlotButtonClickedEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `slotIndex` | `slotIndex` | [int](../common/type-system.md#int) | 只读 | 点击的物品槽的编号，编号对应位置详见\[[物品栏](https://zh.minecraft.wiki/w/%E7%89%A9%E5%93%81%E6%A0%8F)\] |

### ClientJumpButtonReleaseEvent {#clientjumpbuttonreleaseevent}

跳跃按钮按下释放事件

信号：[client.afterEvents.jumpButtonRelease](reference/ClientAfterEvents.md#jumpButtonRelease)。分类：控制。

参数类型：[ClientJumpButtonReleaseAfterEvent](reference/ClientJumpButtonReleaseAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("ClientJumpButtonReleaseEvent")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### OnKeyboardControllerLayoutChangeClientEvent {#onkeyboardcontrollerlayoutchangeclientevent}

键盘按键映射改变事件

信号：[client.afterEvents.keyboardControllerLayoutChange](reference/ClientAfterEvents.md#keyboardControllerLayoutChange)。分类：控制。

参数类型：[ClientKeyboardControllerLayoutChangeAfterEvent](reference/ClientKeyboardControllerLayoutChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnKeyboardControllerLayoutChangeClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `action` | `action` | [str](../common/type-system.md#str) | 只读 | 行为 |
| `newKey` | `newKey` | [int](../common/type-system.md#int) | 只读 | 修改后的键码，详见KeyBoardType枚举 |
| `oldKey` | `oldKey` | [int](../common/type-system.md#int) | 只读 | 修改前的键码，详见KeyBoardType枚举 |

### LeaveEntityClientEvent {#leaveentityclientevent}

玩家远离生物时触发

信号：[client.afterEvents.leaveEntity](reference/ClientAfterEvents.md#leaveEntity)。分类：实体。

参数类型：[ClientLeaveEntityAfterEvent](reference/ClientLeaveEntityAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("LeaveEntityClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 远离的生物实体id |

### LeftClickReleaseClientEvent {#leftclickreleaseclientevent}

玩家松开攻击/摧毁键时触发，例如鼠标左键、新触控攻击键、手柄右扳机键。鼠标左键仅在pc的普通控制模式（即非F11模式）下触发

信号：`client.afterEvents.getNativeEvent('LeftClickReleaseClientEvent')`。分类：控制。

参数类型：[ClientLeftClickReleaseAfterEvent](reference/ClientLeftClickReleaseAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("LeftClickReleaseClientEvent")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

**原生前提与限制：**

- 按键控制流程的图片讲解见[TapOrHoldReleaseClientEvent](events.md#taporholdreleaseclientevent)事件的备注

### LiquidClippedClientEvent {#liquidclippedclientevent}

玩家客户端点击流体时触发（支持原版流体与自定义流体）

信号：[client.afterEvents.liquidClipped](reference/ClientAfterEvents.md#liquidClipped)。分类：物品。

参数类型：[ClientLiquidClippedAfterEvent](reference/ClientLiquidClippedAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("LiquidClippedClientEvent")`。

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

### OnLocalPlayerStopLoading {#onlocalplayerstoploading}

触发时机：玩家进入存档，出生点地形加载完成时触发。该事件触发时可以进行切换维度的操作。

信号：[client.afterEvents.localPlayerLoad](reference/ClientAfterEvents.md#localPlayerLoad)。分类：世界。

参数类型：[ClientLocalPlayerLoadAfterEvent](reference/ClientLocalPlayerLoadAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnLocalPlayerStopLoading")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 加载完成的玩家id |

### ModBlockEntityLoadedClientEvent {#modblockentityloadedclientevent}

客户端自定义方块实体初始化完成时触发

信号：[client.afterEvents.modBlockEntityLoad](reference/ClientAfterEvents.md#modBlockEntityLoad)。分类：方块。

参数类型：[ClientModBlockEntityLoadAfterEvent](reference/ClientModBlockEntityLoadAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("ModBlockEntityLoadedClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `posX` | `posX` | [int](../common/type-system.md#int) | 只读 | 自定义方块实体的位置X |
| `posY` | `posY` | [int](../common/type-system.md#int) | 只读 | 自定义方块实体的位置Y |
| `posZ` | `posZ` | [int](../common/type-system.md#int) | 只读 | 自定义方块实体的位置Z |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |

**原生前提与限制：**

- 只有添加了自定义方块实体扩展功能的自定义方块实体才能触发该事件（见自定义方块实体外观），请用该事件来初始化自定义方块实体的molang，否则方块实体未初始化完成会设置失败。
  - 实际触发时机是自定义方块实体第一次出现在玩家视野中时触发，玩家离开后又回来时方块实体会重新加载并初始化。但由于出生点是常加载区域，来回传送不会重复触发此事件。
  - 该事件在OnModBlockNeteaseEffectCreatedClientEvent后触发。

### ModBlockEntityRemoveClientEvent {#modblockentityremoveclientevent}

客户端自定义方块实体卸载时触发

信号：[client.afterEvents.modBlockEntityRemove](reference/ClientAfterEvents.md#modBlockEntityRemove)。分类：方块。

参数类型：[ClientModBlockEntityRemoveAfterEvent](reference/ClientModBlockEntityRemoveAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("ModBlockEntityRemoveClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `posX` | `posX` | [int](../common/type-system.md#int) | 只读 | 自定义方块实体的位置X |
| `posY` | `posY` | [int](../common/type-system.md#int) | 只读 | 自定义方块实体的位置Y |
| `posZ` | `posZ` | [int](../common/type-system.md#int) | 只读 | 自定义方块实体的位置Z |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |

### ModBlockEntityTickClientEvent {#modblockentitytickclientevent}

客户端自定义方块实体tick事件

信号：[client.afterEvents.modBlockEntityTick](reference/ClientAfterEvents.md#modBlockEntityTick)。分类：方块。

参数类型：[ClientModBlockEntityTickAfterEvent](reference/ClientModBlockEntityTickAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("ModBlockEntityTickClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `posX` | `posX` | [int](../common/type-system.md#int) | 只读 | 自定义方块实体的位置X |
| `posY` | `posY` | [int](../common/type-system.md#int) | 只读 | 自定义方块实体的位置Y |
| `posZ` | `posZ` | [int](../common/type-system.md#int) | 只读 | 自定义方块实体的位置Z |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |

**原生前提与限制：**

- 只有client_tick字段为true的自定义方块实体才能触发该事件（见自定义方块实体
  - 目前客户端实体tick范围为硬编码，范围为玩家为中心的等腰等斜边八边形，其中斜边长度为5，非斜边长度为3

### OnModBlockNeteaseEffectCreatedClientEvent {#onmodblockneteaseeffectcreatedclientevent}

自定义方块实体绑定的特效创建成功事件，在自定义方块实体中绑定的特效创建成功时触发以及使用接口CreateFrameEffectForBlockEntity或CreateParticleEffectForBlockEntity为自定义方块实体添加特效成功时触发。

信号：[client.afterEvents.modBlockNeteaseEffectCreate](reference/ClientAfterEvents.md#modBlockNeteaseEffectCreate)。分类：方块。

参数类型：[ClientModBlockNeteaseEffectCreateAfterEvent](reference/ClientModBlockNeteaseEffectCreateAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnModBlockNeteaseEffectCreatedClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `effectName` | `effectName` | [str](../common/type-system.md#str) | 只读 | 创建成功的特效的自定义键值名称 |
| `id` | `id` | [int](../common/type-system.md#int) | 只读 | 该特效的id |
| `effectType` | `effectType` | [int](../common/type-system.md#int) | 只读 | 该特效的类型，0为粒子特效，1为序列帧特效 |
| `blockPos` | `blockPos` | [tuple](../common/type-system.md#tuple)([float](../common/type-system.md#float),[float](../common/type-system.md#float),[float](../common/type-system.md#float)) | 只读 | 该特效绑定的自定义方块实体的世界坐标 |

### OnMouseMiddleDownClientEvent {#onmousemiddledownclientevent}

鼠标按下中键时触发

信号：`client.afterEvents.getNativeEvent('OnMouseMiddleDownClientEvent')`。分类：控制。

参数类型：[ClientMouseMiddleDownAfterEvent](reference/ClientMouseMiddleDownAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnMouseMiddleDownClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `isDown` | `isDown` | [int](../common/type-system.md#int) | 只读 | 1为按下，0为弹起 |
| `mousePositionX` | `mousePositionX` | [float](../common/type-system.md#float) | 只读 | 按下时的x坐标 |
| `mousePositionY` | `mousePositionY` | [float](../common/type-system.md#float) | 只读 | 按下时的y坐标 |

**原生前提与限制：**

- 仅通过PushScreen创建的界面能够正常返回坐标，开启F11模式的时候，返回最后点击屏幕时的坐标

### OnKeyPressInGame {#onkeypressingame}

按键按下或按键释放时触发

信号：`client.afterEvents.getNativeEvent('OnKeyPressInGame')`。分类：控制。

参数类型：[ClientNativeKeyPressAfterEvent](reference/ClientNativeKeyPressAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnKeyPressInGame")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `screenName` | `screenName` | [str](../common/type-system.md#str) | 只读 | 当前screenName |
| `key` | `key` | [str](../common/type-system.md#str) | 只读 | 键码（注：这里的int型被转成了str型，比如"1"对应的就是枚举值文档中的1），详见KeyBoardType枚举 |
| `isDown` | `isDown` | [str](../common/type-system.md#str) | 只读 | 是否按下，按下为1，弹起为0 |

### MouseWheelClientEvent {#mousewheelclientevent}

鼠标滚轮滚动时触发

信号：`client.afterEvents.getNativeEvent('MouseWheelClientEvent')`。分类：控制。

参数类型：[ClientNativeMouseWheelAfterEvent](reference/ClientNativeMouseWheelAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("MouseWheelClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `direction` | `direction` | [int](../common/type-system.md#int) | 只读 | 1为向上滚动，0为向下滚动 |

### OnMusicStopClientEvent {#onmusicstopclientevent}

音乐停止时，当玩家调用StopCustomMusic来停止自定义背景音乐时，会触发该事件

信号：`client.afterEvents.getNativeEvent('OnMusicStopClientEvent')`。分类：音效。

参数类型：[ClientNativeMusicStopAfterEvent](reference/ClientNativeMusicStopAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnMusicStopClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `musicName` | `musicName` | [str](../common/type-system.md#str) | 只读 | 音乐名称 |

### PerspChangeClientEvent {#perspchangeclientevent}

视角切换时会触发的事件

信号：[client.afterEvents.perspectiveChange](reference/ClientAfterEvents.md#perspectiveChange)。分类：玩家。

参数类型：[ClientPerspectiveChangeAfterEvent](reference/ClientPerspectiveChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("PerspChangeClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `fromValue` | `from` | [int](../common/type-system.md#int) | 只读 | 切换前的视角 |
| `to` | `to` | [int](../common/type-system.md#int) | 只读 | 切换后的视角 |

**原生前提与限制：**

- 视角数字代表含义
    0: 第一人称
    1: 第三人称背面
    2: 第三人称正面

### PhysxTouchClientEvent {#physxtouchclientevent}

给自定义刚体添加的碰撞体，与其他碰撞体或原版实体发生碰撞/结束碰撞时触发。需要在碰撞体创建时使用PxEventMask.Client才会触发

信号：`client.afterEvents.getNativeEvent('PhysxTouchClientEvent')`。分类：物理。

参数类型：[ClientPhysicsTouchAfterEvent](reference/ClientPhysicsTouchAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("PhysxTouchClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `touch` | `touch` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 只读 | 开始接触的碰撞体对的信息。一个碰撞体在创建时使用了PxEventMask.Found，他与其他碰撞体/原版实体开始接触时，会出现在列表中 |
| `lost` | `lost` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 只读 | 结束接触的碰撞体对的信息。一个碰撞体在创建时使用了PxEventMask.Lost，他与其他碰撞体/原版实体结束接触时，会出现在列表中 |

**原生前提与限制：**

- touch列表每个元素的内容：

    

    lost列表每个元素的内容：

    

  - 列表中的碰撞对不分先后，每个碰撞对中的碰撞体0与碰撞体1也不分先后

### PhysxTriggerClientEvent {#physxtriggerclientevent}

给自定义刚体添加的触发器，与其他碰撞体或原版实体进入/离开触发器时触发。需要在触发器创建时使用PxEventMask.Client才会触发

信号：`client.afterEvents.getNativeEvent('PhysxTriggerClientEvent')`。分类：物理。

参数类型：[ClientPhysicsTriggerAfterEvent](reference/ClientPhysicsTriggerAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("PhysxTriggerClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `found` | `found` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 只读 | 进入触发器的碰撞体对的信息。它与其他碰撞体/原版实体进入触发器时，会出现在列表中 |
| `lost` | `lost` | [list](../common/type-system.md#list)([dict](../common/type-system.md#dict)) | 只读 | 离开触发器的碰撞体对的信息。它与其他碰撞体/原版实体离开触发器时，会出现在列表中 |

**原生前提与限制：**

- found列表每个元素的内容：

    

    lost列表每个元素的内容：

### OnLocalPlayerActionClientEvent {#onlocalplayeractionclientevent}

玩家动作事件，当本地玩家开始/停止某些动作时触发该事件

信号：`client.afterEvents.getNativeEvent('OnLocalPlayerActionClientEvent')`。分类：玩家。

参数类型：[ClientPlayerActionAfterEvent](reference/ClientPlayerActionAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnLocalPlayerActionClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `actionType` | `actionType` | [int](../common/type-system.md#int) | 只读 | 动作事件枚举，详见Minecraft枚举值文档的PlayerActionType |

### PlayerAddCustomContainerItemClientEvent {#playeraddcustomcontaineritemclientevent}

玩家成功将物品添加到自定义容器时触发该事件

信号：[client.afterEvents.playerAddCustomContainerItem](reference/ClientAfterEvents.md#playerAddCustomContainerItem)。分类：物品。

参数类型：[ClientPlayerAddCustomContainerItemAfterEvent](reference/ClientPlayerAddCustomContainerItemAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("PlayerAddCustomContainerItemClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `beforeItemDict` | `beforeItemDict` | [dict](../common/type-system.md#dict) | 只读 | 操作前目标槽位的物品信息字典 |
| `changedItemDict` | `changedItemDict` | [dict](../common/type-system.md#dict) | 只读 | 实际添加的物品的物品信息字典 |
| `afterItemDict` | `afterItemDict` | [dict](../common/type-system.md#dict) | 只读 | 操作后目标槽位的物品信息字典 |
| `collectionName` | `collectionName` | [str](../common/type-system.md#str) | 只读 | 容器名称，对应容器json中"custom_description"字段 |
| `collectionType` | `collectionType` | [str](../common/type-system.md#str) | 只读 | 容器类型，目前仅支持netease_container和netease_ui_container |
| `collectionIndex` | `collectionIndex` | [int](../common/type-system.md#int) | 只读 | 容器槽位索引 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 容器方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 容器方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 容器方块z坐标 |

**原生前提与限制：**

- 该事件仅在目标容器为netease_container或netease_ui_container时触发
  - 该事件在物品成功添加后触发，无cancel参数，无法取消操作
  - 容器内物品移动，合堆，分堆的操作会分多次事件触发并且顺序不定，编写逻辑时请勿依赖事件触发顺序

### PlayerAttackEntityEvent {#playerattackentityevent}

触发时机：当本地玩家攻击时触发该事件。

信号：[client.afterEvents.playerAttackEntity](reference/ClientAfterEvents.md#playerAttackEntity)。分类：玩家。

参数类型：[ClientPlayerAttackEntityAfterEvent](reference/ClientPlayerAttackEntityAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("PlayerAttackEntityEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `target` | `victimId` | [str](../common/type-system.md#str) | 只读 | 受击者id |
| `damage` | `damage` | [float](../common/type-system.md#float) | 只读 | 客户端收到的是真实伤害值，且修改无效 |
| `isCrit` | `isCrit` | [bool](../common/type-system.md#bool) | 只读 | 本次攻击是否产生暴击,不支持修改 |

### PlayerChatButtonClickClientEvent {#playerchatbuttonclickclientevent}

玩家点击聊天按钮或回车键触发呼出聊天窗口时客户端抛出的事件

信号：[client.afterEvents.playerChatButtonClick](reference/ClientAfterEvents.md#playerChatButtonClick)。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientPlayerChatButtonClickAfterEvent](reference/ClientPlayerChatButtonClickAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("PlayerChatButtonClickClientEvent")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### DimensionChangeClientEvent {#dimensionchangeclientevent}

玩家维度改变时客户端抛出

信号：[client.afterEvents.playerDimensionChange](reference/ClientAfterEvents.md#playerDimensionChange)。分类：玩家。

参数类型：[ClientPlayerDimensionChangeAfterEvent](reference/ClientPlayerDimensionChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("DimensionChangeClientEvent")`。

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

### DimensionChangeFinishClientEvent {#dimensionchangefinishclientevent}

玩家维度改变完成后客户端抛出

信号：[client.afterEvents.playerDimensionChangeFinish](reference/ClientAfterEvents.md#playerDimensionChangeFinish)。分类：玩家。

参数类型：[ClientPlayerDimensionChangeFinishAfterEvent](reference/ClientPlayerDimensionChangeFinishAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("DimensionChangeFinishClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `fromDimension` | `fromDimensionId` | [int](../common/type-system.md#int) | 只读 | 维度改变前的维度 |
| `toDimension` | `toDimensionId` | [int](../common/type-system.md#int) | 只读 | 维度改变后的维度 |
| `toPos` | `toPos` | [tuple](../common/type-system.md#tuple)([float](../common/type-system.md#float),[float](../common/type-system.md#float),[float](../common/type-system.md#float)) | 只读 | 改变后的位置x,y,z,其中y值为脚底加上角色的身高值 |

**原生前提与限制：**

- 当通过传送门从末地回到主世界时，toPos的y值为32767，其他情况一般会比设置值高1.62

### AddPlayerAOIClientEvent {#addplayeraoiclientevent}

玩家加入游戏时视野内存在其他玩家，或者其余玩家进入当前玩家视野时触发的事件，替换AddPlayerEvent

信号：[client.afterEvents.playerEnteredView](reference/ClientAfterEvents.md#playerEnteredView)。分类：世界。

参数类型：[ClientPlayerEnteredViewAfterEvent](reference/ClientPlayerEnteredViewAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("AddPlayerAOIClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |

**原生前提与限制：**

- 该事件触发只表明在服务端数据中接收到了新玩家，并不能代表此时玩家在客户端中可见，若想在玩家进入视野后立马调用玩家渲染相关接口，建议使用[AddPlayerCreatedClientEvent](events.md#addplayercreatedclientevent)。
  - 玩家加入游戏时视野内每存在一位其他玩家便触发一次该事件，若无其他玩家，则不触发

### OnPlayerHitBlockClientEvent {#onplayerhitblockclientevent}

触发时机：通过OpenPlayerHitBlockDetection打开方块碰撞检测后，当玩家碰撞到方块时触发该事件。玩家着地时会触发[OnGroundClientEvent](events.md#ongroundclientevent)，而不是该事件。客户端和服务端分别作碰撞检测，可能两个事件返回的结果略有差异。

信号：[client.afterEvents.playerHitBlock](reference/ClientAfterEvents.md#playerHitBlock)。分类：玩家。

参数类型：[ClientPlayerHitBlockAfterEvent](reference/ClientPlayerHitBlockAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnPlayerHitBlockClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 碰撞到方块的玩家Id |
| `posX` | `posX` | [int](../common/type-system.md#int) | 只读 | 碰撞方块x坐标 |
| `posY` | `posY` | [int](../common/type-system.md#int) | 只读 | 碰撞方块y坐标 |
| `posZ` | `posZ` | [int](../common/type-system.md#int) | 只读 | 碰撞方块z坐标 |
| `blockId` | `blockId` | [str](../common/type-system.md#str) | 只读 | 碰撞方块的identifier |
| `auxValue` | `auxValue` | [int](../common/type-system.md#int) | 只读 | 碰撞方块的附加值 |

**原生前提与限制：**

- 注：该碰撞检测会屏蔽草、空气、火、高草四种方块

### OnCarriedNewItemChangedClientEvent {#oncarriednewitemchangedclientevent}

手持物品发生变化时，触发该事件；数量改变不会通知

信号：`client.afterEvents.getNativeEvent('OnCarriedNewItemChangedClientEvent')`。分类：物品。

参数类型：[ClientPlayerHotbarItemChangeAfterEvent](reference/ClientPlayerHotbarItemChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnCarriedNewItemChangedClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 切换后物品的物品信息字典 |

### InventoryItemChangedClientEvent {#inventoryitemchangedclientevent}

玩家背包物品变化时客户端抛出的事件。

信号：`client.afterEvents.getNativeEvent('InventoryItemChangedClientEvent')`。分类：物品。

参数类型：[ClientPlayerInventoryItemChangeAfterEvent](reference/ClientPlayerInventoryItemChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("InventoryItemChangedClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `slot` | `slot` | [int](../common/type-system.md#int) | 只读 | 背包槽位 |
| `oldItemDict` | `oldItemDict` | [dict](../common/type-system.md#dict) | 只读 | 变化前槽位中的物品，格式参考物品信息字典 |
| `newItemDict` | `newItemDict` | [dict](../common/type-system.md#dict) | 只读 | 变化后槽位中的物品，格式参考物品信息字典 |

**原生前提与限制：**

- 如果槽位变空，变化后槽位中物品为空气
  - 触发时槽位物品仍为变化前物品
  - 背包内物品移动，合堆，分堆的操作会分多次事件触发并且顺序不定，编写逻辑时请勿依赖事件触发顺序

### OnLocalPlayerStartJumpClientEvent {#onlocalplayerstartjumpclientevent}

本地玩家开始跳跃时触发

信号：[client.afterEvents.playerJump](reference/ClientAfterEvents.md#playerJump)。分类：玩家。

参数类型：[ClientPlayerJumpAfterEvent](reference/ClientPlayerJumpAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnLocalPlayerStartJumpClientEvent")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### RemovePlayerAOIClientEvent {#removeplayeraoiclientevent}

玩家离开当前玩家视野时触发的事件

信号：`client.afterEvents.getNativeEvent('RemovePlayerAOIClientEvent')`。分类：世界。

参数类型：[ClientPlayerLeftViewAfterEvent](reference/ClientPlayerLeftViewAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("RemovePlayerAOIClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |

### PlayerPermissionChangeClientEvent {#playerpermissionchangeclientevent}

玩家权限变更事件

信号：[client.afterEvents.playerPermissionChange](reference/ClientAfterEvents.md#playerPermissionChange)。分类：玩家。

参数类型：[ClientPlayerPermissionChangeAfterEvent](reference/ClientPlayerPermissionChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("PlayerPermissionChangeClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `causePlayer` | `causePlayerId` | [str](../common/type-system.md#str) | 只读 | 发起者id |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `oldPermission` | `oldPermission` | [dict](../common/type-system.md#dict) | 只读 | 变化前的权限字典 |
| `newPermission` | `newPermission` | [dict](../common/type-system.md#dict) | 只读 | 变化后的权限字典 |
| `changeCause` | `changeCause` | [int](../common/type-system.md#int) | 只读 | 变化原因，详见Minecraft枚举值文档的PermissionChangeCause |

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

- 当PlayerPermissionChangeServerEvent事件返回"cancel"为True时，权限变动被取消，该事件不会触发。

### PlayerRemoveCustomContainerItemClientEvent {#playerremovecustomcontaineritemclientevent}

玩家成功从自定义容器中移除物品时触发该事件

信号：[client.afterEvents.playerRemoveCustomContainerItem](reference/ClientAfterEvents.md#playerRemoveCustomContainerItem)。分类：物品。

参数类型：[ClientPlayerRemoveCustomContainerItemAfterEvent](reference/ClientPlayerRemoveCustomContainerItemAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("PlayerRemoveCustomContainerItemClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `beforeItemDict` | `beforeItemDict` | [dict](../common/type-system.md#dict) | 只读 | 操作前目标槽位的物品信息字典 |
| `changedItemDict` | `changedItemDict` | [dict](../common/type-system.md#dict) | 只读 | 实际移除的物品的物品信息字典 |
| `afterItemDict` | `afterItemDict` | [dict](../common/type-system.md#dict) | 只读 | 操作后目标槽位的物品信息字典 |
| `collectionName` | `collectionName` | [str](../common/type-system.md#str) | 只读 | 容器名称，对应容器json中"custom_description"字段 |
| `collectionType` | `collectionType` | [str](../common/type-system.md#str) | 只读 | 容器类型，目前仅支持netease_container和netease_ui_container |
| `collectionIndex` | `collectionIndex` | [int](../common/type-system.md#int) | 只读 | 容器槽位索引 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 容器方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 容器方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 容器方块z坐标 |

**原生前提与限制：**

- 该事件仅在源容器为netease_container或netease_ui_container时触发
  - 该事件在物品成功移除后触发，无cancel参数，无法取消操作
  - 容器内物品移动，合堆，分堆的操作会分多次事件触发并且顺序不定，编写逻辑时请勿依赖事件触发顺序

### AddPlayerCreatedClientEvent {#addplayercreatedclientevent}

玩家进入当前玩家所在的区块AOI后，玩家皮肤数据异步加载完成后触发的事件

信号：`client.afterEvents.getNativeEvent('AddPlayerCreatedClientEvent')`。分类：世界。

参数类型：[ClientPlayerSkinLoadAfterEvent](reference/ClientPlayerSkinLoadAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("AddPlayerCreatedClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |

**原生前提与限制：**

- 由于玩家皮肤是异步加载的原因，该事件触发时机比[AddPlayerAOIClientEvent](events.md#addplayeraoiclientevent)晚，触发该事件后可以对该玩家调用相关玩家渲染接口。
  - 当前客户端每加载好一个玩家的皮肤，就会触发一次该事件，比如刚进入世界时，localPlayer加载好会触发一次，周围的所有玩家加载好后也会分别触发一次。

### OnClientPlayerStartMove {#onclientplayerstartmove}

移动按钮按下触发事件，在按住一个方向键的同时，去按另外一个方向键，不会触发第二次

信号：[client.afterEvents.playerStartMove](reference/ClientAfterEvents.md#playerStartMove)。分类：控制。

参数类型：[ClientPlayerStartMoveAfterEvent](reference/ClientPlayerStartMoveAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnClientPlayerStartMove")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### OnClientPlayerStopMove {#onclientplayerstopmove}

移动按钮按下释放时触发事件，同时按下多个方向键，需要释放所有的方向键才会触发事件

信号：[client.afterEvents.playerStopMove](reference/ClientAfterEvents.md#playerStopMove)。分类：控制。

参数类型：[ClientPlayerStopMoveAfterEvent](reference/ClientPlayerStopMoveAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnClientPlayerStopMove")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### PopScreenAfterClientEvent {#popscreenafterclientevent}

screen移除触发

信号：`client.afterEvents.getNativeEvent('PopScreenAfterClientEvent')`。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientPopScreenAfterEvent](reference/ClientPopScreenAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("PopScreenAfterClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `screenName` | `screenName` | [str](../common/type-system.md#str) | 只读 | UI名字 |
| `screenDef` | `screenDef` | [str](../common/type-system.md#str) | 只读 | 包含命名空间的UI名字，格式为namespace.screenName |

**原生前提与限制：**

- 与PopScreenEvent不同，PopScreenAfterClientEvent触发时机是在完全把UI弹出后，返回的参数是弹出后最顶层UI的

### PushScreenEvent {#pushscreenevent}

screen创建触发

信号：`client.afterEvents.getNativeEvent('PushScreenEvent')`。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientPushScreenAfterEvent](reference/ClientPushScreenAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("PushScreenEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `screenName` | `screenName` | [str](../common/type-system.md#str) | 只读 | UI名字 |
| `screenDef` | `screenDef` | [str](../common/type-system.md#str) | 只读 | 包含命名空间的UI名字，格式为namespace.screenName |

### ClientShapedRecipeTriggeredEvent {#clientshapedrecipetriggeredevent}

玩家合成物品时触发

信号：[client.afterEvents.recipeTrigger](reference/ClientAfterEvents.md#recipeTrigger)。分类：物品。

参数类型：[ClientRecipeTriggerAfterEvent](reference/ClientRecipeTriggerAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("ClientShapedRecipeTriggeredEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `recipeId` | `recipeId` | [str](../common/type-system.md#str) | 只读 | 配方id，对应配方json文件中的identifier字段 |

### GameRenderTickEvent {#gamerendertickevent}

客户端渲染帧开始时触发该事件,一秒触发次数为当前的帧数

信号：[client.afterEvents.render](reference/ClientAfterEvents.md#render)。分类：世界。

参数类型：[ClientRenderAfterEvent](reference/ClientRenderAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("GameRenderTickEvent")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### RightClickReleaseClientEvent {#rightclickreleaseclientevent}

玩家松开使用物品/放置方块键时触发，例如鼠标右键、新触控交互键、手柄左扳机键

信号：`client.afterEvents.getNativeEvent('RightClickReleaseClientEvent')`。分类：控制。

参数类型：[ClientRightClickReleaseAfterEvent](reference/ClientRightClickReleaseAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("RightClickReleaseClientEvent")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

**原生前提与限制：**

- 按键控制流程的图片讲解见[TapOrHoldReleaseClientEvent](events.md#taporholdreleaseclientevent)事件的备注

### ScreenSizeChangedClientEvent {#screensizechangedclientevent}

改变屏幕大小时会触发的事件

信号：[client.afterEvents.screenSizeChange](reference/ClientAfterEvents.md#screenSizeChange)。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientScreenSizeChangeAfterEvent](reference/ClientScreenSizeChangeAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("ScreenSizeChangedClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `beforeX` | `beforeX` | [float](../common/type-system.md#float) | 只读 | 屏幕大小改变前的宽度 |
| `beforeY` | `beforeY` | [float](../common/type-system.md#float) | 只读 | 屏幕大小改变前的高度 |
| `afterX` | `afterX` | [float](../common/type-system.md#float) | 只读 | 屏幕大小改变后的宽度 |
| `afterY` | `afterY` | [float](../common/type-system.md#float) | 只读 | 屏幕大小改变后的高度 |

**原生前提与限制：**

- 该事件仅支持PC

### LoadClientAddonScriptsAfter {#loadclientaddonscriptsafter}

客户端加载mod完成事件

信号：[client.afterEvents.scriptsLoad](reference/ClientAfterEvents.md#scriptsLoad)。分类：世界。

参数类型：[ClientScriptsLoadAfterEvent](reference/ClientScriptsLoadAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("LoadClientAddonScriptsAfter")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### StartRidingClientEvent {#startridingclientevent}

触发时机：一个实体即将骑乘另外一个实体

信号：[client.afterEvents.startRiding](reference/ClientAfterEvents.md#startRiding)。分类：实体。

参数类型：[ClientStartRidingAfterEvent](reference/ClientStartRidingAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("StartRidingClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `rider` | `actorId` | [str](../common/type-system.md#str) | 只读 | 骑乘者的唯一ID |
| `target` | `victimId` | [str](../common/type-system.md#str) | 只读 | 被骑乘实体的唯一ID |

**原生前提与限制：**

- 如果需要修改cancel，请通过服务端事件StartRidingServerEvent同步修改，客户端触发该事件时，实体已经骑乘成功。

### StartUsingItemClientEvent {#startusingitemclientevent}

玩家使用物品（目前仅支持Bucket（奶桶）、Trident（三叉戟）、RangedWeapon（弓）、Food（食物）、Potion（药水）、Crossbow（弩））时抛出

信号：[client.afterEvents.startUsingItem](reference/ClientAfterEvents.md#startUsingItem)。分类：物品。

参数类型：[ClientStartUsingItemAfterEvent](reference/ClientStartUsingItemAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("StartUsingItemClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 使用的物品的物品信息字典 |

### StepOffBlockClientEvent {#stepoffblockclientevent}

触发时机：实体移动离开一个实心方块时触发

信号：[client.afterEvents.stepOffBlock](reference/ClientAfterEvents.md#stepOffBlock)。分类：方块。

参数类型：[ClientStepOffBlockAfterEvent](reference/ClientStepOffBlockAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("StepOffBlockClientEvent")`。

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

### StopUsingItemClientEvent {#stopusingitemclientevent}

玩家停止使用物品（目前仅支持Bucket（奶桶）、Trident（三叉戟）、RangedWeapon（弓）、Food（食物）、Potion（药水）、Crossbow（弩））时抛出

信号：[client.afterEvents.stopUsingItem](reference/ClientAfterEvents.md#stopUsingItem)。分类：物品。

参数类型：[ClientStopUsingItemAfterEvent](reference/ClientStopUsingItemAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("StopUsingItemClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家实体id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 使用的物品的物品信息字典 |

### TapOrHoldReleaseClientEvent {#taporholdreleaseclientevent}

玩家点击屏幕后松手时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以使用[LeftClickReleaseClientEvent](events.md#leftclickreleaseclientevent)与[RightClickReleaseClientEvent](events.md#rightclickreleaseclientevent)事件监听鼠标松开

信号：`client.afterEvents.getNativeEvent('TapOrHoldReleaseClientEvent')`。分类：控制。

参数类型：[ClientTapOrHoldReleaseAfterEvent](reference/ClientTapOrHoldReleaseAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("TapOrHoldReleaseClientEvent")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

**原生前提与限制：**

- 短按及长按后松手都会触发该事件
  - 一张图读懂点触和按键事件触发流程
    !点触说明

### OnScriptTickClient {#onscripttickclient}

客户端tick事件,1秒30次

信号：[client.afterEvents.tick](reference/ClientAfterEvents.md#tick)。分类：世界。

参数类型：[ClientTickAfterEvent](reference/ClientTickAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("OnScriptTickClient")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### UiInitFinished {#uiinitfinished}

UI初始化框架完成,此时可以创建[UI](../server_ui/reference/UI.md)

信号：`client.afterEvents.getNativeEvent('UiInitFinished')`。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientUiInitFinishAfterEvent](reference/ClientUiInitFinishAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("UiInitFinished")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

**原生前提与限制：**

- 切换维度后会重新初始化UI并触发该事件

### UpdatePlayerSkinClientEvent {#updateplayerskinclientevent}

触发时机：玩家加入游戏或通过更衣室局内换肤后 同步皮肤信息至客户端后触发

信号：[client.afterEvents.updatePlayerSkin](reference/ClientAfterEvents.md#updatePlayerSkin)。分类：玩家。

参数类型：[ClientUpdatePlayerSkinAfterEvent](reference/ClientUpdatePlayerSkinAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("UpdatePlayerSkinClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 更换皮肤的玩家id |

**原生前提与限制：**

- 此事件配合 IsOfficialSkin IsHighLevelOfficialSkin IsHighLevelMultiJointOfficialSkin 接口 用于获取玩家的皮肤信息

### WalkAnimBeginClientEvent {#walkanimbeginclientevent}

走路动作开始时触发

信号：[client.afterEvents.walkAnimBegin](reference/ClientAfterEvents.md#walkAnimBegin)。分类：模型。

参数类型：[ClientWalkAnimBeginAfterEvent](reference/ClientWalkAnimBeginAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("WalkAnimBeginClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |

**原生前提与限制：**

- 使用SetModel替换骨骼模型后，该事件才生效

### WalkAnimEndClientEvent {#walkanimendclientevent}

走路动作结束时触发

信号：[client.afterEvents.walkAnimEnd](reference/ClientAfterEvents.md#walkAnimEnd)。分类：模型。

参数类型：[ClientWalkAnimEndAfterEvent](reference/ClientWalkAnimEndAfterEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.afterEvents.getNativeEvent("WalkAnimEndClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |

**原生前提与限制：**

- 使用SetModel替换骨骼模型后，该事件才生效

### ClientBlockUseEvent {#clientblockuseevent}

触发时机：玩家右键点击新版自定义方块（或者通过接口AddBlockItemListenForUseEvent增加监听的MC原生游戏方块）时客户端抛出该事件（该事件tick执行，需要注意效率问题）。

信号：`client.beforeEvents.getNativeEvent('ClientBlockUseEvent')`。分类：方块。

参数类型：[ClientBlockUseBeforeEvent](reference/ClientBlockUseBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("ClientBlockUseEvent")`。

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

**原生前提与限制：**

- 如果拦截与方块交互的逻辑，则不会给服务端发送对应的网络包。

### CameraMotionStopClientEvent {#cameramotionstopclientevent}

相机运动器停止事件。相机添加运动器并开始运行后，运动器自动停止时触发

信号：[client.beforeEvents.cameraMotionStop](reference/ClientBeforeEvents.md#cameraMotionStop)。分类：玩家。

参数类型：[ClientCameraMotionStopBeforeEvent](reference/ClientCameraMotionStopBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("CameraMotionStopClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `motionId` | `motionId` | [int](../common/type-system.md#int) | 只读 | 运动器id |
| `remove` | `remove` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否移除该运动器，设置为False则保留，默认为True，即运动器停止后自动移除 |

**原生前提与限制：**

- 注意：该事件触发表示运动器播放顺利完成，手动调用的StopCameraMotion、RemoveCameraMotion不会触发该事件。

### ChunkAcquireDiscardedClientEvent {#chunkacquirediscardedclientevent}

触发时机：客户端区块即将被卸载时

信号：[client.beforeEvents.chunkUnload](reference/ClientBeforeEvents.md#chunkUnload)。分类：世界。

参数类型：[ClientChunkUnloadBeforeEvent](reference/ClientChunkUnloadBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("ChunkAcquireDiscardedClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `dimension` | `dimension` | [int](../common/type-system.md#int) | 只读 | 区块所在维度 |
| `chunkPosX` | `chunkPosX` | [int](../common/type-system.md#int) | 只读 | 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15] |
| `chunkPosZ` | `chunkPosZ` | [int](../common/type-system.md#int) | 只读 | 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15] |

**原生前提与限制：**

- 区块卸载：游戏只会加载玩家周围的区块，玩家移动到别的区域时，原来所在区域的区块会被卸载，参考[区块介绍 （在新窗口打开）](https://zh.minecraft.wiki/w/%E5%8C%BA%E5%9D%97)

### OnEntityInsideBlockClientEvent {#onentityinsideblockclientevent}

触发时机：当实体碰撞盒所在区域有方块时，客户端持续触发

信号：[client.beforeEvents.entityInsideBlock](reference/ClientBeforeEvents.md#entityInsideBlock)。分类：方块。

参数类型：[ClientEntityInsideBlockBeforeEvent](reference/ClientEntityInsideBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("OnEntityInsideBlockClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 实体所在维度id |
| `slowdownMultiX` | `slowdownMultiX` | [float](../common/type-system.md#float) | 同步回调中 | 实体移速X方向的减速比例 |
| `slowdownMultiY` | `slowdownMultiY` | [float](../common/type-system.md#float) | 同步回调中 | 实体移速Y方向的减速比例 |
| `slowdownMultiZ` | `slowdownMultiZ` | [float](../common/type-system.md#float) | 同步回调中 | 实体移速Z方向的减速比例 |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 方块位置x |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 方块位置y |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 方块位置z |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 可由脚本层回传True给引擎，阻止触发后续原版逻辑 |

**原生前提与限制：**

- 不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义方块JSON组件）
    ，原版方块需要先通过RegisterOnEntityInside接口注册才能触发
  - 压力板和拌线钩不支持该事件，如需监听请参考OnEntityInsideBlockServerEvent事件。
  - 如果需要修改slowdownMulti/cancel，强烈建议与服务端事件同步修改，避免出现被服务端矫正等非预期现象。
  - 如果要在脚本层修改slowdownMulti，回传的一定要是浮点型，例如需要赋值1.0而不是1
  - 有任意slowdownMulti参数被传回非0值时生效减速比例
  - slowdownMulti参数更像是一个Buff，例如并不是立刻计算，而是先保存在实体属性里延后计算、在已经有slowdownMulti属性的情况下会取最低的值、免疫掉落伤害等，与原版蜘蛛网逻辑基本一致。

### EntityStopRidingEvent {#entitystopridingevent}

触发时机：当实体停止骑乘时

信号：[client.beforeEvents.entityStopRiding](reference/ClientBeforeEvents.md#entityStopRiding)。分类：实体。

参数类型：[ClientEntityStopRidingBeforeEvent](reference/ClientEntityStopRidingBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("EntityStopRidingEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `entity` | `id` | [str](../common/type-system.md#str) | 只读 | 实体id |
| `mount` | `rideId` | [str](../common/type-system.md#str) | 只读 | 坐骑id |
| `exitFromRider` | `exitFromRider` | [bool](../common/type-system.md#bool) | 只读 | 是否下坐骑 |
| `entityIsBeingDestroyed` | `entityIsBeingDestroyed` | [bool](../common/type-system.md#bool) | 只读 | 坐骑是否将要销毁 |
| `switchingRides` | `switchingRides` | [bool](../common/type-system.md#bool) | 只读 | 是否换乘坐骑 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True可以取消（需要与服务端事件一同取消） |

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

### ExtinguishFireClientEvent {#extinguishfireclientevent}

玩家扑灭火焰时触发。下雨，倒水等方式熄灭火焰不会触发。

信号：[client.beforeEvents.extinguishFire](reference/ClientBeforeEvents.md#extinguishFire)。分类：玩家。

参数类型：[ClientExtinguishFireBeforeEvent](reference/ClientExtinguishFireBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("ExtinguishFireClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `pos` | `pos` | [tuple](../common/type-system.md#tuple)([float](../common/type-system.md#float),[float](../common/type-system.md#float),[float](../common/type-system.md#float)) | 只读 | 火焰方块的坐标 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 修改为True时，可阻止玩家扑灭火焰。需要与ExtinguishFireServerEvent一起修改。 |

### OnAfterFallOnBlockClientEvent {#onafterfallonblockclientevent}

触发时机：当实体降落到方块后客户端触发，主要用于力的计算

信号：[client.beforeEvents.fallOnBlockMotion](reference/ClientBeforeEvents.md#fallOnBlockMotion)。分类：方块。

参数类型：[ClientFallOnBlockMotionBeforeEvent](reference/ClientFallOnBlockMotionBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("OnAfterFallOnBlockClientEvent")`。

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
  - 如果需要修改实体的力，最好配合服务端事件同步修改，避免产生非预期现象
  - 因为引擎最后一定会按照原版方块规则计算力（普通方块置0，床、粘液块等反弹），所以脚本层如果想直接修改当前力需要将calculate设为true取消原版计算，按照传回值计算
  - 引擎在落地之后OnAfterFallOnBlockClientEvent会一直触发，因此请在脚本层中做对应的逻辑判断

### FallingBlockCauseDamageBeforeClientEvent {#fallingblockcausedamagebeforeclientevent}

触发时机：当下落的方块开始计算砸到实体的伤害时，客户端触发该事件

信号：[client.beforeEvents.fallingBlockCauseDamage](reference/ClientBeforeEvents.md#fallingBlockCauseDamage)。分类：方块。

参数类型：[ClientFallingBlockCauseDamageBeforeEvent](reference/ClientFallingBlockCauseDamageBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("FallingBlockCauseDamageBeforeClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `fallingBlock` | `fallingBlockId` | [int](../common/type-system.md#int) | 只读 | 下落的方块实体id |
| `fallingBlockX` | `fallingBlockX` | [float](../common/type-system.md#float) | 只读 | 下落的方块实体位置x |
| `fallingBlockY` | `fallingBlockY` | [float](../common/type-system.md#float) | 只读 | 下落的方块实体位置y |
| `fallingBlockZ` | `fallingBlockZ` | [float](../common/type-system.md#float) | 只读 | 下落的方块实体位置z |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 重力方块的identifier，包含命名空间及名称 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 下落的方块实体维度id |
| `collidingEntities` | `collidingEntitys` | [list](../common/type-system.md#list)([str](../common/type-system.md#str)) | 只读 | 当前碰撞到的实体列表id（客户端只能获取到玩家），如果没有的话是[None](../common/type-system.md#none) |
| `fallTickAmount` | `fallTickAmount` | [int](../common/type-system.md#int) | 只读 | 下落的方块实体持续下落了多少tick |
| `fallDistance` | `fallDistance` | [float](../common/type-system.md#float) | 只读 | 下落的方块实体持续下落了多少距离 |
| `isHarmful` | `isHarmful` | [bool](../common/type-system.md#bool) | 只读 | 客户端始终为false，因为客户端不会计算伤害值 |
| `fallDamage` | `fallDamage` | [int](../common/type-system.md#int) | 只读 | 对实体的伤害 |

**原生前提与限制：**

- 不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义重力方块）
  - 当该事件的参数数据（fallTickAmount，fallDistance，collidingEntitys，fallDamage）与服务端事件FallingBlockCauseDamageBeforeServerEvent数据有差异时，请以服务端事件数据为准。

### HoldBeforeClientEvent {#holdbeforeclientevent}

玩家长按屏幕，即将响应到游戏内时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以监听[RightClickBeforeClientEvent](events.md#rightclickbeforeclientevent)事件

信号：`client.beforeEvents.getNativeEvent('HoldBeforeClientEvent')`。分类：控制。

参数类型：[ClientHoldBeforeEvent](reference/ClientHoldBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("HoldBeforeClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True可拦截原版的挖方块/使用物品/与实体交互响应 |

**原生前提与限制：**

- 玩家长按屏幕的处理顺序为：
    1. 玩家点击屏幕，在长按判定时间内（默认为400毫秒，可通过SetHoldTimeThreshold接口修改）一直没有进行拖动或松手
    1. 触发该事件
    1. 若事件没有cancel，则根据主手上的物品，准心处的物体类型以及与玩家的距离，进行挖方块/使用物品/与实体交互等操作
       即该事件只会在到达长按判定时间的瞬间触发一次，后面一直按住不会连续触发，可以使用[TapOrHoldReleaseClientEvent](events.md#taporholdreleaseclientevent)监听长按后松手
  - 与[TapBeforeClientEvent](events.md#tapbeforeclientevent)事件类似，被ui层捕获，没有穿透到世界的点击不会触发该事件
  - 点触流程的图片讲解见[TapOrHoldReleaseClientEvent](events.md#taporholdreleaseclientevent)事件的备注

### ClientPlayerInventoryOpenEvent {#clientplayerinventoryopenevent}

打开物品背包界面时触发

信号：[client.beforeEvents.inventoryOpen](reference/ClientBeforeEvents.md#inventoryOpen)。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientInventoryOpenBeforeEvent](reference/ClientInventoryOpenBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("ClientPlayerInventoryOpenEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `isCreative` | `isCreative` | [bool](../common/type-system.md#bool) | 只读 | 是否是创造模式背包界面 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 取消打开物品背包界面 |

### ItemReleaseUsingClientEvent {#itemreleaseusingclientevent}

触发时机：释放正在使用的物品

信号：[client.beforeEvents.itemReleaseUsing](reference/ClientBeforeEvents.md#itemReleaseUsing)。分类：物品。

参数类型：[ClientItemReleaseUsingBeforeEvent](reference/ClientItemReleaseUsingBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("ItemReleaseUsingClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `durationLeft` | `durationLeft` | [float](../common/type-system.md#float) | 只读 | 蓄力剩余时间(当物品缺少"minecraft:maxduration"组件时,蓄力剩余时间为负数) |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 使用的物品的物品信息字典 |
| `maxUseDuration` | `maxUseDuration` | [int](../common/type-system.md#int) | 只读 | 最大蓄力时长 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True可以取消，需要同时取消服务端事件[ItemReleaseUsingServerEvent](../server/native-events.md#itemreleaseusingserverevent) |

### ClientItemTryUseEvent {#clientitemtryuseevent}

玩家点击右键尝试使用物品时客户端抛出的事件，可以通过设置cancel为True取消使用物品。

信号：`client.beforeEvents.getNativeEvent('ClientItemTryUseEvent')`。分类：物品。

参数类型：[ClientItemUseBeforeEvent](reference/ClientItemUseBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("ClientItemTryUseEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 使用的物品的物品信息字典 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 取消使用物品 |

**原生前提与限制：**

- ClientItemTryUseEvent事件设置cancel时即可取消使用，无需服务端ServerItemTryUseEvent再次cancel，且服务端事件将不再触发。
  - [ServerItemTryUseEvent](../server/native-events.md#serveritemtryuseevent)/ClientItemTryUseEvent不能取消对方块使用物品的行为，如使用生物蛋，使用桶倒出/收集，使用打火石点燃草等；如果想要取消这种行为，请使用ClientItemUseOnEvent和ServerItemUseOnEvent

### ClientItemUseOnEvent {#clientitemuseonevent}

玩家在对方块使用物品时客户端抛出的事件。

信号：`client.beforeEvents.getNativeEvent('ClientItemUseOnEvent')`。分类：物品。

参数类型：[ClientItemUseOnBeforeEvent](reference/ClientItemUseOnBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("ClientItemUseOnEvent")`。

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
| `clickX` | `clickX` | [float](../common/type-system.md#float) | 只读 | 点击点的x比例位置 |
| `clickY` | `clickY` | [float](../common/type-system.md#float) | 只读 | 点击点的y比例位置 |
| `clickZ` | `clickZ` | [float](../common/type-system.md#float) | 只读 | 点击点的z比例位置 |
| `ret` | `ret` | [bool](../common/type-system.md#bool) | 同步回调中 | 设为True可取消物品的使用 |

取消映射：`event.cancel = True` 等价于 `event.ret = True`。只影响该原生动作。

**原生前提与限制：**

- 事件设置ret = True 时即可取消使用，无需服务端再次设置ServerItemUseOnEvent取消，且服务端事件将不再触发。

### ClientJumpButtonPressDownEvent {#clientjumpbuttonpressdownevent}

跳跃按钮按下事件，返回值设置参数只对当次按下事件起作用

信号：[client.beforeEvents.jumpButtonPress](reference/ClientBeforeEvents.md#jumpButtonPress)。分类：控制。

参数类型：[ClientJumpButtonPressBeforeEvent](reference/ClientJumpButtonPressBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("ClientJumpButtonPressDownEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `continueJump` | `continueJump` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置是否执行跳跃逻辑 |

取消映射：`event.cancel = True` 等价于 `event.continueJump = False`。只影响该原生动作。

### LeftClickBeforeClientEvent {#leftclickbeforeclientevent}

玩家按下攻击/摧毁键时触发，例如鼠标左键、新触控攻击键、手柄右扳机键。鼠标左键仅在pc的普通控制模式（即非F11模式）下触发

信号：`client.beforeEvents.getNativeEvent('LeftClickBeforeClientEvent')`。分类：控制。

参数类型：[ClientLeftClickBeforeEvent](reference/ClientLeftClickBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("LeftClickBeforeClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True可拦截原版的挖方块或攻击响应 |

**原生前提与限制：**

- 按键控制流程的图片讲解见[TapOrHoldReleaseClientEvent](events.md#taporholdreleaseclientevent)事件的备注

### PlayMusicClientEvent {#playmusicclientevent}

播放背景音乐时触发

信号：[client.beforeEvents.playMusic](reference/ClientBeforeEvents.md#playMusic)。分类：音效。

参数类型：[ClientPlayMusicBeforeEvent](reference/ClientPlayMusicBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("PlayMusicClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `name` | `name` | [str](../common/type-system.md#str) | 只读 | 即资源包中sounds/music_definitions.json中的event_name，并且对应sounds/sound_definitions.json中的key |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设为True可屏蔽该次音效播放 |

### PlaySoundClientEvent {#playsoundclientevent}

播放场景音效或UI音效时触发

信号：[client.beforeEvents.playSound](reference/ClientBeforeEvents.md#playSound)。分类：音效。

参数类型：[ClientPlaySoundBeforeEvent](reference/ClientPlaySoundBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("PlaySoundClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `name` | `name` | [str](../common/type-system.md#str) | 只读 | 即资源包中sounds/sound_definitions.json中的key |
| `pos` | `pos` | [tuple](../common/type-system.md#tuple)([float](../common/type-system.md#float),[float](../common/type-system.md#float),[float](../common/type-system.md#float)) | 只读 | 音效播放的位置。UI音效为(0,0,0) |
| `volume` | `volume` | [float](../common/type-system.md#float) | 只读 | 音量，范围为0-1 |
| `pitch` | `pitch` | [float](../common/type-system.md#float) | 只读 | 播放速度，正常速度为1 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设为True可屏蔽该次音效播放 |

### PlayerTryDestroyBlockClientEvent {#playertrydestroyblockclientevent}

当玩家即将破坏方块时，客户端线程触发该事件。主要用于床，旗帜，箱子这些根据方块实体数据进行渲染的方块，一般情况下请使用[ServerPlayerTryDestroyBlockEvent](../server/native-events.md#serverplayertrydestroyblockevent)

信号：[client.beforeEvents.playerBreakBlock](reference/ClientBeforeEvents.md#playerBreakBlock)。分类：方块。

参数类型：[ClientPlayerBreakBlockBeforeEvent](reference/ClientPlayerBreakBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("PlayerTryDestroyBlockClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `face` | `face` | [int](../common/type-system.md#int) | 只读 | 方块被敲击的面向id，参考Facing枚举 |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxData` | `auxData` | [int](../common/type-system.md#int) | 只读 | 方块附加值 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 试图破坏方块的玩家ID |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 默认为False，在脚本层设置为True就能取消该方块的破坏 |

### PlayerTryAddCustomContainerItemClientEvent {#playertryaddcustomcontaineritemclientevent}

玩家尝试将物品添加到自定义容器时触发该事件

信号：[client.beforeEvents.playerTryAddCustomContainerItem](reference/ClientBeforeEvents.md#playerTryAddCustomContainerItem)。分类：物品。

参数类型：[ClientPlayerTryAddCustomContainerItemBeforeEvent](reference/ClientPlayerTryAddCustomContainerItemBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("PlayerTryAddCustomContainerItemClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 尝试添加物品的物品信息字典 |
| `collectionName` | `collectionName` | [str](../common/type-system.md#str) | 只读 | 放入容器名称，对应容器json中"custom_description"字段 |
| `collectionType` | `collectionType` | [str](../common/type-system.md#str) | 只读 | 放入容器类型，目前仅支持netease_container和netease_ui_container |
| `collectionIndex` | `collectionIndex` | [int](../common/type-system.md#int) | 只读 | 放入容器索引 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 容器方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 容器方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 容器方块z坐标 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消该操作，默认为false，事件中改为true时拒绝此次放入自定义容器的操作 |

**原生前提与限制：**

- 容器内物品移动，合堆，分堆的操作会分多次事件触发并且顺序不定，编写逻辑时请勿依赖事件触发顺序
  - cancel取消本次操作后不会触发对应服务端事件

### PlayerTryDropItemClientEvent {#playertrydropitemclientevent}

触发时机：玩家丢弃物品时触发

信号：[client.beforeEvents.playerTryDropItem](reference/ClientBeforeEvents.md#playerTryDropItem)。分类：物品。

参数类型：[ClientPlayerTryDropItemBeforeEvent](reference/ClientPlayerTryDropItemBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("PlayerTryDropItemClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 物品[dict](../common/type-system.md#dict) |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消此次操作 |

### PlayerTryPutCustomContainerItemClientEvent {#playertryputcustomcontaineritemclientevent}

玩家尝试将物品放入自定义容器时触发该事件

信号：[client.beforeEvents.playerTryPutCustomContainerItem](reference/ClientBeforeEvents.md#playerTryPutCustomContainerItem)。分类：物品。

参数类型：[ClientPlayerTryPutCustomContainerItemBeforeEvent](reference/ClientPlayerTryPutCustomContainerItemBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("PlayerTryPutCustomContainerItemClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 尝试放入物品的物品信息字典 |
| `collectionName` | `collectionName` | [str](../common/type-system.md#str) | 只读 | 放入容器名称，对应容器json中"custom_description"字段 |
| `collectionType` | `collectionType` | [str](../common/type-system.md#str) | 只读 | 放入容器类型，目前仅支持netease_container和netease_ui_container |
| `collectionIndex` | `collectionIndex` | [int](../common/type-system.md#int) | 只读 | 放入容器索引 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 容器方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 容器方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 容器方块z坐标 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消该操作，默认为false，事件中改为true时拒绝此次放入自定义容器的操作 |

**原生前提与限制：**

- 该事件只有目标槽位为空或交换物品时触发，如果目标槽位有相同物品时只会触发PlayerTryAddCustomContainerItemServerEvent事件
  - PC存在shift键移动全部物品，放入同种物品时，可能会触发tryadd和tryput，请开发者注意适配
  - 容器内物品移动，合堆，分堆的操作会分多次事件触发并且顺序不定，编写逻辑时请勿依赖事件触发顺序
  - cancel取消本次操作后不会触发对应服务端事件

### PlayerTryRemoveCustomContainerItemClientEvent {#playertryremovecustomcontaineritemclientevent}

玩家尝试从自定义容器中移除物品时触发该事件

信号：[client.beforeEvents.playerTryRemoveCustomContainerItem](reference/ClientBeforeEvents.md#playerTryRemoveCustomContainerItem)。分类：物品。

参数类型：[ClientPlayerTryRemoveCustomContainerItemBeforeEvent](reference/ClientPlayerTryRemoveCustomContainerItemBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("PlayerTryRemoveCustomContainerItemClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `itemDict` | `itemDict` | [dict](../common/type-system.md#dict) | 只读 | 尝试移除物品的物品信息字典 |
| `collectionName` | `collectionName` | [str](../common/type-system.md#str) | 只读 | 放入容器名称，对应容器json中"custom_description"字段 |
| `collectionType` | `collectionType` | [str](../common/type-system.md#str) | 只读 | 放入容器类型，目前仅支持netease_container和netease_ui_container |
| `collectionIndex` | `collectionIndex` | [int](../common/type-system.md#int) | 只读 | 目标容器索引 |
| `x` | `x` | [int](../common/type-system.md#int) | 只读 | 容器方块x坐标 |
| `y` | `y` | [int](../common/type-system.md#int) | 只读 | 容器方块y坐标 |
| `z` | `z` | [int](../common/type-system.md#int) | 只读 | 容器方块z坐标 |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否取消该操作，默认为false，事件中改为true时拒绝此次移除物品的操作 |

**原生前提与限制：**

- 该事件在关闭容器物品自动返回背包时也会触发，此时如果取消操作物品将会被留在容器中，容器被破坏物品也不会掉落（因为实际存储于玩家身上），当再次打开netease_ui_container容器时会显示。
  - 容器内物品移动，合堆，分堆的操作会分多次事件触发并且顺序不定，编写逻辑时请勿依赖事件触发顺序
  - cancel取消本次操作后不会触发对应服务端事件

### PopScreenEvent {#popscreenevent}

screen移除触发

信号：`client.beforeEvents.getNativeEvent('PopScreenEvent')`。分类：[UI](../server_ui/reference/UI.md)。

参数类型：[ClientPopScreenBeforeEvent](reference/ClientPopScreenBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("PopScreenEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `screenName` | `screenName` | [str](../common/type-system.md#str) | 只读 | UI名字 |
| `screenDef` | `screenDef` | [str](../common/type-system.md#str) | 只读 | 包含命名空间的UI名字，格式为namespace.screenName |

**原生前提与限制：**

- screenName为正在弹出的Screen名，如果需要获取下一个Screen可使用PopScreenAfterClientEvent

### RightClickBeforeClientEvent {#rightclickbeforeclientevent}

玩家按下使用物品/放置方块键时触发，例如鼠标右键、新触控交互键、手柄左扳机键

信号：`client.beforeEvents.getNativeEvent('RightClickBeforeClientEvent')`。分类：控制。

参数类型：[ClientRightClickBeforeEvent](reference/ClientRightClickBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("RightClickBeforeClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True可拦截原版的物品使用/实体交互响应 |

**原生前提与限制：**

- 按键控制流程的图片讲解见[TapOrHoldReleaseClientEvent](events.md#taporholdreleaseclientevent)事件的备注

### UnLoadClientAddonScriptsBefore {#unloadclientaddonscriptsbefore}

客户端卸载mod之前触发

信号：[client.beforeEvents.scriptsUnload](reference/ClientBeforeEvents.md#scriptsUnload)。分类：世界。

参数类型：[ClientScriptsUnloadBeforeEvent](reference/ClientScriptsUnloadBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("UnLoadClientAddonScriptsBefore")`。

此事件没有文档规定的参数字段；仍可用 `getNativeData()` 查看引擎附带的数据。

### ShearsDestoryBlockBeforeClientEvent {#shearsdestoryblockbeforeclientevent}

触发时机：玩家手持剪刀破坏方块时，有剪刀特殊效果的方块会在客户端线程触发该事件

信号：[client.beforeEvents.shearsDestroyBlock](reference/ClientBeforeEvents.md#shearsDestroyBlock)。分类：方块。

参数类型：[ClientShearsDestroyBlockBeforeEvent](reference/ClientShearsDestroyBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("ShearsDestoryBlockBeforeClientEvent")`。

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

- 目前仅绊线会触发，需要取消剪刀效果得配合ShearsDestoryBlockBeforeServerEvent同时使用

### OnStandOnBlockClientEvent {#onstandonblockclientevent}

触发时机：当实体站立到方块上时客户端持续触发

信号：[client.beforeEvents.standOnBlock](reference/ClientBeforeEvents.md#standOnBlock)。分类：方块。

参数类型：[ClientStandOnBlockBeforeEvent](reference/ClientStandOnBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("OnStandOnBlockClientEvent")`。

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
  - 如果要在脚本层修改motion/cancel，强烈建议配合OnStandOnBlockServerEvent服务端事件同步修改，避免出现被服务端矫正等非预期现象
  - 如果要在脚本层修改motion，回传的一定要是浮点型，例如需要赋值0.0而不是0

### StartDestroyBlockClientEvent {#startdestroyblockclientevent}

玩家开始挖方块时触发。创造模式下不触发。

信号：[client.beforeEvents.startDestroyBlock](reference/ClientBeforeEvents.md#startDestroyBlock)。分类：方块。

参数类型：[ClientStartDestroyBlockBeforeEvent](reference/ClientStartDestroyBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("StartDestroyBlockClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `pos` | `pos` | [tuple](../common/type-system.md#tuple)([float](../common/type-system.md#float),[float](../common/type-system.md#float),[float](../common/type-system.md#float)) | 只读 | 方块的坐标 |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `auxValue` | `auxValue` | [int](../common/type-system.md#int) | 只读 | 方块的附加值 |
| `player` | `playerId` | [str](../common/type-system.md#str) | 只读 | 玩家id |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 修改为True时，可阻止玩家进入挖方块的状态。需要与StartDestroyBlockServerEvent一起修改。 |
| `face` | `face` | [int](../common/type-system.md#int) | 只读 | 方块被敲击面,参考Facing枚举 |

**原生前提与限制：**

- 如果是隔着火焰挖方块，即使将该事件cancel掉，火焰也会被扑灭。如果要阻止火焰扑灭，需要配合ExtinguishFireClientEvent使用

### StepOnBlockClientEvent {#steponblockclientevent}

触发时机：实体刚移动至一个新实心方块时触发。

信号：[client.beforeEvents.stepOnBlock](reference/ClientBeforeEvents.md#stepOnBlock)。分类：方块。

参数类型：[ClientStepOnBlockBeforeEvent](reference/ClientStepOnBlockBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("StepOnBlockClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 是否允许触发，默认为False，若设为True，可阻止触发后续原版逻辑 |
| `blockX` | `blockX` | [int](../common/type-system.md#int) | 只读 | 方块x坐标 |
| `blockY` | `blockY` | [int](../common/type-system.md#int) | 只读 | 方块y坐标 |
| `blockZ` | `blockZ` | [int](../common/type-system.md#int) | 只读 | 方块z坐标 |
| `entity` | `entityId` | [str](../common/type-system.md#str) | 只读 | 触发的entity的唯一ID |
| `blockName` | `blockName` | [str](../common/type-system.md#str) | 只读 | 方块的identifier，包含命名空间及名称 |
| `dimension` | `dimensionId` | [int](../common/type-system.md#int) | 只读 | 维度id |

**原生前提与限制：**

- 在合并微软更新之后，本事件触发时机与微软molang实验性玩法组件"minecraft:on_step_on"一致
  - 版本更新后，不再支持压力板和拌线钩这两种非实心方块触发此事件，如需监听请参考OnEntityInsideBlockServerEvent事件。
  - 不是所有方块都会触发该事件，自定义方块需要在json中先配置触发开关（详情参考：自定义方块JSON组件），
    原版方块需要先通过RegisterOnStepOn接口注册才能触发。原版的红石矿默认注册了，但深层红石矿没有默认注册。
  - 如果需要修改cancel，强烈建议配合服务端事件同步修改，避免出现被服务端矫正等非预期现象。

### TapBeforeClientEvent {#tapbeforeclientevent}

玩家点击屏幕并松手，即将响应到游戏内时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以监听[LeftClickBeforeClientEvent](events.md#leftclickbeforeclientevent)事件

信号：`client.beforeEvents.getNativeEvent('TapBeforeClientEvent')`。分类：控制。

参数类型：[ClientTapBeforeEvent](reference/ClientTapBeforeEvent.md)；属性名、类型、读写性及完整示例见类型页。

按原生名取得同一信号：`client.beforeEvents.getNativeEvent("TapBeforeClientEvent")`。

| 属性 | 原生字段 | 原生类型 | 写入 | 说明 |
| --- | --- | --- | --- | --- |
| `cancel` | `cancel` | [bool](../common/type-system.md#bool) | 同步回调中 | 设置为True可拦截原版的攻击或放置响应 |

**原生前提与限制：**

- 玩家点击屏幕的处理顺序为：
    1. 玩家点击屏幕，没有进行拖动，并在短按判定时间（250毫秒）内松手
    1. 触发该事件
    1. 若事件没有cancel，则根据准心处的物体类型以及与玩家的距离，进行攻击或放置等操作
  - 与GetEntityByCoordEvent事件不同的是，被ui层捕获，没有穿透到世界的点击不会触发该事件，例如：
    1. 点击原版的移动/跳跃等按钮
    1. 通过SetIsHud(0)屏蔽了游戏操作
    1. 对按钮使用AddTouchEventHandler接口时isSwallow参数设置为True
  - 点触流程的图片讲解见[TapOrHoldReleaseClientEvent](events.md#taporholdreleaseclientevent)事件的备注