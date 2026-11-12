---
title: "EventChain"
sidebar_label: "EventChain"
---

import ApiFieldAnchor from '@docusaurus/Link';

# EventChain

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/event/core.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[Unreliable](Unreliable.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-guarded" />`guarded` | 由运行时值确定 | `True` |  |
| <ApiFieldAnchor id="field-useCapture" />`useCapture` | 由运行时值确定 | `False` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [capture](#capture) | 方法 |
| [addListener](#addListener) | 方法 |
| [removeListener](#removeListener) | 方法 |
| [dispatch](#dispatch) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [onError](Unreliable.md#onError) | [Unreliable](Unreliable.md) |
| [tryCall](Unreliable.md#tryCall) | [Unreliable](Unreliable.md) |

## 构造器 {#constructor}

```python
EventChain()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## capture {#capture}

```python
capture(fn)
```

添加事件监听器（捕获）

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fn` | 由值/所属选项确定 | `必填` | 传给 [EventChain.capture](EventChain.md#capture) 的 fn 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_capture(instance, fn):
    return instance.capture(fn)
```

## addListener {#addListener}

```python
addListener(fn)
```

添加事件监听器（冒泡）

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fn` | 由值/所属选项确定 | `必填` | 传给 [EventChain.addListener](EventChain.md#addListener) 的 fn 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addListener(instance, fn):
    return instance.addListener(fn)
```

## removeListener {#removeListener}

```python
removeListener(fn)
```

移除或清理 `removeListener` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fn` | 由值/所属选项确定 | `必填` | 传给 [EventChain.removeListener](EventChain.md#removeListener) 的 fn 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeListener(instance, fn):
    return instance.removeListener(fn)
```

## dispatch {#dispatch}

```python
dispatch(evType, _ev)
```

执行 `dispatch` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `evType` | 由值/所属选项确定 | `必填` | 传给 [EventChain.dispatch](EventChain.md#dispatch) 的 evType 参数；结合上方功能说明和下方调用示例使用。 |
| `_ev` | 由值/所属选项确定 | `必填` | 传给 [EventChain.dispatch](EventChain.md#dispatch) 的 _ev 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_dispatch(instance, evType, _ev):
    return instance.dispatch(evType, _ev)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EventChain 对象。
    print(value.guarded)
    print(value.useCapture)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)