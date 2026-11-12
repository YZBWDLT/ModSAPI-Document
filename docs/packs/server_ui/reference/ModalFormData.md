---
title: "ModalFormData"
sidebar_label: "ModalFormData"
---

# ModalFormData

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/builders.py`；声明补充了静态类型信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [title](#title) | 方法 |
| [submitButton](#submitButton) | 方法 |
| [divider](#divider) | 方法 |
| [header](#header) | 方法 |
| [label](#label) | 方法 |
| [toggle](#toggle) | 方法 |
| [textField](#textField) | 方法 |
| [slider](#slider) | 方法 |
| [dropdown](#dropdown) | 方法 |
| [show](#show) | 方法 |

## 构造器 {#constructor}

```python
ModalFormData() -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## title {#title}

```python
title(titleText: str | dict) -> ModalFormData
```

设置或追加 `title` 对应的配置，返回当前对象以便继续构建。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `titleText` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `必填` | 传给 [ModalFormData.title](ModalFormData.md#title) 的 titleText 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ModalFormData](ModalFormData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_title(instance, titleText):
    return instance.title(titleText)
```

## submitButton {#submitButton}

```python
submitButton(submitButtonText: str | dict) -> ModalFormData
```

设置或追加 `submitButton` 对应的配置，返回当前对象以便继续构建。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `submitButtonText` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `必填` | 传给 [ModalFormData.submitButton](ModalFormData.md#submitButton) 的 submitButtonText 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ModalFormData](ModalFormData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_submitButton(instance, submitButtonText):
    return instance.submitButton(submitButtonText)
```

## divider {#divider}

```python
divider() -> ModalFormData
```

设置或追加 `divider` 对应的配置，返回当前对象以便继续构建。

**返回类型：** [ModalFormData](ModalFormData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_divider(instance):
    return instance.divider()
```

## header {#header}

```python
header(text: str | dict) -> ModalFormData
```

设置或追加 `header` 对应的配置，返回当前对象以便继续构建。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `text` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `必填` | 显示文本；RawMessage 仅支持已实现的字面形式。 |

**返回类型：** [ModalFormData](ModalFormData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_header(instance, text):
    return instance.header(text)
```

## label {#label}

```python
label(text: str | dict) -> ModalFormData
```

设置或追加 `label` 对应的配置，返回当前对象以便继续构建。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `text` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `必填` | 显示文本；RawMessage 仅支持已实现的字面形式。 |

**返回类型：** [ModalFormData](ModalFormData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_label(instance, text):
    return instance.label(text)
```

## toggle {#toggle}

```python
toggle(label: str | dict, toggleOptions: ModalFormDataToggleOptions | bool | None = None) -> ModalFormData
```

设置或追加 `toggle` 对应的配置，返回当前对象以便继续构建。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `toggleOptions` | [ModalFormDataToggleOptions](ModalFormDataToggleOptions.md) \| [bool](../../common/type-system.md#bool) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 选项字典，常用 defaultValue；同时接受布尔初始值。 |

**返回类型：** [ModalFormData](ModalFormData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_toggle(instance, label):
    return instance.toggle(label)
```

## textField {#textField}

```python
textField(label: str | dict, placeholderText: str | dict, textFieldOptions: ModalFormDataTextFieldOptions | str | None = None) -> ModalFormData
```

设置或追加 `textField` 对应的配置，返回当前对象以便继续构建。

:::note 当前实现说明
placeholderText 参数被保存，但客户端占位符渲染尚未接入。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `placeholderText` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `必填` | 输入框占位文本；当前客户端占位符布局尚未接入。 |
| `textFieldOptions` | [ModalFormDataTextFieldOptions](ModalFormDataTextFieldOptions.md) \| [str](../../common/type-system.md#str) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 选项字典，常用 defaultValue；tooltip 尚无完整渲染。 |

**返回类型：** [ModalFormData](ModalFormData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_textField(instance, label, placeholderText):
    return instance.textField(label, placeholderText)
```

## slider {#slider}

```python
slider(label: str | dict, minimumValue: float, maximumValue: float, sliderOptions: ModalFormDataSliderOptions | float | None = None, defaultValue: float | None = None) -> ModalFormData
```

设置或追加 `slider` 对应的配置，返回当前对象以便继续构建。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `minimumValue` | [float](../../common/type-system.md#float) | `必填` | 滑块最小值，有限且不大于 maximumValue。 |
| `maximumValue` | [float](../../common/type-system.md#float) | `必填` | 滑块最大值，有限且不小于 minimumValue。 |
| `sliderOptions` | [ModalFormDataSliderOptions](ModalFormDataSliderOptions.md) \| [float](../../common/type-system.md#float) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 选项字典，常用 defaultValue、valueStep；tooltip 尚无完整渲染。 |
| `defaultValue` | [float](../../common/type-system.md#float) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 缺省值；具体是缺失键、初始控件值还是原生默认值取决于所属接口。 |

**返回类型：** [ModalFormData](ModalFormData.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Slider bounds and step must be finite numbers'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Slider requires minimum <= maximum and a positive step'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Slider default is outside its bounds'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_slider(instance, label, minimumValue, maximumValue):
    return instance.slider(label, minimumValue, maximumValue)
```

## dropdown {#dropdown}

```python
dropdown(label: str | dict, items: list[str | dict], dropdownOptions: ModalFormDataDropdownOptions | None = None) -> ModalFormData
```

设置或追加 `dropdown` 对应的配置，返回当前对象以便继续构建。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `items` | [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict)] | `必填` | 下拉选项集合；标准构建器使用文本列表，[CustomForm](CustomForm.md) 使用 label/value 字典列表。 |
| `dropdownOptions` | [ModalFormDataDropdownOptions](ModalFormDataDropdownOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 选项字典，defaultValueIndex 从零起始且必须在列表范围内。 |

**返回类型：** [ModalFormData](ModalFormData.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Dropdown requires a valid default item index'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_dropdown(instance, label, items):
    return instance.dropdown(label, items)
```

## show {#show}

```python
show(player: Player) -> Promise[ModalFormResponse]
```

执行 `show` 操作。原生实现使用 [CustomForm](CustomForm.md), [ObservableBoolean](ObservableBoolean.md), [ObservableString](ObservableString.md), [ObservableNumber](ObservableNumber.md)，行为受网易运行环境约束。

:::note 当前实现说明
formValues 保留非输入元素的位置，并以 [None](../../common/type-system.md#none) 占位；先检查 canceled。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | [Player](../../server/apis/player.md) | `必填` | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |

**返回类型：** [Promise](../../common/reference/Promise.md)[[ModalFormResponse](ModalFormResponse.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** [CustomForm](CustomForm.md), [ObservableBoolean](ObservableBoolean.md), [ObservableString](ObservableString.md), [ObservableNumber](ObservableNumber.md)。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_show(instance, player):
    return instance.show(player)
```

## 使用示例


```python
from __future__ import print_function

from ModSAPI.serverui.beta import ModalFormData

def show(player):
    form = ModalFormData().title("Settings")
    form.toggle("Enabled", {"defaultValue": True})
    form.slider("Volume", 0, 100, {"defaultValue": 50, "valueStep": 5})
    response = form.show(player)
    response.then(lambda result: print(result.canceled, result.formValues))
    response.catch(lambda error: print(error))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)