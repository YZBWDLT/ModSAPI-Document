---
title: "Control"
sidebar_label: "Control"
---

# Control

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/UI.py`。

控件基类

## 获取方式

从 ModSAPI.ui 导入，通过静态方法 register 登记模板描述。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [parent](#parent) | 只读属性 |
| [size](#size) | 可读写属性 |
| [name](#name) | 可读写属性 |
| [offset](#offset) | 可读写属性 |
| [anchor](#anchor) | 可读写属性 |
| [alpha](#alpha) | 可读写属性 |
| [background](#background) | 只读属性 |
| [addPanel](#addPanel) | 方法 |
| [addImage](#addImage) | 方法 |
| [addLabel](#addLabel) | 方法 |
| [addButton](#addButton) | 方法 |
| [addScrollPanel](#addScrollPanel) | 方法 |
| [addControl](#addControl) | 方法 |
| [copy](#copy) | 方法 |
| [trace](#trace) | 方法 |
| [asStaticControl](#asStaticControl) | 方法 |

## 构造器 {#constructor}

```python
Control(parent: Control | UI = None, name: str = None, offset: tuple[Expression. Expression] = [0, 0], size: tuple[Expression, Expression] = [100, 100], alpha: Expression = 1.0, background_color: tuple[Expression, Expression, Expression] = (255, 255, 255), background_alpha: Expression = 0.0, background_texture: str = 'textures/ui/white_bg') -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `parent` | [Control](Control.md) \| [UI](UI.md) | [None](../../common/type-system.md#none) | 传给 [Control.__init__](Control.md#constructor) 的 parent 参数；结合上方功能说明和下方调用示例使用。 |
| `name` | [str](../../common/type-system.md#str) | [None](../../common/type-system.md#none) | 传给 [Control.__init__](Control.md#constructor) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `offset` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md). [Expression](../../common/reference/Expression.md)] | `[0, 0]` | 传给 [Control.__init__](Control.md#constructor) 的 offset 参数；结合上方功能说明和下方调用示例使用。 |
| `size` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md)] | `[100, 100]` | 传给 [Control.__init__](Control.md#constructor) 的 size 参数；结合上方功能说明和下方调用示例使用。 |
| `alpha` | [Expression](../../common/reference/Expression.md) | `1.0` | 传给 [Control.__init__](Control.md#constructor) 的 alpha 参数；结合上方功能说明和下方调用示例使用。 |
| `background_color` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md)] | `(255, 255, 255)` | 传给 [Control.__init__](Control.md#constructor) 的 background_color 参数；结合上方功能说明和下方调用示例使用。 |
| `background_alpha` | [Expression](../../common/reference/Expression.md) | `0.0` | 传给 [Control.__init__](Control.md#constructor) 的 background_alpha 参数；结合上方功能说明和下方调用示例使用。 |
| `background_texture` | [str](../../common/type-system.md#str) | `'textures/ui/white_bg'` | 传给 [Control.__init__](Control.md#constructor) 的 background_texture 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## parent {#parent}

```python
parent: Control | UI
```

父控件。

**访问：** 只读。

**返回类型：** [Control](Control.md) \| [UI](UI.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.parent
```

## size {#size}

```python
size: list[int | str]
```

控件尺寸

支持表达式

**访问：** 可读写。

写入方式：`instance.size = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [list](../../common/type-system.md#list)[[int](../../common/type-system.md#int) \| [str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.size

def write_value(instance, value):
    instance.size = value
```

## name {#name}

```python
name
```

控件名称

**访问：** 可读写。

写入方式：`instance.name = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.name

def write_value(instance, value):
    instance.name = value
```

## offset {#offset}

```python
offset
```

控件位移（位置）

支持表达式

**访问：** 可读写。

写入方式：`instance.offset = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.offset

def write_value(instance, value):
    instance.offset = value
```

## anchor {#anchor}

```python
anchor
```

控件锚点

存储一个列表，0为父控件锚点（anchorFrom）,1为自身锚点（anchorTo）

**访问：** 可读写。

写入方式：`instance.anchor = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.anchor

def write_value(instance, value):
    instance.anchor = value
```

## alpha {#alpha}

```python
alpha
```

控件透明度

支持表达式

**访问：** 可读写。

写入方式：`instance.alpha = value`。参数类型线索：`(value: float) -> None`。

写入参数 `value`：[float](../../common/type-system.md#float)。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.alpha

def write_value(instance, value):
    instance.alpha = value
```

## background {#background}

```python
background: Image
```

读取 `background` 的当前值。

**访问：** 只读。

**返回类型：** [Image](Image.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.background
```

## addPanel {#addPanel}

```python
addPanel(panelData: dict = None) -> Panel
```

添加面板。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `panelData` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 传给 [Control.addPanel](Control.md#addPanel) 的 panelData 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Panel](Panel.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addPanel(instance):
    return instance.addPanel()
```

## addImage {#addImage}

```python
addImage(name: str = None, offset: tuple[float, float] = [0, 0], size: tuple[float, float] = [100, 100], texture: str = '', rotation: float = 0, alpha: float = 1.0, uvOrigin: tuple[Expression] = (0, 0), uvSize: tuple[Expression] = None) -> Image
```

添加图像。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../../common/type-system.md#str) | [None](../../common/type-system.md#none) | 传给 [Control.addImage](Control.md#addImage) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `offset` | [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] | `[0, 0]` | 传给 [Control.addImage](Control.md#addImage) 的 offset 参数；结合上方功能说明和下方调用示例使用。 |
| `size` | [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] | `[100, 100]` | 传给 [Control.addImage](Control.md#addImage) 的 size 参数；结合上方功能说明和下方调用示例使用。 |
| `texture` | [str](../../common/type-system.md#str) | `''` | 传给 [Control.addImage](Control.md#addImage) 的 texture 参数；结合上方功能说明和下方调用示例使用。 |
| `rotation` | [float](../../common/type-system.md#float) | `0` | 旋转角度，具体分量与单位参见成员说明。 |
| `alpha` | [float](../../common/type-system.md#float) | `1.0` | 传给 [Control.addImage](Control.md#addImage) 的 alpha 参数；结合上方功能说明和下方调用示例使用。 |
| `uvOrigin` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md)] | `(0, 0)` | 传给 [Control.addImage](Control.md#addImage) 的 uvOrigin 参数；结合上方功能说明和下方调用示例使用。 |
| `uvSize` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md)] | [None](../../common/type-system.md#none) | 传给 [Control.addImage](Control.md#addImage) 的 uvSize 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Image](Image.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addImage(instance):
    return instance.addImage()
```

## addLabel {#addLabel}

```python
addLabel(labelData: dict = None) -> Label
```

添加文本控件

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `labelData` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 传给 [Control.addLabel](Control.md#addLabel) 的 labelData 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Label](Label.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addLabel(instance):
    return instance.addLabel()
```

## addButton {#addButton}

```python
addButton(buttonData: dict = None) -> Button
```

添加文本控件

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `buttonData` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 传给 [Control.addButton](Control.md#addButton) 的 buttonData 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Button](Button.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addButton(instance):
    return instance.addButton()
```

## addScrollPanel {#addScrollPanel}

```python
addScrollPanel(panelData: dict = None) -> None
```

添加滚动面板

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `panelData` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 传给 [Control.addScrollPanel](Control.md#addScrollPanel) 的 panelData 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addScrollPanel(instance):
    return instance.addScrollPanel()
```

## addControl {#addControl}

```python
addControl(*controls) -> Control | list[Control]
```

添加一个或多个控件。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `*controls` | 可变参数 | `可省略` | 传给 [Control.addControl](Control.md#addControl) 的 *controls 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Control](Control.md) \| [list](../../common/type-system.md#list)[[Control](Control.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addControl(instance, *controls):
    return instance.addControl(*controls)
```

## copy {#copy}

```python
copy()
```

复制此控件子树，不复制父控件或无关控件。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_copy(instance):
    return instance.copy()
```

## trace {#trace}

```python
trace(interval: int = 1, maxAmount: int = 50, width: int = 2, alpha: int = 1, color: tuple = (255, 255, 255)) -> TraceData
```

记录轨迹

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `interval` | [int](../../common/type-system.md#int) | `1` | 传给 [Control.trace](Control.md#trace) 的 interval 参数；结合上方功能说明和下方调用示例使用。 |
| `maxAmount` | [int](../../common/type-system.md#int) | `50` | 传给 [Control.trace](Control.md#trace) 的 maxAmount 参数；结合上方功能说明和下方调用示例使用。 |
| `width` | [int](../../common/type-system.md#int) | `2` | 传给 [Control.trace](Control.md#trace) 的 width 参数；结合上方功能说明和下方调用示例使用。 |
| `alpha` | [int](../../common/type-system.md#int) | `1` | 传给 [Control.trace](Control.md#trace) 的 alpha 参数；结合上方功能说明和下方调用示例使用。 |
| `color` | [tuple](../../common/type-system.md#tuple) | `(255, 255, 255)` | 传给 [Control.trace](Control.md#trace) 的 color 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [TraceData](TraceData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_trace(instance):
    return instance.trace()
```

## asStaticControl {#asStaticControl}

```python
asStaticControl()
```

将此控件作为静态控件，即不会更新size等表达式。主要用于降低性能消耗。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_asStaticControl(instance):
    return instance.asStaticControl()
```

## 使用示例


```python
from ModSAPI.ui import Control, TextField

Control.register("demo:input", "demo_ui.input", TextField(textFieldPath="/input"))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)