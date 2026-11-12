---
sidebar_position: 1
title: 服务端
---

# 服务端

入口：`from ModSAPI.server.beta import world, system`。其他导出见 [导出符号](../exports.md)。

[场景与完整示例](../examples.md) · [支持情况与差异](../compatibility.md)

<div className="modsapi-table-scroll" tabIndex={0} aria-label="接口表格，可横向滚动">

| 类型 | 说明 |
| --- | --- |
| [Block](apis/block.md) | 维度内某个坐标上的方块包装对象。由维度和唯一的 x、y、z 坐标定位，可读取和设置该位置的方块状态。 |
| [BlockComponent](reference/BlockComponent.md) | 方块组件的基类。 |
| [BlockEvent](reference/BlockEvent.md) | 影响特定方块的事件信息。 |
| [BlockExplodeAfterEvent](reference/BlockExplodeAfterEvent.md) | 投射物命中方块的事件信息。 |
| [BlockExplodeAfterEventSignal](reference/BlockExplodeAfterEventSignal.md) | 管理爆炸影响各个方块时的回调。 |
| [BlockInventoryComponent](reference/BlockInventoryComponent.md) | 世界中方块的库存，例如箱子的容器。 |
| [BlockPermutation](reference/BlockPermutation.md) | 描述方块的 [BlockType](reference/BlockType.md) 与属性组合，属性也称方块状态。此对象不绑定到世界中的具体 [Block](apis/block.md)。 |
| [BlockType](reference/BlockType.md) | 方块的类型或模板；除类型标识外，不包含具体状态组合数据。 |
| [BlockVolume](reference/BlockVolume.md) | 以两个角点描述世界中的三维方块区域。两个角点的分量不要求按最小值、最大值排序，且始终保留初始角点身份；编辑时即使两角点交叉，也不会交换它们的含义。角点不能直接当作已排序的方块位置范围；需要边界范围时使用 getBoundingBox。区域按方块计数并包含端点，因此从 (0, 0, 0) 到 (0, 0, 0) 的区域大小为 (1, 1, 1)。 |
| [BlockVolumeBase](reference/BlockVolumeBase.md) | 签名、字段、属性、方法与调用示例 |
| [ChatSendAfterEvent](reference/ChatSendAfterEvent.md) | 玩家发送聊天消息时的事件。 |
| [ChatSendAfterEventSignal](reference/ChatSendAfterEventSignal.md) | 管理聊天消息发送后的回调。 |
| [ChatSendBeforeEvent](reference/ChatSendBeforeEvent.md) | 玩家发送聊天消息时的事件。 |
| [ChatSendBeforeEventSignal](reference/ChatSendBeforeEventSignal.md) | 管理聊天消息发送前的回调。 |
| [ClientEventReceiveAfterEvent](reference/ClientEventReceiveAfterEvent.md) | /scriptevent 命令调用的附加数据。 |
| [ClientEventReceiveAfterEventSignal](reference/ClientEventReceiveAfterEventSignal.md) | 注册用于接收 /scriptevent 命令的事件处理器。 |
| [ClientRequestDataAfterEvent](reference/ClientRequestDataAfterEvent.md) | /scriptevent 命令调用的附加数据。 |
| [ClientRequestDataAfterEventSignal](reference/ClientRequestDataAfterEventSignal.md) | 注册用于接收 /scriptevent 命令的事件处理器。 |
| [CommandResult](reference/CommandResult.md) | 命令执行结果的数据。 |
| [Component](reference/Component.md) | 组件实现的基类。 |
| [Container](apis/container.md) | 容纳多组物品的容器，可属于玩家、运输矿车、羊驼等实体。 |
| [ContainerSlot](reference/ContainerSlot.md) | 容器内的一个槽位，例如实体库存中的槽位。 |
| [CustomCommandRegistry](reference/CustomCommandRegistry.md) | 签名、字段、属性、方法与调用示例 |
| [DataDrivenEntityTriggerAfterEvent](reference/DataDrivenEntityTriggerAfterEvent.md) | 数据驱动实体事件的订阅入口，例如鸡的 minecraft:ageable_grow_up。 |
| [DataDrivenEntityTriggerEventSignal](reference/DataDrivenEntityTriggerEventSignal.md) | 数据驱动实体事件的订阅入口，例如鸡的 minecraft:ageable_grow_up。 |
| [Dimension](apis/dimension.md) | 世界中的特定维度，例如末地。 |
| [Effect](reference/Effect.md) | 已添加到实体的状态效果，例如中毒。 |
| [EffectAddAfterEvent](reference/EffectAddAfterEvent.md) | 向实体添加状态效果时的信息，例如添加中毒效果。 |
| [EffectAddAfterEventSignal](reference/EffectAddAfterEventSignal.md) | 管理向实体添加效果时的回调。 |
| [EffectType](reference/EffectType.md) | 可添加到实体的效果类型，例如中毒。 |
| [Entity](apis/entity.md) | 世界中的实体状态，包括生物、玩家、矿车等对象。 |
| [EntityAddRiderComponent](reference/EntityAddRiderComponent.md) | 为实体生成时附加指定 entityType 的骑乘者。 |
| [EntityAttributeComponent](reference/EntityAttributeComponent.md) | 通过 AttrType 定位的引擎属性，不使用 EntityComponentType。 |
| [EntityComponent](reference/EntityComponent.md) | 实体组件的基类。 |
| [EntityDieAfterEvent](reference/EntityDieAfterEvent.md) | 游戏中实体死亡的事件数据。 |
| [EntityDieAfterEventSignal](reference/EntityDieAfterEventSignal.md) | 实体死亡后的事件订阅入口。 |
| [EntityEquippableComponent](reference/EntityEquippableComponent.md) | 访问生物的装备槽位。玩家实体具有此组件。 |
| [EntityHealthChangedAfterEvent](reference/EntityHealthChangedAfterEvent.md) | 实体生命值变化的事件信息。请勿在回调中无条件修改该实体生命值，否则可能再次触发事件并造成无限循环。 |
| [EntityHealthChangedAfterEventSignal](reference/EntityHealthChangedAfterEventSignal.md) | 管理实体生命值变化时的回调。 |
| [EntityHealthComponent](reference/EntityHealthComponent.md) | 实体的生命值属性。 |
| [EntityHitEntityAfterEvent](reference/EntityHitEntityAfterEvent.md) | 实体近战攻击另一实体的事件信息。 |
| [EntityHitEntityAfterEventSignal](reference/EntityHitEntityAfterEventSignal.md) | 管理实体近战攻击另一实体时的回调。 |
| [EntityHurtAfterEvent](reference/EntityHurtAfterEvent.md) | 游戏中实体受伤的事件数据。 |
| [EntityHurtAfterEventSignal](reference/EntityHurtAfterEventSignal.md) | 管理向实体添加效果时的回调。 |
| [EntityHurtBeforeEvent](reference/EntityHurtBeforeEvent.md) | 游戏中实体受伤的事件数据。 |
| [EntityHurtBeforeEventSignal](reference/EntityHurtBeforeEventSignal.md) | 管理实体受伤时的回调。 |
| [EntityInventoryComponent](reference/EntityInventoryComponent.md) | 实体的库存属性。 |
| [EntityJumpComponent](reference/EntityJumpComponent.md) | 实体的基础移动速度。 |
| [EntityLavaMovementComponent](reference/EntityLavaMovementComponent.md) | 实体在熔岩中的基础移动速度。 |
| [EntityLoadAfterEvent](reference/EntityLoadAfterEvent.md) | 实体加载到世界时的事件数据，可能由区块重新加载或实体切换维度触发。 |
| [EntityLoadAfterEventSignal](reference/EntityLoadAfterEventSignal.md) | 订阅实体加载时的事件处理器。 |
| [EntityMovementComponent](reference/EntityMovementComponent.md) | 实体的基础移动速度。 |
| [EntityRemoveAfterEvent](reference/EntityRemoveAfterEvent.md) | 实体即将从世界移除时的数据，例如离玩家过远而被卸载。 |
| [EntityRemoveAfterEventSignal](reference/EntityRemoveAfterEventSignal.md) | 实体即将从游戏移除时的事件订阅入口，例如卸载或死亡后移除。 |
| [EntitySpawnAfterEvent](reference/EntitySpawnAfterEvent.md) | 实体在世界中生成时的事件数据。 |
| [EntitySpawnAfterEventSignal](reference/EntitySpawnAfterEventSignal.md) | 订阅实体生成时的事件处理器。 |
| [EntityTypeFamilyComponent](reference/EntityTypeFamilyComponent.md) | 从引擎读取实体当前的类型族集合。 |
| [EntityUnderwaterMovementComponent](reference/EntityUnderwaterMovementComponent.md) | 实体在水下的基础移动速度。 |
| [ExplosionAfterEvent](reference/ExplosionAfterEvent.md) | 已经发生的爆炸事件信息。 |
| [ExplosionAfterEventSignal](reference/ExplosionAfterEventSignal.md) | 管理爆炸发生时的回调。 |
| [ExplosionBeforeEvent](reference/ExplosionBeforeEvent.md) | 已经发生的爆炸事件信息。 |
| [ExplosionBeforeEventSignal](reference/ExplosionBeforeEventSignal.md) | 管理爆炸影响各个方块时的回调。 |
| [ItemCompleteUseAfterEvent](reference/ItemCompleteUseAfterEvent.md) | 可蓄力物品完成蓄力的事件信息。 |
| [ItemCompleteUseAfterEventSignal](reference/ItemCompleteUseAfterEventSignal.md) | 管理可蓄力物品完成蓄力时的回调。 |
| [ItemComponent](reference/ItemComponent.md) | 方块组件的基类。 |
| [ItemDurabilityComponent](reference/ItemDurabilityComponent.md) | 具有此组件的物品可在使用过程中损耗耐久。此组件只适用于数据驱动物品。 |
| [ItemEnchantableComponent](reference/ItemEnchantableComponent.md) | 具有此组件的物品可以附魔。 |
| [ItemStack](apis/itemStack.md) | 一组同类物品的堆叠。 |
| [ItemStartUseOnAfterEvent](reference/ItemStartUseOnAfterEvent.md) | 玩家按下使用物品或放置方块按钮并成功交互时的信息；连续建造中仅针对首个交互方块触发。此事件不适用于锄头或斧头。 |
| [ItemStartUseOnAfterEventSignal](reference/ItemStartUseOnAfterEventSignal.md) | 管理物品使用事件的回调。 |
| [ItemType](reference/ItemType.md) | 物品的类型。 |
| [ItemUseAfterEvent](reference/ItemUseAfterEvent.md) | 玩家使用物品成功触发交互时的事件信息。具体触发对象和原生限制以当前实现为准。 |
| [ItemUseAfterEventSignal](reference/ItemUseAfterEventSignal.md) | 管理物品使用事件的回调。 |
| [ListBlockVolume](reference/ListBlockVolume.md) | 独立方块位置的集合，按确定的插入顺序保存。 |
| [LootTableManager](reference/LootTableManager.md) | 战利品表管理器，根据方块和实体的战利品表生成掉落物。 |
| [MolangVariableMap](reference/MolangVariableMap.md) | 用于进一步控制渲染和动画的附加变量集合。 |
| [Player](apis/player.md) | 世界中的玩家对象。 |
| [PlayerBreakBlockAfterEvent](reference/PlayerBreakBlockAfterEvent.md) | 玩家破坏方块后的事件信息。 |
| [PlayerBreakBlockAfterEventSignal](reference/PlayerBreakBlockAfterEventSignal.md) | 管理玩家破坏方块时的回调。 |
| [PlayerBreakBlockBeforeEvent](reference/PlayerBreakBlockBeforeEvent.md) | 玩家破坏方块前的事件信息。 |
| [PlayerBreakBlockBeforeEventSignal](reference/PlayerBreakBlockBeforeEventSignal.md) | 管理玩家破坏方块时的回调。 |
| [PlayerDimensionChangeAfterEvent](reference/PlayerDimensionChangeAfterEvent.md) | 可蓄力物品完成蓄力的事件信息。 |
| [PlayerDimensionChangeAfterEventSignal](reference/PlayerDimensionChangeAfterEventSignal.md) | 管理玩家成功切换维度后的回调。 |
| [PlayerInteractWithEntityAfterEvent](reference/PlayerInteractWithEntityAfterEvent.md) | 玩家成功与实体交互后的事件信息。 |
| [PlayerInteractWithEntityAfterEventSignal](reference/PlayerInteractWithEntityAfterEventSignal.md) | 管理玩家与实体交互后的回调。 |
| [PlayerInteractWithEntityBeforeEvent](reference/PlayerInteractWithEntityBeforeEvent.md) | 玩家与实体交互前的事件信息。 |
| [PlayerInteractWithEntityBeforeEventSignal](reference/PlayerInteractWithEntityBeforeEventSignal.md) | 管理玩家与实体交互后的回调。 |
| [PlayerInventoryItemChangeAfterEvent](reference/PlayerInventoryItemChangeAfterEvent.md) | 玩家库存物品变化后的事件信息。 |
| [PlayerInventoryItemChangeAfterEventSignal](reference/PlayerInventoryItemChangeAfterEventSignal.md) | 管理玩家库存物品变化后的回调。 |
| [PlayerJoinAfterEvent](reference/PlayerJoinAfterEvent.md) | 玩家加入世界的事件信息。玩家首次生成并就绪后，可通过 playerSpawn 获取更详细的信息。 |
| [PlayerJoinAfterEventSignal](reference/PlayerJoinAfterEventSignal.md) | 管理玩家加入世界时的回调。 |
| [PlayerLeaveAfterEvent](reference/PlayerLeaveAfterEvent.md) | 玩家离开世界的事件信息。 |
| [PlayerLeaveAfterEventSignal](reference/PlayerLeaveAfterEventSignal.md) | 管理玩家离开世界时的回调。 |
| [PlayerPlaceBlockAfterEvent](reference/PlayerPlaceBlockAfterEvent.md) | 玩家放置方块的事件信息。 |
| [PlayerPlaceBlockAfterEventSignal](reference/PlayerPlaceBlockAfterEventSignal.md) | 管理玩家放置方块时的回调。 |
| [PlayerSpawnAfterEvent](reference/PlayerSpawnAfterEvent.md) | 玩家加入世界的事件信息。玩家首次生成并就绪后，可通过 playerSpawn 获取更详细的信息。 |
| [PlayerSpawnAfterEventSignal](reference/PlayerSpawnAfterEventSignal.md) | 订阅玩家生成或死亡后重生并完全就绪时的事件。 |
| [PrimitiveShapesManager](reference/PrimitiveShapesManager.md) | 图形基元管理器，用于向世界添加或移除文字等基元。 |
| [ProjectileHitBlockAfterEvent](reference/ProjectileHitBlockAfterEvent.md) | 投射物命中方块的事件信息。 |
| [ProjectileHitBlockAfterEventSignal](reference/ProjectileHitBlockAfterEventSignal.md) | 管理投射物命中方块时的回调。 |
| [ProjectileHitEntityAfterEvent](reference/ProjectileHitEntityAfterEvent.md) | 投射物命中实体的事件信息。 |
| [ProjectileHitEntityAfterEventSignal](reference/ProjectileHitEntityAfterEventSignal.md) | 管理投射物命中实体时的回调。 |
| [ProtectedEntityRegistry](reference/ProtectedEntityRegistry.md) | 签名、字段、属性、方法与调用示例 |
| [RGB](reference/RGB.md) | 签名、字段、属性、方法与调用示例 |
| [RGBA](reference/RGBA.md) | 签名、字段、属性、方法与调用示例 |
| [Scoreboard](reference/Scoreboard.md) | 计分板及其计分项、参与者。 |
| [ScoreboardIdentity](reference/ScoreboardIdentity.md) | 计分板参与者的身份信息。 |
| [ScoreboardObjective](reference/ScoreboardObjective.md) | 计分项的信息。 |
| [ScoreboardScoreInfo](reference/ScoreboardScoreInfo.md) | 计分板参与者及其对应分数。 |
| [ScriptEventCommandMessageAfterEvent](reference/ScriptEventCommandMessageAfterEvent.md) | 从全局指令字符串解析的事件快照，来源信息使用对象引用。id 和 message 均从完整指令读取；消息保留原文，不解析 JSON，也不展开选择器。全局指令钩子不提供非玩家角色对话发起者的信息。 |
| [ScriptEventCommandMessageAfterEventSignal](reference/ScriptEventCommandMessageAfterEventSignal.md) | 通过 [GlobalCommandServerEvent](native-events.md#globalcommandserverevent) 观察完整的 scriptevent 指令字符串，解析标识和消息，不依赖自定义命令的参数数组。回调在原生指令执行前同步触发，不保证引擎执行成功；已取消的指令会被忽略。 |
| [StartupBeforeEvent](reference/StartupBeforeEvent.md) | 签名、字段、属性、方法与调用示例 |
| [StartupBeforeEventSignal](reference/StartupBeforeEventSignal.md) |      |
| [Structure](reference/Structure.md) | 已加载的结构模板，对应 .mcstructure 文件。可通过 /structure 命令或 [StructureManager](reference/StructureManager.md) 将其放置到世界。 |
| [StructureManager](reference/StructureManager.md) | 结构管理器，用于创建、获取、放置和删除结构。 |
| [System](reference/System.md) | 系统级事件和功能的入口。 |
| [SystemAfterEvents](reference/SystemAfterEvents.md) | 游戏脚本系统中的事件集合。 |
| [SystemBeforeEvents](reference/SystemBeforeEvents.md) | 实际操作发生前的事件集合，部分事件允许取消或修改待执行操作。可写字段和执行限制以各事件的原生契约为准；不能直接套用微软受限执行阶段的规则。 |
| [TickingAreaManager](reference/TickingAreaManager.md) | 管理某维度中由本管理器创建的临时常加载区域，可添加、移除或查询。容量限制独立于命令限制，不能查询或修改其他模组及命令创建的区域。游戏关闭时移除这些区域。当前原生能力仅保证加载，逻辑更新限制见具体方法。 |
| [World](apis/world.md) | 签名、字段、属性、方法与调用示例 |
| [WorldAchievementCompleteAfterEvent](reference/WorldAchievementCompleteAfterEvent.md) | [AchievementCompleteEvent](native-events.md#achievementcompleteevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldActorAcquiredItemAfterEvent](reference/WorldActorAcquiredItemAfterEvent.md) | [ActorAcquiredItemServerEvent](native-events.md#actoracquireditemserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldActorHurtAfterEvent](reference/WorldActorHurtAfterEvent.md) | [ActorHurtServerEvent](native-events.md#actorhurtserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldActorUseItemBeforeEvent](reference/WorldActorUseItemBeforeEvent.md) | [ActorUseItemServerEvent](native-events.md#actoruseitemserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldActuallyHurtBeforeEvent](reference/WorldActuallyHurtBeforeEvent.md) | [ActuallyHurtServerEvent](native-events.md#actuallyhurtserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldAfterEvents](events/afterEvents.md) | 世界范围内可订阅的事件集合。 |
| [WorldAttackAnimBeginAfterEvent](reference/WorldAttackAnimBeginAfterEvent.md) | [AttackAnimBeginServerEvent](native-events.md#attackanimbeginserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldAttackAnimEndAfterEvent](reference/WorldAttackAnimEndAfterEvent.md) | [AttackAnimEndServerEvent](native-events.md#attackanimendserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldBeforeEvents](events/beforeEvents.md) | 实际操作发生前的事件集合，多数情况下可取消或修改即将发生的操作。原生钩子同步执行，只有文档规定的输出可写，且须在回调内完成。开发包不实行微软的受限执行阶段；原生前置条件仍然适用。 |
| [WorldBlockDestroyByLiquidAfterEvent](reference/WorldBlockDestroyByLiquidAfterEvent.md) | [BlockDestroyByLiquidServerEvent](native-events.md#blockdestroybyliquidserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldBlockEntityTickAfterEvent](reference/WorldBlockEntityTickAfterEvent.md) | [ServerBlockEntityTickEvent](native-events.md#serverblockentitytickevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldBlockLiquidStateChangeAfterEvent](reference/WorldBlockLiquidStateChangeAfterEvent.md) | [BlockLiquidStateChangeAfterServerEvent](native-events.md#blockliquidstatechangeafterserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldBlockLiquidStateChangeBeforeEvent](reference/WorldBlockLiquidStateChangeBeforeEvent.md) | [BlockLiquidStateChangeServerEvent](native-events.md#blockliquidstatechangeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldBlockNeighborChangeAfterEvent](reference/WorldBlockNeighborChangeAfterEvent.md) | [BlockNeighborChangedServerEvent](native-events.md#blockneighborchangedserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldBlockPatternAfterEvent](reference/WorldBlockPatternAfterEvent.md) | [ServerPostBlockPatternEvent](native-events.md#serverpostblockpatternevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldBlockPatternBeforeEvent](reference/WorldBlockPatternBeforeEvent.md) | [ServerPreBlockPatternEvent](native-events.md#serverpreblockpatternevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldBlockRandomTickAfterEvent](reference/WorldBlockRandomTickAfterEvent.md) | [BlockRandomTickServerEvent](native-events.md#blockrandomtickserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldBlockRemoveAfterEvent](reference/WorldBlockRemoveAfterEvent.md) | [BlockRemoveServerEvent](native-events.md#blockremoveserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldBlockSnowStateChangeAfterEvent](reference/WorldBlockSnowStateChangeAfterEvent.md) | [BlockSnowStateChangeAfterServerEvent](native-events.md#blocksnowstatechangeafterserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldBlockSnowStateChangeBeforeEvent](reference/WorldBlockSnowStateChangeBeforeEvent.md) | [BlockSnowStateChangeServerEvent](native-events.md#blocksnowstatechangeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldBlockStrengthChangeAfterEvent](reference/WorldBlockStrengthChangeAfterEvent.md) | [BlockStrengthChangedServerEvent](native-events.md#blockstrengthchangedserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldBlockUseBeforeEvent](reference/WorldBlockUseBeforeEvent.md) | [ServerBlockUseEvent](native-events.md#serverblockuseevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldChangeLevelUpCostBeforeEvent](reference/WorldChangeLevelUpCostBeforeEvent.md) | [ChangeLevelUpCostServerEvent](native-events.md#changelevelupcostserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldChangeSwimStateAfterEvent](reference/WorldChangeSwimStateAfterEvent.md) | [ChangeSwimStateServerEvent](native-events.md#changeswimstateserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldChestBlockTryPairWithBeforeEvent](reference/WorldChestBlockTryPairWithBeforeEvent.md) | [ChestBlockTryPairWithServerEvent](native-events.md#chestblocktrypairwithserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldChunkGeneratedAfterEvent](reference/WorldChunkGeneratedAfterEvent.md) | [ChunkGeneratedServerEvent](native-events.md#chunkgeneratedserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldChunkLoadAfterEvent](reference/WorldChunkLoadAfterEvent.md) | [ChunkLoadedServerEvent](native-events.md#chunkloadedserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldChunkUnloadBeforeEvent](reference/WorldChunkUnloadBeforeEvent.md) | [ChunkAcquireDiscardedServerEvent](native-events.md#chunkacquirediscardedserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldClientReadyAfterEvent](reference/WorldClientReadyAfterEvent.md) | [ClientLoadAddonsFinishServerEvent](native-events.md#clientloadaddonsfinishserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldCommandBeforeEvent](reference/WorldCommandBeforeEvent.md) | [CommandEvent](native-events.md#commandevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldCommandBlockContainerOpenBeforeEvent](reference/WorldCommandBlockContainerOpenBeforeEvent.md) | [CommandBlockContainerOpenEvent](native-events.md#commandblockcontaineropenevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldCommandBlockUpdateBeforeEvent](reference/WorldCommandBlockUpdateBeforeEvent.md) | [CommandBlockUpdateEvent](native-events.md#commandblockupdateevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldCommandOutputAfterEvent](reference/WorldCommandOutputAfterEvent.md) | [OnCommandOutputServerEvent](native-events.md#oncommandoutputserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldContainerItemChangeAfterEvent](reference/WorldContainerItemChangeAfterEvent.md) | [ContainerItemChangedServerEvent](native-events.md#containeritemchangedserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldContainerLootBeforeEvent](reference/WorldContainerLootBeforeEvent.md) | [OnContainerFillLoottableServerEvent](native-events.md#oncontainerfillloottableserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldCraftItemOutputChangeBeforeEvent](reference/WorldCraftItemOutputChangeBeforeEvent.md) | [CraftItemOutputChangeServerEvent](native-events.md#craftitemoutputchangeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldCustomCommandTriggerBeforeEvent](reference/WorldCustomCommandTriggerBeforeEvent.md) | [CustomCommandTriggerServerEvent](native-events.md#customcommandtriggerserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldDamageBeforeEvent](reference/WorldDamageBeforeEvent.md) | [DamageEvent](native-events.md#damageevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldDestroyBlockAfterEvent](reference/WorldDestroyBlockAfterEvent.md) | [DestroyBlockEvent](native-events.md#destroyblockevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldDirtBlockToGrassBlockAfterEvent](reference/WorldDirtBlockToGrassBlockAfterEvent.md) | [DirtBlockToGrassBlockServerEvent](native-events.md#dirtblocktograssblockserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEffectAddBeforeEvent](reference/WorldEffectAddBeforeEvent.md) | [WillAddEffectServerEvent](native-events.md#willaddeffectserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEffectRefreshAfterEvent](reference/WorldEffectRefreshAfterEvent.md) | [RefreshEffectServerEvent](native-events.md#refresheffectserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEffectRemoveAfterEvent](reference/WorldEffectRemoveAfterEvent.md) | [RemoveEffectServerEvent](native-events.md#removeeffectserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityAddAfterEvent](reference/WorldEntityAddAfterEvent.md) | [AddEntityServerEvent](native-events.md#addentityserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityAreaChangeAfterEvent](reference/WorldEntityAreaChangeAfterEvent.md) | [NewOnEntityAreaEvent](native-events.md#newonentityareaevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityChangeDimensionAfterEvent](reference/WorldEntityChangeDimensionAfterEvent.md) | [EntityChangeDimensionServerEvent](native-events.md#entitychangedimensionserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityCollideAfterEvent](reference/WorldEntityCollideAfterEvent.md) | [OnMobHitMobServerEvent](native-events.md#onmobhitmobserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityDefinitionTriggerAfterEvent](reference/WorldEntityDefinitionTriggerAfterEvent.md) | [EntityDefinitionsEventServerEvent](native-events.md#entitydefinitionseventserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityDroppedItemAfterEvent](reference/WorldEntityDroppedItemAfterEvent.md) | [EntityDroppedItemServerEvent](native-events.md#entitydroppeditemserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityEffectDamageAfterEvent](reference/WorldEntityEffectDamageAfterEvent.md) | [EntityEffectDamageServerEvent](native-events.md#entityeffectdamageserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityHealthChangedBeforeEvent](reference/WorldEntityHealthChangedBeforeEvent.md) | [HealthChangeBeforeServerEvent](native-events.md#healthchangebeforeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityHitBlockAfterEvent](reference/WorldEntityHitBlockAfterEvent.md) | [OnMobHitBlockServerEvent](native-events.md#onmobhitblockserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityInsideBlockBeforeEvent](reference/WorldEntityInsideBlockBeforeEvent.md) | [OnEntityInsideBlockServerEvent](native-events.md#onentityinsideblockserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityKnockbackAfterEvent](reference/WorldEntityKnockbackAfterEvent.md) | [OnKnockBackServerEvent](native-events.md#onknockbackserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityLandAfterEvent](reference/WorldEntityLandAfterEvent.md) | [OnGroundServerEvent](native-events.md#ongroundserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityLoadScriptAfterEvent](reference/WorldEntityLoadScriptAfterEvent.md) | [EntityLoadScriptEvent](native-events.md#entityloadscriptevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityLootAfterEvent](reference/WorldEntityLootAfterEvent.md) | [EntityDieLoottableAfterServerEvent](native-events.md#entitydieloottableafterserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityLootBeforeEvent](reference/WorldEntityLootBeforeEvent.md) | [EntityDieLoottableServerEvent](native-events.md#entitydieloottableserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityMotionStartAfterEvent](reference/WorldEntityMotionStartAfterEvent.md) | [EntityMotionStartServerEvent](native-events.md#entitymotionstartserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityMotionStopBeforeEvent](reference/WorldEntityMotionStopBeforeEvent.md) | [EntityMotionStopServerEvent](native-events.md#entitymotionstopserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityPickupItemAfterEvent](reference/WorldEntityPickupItemAfterEvent.md) | [EntityPickupItemServerEvent](native-events.md#entitypickupitemserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityPlaceBlockAfterEvent](reference/WorldEntityPlaceBlockAfterEvent.md) | [EntityPlaceBlockAfterServerEvent](native-events.md#entityplaceblockafterserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityPlaceBlockBeforeEvent](reference/WorldEntityPlaceBlockBeforeEvent.md) | [ServerEntityTryPlaceBlockEvent](native-events.md#serverentitytryplaceblockevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityRemoveAfterEvent](reference/WorldEntityRemoveAfterEvent.md) | [EntityRemoveEvent](native-events.md#entityremoveevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntitySpawnBeforeEvent](reference/WorldEntitySpawnBeforeEvent.md) | [ServerSpawnMobEvent](native-events.md#serverspawnmobevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityStartRidingAfterEvent](reference/WorldEntityStartRidingAfterEvent.md) | [EntityStartRidingEvent](native-events.md#entitystartridingevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityStopRidingBeforeEvent](reference/WorldEntityStopRidingBeforeEvent.md) | [EntityStopRidingEvent](native-events.md#entitystopridingevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityTameAfterEvent](reference/WorldEntityTameAfterEvent.md) | [MountTamingEvent](native-events.md#mounttamingevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldEntityTickAfterEvent](reference/WorldEntityTickAfterEvent.md) | [EntityTickServerEvent](native-events.md#entitytickserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldExtinguishFireBeforeEvent](reference/WorldExtinguishFireBeforeEvent.md) | [ExtinguishFireServerEvent](native-events.md#extinguishfireserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldFallingBlockBreakBeforeEvent](reference/WorldFallingBlockBreakBeforeEvent.md) | [FallingBlockBreakServerEvent](native-events.md#fallingblockbreakserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldFallingBlockCauseDamageBeforeEvent](reference/WorldFallingBlockCauseDamageBeforeEvent.md) | [FallingBlockCauseDamageBeforeServerEvent](native-events.md#fallingblockcausedamagebeforeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldFallingBlockReturnHeavyBlockAfterEvent](reference/WorldFallingBlockReturnHeavyBlockAfterEvent.md) | [FallingBlockReturnHeavyBlockServerEvent](native-events.md#fallingblockreturnheavyblockserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldFallOnBlockBeforeEvent](reference/WorldFallOnBlockBeforeEvent.md) | [OnBeforeFallOnBlockServerEvent](native-events.md#onbeforefallonblockserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldFallOnBlockMotionBeforeEvent](reference/WorldFallOnBlockMotionBeforeEvent.md) | [OnAfterFallOnBlockServerEvent](native-events.md#onafterfallonblockserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldFarmBlockToDirtBlockAfterEvent](reference/WorldFarmBlockToDirtBlockAfterEvent.md) | [FarmBlockToDirtBlockServerEvent](native-events.md#farmblocktodirtblockserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldFireHurtBeforeEvent](reference/WorldFireHurtBeforeEvent.md) | [OnFireHurtEvent](native-events.md#onfirehurtevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldFurnaceBurnFinishAfterEvent](reference/WorldFurnaceBurnFinishAfterEvent.md) | [FurnaceBurnFinishedServerEvent](native-events.md#furnaceburnfinishedserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldGameTypeChangeAfterEvent](reference/WorldGameTypeChangeAfterEvent.md) | [GameTypeChangedServerEvent](native-events.md#gametypechangedserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldGlobalCommandBeforeEvent](reference/WorldGlobalCommandBeforeEvent.md) | [GlobalCommandServerEvent](native-events.md#globalcommandserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldGrassBlockToDirtBlockAfterEvent](reference/WorldGrassBlockToDirtBlockAfterEvent.md) | [GrassBlockToDirtBlockServerEvent](native-events.md#grassblocktodirtblockserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldHeavyBlockStartFallingAfterEvent](reference/WorldHeavyBlockStartFallingAfterEvent.md) | [HeavyBlockStartFallingServerEvent](native-events.md#heavyblockstartfallingserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldHopperTryPullInAfterEvent](reference/WorldHopperTryPullInAfterEvent.md) | [HopperTryPullInServerEvent](native-events.md#hoppertrypullinserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldHopperTryPullOutAfterEvent](reference/WorldHopperTryPullOutAfterEvent.md) | [HopperTryPullOutServerEvent](native-events.md#hoppertrypulloutserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldItemDurabilityChangeBeforeEvent](reference/WorldItemDurabilityChangeBeforeEvent.md) | [ItemDurabilityChangedServerEvent](native-events.md#itemdurabilitychangedserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldItemPullOutCustomContainerBeforeEvent](reference/WorldItemPullOutCustomContainerBeforeEvent.md) | [ItemPullOutCustomContainerServerEvent](native-events.md#itempulloutcustomcontainerserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldItemPushInCustomContainerBeforeEvent](reference/WorldItemPushInCustomContainerBeforeEvent.md) | [ItemPushInCustomContainerServerEvent](native-events.md#itempushincustomcontainerserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldItemPutInEnchantingModelBeforeEvent](reference/WorldItemPutInEnchantingModelBeforeEvent.md) | [OnItemPutInEnchantingModelServerEvent](native-events.md#onitemputinenchantingmodelserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldItemReleaseUsingBeforeEvent](reference/WorldItemReleaseUsingBeforeEvent.md) | [ItemReleaseUsingServerEvent](native-events.md#itemreleaseusingserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldItemUseAfterEvent](reference/WorldItemUseAfterEvent.md) | [ItemUseAfterServerEvent](native-events.md#itemuseafterserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldItemUseBeforeEvent](reference/WorldItemUseBeforeEvent.md) | [ServerItemTryUseEvent](native-events.md#serveritemtryuseevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldItemUseOnAfterEvent](reference/WorldItemUseOnAfterEvent.md) | [ItemUseOnAfterServerEvent](native-events.md#itemuseonafterserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldItemUseOnBeforeEvent](reference/WorldItemUseOnBeforeEvent.md) | [ServerItemUseOnEvent](native-events.md#serveritemuseonevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldJumpAnimBeginAfterEvent](reference/WorldJumpAnimBeginAfterEvent.md) | [JumpAnimBeginServerEvent](native-events.md#jumpanimbeginserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldLightningLevelChangeAfterEvent](reference/WorldLightningLevelChangeAfterEvent.md) | [OnLightningLevelChangeServerEvent](native-events.md#onlightninglevelchangeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldLiquidClippedAfterEvent](reference/WorldLiquidClippedAfterEvent.md) | [LiquidClippedServerEvent](native-events.md#liquidclippedserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldLobbyPurchaseAfterEvent](reference/WorldLobbyPurchaseAfterEvent.md) | [lobbyGoodBuySucServerEvent](native-events.md#lobbygoodbuysucserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldLocalLightningLevelChangeAfterEvent](reference/WorldLocalLightningLevelChangeAfterEvent.md) | [OnLocalLightningLevelChangeServerEvent](native-events.md#onlocallightninglevelchangeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldLocalRainLevelChangeAfterEvent](reference/WorldLocalRainLevelChangeAfterEvent.md) | [OnLocalRainLevelChangeServerEvent](native-events.md#onlocalrainlevelchangeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldMobDieAfterEvent](reference/WorldMobDieAfterEvent.md) | [MobDieEvent](native-events.md#mobdieevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldMobGriefingBlockBeforeEvent](reference/WorldMobGriefingBlockBeforeEvent.md) | [MobGriefingBlockServerEvent](native-events.md#mobgriefingblockserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldNativeChatSendBeforeEvent](reference/WorldNativeChatSendBeforeEvent.md) | [ServerChatEvent](native-events.md#serverchatevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldNativeEffectAddAfterEvent](reference/WorldNativeEffectAddAfterEvent.md) | [AddEffectServerEvent](native-events.md#addeffectserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldNativeEntityHealthChangeAfterEvent](reference/WorldNativeEntityHealthChangeAfterEvent.md) | [HealthChangeServerEvent](native-events.md#healthchangeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldNativeExplosionBeforeEvent](reference/WorldNativeExplosionBeforeEvent.md) | [ExplosionServerEvent](native-events.md#explosionserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldNativePlayerInventoryItemChangeAfterEvent](reference/WorldNativePlayerInventoryItemChangeAfterEvent.md) | [InventoryItemChangedServerEvent](native-events.md#inventoryitemchangedserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPhysicsTouchAfterEvent](reference/WorldPhysicsTouchAfterEvent.md) | [PhysxTouchServerEvent](native-events.md#physxtouchserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPhysicsTriggerAfterEvent](reference/WorldPhysicsTriggerAfterEvent.md) | [PhysxTriggerServerEvent](native-events.md#physxtriggerserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPistonActionBeforeEvent](reference/WorldPistonActionBeforeEvent.md) | [PistonActionServerEvent](native-events.md#pistonactionserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlaceBlockEntityAfterEvent](reference/WorldPlaceBlockEntityAfterEvent.md) | [ServerPlaceBlockEntityEvent](native-events.md#serverplaceblockentityevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlaceNeteaseLargeFeatureBeforeEvent](reference/WorldPlaceNeteaseLargeFeatureBeforeEvent.md) | [PlaceNeteaseLargeFeatureServerEvent](native-events.md#placeneteaselargefeatureserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlaceNeteaseStructureFeatureBeforeEvent](reference/WorldPlaceNeteaseStructureFeatureBeforeEvent.md) | [PlaceNeteaseStructureFeatureEvent](native-events.md#placeneteasestructurefeatureevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerActionAfterEvent](reference/WorldPlayerActionAfterEvent.md) | [OnPlayerActionServerEvent](native-events.md#onplayeractionserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerActiveShieldBeforeEvent](reference/WorldPlayerActiveShieldBeforeEvent.md) | [OnPlayerActiveShieldServerEvent](native-events.md#onplayeractiveshieldserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerAddAfterEvent](reference/WorldPlayerAddAfterEvent.md) | [AddServerPlayerEvent](native-events.md#addserverplayerevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerAddCustomContainerItemAfterEvent](reference/WorldPlayerAddCustomContainerItemAfterEvent.md) | [PlayerAddCustomContainerItemServerEvent](native-events.md#playeraddcustomcontaineritemserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerArmorChangeAfterEvent](reference/WorldPlayerArmorChangeAfterEvent.md) | [OnNewArmorExchangeServerEvent](native-events.md#onnewarmorexchangeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerAttackEntityBeforeEvent](reference/WorldPlayerAttackEntityBeforeEvent.md) | [PlayerAttackEntityEvent](native-events.md#playerattackentityevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerBlockedByShieldAfterEvent](reference/WorldPlayerBlockedByShieldAfterEvent.md) | [OnPlayerBlockedByShieldAfterServerEvent](native-events.md#onplayerblockedbyshieldafterserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerBlockedByShieldBeforeEvent](reference/WorldPlayerBlockedByShieldBeforeEvent.md) | [OnPlayerBlockedByShieldBeforeServerEvent](native-events.md#onplayerblockedbyshieldbeforeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerCheatSpinAttackAfterEvent](reference/WorldPlayerCheatSpinAttackAfterEvent.md) | [PlayerCheatSpinAttackServerEvent](native-events.md#playercheatspinattackserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerDieAfterEvent](reference/WorldPlayerDieAfterEvent.md) | [PlayerDieEvent](native-events.md#playerdieevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerDimensionChangeFinishAfterEvent](reference/WorldPlayerDimensionChangeFinishAfterEvent.md) | [DimensionChangeFinishServerEvent](native-events.md#dimensionchangefinishserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerDimensionChangeStartAfterEvent](reference/WorldPlayerDimensionChangeStartAfterEvent.md) | [DimensionChangeServerEvent](native-events.md#dimensionchangeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerDoInteractAfterEvent](reference/WorldPlayerDoInteractAfterEvent.md) | [PlayerDoInteractServerEvent](native-events.md#playerdointeractserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerDropItemAfterEvent](reference/WorldPlayerDropItemAfterEvent.md) | [PlayerDropItemServerEvent](native-events.md#playerdropitemserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerEatFoodBeforeEvent](reference/WorldPlayerEatFoodBeforeEvent.md) | [PlayerEatFoodServerEvent](native-events.md#playereatfoodserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerExperienceAddAfterEvent](reference/WorldPlayerExperienceAddAfterEvent.md) | [AddExpEvent](native-events.md#addexpevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerFeedEntityBeforeEvent](reference/WorldPlayerFeedEntityBeforeEvent.md) | [PlayerFeedEntityServerEvent](native-events.md#playerfeedentityserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerFishingAfterEvent](reference/WorldPlayerFishingAfterEvent.md) | [PlayerFishingAfterServerEvent](native-events.md#playerfishingafterserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerFishingBeforeEvent](reference/WorldPlayerFishingBeforeEvent.md) | [PlayerFishingServerEvent](native-events.md#playerfishingserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerGetExperienceOrbBeforeEvent](reference/WorldPlayerGetExperienceOrbBeforeEvent.md) | [ServerPlayerGetExperienceOrbEvent](native-events.md#serverplayergetexperienceorbevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerHitBlockAfterEvent](reference/WorldPlayerHitBlockAfterEvent.md) | [OnPlayerHitBlockServerEvent](native-events.md#onplayerhitblockserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerHotbarItemChangeAfterEvent](reference/WorldPlayerHotbarItemChangeAfterEvent.md) | [OnCarriedNewItemChangedServerEvent](native-events.md#oncarriednewitemchangedserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerHungerChangeBeforeEvent](reference/WorldPlayerHungerChangeBeforeEvent.md) | [PlayerHungerChangeServerEvent](native-events.md#playerhungerchangeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerHurtBeforeEvent](reference/WorldPlayerHurtBeforeEvent.md) | [PlayerHurtEvent](native-events.md#playerhurtevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerInteractBeforeEvent](reference/WorldPlayerInteractBeforeEvent.md) | [PlayerInteractServerEvent](native-events.md#playerinteractserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerInventoryOpenScriptAfterEvent](reference/WorldPlayerInventoryOpenScriptAfterEvent.md) | [PlayerInventoryOpenScriptServerEvent](native-events.md#playerinventoryopenscriptserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerJoinMessageBeforeEvent](reference/WorldPlayerJoinMessageBeforeEvent.md) | [PlayerJoinMessageEvent](native-events.md#playerjoinmessageevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerLeaveBeforeEvent](reference/WorldPlayerLeaveBeforeEvent.md) | [PlayerIntendLeaveServerEvent](native-events.md#playerintendleaveserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerLeftMessageBeforeEvent](reference/WorldPlayerLeftMessageBeforeEvent.md) | [PlayerLeftMessageServerEvent](native-events.md#playerleftmessageserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerLevelChangeAfterEvent](reference/WorldPlayerLevelChangeAfterEvent.md) | [AddLevelEvent](native-events.md#addlevelevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerNamedEntityBeforeEvent](reference/WorldPlayerNamedEntityBeforeEvent.md) | [PlayerNamedEntityServerEvent](native-events.md#playernamedentityserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerOffhandItemChangeAfterEvent](reference/WorldPlayerOffhandItemChangeAfterEvent.md) | [OnOffhandItemChangedServerEvent](native-events.md#onoffhanditemchangedserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerPermissionChangeBeforeEvent](reference/WorldPlayerPermissionChangeBeforeEvent.md) | [PlayerPermissionChangeServerEvent](native-events.md#playerpermissionchangeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerPickupArrowBeforeEvent](reference/WorldPlayerPickupArrowBeforeEvent.md) | [PlayerPickupArrowServerEvent](native-events.md#playerpickuparrowserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerPickupItemBeforeEvent](reference/WorldPlayerPickupItemBeforeEvent.md) | [ServerPlayerTryTouchEvent](native-events.md#serverplayertrytouchevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerRemoveAfterEvent](reference/WorldPlayerRemoveAfterEvent.md) | [DelServerPlayerEvent](native-events.md#delserverplayerevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerRemoveCustomContainerItemAfterEvent](reference/WorldPlayerRemoveCustomContainerItemAfterEvent.md) | [PlayerRemoveCustomContainerItemServerEvent](native-events.md#playerremovecustomcontaineritemserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerRespawnAfterEvent](reference/WorldPlayerRespawnAfterEvent.md) | [PlayerRespawnEvent](native-events.md#playerrespawnevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerRespawnFinishAfterEvent](reference/WorldPlayerRespawnFinishAfterEvent.md) | [PlayerRespawnFinishServerEvent](native-events.md#playerrespawnfinishserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerSleepAfterEvent](reference/WorldPlayerSleepAfterEvent.md) | [PlayerSleepServerEvent](native-events.md#playersleepserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerSpinAttackAfterEvent](reference/WorldPlayerSpinAttackAfterEvent.md) | [PlayerSpinAttackServerEvent](native-events.md#playerspinattackserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerStartFishingBeforeEvent](reference/WorldPlayerStartFishingBeforeEvent.md) | [PlayerStartFishingServerEvent](native-events.md#playerstartfishingserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerStopSleepAfterEvent](reference/WorldPlayerStopSleepAfterEvent.md) | [PlayerStopSleepServerEvent](native-events.md#playerstopsleepserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerTeleportAfterEvent](reference/WorldPlayerTeleportAfterEvent.md) | [PlayerTeleportEvent](native-events.md#playerteleportevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerTryAddCustomContainerItemBeforeEvent](reference/WorldPlayerTryAddCustomContainerItemBeforeEvent.md) | [PlayerTryAddCustomContainerItemServerEvent](native-events.md#playertryaddcustomcontaineritemserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerTryBreakBlockBeforeEvent](reference/WorldPlayerTryBreakBlockBeforeEvent.md) | [ServerPlayerTryDestroyBlockEvent](native-events.md#serverplayertrydestroyblockevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerTryPutCustomContainerItemBeforeEvent](reference/WorldPlayerTryPutCustomContainerItemBeforeEvent.md) | [PlayerTryPutCustomContainerItemServerEvent](native-events.md#playertryputcustomcontaineritemserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerTryRemoveCustomContainerItemBeforeEvent](reference/WorldPlayerTryRemoveCustomContainerItemBeforeEvent.md) | [PlayerTryRemoveCustomContainerItemServerEvent](native-events.md#playertryremovecustomcontaineritemserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldPlayerTrySleepBeforeEvent](reference/WorldPlayerTrySleepBeforeEvent.md) | [PlayerTrySleepServerEvent](native-events.md#playertrysleepserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldProjectileCritHitAfterEvent](reference/WorldProjectileCritHitAfterEvent.md) | [ProjectileCritHitEvent](native-events.md#projectilecrithitevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldProjectileDoHitEffectBeforeEvent](reference/WorldProjectileDoHitEffectBeforeEvent.md) | [ProjectileDoHitEffectEvent](native-events.md#projectiledohiteffectevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldRainLevelChangeAfterEvent](reference/WorldRainLevelChangeAfterEvent.md) | [OnRainLevelChangeServerEvent](native-events.md#onrainlevelchangeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldScriptsLoadAfterEvent](reference/WorldScriptsLoadAfterEvent.md) | [LoadServerAddonScriptsAfter](native-events.md#loadserveraddonscriptsafter) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldShearsDestroyBlockBeforeEvent](reference/WorldShearsDestroyBlockBeforeEvent.md) | [ShearsDestoryBlockBeforeServerEvent](native-events.md#shearsdestoryblockbeforeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldShearsUseToBlockBeforeEvent](reference/WorldShearsUseToBlockBeforeEvent.md) | [ShearsUseToBlockBeforeServerEvent](native-events.md#shearsusetoblockbeforeserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldSpawnProjectileAfterEvent](reference/WorldSpawnProjectileAfterEvent.md) | [SpawnProjectileServerEvent](native-events.md#spawnprojectileserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldStandOnBlockBeforeEvent](reference/WorldStandOnBlockBeforeEvent.md) | [OnStandOnBlockServerEvent](native-events.md#onstandonblockserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldStartDestroyBlockBeforeEvent](reference/WorldStartDestroyBlockBeforeEvent.md) | [StartDestroyBlockServerEvent](native-events.md#startdestroyblockserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldStartRidingBeforeEvent](reference/WorldStartRidingBeforeEvent.md) | [StartRidingServerEvent](native-events.md#startridingserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldStepOffBlockAfterEvent](reference/WorldStepOffBlockAfterEvent.md) | [StepOffBlockServerEvent](native-events.md#stepoffblockserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldStepOnBlockBeforeEvent](reference/WorldStepOnBlockBeforeEvent.md) | [StepOnBlockServerEvent](native-events.md#steponblockserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldStoreBuySuccAfterEvent](reference/WorldStoreBuySuccAfterEvent.md) | [StoreBuySuccServerEvent](native-events.md#storebuysuccserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldTickAfterEvent](reference/WorldTickAfterEvent.md) | [OnScriptTickServer](native-events.md#onscripttickserver) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldUiContainerItemChangeAfterEvent](reference/WorldUiContainerItemChangeAfterEvent.md) | [UIContainerItemChangedServerEvent](native-events.md#uicontaineritemchangedserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldUrgeShipAfterEvent](reference/WorldUrgeShipAfterEvent.md) | [UrgeShipEvent](native-events.md#urgeshipevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldWalkAnimBeginAfterEvent](reference/WorldWalkAnimBeginAfterEvent.md) | [WalkAnimBeginServerEvent](native-events.md#walkanimbeginserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldWalkAnimEndAfterEvent](reference/WorldWalkAnimEndAfterEvent.md) | [WalkAnimEndServerEvent](native-events.md#walkanimendserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |
| [WorldWillTeleportToBeforeEvent](reference/WorldWillTeleportToBeforeEvent.md) | [WillTeleportToServerEvent](native-events.md#willteleporttoserverevent) 的事件参数；同步分发结束后不能再写入输出字段。 |

</div>


## 原生事件

[服务端原生事件目录](native-events.md) · [事件用法与示例](../guides/native-events.md)


## 推荐事件入口

[服务端语义事件](semantic-events.md) · [语义化设计与示例](../guides/semantic-events.md)