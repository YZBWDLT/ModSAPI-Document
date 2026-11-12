---
title: "ClientPlayerAddCustomContainerItemAfterEvent"
sidebar_label: "ClientPlayerAddCustomContainerItemAfterEvent"
---

# ClientPlayerAddCustomContainerItemAfterEvent

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/NativeEventTypes.py`；声明补充了静态类型信息。

此类型由运行时事件契约创建，并通过对应端的 `beta` 导出。通过 `subscribe` 回调取得实例；不要自行构造事件参数。

[PlayerAddCustomContainerItemClientEvent](../events.md#playeraddcustomcontaineritemclientevent) 的事件参数；同步分发结束后不能再写入输出字段。

## 获取方式

通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。

所属信号：[client.afterEvents.playerAddCustomContainerItem](ClientAfterEvents.md#playerAddCustomContainerItem).

基类：[NativeEventData](../../common/reference/NativeEventData.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [beforeItemDict](#beforeItemDict) | 只读属性 |
| [changedItemDict](#changedItemDict) | 只读属性 |
| [afterItemDict](#afterItemDict) | 只读属性 |
| [collectionName](#collectionName) | 只读属性 |
| [collectionType](#collectionType) | 只读属性 |
| [collectionIndex](#collectionIndex) | 只读属性 |
| [x](#x) | 只读属性 |
| [y](#y) | 只读属性 |
| [z](#z) | 只读属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [getNativeData](../../common/reference/NativeEventData.md#getNativeData) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [getNativeValue](../../common/reference/NativeEventData.md#getNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [nativeEventName](../../common/reference/NativeEventData.md#nativeEventName) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [setNativeValue](../../common/reference/NativeEventData.md#setNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |

## beforeItemDict {#beforeItemDict}

```python
beforeItemDict: Optional[dict]
```

数据来源为原生字段 `beforeItemDict`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
操作前目标槽位的物品信息字典；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[dict](../../common/type-system.md#dict)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## changedItemDict {#changedItemDict}

```python
changedItemDict: Optional[dict]
```

数据来源为原生字段 `changedItemDict`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
实际添加的物品的物品信息字典；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[dict](../../common/type-system.md#dict)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## afterItemDict {#afterItemDict}

```python
afterItemDict: Optional[dict]
```

数据来源为原生字段 `afterItemDict`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
操作后目标槽位的物品信息字典；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[dict](../../common/type-system.md#dict)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## collectionName {#collectionName}

```python
collectionName: Optional[str]
```

数据来源为原生字段 `collectionName`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
容器名称，对应容器json中"custom_description"字段；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## collectionType {#collectionType}

```python
collectionType: Optional[str]
```

数据来源为原生字段 `collectionType`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
容器类型，目前仅支持netease_container和netease_ui_container；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## collectionIndex {#collectionIndex}

```python
collectionIndex: Optional[int]
```

数据来源为原生字段 `collectionIndex`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
容器槽位索引；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## x {#x}

```python
x: Optional[int]
```

数据来源为原生字段 `x`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
容器方块x坐标；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## y {#y}

```python
y: Optional[int]
```

数据来源为原生字段 `y`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
容器方块y坐标；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## z {#z}

```python
z: Optional[int]
```

数据来源为原生字段 `z`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
容器方块z坐标；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.playerAddCustomContainerItem.subscribe(on_event)

def cleanup():
    client.afterEvents.playerAddCustomContainerItem.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)