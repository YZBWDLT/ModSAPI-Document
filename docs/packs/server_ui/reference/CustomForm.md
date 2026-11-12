---
title: "CustomForm"
sidebar_label: "CustomForm"
---

import ApiFieldAnchor from '@docusaurus/Link';

# CustomForm

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/FormData.py`；声明补充了静态类型信息。

可自定义的动态表单，支持按钮、标签、开关、下拉框、滑块等控件。基于 [Observable](Observable.md)，观察值变化时会更新表单。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[DynamicForm](DynamicForm.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-ID" />`ID` | 由运行时值确定 | `0` |  |
| <ApiFieldAnchor id="field-id" />`id` | 由运行时值确定 | `id` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [isShowing](#isShowing) | 方法 |
| [header](#header) | 方法 |
| [closeButton](#closeButton) | 方法 |
| [formId](#formId) | 只读属性 |
| [dispose](#dispose) | 方法 |
| [button](#button) | 方法 |
| [close](#close) | 方法 |
| [divider](#divider) | 方法 |
| [dropdown](#dropdown) | 方法 |
| [label](#label) | 方法 |
| [show](#show) | 方法 |
| [slider](#slider) | 方法 |
| [spacer](#spacer) | 方法 |
| [textField](#textField) | 方法 |
| [toggle](#toggle) | 方法 |
| [controlGroup](#controlGroup) | 方法 |
| [create](#create) | 静态/类方法 |

## 构造器 {#constructor}

```python
CustomForm(player: Player, title: str | dict | Observable, options: dict | None = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | [Player](../../server/apis/player.md) | `必填` | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |
| `title` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) \| [Observable](Observable.md) | `必填` | 标题文本，动态表单也可接受相应 [Observable](Observable.md)。 |
| `options` | [dict](../../common/type-system.md#dict) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'Create custom form failed! arg 0 excepted type Player'` |
| [Exception](../../common/type-system.md#exception) | `'Create custom form failed! arg 1 excepted type str \| Observable<str>, but got %s' % ('Observable<%s>' % type(title.getData()).__name__ if hasattr(title, 'getData') else type(title).__name__)` |
| [Exception](../../common/type-system.md#exception) | `'Custom form create failed! arg 2 expected type dict, but got %s' % type(options).__name__` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLocalPlayerId`。

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

## header {#header}

```python
header(text: str | dict | Observable, options: dict | None = None) -> CustomForm
```

设置或追加 `header` 对应的配置，返回当前对象以便继续构建。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `text` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) \| [Observable](Observable.md) | `必填` | 显示文本；RawMessage 仅支持已实现的字面形式。 |
| `options` | [dict](../../common/type-system.md#dict) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_header(instance, text):
    return instance.header(text)
```

## closeButton {#closeButton}

```python
closeButton() -> CustomForm
```

执行 `closeButton` 操作。参数形态和结果约定如下。

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_closeButton(instance):
    return instance.closeButton()
```

## formId {#formId}

```python
formId: int
```

表单的内部分配id。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.formId
```

## dispose {#dispose}

```python
dispose() -> None
```

关闭正在显示的表单，释放它的监听器和所拥有的数据对象。

:::note 当前实现说明
释放表单拥有的订阅和值；外部 [Observable](Observable.md) 的所有权仍属于创建者。
:::

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

## button {#button}

```python
button(label: str | Observable[str], onClick: Callable[[], None], options: ButtonOptions = {'visible': True, 'icon': ''}) -> CustomForm
```

添加一个按钮。

--label - 按钮文本。

--onClick - 按钮按下时触发的回调函数。

--options? - 按钮选项。

返回自身

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [Observable](Observable.md)[[str](../../common/type-system.md#str)] | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `onClick` | [Callable](../../common/type-system.md#callable)[[], [None](../../common/type-system.md#none)] | `必填` | 传给 [CustomForm.button](CustomForm.md#button) 的 onClick 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [ButtonOptions](ButtonOptions.md) | `{'visible': True, 'icon': ''}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 0 expected type str \| Observable<str>, but got %s' % actual_type` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 1 expected type dict, but got %s' % type(options).__name__` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_button(instance, label, onClick):
    return instance.button(label, onClick)
```

## close {#close}

```python
close() -> None
```

关闭此表单。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_close(instance):
    return instance.close()
```

## divider {#divider}

```python
divider(options: DividerOptions = {'visible': True}) -> CustomForm
```

添加一条分割线。

--options - 分割线选项

返回自身

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [DividerOptions](DividerOptions.md) | `{'visible': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 1 expected type dict, but got %s' % type(options).__name__` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_divider(instance):
    return instance.divider()
```

## dropdown {#dropdown}

```python
dropdown(label: str | Observable[str], value: Observable[int], items: list[DropdownItem], options: DropdownOptions = {'visible': True}) -> CustomForm
```

添加一个下拉框。

--label - 标签文本

--value - 当前选中值。（必须为[Observable](Observable.md)&lt;[str](../../common/type-system.md#str)&gt;，且须clientWritable设置为True）

--items - 下拉框显示内容

--options - 下拉框选项

返回自身

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [Observable](Observable.md)[[str](../../common/type-system.md#str)] | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `value` | [Observable](Observable.md)[[int](../../common/type-system.md#int)] | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |
| `items` | [list](../../common/type-system.md#list)[[DropdownItem](DropdownItem.md)] | `必填` | 下拉选项集合；标准构建器使用文本列表，[CustomForm](CustomForm.md) 使用 label/value 字典列表。 |
| `options` | [DropdownOptions](DropdownOptions.md) | `{'visible': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 0 expected type str \| Observable<str>, but got %s' % actual_type` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 1 expected type Observable<int>, but got %s' % type('').__name__` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 2 expected type dict, but got %s' % type(options).__name__` |
| [Exception](../../common/type-system.md#exception) | `'Excepted value observable to be client writable.'` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 1 expected type Observable<int>, but got Observable<%s>' % type(value.getData()).__name__` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_dropdown(instance, label, value, items):
    return instance.dropdown(label, value, items)
```

## label {#label}

```python
label(text: str | Observable[str], options: LabelOptions = {'visible': True}) -> CustomForm
```

添加一个文本。

--text - 文本内容。

--options? - 文本选项。

返回自身

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `text` | [str](../../common/type-system.md#str) \| [Observable](Observable.md)[[str](../../common/type-system.md#str)] | `必填` | 显示文本；RawMessage 仅支持已实现的字面形式。 |
| `options` | [LabelOptions](LabelOptions.md) | `{'visible': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 0 expected type str \| Observable<str>, but got %s' % actual_type` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 1 expected type dict, but got %s' % type(options).__name__` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_label(instance, text):
    return instance.label(text)
```

## show {#show}

```python
show() -> Promise[str]
```

向玩家展示此表单。

:::note 当前实现说明
[Promise](../../common/reference/Promise.md) 返回关闭原因；与标准构建器返回 [FormResponse](FormResponse.md) 的约定不同。
:::

**返回类型：** [Promise](../../common/reference/Promise.md)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [InvalidFormError](InvalidFormError.md) | `self.formId` |
| [FormVisibilityError](FormVisibilityError.md) | `self.formId` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_show(instance):
    return instance.show()
```

## slider {#slider}

```python
slider(label: str | Observable[str], value: Observable[int], minValue: int | Observable[int], maxValue: int | Observable[int], options: SliderOptions = {'visible': True}) -> CustomForm
```

添加一个滑动条。

--label - 滑动条标签文本。

--value - 当前滑动条的值。（必须为[Observable](Observable.md)&lt;[int](../../common/type-system.md#int)&gt;，且须clientWritable设置为True）

--minValue - 最小值

--maxValue - 最大值

--options? - 滑动条选项

返回自身

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [Observable](Observable.md)[[str](../../common/type-system.md#str)] | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `value` | [Observable](Observable.md)[[int](../../common/type-system.md#int)] | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |
| `minValue` | [int](../../common/type-system.md#int) \| [Observable](Observable.md)[[int](../../common/type-system.md#int)] | `必填` | 传给 [CustomForm.slider](CustomForm.md#slider) 的 minValue 参数；结合上方功能说明和下方调用示例使用。 |
| `maxValue` | [int](../../common/type-system.md#int) \| [Observable](Observable.md)[[int](../../common/type-system.md#int)] | `必填` | 传给 [CustomForm.slider](CustomForm.md#slider) 的 maxValue 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [SliderOptions](SliderOptions.md) | `{'visible': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 0 expected type str \| Observable<str>, but got %s' % actual_type` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 1 expected type Observable<int>, but got %s' % type('').__name__` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 0 expected type int \| Observable<int>, but got %s' % actual_type` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 2 expected type dict, but got %s' % type(options).__name__` |
| [Exception](../../common/type-system.md#exception) | `'Excepted value observable to be client writable.'` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 1 expected type Observable<int>, but got Observable<%s>' % type(value.getData()).__name__` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_slider(instance, label, value, minValue, maxValue):
    return instance.slider(label, value, minValue, maxValue)
```

## spacer {#spacer}

```python
spacer(options: SpacerOptions = {'visible': True}) -> CustomForm
```

添加一段空白（效果同添加空白文本）

--options? - 空白选项

返回自身

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [SpacerOptions](SpacerOptions.md) | `{'visible': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_spacer(instance):
    return instance.spacer()
```

## textField {#textField}

```python
textField(label: str | Observable[str], text: Observable[str], options: TextFieldOptions = {'visible': True}) -> CustomForm
```

添加一个文本输入框。

--label - 文本输入框标签文本。

--text - 文本内容（必须为[Observable](Observable.md)&lt;[str](../../common/type-system.md#str)&gt;，且须clientWritable设置为True）

--options? - 文本输入框选项

返回自身

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [Observable](Observable.md)[[str](../../common/type-system.md#str)] | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `text` | [Observable](Observable.md)[[str](../../common/type-system.md#str)] | `必填` | 显示文本；RawMessage 仅支持已实现的字面形式。 |
| `options` | [TextFieldOptions](TextFieldOptions.md) | `{'visible': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 0 expected type str \| Observable<str>, but got %s' % actual_type` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 1 expected type Observable<str>, but got %s' % type(text).__name__` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 2 expected type dict, but got %s' % type(options).__name__` |
| [Exception](../../common/type-system.md#exception) | `'Excepted text observable to be client writable.'` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 1 expected type Observable<str>, but got Observable<%s>' % type(text.getData()).__name__` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_textField(instance, label, text):
    return instance.textField(label, text)
```

## toggle {#toggle}

```python
toggle(label: str | Observable[str], toggled: Observable[bool], options: ToggleOptions = {'visible': True}) -> CustomForm
```

添加一个开关。

--label - 开关标签文本

--toggled - 开关状态（必须为[Observable](Observable.md)&lt;[bool](../../common/type-system.md#bool)&gt;，且须clientWritable设置为True）

--options? - 开关选项

返回自身

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [Observable](Observable.md)[[str](../../common/type-system.md#str)] | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `toggled` | [Observable](Observable.md)[[bool](../../common/type-system.md#bool)] | `必填` | 传给 [CustomForm.toggle](CustomForm.md#toggle) 的 toggled 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [ToggleOptions](ToggleOptions.md) | `{'visible': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 0 expected type str \| Observable<str>, but got %s' % actual_type` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 1 expected type Observable<bool>, but got %s' % type(toggled).__name__` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 2 expected type dict, but got %s' % type(options).__name__` |
| [Exception](../../common/type-system.md#exception) | `'Excepted text observable to be client writable.'` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create button failed! arg 1 expected type Observable<bool>, but got Observable<%s>' % type(toggled.getData()).__name__` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_toggle(instance, label, toggled):
    return instance.toggle(label, toggled)
```

## controlGroup {#controlGroup}

```python
controlGroup(customControlGroup: CustomControlGroup | str, options: ControlGroupOptions = {'visible': True}) -> CustomForm
```

添加一个自定义控件组。

--customControlGroup - 自定义控件组对象或预设的自定义控件组名称（预设的自定义控件组可以在CustomControlGroups中找到）

--options? - 选项

返回自身

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `customControlGroup` | [CustomControlGroup](CustomControlGroup.md) \| [str](../../common/type-system.md#str) | `必填` | 传给 [CustomForm.controlGroup](CustomForm.md#controlGroup) 的 customControlGroup 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [ControlGroupOptions](ControlGroupOptions.md) | `{'visible': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create custom control failed! arg 0 expected type CustomControlGroup \| str, but got %s' % type(customControlGroup).__name__` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create custom control failed! arg 1 expected type dict, but got %s' % type(options).__name__` |
| [Exception](../../common/type-system.md#exception) | `'CustomForm create custom control failed! No custom control group named %s found.' % customControlGroup` |
| [Exception](../../common/type-system.md#exception) | `"CustomForm create custom control failed! Custom control group '%s' belongs to another player." % customControlGroup.id` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_controlGroup(instance, customControlGroup):
    return instance.controlGroup(customControlGroup)
```

## create {#create}

```python
create(player: Player, title: str | Observable[str], options: CustomOptions = {'resizable': False, 'movable': False, 'style': 'oreui', 'closable': True}) -> CustomForm
```

创建一个自定义表单。

--player - 需要接收到此表单的玩家对象

--title - 表单标题

--options? - 表单选项

返回自定义表单对象

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | [Player](../../server/apis/player.md) | `必填` | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |
| `title` | [str](../../common/type-system.md#str) \| [Observable](Observable.md)[[str](../../common/type-system.md#str)] | `必填` | 标题文本，动态表单也可接受相应 [Observable](Observable.md)。 |
| `options` | [CustomOptions](CustomOptions.md) | `{'resizable': False, 'movable': False, 'style': 'oreui', 'closable': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_create(type_object, player, title):
    return type_object.create(player, title)
```

## 使用示例


```python
from __future__ import print_function

from ModSAPI.serverui.beta import CustomForm

def show(player):
    form = CustomForm(player, "Example").label("Hello").closeButton()
    result = form.show()
    result.then(lambda reason: form.dispose())
    result.catch(lambda error: print(error))
    return form
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)