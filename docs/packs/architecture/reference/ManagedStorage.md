---
title: "ManagedStorage"
sidebar_label: "ManagedStorage"
---

# ManagedStorage

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/storage.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [getData](#getData) | 方法 |
| [setData](#setData) | 方法 |
| [removeData](#removeData) | 方法 |
| [clearData](#clearData) | 方法 |

## getData {#getData}

```python
getData(key)
```

读取 `getData` 操作。原生实现使用 `GetExtraData`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `key` | 由值/所属选项确定 | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetExtraData`。

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

设置 `setData` 操作。原生实现使用 `SetExtraData`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `key` | 由值/所属选项确定 | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |
| `value` | 由值/所属选项确定 | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Could not write database key: %s' % key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetExtraData`。

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
clearData(keys = None)
```

清除本数据库写入的键；对于旧数据，需要显式传入键列表。保留未被跟踪的世界 ExtraData。原生写入不具备事务性；失败会报告错误，可重试清除。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `keys` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [ManagedStorage.clearData](ManagedStorage.md#clearData) 的 keys 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Could not remove database key: %s' % key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetExtraData`, `CleanExtraData`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clearData(instance):
    return instance.clearData()
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 ManagedStorage 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)