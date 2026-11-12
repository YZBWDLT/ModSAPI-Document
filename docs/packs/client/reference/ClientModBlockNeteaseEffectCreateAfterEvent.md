---
title: "ClientModBlockNeteaseEffectCreateAfterEvent"
sidebar_label: "ClientModBlockNeteaseEffectCreateAfterEvent"
---

# ClientModBlockNeteaseEffectCreateAfterEvent

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/NativeEventTypes.py`；声明补充了静态类型信息。

此类型由运行时事件契约创建，并通过对应端的 `beta` 导出。通过 `subscribe` 回调取得实例；不要自行构造事件参数。

[OnModBlockNeteaseEffectCreatedClientEvent](../events.md#onmodblockneteaseeffectcreatedclientevent) 的事件参数；同步分发结束后不能再写入输出字段。

## 获取方式

通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。

所属信号：[client.afterEvents.modBlockNeteaseEffectCreate](ClientAfterEvents.md#modBlockNeteaseEffectCreate).

基类：[NativeEventData](../../common/reference/NativeEventData.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [effectName](#effectName) | 只读属性 |
| [id](#id) | 只读属性 |
| [effectType](#effectType) | 只读属性 |
| [blockPos](#blockPos) | 只读属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [getNativeData](../../common/reference/NativeEventData.md#getNativeData) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [getNativeValue](../../common/reference/NativeEventData.md#getNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [nativeEventName](../../common/reference/NativeEventData.md#nativeEventName) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [setNativeValue](../../common/reference/NativeEventData.md#setNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |

## effectName {#effectName}

```python
effectName: Optional[str]
```

数据来源为原生字段 `effectName`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
创建成功的特效的自定义键值名称；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## id {#id}

```python
id: Optional[int]
```

数据来源为原生字段 `id`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
该特效的id；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## effectType {#effectType}

```python
effectType: Optional[int]
```

数据来源为原生字段 `effectType`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
该特效的类型，0为粒子特效，1为序列帧特效；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockPos {#blockPos}

```python
blockPos: Optional[tuple]
```

数据来源为原生字段 `blockPos`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
该特效绑定的自定义方块实体的世界坐标；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[tuple](../../common/type-system.md#tuple)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.modBlockNeteaseEffectCreate.subscribe(on_event)

def cleanup():
    client.afterEvents.modBlockNeteaseEffectCreate.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)