---
title: "WorldCustomCommandTriggerBeforeEvent"
sidebar_label: "WorldCustomCommandTriggerBeforeEvent"
---

# WorldCustomCommandTriggerBeforeEvent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/NativeEventTypes.py`；声明补充了静态类型信息。

此类型由运行时事件契约创建，并通过对应端的 `beta` 导出。通过 `subscribe` 回调取得实例；不要自行构造事件参数。

[CustomCommandTriggerServerEvent](../native-events.md#customcommandtriggerserverevent) 的事件参数；同步分发结束后不能再写入输出字段。

## 获取方式

通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。

所属信号：[world.beforeEvents.customCommandTrigger](../events/beforeEvents.md#customCommandTrigger).

基类：[NativeEventData](../../common/reference/NativeEventData.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [command](#command) | 只读属性 |
| [args](#args) | 只读属性 |
| [variant](#variant) | 只读属性 |
| [origin](#origin) | 只读属性 |
| [return_failed](#return_failed) | 可读写属性 |
| [return_msg_key](#return_msg_key) | 可读写属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [getNativeData](../../common/reference/NativeEventData.md#getNativeData) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [getNativeValue](../../common/reference/NativeEventData.md#getNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [nativeEventName](../../common/reference/NativeEventData.md#nativeEventName) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [setNativeValue](../../common/reference/NativeEventData.md#setNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |

## command {#command}

```python
command: Optional[str]
```

数据来源为原生字段 `command`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
自定义命令名称，对应json中的name字段；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## args {#args}

```python
args: Optional[list]
```

数据来源为原生字段 `args`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
自定义命令参数，详情见下方；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[list](../../common/type-system.md#list)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## variant {#variant}

```python
variant: Optional[int]
```

数据来源为原生字段 `variant`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
表示是哪条变体，范围`[0, 9]`，对应json中args键中的数字，未配置变体则为0；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## origin {#origin}

```python
origin: Optional[dict]
```

数据来源为原生字段 `origin`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
触发源的信息，详情见下方；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[dict](../../common/type-system.md#dict)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## return_failed {#return_failed}

```python
return_failed: Optional[bool]
```

数据来源为原生字段 `return_failed`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
设置自定义命令是否执行失败，默认为False，如果执行失败，返回信息以红色字体显示；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.return_failed = value`。参数类型线索：`(value: bool) -> None`。

在同步分发期间校验并写入原生 return_failed 输出。

写入参数 `value`：[bool](../../common/type-system.md#bool)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[bool](../../common/type-system.md#bool)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## return_msg_key {#return_msg_key}

```python
return_msg_key: Optional[str]
```

数据来源为原生字段 `return_msg_key`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
设置返回给玩家或命令方块的信息，也支持通过语言文件(.lang)定义，默认值为commands.custom.success(自定义命令执行成功)；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.return_msg_key = value`。参数类型线索：`(value: str) -> None`。

在同步分发期间校验并写入原生 return_msg_key 输出。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.beforeEvents.customCommandTrigger.subscribe(on_event)

def cleanup():
    world.beforeEvents.customCommandTrigger.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)