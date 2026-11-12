---
title: "UiLabel"
sidebar_label: "UiLabel"
---

# UiLabel

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/controls.py`；声明补充了静态类型信息。

文字标签控件，支持读取和设置文字及三通道颜色。

## 获取方式

使用 view.getControl(path, "label")。

基类：[UiControl](UiControl.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [text](#text) | 可读写属性 |
| [color](#color) | 可读写属性 |
| [setFontScale](#setFontScale) | 方法 |
| [textAlignment](#textAlignment) | 可读写属性 |
| [lineSpacing](#lineSpacing) | 可读写属性 |
| [textShadow](#textShadow) | 可读写属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [anchorFrom](UiControl.md#anchorFrom) | [UiControl](UiControl.md) |
| [anchorTo](UiControl.md#anchorTo) | [UiControl](UiControl.md) |
| [animate](UiControl.md#animate) | [UiControl](UiControl.md) |
| [bind](UiControl.md#bind) | [UiControl](UiControl.md) |
| [blur](UiControl.md#blur) | [UiControl](UiControl.md) |
| [clipOffset](UiControl.md#clipOffset) | [UiControl](UiControl.md) |
| [clipsChildren](UiControl.md#clipsChildren) | [UiControl](UiControl.md) |
| [focus](UiControl.md#focus) | [UiControl](UiControl.md) |
| [getChild](UiControl.md#getChild) | [UiControl](UiControl.md) |
| [getChildren](UiControl.md#getChildren) | [UiControl](UiControl.md) |
| [getProperties](UiControl.md#getProperties) | [UiControl](UiControl.md) |
| [globalPosition](UiControl.md#globalPosition) | [UiControl](UiControl.md) |
| [isValid](UiControl.md#isValid) | [UiControl](UiControl.md) |
| [maximumSize](UiControl.md#maximumSize) | [UiControl](UiControl.md) |
| [minimumSize](UiControl.md#minimumSize) | [UiControl](UiControl.md) |
| [native](UiControl.md#native) | [UiControl](UiControl.md) |
| [path](UiControl.md#path) | [UiControl](UiControl.md) |
| [position](UiControl.md#position) | [UiControl](UiControl.md) |
| [remove](UiControl.md#remove) | [UiControl](UiControl.md) |
| [setAnchors](UiControl.md#setAnchors) | [UiControl](UiControl.md) |
| [setEnabled](UiControl.md#setEnabled) | [UiControl](UiControl.md) |
| [setLayer](UiControl.md#setLayer) | [UiControl](UiControl.md) |
| [setLayout](UiControl.md#setLayout) | [UiControl](UiControl.md) |
| [setOpacity](UiControl.md#setOpacity) | [UiControl](UiControl.md) |
| [setProperties](UiControl.md#setProperties) | [UiControl](UiControl.md) |
| [setVisible](UiControl.md#setVisible) | [UiControl](UiControl.md) |
| [size](UiControl.md#size) | [UiControl](UiControl.md) |
| [view](UiControl.md#view) | [UiControl](UiControl.md) |
| [visible](UiControl.md#visible) | [UiControl](UiControl.md) |

## text {#text}

```python
text: str
```

读取 `text` 的当前值。

**访问：** 可读写。

写入方式：`instance.text = value`。参数类型线索：`(value: str) -> None`。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.text

def write_value(instance, value):
    instance.text = value
```

## color {#color}

```python
color: tuple[float, float, float]
```

读取 `color` 的当前值。

**访问：** 可读写。

写入方式：`instance.color = value`。参数类型线索：`(value: tuple[float, float, float]) -> None`。

写入参数 `value`：[tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.color

def write_value(instance, value):
    instance.color = value
```

## setFontScale {#setFontScale}

```python
setFontScale(value: float) -> None
```

设置 `setFontScale` 操作。原生实现使用 `SetTextFontSize`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `value` | [float](../../common/type-system.md#float) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetTextFontSize`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setFontScale(instance, value):
    return instance.setFontScale(value)
```

## textAlignment {#textAlignment}

```python
textAlignment: Literal['left', 'center', 'right']
```

文字的水平对齐方式：left、center 或 right。

**访问：** 可读写。

写入方式：`instance.textAlignment = value`。参数类型线索：`(value: Literal['left', 'center', 'right']) -> None`。

写入参数 `value`：[Literal](../../common/type-system.md#literal)['left', 'center', 'right']。

**返回类型：** [Literal](../../common/type-system.md#literal)['left', 'center', 'right']。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.textAlignment

def write_value(instance, value):
    instance.textAlignment = value
```

## lineSpacing {#lineSpacing}

```python
lineSpacing: float
```

原生行间距，单位为像素，不随字体缩放设置改变。

**访问：** 可读写。

写入方式：`instance.lineSpacing = value`。参数类型线索：`(value: float) -> None`。

写入参数 `value`：[float](../../common/type-system.md#float)。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.lineSpacing

def write_value(instance, value):
    instance.lineSpacing = value
```

## textShadow {#textShadow}

```python
textShadow: bool
```

是否启用原生文字阴影。

**访问：** 可读写。

写入方式：`instance.textShadow = value`。参数类型线索：`(value: bool) -> None`。

写入参数 `value`：[bool](../../common/type-system.md#bool)。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.textShadow

def write_value(instance, value):
    instance.textShadow = value
```

## 使用示例


```python
def set_title(label):
    label.text = u"欢迎"
    label.color = (1, 1, 1)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)