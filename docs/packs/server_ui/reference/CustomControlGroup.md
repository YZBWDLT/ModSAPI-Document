---
title: "CustomControlGroup"
sidebar_label: "CustomControlGroup"
---

# CustomControlGroup

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/FormData.py`；声明补充了静态类型信息。

可添加到表单中的控件组。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [player](#player) | 只读属性 |
| [id](#id) | 只读属性 |
| [data](#data) | 只读属性 |
| [button](#button) | 方法 |
| [divider](#divider) | 方法 |
| [dropdown](#dropdown) | 方法 |
| [label](#label) | 方法 |
| [slider](#slider) | 方法 |
| [spacer](#spacer) | 方法 |
| [textField](#textField) | 方法 |
| [toggle](#toggle) | 方法 |
| [create](#create) | 静态/类方法 |

## 构造器 {#constructor}

```python
CustomControlGroup(identifier, player = None)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | 由值/所属选项确定 | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `player` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## player {#player}

```python
player
```

读取 `player` 的当前值。

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.player
```

## id {#id}

```python
id
```

此控件组的标识。

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## data {#data}

```python
data: list[dict]
```

读取 `data` 的当前值。

**访问：** 只读。

**返回类型：** [list](../../common/type-system.md#list)[[dict](../../common/type-system.md#dict)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.data
```

## button {#button}

```python
button(label: str | Observable, onClick: types.FunctionType, options: dict = {'visible': True, 'icon': ''}) -> CustomForm
```

向此控件组添加按钮。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [Observable](Observable.md) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `onClick` | [types.FunctionType](../../common/type-system.md#functiontype) | `必填` | 传给 [CustomControlGroup.button](CustomControlGroup.md#button) 的 onClick 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [dict](../../common/type-system.md#dict) | `{'visible': True, 'icon': ''}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_button(instance, label, onClick):
    return instance.button(label, onClick)
```

## divider {#divider}

```python
divider(options: dict = {'visible': True}) -> CustomForm
```

向此控件组添加分隔线。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [dict](../../common/type-system.md#dict) | `{'visible': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_divider(instance):
    return instance.divider()
```

## dropdown {#dropdown}

```python
dropdown(label: str | Observable, value: Observable, items: list, options: dict = {'visible': True}) -> CustomForm
```

向此控件组添加下拉框。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [Observable](Observable.md) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `value` | [Observable](Observable.md) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |
| `items` | [list](../../common/type-system.md#list) | `必填` | 下拉选项集合；标准构建器使用文本列表，[CustomForm](CustomForm.md) 使用 label/value 字典列表。 |
| `options` | [dict](../../common/type-system.md#dict) | `{'visible': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_dropdown(instance, label, value, items):
    return instance.dropdown(label, value, items)
```

## label {#label}

```python
label(text: str | Observable, options: dict = {'visible': True}) -> CustomForm
```

向此控件组添加文本标签。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `text` | [str](../../common/type-system.md#str) \| [Observable](Observable.md) | `必填` | 显示文本；RawMessage 仅支持已实现的字面形式。 |
| `options` | [dict](../../common/type-system.md#dict) | `{'visible': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_label(instance, text):
    return instance.label(text)
```

## slider {#slider}

```python
slider(label: str | Observable, value: Observable, minValue: int | Observable, maxValue: int | Observable, options: dict = {'visible': True}) -> CustomForm
```

向此控件组添加滑块。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [Observable](Observable.md) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `value` | [Observable](Observable.md) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |
| `minValue` | [int](../../common/type-system.md#int) \| [Observable](Observable.md) | `必填` | 传给 [CustomControlGroup.slider](CustomControlGroup.md#slider) 的 minValue 参数；结合上方功能说明和下方调用示例使用。 |
| `maxValue` | [int](../../common/type-system.md#int) \| [Observable](Observable.md) | `必填` | 传给 [CustomControlGroup.slider](CustomControlGroup.md#slider) 的 maxValue 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [dict](../../common/type-system.md#dict) | `{'visible': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

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

向此控件组添加间隔。

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
textField(label: str | Observable, text: Observable, options: dict = {'visible': True}) -> CustomForm
```

向此控件组添加文本输入框。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [Observable](Observable.md) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `text` | [Observable](Observable.md) | `必填` | 显示文本；RawMessage 仅支持已实现的字面形式。 |
| `options` | [dict](../../common/type-system.md#dict) | `{'visible': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_textField(instance, label, text):
    return instance.textField(label, text)
```

## toggle {#toggle}

```python
toggle(label: str | Observable, toggled: Observable, options: dict = {'visible': True}) -> CustomForm
```

向此控件组添加开关。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) \| [Observable](Observable.md) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `toggled` | [Observable](Observable.md) | `必填` | 传给 [CustomControlGroup.toggle](CustomControlGroup.md#toggle) 的 toggled 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [dict](../../common/type-system.md#dict) | `{'visible': True}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [CustomForm](CustomForm.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_toggle(instance, label, toggled):
    return instance.toggle(label, toggled)
```

## create {#create}

```python
create(identifier: str, player: Player | None = None) -> CustomControlGroup
```

创建自定义控件组。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `player` | [Player](../../server/apis/player.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |

**返回类型：** [CustomControlGroup](CustomControlGroup.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_create(type_object, identifier):
    return type_object.create(identifier)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 CustomControlGroup 对象。
    print(value.player)
    print(value.id)
    print(value.data)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)