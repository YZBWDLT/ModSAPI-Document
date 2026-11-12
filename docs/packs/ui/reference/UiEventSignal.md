---
title: "UiEventSignal"
sidebar_label: "UiEventSignal"
---

# UiEventSignal

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/events.py`；声明补充了静态类型信息。

由所属界面对象管理的事件信号；订阅返回可重复调用的取消函数。

## 获取方式

通过拥有它的 afterEvents 容器获取。subscribe 返回取消函数。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [subscribe](#subscribe) | 方法 |
| [unsubscribe](#unsubscribe) | 方法 |

## subscribe {#subscribe}

```python
subscribe(callback: Callable[[_UiEventT], None]) -> Callable[[], None]
```

执行 `subscribe` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../../common/type-system.md#callable)[[[_UiEventT](../../common/type-system.md#typevar)], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [Callable](../../common/type-system.md#callable)[[], [None](../../common/type-system.md#none)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'UI event subscribers must be callable'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_subscribe(instance, callback):
    return instance.subscribe(callback)
```

## unsubscribe {#unsubscribe}

```python
unsubscribe(callback: Callable[[_UiEventT], None]) -> None
```

执行 `unsubscribe` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../../common/type-system.md#callable)[[[_UiEventT](../../common/type-system.md#typevar)], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

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
    # value 是所属 API 返回或接收的 UiEventSignal 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)