---
title: "GameRule"
sidebar_label: "GameRule"
---

# GameRule

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/enums/stable.py`；声明补充了静态类型信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `CommandBlockOutput` | [str](../type-system.md#str) | `'commandBlockOutput'` |  |
| `CommandBlocksEnabled` | [str](../type-system.md#str) | `'commandBlocksEnabled'` |  |
| `DoDayLightCycle` | [str](../type-system.md#str) | `'doDayLightCycle'` |  |
| `DoEntityDrops` | [str](../type-system.md#str) | `'doEntityDrops'` |  |
| `DoFireTick` | [str](../type-system.md#str) | `'doFireTick'` |  |
| `DoImmediateRespawn` | [str](../type-system.md#str) | `'doImmediateRespawn'` |  |
| `DoInsomnia` | [str](../type-system.md#str) | `'doInsomnia'` |  |
| `DoLimitedCrafting` | [str](../type-system.md#str) | `'doLimitedCrafting'` |  |
| `DoMobLoot` | [str](../type-system.md#str) | `'doMobLoot'` |  |
| `DoMobSpawning` | [str](../type-system.md#str) | `'doMobSpawning'` |  |
| `DoTileDrops` | [str](../type-system.md#str) | `'doTileDrops'` |  |
| `DoWeatherCycle` | [str](../type-system.md#str) | `'doWeatherCycle'` |  |
| `DrowningDamage` | [str](../type-system.md#str) | `'drowningDamage'` |  |
| `FallDamage` | [str](../type-system.md#str) | `'fallDamage'` |  |
| `FireDamage` | [str](../type-system.md#str) | `'fireDamage'` |  |
| `FreezeDamage` | [str](../type-system.md#str) | `'freezeDamage'` |  |
| `FunctionCommandLimit` | [str](../type-system.md#str) | `'functionCommandLimit'` |  |
| `KeepInventory` | [str](../type-system.md#str) | `'keepInventory'` |  |
| `MaxCommandChainLength` | [str](../type-system.md#str) | `'maxCommandChainLength'` |  |
| `MobGriefing` | [str](../type-system.md#str) | `'mobGriefing'` |  |
| `NaturalRegeneration` | [str](../type-system.md#str) | `'naturalRegeneration'` |  |
| `PlayersSleepingPercentage` | [str](../type-system.md#str) | `'playersSleepingPercentage'` |  |
| `ProjectilesCanBreakBlocks` | [str](../type-system.md#str) | `'projectilesCanBreakBlocks'` |  |
| `Pvp` | [str](../type-system.md#str) | `'pvp'` |  |
| `RandomTickSpeed` | [str](../type-system.md#str) | `'randomTickSpeed'` |  |
| `RecipesUnlock` | [str](../type-system.md#str) | `'recipesUnlock'` |  |
| `RespawnBlocksExplode` | [str](../type-system.md#str) | `'respawnBlocksExplode'` |  |
| `SendCommandFeedback` | [str](../type-system.md#str) | `'sendCommandFeedback'` |  |
| `ShowBorderEffect` | [str](../type-system.md#str) | `'showBorderEffect'` |  |
| `ShowCoordinates` | [str](../type-system.md#str) | `'showCoordinates'` |  |
| `ShowDaysPlayed` | [str](../type-system.md#str) | `'showDaysPlayed'` |  |
| `ShowDeathMessages` | [str](../type-system.md#str) | `'showDeathMessages'` |  |
| `ShowRecipeMessages` | [str](../type-system.md#str) | `'showRecipeMessages'` |  |
| `ShowTags` | [str](../type-system.md#str) | `'showTags'` |  |
| `SpawnRadius` | [str](../type-system.md#str) | `'spawnRadius'` |  |
| `TntExplodes` | [str](../type-system.md#str) | `'tntExplodes'` |  |
| `TntExplosionDropDecay` | [str](../type-system.md#str) | `'tntExplosionDropDecay'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 GameRule 对象。
    print(value.CommandBlockOutput)
    print(value.CommandBlocksEnabled)
    print(value.DoDayLightCycle)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)