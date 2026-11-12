---
title: "ServerSubsystem"
sidebar_label: "ServerSubsystem"
---

# ServerSubsystem

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/subsystem.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[Subsystem](Subsystem.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [sendAllClients](#sendAllClients) | 方法 |
| [sendClient](#sendClient) | 方法 |
| [spawnEntity](#spawnEntity) | 方法 |
| [destroyEntity](#destroyEntity) | 方法 |
| [spawnItem](#spawnItem) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [broadcast](Subsystem.md#broadcast) | [Subsystem](Subsystem.md) |
| [canTick](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [engine](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [getEngine](Subsystem.md#getEngine) | [Subsystem](Subsystem.md) |
| [getInstance](Subsystem.md#getInstance) | [Subsystem](Subsystem.md) |
| [getSysName](Subsystem.md#getSysName) | [Subsystem](Subsystem.md) |
| [getSystem](Subsystem.md#getSystem) | [Subsystem](Subsystem.md) |
| [listen](Subsystem.md#listen) | [Subsystem](Subsystem.md) |
| [off](Subsystem.md#off) | [Subsystem](Subsystem.md) |
| [on](Subsystem.md#on) | [Subsystem](Subsystem.md) |
| [onDestroy](Subsystem.md#onDestroy) | [Subsystem](Subsystem.md) |
| [onInit](Subsystem.md#onInit) | [Subsystem](Subsystem.md) |
| [onReady](Subsystem.md#onReady) | [Subsystem](Subsystem.md) |
| [onUpdate](Subsystem.md#onUpdate) | [Subsystem](Subsystem.md) |
| [sysName](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [system](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [ticks](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [unlisten](Subsystem.md#unlisten) | [Subsystem](Subsystem.md) |

## 构造器 {#constructor}

```python
ServerSubsystem(system: object, engine: str, sysName: str) -> 'None'
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `system` | [object](../../common/type-system.md#object) | `必填` | 传给 [ServerSubsystem.__init__](ServerSubsystem.md#constructor) 的 system 参数；结合上方功能说明和下方调用示例使用。 |
| `engine` | [str](../../common/type-system.md#str) | `必填` | 传给 [ServerSubsystem.__init__](ServerSubsystem.md#constructor) 的 engine 参数；结合上方功能说明和下方调用示例使用。 |
| `sysName` | [str](../../common/type-system.md#str) | `必填` | 传给 [ServerSubsystem.__init__](ServerSubsystem.md#constructor) 的 sysName 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## sendAllClients {#sendAllClients}

```python
sendAllClients(eventName, eventData)
```

执行 `sendAllClients` 操作。原生实现使用 `BroadcastToAllClient`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `eventName` | 由值/所属选项确定 | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |
| `eventData` | 由值/所属选项确定 | `必填` | 传给 [ServerSubsystem.sendAllClients](ServerSubsystem.md#sendAllClients) 的 eventData 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `BroadcastToAllClient`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_sendAllClients(instance, eventName, eventData):
    return instance.sendAllClients(eventName, eventData)
```

## sendClient {#sendClient}

```python
sendClient(targetIds, eventName, eventData)
```

执行 `sendClient` 操作。原生实现使用 `NotifyToMultiClients`, `NotifyToClient`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `targetIds` | 由值/所属选项确定 | `必填` | 传给 [ServerSubsystem.sendClient](ServerSubsystem.md#sendClient) 的 targetIds 参数；结合上方功能说明和下方调用示例使用。 |
| `eventName` | 由值/所属选项确定 | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |
| `eventData` | 由值/所属选项确定 | `必填` | 传给 [ServerSubsystem.sendClient](ServerSubsystem.md#sendClient) 的 eventData 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `NotifyToMultiClients`, `NotifyToClient`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_sendClient(instance, targetIds, eventName, eventData):
    return instance.sendClient(targetIds, eventName, eventData)
```

## spawnEntity {#spawnEntity}

```python
spawnEntity(template, location, rot, isNpc = False, isGlobal = False)
```

创建或登记 `spawnEntity` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `template` | 由值/所属选项确定 | `必填` | 传给 [ServerSubsystem.spawnEntity](ServerSubsystem.md#spawnEntity) 的 template 参数；结合上方功能说明和下方调用示例使用。 |
| `location` | 由值/所属选项确定 | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `rot` | 由值/所属选项确定 | `必填` | 传给 [ServerSubsystem.spawnEntity](ServerSubsystem.md#spawnEntity) 的 rot 参数；结合上方功能说明和下方调用示例使用。 |
| `isNpc` | 由值/所属选项确定 | `False` | 传给 [ServerSubsystem.spawnEntity](ServerSubsystem.md#spawnEntity) 的 isNpc 参数；结合上方功能说明和下方调用示例使用。 |
| `isGlobal` | 由值/所属选项确定 | `False` | 传给 [ServerSubsystem.spawnEntity](ServerSubsystem.md#spawnEntity) 的 isGlobal 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_spawnEntity(instance, template, location, rot):
    return instance.spawnEntity(template, location, rot)
```

## destroyEntity {#destroyEntity}

```python
destroyEntity(entityId)
```

执行 `destroyEntity` 操作。原生实现使用 `DestroyEntity`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` | 实体运行 ID；跨回调使用前重新确认实体有效性。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `DestroyEntity`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_destroyEntity(instance, entityId):
    return instance.destroyEntity(entityId)
```

## spawnItem {#spawnItem}

```python
spawnItem(itemDict, location)
```

创建或登记 `spawnItem` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemDict` | 由值/所属选项确定 | `必填` | 传给 [ServerSubsystem.spawnItem](ServerSubsystem.md#spawnItem) 的 itemDict 参数；结合上方功能说明和下方调用示例使用。 |
| `location` | 由值/所属选项确定 | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_spawnItem(instance, itemDict, location):
    return instance.spawnItem(itemDict, location)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 ServerSubsystem 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)