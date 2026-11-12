---
title: "ScriptBridgeMessage"
sidebar_label: "ScriptBridgeMessage"
---

# ScriptBridgeMessage

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/script_bridge.py`；声明补充了静态类型信息。

独立的桥接消息数据；包含命名空间标识、解码后的数据和可选的本地玩家对象。

## 获取方式

通过桥接消息回调或已注册处理器的参数取得，不自行构造。

所属信号：[system.scriptBridge.afterEvents.messageReceive](ScriptBridgeAfterEvents.md#messageReceive).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [id](#id) | 只读属性 |
| [data](#data) | 只读属性 |
| [player](#player) | 只读属性 |

## 构造器 {#constructor}

```python
ScriptBridgeMessage(identifier, data, player = None)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | 由值/所属选项确定 | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |
| `player` | 由值/所属选项确定 | [None](../type-system.md#none) | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## id {#id}

```python
id: str
```

消息或已注册处理器的命名空间标识。

**访问：** 只读。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## data {#data}

```python
data: Any
```

解码后的数据；原生引用恢复为包装对象，不直接暴露运行标识。

**访问：** 只读。

**返回类型：** [Any](../type-system.md#any)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.data
```

## player {#player}

```python
player: Optional[Union[Player, ClientPlayer]]
```

客户端为本地玩家对象；服务端桥接消息为 [None](../type-system.md#none)。

**访问：** 只读。

**返回类型：** [Optional](../type-system.md#optional)[[Union](../type-system.md#union)[[Player](../../server/apis/player.md), [ClientPlayer](../../client/reference/ClientPlayer.md)]]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.player
```

## 使用示例


```python
from ModSAPI.server.beta import system

def on_event(event):
    print(event)

system.scriptBridge.afterEvents.messageReceive.subscribe(on_event)

def cleanup():
    system.scriptBridge.afterEvents.messageReceive.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)