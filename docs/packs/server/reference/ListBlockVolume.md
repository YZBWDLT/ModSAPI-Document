---
title: "ListBlockVolume"
sidebar_label: "ListBlockVolume"
---

# ListBlockVolume

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Block.py`；声明补充了静态类型信息。

独立方块位置的集合，按确定的插入顺序保存。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[BlockVolumeBase](BlockVolumeBase.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [add](#add) | 方法 |
| [remove](#remove) | 方法 |
| [getBlockLocationIterator](#getBlockLocationIterator) | 方法 |
| [getCapacity](#getCapacity) | 方法 |
| [getMin](#getMin) | 方法 |
| [getMax](#getMax) | 方法 |
| [isInside](#isInside) | 方法 |
| [translate](#translate) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [getClosest](BlockVolumeBase.md#getClosest) | [BlockVolumeBase](BlockVolumeBase.md) |
| [getFarthest](BlockVolumeBase.md#getFarthest) | [BlockVolumeBase](BlockVolumeBase.md) |
| [getSpan](BlockVolumeBase.md#getSpan) | [BlockVolumeBase](BlockVolumeBase.md) |

## 构造器 {#constructor}

```python
ListBlockVolume(locations) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `locations` | 由值/所属选项确定 | `必填` | 传给 [ListBlockVolume.__init__](ListBlockVolume.md#constructor) 的 locations 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## add {#add}

```python
add(locations) -> None
```

创建或登记 `add` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `locations` | 由值/所属选项确定 | `必填` | 传给 [ListBlockVolume.add](ListBlockVolume.md#add) 的 locations 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_add(instance, locations):
    return instance.add(locations)
```

## remove {#remove}

```python
remove(locations) -> None
```

移除或清理 `remove` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `locations` | 由值/所属选项确定 | `必填` | 传给 [ListBlockVolume.remove](ListBlockVolume.md#remove) 的 locations 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_remove(instance, locations):
    return instance.remove(locations)
```

## getBlockLocationIterator {#getBlockLocationIterator}

```python
getBlockLocationIterator()
```

读取 `getBlockLocationIterator` 操作。参数形态和结果约定如下。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getBlockLocationIterator(instance):
    return instance.getBlockLocationIterator()
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

## getMin {#getMin}

```python
getMin() -> Vector3
```

读取 `getMin` 操作。参数形态和结果约定如下。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Empty volume has no bounds'` |

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

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Empty volume has no bounds'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getMax(instance):
    return instance.getMax()
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
| `delta` | [Vector3](../extra/vector.md) \| [tuple](../../common/type-system.md#tuple) \| [dict](../../common/type-system.md#dict) | `必填` | 传给 [ListBlockVolume.translate](ListBlockVolume.md#translate) 的 delta 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_translate(instance, delta):
    return instance.translate(delta)
```

## 使用示例


```python
from ModSAPI.server.beta import ListBlockVolume

volume = ListBlockVolume([(0, 64, 0), (2, 64, 2)])
print(volume.getCapacity())
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)