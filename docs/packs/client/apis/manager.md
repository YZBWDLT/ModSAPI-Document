---
title: "Client"
sidebar_label: "Client"
---

# Client

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Client.py`；声明补充了静态类型信息。

客户端统一入口。网易扩展遵循 SAPI 的命名和选项风格。原生服务属于当前会话；Destroy 后操作会抛出 [InvalidClientObjectError](../../common/reference/InvalidClientObjectError.md)。身份属性和 afterEvents 仍可读取以便清理；原生操作异常保留方法名和失败码。

## 获取方式

从客户端入口导入 `client` 单例。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [scriptBridge](#scriptBridge) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [levelId](#levelId) | 只读属性 |
| [localPlayer](#localPlayer) | 只读属性 |
| [camera](#camera) | 只读属性 |
| [ui](#ui) | 只读属性 |
| [afterEvents](#afterEvents) | 只读属性 |
| [beforeEvents](#beforeEvents) | 只读属性 |
| [screen](#screen) | 只读属性 |
| [audio](#audio) | 只读属性 |
| [getStorage](#getStorage) | 方法 |
| [registerQueryVariable](#registerQueryVariable) | 方法 |
| [unregisterQueryVariable](#unregisterQueryVariable) | 方法 |
| [run](#run) | 方法 |
| [runTimeout](#runTimeout) | 方法 |
| [runInterval](#runInterval) | 方法 |
| [clearRun](#clearRun) | 方法 |
| [waitTicks](#waitTicks) | 方法 |
| [sendToServer](#sendToServer) | 方法 |
| [getDataFromServer](#getDataFromServer) | 方法 |
| [runServerFunc](#runServerFunc) | 方法 |
| [getEntity](#getEntity) | 方法 |
| [spawnEntity](#spawnEntity) | 方法 |
| [spawnParticle](#spawnParticle) | 方法 |
| [spawnDynamicParticle](#spawnDynamicParticle) | 方法 |
| [Destroy](#Destroy) | 方法 |

## 构造器 {#constructor}

```python
Client(namespace: str, systemName: str) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `namespace` | [str](../../common/type-system.md#str) | `必填` | 本功能独有的命名空间，避免与其他功能的持久化数据冲突。 |
| `systemName` | [str](../../common/type-system.md#str) | `必填` | 传给 [Client.__init__](manager.md#constructor) 的 systemName 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `WeakSet`。

## scriptBridge {#scriptBridge}

```python
scriptBridge: ScriptBridge
```

此本地客户端与 SAPI 双向通信的入口；消息中的玩家使用包装对象。

**访问：** 只读。

**返回类型：** [ScriptBridge](../../common/reference/ScriptBridge.md)。静态声明不替代本页的实现限制。

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

当前客户端会话是否仍可使用。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## levelId {#levelId}

```python
levelId: str
```

当前世界的运行标识。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.levelId
```

## localPlayer {#localPlayer}

```python
localPlayer: ClientPlayer
```

本地玩家状态和显示控制。

**访问：** 只读。

**返回类型：** [ClientPlayer](../reference/ClientPlayer.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.localPlayer
```

## camera {#camera}

```python
camera: ClientCamera
```

当前客户端会话的相机服务。

**访问：** 只读。

**返回类型：** [ClientCamera](../reference/ClientCamera.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.camera
```

## ui {#ui}

```python
ui: UiService
```

本地界面、响应式状态和主题表单的统一入口。

**访问：** 只读。

**返回类型：** [UiService](../../ui/reference/UiService.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.ui
```

## afterEvents {#afterEvents}

```python
afterEvents: ClientAfterEvents
```

原生后置事件信号及现有客户端、服务端消息信号。开发包分发时同步执行原生信号，不保证与服务端 Script API 的执行阶段一致。

**访问：** 只读。

**返回类型：** [ClientAfterEvents](../reference/ClientAfterEvents.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.afterEvents
```

## beforeEvents {#beforeEvents}

```python
beforeEvents: ClientBeforeEvents
```

待执行操作及可写输出的同步钩子。取消及输出修改必须在回调内完成；延迟写入会抛出 [RuntimeError](../../common/type-system.md#runtimeerror)。原生的双端要求仍然适用；此处不会强制实行微软的受限执行模式。

**访问：** 只读。

**返回类型：** [ClientBeforeEvents](../reference/ClientBeforeEvents.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.beforeEvents
```

## screen {#screen}

```python
screen: Screen
```

原生屏幕注册及界面栈操作。

**访问：** 只读。

**返回类型：** [Screen](../reference/Screen.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.screen
```

## audio {#audio}

```python
audio: Audio
```

本地场景音效和背景音乐。

**访问：** 只读。

**返回类型：** [Audio](../reference/Audio.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.audio
```

## getStorage {#getStorage}

```python
getStorage(namespace: str, options: ClientStorageOptions | None = None) -> KeyValueStorage
```

打开本地 JSON 配置存储，支持 isGlobal 选项，默认为 False。世界范围文件仅属于本设备和存档，不与服务端同步；全局文件由本机各存档共享。命名空间编码避免名称冲突，并符合开发包对文件名字符的限制。

:::note 当前实现说明
isGlobal=False 为本机存档配置，True 为本机全局配置；不会自动同步服务端。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `namespace` | [str](../../common/type-system.md#str) | `必填` | 本功能独有的命名空间，避免与其他功能的持久化数据冲突。 |
| `options` | [ClientStorageOptions](../reference/ClientStorageOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [KeyValueStorage](../../common/reference/KeyValueStorage.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetConfigData`, `SetConfigData`, `GetEngineCompFactory`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getStorage(instance, namespace):
    return instance.getStorage(namespace)
```

## registerQueryVariable {#registerQueryVariable}

```python
registerQueryVariable(name: str, defaultValue: float = 0) -> None
```

注册用于本地渲染的 query.mod.* 节点，属于网易扩展。请使用模组专属后缀避免冲突。数值采用原生单精度浮点数；关闭时移除本实例持有的注册项。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../../common/type-system.md#str) | `必填` | 传给 [Client.registerQueryVariable](manager.md#registerQueryVariable) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `defaultValue` | [float](../../common/type-system.md#float) | `0` | 缺省值；具体是缺失键、初始控件值还是原生默认值取决于所属接口。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Query variable is already registered by this client'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `Register`, `GetEngineCompFactory`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_registerQueryVariable(instance, name):
    return instance.registerQueryVariable(name)
```

## unregisterQueryVariable {#unregisterQueryVariable}

```python
unregisterQueryVariable(name: str) -> None
```

移除本实例持有的注册项；拒绝移除其他脚本持有的名称。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../../common/type-system.md#str) | `必填` | 传给 [Client.unregisterQueryVariable](manager.md#unregisterQueryVariable) 的 name 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Query variable is not owned by this client'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `UnRegister`, `GetEngineCompFactory`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_unregisterQueryVariable(instance, name):
    return instance.unregisterQueryVariable(name)
```

## run {#run}

```python
run(callback: Callable[[], None]) -> int
```

使用一个原生时间单位安排单次回调，每单位为 1/20 秒。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../../common/type-system.md#callable)[[], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

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
runTimeout(callback: Callable[[], None], tickDelay: int = 1) -> int
```

安排单次回调；tickDelay 为非负整数，每单位为 1/20 秒。

:::note 当前实现说明
tickDelay 为非负整数；一个请求单位换算为 0.05 秒，不是渲染帧。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../../common/type-system.md#callable)[[], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |
| `tickDelay` | [int](../../common/type-system.md#int) | `1` | 延迟请求单位，每单位换算 0.05 秒；具体整数/下限校验见所属端说明。 |

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_runTimeout(instance, callback):
    return instance.runTimeout(callback)
```

## runInterval {#runInterval}

```python
runInterval(callback: Callable[[], None], tickInterval: int = 1) -> int
```

安排周期回调；tickInterval 必须为正整数。

:::note 当前实现说明
tickInterval 为正整数；一个请求单位换算为 0.05 秒。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../../common/type-system.md#callable)[[], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |
| `tickInterval` | [int](../../common/type-system.md#int) | `1` | 周期请求单位，每单位换算 0.05 秒；不是原生渲染帧数。 |

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_runInterval(instance, callback):
    return instance.runInterval(callback)
```

## clearRun {#clearRun}

```python
clearRun(runId: int) -> None
```

取消本实例持有的计时器；忽略未知或已完成的任务标识。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `runId` | [int](../../common/type-system.md#int) | `必填` | run/runTimeout/runInterval 返回的任务标识，不能混用原生计时器 ID。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clearRun(instance, runId):
    return instance.clearRun(runId)
```

## waitTicks {#waitTicks}

```python
waitTicks(ticks: int) -> Promise[None]
```

返回在指定正数时间单位后完成的 [Promise](../../common/reference/Promise.md)；会话关闭时拒绝该异步结果。

:::note 当前实现说明
ticks 为正整数；返回本库 [Promise](../../common/reference/Promise.md)，销毁会拒绝未完成等待。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `ticks` | [int](../../common/type-system.md#int) | `必填` | 等待请求单位，正整数；每单位换算 0.05 秒。 |

**返回类型：** [Promise](../../common/reference/Promise.md)[[None](../../common/type-system.md#none)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_waitTicks(instance, ticks):
    return instance.waitTicks(ticks)
```

## sendToServer {#sendToServer}

```python
sendToServer(eventName: str, data: Any = None) -> None
```

发送具名自定义事件；data 必须可由网易远程调用机制序列化。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `eventName` | [str](../../common/type-system.md#str) | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |
| `data` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `NotifyToServer`, `GetLocalPlayerId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_sendToServer(instance, eventName):
    return instance.sendToServer(eventName)
```

## getDataFromServer {#getDataFromServer}

```python
getDataFromServer(dataName: str, data: Any = None, timeout: float = 10.0) -> Promise[Any]
```

请求单次响应。timeout 单位为秒；超时或发送失败会使异步结果失败。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `dataName` | [str](../../common/type-system.md#str) | `必填` | 请求的数据通道名称，响应方需事先注册同名处理器。 |
| `data` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |
| `timeout` | [float](../../common/type-system.md#float) | `10.0` | 等待秒数；有限且大于零，默认 10 秒。 |

**返回类型：** [Promise](../../common/reference/Promise.md)[[Any](../../common/type-system.md#any)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEngineCompFactory`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDataFromServer(instance, dataName):
    return instance.getDataFromServer(dataName)
```

## runServerFunc {#runServerFunc}

```python
runServerFunc(funcName: str, *args, **kwargs) -> Promise[Any]
```

请求调用服务端显式导出的函数。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `funcName` | [str](../../common/type-system.md#str) | `必填` | 传给 [Client.runServerFunc](manager.md#runServerFunc) 的 funcName 参数；结合上方功能说明和下方调用示例使用。 |
| `*args` | 可变参数 | `可省略` | 传给 [Client.runServerFunc](manager.md#runServerFunc) 的 *args 参数；结合上方功能说明和下方调用示例使用。 |
| `**kwargs` | 可变参数 | `可省略` | 传给 [Client.runServerFunc](manager.md#runServerFunc) 的 **kwargs 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Promise](../../common/reference/Promise.md)[[Any](../../common/type-system.md#any)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_runServerFunc(instance, funcName, *args, **kwargs):
    return instance.runServerFunc(funcName, *args, **kwargs)
```

## getEntity {#getEntity}

```python
getEntity(entityId: str) -> ClientEntity | None
```

返回可见实体的包装对象；标识不存在时返回 [None](../../common/type-system.md#none)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `entityId` | [str](../../common/type-system.md#str) | `必填` | 实体运行 ID；跨回调使用前重新确认实体有效性。 |

**返回类型：** [ClientEntity](../reference/ClientEntity.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEntity(instance, entityId):
    return instance.getEntity(entityId)
```

## spawnEntity {#spawnEntity}

```python
spawnEntity(typeId: str, location: VectorLike, options: ClientEntitySpawnOptions | None = None) -> ClientEntity
```

创建可移除的本地实体，支持 rotation 选项，以俯仰角和偏航角表示。本地实体不会保存，原生维度切换会将其移除。不支持的实体模型或创建失败会抛出异常。

:::note 当前实现说明
只创建本地实体，不保存；只有此方法返回的拥有者句柄可以 remove。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `typeId` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的实体、物品或资源类型名称。 |
| `location` | [VectorLike](../../common/type-aliases.md#vectorlike) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `options` | [ClientEntitySpawnOptions](../reference/ClientEntitySpawnOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [ClientEntity](../reference/ClientEntity.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'rotation must contain pitch and yaw'` |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'CreateClientEntityByTypeStr'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_spawnEntity(instance, typeId, location):
    return instance.spawnEntity(typeId, location)
```

## spawnParticle {#spawnParticle}

```python
spawnParticle(typeId: str, location: VectorLike, options: ClientParticleOptions | None = None) -> Particle
```

创建粒子发射器，支持 rotation 和标量字典 molangVariables。在创建前校验全部变量；初始化失败时移除刚创建的发射器，并保留原始异常。

:::note 当前实现说明
创建原生粒子发射器，需要资源定义存在；原生 0 表示创建失败。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `typeId` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的实体、物品或资源类型名称。 |
| `location` | [VectorLike](../../common/type-aliases.md#vectorlike) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `options` | [ClientParticleOptions](../reference/ClientParticleOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [Particle](../reference/Particle.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'molangVariables must be a dictionary'` |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'Create'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEngineCompFactory`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_spawnParticle(instance, typeId, location):
    return instance.spawnParticle(typeId, location)
```

## spawnDynamicParticle {#spawnDynamicParticle}

```python
spawnDynamicParticle(pattern: DynamicParticlePattern, location: VectorLike, options: DynamicParticleOptions | None = None) -> DynamicParticle
```

创建表达式驱动的线或点绘图；选项参见 [DynamicParticle](../reference/DynamicParticle.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `pattern` | [DynamicParticlePattern](../reference/DynamicParticlePattern.md) | `必填` | 传给 [Client.spawnDynamicParticle](manager.md#spawnDynamicParticle) 的 pattern 参数；结合上方功能说明和下方调用示例使用。 |
| `location` | [VectorLike](../../common/type-aliases.md#vectorlike) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `options` | [DynamicParticleOptions](../reference/DynamicParticleOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [DynamicParticle](../reference/DynamicParticle.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_spawnDynamicParticle(instance, pattern, location):
    return instance.spawnDynamicParticle(pattern, location)
```

## Destroy {#Destroy}

```python
Destroy() -> None
```

释放本实例持有的订阅、等待任务、计时器和本地对象引用。各项清理失败独立记录。由引擎管理自然结束的资源，包括声音，仍由引擎负责；不会发送全局停止指令。重复调用无额外影响。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_Destroy(instance):
    return instance.Destroy()
```

## 使用示例


```python
from ModSAPI.client.beta import client

print(client.localPlayer.id)
client.localPlayer.sendToast("Ready", "Example")
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)