---
title: "ScriptBridge"
sidebar_label: "ScriptBridge"
---

# ScriptBridge

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/script_bridge.py`；声明补充了静态类型信息。

双向 SAPI 通信入口，读写数据使用副本，只有显式注册的处理器才能调用。通过 [system.scriptBridge](../../server/reference/System.md#scriptBridge) 或 [client.scriptBridge](../../client/apis/manager.md#scriptBridge) 获取。request 返回本库的 [Promise](Promise.md)；两端 timeoutTicks 均按每单位 1/20 秒换算。不会执行任意源代码。

## 获取方式

使用 [system.scriptBridge](../../server/reference/System.md#scriptBridge) 或 [client.scriptBridge](../../client/apis/manager.md#scriptBridge)；由对应端的生命周期管理，不自行构造。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [isValid](#isValid) | 只读属性 |
| [afterEvents](#afterEvents) | 只读属性 |
| [sendMessage](#sendMessage) | 方法 |
| [request](#request) | 方法 |
| [registerHandler](#registerHandler) | 方法 |
| [unregisterHandler](#unregisterHandler) | 方法 |
| [dispose](#dispose) | 方法 |

## 构造器 {#constructor}

```python
ScriptBridge(transport, referenceEncoder = None, referenceDecoder = None, player = None)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

:::note 当前实现说明
由 [system.scriptBridge](../../server/reference/System.md#scriptBridge) 或 [client.scriptBridge](../../client/apis/manager.md#scriptBridge) 创建并持有；业务代码不直接构造传输器。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `transport` | 由值/所属选项确定 | `必填` | 传给 [ScriptBridge.__init__](ScriptBridge.md#constructor) 的 transport 参数；结合上方功能说明和下方调用示例使用。 |
| `referenceEncoder` | 由值/所属选项确定 | [None](../type-system.md#none) | 传给 [ScriptBridge.__init__](ScriptBridge.md#constructor) 的 referenceEncoder 参数；结合上方功能说明和下方调用示例使用。 |
| `referenceDecoder` | 由值/所属选项确定 | [None](../type-system.md#none) | 传给 [ScriptBridge.__init__](ScriptBridge.md#constructor) 的 referenceDecoder 参数；结合上方功能说明和下方调用示例使用。 |
| `player` | 由值/所属选项确定 | [None](../type-system.md#none) | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## isValid {#isValid}

```python
isValid: bool
```

此入口是否仍接受本地操作。

**访问：** 只读。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## afterEvents {#afterEvents}

```python
afterEvents: ScriptBridgeAfterEvents
```

接收消息的信号集合；保留回调引用以便注销。

**访问：** 只读。

**返回类型：** [ScriptBridgeAfterEvents](ScriptBridgeAfterEvents.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.afterEvents
```

## sendMessage {#sendMessage}

```python
sendMessage(id: str, data: Any = None) -> Promise
```

发送通知；全部原生分包发送完成后完成异步结果。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `id` | [str](../type-system.md#str) | `必填` | 运行标识或类型标识，按本成员的说明传入。 |
| `data` | [Any](../type-system.md#any) | [None](../type-system.md#none) | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回类型：** [Promise](Promise.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_sendMessage(instance, id):
    return instance.sendMessage(id)
```

## request {#request}

```python
request(id: str, data: Any = None, options: Optional[dict] = None) -> Promise
```

请求 SAPI 中已注册的处理器，返回结果解码后的 [Promise](Promise.md)。options.timeoutTicks 为 1–1200 的整数，默认 200。超时、断线、原生发送失败或销毁会使异步结果失败；超时无法撤销远端已开始执行的操作。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `id` | [str](../type-system.md#str) | `必填` | 运行标识或类型标识，按本成员的说明传入。 |
| `data` | [Any](../type-system.md#any) | [None](../type-system.md#none) | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |
| `options` | [Optional](../type-system.md#optional)[[dict](../type-system.md#dict)] | [None](../type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [Promise](Promise.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../type-system.md#typeerror) | `'options may contain only timeoutTicks'` |
| [ValueError](../type-system.md#valueerror) | `'timeoutTicks must be an integer from 1 through 1200'` |
| [ScriptBridgeError](ScriptBridgeError.md) | `'Too many pending requests'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_request(instance, id):
    return instance.request(id)
```

## registerHandler {#registerHandler}

```python
registerHandler(id: str, callback: Callable[[ScriptBridgeMessage], Any]) -> None
```

显式注册处理器；回调参数为 [ScriptBridgeMessage](ScriptBridgeMessage.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `id` | [str](../type-system.md#str) | `必填` | 运行标识或类型标识，按本成员的说明传入。 |
| `callback` | [Callable](../type-system.md#callable)[[[ScriptBridgeMessage](ScriptBridgeMessage.md)], [Any](../type-system.md#any)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../type-system.md#typeerror) | `'callback must be callable'` |
| [ScriptBridgeError](ScriptBridgeError.md) | `'Handler already registered: ' + id` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_registerHandler(instance, id, callback):
    return instance.registerHandler(id, callback)
```

## unregisterHandler {#unregisterHandler}

```python
unregisterHandler(id: str) -> bool
```

移除处理器，并返回该标识是否原本存在。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `id` | [str](../type-system.md#str) | `必填` | 运行标识或类型标识，按本成员的说明传入。 |

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_unregisterHandler(instance, id):
    return instance.unregisterHandler(id)
```

## dispose {#dispose}

```python
dispose() -> None
```

使待完成请求失败，并释放此入口持有的处理器、信号订阅和原生传输资源。

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_dispose(instance):
    return instance.dispose()
```

## 使用示例


```python
from ModSAPI.server.beta import system

def echo(event):
    return event.data

system.scriptBridge.registerHandler("example:echo", echo)

def cleanup():
    system.scriptBridge.unregisterHandler("example:echo")
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)