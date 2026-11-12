---
title: "WorldEntityPlaceBlockBeforeEvent"
sidebar_label: "WorldEntityPlaceBlockBeforeEvent"
---

# WorldEntityPlaceBlockBeforeEvent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/NativeEventTypes.py`；声明补充了静态类型信息。

此类型由运行时事件契约创建，并通过对应端的 `beta` 导出。通过 `subscribe` 回调取得实例；不要自行构造事件参数。

[ServerEntityTryPlaceBlockEvent](../native-events.md#serverentitytryplaceblockevent) 的事件参数；同步分发结束后不能再写入输出字段。

## 获取方式

通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。

所属信号：[world.beforeEvents.entityPlaceBlock](../events/beforeEvents.md#entityPlaceBlock).

基类：[NativeEventData](../../common/reference/NativeEventData.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [x](#x) | 可读写属性 |
| [y](#y) | 可读写属性 |
| [z](#z) | 可读写属性 |
| [fullName](#fullName) | 可读写属性 |
| [auxData](#auxData) | 可读写属性 |
| [entity](#entity) | 只读属性 |
| [dimension](#dimension) | 只读属性 |
| [face](#face) | 只读属性 |
| [cancel](#cancel) | 可读写属性 |
| [clickX](#clickX) | 只读属性 |
| [clickY](#clickY) | 只读属性 |
| [clickZ](#clickZ) | 只读属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [getNativeData](../../common/reference/NativeEventData.md#getNativeData) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [getNativeValue](../../common/reference/NativeEventData.md#getNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [nativeEventName](../../common/reference/NativeEventData.md#nativeEventName) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [setNativeValue](../../common/reference/NativeEventData.md#setNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |

## x {#x}

```python
x: Optional[int]
```

数据来源为原生字段 `x`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
方块x坐标,支持修改；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.x = value`。参数类型线索：`(value: int) -> None`。

在同步分发期间校验并写入原生 x 输出。

写入参数 `value`：[int](../../common/type-system.md#int)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## y {#y}

```python
y: Optional[int]
```

数据来源为原生字段 `y`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
方块y坐标,支持修改；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.y = value`。参数类型线索：`(value: int) -> None`。

在同步分发期间校验并写入原生 y 输出。

写入参数 `value`：[int](../../common/type-system.md#int)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## z {#z}

```python
z: Optional[int]
```

数据来源为原生字段 `z`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
方块z坐标,支持修改；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.z = value`。参数类型线索：`(value: int) -> None`。

在同步分发期间校验并写入原生 z 输出。

写入参数 `value`：[int](../../common/type-system.md#int)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fullName {#fullName}

```python
fullName: Optional[str]
```

数据来源为原生字段 `fullName`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
方块的identifier，包含命名空间及名称,支持修改；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.fullName = value`。参数类型线索：`(value: str) -> None`。

在同步分发期间校验并写入原生 fullName 输出。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## auxData {#auxData}

```python
auxData: Optional[int]
```

数据来源为原生字段 `auxData`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
方块附加值,支持修改；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.auxData = value`。参数类型线索：`(value: int) -> None`。

在同步分发期间校验并写入原生 auxData 输出。

写入参数 `value`：[int](../../common/type-system.md#int)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## entity {#entity}

```python
entity: Optional[Entity]
```

数据来源为原生字段 `entityId`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
试图放置方块的生物ID；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[Entity](../apis/entity.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## dimension {#dimension}

```python
dimension: Optional[Dimension]
```

数据来源为原生字段 `dimensionId`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
维度id；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[Dimension](../apis/dimension.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## face {#face}

```python
face: Optional[int]
```

数据来源为原生字段 `face`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
点击方块的面，参考Facing枚举；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## cancel {#cancel}

```python
cancel: bool
```

数据来源为原生字段 `cancel`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
默认为False，在脚本层设置为True就能取消该方块的放置；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.cancel = value`。参数类型线索：`(value: bool) -> None`。

在同步分发期间校验并写入原生 cancel 输出。

写入参数 `value`：[bool](../../common/type-system.md#bool)。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## clickX {#clickX}

```python
clickX: Optional[float]
```

数据来源为原生字段 `clickX`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
点击点的x比例位置；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## clickY {#clickY}

```python
clickY: Optional[float]
```

数据来源为原生字段 `clickY`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
点击点的y比例位置；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## clickZ {#clickZ}

```python
clickZ: Optional[float]
```

数据来源为原生字段 `clickZ`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
点击点的z比例位置；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.beforeEvents.entityPlaceBlock.subscribe(on_event)

def cleanup():
    world.beforeEvents.entityPlaceBlock.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)