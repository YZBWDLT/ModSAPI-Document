---
title: "UiAnimationEvent"
sidebar_label: "UiAnimationEvent"
---

# UiAnimationEvent

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/animations.py`；声明补充了静态类型信息。

控件动画完成或失败时的事件参数。

## 获取方式

通过动画完成或失败的回调取得。

基类：[UiEvent](UiEvent.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [animation](#animation) | 只读属性 |
| [error](#error) | 只读属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [control](UiEvent.md#control) | [UiEvent](UiEvent.md) |
| [player](UiEvent.md#player) | [UiEvent](UiEvent.md) |
| [position](UiEvent.md#position) | [UiEvent](UiEvent.md) |
| [reason](UiEvent.md#reason) | [UiEvent](UiEvent.md) |
| [view](UiEvent.md#view) | [UiEvent](UiEvent.md) |

## animation {#animation}

```python
animation: UiAnimation
```

读取 `animation` 的当前值。

**访问：** 只读。

**返回类型：** [UiAnimation](UiAnimation.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.animation
```

## error {#error}

```python
error: Exception | None
```

读取 `error` 的当前值。

**访问：** 只读。

**返回类型：** [Exception](../../common/type-system.md#exception) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.error
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UiAnimationEvent 对象。
    print(value.animation)
    print(value.error)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)