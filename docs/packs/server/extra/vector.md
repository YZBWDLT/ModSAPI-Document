---
title: "Vector3"
sidebar_label: "Vector3"
---

# Vector3

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/Vector.py`；声明补充了静态类型信息。

选项通常可直接传 Python 字典；包装类名本身不保证通过模板导出。只使用所属操作已经实现的字段。

创建描述空间位置或方向的向量。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `x` | [float](../../common/type-system.md#float) | `data.x` |  |
| `y` | [float](../../common/type-system.md#float) | `data.y` |  |
| `z` | [float](../../common/type-system.md#float) | `data.z` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [rotateY](#rotateY) | 方法 |
| [getData](#getData) | 方法 |
| [getTuple](#getTuple) | 方法 |
| [getIntTuple](#getIntTuple) | 方法 |
| [distance](#distance) | 只读属性 |

## 构造器 {#constructor}

```python
Vector3(data: dict | tuple) -> None
```

创建描述空间位置或方向的向量。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | [dict](../../common/type-system.md#dict) \| [tuple](../../common/type-system.md#tuple) | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Vector3 requires three coordinates'` |
| [TypeError](../../common/type-system.md#typeerror) | `'Vector3 requires three coordinate fields'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## rotateY {#rotateY}

```python
rotateY(angle: float) -> Vector3
```

绕 y 轴逆时针旋转向量，遵循左手规则。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `angle` | [float](../../common/type-system.md#float) | `必填` | 传给 [Vector3.rotateY](vector.md#rotateY) 的 angle 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Vector3](vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_rotateY(instance, angle):
    return instance.rotateY(angle)
```

## getData {#getData}

```python
getData() -> dict
```

获取字典数据

**返回类型：** [dict](../../common/type-system.md#dict)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getData(instance):
    return instance.getData()
```

## getTuple {#getTuple}

```python
getTuple() -> tuple[float, float, float]
```

读取 `getTuple` 操作。参数形态和结果约定如下。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getTuple(instance):
    return instance.getTuple()
```

## getIntTuple {#getIntTuple}

```python
getIntTuple() -> tuple[int, int, int]
```

读取 `getIntTuple` 操作。参数形态和结果约定如下。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[int](../../common/type-system.md#int), [int](../../common/type-system.md#int), [int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getIntTuple(instance):
    return instance.getIntTuple()
```

## distance {#distance}

```python
distance: float
```

向量到原点的距离。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.distance
```

## 使用示例


```python
from ModSAPI.server.beta import Vector3

position = Vector3((1, 64, 2))
offset = Vector3({"x": 0, "y": 1, "z": 0})
print((position + offset).getTuple())
print(position.distance)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)