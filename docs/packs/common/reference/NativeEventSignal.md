---
title: "NativeEventSignal"
sidebar_label: "NativeEventSignal"
---

# NativeEventSignal

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/native_events.py`；声明补充了静态类型信息。

由客户端或世界持有、按需注册的同步原生信号。重复订阅具有幂等性，各回调异常相互隔离。输出修改对同一信号的后续回调可见。subscribe 返回回调；unsubscribe 支持同一绑定方法的新引用。不补发或模拟事件，包括仅触发一次的生命周期事件。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [nativeEventName](#nativeEventName) | 只读属性 |
| [subscribe](#subscribe) | 方法 |
| [unsubscribe](#unsubscribe) | 方法 |

## 构造器 {#constructor}

```python
NativeEventSignal(owner, spec)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `owner` | 由值/所属选项确定 | `必填` | 传给 [NativeEventSignal.__init__](NativeEventSignal.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |
| `spec` | 由值/所属选项确定 | `必填` | 传给 [NativeEventSignal.__init__](NativeEventSignal.md#constructor) 的 spec 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## nativeEventName {#nativeEventName}

```python
nativeEventName: str
```

准确的引擎事件名称，可用于查阅原生文档。

**访问：** 只读。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.nativeEventName
```

## subscribe {#subscribe}

```python
subscribe(callback: Callable[[_TEvent], None]) -> Callable[[_TEvent], None]
```

订阅并返回可调用对象；所属对象或原生注册无效时抛出异常。不可调用参数抛出 [TypeError](../type-system.md#typeerror)；[InvalidClientObjectError](InvalidClientObjectError.md) 也用于世界生命周期已结束的情况；[NativeOperationError](NativeOperationError.md) 保留原生注册失败信息。旧引擎可能静默忽略未知事件，因此注册成功不能证明引擎支持该事件。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../type-system.md#callable)[[[_TEvent](../type-system.md#typevar)], [None](../type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [Callable](../type-system.md#callable)[[[_TEvent](../type-system.md#typevar)], [None](../type-system.md#none)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../type-system.md#typeerror) | `'callback must be callable'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_subscribe(instance, callback):
    return instance.subscribe(callback)
```

## unsubscribe {#unsubscribe}

```python
unsubscribe(callback: Callable[[_TEvent], None]) -> None
```

移除回调并释放空闲监听器；忽略未知回调。原生注销失败时抛出 [NativeOperationError](NativeOperationError.md) 并保留订阅以便重试。关闭清理时即使原生注销失败，也会在逻辑上关闭订阅。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../type-system.md#callable)[[[_TEvent](../type-system.md#typevar)], [None](../type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../type-system.md#typeerror) | `'callback must be callable'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_unsubscribe(instance, callback):
    return instance.unsubscribe(callback)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 NativeEventSignal 对象。
    print(value.nativeEventName)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)