---
sidebar_position: 4
title: 官方对照与当前支持情况
---

# 官方对照与当前支持情况

比较基准为微软稳定版 server 2.11.0 / server-ui 2.3.0。此页记录**结构对照**，不以名称存在、字典结构或枚举常量来宣称功能已经完整实现。客户端模块是网易扩展。

状态：未实现 = 当前没有对应运行时类型；结构契约 = 参数/数据形状；部分 = 存在缺失或显式拒绝；待行为核验 = 名称和成员存在，仍需核验原生语义。

## @minecraft/server 2.11.0

[微软模块文档](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server?view=minecraft-bedrock-stable)

### 已知限制

- [EntityAttributeComponent.effectiveMin](server/reference/EntityAttributeComponent.md#effectiveMin)：当前读取属性 NBT 的 Min；尚未证明额外最小值修饰因素与微软有效最小值完全等价。
- [EntityAttributeComponent.resetToMaxValue](server/reference/EntityAttributeComponent.md#resetToMaxValue)：使用原生重置；未显式设置过的无穷上限按网易规则恢复默认值，不能宣称所有无穷边界行为与微软运行时一致。
- `EntityEquippableComponent.getEquipment/setEquipment Body`：网易 ArmorSlotType.BODY 是胸甲槽，不是 SAPI 的 Body 槽；尚无经核验的 Body 映射，当前明确拒绝。
- [Player.playSound](server/apis/player.md#playSound)：仅向指定在线玩家播放一次并上报失败；loopCount 非零会明确拒绝，当前后端不能返回新版 SoundInstance 句柄。
- [Player.camera](server/apis/player.md#camera)：服务端仍为空返回；网易客户端摄像机与 SAPI 相机预设/栈/缓动/瞄准并非同一接口，需逐项适配。
- [Player.clientSystemInfo](server/apis/player.md#clientSystemInfo)：现有同步属性为空返回；网易客户端数据只能通过通信获得，尚未建立可靠缓存。
- [World.getLootTableManager](server/apis/world.md#getLootTableManager)：现有空返回；需先核实网易对战利品表读取、上下文和随机生成的支持。
- [DataDrivenEntityTriggerAfterEvent.getModifiers](server/reference/DataDrivenEntityTriggerAfterEvent.md#getModifiers)：现有空实现；未取得与微软组件组修改器同等的事件上下文。
- [PrimitiveShapesManager.addText](server/reference/PrimitiveShapesManager.md#addText)：现有空实现；需补充服务端到客户端的文字绘制生命周期和玩家范围管理。
- [PrimitiveShapesManager.removeText](server/reference/PrimitiveShapesManager.md#removeText)：依赖尚未实现的文字实例管理。
- [PrimitiveShapesManager.removeAll](server/reference/PrimitiveShapesManager.md#removeAll)：现有空实现，不能据此声称已清理绘制对象。
- `Block.getItemStack(withData=True)`：网易接口未提供无损方块实体到物品的序列化；目前只支持不带数据的类型转换。
- [BlockPermutation.getItemStack](server/reference/BlockPermutation.md#getItemStack)：现有原型物品转换只保留类型和数量，尚未核实方块状态到物品 aux 的完整映射；不能保证保留颜色等变种。
- `Dimension/block native parity`：新增过滤、稀疏体积及未加载区块分支已通过离线回归；高度越界、方块实体更新和实际区块加载竞态仍需网易实机核验。
- `GameRules/*missing`：GetGameRulesInfoServer 仅提供部分规则；仅实现了已核实的 18 项读写，不能用本地缓存伪装其他原生规则。
- `System.currentTick`：网易脚本更新为每秒 30 次，当前计时器适配为 20 ticks/s；尚未统一暂停/卡顿下的刻计数语义。
- `World.clearDynamicProperties`：现有动态属性与其他模组共享 ExtraData 命名空间；缺少完整的旧数据所有权索引，直接全删会影响其他模组。
- `Dimension.cloneBlocks`：需正确处理目标重叠、过滤、容器/方块实体、实体和未加载区域；现有调色板复制不足以证明等价。
- `native component registries`：微软运行时自定义方块/物品组件注册与网易 JSON 定义、事件系统不同，尚未建立完整生命周期映射。
- `native-only modern engine features`：AimAssist、LocatorBar/Waypoint、FogSettings、物品书/容器规则/动态方块属性等需对应网易能力，缺少实现不能直接认定可完整模拟。

### 全部官方类型对照

| 名称 | 类别 | 当前结构状态 | 缺失 / 空成员 |
| --- | --- | --- | --- |
| `AABB` | 接口 | 结构契约 | center, extent |
| `AimAssistCategory` | 类 | 未实现 | defaultBlockPriority, defaultEntityPriority, getBlockPriorities, getBlockTagPriorities, getEntityPriorities, getEntityTypeFamilyPriorities, identifier |
| `AimAssistCategorySettings` | 类 | 未实现 | defaultBlockPriority, defaultEntityPriority, getBlockPriorities, getBlockTagPriorities, getEntityPriorities, getEntityTypeFamilyPriorities, identifier, setBlockPriorities, setBlockTagPriorities, setEntityPriorities, setEntityTypeFamilyPriorities |
| `AimAssistPreset` | 类 | 未实现 | defaultItemSettings, getExcludedBlockTagTargets, getExcludedBlockTargets, getExcludedEntityTargets, getExcludedEntityTypeFamilyTargets, getItemSettings, getLiquidTargetingItems, handSettings, identifier |
| `AimAssistPresetSettings` | 类 | 未实现 | defaultItemSettings, getExcludedBlockTagTargets, getExcludedBlockTargets, getExcludedEntityTargets, getExcludedEntityTypeFamilyTargets, getItemSettings, getLiquidTargetingItems, handSettings, identifier, setExcludedBlockTagTargets, setExcludedBlockTargets, setExcludedEntityTargets, setExcludedEntityTypeFamilyTargets, setItemSettings, setLiquidTargetingItems |
| `AimAssistRegistry` | 类 | 未实现 | addCategory, addPreset, getCategories, getCategory, getPreset, getPresets |
| [AimAssistTargetMode](common/reference/AimAssistTargetMode.md) | 枚举 | 常量定义 | — |
| `AnimationOptions` | 接口 | 结构契约 | animation, totalTimeSeconds |
| `BiomeFilter` | 接口 | 结构契约 | excludeBiomes, excludeTags, includeBiomes, includeTags |
| `BiomeSearchOptions` | 接口 | 结构契约 | boundingSize |
| `BiomeType` | 类 | 未实现 | getTags, hasTags, id |
| `BiomeTypes` | 类 | 未实现 | get, getAll |
| [Block](server/apis/block.md) | 类 | 部分 | canBeDestroyedByLiquidSpread, canContainLiquid, getItemStack, getParts, getRedstonePower, getSkyLightLevel, isLiquidBlocking, liquidCanFlowFromDirection, liquidSpreadCausesSpawn, localizationKey |
| [BlockBoundingBox](common/reference/BlockBoundingBox.md) | 接口 | 结构契约 | — |
| [BlockComponent](server/reference/BlockComponent.md) | 类 | 待行为核验 | — |
| `BlockComponentBlockBreakEvent` | 类 | 未实现 | block, blockDestructionSource, brokenBlockPermutation, dimension, entitySource |
| `BlockComponentBlockStateChangeEvent` | 类 | 未实现 | block, dimension, previousPermutation |
| `BlockComponentEntityEvent` | 类 | 未实现 | block, blockPermutation, dimension, entitySource, name |
| `BlockComponentEntityFallOnEvent` | 类 | 未实现 | block, dimension, entity, fallDistance |
| `BlockComponentOnPlaceEvent` | 类 | 未实现 | block, dimension, previousBlock |
| `BlockComponentPlayerBreakEvent` | 类 | 未实现 | block, brokenBlockPermutation, dimension, player |
| `BlockComponentPlayerInteractEvent` | 类 | 未实现 | block, dimension, face, faceLocation, player |
| `BlockComponentPlayerPlaceBeforeEvent` | 类 | 未实现 | block, cancel, dimension, face, permutationToPlace, player |
| `BlockComponentRandomTickEvent` | 类 | 未实现 | block, dimension |
| `BlockComponentRedstoneUpdateEvent` | 类 | 未实现 | block, dimension, powerLevel, previousPowerLevel |
| `BlockComponentRegistry` | 类 | 未实现 | registerCustomComponent |
| `BlockComponentStepOffEvent` | 类 | 未实现 | block, dimension, entity |
| `BlockComponentStepOnEvent` | 类 | 未实现 | block, dimension, entity |
| `BlockComponentTickEvent` | 类 | 未实现 | block, dimension |
| [BlockComponentTypes](common/reference/BlockComponentTypes.md) | 枚举 | 常量定义 | — |
| `BlockContainerAccessEventOptions` | 接口 | 结构契约 | accessSourceFilter, blockFilter |
| `BlockContainerClosedAfterEvent` | 类 | 未实现 | block, closeSource, dimension |
| `BlockContainerClosedAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `BlockContainerOpenedAfterEvent` | 类 | 未实现 | block, dimension, openSource |
| `BlockContainerOpenedAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `BlockCustomComponent` | 接口 | 结构契约 | beforeOnPlayerPlace, onBlockStateChange, onBreak, onEntity, onEntityFallOn, onPlace, onPlayerBreak, onPlayerInteract, onRandomTick, onRedstoneUpdate, onStepOff, onStepOn, onTick |
| `BlockCustomComponentAlreadyRegisteredError` | 类 | 未实现 | — |
| `BlockCustomComponentInstance` | 类 | 未实现 | block, customComponentParameters, isValid, typeId |
| `BlockCustomComponentReloadNewComponentError` | 类 | 未实现 | — |
| `BlockCustomComponentReloadNewEventError` | 类 | 未实现 | — |
| `BlockCustomComponentReloadVersionError` | 类 | 未实现 | — |
| `BlockDynamicPropertiesComponent` | 类 | 未实现 | block, get, isValid, [set](common/type-system.md#set), totalByteCount, typeId |
| [BlockEvent](server/reference/BlockEvent.md) | 类 | 待行为核验 | — |
| [BlockEventOptions](common/reference/BlockEventOptions.md) | 接口 | 结构契约 | — |
| [BlockExplodeAfterEvent](server/reference/BlockExplodeAfterEvent.md) | 类 | 待行为核验 | — |
| [BlockExplodeAfterEventSignal](server/reference/BlockExplodeAfterEventSignal.md) | 类 | 待行为核验 | — |
| `BlockFillOptions` | 接口 | 结构契约 | blockFilter, ignoreChunkBoundErrors |
| [BlockFilter](common/reference/BlockFilter.md) | 接口 | 结构契约 | — |
| `BlockFluidContainerComponent` | 类 | 未实现 | addDye, block, fillLevel, fluidColor, getFluidType, isValid, setFluidType, setPotion, typeId |
| [BlockHitInformation](common/reference/BlockHitInformation.md) | 接口 | 结构契约 | — |
| `BlockInstrumentComponent` | 类 | 未实现 | block, getInstrumentName, isValid, playInstrumentSound, typeId |
| [BlockInventoryComponent](server/reference/BlockInventoryComponent.md) | 类 | 待行为核验 | — |
| `BlockLocationIterator` | 类 | 未实现 | next |
| `BlockMapColorComponent` | 类 | 未实现 | block, color, isValid, tintMethod, tintedColor, typeId |
| `BlockMovableComponent` | 类 | 未实现 | block, isValid, movementType, stickyType, typeId |
| [BlockPermutation](server/reference/BlockPermutation.md) | 类 | 部分 | canBeDestroyedByLiquidSpread, canContainLiquid, isLiquidBlocking, liquidSpreadCausesSpawn, localizationKey |
| `BlockPistonComponent` | 类 | 未实现 | block, getAttachedBlocks, getAttachedBlocksLocations, isMoving, isValid, state, typeId |
| [BlockPistonState](common/reference/BlockPistonState.md) | 枚举 | 常量定义 | — |
| `BlockPrecipitationInteractionsComponent` | 类 | 未实现 | accumulatesSnow, block, isSnowLoggable, isValid, obstructsRain, typeId |
| `BlockQueryOptions` | 接口 | 结构契约 | closest, excludePermutations, excludeTags, excludeTypes, farthest, includePermutations, includeTags, includeTypes, location |
| [BlockRaycastHit](common/reference/BlockRaycastHit.md) | 接口 | 结构契约 | — |
| [BlockRaycastOptions](common/reference/BlockRaycastOptions.md) | 接口 | 结构契约 | includeLiquidBlocks |
| `BlockRecordPlayerComponent` | 类 | 未实现 | block, ejectRecord, getRecord, isPlaying, isValid, pauseRecord, playRecord, setRecord, typeId |
| `BlockRedstoneProducerComponent` | 类 | 未实现 | block, getConnectedFaces, getStronglyPoweredFace, isValid, power, typeId |
| `BlockSignComponent` | 类 | 未实现 | block, getRawText, getText, getTextDyeColor, isValid, isWaxed, setText, setTextDyeColor, setWaxed, typeId |
| `BlockStateType` | 类 | 未实现 | id, validValues |
| `BlockStates` | 类 | 未实现 | get, getAll |
| [BlockType](server/reference/BlockType.md) | 类 | 部分 | localizationKey |
| `BlockTypes` | 类 | 未实现 | get, getAll |
| [BlockVolume](server/reference/BlockVolume.md) | 类 | 待行为核验 | — |
| [BlockVolumeBase](server/reference/BlockVolumeBase.md) | 类 | 待行为核验 | — |
| [BlockVolumeIntersection](common/reference/BlockVolumeIntersection.md) | 枚举 | 常量定义 | — |
| `BookError` | 类 | 未实现 | reason |
| [BookErrorReason](common/reference/BookErrorReason.md) | 枚举 | 常量定义 | — |
| `BookPageContentError` | 类 | 未实现 | pageIndex, reason |
| `ButtonPushAfterEvent` | 类 | 未实现 | block, dimension, source |
| `ButtonPushAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| [ButtonState](common/reference/ButtonState.md) | 枚举 | 常量定义 | — |
| [Camera](client/reference/Camera.md) | 类 | 未实现 | addShake, attachToEntity, clear, fade, isValid, playAnimation, setCamera, setDefaultCamera, setFov, stopShaking |
| `CameraAttachOptions` | 接口 | 结构契约 | entity, locator |
| [CameraFadeOptions](common/reference/CameraFadeOptions.md) | 接口 | 结构契约 | fadeColor, fadeTime |
| `CameraFadeTimeOptions` | 接口 | 结构契约 | fadeInTime, fadeOutTime, holdTime |
| [CameraFixedBoomOptions](common/reference/CameraFixedBoomOptions.md) | 接口 | 结构契约 | entityOffset, viewOffset |
| `CameraFovOptions` | 接口 | 结构契约 | easeOptions, fov |
| `CameraSetFacingOptions` | 接口 | 结构契约 | easeOptions, facingEntity, location |
| `CameraSetLocationOptions` | 接口 | 结构契约 | easeOptions, location |
| `CameraSetPosOptions` | 接口 | 结构契约 | easeOptions, facingLocation, location |
| `CameraSetRotOptions` | 接口 | 结构契约 | easeOptions, location, rotation |
| `CameraShakeOptions` | 接口 | 结构契约 | duration, intensity, [type](common/type-system.md#type) |
| [CameraShakeType](common/reference/CameraShakeType.md) | 枚举 | 常量定义 | — |
| `CameraTargetOptions` | 接口 | 结构契约 | offsetFromTargetCenter, targetEntity |
| `CatmullRomSpline` | 类 | 未实现 | controlPoints |
| [ClientSystemInfo](client/reference/ClientSystemInfo.md) | 类 | 未实现 | locale, maxRenderDistance, memoryTier, platformType |
| [CloneMode](common/reference/CloneMode.md) | 枚举 | 常量定义 | — |
| `CommandError` | 类 | 未实现 | — |
| [CommandPermissionLevel](common/reference/CommandPermissionLevel.md) | 枚举 | 常量定义 | — |
| [CommandResult](server/reference/CommandResult.md) | 类 | 待行为核验 | — |
| [Component](server/reference/Component.md) | 类 | 待行为核验 | — |
| [Container](server/apis/container.md) | 类 | 部分 | containerRules, weight |
| `ContainerAccessSource` | 接口 | 结构契约 | entity |
| `ContainerAccessSourceFilter` | 接口 | 结构契约 | entityFilter |
| `ContainerRules` | 接口 | 结构契约 | allowNestedStorageItems, allowedItems, bannedItems, weightLimit |
| `ContainerRulesError` | 类 | 未实现 | reason |
| [ContainerRulesErrorReason](common/reference/ContainerRulesErrorReason.md) | 枚举 | 常量定义 | — |
| [ContainerSlot](server/reference/ContainerSlot.md) | 类 | 部分 | getCanDestroy, getCanPlaceOn, getDynamicPropertyTotalByteCount, setCanDestroy, setCanPlaceOn |
| [ControlScheme](common/reference/ControlScheme.md) | 枚举 | 常量定义 | — |
| [CustomCommand](common/reference/CustomCommand.md) | 接口 | 结构契约 | cheatsRequired, description, mandatoryParameters, optionalParameters, permissionLevel |
| `CustomCommandError` | 类 | 未实现 | reason |
| [CustomCommandErrorReason](common/reference/CustomCommandErrorReason.md) | 枚举 | 常量定义 | — |
| [CustomCommandOrigin](common/reference/CustomCommandOrigin.md) | 类 | 待行为核验 | — |
| [CustomCommandParamType](common/reference/CustomCommandParamType.md) | 枚举 | 常量定义 | — |
| `CustomCommandParameter` | 接口 | 结构契约 | name, [type](common/type-system.md#type) |
| [CustomCommandRegistry](server/reference/CustomCommandRegistry.md) | 类 | 部分 | registerEnum |
| [CustomCommandResult](common/reference/CustomCommandResult.md) | 接口 | 结构契约 | — |
| [CustomCommandSource](common/reference/CustomCommandSource.md) | 枚举 | 常量定义 | — |
| [CustomCommandStatus](common/reference/CustomCommandStatus.md) | 枚举 | 常量定义 | — |
| `CustomComponentInvalidRegistryError` | 类 | 未实现 | — |
| `CustomComponentNameError` | 类 | 未实现 | reason |
| [CustomComponentNameErrorReason](common/reference/CustomComponentNameErrorReason.md) | 枚举 | 常量定义 | — |
| `CustomComponentParameters` | 类 | 未实现 | params |
| `CustomDimensionAlreadyRegisteredError` | 类 | 未实现 | — |
| `CustomDimensionInvalidRegistryError` | 类 | 未实现 | — |
| `CustomDimensionNameError` | 类 | 未实现 | — |
| `CustomDimensionReloadNewDimensionError` | 类 | 未实现 | — |
| `CustomTexture` | 接口 | 结构契约 | iconHeight, iconWidth, path |
| `DamagedByEntityCondition` | 类 | 未实现 | entityType |
| [DataDrivenEntityTriggerAfterEvent](server/reference/DataDrivenEntityTriggerAfterEvent.md) | 类 | 部分 | getModifiers |
| `DataDrivenEntityTriggerAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `DefinitionModifier` | 接口 | 结构契约 | addedComponentGroups, removedComponentGroups |
| [Difficulty](common/reference/Difficulty.md) | 枚举 | 常量定义 | — |
| [Dimension](server/apis/dimension.md) | 类 | 部分 | calculateClosestBiomeFromSeed, cloneBlocks, containsBiomes, getBiome, getBlockAbove, getBlockBelow, getBlockFromRay, getSkyLightLevel, getTopmostBlock, heightRange, localizationKey, placeFeature, placeFeatureRule, playSound, setWeather, spawnXp |
| [DimensionLocation](common/reference/DimensionLocation.md) | 接口 | 结构契约 | — |
| `DimensionRegistry` | 类 | 未实现 | registerCustomDimension |
| `DimensionType` | 类 | 未实现 | typeId |
| `DimensionTypes` | 类 | 未实现 | get, getAll |
| [Direction](common/reference/Direction.md) | 枚举 | 常量定义 | — |
| [DisplaySlotId](common/reference/DisplaySlotId.md) | 枚举 | 常量定义 | — |
| [DyeColor](common/reference/DyeColor.md) | 枚举 | 常量定义 | — |
| [EaseOptions](common/reference/EaseOptions.md) | 接口 | 结构契约 | easeTime, easeType |
| [EasingType](common/reference/EasingType.md) | 枚举 | 常量定义 | — |
| [Effect](server/reference/Effect.md) | 类 | 部分 | isValid |
| [EffectAddAfterEvent](server/reference/EffectAddAfterEvent.md) | 类 | 待行为核验 | — |
| [EffectAddAfterEventSignal](server/reference/EffectAddAfterEventSignal.md) | 类 | 待行为核验 | — |
| `EffectAddBeforeEvent` | 类 | 未实现 | cancel, duration, effectType, entity |
| `EffectAddBeforeEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| [EffectType](server/reference/EffectType.md) | 类 | 待行为核验 | — |
| `EffectTypes` | 类 | 未实现 | get, getAll |
| `EmptyLootItem` | 类 | 未实现 | quality, subTable, weight |
| `EnchantInfo` | 类 | 未实现 | enchantment, range |
| `EnchantRandomEquipmentFunction` | 类 | 未实现 | chance, conditions |
| `EnchantRandomlyFunction` | 类 | 未实现 | conditions, treasure |
| `EnchantWithLevelsFunction` | 类 | 未实现 | conditions, levels, treasure |
| [Enchantment](common/reference/Enchantment.md) | 接口 | 结构契约 | — |
| `EnchantmentLevelOutOfBoundsError` | 类 | 未实现 | — |
| [EnchantmentSlot](common/reference/EnchantmentSlot.md) | 枚举 | 常量定义 | — |
| `EnchantmentType` | 类 | 未实现 | id, maxLevel |
| `EnchantmentTypeNotCompatibleError` | 类 | 未实现 | — |
| `EnchantmentTypeUnknownIdError` | 类 | 未实现 | — |
| `EnchantmentTypes` | 类 | 未实现 | get, getAll |
| [Entity](server/apis/entity.md) | 类 | 部分 | addItem, getAABB, getAllBlocksStandingOn, getBlockStandingOn, localizationKey, lookAt, nameplateDepthTested, nameplateRenderDistance, teleport |
| [EntityAddRiderComponent](server/reference/EntityAddRiderComponent.md) | 类 | 待行为核验 | — |
| `EntityAgeableComponent` | 类 | 未实现 | duration, entity, getDropItems, getFeedItems, growUp, isValid, transformToItem, typeId |
| [EntityApplyDamageByProjectileOptions](common/reference/EntityApplyDamageByProjectileOptions.md) | 接口 | 结构契约 | — |
| [EntityApplyDamageOptions](common/reference/EntityApplyDamageOptions.md) | 接口 | 结构契约 | — |
| [EntityAttachPoint](common/reference/EntityAttachPoint.md) | 枚举 | 常量定义 | — |
| [EntityAttributeComponent](server/reference/EntityAttributeComponent.md) | 类 | 待行为核验 | — |
| `EntityBaseMovementComponent` | 类 | 未实现 | entity, isValid, maxTurn, typeId |
| `EntityBreathableComponent` | 类 | 未实现 | breathesAir, breathesLava, breathesSolids, breathesWater, entity, generatesBubbles, getBreatheBlocks, getNonBreatheBlocks, inhaleTime, isValid, suffocateTime, totalSupply, typeId |
| `EntityCanClimbComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityCanFlyComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityCanPowerJumpComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityColor2Component` | 类 | 未实现 | entity, isValid, typeId, value |
| `EntityColorComponent` | 类 | 未实现 | entity, isValid, typeId, value |
| [EntityComponent](server/reference/EntityComponent.md) | 类 | 待行为核验 | — |
| [EntityComponentTypes](common/reference/EntityComponentTypes.md) | 枚举 | 常量定义 | — |
| `EntityContainerAccessEventOptions` | 接口 | 结构契约 | accessSourceFilter, entityFilter |
| `EntityContainerClosedAfterEvent` | 类 | 未实现 | closeSource, entity |
| `EntityContainerClosedAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `EntityContainerOpenedAfterEvent` | 类 | 未实现 | entity, openSource |
| `EntityContainerOpenedAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| [EntityDamageCause](common/reference/EntityDamageCause.md) | 枚举 | 常量定义 | — |
| [EntityDamageSource](common/reference/EntityDamageSource.md) | 接口 | 结构契约 | — |
| `EntityDataDrivenTriggerEventOptions` | 接口 | 结构契约 | entities, entityTypes, eventTypes |
| `EntityDefinitionFeedItem` | 类 | 未实现 | growth, item, resultItem |
| [EntityDieAfterEvent](server/reference/EntityDieAfterEvent.md) | 类 | 待行为核验 | — |
| [EntityDieAfterEventSignal](server/reference/EntityDieAfterEventSignal.md) | 类 | 待行为核验 | — |
| [EntityEffectOptions](common/reference/EntityEffectOptions.md) | 接口 | 结构契约 | — |
| `EntityEnderInventoryComponent` | 类 | 未实现 | container, entity, isValid, typeId |
| [EntityEquippableComponent](server/reference/EntityEquippableComponent.md) | 类 | 部分 | getEquipmentSlot |
| [EntityEventOptions](common/reference/EntityEventOptions.md) | 接口 | 结构契约 | — |
| `EntityExhaustionComponent` | 类 | 未实现 | currentValue, defaultValue, effectiveMax, effectiveMin, entity, isValid, resetToDefaultValue, resetToMaxValue, resetToMinValue, setCurrentValue, typeId |
| [EntityFilter](common/reference/EntityFilter.md) | 接口 | 结构契约 | — |
| `EntityFireImmuneComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityFloatsInLiquidComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityFlyingSpeedComponent` | 类 | 未实现 | entity, isValid, typeId, value |
| `EntityFrictionModifierComponent` | 类 | 未实现 | entity, isValid, typeId, value |
| `EntityHasMarkVariantCondition` | 类 | 未实现 | value |
| `EntityHasVariantCondition` | 类 | 未实现 | value |
| `EntityHealAfterEvent` | 类 | 未实现 | healSource, healedEntity, healing |
| `EntityHealAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `EntityHealBeforeEvent` | 类 | 未实现 | cancel, healSource, healedEntity, healing |
| `EntityHealBeforeEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| [EntityHealCause](common/reference/EntityHealCause.md) | 枚举 | 常量定义 | — |
| `EntityHealEventOptions` | 接口 | 结构契约 | allowedHealCauses, entityFilter |
| `EntityHealSource` | 类 | 未实现 | cause |
| `EntityHealableComponent` | 类 | 未实现 | entity, forceUse, getFeedItems, isValid, typeId |
| [EntityHealthChangedAfterEvent](server/reference/EntityHealthChangedAfterEvent.md) | 类 | 待行为核验 | — |
| [EntityHealthChangedAfterEventSignal](server/reference/EntityHealthChangedAfterEventSignal.md) | 类 | 待行为核验 | — |
| [EntityHealthComponent](server/reference/EntityHealthComponent.md) | 类 | 待行为核验 | — |
| `EntityHitBlockAfterEvent` | 类 | 未实现 | blockFace, damagingEntity, hitBlock, hitBlockPermutation |
| `EntityHitBlockAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| [EntityHitEntityAfterEvent](server/reference/EntityHitEntityAfterEvent.md) | 类 | 待行为核验 | — |
| [EntityHitEntityAfterEventSignal](server/reference/EntityHitEntityAfterEventSignal.md) | 类 | 待行为核验 | — |
| [EntityHitInformation](common/reference/EntityHitInformation.md) | 接口 | 结构契约 | — |
| `EntityHungerComponent` | 类 | 未实现 | currentValue, defaultValue, effectiveMax, effectiveMin, entity, isValid, resetToDefaultValue, resetToMaxValue, resetToMinValue, setCurrentValue, typeId |
| [EntityHurtAfterEvent](server/reference/EntityHurtAfterEvent.md) | 类 | 待行为核验 | — |
| `EntityHurtAfterEventOptions` | 接口 | 结构契约 | allowedDamageCauses, entities, entityFilter, entityTypes |
| [EntityHurtAfterEventSignal](server/reference/EntityHurtAfterEventSignal.md) | 类 | 待行为核验 | — |
| [EntityHurtBeforeEvent](server/reference/EntityHurtBeforeEvent.md) | 类 | 待行为核验 | — |
| `EntityHurtBeforeEventOptions` | 接口 | 结构契约 | allowedDamageCauses, entityFilter |
| [EntityHurtBeforeEventSignal](server/reference/EntityHurtBeforeEventSignal.md) | 类 | 待行为核验 | — |
| [EntityInitializationCause](common/reference/EntityInitializationCause.md) | 枚举 | 常量定义 | — |
| [EntityInventoryComponent](server/reference/EntityInventoryComponent.md) | 类 | 部分 | additionalSlotsPerStrength, canBeSiphonedFrom, containerType, inventorySize, private, restrictToOwner |
| `EntityIsBabyComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityIsChargedComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityIsChestedComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityIsDyeableComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityIsHiddenWhenInvisibleComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityIsIgnitedComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityIsIllagerCaptainComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityIsSaddledComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityIsShakingComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityIsShearedComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityIsStackableComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityIsStunnedComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityIsTamedComponent` | 类 | 未实现 | entity, isValid, tamedToPlayer, tamedToPlayerId, typeId |
| `EntityItemComponent` | 类 | 未实现 | entity, isValid, itemStack, typeId |
| `EntityItemDropAfterEvent` | 类 | 未实现 | entity, items |
| `EntityItemDropAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `EntityItemDropEventOptions` | 接口 | 结构契约 | entityFilter, itemFilter |
| `EntityItemPickupAfterEvent` | 类 | 未实现 | entity, items |
| `EntityItemPickupAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `EntityItemPickupBeforeEvent` | 类 | 未实现 | cancel, entity, item |
| `EntityItemPickupBeforeEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `EntityItemPickupEventOptions` | 接口 | 结构契约 | entityFilter, itemFilter |
| `EntityKilledCondition` | 类 | 未实现 | entityType |
| [EntityLavaMovementComponent](server/reference/EntityLavaMovementComponent.md) | 类 | 待行为核验 | — |
| `EntityLeashableComponent` | 类 | 未实现 | canBeStolen, entity, hardDistance, isLeashed, isValid, leashHolder, leashHolderEntityId, leashTo, maxDistance, softDistance, typeId, unleash |
| [EntityLoadAfterEvent](server/reference/EntityLoadAfterEvent.md) | 类 | 待行为核验 | — |
| [EntityLoadAfterEventSignal](server/reference/EntityLoadAfterEventSignal.md) | 类 | 待行为核验 | — |
| `EntityMarkVariantComponent` | 类 | 未实现 | entity, isValid, typeId, value |
| `EntityMovementAmphibiousComponent` | 类 | 未实现 | entity, isValid, maxTurn, typeId |
| `EntityMovementBasicComponent` | 类 | 未实现 | entity, isValid, maxTurn, typeId |
| [EntityMovementComponent](server/reference/EntityMovementComponent.md) | 类 | 待行为核验 | — |
| `EntityMovementFlyComponent` | 类 | 未实现 | entity, isValid, maxTurn, typeId |
| `EntityMovementGenericComponent` | 类 | 未实现 | entity, isValid, maxTurn, typeId |
| `EntityMovementGlideComponent` | 类 | 未实现 | entity, isValid, maxTurn, speedWhenTurning, startSpeed, typeId |
| `EntityMovementHoverComponent` | 类 | 未实现 | entity, isValid, maxTurn, typeId |
| `EntityMovementJumpComponent` | 类 | 未实现 | entity, isValid, maxTurn, typeId |
| `EntityMovementSkipComponent` | 类 | 未实现 | entity, isValid, maxTurn, typeId |
| `EntityMovementSwayComponent` | 类 | 未实现 | entity, isValid, maxTurn, swayAmplitude, swayFrequency, typeId |
| `EntityNavigationClimbComponent` | 类 | 未实现 | avoidDamageBlocks, avoidPortals, avoidSun, avoidWater, canBreach, canBreakDoors, canFloat, canJump, canOpenDoors, canOpenIronDoors, canPassDoors, canPathFromAir, canPathOverLava, canPathOverWater, canSink, canSwim, canWalk, canWalkInLava, entity, isAmphibious, isValid, typeId |
| `EntityNavigationComponent` | 类 | 未实现 | avoidDamageBlocks, avoidPortals, avoidSun, avoidWater, canBreach, canBreakDoors, canFloat, canJump, canOpenDoors, canOpenIronDoors, canPassDoors, canPathFromAir, canPathOverLava, canPathOverWater, canSink, canSwim, canWalk, canWalkInLava, entity, isAmphibious, isValid, typeId |
| `EntityNavigationFloatComponent` | 类 | 未实现 | avoidDamageBlocks, avoidPortals, avoidSun, avoidWater, canBreach, canBreakDoors, canFloat, canJump, canOpenDoors, canOpenIronDoors, canPassDoors, canPathFromAir, canPathOverLava, canPathOverWater, canSink, canSwim, canWalk, canWalkInLava, entity, isAmphibious, isValid, typeId |
| `EntityNavigationFlyComponent` | 类 | 未实现 | avoidDamageBlocks, avoidPortals, avoidSun, avoidWater, canBreach, canBreakDoors, canFloat, canJump, canOpenDoors, canOpenIronDoors, canPassDoors, canPathFromAir, canPathOverLava, canPathOverWater, canSink, canSwim, canWalk, canWalkInLava, entity, isAmphibious, isValid, typeId |
| `EntityNavigationGenericComponent` | 类 | 未实现 | avoidDamageBlocks, avoidPortals, avoidSun, avoidWater, canBreach, canBreakDoors, canFloat, canJump, canOpenDoors, canOpenIronDoors, canPassDoors, canPathFromAir, canPathOverLava, canPathOverWater, canSink, canSwim, canWalk, canWalkInLava, entity, isAmphibious, isValid, typeId |
| `EntityNavigationHoverComponent` | 类 | 未实现 | avoidDamageBlocks, avoidPortals, avoidSun, avoidWater, canBreach, canBreakDoors, canFloat, canJump, canOpenDoors, canOpenIronDoors, canPassDoors, canPathFromAir, canPathOverLava, canPathOverWater, canSink, canSwim, canWalk, canWalkInLava, entity, isAmphibious, isValid, typeId |
| `EntityNavigationWalkComponent` | 类 | 未实现 | avoidDamageBlocks, avoidPortals, avoidSun, avoidWater, canBreach, canBreakDoors, canFloat, canJump, canOpenDoors, canOpenIronDoors, canPassDoors, canPathFromAir, canPathOverLava, canPathOverWater, canSink, canSwim, canWalk, canWalkInLava, entity, isAmphibious, isValid, typeId |
| `EntityOnFireComponent` | 类 | 未实现 | entity, isValid, onFireTicksRemaining, typeId |
| `EntityProjectileComponent` | 类 | 未实现 | airInertia, catchFireOnHurt, critParticlesOnProjectileHurt, destroyOnProjectileHurt, entity, gravity, hitEntitySound, hitGroundSound, hitParticle, isValid, lightningStrikeOnHit, liquidInertia, onFireTime, owner, shoot, shouldBounceOnHit, stopOnHit, typeId |
| `EntityPushThroughComponent` | 类 | 未实现 | entity, isValid, typeId, value |
| [EntityQueryOptions](common/reference/EntityQueryOptions.md) | 接口 | 结构契约 | — |
| [EntityQueryPropertyOptions](common/reference/EntityQueryPropertyOptions.md) | 接口 | 结构契约 | — |
| [EntityQueryScoreOptions](common/reference/EntityQueryScoreOptions.md) | 接口 | 结构契约 | — |
| [EntityRaycastHit](common/reference/EntityRaycastHit.md) | 接口 | 结构契约 | — |
| [EntityRaycastOptions](common/reference/EntityRaycastOptions.md) | 接口 | 结构契约 | — |
| [EntityRemoveAfterEvent](server/reference/EntityRemoveAfterEvent.md) | 类 | 部分 | removedEntityId, typeId |
| [EntityRemoveAfterEventSignal](server/reference/EntityRemoveAfterEventSignal.md) | 类 | 待行为核验 | — |
| `EntityRemoveBeforeEvent` | 类 | 未实现 | removedEntity |
| `EntityRemoveBeforeEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `EntityRideableComponent` | 类 | 未实现 | addRider, controllingSeat, crouchingSkipInteract, ejectRider, ejectRiders, entity, getFamilyTypes, getRiders, getSeats, interactText, isValid, passengerMaxWidth, pullInEntities, riderCanInteract, seatCount, typeId |
| `EntityRidingComponent` | 类 | 未实现 | entity, entityRidingOn, isValid, typeId |
| `EntitySaturationComponent` | 类 | 未实现 | currentValue, defaultValue, effectiveMax, effectiveMin, entity, isValid, resetToDefaultValue, resetToMaxValue, resetToMinValue, setCurrentValue, typeId |
| `EntityScaleComponent` | 类 | 未实现 | entity, isValid, typeId, value |
| `EntitySkinIdComponent` | 类 | 未实现 | entity, isValid, typeId, value |
| `EntitySneakingChangedEventOptions` | 接口 | 结构契约 | entityFilter |
| [EntitySpawnAfterEvent](server/reference/EntitySpawnAfterEvent.md) | 类 | 待行为核验 | — |
| [EntitySpawnAfterEventSignal](server/reference/EntitySpawnAfterEventSignal.md) | 类 | 待行为核验 | — |
| `EntitySpawnError` | 类 | 未实现 | — |
| `EntityStartSneakingAfterEvent` | 类 | 未实现 | entity |
| `EntityStartSneakingAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `EntityStopSneakingAfterEvent` | 类 | 未实现 | entity |
| `EntityStopSneakingAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `EntityStrengthComponent` | 类 | 未实现 | entity, isValid, max, typeId, value |
| [EntitySwingSource](common/reference/EntitySwingSource.md) | 枚举 | 常量定义 | — |
| `EntityTameMountComponent` | 类 | 未实现 | entity, isTamed, isTamedToPlayer, isValid, tame, tameToPlayer, tamedToPlayer, tamedToPlayerId, typeId |
| `EntityTameableComponent` | 类 | 未实现 | entity, getTameItems, isTamed, isValid, probability, tame, tamedToPlayer, tamedToPlayerId, typeId |
| `EntityTamedAfterEvent` | 类 | 未实现 | entity, tamingEntity |
| `EntityTamedAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `EntityTamedBeforeEvent` | 类 | 未实现 | cancel, entity, tamingEntity |
| `EntityTamedBeforeEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `EntityTamedEventOptions` | 接口 | 结构契约 | entityFilter, tamingEntityFilter |
| `EntityType` | 类 | 未实现 | id, localizationKey |
| [EntityTypeFamilyComponent](server/reference/EntityTypeFamilyComponent.md) | 类 | 待行为核验 | — |
| `EntityTypes` | 类 | 未实现 | get, getAll |
| [EntityUnderwaterMovementComponent](server/reference/EntityUnderwaterMovementComponent.md) | 类 | 待行为核验 | — |
| `EntityUpgradeAfterEvent` | 类 | 未实现 | entity, getModifiers, upgradeId |
| `EntityUpgradeAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `EntityVariantComponent` | 类 | 未实现 | entity, isValid, typeId, value |
| `EntityVisibilityRules` | 接口 | 结构契约 | showDead, showInvisible, showSneaking |
| `EntityWantsJockeyComponent` | 类 | 未实现 | entity, isValid, typeId |
| `EntityWaypoint` | 类 | 未实现 | color, entity, entityRules, getDimensionLocation, isEnabled, isValid, remove, textureSelector |
| [EqualsComparison](common/reference/EqualsComparison.md) | 接口 | 结构契约 | equals |
| [EquipmentSlot](common/reference/EquipmentSlot.md) | 枚举 | 常量定义 | — |
| `ExplorationMapFunction` | 类 | 未实现 | conditions, destination |
| [ExplosionAfterEvent](server/reference/ExplosionAfterEvent.md) | 类 | 待行为核验 | — |
| [ExplosionAfterEventSignal](server/reference/ExplosionAfterEventSignal.md) | 类 | 待行为核验 | — |
| [ExplosionBeforeEvent](server/reference/ExplosionBeforeEvent.md) | 类 | 部分 | cancel, setImpactedBlocks |
| [ExplosionBeforeEventSignal](server/reference/ExplosionBeforeEventSignal.md) | 类 | 待行为核验 | — |
| `ExplosionDecayFunction` | 类 | 未实现 | conditions |
| [ExplosionOptions](common/reference/ExplosionOptions.md) | 接口 | 结构契约 | — |
| `FeedItem` | 类 | 未实现 | getEffects, healAmount, item, resultItem |
| `FeedItemEffect` | 类 | 未实现 | amplifier, chance, duration, name |
| `FillContainerFunction` | 类 | 未实现 | conditions, lootTable |
| `FluidContainer` | 类 | 未实现 | — |
| [FluidType](common/reference/FluidType.md) | 枚举 | 常量定义 | — |
| `FogSettings` | 类 | 未实现 | getStack, getTags, pop, push, remove, setStack |
| `FogSettingsError` | 类 | 未实现 | — |
| [GameMode](common/reference/GameMode.md) | 枚举 | 常量定义 | — |
| [GameRule](common/reference/GameRule.md) | 枚举 | 常量定义 | — |
| `GameRuleChangeAfterEvent` | 类 | 未实现 | rule, value |
| `GameRuleChangeAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| [GameRules](common/reference/GameRules.md) | 类 | 部分 | commandBlockOutput, doInsomnia, doLimitedCrafting, drowningDamage, fallDamage, fireDamage, freezeDamage, functionCommandLimit, maxCommandChainLength, playersSleepingPercentage, projectilesCanBreakBlocks, recipesUnlock, sendCommandFeedback, showBorderEffect, showDaysPlayed, showDeathMessages, showRecipeMessages, showTags, tntExplosionDropDecay |
| `GetBlocksStandingOnOptions` | 接口 | 结构契约 | blockFilter, ignoreThinBlocks |
| [GraphicsMode](common/reference/GraphicsMode.md) | 枚举 | 常量定义 | — |
| [GreaterThanComparison](common/reference/GreaterThanComparison.md) | 接口 | 结构契约 | greaterThan |
| [GreaterThanOrEqualsComparison](common/reference/GreaterThanOrEqualsComparison.md) | 接口 | 结构契约 | greaterThanOrEquals |
| [HeldItemOption](common/reference/HeldItemOption.md) | 枚举 | 常量定义 | — |
| `HotbarEventOptions` | 接口 | 结构契约 | allowedSlots |
| [HudElement](common/reference/HudElement.md) | 枚举 | 常量定义 | — |
| [HudVisibility](common/reference/HudVisibility.md) | 枚举 | 常量定义 | — |
| `ISerializable` | 类 | 未实现 | — |
| [InputButton](common/reference/InputButton.md) | 枚举 | 常量定义 | — |
| `InputEventOptions` | 接口 | 结构契约 | buttons, state |
| `InputInfo` | 类 | 未实现 | getButtonState, getMovementVector, lastInputModeUsed, touchOnlyAffectsHotbar |
| [InputMode](common/reference/InputMode.md) | 枚举 | 常量定义 | — |
| [InputPermissionCategory](common/reference/InputPermissionCategory.md) | 枚举 | 常量定义 | — |
| `InvalidBlockComponentError` | 类 | 未实现 | — |
| `InvalidContainerError` | 类 | 未实现 | — |
| `InvalidContainerSlotError` | 类 | 未实现 | — |
| `InvalidEntityComponentError` | 类 | 未实现 | — |
| [InvalidEntityError](common/reference/InvalidEntityError.md) | 类 | 待行为核验 | — |
| `InvalidItemStackError` | 类 | 未实现 | itemType |
| `InvalidIteratorError` | 类 | 未实现 | — |
| `InvalidPotionDeliveryTypeError` | 类 | 未实现 | — |
| `InvalidPotionEffectTypeError` | 类 | 未实现 | — |
| [InvalidStructureError](common/reference/InvalidStructureError.md) | 类 | 待行为核验 | — |
| `InvalidWaypointError` | 类 | 未实现 | — |
| `InvalidWaypointTextureSelectorError` | 类 | 未实现 | — |
| `InventoryItemEventOptions` | 接口 | 结构契约 | allowedSlots, excludeItems, excludeTags, ignoreQuantityChange, includeItems, includeTags, inventoryType |
| `IsBabyCondition` | 类 | 未实现 | — |
| `ItemBlockDynamicPropertiesComponent` | 类 | 未实现 | get, isValid, [set](common/type-system.md#set), totalByteCount, typeId |
| `ItemBookComponent` | 类 | 未实现 | author, contents, getPageContent, getRawPageContent, insertPage, isSigned, isValid, pageCount, rawContents, removePage, setContents, setPageContent, signBook, title, typeId |
| [ItemCompleteUseAfterEvent](server/reference/ItemCompleteUseAfterEvent.md) | 类 | 待行为核验 | — |
| [ItemCompleteUseAfterEventSignal](server/reference/ItemCompleteUseAfterEventSignal.md) | 类 | 待行为核验 | — |
| `ItemCompleteUseEvent` | 类 | 未实现 | itemStack, source |
| [ItemComponent](server/reference/ItemComponent.md) | 类 | 待行为核验 | — |
| `ItemComponentBeforeDurabilityDamageEvent` | 类 | 未实现 | attackingEntity, durabilityDamage, hitEntity, itemStack |
| `ItemComponentCompleteUseEvent` | 类 | 未实现 | itemStack, source |
| `ItemComponentConsumeEvent` | 类 | 未实现 | itemStack, source |
| `ItemComponentHitEntityEvent` | 类 | 未实现 | attackingEntity, hadEffect, hitEntity, itemStack |
| `ItemComponentMineBlockEvent` | 类 | 未实现 | block, itemStack, minedBlockPermutation, source |
| `ItemComponentRegistry` | 类 | 未实现 | registerCustomComponent |
| [ItemComponentTypes](common/reference/ItemComponentTypes.md) | 枚举 | 常量定义 | — |
| `ItemComponentUseEvent` | 类 | 未实现 | itemStack, source |
| `ItemComponentUseOnEvent` | 类 | 未实现 | block, blockFace, faceLocation, itemStack, source, usedOnBlockPermutation |
| `ItemCompostableComponent` | 类 | 未实现 | compostingChance, isValid, typeId |
| `ItemCooldownComponent` | 类 | 未实现 | cooldownCategory, cooldownTicks, getCooldownTicksRemaining, isCooldownCategory, isValid, startCooldown, typeId |
| `ItemCustomComponent` | 接口 | 结构契约 | onBeforeDurabilityDamage, onCompleteUse, onConsume, onHitEntity, onMineBlock, onUse, onUseOn |
| `ItemCustomComponentAlreadyRegisteredError` | 类 | 未实现 | — |
| `ItemCustomComponentInstance` | 类 | 未实现 | customComponentParameters, isValid, typeId |
| `ItemCustomComponentReloadNewComponentError` | 类 | 未实现 | — |
| `ItemCustomComponentReloadNewEventError` | 类 | 未实现 | — |
| `ItemCustomComponentReloadVersionError` | 类 | 未实现 | — |
| [ItemDurabilityComponent](server/reference/ItemDurabilityComponent.md) | 类 | 部分 | getDamageChance, getDamageChanceRange, unbreakable |
| `ItemDyeableComponent` | 类 | 未实现 | color, defaultColor, isValid, typeId |
| [ItemEnchantableComponent](server/reference/ItemEnchantableComponent.md) | 类 | 待行为核验 | — |
| `ItemFilter` | 接口 | 结构契约 | includeTypes |
| `ItemFoodComponent` | 类 | 未实现 | canAlwaysEat, isValid, nutrition, saturationModifier, typeId, usingConvertsTo |
| `ItemInventoryComponent` | 类 | 未实现 | container, isValid, typeId |
| [ItemLockMode](common/reference/ItemLockMode.md) | 枚举 | 常量定义 | — |
| `ItemPotionComponent` | 类 | 未实现 | isValid, potionDeliveryType, potionEffectType, typeId |
| `ItemReleaseUseAfterEvent` | 类 | 未实现 | itemStack, source, useDuration |
| `ItemReleaseUseAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| [ItemStack](server/apis/itemStack.md) | 类 | 部分 | getCanDestroy, getCanPlaceOn, getDynamicPropertyTotalByteCount, localizationKey, matches, setCanDestroy, setCanPlaceOn, weight |
| `ItemStartUseAfterEvent` | 类 | 未实现 | itemStack, source, useDuration |
| `ItemStartUseAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| [ItemStartUseOnAfterEvent](server/reference/ItemStartUseOnAfterEvent.md) | 类 | 待行为核验 | — |
| [ItemStartUseOnAfterEventSignal](server/reference/ItemStartUseOnAfterEventSignal.md) | 类 | 待行为核验 | — |
| `ItemStopUseAfterEvent` | 类 | 未实现 | itemStack, source, useDuration |
| `ItemStopUseAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `ItemStopUseOnAfterEvent` | 类 | 未实现 | block, itemStack, source |
| `ItemStopUseOnAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| [ItemType](server/reference/ItemType.md) | 类 | 部分 | localizationKey |
| `ItemTypes` | 类 | 未实现 | get, getAll |
| [ItemUseAfterEvent](server/reference/ItemUseAfterEvent.md) | 类 | 待行为核验 | — |
| [ItemUseAfterEventSignal](server/reference/ItemUseAfterEventSignal.md) | 类 | 待行为核验 | — |
| `ItemUseBeforeEvent` | 类 | 未实现 | cancel, itemStack, source |
| `ItemUseBeforeEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `ItemUseOnEvent` | 类 | 未实现 | block, blockFace, faceLocation, itemStack |
| `JigsawPlaceOptions` | 接口 | 结构契约 | includeEntities, keepJigsaws, liquidSettings |
| `JigsawStructurePlaceOptions` | 接口 | 结构契约 | ignoreStartHeight, includeEntities, keepJigsaws, liquidSettings |
| `KilledByEntityCondition` | 类 | 未实现 | entityType |
| `KilledByPlayerCondition` | 类 | 未实现 | — |
| `KilledByPlayerOrPetsCondition` | 类 | 未实现 | — |
| [LessThanComparison](common/reference/LessThanComparison.md) | 接口 | 结构契约 | lessThan |
| [LessThanOrEqualsComparison](common/reference/LessThanOrEqualsComparison.md) | 接口 | 结构契约 | lessThanOrEquals |
| `LeverActionAfterEvent` | 类 | 未实现 | block, dimension, isPowered, player |
| `LeverActionAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `LinearSpline` | 类 | 未实现 | controlPoints |
| [LiquidSettings](common/reference/LiquidSettings.md) | 枚举 | 常量定义 | — |
| [LiquidType](common/reference/LiquidType.md) | 枚举 | 常量定义 | — |
| [ListBlockVolume](server/reference/ListBlockVolume.md) | 类 | 待行为核验 | — |
| `LocationInUnloadedChunkError` | 类 | 未实现 | — |
| `LocationOutOfWorldBoundariesError` | 类 | 未实现 | — |
| `LocationWaypoint` | 类 | 未实现 | color, getDimensionLocation, isEnabled, isValid, remove, setDimensionLocation, textureSelector |
| `LocatorBar` | 类 | 未实现 | addWaypoint, count, getAllWaypoints, hasWaypoint, maxCount, removeAllWaypoints, removeWaypoint |
| `LocatorBarError` | 类 | 未实现 | reason |
| [LocatorBarErrorReason](common/reference/LocatorBarErrorReason.md) | 枚举 | 常量定义 | — |
| `LootItem` | 类 | 未实现 | conditions, functions, name, quality, subTable, weight |
| `LootItemCondition` | 类 | 未实现 | — |
| `LootItemFunction` | 类 | 未实现 | conditions |
| `LootPool` | 类 | 未实现 | bonusRolls, conditions, entries, rolls, tiers |
| `LootPoolEntry` | 类 | 未实现 | quality, subTable, weight |
| `LootPoolTiers` | 类 | 未实现 | bonusChance, bonusRolls, initialRange |
| `LootTable` | 类 | 未实现 | path, pools |
| `LootTableEntry` | 类 | 未实现 | lootTable, quality, subTable, weight |
| [LootTableManager](server/reference/LootTableManager.md) | 类 | 部分 | generateLootFromBlock, generateLootFromBlockPermutation, generateLootFromBlockType, generateLootFromEntity, generateLootFromEntityType, generateLootFromTable, getLootTable |
| `LootTableReference` | 类 | 未实现 | path, quality, subTable, weight |
| `LootingEnchantFunction` | 类 | 未实现 | conditions, count |
| `MatchToolCondition` | 类 | 未实现 | count, durability, enchantments, itemName, itemTagsAll, itemTagsAny, itemTagsNone |
| [MemoryTier](common/reference/MemoryTier.md) | 枚举 | 常量定义 | — |
| [MolangVariableMap](server/reference/MolangVariableMap.md) | 类 | 待行为核验 | — |
| [MoonPhase](common/reference/MoonPhase.md) | 枚举 | 常量定义 | — |
| [MovementType](common/reference/MovementType.md) | 枚举 | 常量定义 | — |
| [MusicOptions](common/reference/MusicOptions.md) | 接口 | 结构契约 | — |
| `NamespaceNameError` | 类 | 未实现 | reason |
| [NamespaceNameErrorReason](common/reference/NamespaceNameErrorReason.md) | 枚举 | 常量定义 | — |
| [NotEqualsComparison](common/reference/NotEqualsComparison.md) | 接口 | 结构契约 | notEquals |
| [ObjectiveSortOrder](common/reference/ObjectiveSortOrder.md) | 枚举 | 常量定义 | — |
| [PaletteColor](common/reference/PaletteColor.md) | 枚举 | 常量定义 | — |
| `PassengerOfEntityCondition` | 类 | 未实现 | entityType |
| `PistonActivateAfterEvent` | 类 | 未实现 | block, dimension, isExpanding, piston |
| `PistonActivateAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `PlaceJigsawError` | 类 | 未实现 | — |
| [PlatformType](common/reference/PlatformType.md) | 枚举 | 常量定义 | — |
| [PlayAnimationOptions](common/reference/PlayAnimationOptions.md) | 接口 | 结构契约 | — |
| [Player](server/apis/player.md) | 类 | 部分 | addItem, clearPropertyOverridesForEntity, commandPermissionLevel, fogSettings, getAABB, getAimAssist, getAllBlocksStandingOn, getBlockStandingOn, getControlScheme, getItemCooldown, graphicsMode, inputInfo, inputPermissions, isEmoting, isGliding, isJumping, localizationKey, locatorBar, lookAt, nameplateDepthTested, nameplateRenderDistance, onScreenDisplay, playMusic, queueMusic, removePropertyOverrideForEntity, setControlScheme, setPropertyOverrideForEntity, setSpawnPoint, startItemCooldown, stopMusic, totalXpNeededForNextLevel |
| `PlayerAimAssist` | 类 | 未实现 | [set](common/type-system.md#set), settings |
| `PlayerAimAssistSettings` | 接口 | 结构契约 | distance, presetId, targetMode, viewAngle |
| [PlayerBreakBlockAfterEvent](server/reference/PlayerBreakBlockAfterEvent.md) | 类 | 部分 | itemStackAfterBreak, itemStackBeforeBreak |
| [PlayerBreakBlockAfterEventSignal](server/reference/PlayerBreakBlockAfterEventSignal.md) | 类 | 待行为核验 | — |
| [PlayerBreakBlockBeforeEvent](server/reference/PlayerBreakBlockBeforeEvent.md) | 类 | 部分 | itemStack |
| [PlayerBreakBlockBeforeEventSignal](server/reference/PlayerBreakBlockBeforeEventSignal.md) | 类 | 待行为核验 | — |
| `PlayerBreakingBlockEventOptions` | 接口 | 结构契约 | blockFilter, playerFilter |
| `PlayerButtonInputAfterEvent` | 类 | 未实现 | button, newButtonState, player |
| `PlayerButtonInputAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `PlayerCancelBreakingBlockAfterEvent` | 类 | 未实现 | block, blockPermutation, breakProgress, dimension, face, heldItemStack, player |
| `PlayerCancelBreakingBlockAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `PlayerCursorInventoryComponent` | 类 | 未实现 | clear, entity, isValid, item, typeId |
| [PlayerDimensionChangeAfterEvent](server/reference/PlayerDimensionChangeAfterEvent.md) | 类 | 待行为核验 | — |
| [PlayerDimensionChangeAfterEventSignal](server/reference/PlayerDimensionChangeAfterEventSignal.md) | 类 | 待行为核验 | — |
| `PlayerEmoteAfterEvent` | 类 | 未实现 | personaPieceId, player |
| `PlayerEmoteAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `PlayerGameModeChangeAfterEvent` | 类 | 未实现 | fromGameMode, player, toGameMode |
| `PlayerGameModeChangeAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `PlayerGameModeChangeBeforeEvent` | 类 | 未实现 | cancel, fromGameMode, player, toGameMode |
| `PlayerGameModeChangeBeforeEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `PlayerHotbarSelectedSlotChangeAfterEvent` | 类 | 未实现 | itemStack, newSlotSelected, player, previousSlotSelected |
| `PlayerHotbarSelectedSlotChangeAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `PlayerInputModeChangeAfterEvent` | 类 | 未实现 | newInputModeUsed, player, previousInputModeUsed |
| `PlayerInputModeChangeAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `PlayerInputPermissionCategoryChangeAfterEvent` | 类 | 未实现 | category, enabled, player |
| `PlayerInputPermissionCategoryChangeAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `PlayerInputPermissions` | 类 | 未实现 | isPermissionCategoryEnabled, setPermissionCategory |
| `PlayerInteractWithBlockAfterEvent` | 类 | 未实现 | beforeItemStack, block, blockFace, faceLocation, isFirstEvent, itemStack, player |
| `PlayerInteractWithBlockAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `PlayerInteractWithBlockBeforeEvent` | 类 | 未实现 | block, blockFace, cancel, faceLocation, isFirstEvent, itemStack, player |
| `PlayerInteractWithBlockBeforeEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| [PlayerInteractWithEntityAfterEvent](server/reference/PlayerInteractWithEntityAfterEvent.md) | 类 | 待行为核验 | — |
| [PlayerInteractWithEntityAfterEventSignal](server/reference/PlayerInteractWithEntityAfterEventSignal.md) | 类 | 待行为核验 | — |
| [PlayerInteractWithEntityBeforeEvent](server/reference/PlayerInteractWithEntityBeforeEvent.md) | 类 | 待行为核验 | — |
| [PlayerInteractWithEntityBeforeEventSignal](server/reference/PlayerInteractWithEntityBeforeEventSignal.md) | 类 | 待行为核验 | — |
| [PlayerInventoryItemChangeAfterEvent](server/reference/PlayerInventoryItemChangeAfterEvent.md) | 类 | 待行为核验 | — |
| [PlayerInventoryItemChangeAfterEventSignal](server/reference/PlayerInventoryItemChangeAfterEventSignal.md) | 类 | 待行为核验 | — |
| [PlayerInventoryType](common/reference/PlayerInventoryType.md) | 枚举 | 常量定义 | — |
| [PlayerJoinAfterEvent](server/reference/PlayerJoinAfterEvent.md) | 类 | 部分 | playerId |
| [PlayerJoinAfterEventSignal](server/reference/PlayerJoinAfterEventSignal.md) | 类 | 待行为核验 | — |
| [PlayerLeaveAfterEvent](server/reference/PlayerLeaveAfterEvent.md) | 类 | 部分 | playerId |
| [PlayerLeaveAfterEventSignal](server/reference/PlayerLeaveAfterEventSignal.md) | 类 | 待行为核验 | — |
| `PlayerLeaveBeforeEvent` | 类 | 未实现 | player |
| `PlayerLeaveBeforeEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| [PlayerPermissionLevel](common/reference/PlayerPermissionLevel.md) | 枚举 | 常量定义 | — |
| [PlayerPlaceBlockAfterEvent](server/reference/PlayerPlaceBlockAfterEvent.md) | 类 | 待行为核验 | — |
| [PlayerPlaceBlockAfterEventSignal](server/reference/PlayerPlaceBlockAfterEventSignal.md) | 类 | 待行为核验 | — |
| [PlayerSoundOptions](common/reference/PlayerSoundOptions.md) | 接口 | 结构契约 | loopCount |
| [PlayerSpawnAfterEvent](server/reference/PlayerSpawnAfterEvent.md) | 类 | 待行为核验 | — |
| [PlayerSpawnAfterEventSignal](server/reference/PlayerSpawnAfterEventSignal.md) | 类 | 待行为核验 | — |
| [PlayerSplitScreenSlot](common/reference/PlayerSplitScreenSlot.md) | 枚举 | 常量定义 | — |
| `PlayerStartBreakingBlockAfterEvent` | 类 | 未实现 | block, blockPermutation, dimension, face, heldItemStack, player |
| `PlayerStartBreakingBlockAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `PlayerSwingEventOptions` | 接口 | 结构契约 | heldItemOption, swingSource |
| `PlayerSwingStartAfterEvent` | 类 | 未实现 | heldItemStack, player, swingSource |
| `PlayerSwingStartAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `PlayerVisibilityRules` | 接口 | 结构契约 | showDead, showHidden, showInvisible, showSneaking, showSpectator, showSpectatorToSpectator |
| `PlayerWaypoint` | 类 | 未实现 | color, entity, entityRules, getDimensionLocation, isEnabled, isValid, playerRules, remove, textureSelector |
| `PotionDeliveryType` | 类 | 未实现 | id |
| `PotionEffectType` | 类 | 未实现 | durationTicks, id |
| `Potions` | 类 | 未实现 | getAllDeliveryTypes, getAllEffectTypes, getDeliveryType, getEffectType, resolve |
| `PressurePlatePopAfterEvent` | 类 | 未实现 | block, dimension, previousRedstonePower, redstonePower |
| `PressurePlatePopAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `PressurePlatePushAfterEvent` | 类 | 未实现 | block, dimension, previousRedstonePower, redstonePower, source |
| `PressurePlatePushAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `PrimitiveShape` | 类 | 未实现 | attachedTo, color, dimension, hasDuration, location, maximumRenderDistance, remove, rotation, scale, setLocation, timeLeft, totalTimeLeft, visibleTo |
| `PrimitiveShapeError` | 类 | 未实现 | — |
| `PrimitiveShapeQueryOptions` | 接口 | 结构契约 | attachedTo, location, maxDistance, minDistance |
| [PrimitiveShapesManager](server/reference/PrimitiveShapesManager.md) | 类 | 部分 | addText, getShapes, removeAll, removeText |
| `ProgressKeyFrame` | 接口 | 结构契约 | alpha, easingFunc, timeSeconds |
| [ProjectileHitBlockAfterEvent](server/reference/ProjectileHitBlockAfterEvent.md) | 类 | 待行为核验 | — |
| [ProjectileHitBlockAfterEventSignal](server/reference/ProjectileHitBlockAfterEventSignal.md) | 类 | 待行为核验 | — |
| [ProjectileHitEntityAfterEvent](server/reference/ProjectileHitEntityAfterEvent.md) | 类 | 待行为核验 | — |
| [ProjectileHitEntityAfterEventSignal](server/reference/ProjectileHitEntityAfterEventSignal.md) | 类 | 待行为核验 | — |
| `ProjectileShootOptions` | 接口 | 结构契约 | uncertainty |
| [RGB](server/reference/RGB.md) | 接口 | 结构契约 | blue, green, red |
| [RGBA](server/reference/RGBA.md) | 接口 | 结构契约 | alpha, blue, green, red |
| `RandomAuxValueFunction` | 类 | 未实现 | conditions, values |
| `RandomBlockStateFunction` | 类 | 未实现 | blockState, conditions, values |
| `RandomChanceCondition` | 类 | 未实现 | chance |
| `RandomChanceWithLootingCondition` | 类 | 未实现 | chance, lootingMultiplier |
| `RandomDifficultyChanceCondition` | 类 | 未实现 | chances |
| `RandomDyeFunction` | 类 | 未实现 | conditions |
| `RandomRegionalDifficultyChanceCondition` | 类 | 未实现 | maxChance |
| [RangeComparison](common/reference/RangeComparison.md) | 接口 | 结构契约 | lowerBound, upperBound |
| `RawMessage` | 接口 | 结构契约 | rawtext, score, text, translate, with |
| `RawMessageError` | 类 | 未实现 | — |
| `RawMessageScore` | 接口 | 结构契约 | name, objective |
| `RawText` | 接口 | 结构契约 | rawtext |
| `RotationKeyFrame` | 接口 | 结构契约 | easingFunc, rotation, timeSeconds |
| [Scoreboard](server/reference/Scoreboard.md) | 类 | 部分 | getObjectiveAtDisplaySlot, getParticipants, removeObjective, setObjectiveAtDisplaySlot |
| [ScoreboardIdentity](server/reference/ScoreboardIdentity.md) | 类 | 待行为核验 | — |
| [ScoreboardIdentityType](common/reference/ScoreboardIdentityType.md) | 枚举 | 常量定义 | — |
| [ScoreboardObjective](server/reference/ScoreboardObjective.md) | 类 | 部分 | hasParticipant, removeParticipant, setScore |
| `ScoreboardObjectiveDisplayOptions` | 接口 | 结构契约 | objective, sortOrder |
| [ScoreboardScoreInfo](server/reference/ScoreboardScoreInfo.md) | 类 | 待行为核验 | — |
| `ScreenDisplay` | 类 | 未实现 | getHiddenHudElements, hideAllExcept, isForcedHidden, isValid, resetHudElementsVisibility, setActionBar, setHudVisibility, setTitle, updateSubtitle |
| [ScriptEventCommandMessageAfterEvent](server/reference/ScriptEventCommandMessageAfterEvent.md) | 类 | 待行为核验 | — |
| [ScriptEventCommandMessageAfterEventSignal](server/reference/ScriptEventCommandMessageAfterEventSignal.md) | 类 | 待行为核验 | — |
| [ScriptEventMessageFilterOptions](common/reference/ScriptEventMessageFilterOptions.md) | 接口 | 结构契约 | namespaces |
| [ScriptEventSource](common/reference/ScriptEventSource.md) | 枚举 | 常量定义 | — |
| `Seat` | 类 | 未实现 | lockRiderRotation, maxRiderCount, minRiderCount, position, seatRotation |
| `SetArmorTrimFunction` | 类 | 未实现 | conditions, material, pattern |
| `SetBannerDetailsFunction` | 类 | 未实现 | conditions, [type](common/type-system.md#type) |
| `SetBookContentsFunction` | 类 | 未实现 | author, conditions, pages, title |
| `SetDataFromColorIndexFunction` | 类 | 未实现 | conditions |
| `SetItemCountFunction` | 类 | 未实现 | conditions, count |
| `SetItemDamageFunction` | 类 | 未实现 | conditions, damage |
| `SetItemDataFunction` | 类 | 未实现 | conditions, data |
| `SetItemLoreFunction` | 类 | 未实现 | conditions, lore |
| `SetItemNameFunction` | 类 | 未实现 | conditions, name |
| `SetOminousBottleFunction` | 类 | 未实现 | amplifier, conditions |
| `SetPotionFunction` | 类 | 未实现 | conditions, id |
| `SetSpawnEggFunction` | 类 | 未实现 | conditions, id |
| `SetStewEffectFunction` | 类 | 未实现 | conditions, effects |
| `ShutdownBeforeEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `ShutdownEvent` | 类 | 未实现 | — |
| [SignSide](common/reference/SignSide.md) | 枚举 | 常量定义 | — |
| `SmeltItemFunction` | 类 | 未实现 | conditions |
| `SoundCompletedAfterEvent` | 类 | 未实现 | soundInstanceId |
| `SoundCompletedAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `SoundDefinition` | 类 | 未实现 | durationInfo, musicInfo, soundEventId, tags |
| `SoundDefinitionDurationInfo` | 接口 | 结构契约 | duration |
| `SoundDefinitionFilter` | 接口 | 结构契约 | artists, genres, maxDuration, minDuration, moods, tags, titles |
| `SoundDefinitionMusicInfo` | 接口 | 结构契约 | artist, genres, moods, title |
| `SoundDefinitionRegistry` | 类 | 未实现 | getDefinitions |
| `SoundDurationInfo` | 类 | 未实现 | duration, getPlaybackPosition, isActive |
| `SoundInstance` | 类 | 未实现 | durationInfo, fade, id, pause, recipient, resume, seekTo, setPitch, setVolume, soundEventId, stop |
| [SpawnEntityOptions](common/reference/SpawnEntityOptions.md) | 接口 | 结构契约 | — |
| `SpecificEnchantFunction` | 类 | 未实现 | conditions, enchantments |
| `SplineAnimation` | 接口 | 结构契约 | progressKeyFrames, rotationKeyFrames |
| [StartupBeforeEventSignal](server/reference/StartupBeforeEventSignal.md) | 类 | 待行为核验 | — |
| `StartupEvent` | 类 | 未实现 | blockComponentRegistry, customCommandRegistry, dimensionRegistry, itemComponentRegistry, worldClockRegistry |
| [StickyType](common/reference/StickyType.md) | 枚举 | 常量定义 | — |
| [Structure](server/reference/Structure.md) | 类 | 待行为核验 | — |
| [StructureAnimationMode](common/reference/StructureAnimationMode.md) | 枚举 | 常量定义 | — |
| [StructureCreateOptions](common/reference/StructureCreateOptions.md) | 接口 | 结构契约 | includeBlocks, includeEntities, saveMode |
| [StructureManager](server/reference/StructureManager.md) | 类 | 部分 | getPackStructureIds, getWorldStructureIds, placeJigsaw, placeJigsawStructure |
| [StructureMirrorAxis](common/reference/StructureMirrorAxis.md) | 枚举 | 常量定义 | — |
| [StructurePlaceOptions](common/reference/StructurePlaceOptions.md) | 接口 | 结构契约 | animationMode, animationSeconds, includeBlocks, includeEntities, integrity, integritySeed, mirror, rotation, waterlogged |
| [StructureRotation](common/reference/StructureRotation.md) | 枚举 | 常量定义 | — |
| [StructureSaveMode](common/reference/StructureSaveMode.md) | 枚举 | 常量定义 | — |
| [System](server/reference/System.md) | 类 | 部分 | currentTick, isEditorWorld, sendScriptEvent, serverSystemInfo |
| [SystemAfterEvents](server/reference/SystemAfterEvents.md) | 类 | 待行为核验 | — |
| [SystemBeforeEvents](server/reference/SystemBeforeEvents.md) | 类 | 部分 | shutdown |
| `SystemInfo` | 类 | 未实现 | memoryTier |
| `TargetBlockHitAfterEvent` | 类 | 未实现 | block, dimension, hitVector, previousRedstonePower, redstonePower, source |
| `TargetBlockHitAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| [TeleportOptions](common/reference/TeleportOptions.md) | 接口 | 结构契约 | forceProvidedPositionOnDimensionChange |
| `TextPrimitive` | 类 | 未实现 | attachedTo, backfaceVisible, backgroundColorOverride, color, depthTest, dimension, hasDuration, lineGapHeight, location, maximumRenderDistance, remove, rotation, scale, setLocation, setText, text, textBackfaceVisible, timeLeft, totalTimeLeft, useRotation, visibleTo |
| [TickingArea](common/reference/TickingArea.md) | 接口 | 结构契约 | — |
| `TickingAreaError` | 类 | 未实现 | reason |
| [TickingAreaErrorReason](common/reference/TickingAreaErrorReason.md) | 枚举 | 常量定义 | — |
| [TickingAreaManager](server/reference/TickingAreaManager.md) | 类 | 待行为核验 | — |
| [TickingAreaOptions](common/reference/TickingAreaOptions.md) | 接口 | 结构契约 | from |
| `TimeMarker` | 类 | 未实现 | name, period, time |
| `TimeMarkerOptions` | 接口 | 结构契约 | name, period, time |
| [TimeOfDay](common/reference/TimeOfDay.md) | 枚举 | 常量定义 | — |
| [TintMethod](common/reference/TintMethod.md) | 枚举 | 常量定义 | — |
| `TitleDisplayOptions` | 接口 | 结构契约 | fadeInDuration, fadeOutDuration, stayDuration, subtitle |
| `Trigger` | 类 | 未实现 | eventName |
| `TripWireTripAfterEvent` | 类 | 未实现 | block, dimension, isPowered, sources |
| `TripWireTripAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| [UnloadedChunksError](common/reference/UnloadedChunksError.md) | 类 | 待行为核验 | — |
| [Vector2](common/reference/Vector2.md) | 接口 | 结构契约 | — |
| [Vector3](server/extra/vector.md) | 接口 | 结构契约 | — |
| [VectorXZ](common/reference/VectorXZ.md) | 接口 | 结构契约 | — |
| `Waypoint` | 类 | 未实现 | color, getDimensionLocation, isEnabled, isValid, remove, textureSelector |
| [WaypointTexture](common/reference/WaypointTexture.md) | 枚举 | 常量定义 | — |
| `WaypointTextureBounds` | 接口 | 结构契约 | lowerBound, texture, upperBound |
| `WaypointTextureSelector` | 接口 | 结构契约 | textureBoundsList |
| `WeatherChangeAfterEvent` | 类 | 未实现 | dimension, newWeather, previousWeather |
| `WeatherChangeAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `WeatherChangeBeforeEvent` | 类 | 未实现 | cancel, duration, newWeather, previousWeather |
| `WeatherChangeBeforeEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| [WeatherType](common/reference/WeatherType.md) | 枚举 | 常量定义 | — |
| [World](server/apis/world.md) | 类 | 部分 | clearDynamicProperties, getAimAssist, getClock, getPackSettings, isHardcore, playMusic, primitiveShapesManager, queueMusic, soundDefinitionRegistry, stopMusic |
| [WorldAfterEvents](server/events/afterEvents.md) | 类 | 部分 | blockContainerClosed, blockContainerOpened, buttonPush, entityContainerClosed, entityContainerOpened, entityHeal, entityHitBlock, entityItemDrop, entityItemPickup, entityStartSneaking, entityStopSneaking, entityTamed, entityUpgrade, gameRuleChange, itemReleaseUse, itemStartUse, itemStopUse, itemStopUseOn, leverAction, pistonActivate, playerButtonInput, playerCancelBreakingBlock, playerEmote, playerGameModeChange, playerHotbarSelectedSlotChange, playerInputModeChange, playerInputPermissionCategoryChange, playerInteractWithBlock, playerStartBreakingBlock, playerSwingStart, pressurePlatePop, pressurePlatePush, soundCompleted, targetBlockHit, tripWireTrip, weatherChange, worldClockOnPaused, worldClockOnResumed, worldClockOnTimeMarker, worldClockOnTimeModified, worldLoad |
| [WorldBeforeEvents](server/events/beforeEvents.md) | 类 | 部分 | effectAdd, entityHeal, entityItemPickup, entityRemove, entityTamed, itemUse, playerGameModeChange, playerInteractWithBlock, playerLeave, weatherChange, worldClockOnRestart |
| `WorldClock` | 类 | 未实现 | addTimeMarker, isPaused, name, removeTimeMarker, rewindTo, [set](common/type-system.md#set), skipTo, time, timeMarkers |
| `WorldClockAddTimeMarkerError` | 类 | 未实现 | — |
| `WorldClockEventOptions` | 接口 | 结构契约 | clock |
| `WorldClockInvalidRegistryError` | 类 | 未实现 | — |
| `WorldClockInvalidTimeMarkerError` | 类 | 未实现 | — |
| `WorldClockNotFoundError` | 类 | 未实现 | — |
| `WorldClockOnPausedAfterEvent` | 类 | 未实现 | clock |
| `WorldClockOnPausedAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `WorldClockOnRestartBeforeEvent` | 类 | 未实现 | cancel, clock, newTime |
| `WorldClockOnRestartBeforeEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `WorldClockOnResumedAfterEvent` | 类 | 未实现 | clock |
| `WorldClockOnResumedAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `WorldClockOnTimeMarkerAfterEvent` | 类 | 未实现 | clock, timeMarker |
| `WorldClockOnTimeMarkerAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `WorldClockOnTimeModifiedAfterEvent` | 类 | 未实现 | clock |
| `WorldClockOnTimeModifiedAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `WorldClockRegistrationError` | 类 | 未实现 | — |
| `WorldClockRegistrationOptions` | 接口 | 结构契约 | timeMarkers |
| `WorldClockRegistry` | 类 | 未实现 | registerClock |
| `WorldClockReloadNewWorldClockError` | 类 | 未实现 | — |
| `WorldClockReloadTimeMarkerError` | 类 | 未实现 | — |
| `WorldClockRemoveMinecraftTimeMarkerError` | 类 | 未实现 | — |
| `WorldClockRewindError` | 类 | 未实现 | — |
| `WorldClockTimeMarkerEventOptions` | 接口 | 结构契约 | clock, timeMarker |
| `WorldClockTimeMarkerNotFoundError` | 类 | 未实现 | — |
| `WorldLoadAfterEvent` | 类 | 未实现 | — |
| `WorldLoadAfterEventSignal` | 类 | 未实现 | subscribe, unsubscribe |
| `WorldSoundOptions` | 接口 | 结构契约 | isBroadcast, loopCount, pitch, volume |

## @minecraft/server-ui 2.3.0

[微软模块文档](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-ui/minecraft-server-ui?view=minecraft-bedrock-stable)

### 已知限制

- `CustomForm.image`：网易 JSON [UI](server_ui/reference/UI.md) 以全局贴图路径查找资源，当前适配器无法按官方 pack 标识解析并隔离贴图；动态图也未核实。
- `ObservableString.getFilteredText`：未找到按玩家调用微软文本过滤服务的网易接口；不能把未过滤原文冒充过滤结果。
- `*.translate`：未找到可供当前 JSON [UI](server_ui/reference/UI.md) 适配器调用的本地化键解析接口；目前仅支持 text/rawtext 的字面文本。
- `*.tooltip`：已保留参数；悬浮提示和移动端呈现尚未接入，不能视为已经支持。
- `*.description`：已保留动态参数；描述文字布局尚未接入。
- `ModalFormData.textField.placeholderText`：参数已保存，客户端占位符布局尚未接入。
- `UserBusy/native`：当前检测本库正在显示的表单；原生聊天/背包/第三方 [UI](server_ui/reference/UI.md) 的忙碌状态和打开失败需客户端握手，尚未实现。
- `CustomForm/native DDUI`：网易侧使用 JSON [UI](server_ui/reference/UI.md) 渲染，不能提供微软 DDUI 原生外观、引擎错误和限制执行阶段的完全等价行为。
- `CustomForm.dropdown/dynamic items`：当前实现会重建变化的下拉项目并复用未变化节点；真实客户端布局和更新时序仍需实机验证。
- `*.RawMessage(score/selector)`：当前 JSON [UI](server_ui/reference/UI.md) 只接受字面 text/rawtext；score/selector 解析及依赖玩家上下文的格式尚未接入。

### 全部官方类型对照

| 名称 | 类别 | 当前结构状态 | 缺失 / 空成员 |
| --- | --- | --- | --- |
| [ActionFormData](server_ui/reference/ActionFormData.md) | 类 | 待行为核验 | — |
| [ActionFormResponse](server_ui/reference/ActionFormResponse.md) | 类 | 待行为核验 | — |
| [ButtonOptions](server_ui/reference/ButtonOptions.md) | 接口 | 结构契约 | disabled, imageDetails, tooltip, visible |
| [CustomForm](server_ui/reference/CustomForm.md) | 类 | 部分 | image |
| [DataDrivenScreenClosedReason](server_ui/reference/DataDrivenScreenClosedReason.md) | 枚举 | 常量定义 | — |
| [DividerOptions](server_ui/reference/DividerOptions.md) | 接口 | 结构契约 | visible |
| `DropdownItemData` | 接口 | 结构契约 | description, label, value |
| [DropdownOptions](server_ui/reference/DropdownOptions.md) | 接口 | 结构契约 | description, disabled, tooltip, visible |
| [FormCancelationReason](server_ui/reference/FormCancelationReason.md) | 枚举 | 常量定义 | — |
| [FormRejectError](server_ui/reference/FormRejectError.md) | 类 | 待行为核验 | — |
| [FormRejectReason](server_ui/reference/FormRejectReason.md) | 枚举 | 常量定义 | — |
| [FormResponse](server_ui/reference/FormResponse.md) | 类 | 待行为核验 | — |
| [FormVisibilityError](server_ui/reference/FormVisibilityError.md) | 类 | 待行为核验 | — |
| [FormVisibilityErrorReason](server_ui/reference/FormVisibilityErrorReason.md) | 枚举 | 常量定义 | — |
| `ImageDetails` | 接口 | 结构契约 | imagePackId, imageSrc |
| `ImageOptions` | 接口 | 结构契约 | onClick, tooltip, visible, width |
| [InvalidFormError](server_ui/reference/InvalidFormError.md) | 类 | 待行为核验 | — |
| [InvalidFormModificationError](server_ui/reference/InvalidFormModificationError.md) | 类 | 待行为核验 | — |
| [InvalidObservableError](server_ui/reference/InvalidObservableError.md) | 类 | 待行为核验 | — |
| [MessageBox](server_ui/reference/MessageBox.md) | 类 | 部分 | button1WithOptions, button2WithOptions |
| `MessageBoxButtonOptions` | 接口 | 结构契约 | imageDetails, tooltip |
| [MessageBoxResult](server_ui/reference/MessageBoxResult.md) | 接口 | 结构契约 | — |
| [MessageFormData](server_ui/reference/MessageFormData.md) | 类 | 待行为核验 | — |
| [MessageFormResponse](server_ui/reference/MessageFormResponse.md) | 类 | 待行为核验 | — |
| [ModalFormData](server_ui/reference/ModalFormData.md) | 类 | 待行为核验 | — |
| [ModalFormDataDropdownOptions](server_ui/reference/ModalFormDataDropdownOptions.md) | 接口 | 结构契约 | defaultValueIndex, tooltip |
| [ModalFormDataSliderOptions](server_ui/reference/ModalFormDataSliderOptions.md) | 接口 | 结构契约 | defaultValue, tooltip, valueStep |
| [ModalFormDataTextFieldOptions](server_ui/reference/ModalFormDataTextFieldOptions.md) | 接口 | 结构契约 | defaultValue, tooltip |
| [ModalFormDataToggleOptions](server_ui/reference/ModalFormDataToggleOptions.md) | 接口 | 结构契约 | defaultValue, tooltip |
| [ModalFormResponse](server_ui/reference/ModalFormResponse.md) | 类 | 待行为核验 | — |
| [ObservableBoolean](server_ui/reference/ObservableBoolean.md) | 类 | 待行为核验 | — |
| [ObservableNumber](server_ui/reference/ObservableNumber.md) | 类 | 待行为核验 | — |
| [ObservableOptions](server_ui/reference/ObservableOptions.md) | 接口 | 结构契约 | clientWritable |
| [ObservableString](server_ui/reference/ObservableString.md) | 类 | 部分 | getFilteredText |
| [ObservableUIRawMessage](server_ui/reference/ObservableUIRawMessage.md) | 类 | 待行为核验 | — |
| [PlayerLeftError](server_ui/reference/PlayerLeftError.md) | 类 | 待行为核验 | — |
| [SliderOptions](server_ui/reference/SliderOptions.md) | 接口 | 结构契约 | description, disabled, step, tooltip, visible |
| `SpacingOptions` | 接口 | 结构契约 | visible |
| [TextFieldOptions](server_ui/reference/TextFieldOptions.md) | 接口 | 结构契约 | description, disabled, tooltip, visible |
| [TextFilteringError](server_ui/reference/TextFilteringError.md) | 枚举 | 常量定义 | — |
| `TextOptions` | 接口 | 结构契约 | tooltip, visible |
| [ToggleOptions](server_ui/reference/ToggleOptions.md) | 接口 | 结构契约 | description, disabled, tooltip, visible |
| [UIManager](server_ui/reference/UIManager.md) | 类 | 待行为核验 | — |
| `UIRawMessage` | 接口 | 结构契约 | rawtext, text, translate, with |