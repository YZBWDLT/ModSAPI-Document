---
title: "WorldChangeLevelUpCostBeforeEvent"
sidebar_label: "WorldChangeLevelUpCostBeforeEvent"
---

# WorldChangeLevelUpCostBeforeEvent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/NativeEventTypes.py`；声明补充了静态类型信息。

此类型由运行时事件契约创建，并通过对应端的 `beta` 导出。通过 `subscribe` 回调取得实例；不要自行构造事件参数。

[ChangeLevelUpCostServerEvent](../native-events.md#changelevelupcostserverevent) 的事件参数；同步分发结束后不能再写入输出字段。

## 获取方式

通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。

所属信号：[world.beforeEvents.changeLevelUpCost](../events/beforeEvents.md#changeLevelUpCost).

基类：[NativeEventData](../../common/reference/NativeEventData.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [level](#level) | 只读属性 |
| [levelUpCostExp](#levelUpCostExp) | 可读写属性 |
| [changed](#changed) | 可读写属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [getNativeData](../../common/reference/NativeEventData.md#getNativeData) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [getNativeValue](../../common/reference/NativeEventData.md#getNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [nativeEventName](../../common/reference/NativeEventData.md#nativeEventName) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [setNativeValue](../../common/reference/NativeEventData.md#setNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |

## level {#level}

```python
level: Optional[int]
```

数据来源为原生字段 `level`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
玩家当前等级；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## levelUpCostExp {#levelUpCostExp}

```python
levelUpCostExp: Optional[int]
```

数据来源为原生字段 `levelUpCostExp`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
当前等级升级到下个等级需要的经验值，当设置升级经验小于1时会被强制调整到1；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.levelUpCostExp = value`。参数类型线索：`(value: int) -> None`。

在同步分发期间校验并写入原生 levelUpCostExp 输出。

写入参数 `value`：[int](../../common/type-system.md#int)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## changed {#changed}

```python
changed: Optional[bool]
```

数据来源为原生字段 `changed`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
设置为True，重载玩家升级经验才会生效；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.changed = value`。参数类型线索：`(value: bool) -> None`。

在同步分发期间校验并写入原生 changed 输出。

写入参数 `value`：[bool](../../common/type-system.md#bool)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[bool](../../common/type-system.md#bool)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.beforeEvents.changeLevelUpCost.subscribe(on_event)

def cleanup():
    world.beforeEvents.changeLevelUpCost.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)