---
sidebar_position: 1
title: 客户端
---

# 客户端

入口：`from ModSAPI.client.beta import client`。所有操作只影响本机；客户端数据不能替代服务端权限校验。

[场景与完整示例](../examples.md) · [支持情况与差异](../compatibility.md)

<div className="modsapi-table-scroll" tabIndex={0} aria-label="接口表格，可横向滚动">

| 类型 | 说明 |
| --- | --- |
| [Audio](reference/Audio.md) | 播放本地音效和背景音乐；原生调用失败时明确抛出异常。 |
| [Camera](reference/Camera.md) | 微软相机预设的占位接口；原生相机控制请使用 [client.camera](apis/manager.md#camera)。未支持的方法会抛出异常。 |
| [Client](apis/manager.md) | 客户端统一入口。网易扩展遵循 SAPI 的命名和选项风格。原生服务属于当前会话；Destroy 后操作会抛出 [InvalidClientObjectError](../common/reference/InvalidClientObjectError.md)。身份属性和 afterEvents 仍可读取以便清理；原生操作异常保留方法名和失败码。 |
| [ClientAchievementButtonMovedAfterEvent](reference/ClientAchievementButtonMovedAfterEvent.md) | [AchievementButtonMovedClientEvent](events.md#achievementbuttonmovedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientActorAcquiredItemAfterEvent](reference/ClientActorAcquiredItemAfterEvent.md) | [ActorAcquiredItemClientEvent](events.md#actoracquireditemclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientActorUseItemAfterEvent](reference/ClientActorUseItemAfterEvent.md) | [ActorUseItemClientEvent](events.md#actoruseitemclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientAfterEvents](reference/ClientAfterEvents.md) | 客户端通知集合，包括有文档说明的原生后置钩子。 |
| [ClientAnvilCreateResultItemAfterEvent](reference/ClientAnvilCreateResultItemAfterEvent.md) | [AnvilCreateResultItemAfterClientEvent](events.md#anvilcreateresultitemafterclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientApproachEntityAfterEvent](reference/ClientApproachEntityAfterEvent.md) | [ApproachEntityClientEvent](events.md#approachentityclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientAttackAnimBeginAfterEvent](reference/ClientAttackAnimBeginAfterEvent.md) | [AttackAnimBeginClientEvent](events.md#attackanimbeginclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientAttackAnimEndAfterEvent](reference/ClientAttackAnimEndAfterEvent.md) | [AttackAnimEndClientEvent](events.md#attackanimendclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientBackButtonReleaseAfterEvent](reference/ClientBackButtonReleaseAfterEvent.md) | [OnBackButtonReleaseClientEvent](events.md#onbackbuttonreleaseclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientBeforeEvents](reference/ClientBeforeEvents.md) | 待执行操作和原生输出变化的客户端同步钩子。只能修改开发包明确标记为可写的字段，且必须在回调内完成。部分操作需要客户端和服务端共同取消，具体见事件目录。此处不实现微软的受限执行阶段。 |
| [ClientBlockAnimateRandomTickAfterEvent](reference/ClientBlockAnimateRandomTickAfterEvent.md) | [BlockAnimateRandomTickEvent](events.md#blockanimaterandomtickevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientBlockUseBeforeEvent](reference/ClientBlockUseBeforeEvent.md) | [ClientBlockUseEvent](events.md#clientblockuseevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientCamera](reference/ClientCamera.md) | 控制本地原生相机，向量须为有限数，角度单位为度。参数不合法时抛出 [TypeError](../common/type-system.md#typeerror) 或 [ValueError](../common/type-system.md#valueerror)；原生拒绝操作时抛出 [NativeOperationError](../common/reference/NativeOperationError.md)。改动是临时的，可能在下一渲染帧才可见。 |
| [ClientCameraMotionStartAfterEvent](reference/ClientCameraMotionStartAfterEvent.md) | [CameraMotionStartClientEvent](events.md#cameramotionstartclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientCameraMotionStopBeforeEvent](reference/ClientCameraMotionStopBeforeEvent.md) | [CameraMotionStopClientEvent](events.md#cameramotionstopclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientChestCloseAfterEvent](reference/ClientChestCloseAfterEvent.md) | [ClientChestCloseEvent](events.md#clientchestcloseevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientChestOpenAfterEvent](reference/ClientChestOpenAfterEvent.md) | [ClientChestOpenEvent](events.md#clientchestopenevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientChunkLoadAfterEvent](reference/ClientChunkLoadAfterEvent.md) | [ChunkLoadedClientEvent](events.md#chunkloadedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientChunkUnloadBeforeEvent](reference/ClientChunkUnloadBeforeEvent.md) | [ChunkAcquireDiscardedClientEvent](events.md#chunkacquirediscardedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientCloseNeteaseShopAfterEvent](reference/ClientCloseNeteaseShopAfterEvent.md) | [CloseNeteaseShopEvent](events.md#closeneteaseshopevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientCommandOutputAfterEvent](reference/ClientCommandOutputAfterEvent.md) | [OnCommandOutputClientEvent](events.md#oncommandoutputclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientContainer](reference/ClientContainer.md) | 实时只读的本地玩家背包，容量来自原生结果。不长期缓存物品或容量。检查多个槽位时优先使用 getItems，一次完成批量读取；单格完整读取先查询轻量边界，再使用 GetPlayerItem 获取目标格数据。 |
| [ClientContainerSlot](reference/ClientContainerSlot.md) | 实时只读的背包或装备槽位，空槽位仍然有效。 |
| [ClientControlMode](reference/ClientControlMode.md) | 明确指定原生触控布局和交互方式。 |
| [ClientControlModeOptions](reference/ClientControlModeOptions.md) | 可选的原生模式锁定配置，在请求布局之后应用。 |
| [ClientCraftUpdateResultItemAfterEvent](reference/ClientCraftUpdateResultItemAfterEvent.md) | [CraftUpdateResultItemClientEvent](events.md#craftupdateresultitemclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientCustomGamepadChangeAfterEvent](reference/ClientCustomGamepadChangeAfterEvent.md) | [OnCustomGamepadChangedEvent](events.md#oncustomgamepadchangedevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientCustomGamepadPressInGameAfterEvent](reference/ClientCustomGamepadPressInGameAfterEvent.md) | [OnCustomGamepadPressInGame](events.md#oncustomgamepadpressingame) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientCustomKeyChangeAfterEvent](reference/ClientCustomKeyChangeAfterEvent.md) | [OnCustomKeyChangedEvent](events.md#oncustomkeychangedevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientCustomKeyPressInGameAfterEvent](reference/ClientCustomKeyPressInGameAfterEvent.md) | [OnCustomKeyPressInGame](events.md#oncustomkeypressingame) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientDimension](reference/ClientDimension.md) | 客户端观察到的维度，身份信息在会话结束后仍可读取。此对象描述被观察的维度，不一定是当前可见维度；不会赋予访问未加载区块或服务端的能力。 |
| [ClientEntity](reference/ClientEntity.md) | 客户端可见实体的包装对象；仅允许移除由本地创建的实体。 |
| [ClientEntityAddAfterEvent](reference/ClientEntityAddAfterEvent.md) | [AddEntityClientEvent](events.md#addentityclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientEntityAttributeComponent](reference/ClientEntityAttributeComponent.md) | 通过 entity.getComponent() 取得的实时只读客户端属性。仅提供已同步的当前值和最大值；默认值、最小值及权威修改需使用服务端接口。原生客户端未同步权威的攻击伤害、击退抗性和跳跃强度，因此不提供这些属性。 |
| [ClientEntityCollideAfterEvent](reference/ClientEntityCollideAfterEvent.md) | [OnMobHitMobClientEvent](events.md#onmobhitmobclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientEntityComponentTypes](reference/ClientEntityComponentTypes.md) | 已支持的只读客户端组件标识符，包括本地背包。 |
| [ClientEntityEquippableComponent](reference/ClientEntityEquippableComponent.md) | 本地玩家只读六槽装备，实际写入应在服务端完成。 |
| [ClientEntityHealthChangedAfterEvent](reference/ClientEntityHealthChangedAfterEvent.md) | [HealthChangeClientEvent](events.md#healthchangeclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientEntityInsideBlockBeforeEvent](reference/ClientEntityInsideBlockBeforeEvent.md) | [OnEntityInsideBlockClientEvent](events.md#onentityinsideblockclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientEntityInventoryComponent](reference/ClientEntityInventoryComponent.md) | 本地玩家只读背包入口，不提供全部背包 JSON 配置。 |
| [ClientEntityLandAfterEvent](reference/ClientEntityLandAfterEvent.md) | [OnGroundClientEvent](events.md#ongroundclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientEntityModelChangeAfterEvent](reference/ClientEntityModelChangeAfterEvent.md) | [EntityModelChangedClientEvent](events.md#entitymodelchangedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientEntityRemoveAfterEvent](reference/ClientEntityRemoveAfterEvent.md) | [RemoveEntityClientEvent](events.md#removeentityclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientEntitySpawnOptions](reference/ClientEntitySpawnOptions.md) | 本地实体生成选项；rotation 为俯仰角和偏航角，单位为度。 |
| [ClientEntityStopRidingBeforeEvent](reference/ClientEntityStopRidingBeforeEvent.md) | [EntityStopRidingEvent](events.md#entitystopridingevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientEventSignal](reference/ClientEventSignal.md) | 同步原生后置事件信号，按需注册引擎监听。subscribe 返回回调，重复订阅具有幂等性。unsubscribe 可接受同一绑定方法的新引用。各回调的异常独立记录，后续订阅者仍会运行。 |
| [ClientExtinguishFireBeforeEvent](reference/ClientExtinguishFireBeforeEvent.md) | [ExtinguishFireClientEvent](events.md#extinguishfireclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientFallingBlockCauseDamageBeforeEvent](reference/ClientFallingBlockCauseDamageBeforeEvent.md) | [FallingBlockCauseDamageBeforeClientEvent](events.md#fallingblockcausedamagebeforeclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientFallOnBlockMotionBeforeEvent](reference/ClientFallOnBlockMotionBeforeEvent.md) | [OnAfterFallOnBlockClientEvent](events.md#onafterfallonblockclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientGamepadControllerLayoutChangeAfterEvent](reference/ClientGamepadControllerLayoutChangeAfterEvent.md) | [OnGamepadControllerLayoutChangeClientEvent](events.md#ongamepadcontrollerlayoutchangeclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientGamepadKeyPressAfterEvent](reference/ClientGamepadKeyPressAfterEvent.md) | [OnGamepadKeyPressClientEvent](events.md#ongamepadkeypressclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientGamepadStickAfterEvent](reference/ClientGamepadStickAfterEvent.md) | [OnGamepadStickClientEvent](events.md#ongamepadstickclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientGamepadTriggerAfterEvent](reference/ClientGamepadTriggerAfterEvent.md) | [OnGamepadTriggerClientEvent](events.md#ongamepadtriggerclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientGameTypeChangeAfterEvent](reference/ClientGameTypeChangeAfterEvent.md) | [GameTypeChangedClientEvent](events.md#gametypechangedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientGetEntityByCoordAfterEvent](reference/ClientGetEntityByCoordAfterEvent.md) | [GetEntityByCoordEvent](events.md#getentitybycoordevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientGetEntityByCoordReleaseAfterEvent](reference/ClientGetEntityByCoordReleaseAfterEvent.md) | [GetEntityByCoordReleaseClientEvent](events.md#getentitybycoordreleaseclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientGridComponentSizeChangeAfterEvent](reference/ClientGridComponentSizeChangeAfterEvent.md) | [GridComponentSizeChangedClientEvent](events.md#gridcomponentsizechangedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientGrindStoneRemoveEnchantAfterEvent](reference/ClientGrindStoneRemoveEnchantAfterEvent.md) | [GrindStoneRemovedEnchantClientEvent](events.md#grindstoneremovedenchantclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientGyroSensorChangeAfterEvent](reference/ClientGyroSensorChangeAfterEvent.md) | [GyroSensorChangedClientEvent](events.md#gyrosensorchangedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientHoldBeforeEvent](reference/ClientHoldBeforeEvent.md) | [HoldBeforeClientEvent](events.md#holdbeforeclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientHudButtonChangeAfterEvent](reference/ClientHudButtonChangeAfterEvent.md) | [HudButtonChangedClientEvent](events.md#hudbuttonchangedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientInput](reference/ClientInput.md) | 通过 [client.input](apis/manager.md#input) 取得本机输入服务。权限修改只影响当前设备的输入响应，不代表服务端授权。临时覆盖层无需轮询，可叠加管理；直接权限写入修改覆盖层下方的基础值。reset 与客户端退出会尝试恢复所持有的初始值，并保留不同的外部写入。鼠标模拟模式也会保留可读取的初始值。控制布局、布局锁定和原生点击响应没有已核验的读取接口，属于直接配置，不能由 reset 恢复未知旧值。 |
| [ClientInputAction](reference/ClientInputAction.md) | 一次本地原生动作请求，不表示持续按住键盘或按钮。 |
| [ClientInputOverride](reference/ClientInputOverride.md) | 持有独立所有权的权限覆盖层；所属界面关闭时应释放。重叠通道由较晚创建的层优先控制。原生释放失败后可重试，不会释放其他层持有的权限。 |
| [ClientInputPermission](reference/ClientInputPermission.md) | 网易原生输入通道，与微软输入权限类别的含义和组合规则不同。 |
| [ClientInventoryCloseAfterEvent](reference/ClientInventoryCloseAfterEvent.md) | [ClientPlayerInventoryCloseEvent](events.md#clientplayerinventorycloseevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientInventoryOpenBeforeEvent](reference/ClientInventoryOpenBeforeEvent.md) | [ClientPlayerInventoryOpenEvent](events.md#clientplayerinventoryopenevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientItemReadOptions](reference/ClientItemReadOptions.md) | 原生读取选项，includeUserData 默认 True。 |
| [ClientItemReleaseUsingBeforeEvent](reference/ClientItemReleaseUsingBeforeEvent.md) | [ItemReleaseUsingClientEvent](events.md#itemreleaseusingclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientItemSlotButtonClickedAfterEvent](reference/ClientItemSlotButtonClickedAfterEvent.md) | [OnItemSlotButtonClickedEvent](events.md#onitemslotbuttonclickedevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientItemUseBeforeEvent](reference/ClientItemUseBeforeEvent.md) | [ClientItemTryUseEvent](events.md#clientitemtryuseevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientItemUseOnBeforeEvent](reference/ClientItemUseOnBeforeEvent.md) | [ClientItemUseOnEvent](events.md#clientitemuseonevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientJumpButtonPressBeforeEvent](reference/ClientJumpButtonPressBeforeEvent.md) | [ClientJumpButtonPressDownEvent](events.md#clientjumpbuttonpressdownevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientJumpButtonReleaseAfterEvent](reference/ClientJumpButtonReleaseAfterEvent.md) | [ClientJumpButtonReleaseEvent](events.md#clientjumpbuttonreleaseevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientKeyboardControllerLayoutChangeAfterEvent](reference/ClientKeyboardControllerLayoutChangeAfterEvent.md) | [OnKeyboardControllerLayoutChangeClientEvent](events.md#onkeyboardcontrollerlayoutchangeclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientKeyPressAfterEvent](reference/ClientKeyPressAfterEvent.md) | 键盘事件快照，包括整数键码、按下状态和屏幕名称。 |
| [ClientLeaveEntityAfterEvent](reference/ClientLeaveEntityAfterEvent.md) | [LeaveEntityClientEvent](events.md#leaveentityclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientLeftClickBeforeEvent](reference/ClientLeftClickBeforeEvent.md) | [LeftClickBeforeClientEvent](events.md#leftclickbeforeclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientLeftClickReleaseAfterEvent](reference/ClientLeftClickReleaseAfterEvent.md) | [LeftClickReleaseClientEvent](events.md#leftclickreleaseclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientLiquidClippedAfterEvent](reference/ClientLiquidClippedAfterEvent.md) | [LiquidClippedClientEvent](events.md#liquidclippedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientLocalPlayerLoadAfterEvent](reference/ClientLocalPlayerLoadAfterEvent.md) | [OnLocalPlayerStopLoading](events.md#onlocalplayerstoploading) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientModBlockEntityLoadAfterEvent](reference/ClientModBlockEntityLoadAfterEvent.md) | [ModBlockEntityLoadedClientEvent](events.md#modblockentityloadedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientModBlockEntityRemoveAfterEvent](reference/ClientModBlockEntityRemoveAfterEvent.md) | [ModBlockEntityRemoveClientEvent](events.md#modblockentityremoveclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientModBlockEntityTickAfterEvent](reference/ClientModBlockEntityTickAfterEvent.md) | [ModBlockEntityTickClientEvent](events.md#modblockentitytickclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientModBlockNeteaseEffectCreateAfterEvent](reference/ClientModBlockNeteaseEffectCreateAfterEvent.md) | [OnModBlockNeteaseEffectCreatedClientEvent](events.md#onmodblockneteaseeffectcreatedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientMouseMiddleDownAfterEvent](reference/ClientMouseMiddleDownAfterEvent.md) | [OnMouseMiddleDownClientEvent](events.md#onmousemiddledownclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientMouseWheelAfterEvent](reference/ClientMouseWheelAfterEvent.md) | 滚轮事件快照，向上为 +1，向下为 -1。 |
| [ClientMusicOptions](reference/ClientMusicOptions.md) | 原生背景音乐支持音量和循环，不支持淡入。 |
| [ClientMusicStopAfterEvent](reference/ClientMusicStopAfterEvent.md) | 音乐停止通知，不用于标识场景音效实例。 |
| [ClientNativeKeyPressAfterEvent](reference/ClientNativeKeyPressAfterEvent.md) | [OnKeyPressInGame](events.md#onkeypressingame) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientNativeMouseWheelAfterEvent](reference/ClientNativeMouseWheelAfterEvent.md) | [MouseWheelClientEvent](events.md#mousewheelclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientNativeMusicStopAfterEvent](reference/ClientNativeMusicStopAfterEvent.md) | [OnMusicStopClientEvent](events.md#onmusicstopclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientParticleBindOptions](reference/ClientParticleBindOptions.md) | 骨骼空间绑定选项；rotation 与旧名称 rotate 不能同时使用。 |
| [ClientParticleOptions](reference/ClientParticleOptions.md) | 发射器朝向及有限标量 MoLang 变量。 |
| [ClientPerspective](reference/ClientPerspective.md) | [ClientCamera.perspective](reference/ClientCamera.md#perspective) 接受的命名常量。 |
| [ClientPerspectiveChangeAfterEvent](reference/ClientPerspectiveChangeAfterEvent.md) | [PerspChangeClientEvent](events.md#perspchangeclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPhysicsTouchAfterEvent](reference/ClientPhysicsTouchAfterEvent.md) | [PhysxTouchClientEvent](events.md#physxtouchclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPhysicsTriggerAfterEvent](reference/ClientPhysicsTriggerAfterEvent.md) | [PhysxTriggerClientEvent](events.md#physxtriggerclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayer](reference/ClientPlayer.md) | 本地玩家的可读状态及本地显示控制。 |
| [ClientPlayerActionAfterEvent](reference/ClientPlayerActionAfterEvent.md) | [OnLocalPlayerActionClientEvent](events.md#onlocalplayeractionclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerAddCustomContainerItemAfterEvent](reference/ClientPlayerAddCustomContainerItemAfterEvent.md) | [PlayerAddCustomContainerItemClientEvent](events.md#playeraddcustomcontaineritemclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerAttackEntityAfterEvent](reference/ClientPlayerAttackEntityAfterEvent.md) | [PlayerAttackEntityEvent](events.md#playerattackentityevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerBreakBlockBeforeEvent](reference/ClientPlayerBreakBlockBeforeEvent.md) | [PlayerTryDestroyBlockClientEvent](events.md#playertrydestroyblockclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerChatButtonClickAfterEvent](reference/ClientPlayerChatButtonClickAfterEvent.md) | [PlayerChatButtonClickClientEvent](events.md#playerchatbuttonclickclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerDimensionChangeAfterEvent](reference/ClientPlayerDimensionChangeAfterEvent.md) | [DimensionChangeClientEvent](events.md#dimensionchangeclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerDimensionChangeFinishAfterEvent](reference/ClientPlayerDimensionChangeFinishAfterEvent.md) | [DimensionChangeFinishClientEvent](events.md#dimensionchangefinishclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerEnteredViewAfterEvent](reference/ClientPlayerEnteredViewAfterEvent.md) | [AddPlayerAOIClientEvent](events.md#addplayeraoiclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerHitBlockAfterEvent](reference/ClientPlayerHitBlockAfterEvent.md) | [OnPlayerHitBlockClientEvent](events.md#onplayerhitblockclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerHotbarItemChangeAfterEvent](reference/ClientPlayerHotbarItemChangeAfterEvent.md) | [OnCarriedNewItemChangedClientEvent](events.md#oncarriednewitemchangedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerInventoryItemChangeAfterEvent](reference/ClientPlayerInventoryItemChangeAfterEvent.md) | [InventoryItemChangedClientEvent](events.md#inventoryitemchangedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerJumpAfterEvent](reference/ClientPlayerJumpAfterEvent.md) | [OnLocalPlayerStartJumpClientEvent](events.md#onlocalplayerstartjumpclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerLeftViewAfterEvent](reference/ClientPlayerLeftViewAfterEvent.md) | [RemovePlayerAOIClientEvent](events.md#removeplayeraoiclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerPermissionChangeAfterEvent](reference/ClientPlayerPermissionChangeAfterEvent.md) | [PlayerPermissionChangeClientEvent](events.md#playerpermissionchangeclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerRemoveCustomContainerItemAfterEvent](reference/ClientPlayerRemoveCustomContainerItemAfterEvent.md) | [PlayerRemoveCustomContainerItemClientEvent](events.md#playerremovecustomcontaineritemclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerSkinLoadAfterEvent](reference/ClientPlayerSkinLoadAfterEvent.md) | [AddPlayerCreatedClientEvent](events.md#addplayercreatedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerStartMoveAfterEvent](reference/ClientPlayerStartMoveAfterEvent.md) | [OnClientPlayerStartMove](events.md#onclientplayerstartmove) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerStopMoveAfterEvent](reference/ClientPlayerStopMoveAfterEvent.md) | [OnClientPlayerStopMove](events.md#onclientplayerstopmove) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerTryAddCustomContainerItemBeforeEvent](reference/ClientPlayerTryAddCustomContainerItemBeforeEvent.md) | [PlayerTryAddCustomContainerItemClientEvent](events.md#playertryaddcustomcontaineritemclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerTryDropItemBeforeEvent](reference/ClientPlayerTryDropItemBeforeEvent.md) | [PlayerTryDropItemClientEvent](events.md#playertrydropitemclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerTryPutCustomContainerItemBeforeEvent](reference/ClientPlayerTryPutCustomContainerItemBeforeEvent.md) | [PlayerTryPutCustomContainerItemClientEvent](events.md#playertryputcustomcontaineritemclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayerTryRemoveCustomContainerItemBeforeEvent](reference/ClientPlayerTryRemoveCustomContainerItemBeforeEvent.md) | [PlayerTryRemoveCustomContainerItemClientEvent](events.md#playertryremovecustomcontaineritemclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlayMusicBeforeEvent](reference/ClientPlayMusicBeforeEvent.md) | [PlayMusicClientEvent](events.md#playmusicclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPlaySoundBeforeEvent](reference/ClientPlaySoundBeforeEvent.md) | [PlaySoundClientEvent](events.md#playsoundclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPopScreenAfterEvent](reference/ClientPopScreenAfterEvent.md) | [PopScreenAfterClientEvent](events.md#popscreenafterclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPopScreenBeforeEvent](reference/ClientPopScreenBeforeEvent.md) | [PopScreenEvent](events.md#popscreenevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientPushScreenAfterEvent](reference/ClientPushScreenAfterEvent.md) | [PushScreenEvent](events.md#pushscreenevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientRecipeTriggerAfterEvent](reference/ClientRecipeTriggerAfterEvent.md) | [ClientShapedRecipeTriggeredEvent](events.md#clientshapedrecipetriggeredevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientRenderAfterEvent](reference/ClientRenderAfterEvent.md) | [GameRenderTickEvent](events.md#gamerendertickevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientRightClickBeforeEvent](reference/ClientRightClickBeforeEvent.md) | [RightClickBeforeClientEvent](events.md#rightclickbeforeclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientRightClickReleaseAfterEvent](reference/ClientRightClickReleaseAfterEvent.md) | [RightClickReleaseClientEvent](events.md#rightclickreleaseclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientScreenSizeChangeAfterEvent](reference/ClientScreenSizeChangeAfterEvent.md) | [ScreenSizeChangedClientEvent](events.md#screensizechangedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientScriptsLoadAfterEvent](reference/ClientScriptsLoadAfterEvent.md) | [LoadClientAddonScriptsAfter](events.md#loadclientaddonscriptsafter) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientScriptsUnloadBeforeEvent](reference/ClientScriptsUnloadBeforeEvent.md) | [UnLoadClientAddonScriptsBefore](events.md#unloadclientaddonscriptsbefore) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientShearsDestroyBlockBeforeEvent](reference/ClientShearsDestroyBlockBeforeEvent.md) | [ShearsDestoryBlockBeforeClientEvent](events.md#shearsdestoryblockbeforeclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientSoundOptions](reference/ClientSoundOptions.md) | 本地声音选项：位置通常为世界坐标；提供 entity 时为相对偏移。 |
| [ClientStandOnBlockBeforeEvent](reference/ClientStandOnBlockBeforeEvent.md) | [OnStandOnBlockClientEvent](events.md#onstandonblockclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientStartDestroyBlockBeforeEvent](reference/ClientStartDestroyBlockBeforeEvent.md) | [StartDestroyBlockClientEvent](events.md#startdestroyblockclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientStartRidingAfterEvent](reference/ClientStartRidingAfterEvent.md) | [StartRidingClientEvent](events.md#startridingclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientStartUsingItemAfterEvent](reference/ClientStartUsingItemAfterEvent.md) | [StartUsingItemClientEvent](events.md#startusingitemclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientStepOffBlockAfterEvent](reference/ClientStepOffBlockAfterEvent.md) | [StepOffBlockClientEvent](events.md#stepoffblockclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientStepOnBlockBeforeEvent](reference/ClientStepOnBlockBeforeEvent.md) | [StepOnBlockClientEvent](events.md#steponblockclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientStopUsingItemAfterEvent](reference/ClientStopUsingItemAfterEvent.md) | [StopUsingItemClientEvent](events.md#stopusingitemclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientStorageOptions](reference/ClientStorageOptions.md) | isGlobal 用于选择设备全局配置或当前本地存档范围。 |
| [ClientSystemInfo](reference/ClientSystemInfo.md) | 客户端实例的设备信息。 |
| [ClientTapBeforeEvent](reference/ClientTapBeforeEvent.md) | [TapBeforeClientEvent](events.md#tapbeforeclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientTapOrHoldReleaseAfterEvent](reference/ClientTapOrHoldReleaseAfterEvent.md) | [TapOrHoldReleaseClientEvent](events.md#taporholdreleaseclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientTickAfterEvent](reference/ClientTickAfterEvent.md) | [OnScriptTickClient](events.md#onscripttickclient) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientUiInitFinishAfterEvent](reference/ClientUiInitFinishAfterEvent.md) | [UiInitFinished](events.md#uiinitfinished) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientUiReadyAfterEvent](reference/ClientUiReadyAfterEvent.md) | 界面就绪通知，维度切换后可能再次触发。 |
| [ClientUpdatePlayerSkinAfterEvent](reference/ClientUpdatePlayerSkinAfterEvent.md) | [UpdatePlayerSkinClientEvent](events.md#updateplayerskinclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientWalkAnimBeginAfterEvent](reference/ClientWalkAnimBeginAfterEvent.md) | [WalkAnimBeginClientEvent](events.md#walkanimbeginclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientWalkAnimEndAfterEvent](reference/ClientWalkAnimEndAfterEvent.md) | [WalkAnimEndClientEvent](events.md#walkanimendclientevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [ClientWalkMode](reference/ClientWalkMode.md) | 原生选择的行走模式，与实际玩家速度分别读取。 |
| [DynamicParticle](reference/DynamicParticle.md) | 表达式驱动的绘图对象，与原生粒子发射器不同。pattern 接受 x、y、z 和三通道颜色，各项可为数值、[ExpressionString](reference/ExpressionString.md) 或字符串。选项包括 mode（line 或 point）、interval（正数，每单位 1/20 秒）、maxAmount（正整数）和 visible（布尔值）。运行时表达式失败会停止更新、清理图形并设置 lastError。 |
| [DynamicParticleOptions](reference/DynamicParticleOptions.md) | 限制保留的图形数量；interval 每单位为原生的 1/20 秒。 |
| [DynamicParticlePattern](reference/DynamicParticlePattern.md) | 数值或文本表达式；颜色必须包含三个通道。 |
| [ExpressionString](reference/ExpressionString.md) | 签名、字段、属性、方法与调用示例 |
| [Particle](reference/Particle.md) | 单个粒子发射器。原生调用失败会抛出异常；已移除对象拒绝修改。 |
| [SafeEvalError](reference/SafeEvalError.md) | 签名、字段、属性、方法与调用示例 |
| [Screen](reference/Screen.md) | 原生屏幕操作；仅在 afterEvents.uiReady 触发后创建屏幕。 |
| [ScreenManager](reference/ScreenManager.md) | 屏幕管理器。 |
| [ServerEventReceiveAfterEvent](reference/ServerEventReceiveAfterEvent.md) | /scriptevent 命令调用的附加数据。 |
| [ServerEventReceiveAfterEventSignal](reference/ServerEventReceiveAfterEventSignal.md) | 注册用于接收 /scriptevent 命令的事件处理器。 |
| [ServerRequestDataAfterEvent](reference/ServerRequestDataAfterEvent.md) | /scriptevent 命令调用的附加数据。 |
| [ServerRequestDataAfterEventSignal](reference/ServerRequestDataAfterEventSignal.md) | 注册用于接收 /scriptevent 命令的事件处理器。 |
| [SoundPlayback](reference/SoundPlayback.md) | [Audio.playSound](reference/Audio.md#playSound) 返回的场景音效实例。自然播放结束由引擎管理；isStopped 仅记录是否成功请求停止，不能用于判断自然结束。网易文档指出，创建后的七帧内按实例标识停止可能不可靠；建议至少等待十五帧再停止新声音。原生拒绝操作时会报告异常。 |
| [Variable](reference/Variable.md) | 使用注入时钟的表达式上下文；导入模块时不会创建计时器。 |

</div>


## 原生事件

[客户端原生事件目录](events.md) · [事件用法与示例](../guides/native-events.md)


## 推荐事件入口

[客户端语义事件](semantic-events.md) · [语义化设计与示例](../guides/semantic-events.md)