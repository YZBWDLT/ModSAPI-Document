---
title: "MoreUI"
sidebar_label: "MoreUI"
---

# MoreUI

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/FormData.py`；声明补充了静态类型信息。

由多个表单组成的自定义界面。

## 获取方式

模板通过 `from ModSAPI.serverui.system import systems` 后使用 [systems.modules.MoreUI](MoreUI.md)；它未直接导出到 serverui.beta。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [create](#create) | 静态/类方法 |
| [addCustomForm](#addCustomForm) | 方法 |
| [layout](#layout) | 可读写属性 |
| [addForm](#addForm) | 方法 |
| [show](#show) | 方法 |
| [close](#close) | 方法 |

## 构造器 {#constructor}

```python
MoreUI(player, layout = {})
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | 由值/所属选项确定 | `必填` | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |
| `layout` | 由值/所属选项确定 | `{}` | 布局字典；字段与长度约束见 [FormLayout](FormLayout.md) 或 [MoreUILayout](MoreUILayout.md)。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'Create MoreUI failed! arg 0 excepted type Player.'` |
| [Exception](../../common/type-system.md#exception) | `'Create MoreUI failed! arg 1 excepted type dict, but got type %s' % layout` |
| [Exception](../../common/type-system.md#exception) | `'Create MoreUI failed! arg 0 excepted type <Player>, but got %s' % type(player).__name__` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## create {#create}

```python
create(player: Player, layout: MoreUILayoutDict = {}) -> MoreUI
```

创建 [MoreUI](MoreUI.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | [Player](../../server/apis/player.md) | `必填` | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |
| `layout` | [MoreUILayoutDict](MoreUILayoutDict.md) | `{}` | 布局字典；字段与长度约束见 [FormLayout](FormLayout.md) 或 [MoreUILayout](MoreUILayout.md)。 |

**返回类型：** [MoreUI](MoreUI.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_create(type_object, player):
    return type_object.create(player)
```

## addCustomForm {#addCustomForm}

```python
addCustomForm(title: str | Observable[str], options: CustomOptions = {}, layout: FormLayoutDict = {}) -> MoreUICustomData
```

向UI添加一个自定义表单([CustomForm](CustomForm.md))。

--title - 表单标题。

--options? - 表单创建选项。

--layout? - 表单布局。

返回表单数据

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `title` | [str](../../common/type-system.md#str) \| [Observable](Observable.md)[[str](../../common/type-system.md#str)] | `必填` | 标题文本，动态表单也可接受相应 [Observable](Observable.md)。 |
| `options` | [CustomOptions](CustomOptions.md) | `{}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |
| `layout` | [FormLayoutDict](FormLayoutDict.md) | `{}` | 布局字典；字段与长度约束见 [FormLayout](FormLayout.md) 或 [MoreUILayout](MoreUILayout.md)。 |

**返回类型：** [MoreUICustomData](MoreUICustomData.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'Add custom form failed! Arg 2 excepted dict, but got %s' % layout` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addCustomForm(instance, title):
    return instance.addCustomForm(title)
```

## layout {#layout}

```python
layout: MoreUILayout
```

此界面的布局。

**访问：** 可读写。

写入方式：`instance.layout = value`。参数类型线索：`(style: MoreUILayoutDict)`。

写入参数 `style`：[MoreUILayoutDict](MoreUILayoutDict.md)。

**返回类型：** [MoreUILayout](MoreUILayout.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'Set layout failed! style excepted type dict, but got %s' % type(style).__name__` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.layout

def write_value(instance, value):
    instance.layout = value
```

## addForm {#addForm}

```python
addForm(form: CustomForm, layout: FormLayoutDict = {}) -> MoreUICustomData
```

向UI添加一个已经创建好的表单。

--form - 表单对象([CustomForm](CustomForm.md))

--layout? - 表单布局

返回表单数据

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `form` | [CustomForm](CustomForm.md) | `必填` | 传给 [MoreUI.addForm](MoreUI.md#addForm) 的 form 参数；结合上方功能说明和下方调用示例使用。 |
| `layout` | [FormLayoutDict](FormLayoutDict.md) | `{}` | 布局字典；字段与长度约束见 [FormLayout](FormLayout.md) 或 [MoreUILayout](MoreUILayout.md)。 |

**返回类型：** [MoreUICustomData](MoreUICustomData.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'Add form failed! Arg 0 excepted type <CustomForm>, but got %s' % type(form).__name__` |
| [Exception](../../common/type-system.md#exception) | `'Add form failed! Arg 1 excepted type dict, but got %s' % type(layout).__name__` |
| [ValueError](../../common/type-system.md#valueerror) | `'Combined forms must belong to the same player'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Form has already been added'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Form is unavailable or already belongs to another window'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addForm(instance, form):
    return instance.addForm(form)
```

## show {#show}

```python
show() -> None
```

向玩家发送表单。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_show(instance):
    return instance.show()
```

## close {#close}

```python
close()
```

关闭全部子表单，再报告首次发送或回调失败。

**返回值：** 当前对象，可继续链式构建。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `参见本成员的前置条件。` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetSystem`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_close(instance):
    return instance.close()
```

## 使用示例


```python
from ModSAPI.serverui.system import systems

MoreUI = systems.modules.MoreUI

def show(player):
    window = MoreUI(player, {"row": [1], "column": [1, 1]})
    window.addCustomForm("Left").form.label("A")
    window.addCustomForm("Right").form.label("B")
    window.show()
    return window
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)