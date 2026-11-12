---
title: "BlockVolume"
sidebar_label: "BlockVolume"
---

import ApiFieldAnchor from '@docusaurus/Link';

# BlockVolume

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Block.py`；声明补充了静态类型信息。

以两个角点描述世界中的三维方块区域。两个角点的分量不要求按最小值、最大值排序，且始终保留初始角点身份；编辑时即使两角点交叉，也不会交换它们的含义。角点不能直接当作已排序的方块位置范围；需要边界范围时使用 getBoundingBox。区域按方块计数并包含端点，因此从 (0, 0, 0) 到 (0, 0, 0) 的区域大小为 (1, 1, 1)。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[BlockVolumeBase](BlockVolumeBase.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-to" />`to` | 由运行时值确定 | `property(lambda self: self.toLocation, lambda self, value: setattr(self, 'toLocation', value))` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [fromLocation](#fromLocation) | 可读写属性 |
| [toLocation](#toLocation) | 可读写属性 |
| [doesLocationTouchFaces](#doesLocationTouchFaces) | 方法 |
| [doesVolumeTouchFaces](#doesVolumeTouchFaces) | 方法 |
| [intersects](#intersects) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [getBlockLocationIterator](BlockVolumeBase.md#getBlockLocationIterator) | [BlockVolumeBase](BlockVolumeBase.md) |
| [getCapacity](BlockVolumeBase.md#getCapacity) | [BlockVolumeBase](BlockVolumeBase.md) |
| [getClosest](BlockVolumeBase.md#getClosest) | [BlockVolumeBase](BlockVolumeBase.md) |
| [getFarthest](BlockVolumeBase.md#getFarthest) | [BlockVolumeBase](BlockVolumeBase.md) |
| [getMax](BlockVolumeBase.md#getMax) | [BlockVolumeBase](BlockVolumeBase.md) |
| [getMin](BlockVolumeBase.md#getMin) | [BlockVolumeBase](BlockVolumeBase.md) |
| [getSpan](BlockVolumeBase.md#getSpan) | [BlockVolumeBase](BlockVolumeBase.md) |
| [isInside](BlockVolumeBase.md#isInside) | [BlockVolumeBase](BlockVolumeBase.md) |
| [translate](BlockVolumeBase.md#translate) | [BlockVolumeBase](BlockVolumeBase.md) |

## 构造器 {#constructor}

```python
BlockVolume(fromLocation: Vector3, toLocation: Vector3) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fromLocation` | [Vector3](../extra/vector.md) | `必填` | 传给 [BlockVolume.__init__](BlockVolume.md#constructor) 的 fromLocation 参数；结合上方功能说明和下方调用示例使用。 |
| `toLocation` | [Vector3](../extra/vector.md) | `必填` | 传给 [BlockVolume.__init__](BlockVolume.md#constructor) 的 toLocation 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fromLocation {#fromLocation}

```python
fromLocation: Vector3
```

读取 `fromLocation` 的当前值。

:::note 当前实现说明
Python 名称，不使用保留字 from。体积端点包含边界。
:::

**访问：** 可读写。

写入方式：`instance.fromLocation = value`。参数类型线索：`(value: Vector3 \| tuple \| dict) -> None`。

写入参数 `value`：[Vector3](../extra/vector.md) \| [tuple](../../common/type-system.md#tuple) \| [dict](../../common/type-system.md#dict)。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.fromLocation

def write_value(instance, value):
    instance.fromLocation = value
```

## toLocation {#toLocation}

```python
toLocation: Vector3
```

读取 `toLocation` 的当前值。

**访问：** 可读写。

写入方式：`instance.toLocation = value`。参数类型线索：`(value: Vector3 \| tuple \| dict) -> None`。

写入参数 `value`：[Vector3](../extra/vector.md) \| [tuple](../../common/type-system.md#tuple) \| [dict](../../common/type-system.md#dict)。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.toLocation

def write_value(instance, value):
    instance.toLocation = value
```

## doesLocationTouchFaces {#doesLocationTouchFaces}

```python
doesLocationTouchFaces(pos: Vector3 | tuple | dict) -> bool
```

执行 `doesLocationTouchFaces` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `pos` | [Vector3](../extra/vector.md) \| [tuple](../../common/type-system.md#tuple) \| [dict](../../common/type-system.md#dict) | `必填` | 传给 [BlockVolume.doesLocationTouchFaces](BlockVolume.md#doesLocationTouchFaces) 的 pos 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_doesLocationTouchFaces(instance, pos):
    return instance.doesLocationTouchFaces(pos)
```

## doesVolumeTouchFaces {#doesVolumeTouchFaces}

```python
doesVolumeTouchFaces(other: BlockVolumeBase) -> bool
```

执行 `doesVolumeTouchFaces` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `other` | [BlockVolumeBase](BlockVolumeBase.md) | `必填` | 传给 [BlockVolume.doesVolumeTouchFaces](BlockVolume.md#doesVolumeTouchFaces) 的 other 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_doesVolumeTouchFaces(instance, other):
    return instance.doesVolumeTouchFaces(other)
```

## intersects {#intersects}

```python
intersects(other: BlockVolumeBase) -> int
```

执行 `intersects` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `other` | [BlockVolumeBase](BlockVolumeBase.md) | `必填` | 传给 [BlockVolume.intersects](BlockVolume.md#intersects) 的 other 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_intersects(instance, other):
    return instance.intersects(other)
```

## 使用示例


```python
from ModSAPI.server.beta import BlockVolume

volume = BlockVolume((0, 64, 0), (2, 65, 2))
print(volume.getCapacity())
for location in volume.getBlockLocationIterator():
    print(location.getTuple())
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)