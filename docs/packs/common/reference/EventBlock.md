---
title: "EventBlock"
sidebar_label: "EventBlock"
---

# EventBlock

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/event_values.py`；声明补充了静态类型信息。

两端均可读取的只读方块快照，无需原生查询。实际方块可能已变化；若需读取服务端实时状态，请显式使用事件中已知的维度和 blockLocation 查询。

## 获取方式

从语义化方块交互事件的 block 属性读取；这是纯数据快照。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [typeId](#typeId) | 只读属性 |
| [location](#location) | 只读属性 |
| [dimension](#dimension) | 只读属性 |
| [auxValue](#auxValue) | 只读属性 |

## 构造器 {#constructor}

```python
EventBlock(typeId: Optional[str], location: Any, dimension: Optional[Union[Dimension, ClientDimension]] = None, auxValue: Optional[int] = None) -> None
```

校验并复制一次方块观察数据，不读取世界。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `typeId` | [Optional](../type-system.md#optional)[[str](../type-system.md#str)] | `必填` | 带命名空间的实体、物品或资源类型名称。 |
| `location` | [Any](../type-system.md#any) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `dimension` | [Optional](../type-system.md#optional)[[Union](../type-system.md#union)[[Dimension](../../server/apis/dimension.md), [ClientDimension](../../client/reference/ClientDimension.md)]] | [None](../type-system.md#none) | 传给 [EventBlock.__init__](EventBlock.md#constructor) 的 dimension 参数；结合上方功能说明和下方调用示例使用。 |
| `auxValue` | [Optional](../type-system.md#optional)[[int](../type-system.md#int)] | [None](../type-system.md#none) | 传给 [EventBlock.__init__](EventBlock.md#constructor) 的 auxValue 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../type-system.md#typeerror) | `'dimension must be a dimension object'` |
| [TypeError](../type-system.md#typeerror) | `'auxValue must be an integer'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## typeId {#typeId}

```python
typeId: Optional[str]
```

事件报告的带命名空间的方块类型；未知时为 [None](../type-system.md#none)。

**访问：** 只读。

**返回类型：** [Optional](../type-system.md#optional)[[str](../type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## location {#location}

```python
location: Vector3
```

新的位置向量副本；修改它不会改变事件坐标。

**访问：** 只读。

**返回类型：** [Vector3](../../server/extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.location
```

## dimension {#dimension}

```python
dimension: Optional[Union[Dimension, ClientDimension]]
```

观察到的 [Dimension](../../server/apis/dimension.md) 或 [ClientDimension](../../client/reference/ClientDimension.md)；未知时为 [None](../type-system.md#none)。

**访问：** 只读。

**返回类型：** [Optional](../type-system.md#optional)[[Union](../type-system.md#union)[[Dimension](../../server/apis/dimension.md), [ClientDimension](../../client/reference/ClientDimension.md)]]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.dimension
```

## auxValue {#auxValue}

```python
auxValue: Optional[int]
```

原生辅助值；仅在提供时存在，不等同于方块状态组合。

**访问：** 只读。

**返回类型：** [Optional](../type-system.md#optional)[[int](../type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.auxValue
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EventBlock 对象。
    print(value.typeId)
    print(value.location)
    print(value.dimension)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)