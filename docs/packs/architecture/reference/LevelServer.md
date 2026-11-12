---
title: "LevelServer"
sidebar_label: "LevelServer"
---

import ApiFieldAnchor from '@docusaurus/Link';

# LevelServer

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/level/server.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-game" />`game` | 由运行时值确定 | `compServer.CreateGame(levelId)` |  |
| <ApiFieldAnchor id="field-chunkSource" />`chunkSource` | 由运行时值确定 | `compServer.CreateChunkSource(levelId)` |  |
| <ApiFieldAnchor id="field-achievement" />`achievement` | 由运行时值确定 | `compServer.CreateAchievement(levelId)` |  |
| <ApiFieldAnchor id="field-biome" />`biome` | 由运行时值确定 | `compServer.CreateBiome(levelId)` |  |
| <ApiFieldAnchor id="field-dimension" />`dimension` | 由运行时值确定 | `compServer.CreateDimension(levelId)` |  |
| <ApiFieldAnchor id="field-blockInfo" />`blockInfo` | 由运行时值确定 | `compServer.CreateBlockInfo(levelId)` |  |
| <ApiFieldAnchor id="field-weather" />`weather` | 由运行时值确定 | `compServer.CreateWeather(levelId)` |  |
| <ApiFieldAnchor id="field-time" />`time` | 由运行时值确定 | `compServer.CreateTime(levelId)` |  |
| <ApiFieldAnchor id="field-block" />`block` | 由运行时值确定 | `compServer.CreateBlock(levelId)` |  |
| <ApiFieldAnchor id="field-blockEntity" />`blockEntity` | 由运行时值确定 | `compServer.CreateBlockEntity(levelId)` |  |
| <ApiFieldAnchor id="field-blockEntityData" />`blockEntityData` | 由运行时值确定 | `compServer.CreateBlockEntityData(levelId)` |  |
| <ApiFieldAnchor id="field-blockState" />`blockState` | 由运行时值确定 | `compServer.CreateBlockState(levelId)` |  |
| <ApiFieldAnchor id="field-blockUseEventWhiteList" />`blockUseEventWhiteList` | 由运行时值确定 | `compServer.CreateBlockUseEventWhiteList(levelId)` |  |
| <ApiFieldAnchor id="field-message" />`message` | 由运行时值确定 | `compServer.CreateMsg(levelId)` |  |
| <ApiFieldAnchor id="field-command" />`command` | 由运行时值确定 | `compServer.CreateCommand(levelId)` |  |
| <ApiFieldAnchor id="field-chestBlock" />`chestBlock` | 由运行时值确定 | `compServer.CreateChestBlock(levelId)` |  |
| <ApiFieldAnchor id="field-explosion" />`explosion` | 由运行时值确定 | `compServer.CreateExplosion(levelId)` |  |
| <ApiFieldAnchor id="field-extraData" />`extraData` | 由运行时值确定 | `compServer.CreateExtraData(levelId)` |  |
| <ApiFieldAnchor id="field-feature" />`feature` | 由运行时值确定 | `compServer.CreateFeature(levelId)` |  |
| <ApiFieldAnchor id="field-itemBanned" />`itemBanned` | 由运行时值确定 | `compServer.CreateItemBanned(levelId)` |  |
| <ApiFieldAnchor id="field-mobSpawn" />`mobSpawn` | 由运行时值确定 | `compServer.CreateMobSpawn(levelId)` |  |
| <ApiFieldAnchor id="field-projectile" />`projectile` | 由运行时值确定 | `compServer.CreateProjectile(levelId)` |  |
| <ApiFieldAnchor id="field-portal" />`portal` | 由运行时值确定 | `compServer.CreatePortal(levelId)` |  |
| <ApiFieldAnchor id="field-recipe" />`recipe` | 由运行时值确定 | `compServer.CreateRecipe(levelId)` |  |
| <ApiFieldAnchor id="field-redstone" />`redstone` | 由运行时值确定 | `compServer.CreateRedStone(levelId)` |  |

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