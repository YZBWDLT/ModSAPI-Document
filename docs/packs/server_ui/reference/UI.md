---
title: "UI"
sidebar_label: "UI"
---

# UI

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/UI.py`。

本库专有的自定义界面。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [age](#age) | 只读属性 |
| [size](#size) | 可读写属性 |
| [background](#background) | 只读属性 |
| [addPanel](#addPanel) | 方法 |
| [addImage](#addImage) | 方法 |
| [addLabel](#addLabel) | 方法 |
| [addButton](#addButton) | 方法 |
| [addScrollPanel](#addScrollPanel) | 方法 |
| [show](#show) | 方法 |
| [addControl](#addControl) | 方法 |
| [onUpdate](#onUpdate) | 方法 |
| [remove](#remove) | 方法 |

## 构造器 {#constructor}

```python
UI()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## age {#age}

```python
age: Expression
```

UI寿命(从弹出界面开始),单位: tick(1秒30tick)

未弹出界面时返回-1

支持表达式

**访问：** 只读。

**返回类型：** [Expression](../../common/reference/Expression.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.age
```

## size {#size}

```python
size
```

屏幕尺寸，仅已弹出的界面可以获取值，未弹出的为0

手动设置无效

支持表达式

**访问：** 可读写。

写入方式：`instance.size = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.size

def write_value(instance, value):
    instance.size = value
```

## background {#background}

```python
background
```

背景数据

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

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
| `panelData` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 传给 [UI.addPanel](UI.md#addPanel) 的 panelData 参数；结合上方功能说明和下方调用示例使用。 |

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
| `name` | [str](../../common/type-system.md#str) | [None](../../common/type-system.md#none) | 传给 [UI.addImage](UI.md#addImage) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `offset` | [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] | `[0, 0]` | 传给 [UI.addImage](UI.md#addImage) 的 offset 参数；结合上方功能说明和下方调用示例使用。 |
| `size` | [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] | `[100, 100]` | 传给 [UI.addImage](UI.md#addImage) 的 size 参数；结合上方功能说明和下方调用示例使用。 |
| `texture` | [str](../../common/type-system.md#str) | `''` | 传给 [UI.addImage](UI.md#addImage) 的 texture 参数；结合上方功能说明和下方调用示例使用。 |
| `rotation` | [float](../../common/type-system.md#float) | `0` | 旋转角度，具体分量与单位参见成员说明。 |
| `alpha` | [float](../../common/type-system.md#float) | `1.0` | 传给 [UI.addImage](UI.md#addImage) 的 alpha 参数；结合上方功能说明和下方调用示例使用。 |
| `uvOrigin` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md)] | `(0, 0)` | 传给 [UI.addImage](UI.md#addImage) 的 uvOrigin 参数；结合上方功能说明和下方调用示例使用。 |
| `uvSize` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md)] | [None](../../common/type-system.md#none) | 传给 [UI.addImage](UI.md#addImage) 的 uvSize 参数；结合上方功能说明和下方调用示例使用。 |

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
| `labelData` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 传给 [UI.addLabel](UI.md#addLabel) 的 labelData 参数；结合上方功能说明和下方调用示例使用。 |

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
| `buttonData` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 传给 [UI.addButton](UI.md#addButton) 的 buttonData 参数；结合上方功能说明和下方调用示例使用。 |

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
| `panelData` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 传给 [UI.addScrollPanel](UI.md#addScrollPanel) 的 panelData 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addScrollPanel(instance):
    return instance.addScrollPanel()
```

## show {#show}

```python
show() -> None
```

执行 `show` 操作。原生实现使用 `PushScreen`，行为受网易运行环境约束。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `PushScreen`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_show(instance):
    return instance.show()
```

## addControl {#addControl}

```python
addControl(*controls) -> Control | list[Control]
```

添加一个或多个控件。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `*controls` | 可变参数 | `可省略` | 传给 [UI.addControl](UI.md#addControl) 的 *controls 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Control](Control.md) \| [list](../../common/type-system.md#list)[[Control](Control.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addControl(instance, *controls):
    return instance.addControl(*controls)
```

## onUpdate {#onUpdate}

```python
onUpdate(callback: types.FunctionType) -> None
```

设置界面刷新时要执行的函数

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [types.FunctionType](../../common/type-system.md#functiontype) | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_onUpdate(instance, callback):
    return instance.onUpdate(callback)
```

## remove {#remove}

```python
remove()
```

移除或清理 `remove` 操作。参数形态和结果约定如下。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_remove(instance):
    return instance.remove()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UI 对象。
    print(value.age)
    print(value.size)
    print(value.background)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)