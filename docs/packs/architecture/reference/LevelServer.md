---
title: "LevelServer"
sidebar_label: "LevelServer"
---

# LevelServer

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/level/server.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `game` | 由运行时值确定 | `compServer.CreateGame(levelId)` |  |
| `chunkSource` | 由运行时值确定 | `compServer.CreateChunkSource(levelId)` |  |
| `achievement` | 由运行时值确定 | `compServer.CreateAchievement(levelId)` |  |
| `biome` | 由运行时值确定 | `compServer.CreateBiome(levelId)` |  |
| `dimension` | 由运行时值确定 | `compServer.CreateDimension(levelId)` |  |
| `blockInfo` | 由运行时值确定 | `compServer.CreateBlockInfo(levelId)` |  |
| `weather` | 由运行时值确定 | `compServer.CreateWeather(levelId)` |  |
| `time` | 由运行时值确定 | `compServer.CreateTime(levelId)` |  |
| `block` | 由运行时值确定 | `compServer.CreateBlock(levelId)` |  |
| `blockEntity` | 由运行时值确定 | `compServer.CreateBlockEntity(levelId)` |  |
| `blockEntityData` | 由运行时值确定 | `compServer.CreateBlockEntityData(levelId)` |  |
| `blockState` | 由运行时值确定 | `compServer.CreateBlockState(levelId)` |  |
| `blockUseEventWhiteList` | 由运行时值确定 | `compServer.CreateBlockUseEventWhiteList(levelId)` |  |
| `message` | 由运行时值确定 | `compServer.CreateMsg(levelId)` |  |
| `command` | 由运行时值确定 | `compServer.CreateCommand(levelId)` |  |
| `chestBlock` | 由运行时值确定 | `compServer.CreateChestBlock(levelId)` |  |
| `explosion` | 由运行时值确定 | `compServer.CreateExplosion(levelId)` |  |
| `extraData` | 由运行时值确定 | `compServer.CreateExtraData(levelId)` |  |
| `feature` | 由运行时值确定 | `compServer.CreateFeature(levelId)` |  |
| `itemBanned` | 由运行时值确定 | `compServer.CreateItemBanned(levelId)` |  |
| `mobSpawn` | 由运行时值确定 | `compServer.CreateMobSpawn(levelId)` |  |
| `projectile` | 由运行时值确定 | `compServer.CreateProjectile(levelId)` |  |
| `portal` | 由运行时值确定 | `compServer.CreatePortal(levelId)` |  |
| `recipe` | 由运行时值确定 | `compServer.CreateRecipe(levelId)` |  |
| `redstone` | 由运行时值确定 | `compServer.CreateRedStone(levelId)` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 LevelServer 对象。
    print(value.game)
    print(value.chunkSource)
    print(value.achievement)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)