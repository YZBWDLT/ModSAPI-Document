---
title: "MessageBox"
sidebar_label: "MessageBox"
---

# MessageBox

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/MessageBox.py`；声明补充了静态类型信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [body](#body) | 方法 |
| [button1](#button1) | 方法 |
| [button2](#button2) | 方法 |
| [close](#close) | 方法 |
| [dispose](#dispose) | 方法 |
| [isShowing](#isShowing) | 方法 |
| [show](#show) | 方法 |

## 构造器 {#constructor}

```python
MessageBox(player: Player, title: str | dict | Observable) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | [Player](../../server/apis/player.md) | `必填` | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |
| `title` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) \| [Observable](Observable.md) | `必填` | 标题文本，动态表单也可接受相应 [Observable](Observable.md)。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## body {#body}

```python
body(body: str | dict | Observable) -> MessageBox
```

执行 `body` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `body` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) \| [Observable](Observable.md) | `必填` | 传给 [MessageBox.body](MessageBox.md#body) 的 body 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [MessageBox](MessageBox.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_body(instance, body):
    return instance.body(body)
```

## button1 {#button1}

```python
button1(label: str | dict | Observable, tooltip: str | dict | Observable | None = None) -> MessageBox
```

执行 `button1` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) \| [Observable](Observable.md) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `tooltip` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) \| [Observable](Observable.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [MessageBox.button1](MessageBox.md#button1) 的 tooltip 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [MessageBox](MessageBox.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_button1(instance, label):
    return instance.button1(label)
```

## button2 {#button2}

```python
button2(label: str | dict | Observable, tooltip: str | dict | Observable | None = None) -> MessageBox
```

执行 `button2` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) \| [Observable](Observable.md) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `tooltip` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) \| [Observable](Observable.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [MessageBox.button2](MessageBox.md#button2) 的 tooltip 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [MessageBox](MessageBox.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_button2(instance, label):
    return instance.button2(label)
```

## close {#close}

```python
close() -> None
```

执行 `close` 操作。参数形态和结果约定如下。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_close(instance):
    return instance.close()
```

## dispose {#dispose}

```python
dispose() -> None
```

关闭消息框并释放它的表单；可以重复调用。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_dispose(instance):
    return instance.dispose()
```

## isShowing {#isShowing}

```python
isShowing() -> bool
```

检查 `isShowing` 操作。参数形态和结果约定如下。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_isShowing(instance):
    return instance.isShowing()
```

## show {#show}

```python
show() -> Promise[MessageBoxResult]
```

执行 `show` 操作。参数形态和结果约定如下。

**返回类型：** [Promise](../../common/reference/Promise.md)[[MessageBoxResult](MessageBoxResult.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_show(instance):
    return instance.show()
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 MessageBox 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)