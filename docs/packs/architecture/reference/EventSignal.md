---
title: "EventSignal"
sidebar_label: "EventSignal"
---

# EventSignal

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/event/core.py`。

## 获取方式

从 client/world 的 beforeEvents 或 afterEvents 属性获取；不自行构造。

基类：[Unreliable](Unreliable.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [on](#on) | 方法 |
| [off](#off) | 方法 |
| [emit](#emit) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [onError](Unreliable.md#onError) | [Unreliable](Unreliable.md) |
| [tryCall](Unreliable.md#tryCall) | [Unreliable](Unreliable.md) |

## 构造器 {#constructor}

```python
EventSignal()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## on {#on}

```python
on(fn)
```

执行 `on` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fn` | 由值/所属选项确定 | `必填` | 传给 [EventSignal.on](EventSignal.md#on) 的 fn 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_on(instance, fn):
    return instance.on(fn)
```

## off {#off}

```python
off(fn)
```

执行 `off` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fn` | 由值/所属选项确定 | `必填` | 传给 [EventSignal.off](EventSignal.md#off) 的 fn 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_off(instance, fn):
    return instance.off(fn)
```

## emit {#emit}

```python
emit(*args)
```

执行 `emit` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `*args` | 可变参数 | `可省略` | 传给 [EventSignal.emit](EventSignal.md#emit) 的 *args 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_emit(instance, *args):
    return instance.emit(*args)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 EventSignal 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)