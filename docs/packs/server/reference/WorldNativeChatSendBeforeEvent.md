---
title: "WorldNativeChatSendBeforeEvent"
sidebar_label: "WorldNativeChatSendBeforeEvent"
---

# WorldNativeChatSendBeforeEvent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/NativeEventTypes.py`；声明补充了静态类型信息。

此类型由运行时事件契约创建，并通过对应端的 `beta` 导出。通过 `subscribe` 回调取得实例；不要自行构造事件参数。

[ServerChatEvent](../native-events.md#serverchatevent) 的事件参数；同步分发结束后不能再写入输出字段。

## 获取方式

通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。

所属信号：`world.beforeEvents.getNativeEvent('ServerChatEvent')`.

基类：[NativeEventData](../../common/reference/NativeEventData.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [username](#username) | 可读写属性 |
| [player](#player) | 只读属性 |
| [message](#message) | 可读写属性 |
| [cancel](#cancel) | 可读写属性 |
| [bChatById](#bChatById) | 可读写属性 |
| [bForbid](#bForbid) | 可读写属性 |
| [targets](#targets) | 可读写属性 |
| [gameChatPrefix](#gameChatPrefix) | 可读写属性 |
| [gameChatPrefixColorR](#gameChatPrefixColorR) | 可读写属性 |
| [gameChatPrefixColorG](#gameChatPrefixColorG) | 可读写属性 |
| [gameChatPrefixColorB](#gameChatPrefixColorB) | 可读写属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [getNativeData](../../common/reference/NativeEventData.md#getNativeData) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [getNativeValue](../../common/reference/NativeEventData.md#getNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [nativeEventName](../../common/reference/NativeEventData.md#nativeEventName) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [setNativeValue](../../common/reference/NativeEventData.md#setNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |

## username {#username}

```python
username: Optional[str]
```

数据来源为原生字段 `username`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
玩家名称；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.username = value`。参数类型线索：`(value: str) -> None`。

在同步分发期间校验并写入原生 username 输出。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## player {#player}

```python
player: Optional[Player]
```

数据来源为原生字段 `playerId`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
玩家id；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[Player](../apis/player.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## message {#message}

```python
message: Optional[str]
```

数据来源为原生字段 `message`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
玩家发送的聊天消息内容；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.message = value`。参数类型线索：`(value: str) -> None`。

在同步分发期间校验并写入原生 message 输出。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## cancel {#cancel}

```python
cancel: bool
```

数据来源为原生字段 `cancel`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
是否取消这个聊天事件，若取消可以设置为True；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.cancel = value`。参数类型线索：`(value: bool) -> None`。

在同步分发期间校验并写入原生 cancel 输出。

写入参数 `value`：[bool](../../common/type-system.md#bool)。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## bChatById {#bChatById}

```python
bChatById: Optional[bool]
```

数据来源为原生字段 `bChatById`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
是否把聊天消息发送给指定在线玩家，而不是广播给所有在线玩家，若只发送某些玩家可以设置为True；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.bChatById = value`。参数类型线索：`(value: bool) -> None`。

在同步分发期间校验并写入原生 bChatById 输出。

写入参数 `value`：[bool](../../common/type-system.md#bool)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[bool](../../common/type-system.md#bool)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## bForbid {#bForbid}

```python
bForbid: Optional[bool]
```

数据来源为原生字段 `bForbid`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
是否禁言，仅apollo可用。true：被禁言，玩家聊天会提示“你已被管理员禁言”。；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.bForbid = value`。参数类型线索：`(value: bool) -> None`。

在同步分发期间校验并写入原生 bForbid 输出。

写入参数 `value`：[bool](../../common/type-system.md#bool)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[bool](../../common/type-system.md#bool)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## targets {#targets}

```python
targets: Optional[tuple[Player, ...]]
```

数据来源为原生字段 `toPlayerIds`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
接收聊天消息的玩家id列表，bChatById为True时生效；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.targets = value`。参数类型线索：`(value: Optional[tuple[Player, ...]]) -> None`。

在同步分发期间校验并写入原生 toPlayerIds 输出。

写入参数 `value`：[Optional](../../common/type-system.md#optional)[[tuple](../../common/type-system.md#tuple)[[Player](../apis/player.md), ...]]。

**返回类型：** [Optional](../../common/type-system.md#optional)[[tuple](../../common/type-system.md#tuple)[[Player](../apis/player.md), ...]]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## gameChatPrefix {#gameChatPrefix}

```python
gameChatPrefix: Optional[str]
```

数据来源为原生字段 `gameChatPrefix`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
设置当前玩家在网易聊天界面中的前缀，字数限制4，从字符串头部开始取。前缀文本输入非字符串格式时会被置为空。若cancel为True，会取消掉本次的前缀修改；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.gameChatPrefix = value`。参数类型线索：`(value: str) -> None`。

在同步分发期间校验并写入原生 gameChatPrefix 输出。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## gameChatPrefixColorR {#gameChatPrefixColorR}

```python
gameChatPrefixColorR: Optional[float]
```

数据来源为原生字段 `gameChatPrefixColorR`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
设置当前玩家在网易聊天界面中前缀颜色rgb的r值，范围为`[0,1]`。颜色数值输入其他格式时会被置为0。若cancel为True，会取消掉本次的颜色修改；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.gameChatPrefixColorR = value`。参数类型线索：`(value: float) -> None`。

在同步分发期间校验并写入原生 gameChatPrefixColorR 输出。

写入参数 `value`：[float](../../common/type-system.md#float)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## gameChatPrefixColorG {#gameChatPrefixColorG}

```python
gameChatPrefixColorG: Optional[float]
```

数据来源为原生字段 `gameChatPrefixColorG`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
设置当前玩家在网易聊天界面中前缀颜色rgb的g值，范围为`[0,1]`。颜色数值输入其他格式时会被置为0。若cancel为True，会取消掉本次的颜色修改；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.gameChatPrefixColorG = value`。参数类型线索：`(value: float) -> None`。

在同步分发期间校验并写入原生 gameChatPrefixColorG 输出。

写入参数 `value`：[float](../../common/type-system.md#float)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## gameChatPrefixColorB {#gameChatPrefixColorB}

```python
gameChatPrefixColorB: Optional[float]
```

数据来源为原生字段 `gameChatPrefixColorB`；仅可在同步回调内写入。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
设置当前玩家在网易聊天界面中前缀颜色rgb的b值，范围为`[0,1]`。颜色数值输入其他格式时会被置为0。若cancel为True，会取消掉本次的颜色修改；此字段可在同步回调中赋值。
:::

**访问：** 可读写。

写入方式：`instance.gameChatPrefixColorB = value`。参数类型线索：`(value: float) -> None`。

在同步分发期间校验并写入原生 gameChatPrefixColorB 输出。

写入参数 `value`：[float](../../common/type-system.md#float)。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.beforeEvents.getNativeEvent('ServerChatEvent').subscribe(on_event)

def cleanup():
    world.beforeEvents.getNativeEvent('ServerChatEvent').unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)