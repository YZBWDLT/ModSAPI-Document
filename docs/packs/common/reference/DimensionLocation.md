---
title: "DimensionLocation"
sidebar_label: "DimensionLocation"
---

# DimensionLocation

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/Vector.py`；声明补充了静态类型信息。

选项通常可直接传 Python 字典；包装类名本身不保证通过模板导出。只使用所属操作已经实现的字段。

世界中的精确坐标，包含维度和位置。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [dimension](#dimension) | 可读写属性 |
| [x](#x) | 可读写属性 |
| [y](#y) | 可读写属性 |
| [z](#z) | 可读写属性 |

## 构造器 {#constructor}

```python
DimensionLocation(dimension, location)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `dimension` | 由值/所属选项确定 | `必填` | 传给 [DimensionLocation.__init__](DimensionLocation.md#constructor) 的 dimension 参数；结合上方功能说明和下方调用示例使用。 |
| `location` | 由值/所属选项确定 | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## dimension {#dimension}

```python
dimension
```

读取 `dimension` 的当前值。

**访问：** 可读写。

写入方式：`instance.dimension = value`。参数类型线索：`(value: Dimension) -> None`。

写入参数 `value`：[Dimension](../../server/apis/dimension.md)。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.dimension

def write_value(instance, value):
    instance.dimension = value
```

## x {#x}

```python
x
```

读取 `x` 的当前值。

**访问：** 可读写。

写入方式：`instance.x = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.x

def write_value(instance, value):
    instance.x = value
```

## y {#y}

```python
y
```

读取 `y` 的当前值。

**访问：** 可读写。

写入方式：`instance.y = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.y

def write_value(instance, value):
    instance.y = value
```

## z {#z}

```python
z
```

读取 `z` 的当前值。

**访问：** 可读写。

写入方式：`instance.z = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.z

def write_value(instance, value):
    instance.z = value
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 DimensionLocation 对象。
    print(value.dimension)
    print(value.x)
    print(value.y)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)