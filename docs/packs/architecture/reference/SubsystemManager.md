---
title: "SubsystemManager"
sidebar_label: "SubsystemManager"
---

import ApiFieldAnchor from '@docusaurus/Link';

# SubsystemManager

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/subsystem.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-registeredSubsystems" />`registeredSubsystems` | 由运行时值确定 | `[]` |  |
| <ApiFieldAnchor id="field-client" />`client` | 由运行时值确定 | [None](../../common/type-system.md#none) |  |
| <ApiFieldAnchor id="field-server" />`server` | 由运行时值确定 | [None](../../common/type-system.md#none) |  |
| <ApiFieldAnchor id="field-rawEngine" />`rawEngine` | 由运行时值确定 | [None](../../common/type-system.md#none) |  |
| <ApiFieldAnchor id="field-rawSysName" />`rawSysName` | 由运行时值确定 | [None](../../common/type-system.md#none) |  |
| <ApiFieldAnchor id="field-clientSubs" />`clientSubs` | 由运行时值确定 | `{}` |  |
| <ApiFieldAnchor id="field-serverSubs" />`serverSubs` | 由运行时值确定 | `{}` |  |
| <ApiFieldAnchor id="field-clientListeners" />`clientListeners` | 由运行时值确定 | `[]` |  |
| <ApiFieldAnchor id="field-serverListeners" />`serverListeners` | 由运行时值确定 | `[]` |  |
| <ApiFieldAnchor id="field-engine" />`engine` | 由运行时值确定 | `engine` |  |
| <ApiFieldAnchor id="field-sysName" />`sysName` | 由运行时值确定 | `sysName` |  |
| <ApiFieldAnchor id="field-system" />`system` | 由运行时值确定 | `system` |  |
| <ApiFieldAnchor id="field-lastTickTime" />`lastTickTime` | 由运行时值确定 | `time.time()` |  |
| <ApiFieldAnchor id="field-lastTickTimeServer" />`lastTickTimeServer` | 由运行时值确定 | `time.time()` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [getInst](#getInst) | 静态/类方法 |
| [createClientSystem](#createClientSystem) | 静态/类方法 |
| [createServerSystem](#createServerSystem) | 静态/类方法 |
| [createClient](#createClient) | 静态/类方法 |
| [createServer](#createServer) | 静态/类方法 |
| [__init__](#constructor) | 构造器 |
| [destroy](#destroy) | 方法 |
| [getSubsystems](#getSubsystems) | 方法 |
| [appendAllSubsystems](#appendAllSubsystems) | 方法 |
| [startTicking](#startTicking) | 方法 |
| [addSubsystem](#addSubsystem) | 方法 |
| [addSubsystemInst](#addSubsystemInst) | 方法 |
| [getSubsystem](#getSubsystem) | 方法 |
| [removeSubsystem](#removeSubsystem) | 方法 |
| [registerSubsystem](#registerSubsystem) | 静态/类方法 |
| [unregisterSubsystems](#unregisterSubsystems) | 静态/类方法 |
| [tickServer](#tickServer) | 方法 |
| [tickClient](#tickClient) | 方法 |
| [tickRender](#tickRender) | 方法 |
| [addListener](#addListener) | 方法 |
| [removeListener](#removeListener) | 方法 |

## getInst {#getInst}

```python
getInst()
```

读取 `getInst` 操作。参数形态和结果约定如下。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getInst(type_object):
    return type_object.getInst()
```

## createClientSystem {#createClientSystem}

```python
createClientSystem(engine, sysName, clsPath)
```

创建或登记 `createClientSystem` 操作。原生实现使用 `GetEngineNamespace`, `GetEngineSystemName`, `RegisterSystem`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `engine` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.createClientSystem](SubsystemManager.md#createClientSystem) 的 engine 参数；结合上方功能说明和下方调用示例使用。 |
| `sysName` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.createClientSystem](SubsystemManager.md#createClientSystem) 的 sysName 参数；结合上方功能说明和下方调用示例使用。 |
| `clsPath` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.createClientSystem](SubsystemManager.md#createClientSystem) 的 clsPath 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEngineNamespace`, `GetEngineSystemName`, `RegisterSystem`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createClientSystem(type_object, engine, sysName, clsPath):
    return type_object.createClientSystem(engine, sysName, clsPath)
```

## createServerSystem {#createServerSystem}

```python
createServerSystem(engine, sysName, clsPath)
```

创建或登记 `createServerSystem` 操作。原生实现使用 `GetEngineNamespace`, `GetEngineSystemName`, `RegisterSystem`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `engine` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.createServerSystem](SubsystemManager.md#createServerSystem) 的 engine 参数；结合上方功能说明和下方调用示例使用。 |
| `sysName` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.createServerSystem](SubsystemManager.md#createServerSystem) 的 sysName 参数；结合上方功能说明和下方调用示例使用。 |
| `clsPath` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.createServerSystem](SubsystemManager.md#createServerSystem) 的 clsPath 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEngineNamespace`, `GetEngineSystemName`, `RegisterSystem`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createServerSystem(type_object, engine, sysName, clsPath):
    return type_object.createServerSystem(engine, sysName, clsPath)
```

## createClient {#createClient}

```python
createClient(engine, sysName)
```

创建或登记 `createClient` 操作。原生实现使用 `GetEngineNamespace`, `GetEngineSystemName`, `RegisterSystem`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `engine` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.createClient](SubsystemManager.md#createClient) 的 engine 参数；结合上方功能说明和下方调用示例使用。 |
| `sysName` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.createClient](SubsystemManager.md#createClient) 的 sysName 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEngineNamespace`, `GetEngineSystemName`, `RegisterSystem`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createClient(type_object, engine, sysName):
    return type_object.createClient(engine, sysName)
```

## createServer {#createServer}

```python
createServer(engine, sysName)
```

创建或登记 `createServer` 操作。原生实现使用 `GetEngineNamespace`, `GetEngineSystemName`, `RegisterSystem`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `engine` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.createServer](SubsystemManager.md#createServer) 的 engine 参数；结合上方功能说明和下方调用示例使用。 |
| `sysName` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.createServer](SubsystemManager.md#createServer) 的 sysName 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEngineNamespace`, `GetEngineSystemName`, `RegisterSystem`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createServer(type_object, engine, sysName):
    return type_object.createServer(engine, sysName)
```

## 构造器 {#constructor}

```python
SubsystemManager(system, engine, sysName)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `system` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.__init__](SubsystemManager.md#constructor) 的 system 参数；结合上方功能说明和下方调用示例使用。 |
| `engine` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.__init__](SubsystemManager.md#constructor) 的 engine 参数；结合上方功能说明和下方调用示例使用。 |
| `sysName` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.__init__](SubsystemManager.md#constructor) 的 sysName 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEngineNamespace`, `GetEngineSystemName`, `AddTimer`, `GetLevelId`, `GetEngineCompFactory`。

## destroy {#destroy}

```python
destroy()
```

取消启动流程，并释放所拥有的全部子系统和引擎监听器。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `CancelTimer`, `UnListenForEvent`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_destroy(instance):
    return instance.destroy()
```

## getSubsystems {#getSubsystems}

```python
getSubsystems()
```

读取 `getSubsystems` 操作。参数形态和结果约定如下。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getSubsystems(instance):
    return instance.getSubsystems()
```

## appendAllSubsystems {#appendAllSubsystems}

```python
appendAllSubsystems(isServer)
```

执行 `appendAllSubsystems` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `isServer` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.appendAllSubsystems](SubsystemManager.md#appendAllSubsystems) 的 isServer 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_appendAllSubsystems(instance, isServer):
    return instance.appendAllSubsystems(isServer)
```

## startTicking {#startTicking}

```python
startTicking(isServer)
```

执行 `startTicking` 操作。原生实现使用 `ListenForEvent`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `isServer` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.startTicking](SubsystemManager.md#startTicking) 的 isServer 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Subsystem manager has been destroyed'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `ListenForEvent`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_startTicking(instance, isServer):
    return instance.startTicking(isServer)
```

## addSubsystem {#addSubsystem}

```python
addSubsystem(subsystemCls)
```

创建或登记 `addSubsystem` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `subsystemCls` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.addSubsystem](SubsystemManager.md#addSubsystem) 的 subsystemCls 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Subsystem manager has been destroyed'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Subsystem name is already registered'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addSubsystem(instance, subsystemCls):
    return instance.addSubsystem(subsystemCls)
```

## addSubsystemInst {#addSubsystemInst}

```python
addSubsystemInst(subsystem)
```

创建或登记 `addSubsystemInst` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `subsystem` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.addSubsystemInst](SubsystemManager.md#addSubsystemInst) 的 subsystem 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addSubsystemInst(instance, subsystem):
    return instance.addSubsystemInst(subsystem)
```

## getSubsystem {#getSubsystem}

```python
getSubsystem(subsystemCls: object) -> 'Subsystem'
```

读取 `getSubsystem` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `subsystemCls` | [object](../../common/type-system.md#object) | `必填` | 传给 [SubsystemManager.getSubsystem](SubsystemManager.md#getSubsystem) 的 subsystemCls 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Subsystem](Subsystem.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getSubsystem(instance, subsystemCls):
    return instance.getSubsystem(subsystemCls)
```

## removeSubsystem {#removeSubsystem}

```python
removeSubsystem(subsystemCls)
```

移除或清理 `removeSubsystem` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `subsystemCls` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.removeSubsystem](SubsystemManager.md#removeSubsystem) 的 subsystemCls 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeSubsystem(instance, subsystemCls):
    return instance.removeSubsystem(subsystemCls)
```

## registerSubsystem {#registerSubsystem}

```python
registerSubsystem(subsystem)
```

创建或登记 `registerSubsystem` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `subsystem` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.registerSubsystem](SubsystemManager.md#registerSubsystem) 的 subsystem 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_registerSubsystem(type_object, subsystem):
    return type_object.registerSubsystem(subsystem)
```

## unregisterSubsystems {#unregisterSubsystems}

```python
unregisterSubsystems()
```

执行 `unregisterSubsystems` 操作。参数形态和结果约定如下。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_unregisterSubsystems(type_object):
    return type_object.unregisterSubsystems()
```

## tickServer {#tickServer}

```python
tickServer(data = None)
```

执行 `tickServer` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_tickServer(instance):
    return instance.tickServer()
```

## tickClient {#tickClient}

```python
tickClient(data = None)
```

执行 `tickClient` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_tickClient(instance):
    return instance.tickClient()
```

## tickRender {#tickRender}

```python
tickRender(_)
```

执行 `tickRender` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `_` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.tickRender](SubsystemManager.md#tickRender) 的 _ 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_tickRender(instance, _):
    return instance.tickRender(_)
```

## addListener {#addListener}

```python
addListener(event, fn, isCustomEvent = False)
```

创建或登记 `addListener` 操作。原生实现使用 `ListenForEvent`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `event` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.addListener](SubsystemManager.md#addListener) 的 event 参数；结合上方功能说明和下方调用示例使用。 |
| `fn` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.addListener](SubsystemManager.md#addListener) 的 fn 参数；结合上方功能说明和下方调用示例使用。 |
| `isCustomEvent` | 由值/所属选项确定 | `False` | 传给 [SubsystemManager.addListener](SubsystemManager.md#addListener) 的 isCustomEvent 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Subsystem manager has been destroyed'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `ListenForEvent`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addListener(instance, event, fn):
    return instance.addListener(event, fn)
```

## removeListener {#removeListener}

```python
removeListener(event, fn)
```

移除或清理 `removeListener` 操作。原生实现使用 `UnListenForEvent`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `event` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.removeListener](SubsystemManager.md#removeListener) 的 event 参数；结合上方功能说明和下方调用示例使用。 |
| `fn` | 由值/所属选项确定 | `必填` | 传给 [SubsystemManager.removeListener](SubsystemManager.md#removeListener) 的 fn 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `UnListenForEvent`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeListener(instance, event, fn):
    return instance.removeListener(event, fn)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 SubsystemManager 对象。
    print(value.registeredSubsystems)
    print(value.client)
    print(value.server)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)