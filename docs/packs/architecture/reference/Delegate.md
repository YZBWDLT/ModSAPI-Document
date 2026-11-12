---
title: "Delegate"
sidebar_label: "Delegate"
---

# Delegate

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/event/core.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[Unreliable](Unreliable.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [bind](#bind) | 方法 |
| [call](#call) | 方法 |
| [unbind](#unbind) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [onError](Unreliable.md#onError) | [Unreliable](Unreliable.md) |
| [tryCall](Unreliable.md#tryCall) | [Unreliable](Unreliable.md) |

## 构造器 {#constructor}

```python
Delegate()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## bind {#bind}

```python
bind(fn)
```

执行 `bind` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fn` | 由值/所属选项确定 | `必填` | 传给 [Delegate.bind](Delegate.md#bind) 的 fn 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_bind(instance, fn):
    return instance.bind(fn)
```

## call {#call}

```python
call(*args)
```

执行 `call` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `*args` | 可变参数 | `可省略` | 传给 [Delegate.call](Delegate.md#call) 的 *args 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_call(instance, *args):
    return instance.call(*args)
```

## unbind {#unbind}

```python
unbind()
```

执行 `unbind` 操作。参数形态和结果约定如下。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_unbind(instance):
    return instance.unbind()
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 Delegate 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)