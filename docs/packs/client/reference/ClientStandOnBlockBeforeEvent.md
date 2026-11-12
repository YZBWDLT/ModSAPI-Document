---
title: "ClientStandOnBlockBeforeEvent"
sidebar_label: "ClientStandOnBlockBeforeEvent"
---

# ClientStandOnBlockBeforeEvent

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/NativeEventTypes.py`；声明补充了静态类型信息。

此类型由运行时事件契约创建，并通过对应端的 `beta` 导出。通过 `subscribe` 回调取得实例；不要自行构造事件参数。

[OnStandOnBlockClientEvent](../events.md#onstandonblockclientevent) 的事件参数；同步分发结束后不能再写入输出字段。

## 获取方式

通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。

所属信号：[client.beforeEvents.standOnBlock](ClientBeforeEvents.md#standOnBlock).

基类：[NativeEventData](../../common/reference/NativeEventData.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [entity](#entity) | 只读属性 |
| [dimension](#dimension) | 只读属性 |
| [posX](#posX) | 只读属性 |
| [posY](#posY) | 只读属性 |
| [posZ](#posZ) | 只读属性 |
| [motionX](#motionX) | 可读写属性 |
| [motionY](#motionY) | 可读写属性 |
| [motionZ](#motionZ) | 可读写属性 |
| [blockX](#blockX) | 只读属性 |
| [blockY](#blockY) | 只读属性 |
| [blockZ](#blockZ) | 只读属性 |
| [blockName](#blockName) | 只读属性 |
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
entity: Optional[ClientEntity]
```

数据来源为原生字段 `entityId`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
实体id；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[ClientEntity](ClientEntity.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## dimension {#dimension}

```python
dimension: Optional[ClientDimension]
```

数据来源为原生字段 `dimensionId`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
实体所在维度id；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[ClientDimension](ClientDimension.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## posX {#posX}

```python
posX: Optional[float]
```

数据来源为原生字段 `posX`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
实体位置x；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## posY {#posY}

```python
posY: Optional[float]
```

数据来源为原生字段 `posY`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
实体位置y；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## posZ {#posZ}

```python
posZ: Optional[float]
```

数据来源为原生字段 `posZ`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
实体位置z；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## motionX {#motionX}

```python
motionX: Optional[float]
```

数据来源为原生字段 `motionX`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
瞬时移动X方向的力；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.motionX = value`。参数类型线索：`(value: float) -> None`。

在同步分发期间校验并写入原生 motionX 输出。

写入参数 `value`：[float](../../common/type-system.md#float)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## motionY {#motionY}

```python
motionY: Optional[float]
```

数据来源为原生字段 `motionY`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
瞬时移动Y方向的力；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.motionY = value`。参数类型线索：`(value: float) -> None`。

在同步分发期间校验并写入原生 motionY 输出。

写入参数 `value`：[float](../../common/type-system.md#float)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## motionZ {#motionZ}

```python
motionZ: Optional[float]
```

数据来源为原生字段 `motionZ`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
瞬时移动Z方向的力；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.motionZ = value`。参数类型线索：`(value: float) -> None`。

在同步分发期间校验并写入原生 motionZ 输出。

写入参数 `value`：[float](../../common/type-system.md#float)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockX {#blockX}

```python
blockX: Optional[int]
```

数据来源为原生字段 `blockX`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
方块位置x；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockY {#blockY}

```python
blockY: Optional[int]
```

数据来源为原生字段 `blockY`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
方块位置y；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockZ {#blockZ}

```python
blockZ: Optional[int]
```

数据来源为原生字段 `blockZ`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
方块位置z；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockName {#blockName}

```python
blockName: Optional[str]
```

数据来源为原生字段 `blockName`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
方块的identifier，包含命名空间及名称；只读。
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
可由脚本层回传True给引擎，阻止触发后续原版逻辑；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.cancel = value`。参数类型线索：`(value: bool) -> None`。

在同步分发期间校验并写入原生 cancel 输出。

写入参数 `value`：[bool](../../common/type-system.md#bool)。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.beforeEvents.standOnBlock.subscribe(on_event)

def cleanup():
    client.beforeEvents.standOnBlock.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)