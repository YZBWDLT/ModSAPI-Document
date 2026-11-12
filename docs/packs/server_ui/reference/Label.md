---
title: "Label"
sidebar_label: "Label"
---

# Label

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/UI.py`。

文本标签控件。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[Control](Control.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `name` | 由运行时值确定 | `name if name else 'label%s' % random.randint(0, 2147483648)` |  |
| `offset` | 由运行时值确定 | `offset` |  |
| `size` | 由运行时值确定 | `size` |  |
| `alpha` | 由运行时值确定 | `alpha` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [text](#text) | 可读写属性 |
| [fontSize](#fontSize) | 可读写属性 |
| [align](#align) | 可读写属性 |
| [linePadding](#linePadding) | 可读写属性 |
| [color](#color) | 可读写属性 |
| [copy](#copy) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [addButton](Control.md#addButton) | [Control](Control.md) |
| [addControl](Control.md#addControl) | [Control](Control.md) |
| [addImage](Control.md#addImage) | [Control](Control.md) |
| [addLabel](Control.md#addLabel) | [Control](Control.md) |
| [addPanel](Control.md#addPanel) | [Control](Control.md) |
| [addScrollPanel](Control.md#addScrollPanel) | [Control](Control.md) |
| [anchor](Control.md#anchor) | [Control](Control.md) |
| [asStaticControl](Control.md#asStaticControl) | [Control](Control.md) |
| [background](Control.md#background) | [Control](Control.md) |
| [parent](Control.md#parent) | [Control](Control.md) |
| [trace](Control.md#trace) | [Control](Control.md) |

## 构造器 {#constructor}

```python
Label(parent: Control | UI = None, name: str = None, offset: tuple[Expression, Expression] = [0, 0], size: tuple[Expression, Expression] = [100, 100], alpha: Expression = 1.0, text: str = '', fontSize: Expression = 1.0, align: str = 'center', linePadding: Expression = 0.0, color: tuple[Expression, Expression, Expression] = (255, 255, 255)) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `parent` | [Control](Control.md) \| [UI](UI.md) | [None](../../common/type-system.md#none) | 传给 [Label.__init__](Label.md#constructor) 的 parent 参数；结合上方功能说明和下方调用示例使用。 |
| `name` | [str](../../common/type-system.md#str) | [None](../../common/type-system.md#none) | 传给 [Label.__init__](Label.md#constructor) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `offset` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md)] | `[0, 0]` | 传给 [Label.__init__](Label.md#constructor) 的 offset 参数；结合上方功能说明和下方调用示例使用。 |
| `size` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md)] | `[100, 100]` | 传给 [Label.__init__](Label.md#constructor) 的 size 参数；结合上方功能说明和下方调用示例使用。 |
| `alpha` | [Expression](../../common/reference/Expression.md) | `1.0` | 传给 [Label.__init__](Label.md#constructor) 的 alpha 参数；结合上方功能说明和下方调用示例使用。 |
| `text` | [str](../../common/type-system.md#str) | `''` | 显示文本；RawMessage 仅支持已实现的字面形式。 |
| `fontSize` | [Expression](../../common/reference/Expression.md) | `1.0` | 传给 [Label.__init__](Label.md#constructor) 的 fontSize 参数；结合上方功能说明和下方调用示例使用。 |
| `align` | [str](../../common/type-system.md#str) | `'center'` | 传给 [Label.__init__](Label.md#constructor) 的 align 参数；结合上方功能说明和下方调用示例使用。 |
| `linePadding` | [Expression](../../common/reference/Expression.md) | `0.0` | 传给 [Label.__init__](Label.md#constructor) 的 linePadding 参数；结合上方功能说明和下方调用示例使用。 |
| `color` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md)] | `(255, 255, 255)` | 传给 [Label.__init__](Label.md#constructor) 的 color 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## text {#text}

```python
text
```

标签的文本内容。

**访问：** 可读写。

写入方式：`instance.text = value`。参数类型线索：`(value: str) -> None`。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.text

def write_value(instance, value):
    instance.text = value
```

## fontSize {#fontSize}

```python
fontSize: Expression
```

文本大小，默认为1.0，支持表达式

**访问：** 可读写。

写入方式：`instance.fontSize = value`。参数类型线索：`(value: float \| Expression) -> None`。

写入参数 `value`：[float](../../common/type-system.md#float) \| [Expression](../../common/reference/Expression.md)。

**返回类型：** [Expression](../../common/reference/Expression.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.fontSize

def write_value(instance, value):
    instance.fontSize = value
```

## align {#align}

```python
align: str
```

文本对齐方向，可设置为left | right | center

**访问：** 可读写。

写入方式：`instance.align = value`。参数类型线索：`(value: str) -> None`。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.align

def write_value(instance, value):
    instance.align = value
```

## linePadding {#linePadding}

```python
linePadding: Expression
```

文本行间距，默认为0，支持表达式

**访问：** 可读写。

写入方式：`instance.linePadding = value`。参数类型线索：`(value: float \| Expression) -> None`。

写入参数 `value`：[float](../../common/type-system.md#float) \| [Expression](../../common/reference/Expression.md)。

**返回类型：** [Expression](../../common/reference/Expression.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.linePadding

def write_value(instance, value):
    instance.linePadding = value
```

## color {#color}

```python
color: tuple[Expression, Expression, Expression]
```

颜色，使用rgb格式，默认为(255, 255, 255)

支持表达式

**访问：** 可读写。

写入方式：`instance.color = value`。参数类型线索：`(value: tuple[int \| Expression] \| list[int \| Expression]) -> None`。

写入参数 `value`：[tuple](../../common/type-system.md#tuple)[[int](../../common/type-system.md#int) \| [Expression](../../common/reference/Expression.md)] \| [list](../../common/type-system.md#list)[[int](../../common/type-system.md#int) \| [Expression](../../common/reference/Expression.md)]。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.color

def write_value(instance, value):
    instance.color = value
```

## copy {#copy}

```python
copy()
```

执行 `copy` 操作。参数形态和结果约定如下。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_copy(instance):
    return instance.copy()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 Label 对象。
    print(value.text)
    print(value.fontSize)
    print(value.align)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)