---
title: "ClientEventSignal"
sidebar_label: "ClientEventSignal"
---

# ClientEventSignal

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/NativeEvents.py`；声明补充了静态类型信息。

同步原生后置事件信号，按需注册引擎监听。subscribe 返回回调，重复订阅具有幂等性。unsubscribe 可接受同一绑定方法的新引用。各回调的异常独立记录，后续订阅者仍会运行。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [subscribe](#subscribe) | 方法 |
| [unsubscribe](#unsubscribe) | 方法 |

## 构造器 {#constructor}

```python
ClientEventSignal(owner, eventName, convert)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `owner` | 由值/所属选项确定 | `必填` | 传给 [ClientEventSignal.__init__](ClientEventSignal.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |
| `eventName` | 由值/所属选项确定 | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |
| `convert` | 由值/所属选项确定 | `必填` | 传给 [ClientEventSignal.__init__](ClientEventSignal.md#constructor) 的 convert 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## subscribe {#subscribe}

```python
subscribe(callback: Callable[[T], None]) -> Callable[[T], None]
```

注册可调用对象；所属客户端已结束时抛出异常。

:::note 当前实现说明
重复订阅同一回调幂等；原生同步分发，订阅者异常分别记录。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../../common/type-system.md#callable)[[[T](../../common/type-system.md#typevar)], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [Callable](../../common/type-system.md#callable)[[[T](../../common/type-system.md#typevar)], [None](../../common/type-system.md#none)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [InvalidClientObjectError](../../common/reference/InvalidClientObjectError.md) | `'Event signal has been disposed'` |
| [TypeError](../../common/type-system.md#typeerror) | `'callback must be callable'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_subscribe(instance, callback):
    return instance.subscribe(callback)
```

## unsubscribe {#unsubscribe}

```python
unsubscribe(callback: Callable[[T], None]) -> None
```

移除订阅；未知回调不产生额外操作。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../../common/type-system.md#callable)[[[T](../../common/type-system.md#typevar)], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

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
    # value 是所属 API 返回或接收的 ClientEventSignal 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)