---
title: "MolangVariableMap"
sidebar_label: "MolangVariableMap"
---

# MolangVariableMap

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/MolangVariableMap.py`；声明补充了静态类型信息。

用于进一步控制渲染和动画的附加变量集合。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [setColorRGB](#setColorRGB) | 方法 |
| [setColorRGBA](#setColorRGBA) | 方法 |
| [setFloat](#setFloat) | 方法 |
| [setSpeedAndDirection](#setSpeedAndDirection) | 方法 |
| [setVector3](#setVector3) | 方法 |
| [getData](#getData) | 方法 |

## 构造器 {#constructor}

```python
MolangVariableMap()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## setColorRGB {#setColorRGB}

```python
setColorRGB(variableName: str, color: RGB)
```

添加颜色变量：变量名后的 .r、.g、.b 分别为红、绿、蓝通道，取值范围均为 0–1。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `variableName` | [str](../../common/type-system.md#str) | `必填` | 传给 [MolangVariableMap.setColorRGB](MolangVariableMap.md#setColorRGB) 的 variableName 参数；结合上方功能说明和下方调用示例使用。 |
| `color` | [RGB](RGB.md) | `必填` | 传给 [MolangVariableMap.setColorRGB](MolangVariableMap.md#setColorRGB) 的 color 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setColorRGB(instance, variableName, color):
    return instance.setColorRGB(variableName, color)
```

## setColorRGBA {#setColorRGBA}

```python
setColorRGBA(variableName: str, color: RGBA)
```

添加颜色变量：变量名后的 .r、.g、.b 为红、绿、蓝通道，.a 为不透明度，取值范围均为 0–1。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `variableName` | [str](../../common/type-system.md#str) | `必填` | 传给 [MolangVariableMap.setColorRGBA](MolangVariableMap.md#setColorRGBA) 的 variableName 参数；结合上方功能说明和下方调用示例使用。 |
| `color` | [RGBA](RGBA.md) | `必填` | 传给 [MolangVariableMap.setColorRGBA](MolangVariableMap.md#setColorRGBA) 的 color 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setColorRGBA(instance, variableName, color):
    return instance.setColorRGBA(variableName, color)
```

## setFloat {#setFloat}

```python
setFloat(variableName: str, value: float)
```

向 MoLang 添加浮点变量。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `variableName` | [str](../../common/type-system.md#str) | `必填` | 传给 [MolangVariableMap.setFloat](MolangVariableMap.md#setFloat) 的 variableName 参数；结合上方功能说明和下方调用示例使用。 |
| `value` | [float](../../common/type-system.md#float) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setFloat(instance, variableName, value):
    return instance.setFloat(variableName, value)
```

## setSpeedAndDirection {#setSpeedAndDirection}

```python
setSpeedAndDirection(variableName: str, speed: float, direction: Vector3)
```

添加运动变量：变量名后的 .speed 表示速度，.direction_x、.direction_y、.direction_z 表示方向分量。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `variableName` | [str](../../common/type-system.md#str) | `必填` | 传给 [MolangVariableMap.setSpeedAndDirection](MolangVariableMap.md#setSpeedAndDirection) 的 variableName 参数；结合上方功能说明和下方调用示例使用。 |
| `speed` | [float](../../common/type-system.md#float) | `必填` | 传给 [MolangVariableMap.setSpeedAndDirection](MolangVariableMap.md#setSpeedAndDirection) 的 speed 参数；结合上方功能说明和下方调用示例使用。 |
| `direction` | [Vector3](../extra/vector.md) | `必填` | 传给 [MolangVariableMap.setSpeedAndDirection](MolangVariableMap.md#setSpeedAndDirection) 的 direction 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setSpeedAndDirection(instance, variableName, speed, direction):
    return instance.setSpeedAndDirection(variableName, speed, direction)
```

## setVector3 {#setVector3}

```python
setVector3(variableName: str, vector: Vector3)
```

添加向量变量：变量名后的 .x、.y、.z 分别表示三个坐标分量。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `variableName` | [str](../../common/type-system.md#str) | `必填` | 传给 [MolangVariableMap.setVector3](MolangVariableMap.md#setVector3) 的 variableName 参数；结合上方功能说明和下方调用示例使用。 |
| `vector` | [Vector3](../extra/vector.md) | `必填` | 传给 [MolangVariableMap.setVector3](MolangVariableMap.md#setVector3) 的 vector 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setVector3(instance, variableName, vector):
    return instance.setVector3(variableName, vector)
```

## getData {#getData}

```python
getData() -> dict
```

读取此 [MolangVariableMap](MolangVariableMap.md) 的数据。

**返回类型：** [dict](../../common/type-system.md#dict)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getData(instance):
    return instance.getData()
```

## 使用示例


```python
from ModSAPI.server.beta import MolangVariableMap

variables = MolangVariableMap()
variables.setFloat("variable.size", 1.5)
variables.setColorRGB("variable.color", {"red": 1, "green": 0.5, "blue": 0})
print(variables.getData())
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)