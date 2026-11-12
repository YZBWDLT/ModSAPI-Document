---
title: "UiAnimation"
sidebar_label: "UiAnimation"
---

# UiAnimation

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/animations.py`；声明补充了静态类型信息。

单个原生动画通道，完成、取消或视图关闭时释放。支持透明度、位置、尺寸和图片裁剪比例；原生只写属性需要明确的起始值，时长以秒计。暂停后调用 play 继续播放。

## 获取方式

由 [UiControl.animate](UiControl.md#animate) 返回；使用 pause、play、cancel 和 dispose 管理。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [control](#control) | 只读属性 |
| [propertyName](#propertyName) | 只读属性 |
| [state](#state) | 只读属性 |
| [error](#error) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [afterEvents](#afterEvents) | 只读属性 |
| [pause](#pause) | 方法 |
| [play](#play) | 方法 |
| [cancel](#cancel) | 方法 |
| [dispose](#dispose) | 方法 |

## control {#control}

```python
control: UiControl
```

读取 `control` 的当前值。

**访问：** 只读。

**返回类型：** [UiControl](UiControl.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.control
```

## propertyName {#propertyName}

```python
propertyName: str
```

读取 `propertyName` 的当前值。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.propertyName
```

## state {#state}

```python
state: str
```

读取 `state` 的当前值。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.state
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

## isValid {#isValid}

```python
isValid: bool
```

读取 `isValid` 的当前值。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## afterEvents {#afterEvents}

```python
afterEvents: UiAnimationEvents
```

读取 `afterEvents` 的当前值。

**访问：** 只读。

**返回类型：** [UiAnimationEvents](UiAnimationEvents.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.afterEvents
```

## pause {#pause}

```python
pause() -> None
```

执行 `pause` 操作。原生实现使用 `PauseAnimation`，行为受网易运行环境约束。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `PauseAnimation`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_pause(instance):
    return instance.pause()
```

## play {#play}

```python
play() -> None
```

执行 `play` 操作。原生实现使用 `PlayAnimation`，行为受网易运行环境约束。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `PlayAnimation`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_play(instance):
    return instance.play()
```

## cancel {#cancel}

```python
cancel() -> None
```

释放本动画通道；之前清理失败时，仅重试尚未成功释放的资源。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `参见本成员的前置条件。` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_cancel(instance):
    return instance.cancel()
```

## dispose {#dispose}

```python
dispose() -> None
```

释放当前动画的原生登记，重复调用没有副作用。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_dispose(instance):
    return instance.dispose()
```

## 使用示例


```python
def stop_animation(animation):
    animation.cancel()
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)