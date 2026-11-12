---
title: "QueryClient"
sidebar_label: "QueryClient"
---

# QueryClient

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/query/queryClient.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [cache](#cache) | 静态/类方法 |
| [queryOfKey](#queryOfKey) | 静态/类方法 |
| [queryOfEntity](#queryOfEntity) | 静态/类方法 |
| [pos](#pos) | 静态/类方法 |
| [type](#type) | 静态/类方法 |
| [rot](#rot) | 静态/类方法 |
| [action](#action) | 静态/类方法 |
| [motion](#motion) | 静态/类方法 |

## cache {#cache}

```python
cache(key: str, id: int, getter: object) -> QueryCache
```

执行 `cache` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `key` | [str](../../common/type-system.md#str) | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |
| `id` | [int](../../common/type-system.md#int) | `必填` | 运行标识或类型标识，按本成员的说明传入。 |
| `getter` | [object](../../common/type-system.md#object) | `必填` | 传给 [QueryClient.cache](QueryClient.md#cache) 的 getter 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [QueryCache](QueryCache.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_cache(type_object, key, id, getter):
    return type_object.cache(key, id, getter)
```

## queryOfKey {#queryOfKey}

```python
queryOfKey(key: str, entityFilter: object = None) -> dict[str, QueryCache]
```

执行 `queryOfKey` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `key` | [str](../../common/type-system.md#str) | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |
| `entityFilter` | [object](../../common/type-system.md#object) | [None](../../common/type-system.md#none) | 传给 [QueryClient.queryOfKey](QueryClient.md#queryOfKey) 的 entityFilter 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [QueryCache](QueryCache.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_queryOfKey(type_object, key):
    return type_object.queryOfKey(key)
```

## queryOfEntity {#queryOfEntity}

```python
queryOfEntity(entityId: int, keyFilter: object = None) -> dict[str, QueryCache]
```

执行 `queryOfEntity` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `entityId` | [int](../../common/type-system.md#int) | `必填` | 实体运行 ID；跨回调使用前重新确认实体有效性。 |
| `keyFilter` | [object](../../common/type-system.md#object) | [None](../../common/type-system.md#none) | 传给 [QueryClient.queryOfEntity](QueryClient.md#queryOfEntity) 的 keyFilter 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [QueryCache](QueryCache.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_queryOfEntity(type_object, entityId):
    return type_object.queryOfEntity(entityId)
```

## pos {#pos}

```python
pos(id)
```

执行 `pos` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `id` | 由值/所属选项确定 | `必填` | 运行标识或类型标识，按本成员的说明传入。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_pos(type_object, id):
    return type_object.pos(id)
```

## type {#type}

```python
type(id)
```

执行 [type](../../common/type-system.md#type) 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `id` | 由值/所属选项确定 | `必填` | 运行标识或类型标识，按本成员的说明传入。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_type(type_object, id):
    return type_object.type(id)
```

## rot {#rot}

```python
rot(id)
```

执行 `rot` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `id` | 由值/所属选项确定 | `必填` | 运行标识或类型标识，按本成员的说明传入。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_rot(type_object, id):
    return type_object.rot(id)
```

## action {#action}

```python
action(id)
```

执行 `action` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `id` | 由值/所属选项确定 | `必填` | 运行标识或类型标识，按本成员的说明传入。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_action(type_object, id):
    return type_object.action(id)
```

## motion {#motion}

```python
motion(id)
```

执行 `motion` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `id` | 由值/所属选项确定 | `必填` | 运行标识或类型标识，按本成员的说明传入。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_motion(type_object, id):
    return type_object.motion(id)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 QueryClient 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)