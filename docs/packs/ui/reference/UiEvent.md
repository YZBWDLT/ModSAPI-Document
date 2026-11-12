---
title: "UiEvent"
sidebar_label: "UiEvent"
---

# UiEvent

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/events.py`；声明补充了静态类型信息。

本地界面事件参数，提供包装后的玩家、视图和控件引用。

## 获取方式

从视图生命周期或按钮交互的订阅回调取得。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [player](#player) | 只读属性 |
| [view](#view) | 只读属性 |
| [control](#control) | 只读属性 |
| [position](#position) | 只读属性 |
| [reason](#reason) | 只读属性 |

## player {#player}

```python
player: ClientPlayer
```

读取 `player` 的当前值。

**访问：** 只读。

**返回类型：** [ClientPlayer](../../client/reference/ClientPlayer.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.player
```

## view {#view}

```python
view: UiView
```

读取 `view` 的当前值。

**访问：** 只读。

**返回类型：** [UiView](UiView.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.view
```

## control {#control}

```python
control: UiControl | None
```

读取 `control` 的当前值。

**访问：** 只读。

**返回类型：** [UiControl](UiControl.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.control
```

## position {#position}

```python
position: tuple[float, float] | None
```

触点的原生界面像素坐标；原生事件没有提供坐标时为 [None](../../common/type-system.md#none)。

**访问：** 只读。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.position
```

## reason {#reason}

```python
reason: str | None
```

读取 `reason` 的当前值。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.reason
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UiEvent 对象。
    print(value.player)
    print(value.view)
    print(value.control)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)