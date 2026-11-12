---
title: "DatabaseView"
sidebar_label: "DatabaseView"
---

# DatabaseView

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/database_views.py`。

字典视图，保留其他视图实例已写入的修改。cache 是独立快照；为兼容原有行为，get 在键缺失或值为 [None](../../common/type-system.md#none) 时会保存默认值。读取嵌套值时返回副本。批量回调修改独立的工作字典，仅在成功后保存一次。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `cache` | 由运行时值确定 | `self._read()` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [get](#get) | 方法 |
| [set](#set) | 方法 |
| [has](#has) | 方法 |
| [batch](#batch) | 方法 |
| [__init__](#constructor) | 构造器 |

## get {#get}

```python
get(item, default = None)
```

读取 `get` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `item` | 由值/所属选项确定 | `必填` | 传给 [DatabaseView.get](DatabaseView.md#get) 的 item 参数；结合上方功能说明和下方调用示例使用。 |
| `default` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [DatabaseView.get](DatabaseView.md#get) 的 default 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_get(instance, item):
    return instance.get(item)
```

## set {#set}

```python
set(key, value)
```

设置 [set](../../common/type-system.md#set) 操作。参数形态和结果约定如下。

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
def call_set(instance, key, value):
    return instance.set(key, value)
```

## has {#has}

```python
has(item)
```

检查 `has` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `item` | 由值/所属选项确定 | `必填` | 传给 [DatabaseView.has](DatabaseView.md#has) 的 item 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_has(instance, item):
    return instance.has(item)
```

## batch {#batch}

```python
batch(updater)
```

执行 `batch` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `updater` | 由值/所属选项确定 | `必填` | 传给 [DatabaseView.batch](DatabaseView.md#batch) 的 updater 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'updater must be callable'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_batch(instance, updater):
    return instance.batch(updater)
```

## 构造器 {#constructor}

```python
DatabaseView(db, key)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `db` | 由值/所属选项确定 | `必填` | 传给 [DatabaseView.__init__](DatabaseView.md#constructor) 的 db 参数；结合上方功能说明和下方调用示例使用。 |
| `key` | 由值/所属选项确定 | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 DatabaseView 对象。
    print(value.cache)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)