---
title: "Form"
sidebar_label: "Form"
---

import ApiFieldAnchor from '@docusaurus/Link';

# Form

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/core/general/form.py`；声明补充了静态类型信息。

两端通用的主题组合表单，使用包装后的玩家对象作为显示目标。

## 获取方式

从 ModSAPI.ui 导入 [Form](Form.md)，或使用 [client.ui.createForm](UiService.md#createForm) / [system.ui.createForm](UiService.md#createForm)。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-identifier" />`identifier` | [str](../../common/type-system.md#str) | `''` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [create](#create) | 静态/类方法 |
| [__init__](#constructor) | 构造器 |
| [dispose](#dispose) | 方法 |
| [getShowingPlayers](#getShowingPlayers) | 方法 |
| [isShowing](#isShowing) | 方法 |
| [button](#button) | 方法 |
| [toggle](#toggle) | 方法 |
| [divider](#divider) | 方法 |
| [label](#label) | 方法 |
| [slider](#slider) | 方法 |
| [textField](#textField) | 方法 |
| [dropdown](#dropdown) | 方法 |
| [listView](#listView) | 方法 |
| [group](#group) | 方法 |
| [custom](#custom) | 方法 |
| [show](#show) | 方法 |
| [close](#close) | 方法 |

## create {#create}

```python
create(title: str | Observable, options: dict | None = None) -> Form
```

创建表单，可提供主题、样式、网格位置和内容布局选项。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `title` | [str](../../common/type-system.md#str) \| [Observable](Observable.md) | `必填` | 标题文本，动态表单也可接受相应 [Observable](Observable.md)。 |
| `options` | [dict](../../common/type-system.md#dict) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [Form](Form.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_create(type_object, title):
    return type_object.create(title)
```

## 构造器 {#constructor}

```python
Form(title: TextValue = '', options: dict | None = None) -> None
```

