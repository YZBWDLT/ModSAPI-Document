---
title: "DimensionLocation"
sidebar_label: "DimensionLocation"
---

# DimensionLocation

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/Vector.py`；声明补充了静态类型信息。

这是值对象或结果包装对象，成员通过属性访问；是否接受字典输入由所属操作的签名决定。包装类型不一定是模板入口的直接导出符号。

关联维度对象的可变坐标值。输入坐标通过 [Vector3](../../server/extra/vector.md) 复制，并且必须为有限数值。读取或修改该值不会移动实体，也不会查询世界。

## 获取方式

从服务端入口导入 [DimensionLocation](DimensionLocation.md)；构造时传入 [Dimension](../../server/apis/dimension.md) 对象和 [Vector3](../../server/extra/vector.md)、三项序列或坐标字典。也可从返回该类型的操作取得。

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
DimensionLocation(dimension: Dimension, location: Vector3 | tuple[float, float, float] | list[float] | dict[str, float]) -> None
```

复制兼容 [Vector3](../../server/extra/vector.md) 的坐标，并保留传入的维度对象。

:::note 当前实现说明
复制坐标并保留维度对象；无 SDK 端的查询或实体移动。布尔值、非数值以及非有限数会被拒绝，坐标属性写入失败保留旧值。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `dimension` | [Dimension](../../server/apis/dimension.md) | `必填` | 传给 [DimensionLocation.__init__](DimensionLocation.md#constructor) 的 dimension 参数；结合上方功能说明和下方调用示例使用。 |
| `location` | [Vector3](../../server/extra/vector.md) \| [tuple](../type-system.md#tuple)[[float](../type-system.md#float), [float](../type-system.md#float), [float](../type-system.md#float)] \| [list](../type-system.md#list)[[float](../type-system.md#float)] \| [dict](../type-system.md#dict)[[str](../type-system.md#str), [float](../type-system.md#float)] | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## dimension {#dimension}

```python
dimension: Dimension
```

关联的维度对象；读取时不会执行原生查询。

**访问：** 可读写。

写入方式：`instance.dimension = value`。参数类型线索：`(value: Dimension) -> None`。

写入参数 `value`：[Dimension](../../server/apis/dimension.md)。

**返回类型：** [Dimension](../../server/apis/dimension.md)。静态声明不替代本页的实现限制。

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
x: float
```

有限数值形式的 X 坐标。

**访问：** 可读写。

写入方式：`instance.x = value`。参数类型线索：`(value: float) -> None`。

写入参数 `value`：[float](../type-system.md#float)。

**返回类型：** [float](../type-system.md#float)。静态声明不替代本页的实现限制。

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
y: float
```

有限数值形式的 Y 坐标。

**访问：** 可读写。

写入方式：`instance.y = value`。参数类型线索：`(value: float) -> None`。

写入参数 `value`：[float](../type-system.md#float)。

**返回类型：** [float](../type-system.md#float)。静态声明不替代本页的实现限制。

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
z: float
```

有限数值形式的 Z 坐标。

**访问：** 可读写。

写入方式：`instance.z = value`。参数类型线索：`(value: float) -> None`。

写入参数 `value`：[float](../type-system.md#float)。

**返回类型：** [float](../type-system.md#float)。静态声明不替代本页的实现限制。

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