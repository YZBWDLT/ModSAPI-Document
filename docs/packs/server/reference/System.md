---
title: "System"
sidebar_label: "System"
---

# System

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/System.py`；声明补充了静态类型信息。

系统级事件和功能的入口。

## 获取方式

从服务端入口导入 `system` 单例。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [scriptBridge](#scriptBridge) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [beforeEvents](#beforeEvents) | 只读属性 |
| [ui](#ui) | 只读属性 |
| [afterEvents](#afterEvents) | 只读属性 |
| [run](#run) | 方法 |
| [runTimeout](#runTimeout) | 方法 |
| [runInterval](#runInterval) | 方法 |
| [clearRun](#clearRun) | 方法 |
| [sendToClient](#sendToClient) | 方法 |
| [sendToAllClients](#sendToAllClients) | 方法 |
| [getDataFromClient](#getDataFromClient) | 方法 |
| [runClientFunc](#runClientFunc) | 方法 |
| [runJob](#runJob) | 方法 |
| [waitTicks](#waitTicks) | 方法 |
| [clearJob](#clearJob) | 方法 |
| [Destroy](#Destroy) | 方法 |
| [exportFunc](#exportFunc) | 方法 |
| [importFunc](#importFunc) | 方法 |

## 构造器 {#constructor}

```python
System(namespace, systemName)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `namespace` | 由值/所属选项确定 | `必填` | 本功能独有的命名空间，避免与其他功能的持久化数据冲突。 |
| `systemName` | 由值/所属选项确定 | `必填` | 传给 [System.__init__](System.md#constructor) 的 systemName 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `ListenForEvent`, `GetLevelId`, `GetEngineNamespace`, `GetEngineSystemName`, `GetEngineCompFactory`。

## scriptBridge {#scriptBridge}

```python
scriptBridge: ScriptBridge
```

与 SAPI 双向通信的入口，支持显式处理器注册和消息通知。

**访问：** 只读。

**返回类型：** [ScriptBridge](../../common/reference/ScriptBridge.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'System has been destroyed'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.scriptBridge
```

## isValid {#isValid}

```python
isValid: bool
```

当前服务端系统是否仍可接受新的操作。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## beforeEvents {#beforeEvents}

```python
beforeEvents: SystemBeforeEvents
```

读取 `beforeEvents` 的当前值。

**访问：** 只读。

**返回类型：** [SystemBeforeEvents](SystemBeforeEvents.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.beforeEvents
```

## ui {#ui}

```python
ui: UiService
```

服务端界面入口，显示目标使用明确的玩家包装对象。

**访问：** 只读。

**返回类型：** [UiService](../../ui/reference/UiService.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'System has been destroyed'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.ui
```

## afterEvents {#afterEvents}

```python
afterEvents: SystemAfterEvents
```

系统级操作的后置事件集合。

**访问：** 只读。

**返回类型：** [SystemAfterEvents](SystemAfterEvents.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.afterEvents
```

## run {#run}

```python
run(callback: typing.Callable[[], None]) -> int
```

安排函数在后续可用时机执行，常用于延迟行为和循环。实际调度受引擎及负载影响，不保证在当前刻或下一刻执行；本适配器的时间单位及限制见调度指南。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [typing.Callable](../../common/type-system.md#callable)[[], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_run(instance, callback):
    return instance.run(callback)
```

## runTimeout {#runTimeout}

```python
runTimeout(callback: typing.Callable[[], None], tickDelay: int = 1) -> int
```

在 tickDelay 指定的延迟后执行代码。

:::note 当前实现说明
原生延迟按 0.05 秒乘请求值换算；服务端负值限制为零，不代表微软执行阶段。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [typing.Callable](../../common/type-system.md#callable)[[], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |
| `tickDelay` | [int](../../common/type-system.md#int) | `1` | 延迟请求单位，每单位换算 0.05 秒；具体整数/下限校验见所属端说明。 |

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'System has been destroyed'` |
| [TypeError](../../common/type-system.md#typeerror) | `'callback must be callable'` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Engine failed to create timer'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `AddTimer`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_runTimeout(instance, callback):
    return instance.runTimeout(callback)
```

## runInterval {#runInterval}

```python
runInterval(callback: typing.Callable[[], None], tickInterval: int = 1) -> int
```

按固定间隔执行代码。

:::note 当前实现说明
原生周期按 0.05 秒换算，服务端最小周期为一个请求单位。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [typing.Callable](../../common/type-system.md#callable)[[], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |
| `tickInterval` | [int](../../common/type-system.md#int) | `1` | 周期请求单位，每单位换算 0.05 秒；不是原生渲染帧数。 |

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'System has been destroyed'` |
| [TypeError](../../common/type-system.md#typeerror) | `'callback must be callable'` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Engine failed to create repeated timer'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `AddRepeatedTimer`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_runInterval(instance, callback):
    return instance.runInterval(callback)
```

## clearRun {#clearRun}

```python
clearRun(runId: int)
```

取消此前通过 [System.run](System.md#run) 等方法安排的任务。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `runId` | [int](../../common/type-system.md#int) | `必填` | run/runTimeout/runInterval 返回的任务标识，不能混用原生计时器 ID。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `CancelTimer`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clearRun(instance, runId):
    return instance.clearRun(runId)
```

## sendToClient {#sendToClient}

```python
sendToClient(player, eventName: str, data: typing.Any = None)
```

向客户端发送数据。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | 由值/所属选项确定 | `必填` | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |
| `eventName` | [str](../../common/type-system.md#str) | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |
| `data` | [typing.Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'System has been destroyed'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `NotifyToClient`, `NotifyToMultiClients`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_sendToClient(instance, player, eventName):
    return instance.sendToClient(player, eventName)
```

## sendToAllClients {#sendToAllClients}

```python
sendToAllClients(eventName: str, data: typing.Any)
```

向全部客户端发送数据。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `eventName` | [str](../../common/type-system.md#str) | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |
| `data` | [typing.Any](../../common/type-system.md#any) | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'System has been destroyed'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `BroadcastToAllClient`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_sendToAllClients(instance, eventName, data):
    return instance.sendToAllClients(eventName, data)
```

## getDataFromClient {#getDataFromClient}

```python
getDataFromClient(player: Player | str, dataName: str, data: typing.Any = None, timeout: float = 10.0) -> Promise[typing.Any]
```

请求单次响应；timeout 单位为秒。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | [Player](../apis/player.md) \| [str](../../common/type-system.md#str) | `必填` | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |
| `dataName` | [str](../../common/type-system.md#str) | `必填` | 请求的数据通道名称，响应方需事先注册同名处理器。 |
| `data` | [typing.Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |
| `timeout` | [float](../../common/type-system.md#float) | `10.0` | 等待秒数；有限且大于零，默认 10 秒。 |

**返回类型：** [Promise](../../common/reference/Promise.md)[[typing.Any](../../common/type-system.md#any)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'System has been destroyed'` |
| [TypeError](../../common/type-system.md#typeerror) | `'player should be a Player \| str.'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDataFromClient(instance, player, dataName):
    return instance.getDataFromClient(player, dataName)
```

## runClientFunc {#runClientFunc}

```python
runClientFunc(player, funcName, *args, **kwargs)
```

请求在客户端执行函数。funcName 为通过 clientCallable 在客户端注册的函数名。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | 由值/所属选项确定 | `必填` | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |
| `funcName` | 由值/所属选项确定 | `必填` | 传给 [System.runClientFunc](System.md#runClientFunc) 的 funcName 参数；结合上方功能说明和下方调用示例使用。 |
| `*args` | 可变参数 | `可省略` | 传给 [System.runClientFunc](System.md#runClientFunc) 的 *args 参数；结合上方功能说明和下方调用示例使用。 |
| `**kwargs` | 可变参数 | `可省略` | 传给 [System.runClientFunc](System.md#runClientFunc) 的 **kwargs 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_runClientFunc(instance, player, funcName, *args, **kwargs):
    return instance.runClientFunc(player, funcName, *args, **kwargs)
```

## runJob {#runJob}

```python
runJob(generator: typing.Iterator) -> int
```

执行 `runJob` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `generator` | [typing.Iterator](../../common/type-system.md#iterator) | `必填` | 可迭代的生成器任务；每一步应及时 yield。 |

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'System has been destroyed'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_runJob(instance, generator):
    return instance.runJob(generator)
```

## waitTicks {#waitTicks}

```python
waitTicks(ticks: int) -> Promise[None]
```

执行 `waitTicks` 操作。参数形态和结果约定如下。

:::note 当前实现说明
返回本库 [Promise](../../common/reference/Promise.md)；完成回调不接收参数。销毁时拒绝未完成等待。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `ticks` | [int](../../common/type-system.md#int) | `必填` | 等待请求单位，正整数；每单位换算 0.05 秒。 |

**返回类型：** [Promise](../../common/reference/Promise.md)[[None](../../common/type-system.md#none)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'ticks must be a positive integer'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_waitTicks(instance, ticks):
    return instance.waitTicks(ticks)
```

## clearJob {#clearJob}

```python
clearJob(jobId: int)
```

移除或清理 `clearJob` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `jobId` | [int](../../common/type-system.md#int) | `必填` | runJob 返回的任务标识。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clearJob(instance, jobId):
    return instance.clearJob(jobId)
```

## Destroy {#Destroy}

```python
Destroy()
```

释放所拥有的资源；单项清理失败不会阻止其余清理。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `CancelTimer`, `UnListenForEvent`, `GetEngineNamespace`, `GetEngineSystemName`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_Destroy(instance):
    return instance.Destroy()
```

## exportFunc {#exportFunc}

```python
exportFunc(identifier: str, callback: typing.Callable)
```

导出可供其他系统或模块调用的函数。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `callback` | [typing.Callable](../../common/type-system.md#callable) | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_exportFunc(instance, identifier, callback):
    return instance.exportFunc(identifier, callback)
```

## importFunc {#importFunc}

```python
importFunc(identifier: str) -> typing.Callable | None
```

导入其他系统或模块导出的函数。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |

**返回类型：** [typing.Callable](../../common/type-system.md#callable) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_importFunc(instance, identifier):
    return instance.importFunc(identifier)
```

## 使用示例


```python
from __future__ import print_function

from ModSAPI.server.beta import system

run_id = system.runInterval(lambda: print("tick"), 20)
system.runTimeout(lambda: system.clearRun(run_id), 100)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)