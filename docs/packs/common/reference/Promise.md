---
title: "Promise"
sidebar_label: "Promise"
---

# Promise

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/promise.py`；声明补充了静态类型信息。

本库的异步结果对象，语义不完全等同于 JavaScript 的 [Promise](Promise.md)。

## 获取方式

从异步请求、表单或等待操作获取，不需要直接构造。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [then](#then) | 方法 |
| [catch](#catch) | 方法 |

## 构造器 {#constructor}

```python
Promise(type: T | None = None) -> None
```

创建 [Promise](Promise.md)。callback 用于定义异步结果何时完成。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| [type](../type-system.md#type) | [T](../type-system.md#typevar) \| [None](../type-system.md#none) | [None](../type-system.md#none) | 传给 [Promise.__init__](Promise.md#constructor) 的 [type](../type-system.md#type) 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## then {#then}

```python
then(callback: Callable[[T], None]) -> None
```

[Promise](Promise.md) 完成后执行回调函数。

:::note 当前实现说明
没有链式返回值；不要接着调用 .catch，也不支持 await。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../type-system.md#callable)[[[T](../type-system.md#typevar)], [None](../type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../type-system.md#typeerror) | `'callback must be callable'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_then(instance, callback):
    return instance.then(callback)
```

## catch {#catch}

```python
catch(callback: Callable[[Exception], None]) -> None
```

注册错误回调；异步操作已经失败后仍可注册。

:::note 当前实现说明
在原对象注册错误回调；不是 JavaScript [Promise](Promise.md) 链。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../type-system.md#callable)[[[Exception](../type-system.md#exception)], [None](../type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../type-system.md#typeerror) | `'callback must be callable'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_catch(instance, callback):
    return instance.catch(callback)
```

## 使用示例


```python
from __future__ import print_function

# request 是 getDataFromServer / show / waitTicks 等方法的返回值。
def observe(request):
    request.then(lambda value: print(value))
    request.catch(lambda error: print(error))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)