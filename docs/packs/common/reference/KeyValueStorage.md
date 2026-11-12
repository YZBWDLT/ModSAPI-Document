---
title: "KeyValueStorage"
sidebar_label: "KeyValueStorage"
---

# KeyValueStorage

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/storage.py`；声明补充了静态类型信息。

通过 [client.getStorage](../../client/apis/manager.md#getStorage) 或 [world.getStorage](../../server/apis/world.md#getStorage) 获取的网易扩展。每个命名空间保存一个文档，最多为 1 MiB 的 UTF-8 JSON，嵌套深度最多 32 层。读写均使用副本。[None](../type-system.md#none) 表示存储的空值；删除键须调用 delete()。操作同步执行，不提供跨线程、进程或命名空间的事务。

## 获取方式

使用 `world.getStorage(namespace)` 或 `client.getStorage(namespace, options)`。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [namespace](#namespace) | 只读属性 |
| [get](#get) | 方法 |
| [has](#has) | 方法 |
| [getKeys](#getKeys) | 方法 |
| [set](#set) | 方法 |
| [setMany](#setMany) | 方法 |
| [delete](#delete) | 方法 |
| [clear](#clear) | 方法 |

## 构造器 {#constructor}

```python
KeyValueStorage(namespace, read, write, guard = None)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `namespace` | 由值/所属选项确定 | `必填` | 本功能独有的命名空间，避免与其他功能的持久化数据冲突。 |
| `read` | 由值/所属选项确定 | `必填` | 传给 [KeyValueStorage.__init__](KeyValueStorage.md#constructor) 的 read 参数；结合上方功能说明和下方调用示例使用。 |
| `write` | 由值/所属选项确定 | `必填` | 传给 [KeyValueStorage.__init__](KeyValueStorage.md#constructor) 的 write 参数；结合上方功能说明和下方调用示例使用。 |
| `guard` | 由值/所属选项确定 | [None](../type-system.md#none) | 传给 [KeyValueStorage.__init__](KeyValueStorage.md#constructor) 的 guard 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## namespace {#namespace}

```python
namespace: str
```

调用者提供的命名空间，与文档内部的各个键无关。

**访问：** 只读。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.namespace
```

## get {#get}

```python
get(key: str, defaultValue: Any = None) -> Any
```

返回值的独立副本；键缺失时返回 defaultValue 的副本。

:::note 当前实现说明
返回副本；[None](../type-system.md#none) 是合法存储值，缺失键才使用 defaultValue。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `key` | [str](../type-system.md#str) | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |
| `defaultValue` | [Any](../type-system.md#any) | [None](../type-system.md#none) | 缺省值；具体是缺失键、初始控件值还是原生默认值取决于所属接口。 |

**返回类型：** [Any](../type-system.md#any)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_get(instance, key):
    return instance.get(key)
```

## has {#has}

```python
has(key: str) -> bool
```

检查键是否存在；值为 [None](../type-system.md#none) 的已存储键仍视为存在。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `key` | [str](../type-system.md#str) | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_has(instance, key):
    return instance.has(key)
```

## getKeys {#getKeys}

```python
getKeys() -> list[str]
```

返回键名快照，不保证顺序。

**返回类型：** [list](../type-system.md#list)[[str](../type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getKeys(instance):
    return instance.getKeys()
```

## set {#set}

```python
set(key: str, value: Any) -> None
```

校验并保存副本；原生失败时抛出 [NativeOperationError](NativeOperationError.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `key` | [str](../type-system.md#str) | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |
| `value` | [Any](../type-system.md#any) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_set(instance, key, value):
    return instance.set(key, value)
```

## setMany {#setMany}

```python
setMany(values: dict[str, Any]) -> None
```

先校验全部批量数据，再合并并执行一次原生写入。

:::note 当前实现说明
校验整批数据后合并并发出一次写入；不提供跨进程事务或锁。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `values` | [dict](../type-system.md#dict)[[str](../type-system.md#str), [Any](../type-system.md#any)] | `必填` | 传给 [KeyValueStorage.setMany](KeyValueStorage.md#setMany) 的 values 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../type-system.md#typeerror) | `'values must be a dictionary'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setMany(instance, values):
    return instance.setMany(values)
```

## delete {#delete}

```python
delete(key: str) -> bool
```

删除键；不存在时返回 False，成功保存修改后返回 True。

:::note 当前实现说明
成功删除返回 True，键不存在返回 False。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `key` | [str](../type-system.md#str) | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_delete(instance, key):
    return instance.delete(key)
```

## clear {#clear}

```python
clear() -> None
```

显式将当前命名空间替换为空文档。

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clear(instance):
    return instance.clear()
```

## 使用示例


```python
from ModSAPI.server.beta import world

store = world.getStorage("example:data")
store.setMany({"version": 1, "visits": 0})
store.set("visits", store.get("visits", 0) + 1)
print(store.getKeys())
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)