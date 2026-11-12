---
title: "BlockVolumeBase"
sidebar_label: "BlockVolumeBase"
---

# BlockVolumeBase

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Block.py`；声明补充了静态类型信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [getBlockLocationIterator](#getBlockLocationIterator) | 方法 |
| [getMin](#getMin) | 方法 |
| [getMax](#getMax) | 方法 |
| [getSpan](#getSpan) | 方法 |
| [getCapacity](#getCapacity) | 方法 |
| [isInside](#isInside) | 方法 |
| [translate](#translate) | 方法 |
| [getClosest](#getClosest) | 方法 |
| [getFarthest](#getFarthest) | 方法 |

## 构造器 {#constructor}

```python
BlockVolumeBase(data: dict[str, Vector3]) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Vector3](../extra/vector.md)] | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## getBlockLocationIterator {#getBlockLocationIterator}

```python
getBlockLocationIterator()
```

返回遍历此区域全部世界方块位置的 BlockLocationIterator。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getBlockLocationIterator(instance):
    return instance.getBlockLocationIterator()
```

## getMin {#getMin}

```python
getMin() -> Vector3
```

读取 `getMin` 操作。参数形态和结果约定如下。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getMin(instance):
    return instance.getMin()
```

## getMax {#getMax}

```python
getMax() -> Vector3
```

读取 `getMax` 操作。参数形态和结果约定如下。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getMax(instance):
    return instance.getMax()
```

## getSpan {#getSpan}

```python
getSpan() -> Vector3
```

读取 `getSpan` 操作。参数形态和结果约定如下。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getSpan(instance):
    return instance.getSpan()
```

## getCapacity {#getCapacity}

```python
getCapacity() -> int
```

读取 `getCapacity` 操作。参数形态和结果约定如下。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getCapacity(instance):
    return instance.getCapacity()
```

## isInside {#isInside}

```python
isInside(location: Vector3 | tuple | dict) -> bool
```

检查 `isInside` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../extra/vector.md) \| [tuple](../../common/type-system.md#tuple) \| [dict](../../common/type-system.md#dict) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_isInside(instance, location):
    return instance.isInside(location)
```

## translate {#translate}

```python
translate(delta: Vector3 | tuple | dict) -> None
```

执行 `translate` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `delta` | [Vector3](../extra/vector.md) \| [tuple](../../common/type-system.md#tuple) \| [dict](../../common/type-system.md#dict) | `必填` | 传给 [BlockVolumeBase.translate](BlockVolumeBase.md#translate) 的 delta 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_translate(instance, delta):
    return instance.translate(delta)
```

## getClosest {#getClosest}

```python
getClosest(count: int, location: Vector3 | tuple | dict) -> list[Vector3]
```

读取 `getClosest` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `count` | [int](../../common/type-system.md#int) | `必填` | 传给 [BlockVolumeBase.getClosest](BlockVolumeBase.md#getClosest) 的 count 参数；结合上方功能说明和下方调用示例使用。 |
| `location` | [Vector3](../extra/vector.md) \| [tuple](../../common/type-system.md#tuple) \| [dict](../../common/type-system.md#dict) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |

**返回类型：** [list](../../common/type-system.md#list)[[Vector3](../extra/vector.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getClosest(instance, count, location):
    return instance.getClosest(count, location)
```

## getFarthest {#getFarthest}

```python
getFarthest(count: int, location: Vector3 | tuple | dict) -> list[Vector3]
```

读取 `getFarthest` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `count` | [int](../../common/type-system.md#int) | `必填` | 传给 [BlockVolumeBase.getFarthest](BlockVolumeBase.md#getFarthest) 的 count 参数；结合上方功能说明和下方调用示例使用。 |
| `location` | [Vector3](../extra/vector.md) \| [tuple](../../common/type-system.md#tuple) \| [dict](../../common/type-system.md#dict) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |

**返回类型：** [list](../../common/type-system.md#list)[[Vector3](../extra/vector.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getFarthest(instance, count, location):
    return instance.getFarthest(count, location)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 BlockVolumeBase 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)