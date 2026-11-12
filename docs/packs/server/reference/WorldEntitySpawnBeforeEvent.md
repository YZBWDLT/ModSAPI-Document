---
title: "WorldEntitySpawnBeforeEvent"
sidebar_label: "WorldEntitySpawnBeforeEvent"
---

# WorldEntitySpawnBeforeEvent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/NativeEventTypes.py`；声明补充了静态类型信息。

此类型由运行时事件契约创建，并通过对应端的 `beta` 导出。通过 `subscribe` 回调取得实例；不要自行构造事件参数。

[ServerSpawnMobEvent](../native-events.md#serverspawnmobevent) 的事件参数；同步分发结束后不能再写入输出字段。

## 获取方式

通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。

所属信号：[world.beforeEvents.entitySpawn](../events/beforeEvents.md#entitySpawn).

基类：[NativeEventData](../../common/reference/NativeEventData.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [entity](#entity) | 只读属性 |
| [identifier](#identifier) | 只读属性 |
| [type](#type) | 只读属性 |
| [baby](#baby) | 只读属性 |
| [x](#x) | 只读属性 |
| [y](#y) | 只读属性 |
| [z](#z) | 只读属性 |
| [dimension](#dimension) | 只读属性 |
| [realIdentifier](#realIdentifier) | 只读属性 |
| [cancel](#cancel) | 可读写属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [getNativeData](../../common/reference/NativeEventData.md#getNativeData) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [getNativeValue](../../common/reference/NativeEventData.md#getNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [nativeEventName](../../common/reference/NativeEventData.md#nativeEventName) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [setNativeValue](../../common/reference/NativeEventData.md#setNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |

## entity {#entity}

```python
entity: Optional[Entity]
```

数据来源为原生字段 `entityId`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
实体id；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[Entity](../apis/entity.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## identifier {#identifier}

```python
identifier: Optional[str]
```

数据来源为原生字段 `identifier`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
生成实体的命名空间；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## type {#type}

```python
type: Optional[int]
```

数据来源为原生字段 [type](../../common/type-system.md#type)；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
生成实体的类型，参考EntityType；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## baby {#baby}

```python
baby: Optional[bool]
```

数据来源为原生字段 `baby`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
生成怪物是否是幼年怪；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[bool](../../common/type-system.md#bool)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## x {#x}

```python
x: Optional[float]
```

数据来源为原生字段 `x`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
生成实体坐标x；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## y {#y}

```python
y: Optional[float]
```

数据来源为原生字段 `y`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
生成实体坐标y；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## z {#z}

```python
z: Optional[float]
```

数据来源为原生字段 `z`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
生成实体坐标z；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## dimension {#dimension}

```python
dimension: Optional[Dimension]
```

数据来源为原生字段 `dimensionId`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
生成实体的维度，默认值为0（0为主世界，1为地狱，2为末地）；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[Dimension](../apis/dimension.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## realIdentifier {#realIdentifier}

```python
realIdentifier: Optional[str]
```

数据来源为原生字段 `realIdentifier`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
生成实体的命名空间，通过MOD API生成的生物在这个参数也能获取到真正的命名空间，而不是以custom开头的；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## cancel {#cancel}

```python
cancel: bool
```

数据来源为原生字段 `cancel`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
是否取消生成该实体；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.cancel = value`。参数类型线索：`(value: bool) -> None`。

在同步分发期间校验并写入原生 cancel 输出。

写入参数 `value`：[bool](../../common/type-system.md#bool)。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.beforeEvents.entitySpawn.subscribe(on_event)

def cleanup():
    world.beforeEvents.entitySpawn.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)