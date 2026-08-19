---
sidebar_position: 2
---

# Form - 表单对象

## 概述

自定义表单接口，用于创建和管理表单控件，支持 Observable 数据绑定和链式调用。

## 创建

### create

`create(title: str | Observable, style?: ControlStyle)`

创建一个表单。

#### 参数

- title
  - 表单标题
- style?: [ControlStyle](./extra#ControlStyle)
  - 表单样式

## 属性

### isShowing

`[只读] isShowing: bool`

表单是否正在显示。

### identifier

`identifier: str`

表单标识符，可以不设置，主要用于方便编写一些逻辑。

## 方法

### button

`button(label: str | Observable, callbacks: ButtonCallbacks, style?: ControlStyle): Form`

添加一个按钮控件。

#### 参数

- label: str | [Observable](./observable)
  - 按钮标签文本。

- callbacks: [ButtonCallbacks](./extra#ButtonCallbacks)
  - 按钮回调函数，支持 `onClick`、`onMoveIn`、`onMoveOut`。

- style?: [ControlStyle](./extra#ControlStyle)
  - 控件样式。

#### 返回值

- Form
  - 返回当前表单实例，支持链式调用。

---

### toggle

`toggle(label: str | Observable, state: Observable, style?: ControlStyle): Form`

添加一个开关控件。

#### 参数

- label: str | [Observable](./observable)
  - 开关标签文本。

- state: [Observable](./observable)
  - 开关状态，支持双向绑定。

- style?: [ControlStyle](./extra#ControlStyle)
  - 控件样式。

#### 返回值

- Form
  - 返回当前表单实例，支持链式调用。

---

### divider

`divider(style?: ControlStyle): Form`

添加一个分割线控件。

#### 参数

- style?: [ControlStyle](./extra#ControlStyle)
  - 控件样式。

#### 返回值

- Form
  - 返回当前表单实例，支持链式调用。

---

### label

`label(text: str | Observable, style?: ControlStyle): Form`

添加一个文本标签控件。

#### 参数

- text: str | [Observable](./observable)
  - 标签文本内容。

- style?: [ControlStyle](./extra#ControlStyle)
  - 控件样式。

#### 返回值

- Form
  - 返回当前表单实例，支持链式调用。

---

### slider

`slider(label: str | Observable, value: Observable, minValue?: float | Observable, maxValue?: float | Observable, step?: float | Observable, style?: ControlStyle): Form`

添加一个滑动条控件。

#### 参数

- label: str | [Observable](./observable)
  - 滑动条标签文本。

- value: [Observable](./observable)
  - 滑动条当前值，支持双向绑定。

- minValue?: float | [Observable](./observable)
  - 滑动条最小值，默认 `0.0`。

- maxValue?: float | [Observable](./observable)
  - 滑动条最大值，默认 `1.0`。

- step?: float | [Observable](./observable)
  - 滑动条步长，默认 `1.0`。

- style?: [ControlStyle](./extra#ControlStyle)
  - 控件样式。

#### 返回值

- Form
  - 返回当前表单实例，支持链式调用。

---

### textfield

`textfield(label: str | Observable, value: Observable, style?: ControlStyle): Form`

添加一个文本输入框控件。

#### 参数

- label: str | [Observable](./observable)
  - 输入框标签文本。

- value: [Observable](./observable)
  - 输入框当前值，支持双向绑定。

- style?: [ControlStyle](./extra#ControlStyle)
  - 控件样式。

#### 返回值

- Form
  - 返回当前表单实例，支持链式调用。

---

### dropdown

`dropdown(label: str | Observable, items: list[DropdownItem], value: Observable, style?: ControlStyle): Form`

添加一个下拉框控件。

#### 参数

- label: str | [Observable](./observable)
  - 下拉框标签文本。

- items: list[[DropdownItem](./extra#DropdownItem)]
  - 下拉框选项列表。

- value: [Observable](./observable)
  - 下拉框当前选中值，支持双向绑定。

- style?: [ControlStyle](./extra#ControlStyle)
  - 控件样式。

#### 返回值

- Form
  - 返回当前表单实例，支持链式调用。

---

### custom

`custom(params?: dict, style?: ControlStyle): Form`

添加一个自定义控件。

#### 参数

- params?: dict
  - 自定义控件参数。

- style?: [ControlStyle](./extra#ControlStyle)
  - 控件样式。

#### 返回值

- Form
  - 返回当前表单实例，支持链式调用。

---

### show

`show(target: list[str] | str, options?: FormOptions): FormShowResult`

显示表单。

#### 参数

- target: list[str] | str
  - 要显示的表单目标，可填单个玩家 ID 或玩家 ID 列表。

- options?: [FormOptions](./extra#FormOptions)
  - 表单显示选项。

#### 返回值

- [FormShowResult](./form-show-result.md)
  - 表单显示结果对象，用于注册表单关闭事件。

---

### close

`close(): Form`

关闭表单。

#### 参数

无

#### 返回值

- Form
  - 返回当前表单实例，支持链式调用。

---

## 使用示例

```python
from xxx.xxx import Form
from xxx.xxx import Observable

# 创建表单
form = Form()

# 创建 Observable 数据
username = Observable("")
volume = Observable(50.0)
is_enabled = Observable(True)
language = Observable("python")

# 链式构建表单
form.label("用户设置", style={"font_size": 20}) \
    .divider() \
    .textfield("用户名", username, style={"placeholder": "请输入用户名"}) \
    .slider("音量", volume, minValue=0.0, maxValue=100.0, step=1.0) \
    .toggle("启用通知", is_enabled) \
    .dropdown("语言", [
        {"label": "Python", "value": "python"},
        {"label": "JavaScript", "value": "js"},
        {"label": "Java", "value": "java"}
    ], language) \
    .button("提交", callbacks={
        "onClick": lambda: print(f"用户名: {username.get()}, 音量: {volume.get()}")
    })

# 显示表单
form.show("player_001", options={"title": "用户设置", "width": 500})
```