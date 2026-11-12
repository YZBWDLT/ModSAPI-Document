---
title: "ChainedEvent"
sidebar_label: "ChainedEvent"
---

# ChainedEvent

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/event/core.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `eventType` | 由运行时值确定 | `eventType` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [stop](#stop) | 方法 |
| [prevent](#prevent) | 方法 |
| [dict](#dict) | 方法 |
| [setEvent](#setEvent) | 方法 |

## 构造器 {#constructor}

```python
ChainedEvent(eventType, interruptRef, data)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `eventType` | 由值/所属选项确定 | `必填` | 传给 [ChainedEvent.__init__](ChainedEvent.md#constructor) 的 eventType 参数；结合上方功能说明和下方调用示例使用。 |
| `interruptRef` | 由值/所属选项确定 | `必填` | 传给 [ChainedEvent.__init__](ChainedEvent.md#constructor) 的 interruptRef 参数；结合上方功能说明和下方调用示例使用。 |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## stop {#stop}

```python
stop()
```

停止事件传递

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_stop(instance):
    return instance.stop()
```

## prevent {#prevent}

```python
prevent()
```

阻止默认事件 (cancel 设置为 True)

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_prevent(instance):
    return instance.prevent()
```

## dict {#dict}

```python
dict()
```

执行 [dict](../../common/type-system.md#dict) 操作。参数形态和结果约定如下。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_dict(instance):
    return instance.dict()
```

## setEvent {#setEvent}

```python
setEvent(p, v)
```

设置 `setEvent` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `p` | 由值/所属选项确定 | `必填` | 传给 [ChainedEvent.setEvent](ChainedEvent.md#setEvent) 的 p 参数；结合上方功能说明和下方调用示例使用。 |
| `v` | 由值/所属选项确定 | `必填` | 传给 [ChainedEvent.setEvent](ChainedEvent.md#setEvent) 的 v 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setEvent(instance, p, v):
    return instance.setEvent(p, v)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ChainedEvent 对象。
    print(value.eventType)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)