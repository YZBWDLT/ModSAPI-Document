---
title: "EventSignal"
sidebar_label: "EventSignal"
---

# EventSignal

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/event_facade.py`；声明补充了静态类型信息。

在共享原生订阅之上提供筛选的同步语义事件信号。subscribe(callback, options=[None](../type-system.md#none)) 返回回调；注册前校验选项并复制筛选条件。重复订阅同一回调会更新筛选条件，空序列不匹配任何对象。一个原生数据包可拆分为多次通知，例如按兴趣区域中的实体或物理接触对分别通知。

## 获取方式

从 client/world 的 beforeEvents 或 afterEvents 属性获取；不自行构造。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [nativeEventNames](#nativeEventNames) | 只读属性 |
| [subscribe](#subscribe) | 方法 |
| [unsubscribe](#unsubscribe) | 方法 |

## 构造器 {#constructor}

```python
EventSignal(collection, spec)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `collection` | 由值/所属选项确定 | `必填` | 传给 [EventSignal.__init__](EventSignal.md#constructor) 的 collection 参数；结合上方功能说明和下方调用示例使用。 |
| `spec` | 由值/所属选项确定 | `必填` | 传给 [EventSignal.__init__](EventSignal.md#constructor) 的 spec 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## nativeEventNames {#nativeEventNames}

```python
nativeEventNames: tuple[str, ...]
```

准确的原生来源名称；与原生信号共享引擎监听器。

**访问：** 只读。

**返回类型：** [tuple](../type-system.md#tuple)[[str](../type-system.md#str), ...]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.nativeEventNames
```

## subscribe {#subscribe}

```python
subscribe(callback: Callable[[_TSemantic], None], options: Optional[EventSubscriptionOptions] = None) -> Callable[[_TSemantic], None]
```

校验参数和生命周期后注册并返回回调。回调或选项类型错误时抛出 [TypeError](../type-system.md#typeerror)；未知选项或不合法值抛出 [ValueError](../type-system.md#valueerror)；所属对象已结束时抛出 [InvalidClientObjectError](InvalidClientObjectError.md)；原生注册失败保留 [NativeOperationError](NativeOperationError.md) 详情。多来源注册部分失败时，先回滚已注册部分再抛出异常。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../type-system.md#callable)[[[_TSemantic](../type-system.md#typevar)], [None](../type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |
| `options` | [Optional](../type-system.md#optional)[[EventSubscriptionOptions](EventSubscriptionOptions.md)] | [None](../type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [Callable](../type-system.md#callable)[[[_TSemantic](../type-system.md#typevar)], [None](../type-system.md#none)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [InvalidClientObjectError](InvalidClientObjectError.md) | `'Semantic event signal has been disposed'` |
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
unsubscribe(callback: Callable[[_TSemantic], None]) -> None
```

先在逻辑上移除回调，再释放空闲来源；未知回调可安全忽略。原生清理失败时回调已禁用，同时抛出原生异常；可再次调用 unsubscribe 重试待完成的清理。其他订阅者和原生信号使用者保持连接。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../type-system.md#callable)[[[_TSemantic](../type-system.md#typevar)], [None](../type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

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
    # value 是上方获取方式取得的 EventSignal 对象。
    print(value.nativeEventNames)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)