---
title: "ServerKVDatabase"
sidebar_label: "ServerKVDatabase"
---

# ServerKVDatabase

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/easyDatabase.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[ManagedStorage](ManagedStorage.md), [ServerSubsystem](ServerSubsystem.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `data` | 由运行时值确定 | [LevelServer.extraData](LevelServer.md#字段与常量) |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [createView](#createView) | 方法 |
| [createArrayView](#createArrayView) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [broadcast](Subsystem.md#broadcast) | [Subsystem](Subsystem.md) |
| [canTick](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [clearData](ManagedStorage.md#clearData) | [ManagedStorage](ManagedStorage.md) |
| [destroyEntity](ServerSubsystem.md#destroyEntity) | [ServerSubsystem](ServerSubsystem.md) |
| [engine](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [getData](ManagedStorage.md#getData) | [ManagedStorage](ManagedStorage.md) |
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
| [removeData](ManagedStorage.md#removeData) | [ManagedStorage](ManagedStorage.md) |
| [sendAllClients](ServerSubsystem.md#sendAllClients) | [ServerSubsystem](ServerSubsystem.md) |
| [sendClient](ServerSubsystem.md#sendClient) | [ServerSubsystem](ServerSubsystem.md) |
| [setData](ManagedStorage.md#setData) | [ManagedStorage](ManagedStorage.md) |
| [spawnEntity](ServerSubsystem.md#spawnEntity) | [ServerSubsystem](ServerSubsystem.md) |
| [spawnItem](ServerSubsystem.md#spawnItem) | [ServerSubsystem](ServerSubsystem.md) |
| [sysName](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [system](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [ticks](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [unlisten](Subsystem.md#unlisten) | [Subsystem](Subsystem.md) |

## createView {#createView}

```python
createView(key)
```

创建或登记 `createView` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `key` | 由值/所属选项确定 | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createView(instance, key):
    return instance.createView(key)
```

## createArrayView {#createArrayView}

```python
createArrayView(key)
```

创建或登记 `createArrayView` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `key` | 由值/所属选项确定 | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createArrayView(instance, key):
    return instance.createArrayView(key)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ServerKVDatabase 对象。
    print(value.data)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)