---
title: "LevelClient"
sidebar_label: "LevelClient"
---

# LevelClient

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/level/client.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `levelId` | 由运行时值确定 | `levelId` |
| `localPlayerId` | 由运行时值确定 | `localPlayerId` |
| `localPlayer` | 由运行时值确定 | `compClient.CreatePlayer(localPlayerId)` |
| `achievement` | 由运行时值确定 | `compClient.CreateAchievement(levelId)` |
| `actorRender` | 由运行时值确定 | `compClient.CreateActorRender(levelId)` |
| `biome` | 由运行时值确定 | `compClient.CreateBiome(levelId)` |
| `block` | 由运行时值确定 | `compClient.CreateBlock(levelId)` |
| `blockGeometry` | 由运行时值确定 | `compClient.CreateBlockGeometry(levelId)` |
| `blockInfo` | 由运行时值确定 | `compClient.CreateBlockInfo(levelId)` |
| `blockUseEventWhiteList` | 由运行时值确定 | `compClient.CreateBlockUseEventWhiteList(levelId)` |
| `camera` | 由运行时值确定 | `compClient.CreateCamera(levelId)` |
| `chunkSource` | 由运行时值确定 | `compClient.CreateChunkSource(levelId)` |
| `configClient` | 由运行时值确定 | `compClient.CreateConfigClient(levelId)` |
| `customAudio` | 由运行时值确定 | `compClient.CreateCustomAudio(levelId)` |
| `dimension` | 由运行时值确定 | `compClient.CreateDimension(levelId)` |
| `drawing` | 由运行时值确定 | `compClient.CreateDrawing(levelId)` |
| `fog` | 由运行时值确定 | `compClient.CreateFog(levelId)` |
| `game` | 由运行时值确定 | `compClient.CreateGame(levelId)` |
| `model` | 由运行时值确定 | `compClient.CreateModel(levelId)` |
| `neteaseShop` | 由运行时值确定 | `compClient.CreateNeteaseShop(levelId)` |
| `operation` | 由运行时值确定 | `compClient.CreateOperation(levelId)` |
| `playerView` | 由运行时值确定 | `compClient.CreatePlayerView(localPlayerId)` |
| `postProcess` | 由运行时值确定 | `compClient.CreatePostProcess(levelId)` |
| `recipe` | 由运行时值确定 | `compClient.CreateRecipe(levelId)` |
| `skyRender` | 由运行时值确定 | `compClient.CreateSkyRender(levelId)` |
| `textBoard` | 由运行时值确定 | `compClient.CreateTextBoard(levelId)` |
| `textNotify` | 由运行时值确定 | `compClient.CreateTextNotifyClient(levelId)` |
| `virtualWorld` | 由运行时值确定 | `compClient.CreateVirtualWorld(levelId)` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [getInst](#getInst) | 静态/类方法 |

## 构造器 {#constructor}

```python
LevelClient()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLevelId`, `GetLocalPlayerId`。

## getInst {#getInst}

```python
getInst()
```

读取 `getInst` 操作。参数形态和结果约定如下。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getInst(type_object):
    return type_object.getInst()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 LevelClient 对象。
    print(value.levelId)
    print(value.localPlayerId)
    print(value.localPlayer)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)