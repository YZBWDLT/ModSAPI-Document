---
title: "Subsystem"
sidebar_label: "Subsystem"
---

# Subsystem

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/subsystem.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `system` | 由运行时值确定 | `system` |
| `engine` | 由运行时值确定 | `engine` |
| `sysName` | 由运行时值确定 | `sysName` |
| `ticks` | 由运行时值确定 | `0` |
| `canTick` | 由运行时值确定 | `False` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [onUpdate](#onUpdate) | 方法 |
| [onReady](#onReady) | 方法 |
| [onInit](#onInit) | 方法 |
| [onDestroy](#onDestroy) | 方法 |
| [getInstance](#getInstance) | 静态/类方法 |
| [getSystem](#getSystem) | 方法 |
| [getEngine](#getEngine) | 方法 |
| [getSysName](#getSysName) | 方法 |
| [on](#on) | 方法 |
| [off](#off) | 方法 |
| [listen](#listen) | 方法 |
| [unlisten](#unlisten) | 方法 |
| [broadcast](#broadcast) | 方法 |

## 构造器 {#constructor}

```python
Subsystem(system: object, engine: str, sysName: str) -> 'None'
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `system` | [object](../../common/type-system.md#object) | `必填` | 传给 [Subsystem.__init__](Subsystem.md#constructor) 的 system 参数；结合上方功能说明和下方调用示例使用。 |
| `engine` | [str](../../common/type-system.md#str) | `必填` | 传给 [Subsystem.__init__](Subsystem.md#constructor) 的 engine 参数；结合上方功能说明和下方调用示例使用。 |
| `sysName` | [str](../../common/type-system.md#str) | `必填` | 传给 [Subsystem.__init__](Subsystem.md#constructor) 的 sysName 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## onUpdate {#onUpdate}

```python
onUpdate(dt)
```

每tick调用

需要设置 `canTick` 为 `True`

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `dt` | 由值/所属选项确定 | `必填` | 传给 [Subsystem.onUpdate](Subsystem.md#onUpdate) 的 dt 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## onReady {#onReady}

```python
onReady()
```

所有子系统初始化完毕后调用

此时所有子系统已经创建完毕，可以通过 `getSubsystem` 获取其他子系统

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## onInit {#onInit}

```python
onInit()
```

当前子系统创建完毕后调用

此时 `SubystemManager` 已经创建完毕

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## onDestroy {#onDestroy}

```python
onDestroy()
```

当前没有功能性实现，不应依赖此成员完成操作。

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## getInstance {#getInstance}

```python
getInstance()
```

读取 `getInstance` 操作。参数形态和结果约定如下。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getInstance(type_object):
    return type_object.getInstance()
```

## getSystem {#getSystem}

```python
getSystem()
```

读取 `getSystem` 操作。参数形态和结果约定如下。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getSystem(instance):
    return instance.getSystem()
```

## getEngine {#getEngine}

```python
getEngine()
```

读取 `getEngine` 操作。参数形态和结果约定如下。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEngine(instance):
    return instance.getEngine()
```

## getSysName {#getSysName}

```python
getSysName()
```

读取 `getSysName` 操作。参数形态和结果约定如下。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getSysName(instance):
    return instance.getSysName()
```

## on {#on}

```python
on(eventName, handler, isCustomEvent = True)
```

执行 `on` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `eventName` | 由值/所属选项确定 | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |
| `handler` | 由值/所属选项确定 | `必填` | 传给 [Subsystem.on](Subsystem.md#on) 的 handler 参数；结合上方功能说明和下方调用示例使用。 |
| `isCustomEvent` | 由值/所属选项确定 | `True` | 传给 [Subsystem.on](Subsystem.md#on) 的 isCustomEvent 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_on(instance, eventName, handler):
    return instance.on(eventName, handler)
```

## off {#off}

```python
off(eventName, handler, isCustomEvent = True)
```

执行 `off` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `eventName` | 由值/所属选项确定 | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |
| `handler` | 由值/所属选项确定 | `必填` | 传给 [Subsystem.off](Subsystem.md#off) 的 handler 参数；结合上方功能说明和下方调用示例使用。 |
| `isCustomEvent` | 由值/所属选项确定 | `True` | 传给 [Subsystem.off](Subsystem.md#off) 的 isCustomEvent 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_off(instance, eventName, handler):
    return instance.off(eventName, handler)
```

## listen {#listen}

```python
listen(eventName, handler)
```

执行 `listen` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `eventName` | 由值/所属选项确定 | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |
| `handler` | 由值/所属选项确定 | `必填` | 传给 [Subsystem.listen](Subsystem.md#listen) 的 handler 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_listen(instance, eventName, handler):
    return instance.listen(eventName, handler)
```

## unlisten {#unlisten}

```python
unlisten(eventName, handler)
```

执行 `unlisten` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `eventName` | 由值/所属选项确定 | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |
| `handler` | 由值/所属选项确定 | `必填` | 传给 [Subsystem.unlisten](Subsystem.md#unlisten) 的 handler 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_unlisten(instance, eventName, handler):
    return instance.unlisten(eventName, handler)
```

## broadcast {#broadcast}

```python
broadcast(eventName, eventData)
```

执行 `broadcast` 操作。原生实现使用 `BroadcastEvent`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `eventName` | 由值/所属选项确定 | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |
| `eventData` | 由值/所属选项确定 | `必填` | 传给 [Subsystem.broadcast](Subsystem.md#broadcast) 的 eventData 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `BroadcastEvent`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_broadcast(instance, eventName, eventData):
    return instance.broadcast(eventName, eventData)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 Subsystem 对象。
    print(value.system)
    print(value.engine)
    print(value.sysName)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)