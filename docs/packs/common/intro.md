---
sidebar_position: 1
title: 公共类型与错误
---

# 公共类型与错误

[场景与完整示例](../examples.md) · [支持情况与差异](../compatibility.md)

<div className="modsapi-table-scroll" tabIndex={0} aria-label="接口表格，可横向滚动">

| 类型 | 说明 |
| --- | --- |
| [AimAssistTargetMode](reference/AimAssistTargetMode.md) | 签名、字段、属性、方法与调用示例 |
| [BlockBoundingBox](reference/BlockBoundingBox.md) | 签名、字段、属性、方法与调用示例 |
| [BlockComponentTypes](reference/BlockComponentTypes.md) | 签名、字段、属性、方法与调用示例 |
| [BlockEventOptions](reference/BlockEventOptions.md) | 方块事件订阅的可选参数。 |
| [BlockFilter](reference/BlockFilter.md) | 根据类型、标签或状态组合包含或排除方块。未设置包含条件时，选择所有未被排除的方块；设置了包含条件时，方块还必须至少匹配一项包含条件。 |
| [BlockHitInformation](reference/BlockHitInformation.md) | 方块被命中时的附加信息。 |
| [BlockInteractionEvent](reference/BlockInteractionEvent.md) | [BlockInteractionEvent](reference/BlockInteractionEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [BlockPistonState](reference/BlockPistonState.md) | 签名、字段、属性、方法与调用示例 |
| [BlockRaycastHit](reference/BlockRaycastHit.md) | 方块射线命中的结果信息。 |
| [BlockRaycastOptions](reference/BlockRaycastOptions.md) | 沿实体视线方向查找首个相交方块的射线选项。 |
| [BlockVolumeIntersection](reference/BlockVolumeIntersection.md) | 签名、字段、属性、方法与调用示例 |
| [BookErrorReason](reference/BookErrorReason.md) | 签名、字段、属性、方法与调用示例 |
| [ButtonState](reference/ButtonState.md) | 签名、字段、属性、方法与调用示例 |
| [CameraFadeOptions](reference/CameraFadeOptions.md) | 全屏颜色渐变的配置选项。 |
| [CameraFixedBoomOptions](reference/CameraFixedBoomOptions.md) | 签名、字段、属性、方法与调用示例 |
| [CameraShakeType](reference/CameraShakeType.md) | 签名、字段、属性、方法与调用示例 |
| [CloneMode](reference/CloneMode.md) | 签名、字段、属性、方法与调用示例 |
| [CommandPermissionLevel](reference/CommandPermissionLevel.md) | 签名、字段、属性、方法与调用示例 |
| [ContainerRulesErrorReason](reference/ContainerRulesErrorReason.md) | 签名、字段、属性、方法与调用示例 |
| [ControlScheme](reference/ControlScheme.md) | 签名、字段、属性、方法与调用示例 |
| [CustomCommand](reference/CustomCommand.md) | 定义自定义命令的名称、权限及参数。 |
| [CustomCommandErrorReason](reference/CustomCommandErrorReason.md) | 签名、字段、属性、方法与调用示例 |
| [CustomCommandOrigin](reference/CustomCommandOrigin.md) | 命令触发来源的详细信息。 |
| [CustomCommandParamType](reference/CustomCommandParamType.md) | 签名、字段、属性、方法与调用示例 |
| [CustomCommandResult](reference/CustomCommandResult.md) | 自定义命令执行结果，可用于调整命令行为。 |
| [CustomCommandSource](reference/CustomCommandSource.md) | 执行命令的来源。 |
| [CustomCommandStatus](reference/CustomCommandStatus.md) | 自定义命令执行结果的状态码。 |
| [CustomComponentNameErrorReason](reference/CustomComponentNameErrorReason.md) | 签名、字段、属性、方法与调用示例 |
| [Difficulty](reference/Difficulty.md) | 签名、字段、属性、方法与调用示例 |
| [DimensionLocation](reference/DimensionLocation.md) | 世界中的精确坐标，包含维度和位置。 |
| [Direction](reference/Direction.md) | 通用的相对方向枚举。 |
| [DisplaySlotId](reference/DisplaySlotId.md) | 签名、字段、属性、方法与调用示例 |
| [DyeColor](reference/DyeColor.md) | 签名、字段、属性、方法与调用示例 |
| [DynamicParticleOptions](reference/DynamicParticleOptions.md) | 签名、字段、属性、方法与调用示例 |
| [DynamicParticlePattern](reference/DynamicParticlePattern.md) | 签名、字段、属性、方法与调用示例 |
| [EaseOptions](reference/EaseOptions.md) | 签名、字段、属性、方法与调用示例 |
| [EasingType](reference/EasingType.md) | 签名、字段、属性、方法与调用示例 |
| [EffectChangeEvent](reference/EffectChangeEvent.md) | [EffectChangeEvent](reference/EffectChangeEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [Enchantment](reference/Enchantment.md) | 应用于物品的附魔及其等级。 |
| [EnchantmentSlot](reference/EnchantmentSlot.md) | 签名、字段、属性、方法与调用示例 |
| [EntityApplyDamageByProjectileOptions](reference/EntityApplyDamageByProjectileOptions.md) | 通过投射物造成伤害时的附加选项。 |
| [EntityApplyDamageOptions](reference/EntityApplyDamageOptions.md) | 伤害操作的附加说明与元数据。 |
| [EntityAreaEvent](reference/EntityAreaEvent.md) | [EntityAreaEvent](reference/EntityAreaEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [EntityAttachPoint](reference/EntityAttachPoint.md) | 签名、字段、属性、方法与调用示例 |
| [EntityComponentTypes](reference/EntityComponentTypes.md) | 可通过 [Entity.getComponent](../server/apis/entity.md#getComponent) 访问的实体组件类型。 |
| [EntityDamageCause](reference/EntityDamageCause.md) | 描述实体受到伤害的原因。 |
| [EntityDamageSource](reference/EntityDamageSource.md) | 实体受到伤害的来源信息。 |
| [EntityEffectOptions](reference/EntityEffectOptions.md) | 实体状态效果的附加选项。 |
| [EntityEventOptions](reference/EntityEventOptions.md) | 实体事件订阅的可选参数。 |
| [EntityFilter](reference/EntityFilter.md) | 实体筛选选项。 |
| [EntityHealCause](reference/EntityHealCause.md) | 签名、字段、属性、方法与调用示例 |
| [EntityHitInformation](reference/EntityHitInformation.md) | 被命中实体的附加信息。 |
| [EntityInitializationCause](reference/EntityInitializationCause.md) | 签名、字段、属性、方法与调用示例 |
| [EntityPresenceEvent](reference/EntityPresenceEvent.md) | [EntityPresenceEvent](reference/EntityPresenceEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [EntityQueryOptions](reference/EntityQueryOptions.md) | 选取指定区域内实体的查询选项。 |
| [EntityQueryPropertyOptions](reference/EntityQueryPropertyOptions.md) | 签名、字段、属性、方法与调用示例 |
| [EntityQueryPropertyValue](reference/EntityQueryPropertyValue.md) | 签名、字段、属性、方法与调用示例 |
| [EntityQueryScoreOptions](reference/EntityQueryScoreOptions.md) | 根据玩家在某计分项中的分数进行筛选的附加选项。 |
| [EntityRaycastHit](reference/EntityRaycastHit.md) | 实体射线命中的结果信息。 |
| [EntityRaycastOptions](reference/EntityRaycastOptions.md) | 沿实体视线方向查找首个相交方块的射线选项。 |
| [EntitySwingSource](reference/EntitySwingSource.md) | 签名、字段、属性、方法与调用示例 |
| [EqualsComparison](reference/EqualsComparison.md) | 实体筛选中的等于比较。 |
| [EquipmentSlot](reference/EquipmentSlot.md) | 生物的装备槽位，包括护甲、副手和主手。 |
| [EventBlock](reference/EventBlock.md) | 两端均可读取的只读方块快照，无需原生查询。实际方块可能已变化；若需读取服务端实时状态，请显式使用事件中已知的维度和 blockLocation 查询。 |
| [EventItemStack](reference/EventItemStack.md) | 两端均可使用的只读物品快照，无需引擎查询即可读取 SAPI 风格的 typeId、amount 和完整原生元数据。可从事件中读取，也可创建用于编辑战利品。此类型不同于服务端可修改的 [ItemStack](../server/apis/itemStack.md)。getItemDict 保留 userData；缺失的原生数据无法凭空恢复。 |
| [EventSignal](reference/EventSignal.md) | 在共享原生订阅之上提供筛选的同步语义事件信号。subscribe(callback, options=[None](type-system.md#none)) 返回回调；注册前校验选项并复制筛选条件。重复订阅同一回调会更新筛选条件，空序列不匹配任何对象。一个原生数据包可拆分为多次通知，例如按兴趣区域中的实体或物理接触对分别通知。 |
| [EventSubscriptionOptions](reference/EventSubscriptionOptions.md) | 筛选条件的副本。每个信号仅接受其目录中列出的选项键。 |
| [ExplosionOptions](reference/ExplosionOptions.md) | [Dimension.createExplosion](../server/apis/dimension.md#createExplosion) 的附加配置选项。 |
| [Expression](reference/Expression.md) | 表达式 |
| [ExtensionError](reference/ExtensionError.md) | 扩展功能运行时异常的基类；参数错误仍使用内置异常类型。 |
| [FluidType](reference/FluidType.md) | 签名、字段、属性、方法与调用示例 |
| [GameMode](reference/GameMode.md) | 世界中的游戏模式。 |
| [GameRule](reference/GameRule.md) | 签名、字段、属性、方法与调用示例 |
| [GameRules](reference/GameRules.md) | 游戏规则，也可通过 /gamerule 命令控制。 |
| [GraphicsMode](reference/GraphicsMode.md) | 签名、字段、属性、方法与调用示例 |
| [GreaterThanComparison](reference/GreaterThanComparison.md) | 实体筛选中的大于比较。 |
| [GreaterThanOrEqualsComparison](reference/GreaterThanOrEqualsComparison.md) | 实体筛选中的大于或等于比较。 |
| [HeldItemOption](reference/HeldItemOption.md) | 签名、字段、属性、方法与调用示例 |
| [HudElement](reference/HudElement.md) | 签名、字段、属性、方法与调用示例 |
| [HudVisibility](reference/HudVisibility.md) | 签名、字段、属性、方法与调用示例 |
| [InputAxisEvent](reference/InputAxisEvent.md) | [InputAxisEvent](reference/InputAxisEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [InputButton](reference/InputButton.md) | 签名、字段、属性、方法与调用示例 |
| [InputButtonEvent](reference/InputButtonEvent.md) | [InputButtonEvent](reference/InputButtonEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [InputDevice](reference/InputDevice.md) | 物理输入设备来源；这些值不对应微软的 [InputMode](reference/InputMode.md) 枚举。 |
| [InputMode](reference/InputMode.md) | 签名、字段、属性、方法与调用示例 |
| [InputPermissionCategory](reference/InputPermissionCategory.md) | 签名、字段、属性、方法与调用示例 |
| [InvalidClientObjectError](reference/InvalidClientObjectError.md) | 客户端、实体或效果对象已超出可用生命周期。 |
| [InvalidStructureError](reference/InvalidStructureError.md) | 结构无效时抛出。结构被删除后会失效。 |
| [InventoryChangeEvent](reference/InventoryChangeEvent.md) | [InventoryChangeEvent](reference/InventoryChangeEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [ItemComponentTypes](reference/ItemComponentTypes.md) | 签名、字段、属性、方法与调用示例 |
| [ItemLockMode](reference/ItemLockMode.md) | 描述物品在容器中的移动限制。 |
| [ItemUseAttemptEvent](reference/ItemUseAttemptEvent.md) | [ItemUseAttemptEvent](reference/ItemUseAttemptEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [KeyValueStorage](reference/KeyValueStorage.md) | 通过 [client.getStorage](../client/apis/manager.md#getStorage) 或 [world.getStorage](../server/apis/world.md#getStorage) 获取的网易扩展。每个命名空间保存一个文档，最多为 1 MiB 的 UTF-8 JSON，嵌套深度最多 32 层。读写均使用副本。[None](type-system.md#none) 表示存储的空值；删除键须调用 delete()。操作同步执行，不提供跨线程、进程或命名空间的事务。 |
| [LessThanComparison](reference/LessThanComparison.md) | 实体筛选中的小于比较。 |
| [LessThanOrEqualsComparison](reference/LessThanOrEqualsComparison.md) | 实体筛选中的小于或等于比较。 |
| [LiquidSettings](reference/LiquidSettings.md) | 签名、字段、属性、方法与调用示例 |
| [LiquidType](reference/LiquidType.md) | 可放置在方块上或在世界中流动的液体类型。 |
| [LocatorBarErrorReason](reference/LocatorBarErrorReason.md) | 签名、字段、属性、方法与调用示例 |
| [LootGenerateBeforeEvent](reference/LootGenerateBeforeEvent.md) | [LootGenerateBeforeEvent](reference/LootGenerateBeforeEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [MemoryTier](reference/MemoryTier.md) | 签名、字段、属性、方法与调用示例 |
| [MoonPhase](reference/MoonPhase.md) | 签名、字段、属性、方法与调用示例 |
| [Motion](reference/Motion.md) | 运动器 |
| [MovementType](reference/MovementType.md) | 签名、字段、属性、方法与调用示例 |
| [MusicOptions](reference/MusicOptions.md) | 为玩家播放音乐的附加选项。 |
| [NamespaceNameErrorReason](reference/NamespaceNameErrorReason.md) | 签名、字段、属性、方法与调用示例 |
| [NativeEventData](reference/NativeEventData.md) | 引擎事件快照，只允许文档明确规定的同步输出。可选字段或随开发包版本变化的字段缺失时返回 [None](type-system.md#none)。读取容器值时返回副本，修改后须重新赋值才能提交输出。实体、玩家和维度字段返回对象引用；准确原生标识仅通过显式的 getNativeData 或 getNativeValue 读取。事件参数由适配器创建，请勿自行实例化。 |
| [NativeEventSignal](reference/NativeEventSignal.md) | 由客户端或世界持有、按需注册的同步原生信号。重复订阅具有幂等性，各回调异常相互隔离。输出修改对同一信号的后续回调可见。subscribe 返回回调；unsubscribe 支持同一绑定方法的新引用。不补发或模拟事件，包括仅触发一次的生命周期事件。 |
| [NativeOperationError](reference/NativeOperationError.md) | 原生操作失败。可读取 operation、code 和 cause 诊断原因。 |
| [NotEqualsComparison](reference/NotEqualsComparison.md) | 实体筛选中的不等于比较。 |
| [ObjectiveSortOrder](reference/ObjectiveSortOrder.md) | 签名、字段、属性、方法与调用示例 |
| [PaletteColor](reference/PaletteColor.md) | 签名、字段、属性、方法与调用示例 |
| [ParticleBindEntityOptions](reference/ParticleBindEntityOptions.md) | 签名、字段、属性、方法与调用示例 |
| [PhysicsContactEvent](reference/PhysicsContactEvent.md) | [PhysicsContactEvent](reference/PhysicsContactEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [PlatformType](reference/PlatformType.md) | 签名、字段、属性、方法与调用示例 |
| [PlayAnimationOptions](reference/PlayAnimationOptions.md) | 动画播放的附加选项。 |
| [PlayerInventoryType](reference/PlayerInventoryType.md) | 签名、字段、属性、方法与调用示例 |
| [PlayerPermissionLevel](reference/PlayerPermissionLevel.md) | 玩家权限等级。 |
| [PlayerSoundOptions](reference/PlayerSoundOptions.md) | 为玩家播放音乐的附加选项。 |
| [PlayerSplitScreenSlot](reference/PlayerSplitScreenSlot.md) | 签名、字段、属性、方法与调用示例 |
| [PlayerStateChangeEvent](reference/PlayerStateChangeEvent.md) | [PlayerStateChangeEvent](reference/PlayerStateChangeEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [PointerActionBeforeEvent](reference/PointerActionBeforeEvent.md) | [PointerActionBeforeEvent](reference/PointerActionBeforeEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [PointerReleaseEvent](reference/PointerReleaseEvent.md) | [PointerReleaseEvent](reference/PointerReleaseEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [Promise](reference/Promise.md) | 本库的异步结果对象，语义不完全等同于 JavaScript 的 [Promise](reference/Promise.md)。 |
| [RangeComparison](reference/RangeComparison.md) | 比较范围的下限。 |
| [ScoreboardIdentityType](reference/ScoreboardIdentityType.md) | 签名、字段、属性、方法与调用示例 |
| [ScreenClosingEvent](reference/ScreenClosingEvent.md) | [ScreenClosingEvent](reference/ScreenClosingEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [ScreenStackChangeEvent](reference/ScreenStackChangeEvent.md) | [ScreenStackChangeEvent](reference/ScreenStackChangeEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [ScriptBridge](reference/ScriptBridge.md) | 双向 SAPI 通信入口，读写数据使用副本，只有显式注册的处理器才能调用。通过 [system.scriptBridge](../server/reference/System.md#scriptBridge) 或 [client.scriptBridge](../client/apis/manager.md#scriptBridge) 获取。request 返回本库的 [Promise](reference/Promise.md)；两端 timeoutTicks 均按每单位 1/20 秒换算。不会执行任意源代码。 |
| [ScriptBridgeAfterEvents](reference/ScriptBridgeAfterEvents.md) | 按 SAPI 风格组织的桥接通知信号集合。 |
| [ScriptBridgeError](reference/ScriptBridgeError.md) | 桥接失败异常，包含稳定的 code 和可选的远端异常名称 remoteName。 |
| [ScriptBridgeMessage](reference/ScriptBridgeMessage.md) | 独立的桥接消息数据；包含命名空间标识、解码后的数据和可选的本地玩家对象。 |
| [ScriptBridgeMessageSignal](reference/ScriptBridgeMessageSignal.md) | 桥接通知信号；订阅时复制按完整标识筛选的条件。 |
| [ScriptEventMessageFilterOptions](reference/ScriptEventMessageFilterOptions.md) | 订阅脚本事件回调的附加选项。 |
| [ScriptEventSource](reference/ScriptEventSource.md) | 脚本事件的来源类型。 |
| [SignSide](reference/SignSide.md) | 签名、字段、属性、方法与调用示例 |
| [SpawnEntityOptions](reference/SpawnEntityOptions.md) | 生成实体的附加选项。 |
| [StickyType](reference/StickyType.md) | 签名、字段、属性、方法与调用示例 |
| [StorageDataError](reference/StorageDataError.md) | 存储数据格式损坏；适配器不会自动覆盖这些数据。 |
| [StructureAnimationMode](reference/StructureAnimationMode.md) | 签名、字段、属性、方法与调用示例 |
| [StructureCreateOptions](reference/StructureCreateOptions.md) | 签名、字段、属性、方法与调用示例 |
| [StructureMirrorAxis](reference/StructureMirrorAxis.md) | 签名、字段、属性、方法与调用示例 |
| [StructurePlaceOptions](reference/StructurePlaceOptions.md) | 签名、字段、属性、方法与调用示例 |
| [StructureRotation](reference/StructureRotation.md) | 签名、字段、属性、方法与调用示例 |
| [StructureSaveMode](reference/StructureSaveMode.md) | 签名、字段、属性、方法与调用示例 |
| [StructureUneditableError](reference/StructureUneditableError.md) | 结构无效时抛出。结构被删除后会失效。 |
| [TeleportOptions](reference/TeleportOptions.md) | 沿实体视线方向查找首个相交方块的射线选项。 |
| [TickingArea](reference/TickingArea.md) | 特定常加载区域的上下文信息。 |
| [TickingAreaErrorReason](reference/TickingAreaErrorReason.md) | 签名、字段、属性、方法与调用示例 |
| [TickingAreaOptions](reference/TickingAreaOptions.md) | 动画播放的附加选项。 |
| [TimeOfDay](reference/TimeOfDay.md) | 签名、字段、属性、方法与调用示例 |
| [TintMethod](reference/TintMethod.md) | 签名、字段、属性、方法与调用示例 |
| [UnloadedChunksError](reference/UnloadedChunksError.md) | 请求的方块区域包含尚未加载的区块。 |
| [UnsupportedFeatureError](reference/UnsupportedFeatureError.md) | 当前安装的开发包不提供所请求的原生能力。 |
| [Vector2](reference/Vector2.md) | 二维向量。 |
| [Vector3](../server/extra/vector.md) | 签名、字段、属性、方法与调用示例 |
| [VectorXZ](reference/VectorXZ.md) | 由 x、z 分量构成的平面向量。 |
| [WaypointTexture](reference/WaypointTexture.md) | 签名、字段、属性、方法与调用示例 |
| [WeatherLevelChangeEvent](reference/WeatherLevelChangeEvent.md) | [WeatherLevelChangeEvent](reference/WeatherLevelChangeEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。 |
| [WeatherType](reference/WeatherType.md) | 签名、字段、属性、方法与调用示例 |

</div>