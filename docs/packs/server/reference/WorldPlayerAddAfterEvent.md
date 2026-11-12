---
title: "WorldPlayerAddAfterEvent"
sidebar_label: "WorldPlayerAddAfterEvent"
---

# WorldPlayerAddAfterEvent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/NativeEventTypes.py`；声明补充了静态类型信息。

此类型由运行时事件契约创建，并通过对应端的 `beta` 导出。通过 `subscribe` 回调取得实例；不要自行构造事件参数。

[AddServerPlayerEvent](../native-events.md#addserverplayerevent) 的事件参数；同步分发结束后不能再写入输出字段。

## 获取方式

通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。

所属信号：[world.afterEvents.playerAdd](../events/afterEvents.md#playerAdd).

基类：[NativeEventData](../../common/reference/NativeEventData.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [player](#player) | 只读属性 |
| [isTransfer](#isTransfer) | 只读属性 |
| [isReconnect](#isReconnect) | 只读属性 |
| [isPeUser](#isPeUser) | 只读属性 |
| [transferParam](#transferParam) | 只读属性 |
| [uid](#uid) | 只读属性 |
| [proxyId](#proxyId) | 只读属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [getNativeData](../../common/reference/NativeEventData.md#getNativeData) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [getNativeValue](../../common/reference/NativeEventData.md#getNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [nativeEventName](../../common/reference/NativeEventData.md#nativeEventName) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [setNativeValue](../../common/reference/NativeEventData.md#setNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |

## player {#player}

```python
player: Optional[Player]
```

数据来源为原生字段 `id`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
玩家id；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[Player](../apis/player.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## isTransfer {#isTransfer}

```python
isTransfer: Optional[bool]
```

数据来源为原生字段 `isTransfer`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
是否是切服时进入服务器，仅用于Apollo。如果是True，则表示切服时加入服务器，若是False，则表示登录进入网络游戏；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[bool](../../common/type-system.md#bool)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## isReconnect {#isReconnect}

```python
isReconnect: Optional[bool]
```

数据来源为原生字段 `isReconnect`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
是否是断线重连，仅用于Apollo。如果是True，则表示本次登录是断线重连，若是False，则表示本次是正常登录或者转服；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[bool](../../common/type-system.md#bool)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## isPeUser {#isPeUser}

```python
isPeUser: Optional[bool]
```

数据来源为原生字段 `isPeUser`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
是否从手机端登录，仅用于Apollo。如果是True，则表示本次登录是从手机端登录，若是False，则表示本次登录是从PC端登录；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[bool](../../common/type-system.md#bool)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## transferParam {#transferParam}

```python
transferParam: Optional[str]
```

数据来源为原生字段 `transferParam`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
切服传入参数，仅用于Apollo。调用【TransferToOtherServer】或【TransferToOtherServerById】传入的切服参数；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## uid {#uid}

```python
uid: Optional[int]
```

数据来源为原生字段 `uid`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
仅用于Apollo，玩家的netease uid，玩家的唯一标识；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## proxyId {#proxyId}

```python
proxyId: Optional[int]
```

数据来源为原生字段 `proxyId`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
仅用于Apollo，当前客户端连接的proxy服务器id；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.playerAdd.subscribe(on_event)

def cleanup():
    world.afterEvents.playerAdd.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)