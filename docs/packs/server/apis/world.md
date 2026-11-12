---
title: "World"
sidebar_label: "World"
---

# World

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/World.py`；声明补充了静态类型信息。

## 获取方式

从服务端入口导入 `world` 单例。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [isValid](#isValid) | 只读属性 |
| [Destroy](#Destroy) | 方法 |
| [levelId](#levelId) | 只读属性 |
| [afterEvents](#afterEvents) | 只读属性 |
| [beforeEvents](#beforeEvents) | 只读属性 |
| [gameRules](#gameRules) | 只读属性 |
| [scoreboard](#scoreboard) | 只读属性 |
| [tickingAreaManager](#tickingAreaManager) | 只读属性 |
| [structureManager](#structureManager) | 只读属性 |
| [getStorage](#getStorage) | 方法 |
| [getAllPlayers](#getAllPlayers) | 静态/类方法 |
| [getPlayers](#getPlayers) | 静态/类方法 |
| [getDimension](#getDimension) | 静态/类方法 |
| [setDynamicProperty](#setDynamicProperty) | 静态/类方法 |
| [getDynamicProperty](#getDynamicProperty) | 静态/类方法 |
| [getDynamicPropertyIds](#getDynamicPropertyIds) | 静态/类方法 |
| [getDynamicPropertyTotalByteCount](#getDynamicPropertyTotalByteCount) | 静态/类方法 |
| [getEntity](#getEntity) | 方法 |
| [getTimeOfDay](#getTimeOfDay) | 静态/类方法 |
| [getAbsoluteTime](#getAbsoluteTime) | 静态/类方法 |
| [getDay](#getDay) | 静态/类方法 |
| [getMoonPhase](#getMoonPhase) | 静态/类方法 |
| [seed](#seed) | 只读属性 |
| [getDefaultSpawnLocation](#getDefaultSpawnLocation) | 静态/类方法 |
| [setDefaultSpawnLocation](#setDefaultSpawnLocation) | 静态/类方法 |
| [getDifficulty](#getDifficulty) | 静态/类方法 |
| [setDifficulty](#setDifficulty) | 静态/类方法 |
| [setDynamicProperties](#setDynamicProperties) | 静态/类方法 |
| [setTimeOfDay](#setTimeOfDay) | 静态/类方法 |
| [setAbsoluteTime](#setAbsoluteTime) | 静态/类方法 |
| [sendMessage](#sendMessage) | 方法 |
| [getLootTableManager](#getLootTableManager) | 静态/类方法 |

## 构造器 {#constructor}

```python
World(namespace, systemName)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `namespace` | 由值/所属选项确定 | `必填` | 本功能独有的命名空间，避免与其他功能的持久化数据冲突。 |
| `systemName` | 由值/所属选项确定 | `必填` | 传给 [World.__init__](world.md#constructor) 的 systemName 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## isValid {#isValid}

```python
isValid: bool
```

此世界入口是否仍持有有效的开发包会话。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## Destroy {#Destroy}

```python
Destroy() -> None
```

释放世界事件订阅，包括尚待分发的回调。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_Destroy(instance):
    return instance.Destroy()
```

## levelId {#levelId}

```python
levelId: str
```

当前世界的运行标识。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.levelId
```

## afterEvents {#afterEvents}

```python
afterEvents: WorldAfterEvents
```

世界范围的后置事件集合。原生事件按开发包实际分发时机执行；不能据此假定具有微软接口的延后执行阶段。

**访问：** 只读。

**返回类型：** [WorldAfterEvents](../events/afterEvents.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.afterEvents
```

## beforeEvents {#beforeEvents}

```python
beforeEvents: WorldBeforeEvents
```

世界范围的前置事件集合。原生回调同步执行，仅允许按具体事件契约修改输出；执行限制以当前适配器为准。

**访问：** 只读。

**返回类型：** [WorldBeforeEvents](../events/beforeEvents.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.beforeEvents
```

## gameRules {#gameRules}

```python
gameRules: GameRules
```

应用于此世界的游戏规则。

**访问：** 只读。

**返回类型：** [GameRules](../../common/reference/GameRules.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.gameRules
```

## scoreboard {#scoreboard}

```python
scoreboard: Scoreboard
```

读取 `scoreboard` 的当前值。

**访问：** 只读。

**返回类型：** [Scoreboard](../reference/Scoreboard.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.scoreboard
```

## tickingAreaManager {#tickingAreaManager}

```python
tickingAreaManager: TickingAreaManager
```

管理本模组创建的常加载区域，支持添加、移除和查询。

**访问：** 只读。

**返回类型：** [TickingAreaManager](../reference/TickingAreaManager.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.tickingAreaManager
```

## structureManager {#structureManager}

```python
structureManager: StructureManager
```

返回 [Structure](../reference/Structure.md) 相关操作的管理器。

**访问：** 只读。

**返回类型：** [StructureManager](../reference/StructureManager.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.structureManager
```

## getStorage {#getStorage}

```python
getStorage(namespace: str) -> KeyValueStorage
```

返回按命名空间隔离的持久化 JSON 存储，属于网易扩展。命名空间应标识所属模组；数据存于保留的世界 ExtraData 键，每次成功写入均保存。数据不合法时抛出 [TypeError](../../common/type-system.md#typeerror) 或 [ValueError](../../common/type-system.md#valueerror)，原生失败时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)。与客户端存储不共享数据。

:::note 当前实现说明
网易扩展。与客户端存储不共享；每个命名空间为独立 JSON 文档。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `namespace` | [str](../../common/type-system.md#str) | `必填` | 本功能独有的命名空间，避免与其他功能的持久化数据冲突。 |

**返回类型：** [KeyValueStorage](../../common/reference/KeyValueStorage.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetExtraData`, `SetExtraData`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getStorage(instance, namespace):
    return instance.getStorage(namespace)
```

## getAllPlayers {#getAllPlayers}

```python
getAllPlayers() -> list[Player]
```

返回世界中全部活跃玩家的列表。

**返回类型：** [list](../../common/type-system.md#list)[[Player](player.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerList`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getAllPlayers(type_object):
    return type_object.getAllPlayers()
```

## getPlayers {#getPlayers}

```python
getPlayers(options: EntityQueryOptions | dict = None) -> list[Player]
```

根据 [EntityQueryOptions](../../common/reference/EntityQueryOptions.md) 中的条件筛选玩家。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [EntityQueryOptions](../../common/reference/EntityQueryOptions.md) \| [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [list](../../common/type-system.md#list)[[Player](player.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getPlayers(type_object):
    return type_object.getPlayers()
```

## getDimension {#getDimension}

```python
getDimension(dimensionId: str) -> Dimension
```

返回维度对象。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `dimensionId` | [str](../../common/type-system.md#str) | `必填` | 传给 [World.getDimension](world.md#getDimension) 的 dimensionId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Dimension](dimension.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDimension(type_object, dimensionId):
    return type_object.getDimension(dimensionId)
```

## setDynamicProperty {#setDynamicProperty}

```python
setDynamicProperty(identifier: str, value: typing.Any = None) -> None
```

设置世界动态属性，或以 [None](../../common/type-system.md#none) 删除它；写入前复制值，每次统一保存一次。原生写入或保存失败时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)；引擎不保证回滚此前已经发生的修改。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `value` | [typing.Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SaveExtraData`, `CleanExtraData`, `SetExtraData`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setDynamicProperty(type_object, identifier):
    return type_object.setDynamicProperty(identifier)
```

## getDynamicProperty {#getDynamicProperty}

```python
getDynamicProperty(identifier: str) -> typing.Any
```

读取属性值。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |

**返回类型：** [typing.Any](../../common/type-system.md#any)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLevelId`, `GetExtraData`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDynamicProperty(type_object, identifier):
    return type_object.getDynamicProperty(identifier)
```

## getDynamicPropertyIds {#getDynamicPropertyIds}

```python
getDynamicPropertyIds() -> list[str]
```

读取此世界已设置的动态属性标识集合。

**返回类型：** [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetWholeExtraData`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDynamicPropertyIds(type_object):
    return type_object.getDynamicPropertyIds()
```

## getDynamicPropertyTotalByteCount {#getDynamicPropertyTotalByteCount}

```python
getDynamicPropertyTotalByteCount() -> int
```

读取动态属性的总字节数，可用于监测存储量，避免动态属性数据过大。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetWholeExtraData`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDynamicPropertyTotalByteCount(type_object):
    return type_object.getDynamicPropertyTotalByteCount()
```

## getEntity {#getEntity}

```python
getEntity(id) -> Entity | None
```

按给定运行标识获取实体。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `id` | 由值/所属选项确定 | `必填` | 运行标识或类型标识，按本成员的说明传入。 |

**返回类型：** [Entity](entity.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEntity(instance, id):
    return instance.getEntity(id)
```

## getTimeOfDay {#getTimeOfDay}

```python
getTimeOfDay() -> int
```

返回一天中的时间，单位为刻，范围为 0–24000。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getTimeOfDay(type_object):
    return type_object.getTimeOfDay()
```

## getAbsoluteTime {#getAbsoluteTime}

```python
getAbsoluteTime() -> int
```

返回世界启动以来的绝对时间。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetTime'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetTime`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getAbsoluteTime(type_object):
    return type_object.getAbsoluteTime()
```

## getDay {#getDay}

```python
getDay() -> int
```

读取 `getDay` 操作。参数形态和结果约定如下。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDay(type_object):
    return type_object.getDay()
```

## getMoonPhase {#getMoonPhase}

```python
getMoonPhase() -> int
```

读取 `getMoonPhase` 操作。参数形态和结果约定如下。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getMoonPhase(type_object):
    return type_object.getMoonPhase()
```

## seed {#seed}

```python
seed: str
```

读取 `seed` 的当前值。底层调用 `GetSeed`, `GetLevelId`。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetSeed`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.seed
```

## getDefaultSpawnLocation {#getDefaultSpawnLocation}

```python
getDefaultSpawnLocation() -> Vector3
```

读取 `getDefaultSpawnLocation` 操作。原生实现使用 `GetSpawnPosition`, `GetLevelId`，行为受网易运行环境约束。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetSpawnPosition`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDefaultSpawnLocation(type_object):
    return type_object.getDefaultSpawnLocation()
```

## setDefaultSpawnLocation {#setDefaultSpawnLocation}

```python
setDefaultSpawnLocation(spawnLocation: Vector3 | tuple | dict) -> None
```

设置 `setDefaultSpawnLocation` 操作。原生实现使用 `SetCommand`, `GetLevelId`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `spawnLocation` | [Vector3](../extra/vector.md) \| [tuple](../../common/type-system.md#tuple) \| [dict](../../common/type-system.md#dict) | `必填` | 传给 [World.setDefaultSpawnLocation](world.md#setDefaultSpawnLocation) 的 spawnLocation 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to set default spawn location'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetCommand`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setDefaultSpawnLocation(type_object, spawnLocation):
    return type_object.setDefaultSpawnLocation(spawnLocation)
```

## getDifficulty {#getDifficulty}

```python
getDifficulty() -> str
```

读取 `getDifficulty` 操作。原生实现使用 `GetGameDiffculty`, `GetLevelId`，行为受网易运行环境约束。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to read world difficulty'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameDiffculty`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDifficulty(type_object):
    return type_object.getDifficulty()
```

## setDifficulty {#setDifficulty}

```python
setDifficulty(difficulty: str) -> None
```

设置 `setDifficulty` 操作。原生实现使用 `SetGameDifficulty`, `GetLevelId`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `difficulty` | [str](../../common/type-system.md#str) | `必填` | 传给 [World.setDifficulty](world.md#setDifficulty) 的 difficulty 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown difficulty: %r' % difficulty` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to set world difficulty'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetGameDifficulty`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setDifficulty(type_object, difficulty):
    return type_object.setDifficulty(difficulty)
```

## setDynamicProperties {#setDynamicProperties}

```python
setDynamicProperties(properties: dict) -> None
```

预先校验所有标识并复制值，再批量修改，最后统一保存一次。[None](../../common/type-system.md#none) 表示删除，空字典不调用引擎。原生写入或保存失败时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)；引擎不保证回滚此前已经发生的修改。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `properties` | [dict](../../common/type-system.md#dict) | `必填` | 传给 [World.setDynamicProperties](world.md#setDynamicProperties) 的 properties 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SaveExtraData`, `CleanExtraData`, `SetExtraData`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setDynamicProperties(type_object, properties):
    return type_object.setDynamicProperties(properties)
```

## setTimeOfDay {#setTimeOfDay}

```python
setTimeOfDay(timeOfDay: int)
```

以整数刻设置一天内的时间，范围为 0～24000。网易原生接口在目标时间早于当前时间时前进到次日；原生拒绝时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `timeOfDay` | [int](../../common/type-system.md#int) | `必填` | 传给 [World.setTimeOfDay](world.md#setTimeOfDay) 的 timeOfDay 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'timeOfDay must be between 0 and 24000'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetTimeOfDay`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setTimeOfDay(type_object, timeOfDay):
    return type_object.setTimeOfDay(timeOfDay)
```

## setAbsoluteTime {#setAbsoluteTime}

```python
setAbsoluteTime(absoluteTime: int)
```

以整数刻设置世界绝对时间；原生拒绝或调用失败时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `absoluteTime` | [int](../../common/type-system.md#int) | `必填` | 传给 [World.setAbsoluteTime](world.md#setAbsoluteTime) 的 absoluteTime 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetTime`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setAbsoluteTime(type_object, absoluteTime):
    return type_object.setAbsoluteTime(absoluteTime)
```

## sendMessage {#sendMessage}

```python
sendMessage(message: str)
```

向全部玩家发送消息。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `message` | [str](../../common/type-system.md#str) | `必填` | 传给 [World.sendMessage](world.md#sendMessage) 的 message 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_sendMessage(instance, message):
    return instance.sendMessage(message)
```

## getLootTableManager {#getLootTableManager}

```python
getLootTableManager()
```

当前没有功能性实现，不应依赖此成员完成操作。

:::note 当前实现说明
当前为空返回，不能作为已实现的战利品 API 使用。
:::

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
from ModSAPI.server.beta import world

for player in world.getAllPlayers():
    player.sendMessage("Hello")
print(world.getDimension("overworld").id)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)