创建并登记表单；选项支持 theme、style、grid 和 layout。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `title` | [TextValue](../../common/type-aliases.md#textvalue) | `''` | 标题文本，动态表单也可接受相应 [Observable](Observable.md)。 |
| `options` | [dict](../../common/type-system.md#dict) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'The UI runtime has been destroyed'` |
| [TypeError](../../common/type-system.md#typeerror) | `'Form options must be a dictionary'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown form options: %s' % ', '.join(sorted(unknown))` |
| [TypeError](../../common/type-system.md#typeerror) | `'form style must be a dict'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Form grid position requires Screen.setGrid()'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## dispose {#dispose}

```python
dispose() -> None
```

关闭该表单的所有显示实例，释放按钮回调和关闭监听。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `参见本成员的前置条件。` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_dispose(instance):
    return instance.dispose()
```

## getShowingPlayers {#getShowingPlayers}

```python
getShowingPlayers() -> list[Player | ClientPlayer]
```

取得当前显示或等待创建此表单的在线玩家对象。

**返回类型：** [list](../../common/type-system.md#list)[[Player](../../server/apis/player.md) \| [ClientPlayer](../../client/reference/ClientPlayer.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerList`, `GetLocalPlayerId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getShowingPlayers(instance):
    return instance.getShowingPlayers()
```

## isShowing {#isShowing}

```python
isShowing(player: Player | ClientPlayer | None = None) -> bool
```

当前是否有玩家显示此表单，或指定玩家是否正在显示。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | [Player](../../server/apis/player.md) \| [ClientPlayer](../../client/reference/ClientPlayer.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_isShowing(instance):
    return instance.isShowing()
```

## button {#button}

```python
button(label: TextValue, callbacks: ButtonHandler | None = {}, style: ControlStyle = {}, params: dict[str, Any] = {}, grid: GridPosition | None = None) -> Form
```

追加按钮；处理函数接收触发按钮的玩家包装对象。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [TextValue](../../common/type-aliases.md#textvalue) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `callbacks` | [ButtonHandler](../../common/type-aliases.md#buttonhandler) \| [None](../../common/type-system.md#none) | `{}` | 传给 [Form.button](Form.md#button) 的 callbacks 参数；结合上方功能说明和下方调用示例使用。 |
| `style` | [ControlStyle](ControlStyle.md) | `{}` | 传给 [Form.button](Form.md#button) 的 style 参数；结合上方功能说明和下方调用示例使用。 |
| `params` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] | `{}` | 传给 [Form.button](Form.md#button) 的 params 参数；结合上方功能说明和下方调用示例使用。 |
| `grid` | [GridPosition](GridPosition.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Form.button](Form.md#button) 的 grid 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Form](Form.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_button(instance, label):
    return instance.button(label)
```

## toggle {#toggle}

```python
toggle(label: TextValue, state: BoolValue, style: ControlStyle = {}, params: dict[str, Any] = {}, grid: GridPosition | None = None) -> Form
```

追加开关，输入变化与绑定状态同步。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [TextValue](../../common/type-aliases.md#textvalue) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `state` | [BoolValue](../../common/type-aliases.md#boolvalue) | `必填` | 传给 [Form.toggle](Form.md#toggle) 的 state 参数；结合上方功能说明和下方调用示例使用。 |
| `style` | [ControlStyle](ControlStyle.md) | `{}` | 传给 [Form.toggle](Form.md#toggle) 的 style 参数；结合上方功能说明和下方调用示例使用。 |
| `params` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] | `{}` | 传给 [Form.toggle](Form.md#toggle) 的 params 参数；结合上方功能说明和下方调用示例使用。 |
| `grid` | [GridPosition](GridPosition.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Form.toggle](Form.md#toggle) 的 grid 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Form](Form.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_toggle(instance, label, state):
    return instance.toggle(label, state)
```

## divider {#divider}

```python
divider(style: ControlStyle = {}, params: dict[str, Any] = {}, grid: GridPosition | None = None) -> Form
```

追加分割线，可提供独立布局选项。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `style` | [ControlStyle](ControlStyle.md) | `{}` | 传给 [Form.divider](Form.md#divider) 的 style 参数；结合上方功能说明和下方调用示例使用。 |
| `params` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] | `{}` | 传给 [Form.divider](Form.md#divider) 的 params 参数；结合上方功能说明和下方调用示例使用。 |
| `grid` | [GridPosition](GridPosition.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Form.divider](Form.md#divider) 的 grid 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Form](Form.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_divider(instance):
    return instance.divider()
```

## label {#label}

```python
label(text: TextValue, style: ControlStyle = {}, params: dict[str, Any] = {}, grid: GridPosition | None = None) -> Form
```

追加文字标签，文字和字体缩放可绑定状态。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `text` | [TextValue](../../common/type-aliases.md#textvalue) | `必填` | 显示文本；RawMessage 仅支持已实现的字面形式。 |
| `style` | [ControlStyle](ControlStyle.md) | `{}` | 传给 [Form.label](Form.md#label) 的 style 参数；结合上方功能说明和下方调用示例使用。 |
| `params` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] | `{}` | 传给 [Form.label](Form.md#label) 的 params 参数；结合上方功能说明和下方调用示例使用。 |
| `grid` | [GridPosition](GridPosition.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Form.label](Form.md#label) 的 grid 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Form](Form.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_label(instance, text):
    return instance.label(text)
```

## slider {#slider}

```python
slider(label: TextValue, value: NumberValue, minValue: NumberValue = 0.0, maxValue: NumberValue = 1.0, step: NumberValue = 1, style: ControlStyle = {}, params: dict[str, Any] = {}, grid: GridPosition | None = None) -> Form
```

追加滑动条；步长为零时连续取值，反向边界会自动排序。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [TextValue](../../common/type-aliases.md#textvalue) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `value` | [NumberValue](../../common/type-aliases.md#numbervalue) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |
| `minValue` | [NumberValue](../../common/type-aliases.md#numbervalue) | `0.0` | 传给 [Form.slider](Form.md#slider) 的 minValue 参数；结合上方功能说明和下方调用示例使用。 |
| `maxValue` | [NumberValue](../../common/type-aliases.md#numbervalue) | `1.0` | 传给 [Form.slider](Form.md#slider) 的 maxValue 参数；结合上方功能说明和下方调用示例使用。 |
| `step` | [NumberValue](../../common/type-aliases.md#numbervalue) | `1` | 传给 [Form.slider](Form.md#slider) 的 step 参数；结合上方功能说明和下方调用示例使用。 |
| `style` | [ControlStyle](ControlStyle.md) | `{}` | 传给 [Form.slider](Form.md#slider) 的 style 参数；结合上方功能说明和下方调用示例使用。 |
| `params` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] | `{}` | 传给 [Form.slider](Form.md#slider) 的 params 参数；结合上方功能说明和下方调用示例使用。 |
| `grid` | [GridPosition](GridPosition.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Form.slider](Form.md#slider) 的 grid 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Form](Form.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_slider(instance, label, value):
    return instance.slider(label, value)
```

## textField {#textField}

```python
textField(label: TextValue, value: TextValue, style: ControlStyle = {}, params: dict[str, Any] = {}, grid: GridPosition | None = None) -> Form
```

追加可绑定可写状态的文本输入控件。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [TextValue](../../common/type-aliases.md#textvalue) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `value` | [TextValue](../../common/type-aliases.md#textvalue) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |
| `style` | [ControlStyle](ControlStyle.md) | `{}` | 传给 [Form.textField](Form.md#textField) 的 style 参数；结合上方功能说明和下方调用示例使用。 |
| `params` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] | `{}` | 传给 [Form.textField](Form.md#textField) 的 params 参数；结合上方功能说明和下方调用示例使用。 |
| `grid` | [GridPosition](GridPosition.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Form.textField](Form.md#textField) 的 grid 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Form](Form.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_textField(instance, label, value):
    return instance.textField(label, value)
```

## dropdown {#dropdown}

```python
dropdown(label: TextValue, items: list[DropdownItem], value: int | str | Observable[int] | Observable[str], style: ControlStyle = {}, params: dict[str, Any] = {}, grid: GridPosition | None = None) -> Form
```

items 为静态选项；菜单标题与选中值可绑定 [Observable](Observable.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [TextValue](../../common/type-aliases.md#textvalue) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `items` | [list](../../common/type-system.md#list)[[DropdownItem](DropdownItem.md)] | `必填` | 下拉选项集合；标准构建器使用文本列表，[CustomForm](../../server_ui/reference/CustomForm.md) 使用 label/value 字典列表。 |
| `value` | [int](../../common/type-system.md#int) \| [str](../../common/type-system.md#str) \| [Observable](Observable.md)[[int](../../common/type-system.md#int)] \| [Observable](Observable.md)[[str](../../common/type-system.md#str)] | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |
| `style` | [ControlStyle](ControlStyle.md) | `{}` | 传给 [Form.dropdown](Form.md#dropdown) 的 style 参数；结合上方功能说明和下方调用示例使用。 |
| `params` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] | `{}` | 传给 [Form.dropdown](Form.md#dropdown) 的 params 参数；结合上方功能说明和下方调用示例使用。 |
| `grid` | [GridPosition](GridPosition.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Form.dropdown](Form.md#dropdown) 的 grid 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Form](Form.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_dropdown(instance, label, items, value):
    return instance.dropdown(label, items, value)
```

## listView {#listView}

```python
listView(label: TextValue, items: ListViewItems, value: ListViewValue = None, style: ListViewStyle = {}, params: dict[str, Any] = {}, grid: GridPosition | None = None) -> Form
```

追加内部滚动的单选列表，项目和选中值均可绑定状态。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [TextValue](../../common/type-aliases.md#textvalue) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `items` | [ListViewItems](../../common/type-aliases.md#listviewitems) | `必填` | 下拉选项集合；标准构建器使用文本列表，[CustomForm](../../server_ui/reference/CustomForm.md) 使用 label/value 字典列表。 |
| `value` | [ListViewValue](../../common/type-aliases.md#listviewvalue) | [None](../../common/type-system.md#none) | 需要写入的值，类型、范围及副本语义见本成员说明。 |
| `style` | [ListViewStyle](ListViewStyle.md) | `{}` | 传给 [Form.listView](Form.md#listView) 的 style 参数；结合上方功能说明和下方调用示例使用。 |
| `params` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] | `{}` | 传给 [Form.listView](Form.md#listView) 的 params 参数；结合上方功能说明和下方调用示例使用。 |
| `grid` | [GridPosition](GridPosition.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Form.listView](Form.md#listView) 的 grid 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Form](Form.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_listView(instance, label, items):
    return instance.listView(label, items)
```

## group {#group}

```python
group(children: GroupChildren = {}, style: GroupStyle = {}, params: dict[str, Any] = {}, grid: GridPosition | None = None) -> Form
```

追加已登记的控件组，通过 children 提供具名子控件的数据和回调。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `children` | [GroupChildren](../../common/type-aliases.md#groupchildren) | `{}` | 传给 [Form.group](Form.md#group) 的 children 参数；结合上方功能说明和下方调用示例使用。 |
| `style` | [GroupStyle](GroupStyle.md) | `{}` | 传给 [Form.group](Form.md#group) 的 style 参数；结合上方功能说明和下方调用示例使用。 |
| `params` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] | `{}` | 传给 [Form.group](Form.md#group) 的 params 参数；结合上方功能说明和下方调用示例使用。 |
| `grid` | [GridPosition](GridPosition.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Form.group](Form.md#group) 的 grid 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Form](Form.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'group children must be a dict'` |
| [TypeError](../../common/type-system.md#typeerror) | `'group child data must be a dict'` |
| [ValueError](../../common/type-system.md#valueerror) | `'group style %s must be a list with two elements' % pair` |
| [TypeError](../../common/type-system.md#typeerror) | `'group child params must be a dict'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_group(instance):
    return instance.group()
```

## custom {#custom}

```python
custom(params: dict[str, Any] = {}, style: ControlStyle = {}, grid: GridPosition | None = None) -> Form
```

追加自定义原生模板，支持参数数据和客户端创建、更新回调。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `params` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] | `{}` | 传给 [Form.custom](Form.md#custom) 的 params 参数；结合上方功能说明和下方调用示例使用。 |
| `style` | [ControlStyle](ControlStyle.md) | `{}` | 传给 [Form.custom](Form.md#custom) 的 style 参数；结合上方功能说明和下方调用示例使用。 |
| `grid` | [GridPosition](GridPosition.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Form.custom](Form.md#custom) 的 grid 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Form](Form.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'custom params must be a dict'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_custom(instance):
    return instance.custom()
```

## show {#show}

```python
show(player: Player | ClientPlayer | Iterable[Player] | None = None, onClose: Callable[[FormCloseEvent], None] | None = None) -> FormSession
```

向玩家包装对象显示表单；省略目标只适用于本地客户端。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | [Player](../../server/apis/player.md) \| [ClientPlayer](../../client/reference/ClientPlayer.md) \| [Iterable](../../common/type-system.md#iterable)[[Player](../../server/apis/player.md)] \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |
| `onClose` | [Callable](../../common/type-system.md#callable)[[[FormCloseEvent](FormCloseEvent.md)], [None](../../common/type-system.md#none)] \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Form.show](Form.md#show) 的 onClose 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [FormSession](FormSession.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'onClose must be callable or None'` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'该表单已经被显示出来了，关闭后才能再次调用 show()。'` |
| [ValueError](../../common/type-system.md#valueerror) | `'A client can only open its local UI'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `NotifyToMultiClients`, `GetLocalPlayerId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_show(instance):
    return instance.show()
```

## close {#close}

```python
close(player: Player | ClientPlayer | Iterable[Player] | None = None) -> None
```

为指定玩家关闭此表单；省略目标时关闭它的当前受众。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | [Player](../../server/apis/player.md) \| [ClientPlayer](../../client/reference/ClientPlayer.md) \| [Iterable](../../common/type-system.md#iterable)[[Player](../../server/apis/player.md)] \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `NotifyToMultiClients`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_close(instance):
    return instance.close()
```

## 使用示例


```python
from ModSAPI.client.beta import client

def create_form():
    form = client.ui.createForm(u"设置", {"theme": "fluent"})
    form.button(u"关闭", lambda player: form.close())
    return form
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)