---
title: "ClientKVDatabase"
sidebar_label: "ClientKVDatabase"
---

import ApiFieldAnchor from '@docusaurus/Link';

# ClientKVDatabase

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/persistent/client.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[ClientSubsystem](ClientSubsystem.md), [DBSource](DBSource.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-conf" />`conf` | 由运行时值确定 | `level.configClient` |  |
| <ApiFieldAnchor id="field-data" />`data` | 由运行时值确定 | `self._read()` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [getData](#getData) | 方法 |
| [setData](#setData) | 方法 |
| [removeData](#removeData) | 方法 |
| [clearData](#clearData) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [broadcast](Subsystem.md#broadcast) | [Subsystem](Subsystem.md) |
| [canTick](Subsystem.md#field-canTick) | [Subsystem](Subsystem.md) |
| [createArrayView](DBSource.md#createArrayView) | [DBSource](DBSource.md) |
| [createEffectBind](ClientSubsystem.md#createEffectBind) | [ClientSubsystem](ClientSubsystem.md) |
| [createParticle](ClientSubsystem.md#createParticle) | [ClientSubsystem](ClientSubsystem.md) |
| [createSfx](ClientSubsystem.md#createSfx) | [ClientSubsystem](ClientSubsystem.md) |
| [createView](DBSource.md#createView) | [DBSource](DBSource.md) |
| [destroyEntity](ClientSubsystem.md#destroyEntity) | [ClientSubsystem](ClientSubsystem.md) |
| [destroySfx](ClientSubsystem.md#destroySfx) | [ClientSubsystem](ClientSubsystem.md) |
| [engine](Subsystem.md#field-engine) | [Subsystem](Subsystem.md) |
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
| [sendServer](ClientSubsystem.md#sendServer) | [ClientSubsystem](ClientSubsystem.md) |
| [spawnEntity](ClientSubsystem.md#spawnEntity) | [ClientSubsystem](ClientSubsystem.md) |
| [sysName](Subsystem.md#field-sysName) | [Subsystem](Subsystem.md) |
| [system](Subsystem.md#field-system) | [Subsystem](Subsystem.md) |
| [ticks](Subsystem.md#field-ticks) | [Subsystem](Subsystem.md) |
| [unlisten](Subsystem.md#unlisten) | [Subsystem](Subsystem.md) |

## 构造器 {#constructor}

```python
ClientKVDatabase(system, engine, sysName)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `system` | 由值/所属选项确定 | `必填` | 传给 [ClientKVDatabase.__init__](ClientKVDatabase.md#constructor) 的 system 参数；结合上方功能说明和下方调用示例使用。 |
| `engine` | 由值/所属选项确定 | `必填` | 传给 [ClientKVDatabase.__init__](ClientKVDatabase.md#constructor) 的 engine 参数；结合上方功能说明和下方调用示例使用。 |
| `sysName` | 由值/所属选项确定 | `必填` | 传给 [ClientKVDatabase.__init__](ClientKVDatabase.md#constructor) 的 sysName 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## getData {#getData}

```python
getData(key)
```

读取 `getData` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `key` | 由值/所属选项确定 | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getData(instance, key):
    return instance.getData(key)
```

## setData {#setData}

```python
setData(key, value)
```

设置 `setData` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `key` | 由值/所属选项确定 | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |
| `value` | 由值/所属选项确定 | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setData(instance, key, value):
    return instance.setData(key, value)
```

## removeData {#removeData}

```python
removeData(key)
```

移除或清理 `removeData` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `key` | 由值/所属选项确定 | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeData(instance, key):
    return instance.removeData(key)
```

## clearData {#clearData}

```python
clearData()
```

移除或清理 `clearData` 操作。参数形态和结果约定如下。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clearData(instance):
    return instance.clearData()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientKVDatabase 对象。
    print(value.conf)
    print(value.data)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)