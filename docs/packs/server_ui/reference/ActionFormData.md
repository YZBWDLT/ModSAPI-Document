---
title: "ActionFormData"
sidebar_label: "ActionFormData"
---

# ActionFormData

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/builders.py`；声明补充了静态类型信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [title](#title) | 方法 |
| [body](#body) | 方法 |
| [button](#button) | 方法 |
| [divider](#divider) | 方法 |
| [header](#header) | 方法 |
| [label](#label) | 方法 |
| [show](#show) | 方法 |

## 构造器 {#constructor}

```python
ActionFormData() -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## title {#title}

```python
title(titleText: str | dict) -> ActionFormData
```

设置或追加 `title` 对应的配置，返回当前对象以便继续构建。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `titleText` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `必填` | 传给 [ActionFormData.title](ActionFormData.md#title) 的 titleText 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ActionFormData](ActionFormData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_title(instance, titleText):
    return instance.title(titleText)
```

## body {#body}

```python
body(bodyText: str | dict) -> ActionFormData
```

设置或追加 `body` 对应的配置，返回当前对象以便继续构建。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `bodyText` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `必填` | 传给 [ActionFormData.body](ActionFormData.md#body) 的 bodyText 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ActionFormData](ActionFormData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_body(instance, bodyText):
    return instance.body(bodyText)
```

## button {#button}

```python
button(text: str | dict, iconPath: str | None = None) -> ActionFormData
```

设置或追加 `button` 对应的配置，返回当前对象以便继续构建。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `text` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `必填` | 显示文本；RawMessage 仅支持已实现的字面形式。 |
| `iconPath` | [str](../../common/type-system.md#str) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [ActionFormData.button](ActionFormData.md#button) 的 iconPath 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ActionFormData](ActionFormData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_button(instance, text):
    return instance.button(text)
```

## divider {#divider}

```python
divider() -> ActionFormData
```

设置或追加 `divider` 对应的配置，返回当前对象以便继续构建。

**返回类型：** [ActionFormData](ActionFormData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_divider(instance):
    return instance.divider()
```

## header {#header}

```python
header(text: str | dict) -> ActionFormData
```

设置或追加 `header` 对应的配置，返回当前对象以便继续构建。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `text` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `必填` | 显示文本；RawMessage 仅支持已实现的字面形式。 |

**返回类型：** [ActionFormData](ActionFormData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_header(instance, text):
    return instance.header(text)
```

## label {#label}

```python
label(text: str | dict) -> ActionFormData
```

设置或追加 `label` 对应的配置，返回当前对象以便继续构建。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `text` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `必填` | 显示文本；RawMessage 仅支持已实现的字面形式。 |

**返回类型：** [ActionFormData](ActionFormData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_label(instance, text):
    return instance.label(text)
```

## show {#show}

```python
show(player: Player) -> Promise[ActionFormResponse]
```

执行 `show` 操作。原生实现使用 [CustomForm](CustomForm.md)，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | [Player](../../server/apis/player.md) | `必填` | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |

**返回类型：** [Promise](../../common/reference/Promise.md)[[ActionFormResponse](ActionFormResponse.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** [CustomForm](CustomForm.md)。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_show(instance, player):
    return instance.show(player)
```

## 使用示例


```python
from __future__ import print_function

from ModSAPI.serverui.beta import ActionFormData

def show(player):
    result = ActionFormData().title("Menu").button("Start").show(player)
    result.then(lambda response: print(response.canceled, response.selection))
    result.catch(lambda error: print(error))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)