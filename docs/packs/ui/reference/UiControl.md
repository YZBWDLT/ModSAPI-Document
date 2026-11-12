---
title: "UiControl"
sidebar_label: "UiControl"
---

# UiControl

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/controls.py`；声明补充了静态类型信息。

由视图拥有的原生控件；原生操作要求所属视图存活且已经就绪。

## 获取方式

由 [UiView.getControl](UiView.md#getControl)、[UiView.createControl](UiView.md#createControl) 或 [UiControl.getChild](UiControl.md#getChild) 返回。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [view](#view) | 只读属性 |
| [path](#path) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [native](#native) | 只读属性 |
| [visible](#visible) | 可读写属性 |
| [setVisible](#setVisible) | 方法 |
| [position](#position) | 可读写属性 |
| [size](#size) | 可读写属性 |
| [setOpacity](#setOpacity) | 方法 |
| [setEnabled](#setEnabled) | 方法 |
| [setLayer](#setLayer) | 方法 |
| [globalPosition](#globalPosition) | 只读属性 |
| [anchorFrom](#anchorFrom) | 可读写属性 |
| [anchorTo](#anchorTo) | 可读写属性 |
| [setAnchors](#setAnchors) | 方法 |
| [minimumSize](#minimumSize) | 可读写属性 |
| [maximumSize](#maximumSize) | 可读写属性 |
| [clipsChildren](#clipsChildren) | 可读写属性 |
| [clipOffset](#clipOffset) | 可读写属性 |
| [focus](#focus) | 方法 |
| [blur](#blur) | 方法 |
| [getChildren](#getChildren) | 方法 |
| [setLayout](#setLayout) | 方法 |
| [setProperties](#setProperties) | 方法 |
| [getProperties](#getProperties) | 方法 |
| [bind](#bind) | 方法 |
| [animate](#animate) | 方法 |
| [getChild](#getChild) | 方法 |
| [remove](#remove) | 方法 |

## view {#view}

```python
view: UiView
```

读取 `view` 的当前值。

**访问：** 只读。

**返回类型：** [UiView](UiView.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.view
```

## path {#path}

```python
path: str
```

读取 `path` 的当前值。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.path
```

## isValid {#isValid}

```python
isValid: bool
```

读取 `isValid` 的当前值。底层调用 `GetBaseUIControl`。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBaseUIControl`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## native {#native}

```python
native: Any
```

明确取得当前存活的原生界面控件，供原生扩展操作使用。

**访问：** 只读。

**返回类型：** [Any](../../common/type-system.md#any)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [InvalidClientObjectError](../../common/reference/InvalidClientObjectError.md) | `'The UI control no longer exists'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBaseUIControl`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.native
```

## visible {#visible}

```python
visible: bool
```

读取 `visible` 的当前值。

**访问：** 可读写。

写入方式：`instance.visible = value`。参数类型线索：`(value: bool) -> None`。

写入参数 `value`：[bool](../../common/type-system.md#bool)。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.visible

def write_value(instance, value):
    instance.visible = value
```

## setVisible {#setVisible}

```python
setVisible(value: bool, refresh: bool = True) -> None
```

修改可见性；可先传 refresh=False 批量修改，再调用视图 refresh 统一刷新。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `value` | [bool](../../common/type-system.md#bool) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |
| `refresh` | [bool](../../common/type-system.md#bool) | `True` | 传给 [UiControl.setVisible](UiControl.md#setVisible) 的 refresh 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetVisible`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setVisible(instance, value):
    return instance.setVisible(value)
```

## position {#position}

```python
position: tuple[float, float]
```

读取 `position` 的当前值。

**访问：** 可读写。

写入方式：`instance.position = value`。参数类型线索：`(value: tuple[float, float]) -> None`。

写入参数 `value`：[tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.position

def write_value(instance, value):
    instance.position = value
```

## size {#size}

```python
size: tuple[float, float]
```

读取 `size` 的当前值。

**访问：** 可读写。

写入方式：`instance.size = value`。参数类型线索：`(value: tuple[float, float]) -> None`。

写入参数 `value`：[tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.size

def write_value(instance, value):
    instance.size = value
```

## setOpacity {#setOpacity}

```python
setOpacity(value: float) -> None
```

设置 0～1 的透明度；原生接口没有对应读取方法。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `value` | [float](../../common/type-system.md#float) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetAlpha`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setOpacity(instance, value):
    return instance.setOpacity(value)
```

## setEnabled {#setEnabled}

```python
setEnabled(value: bool) -> None
```

设置 `setEnabled` 操作。原生实现使用 `SetTouchEnable`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `value` | [bool](../../common/type-system.md#bool) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetTouchEnable`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setEnabled(instance, value):
    return instance.setEnabled(value)
```

## setLayer {#setLayer}

```python
setLayer(value: int, refresh: bool = True) -> None
```

设置 `setLayer` 操作。原生实现使用 `SetLayer`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `value` | [int](../../common/type-system.md#int) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |
| `refresh` | [bool](../../common/type-system.md#bool) | `True` | 传给 [UiControl.setLayer](UiControl.md#setLayer) 的 refresh 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetLayer`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setLayer(instance, value):
    return instance.setLayer(value)
```

## globalPosition {#globalPosition}

```python
globalPosition: tuple[float, float]
```

控件当前的全局位置，单位为原生界面像素。

**访问：** 只读。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.globalPosition
```

## anchorFrom {#anchorFrom}

```python
anchorFrom: str
```

位置和百分比布局使用的父控件锚点。

**访问：** 可读写。

写入方式：`instance.anchorFrom = value`。参数类型线索：`(value: str) -> None`。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.anchorFrom

def write_value(instance, value):
    instance.anchorFrom = value
```

## anchorTo {#anchorTo}

```python
anchorTo: str
```

此控件自身的锚点，使用 [UiAnchor](UiAnchor.md) 常量。

**访问：** 可读写。

写入方式：`instance.anchorTo = value`。参数类型线索：`(value: str) -> None`。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.anchorTo

def write_value(instance, value):
    instance.anchorTo = value
```

## setAnchors {#setAnchors}

```python
setAnchors(fromAnchor: str, toAnchor: str | None = None) -> None
```

一次设置两个锚点；省略 toAnchor 时，两者均使用 fromAnchor。原生更新失败时尝试恢复原来的锚点；恢复失败的信息保存在 rollbackErrors。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fromAnchor` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiControl.setAnchors](UiControl.md#setAnchors) 的 fromAnchor 参数；结合上方功能说明和下方调用示例使用。 |
| `toAnchor` | [str](../../common/type-system.md#str) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [UiControl.setAnchors](UiControl.md#setAnchors) 的 toAnchor 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetAnchorFrom`, `SetAnchorTo`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setAnchors(instance, fromAnchor):
    return instance.setAnchors(fromAnchor)
```

## minimumSize {#minimumSize}

```python
minimumSize: tuple[float, float]
```

原生最小像素尺寸；(0, 0) 表示取消限制。

**访问：** 可读写。

写入方式：`instance.minimumSize = value`。参数类型线索：`(value: tuple[float, float]) -> None`。

写入参数 `value`：[tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.minimumSize

def write_value(instance, value):
    instance.minimumSize = value
```

## maximumSize {#maximumSize}

```python
maximumSize: tuple[float, float]
```

原生最大像素尺寸；(0, 0) 表示取消限制。

**访问：** 可读写。

写入方式：`instance.maximumSize = value`。参数类型线索：`(value: tuple[float, float]) -> None`。

写入参数 `value`：[tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.maximumSize

def write_value(instance, value):
    instance.maximumSize = value
```

## clipsChildren {#clipsChildren}

```python
clipsChildren: bool
```

是否根据此控件的裁剪范围裁剪子控件。

**访问：** 可读写。

写入方式：`instance.clipsChildren = value`。参数类型线索：`(value: bool) -> None`。

写入参数 `value`：[bool](../../common/type-system.md#bool)。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.clipsChildren

def write_value(instance, value):
    instance.clipsChildren = value
```

## clipOffset {#clipOffset}

```python
clipOffset: tuple[float, float]
```

原生二维裁剪偏移，单位为界面像素。

**访问：** 可读写。

写入方式：`instance.clipOffset = value`。参数类型线索：`(value: tuple[float, float]) -> None`。

写入参数 `value`：[tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.clipOffset

def write_value(instance, value):
    instance.clipOffset = value
```

## focus {#focus}

```python
focus() -> None
```

选中此控件；选中文本框时，原生系统可能弹出键盘。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetSelectControl`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_focus(instance):
    return instance.focus()
```

## blur {#blur}

```python
blur() -> None
```

请求取消此控件的原生选中状态。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetSelectControl`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_blur(instance):
    return instance.blur()
```

## getChildren {#getChildren}

```python
getChildren(recursive: bool = False) -> tuple[UiControl, ...]
```

重新获取子控件对象；可选择包含全部后代控件。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `recursive` | [bool](../../common/type-system.md#bool) | `False` | 传给 [UiControl.getChildren](UiControl.md#getChildren) 的 recursive 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [tuple](../../common/type-system.md#tuple)[[UiControl](UiControl.md), ...]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'Native child enumeration must return a sequence'` |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `method` |
| [ValueError](../../common/type-system.md#valueerror) | `'Native child names must be single path components'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Native child path must stay below its parent'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getChildren(instance):
    return instance.getChildren()
```

## setLayout {#setLayout}

```python
setLayout(values: dict[str, float | str]) -> None
```

应用位置和尺寸表达式，支持像素及百分比，例如 100%-8px。中途失败时尝试恢复已经修改的轴；恢复本身失败时，异常的 rollbackErrors 保留这些错误。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `values` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [float](../../common/type-system.md#float) \| [str](../../common/type-system.md#str)] | `必填` | 传给 [UiControl.setLayout](UiControl.md#setLayout) 的 values 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetFullLayout'` |
| [TypeError](../../common/type-system.md#typeerror) | `'Layout dimensions cannot be booleans'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Layout dimensions cannot use default'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setLayout(instance, values):
    return instance.setLayout(values)
```

## setProperties {#setProperties}

```python
setProperties(values: dict[str, str | int | float | bool]) -> None
```

先校验属性名称和值，再合并原生属性包中的标量数据。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `values` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [str](../../common/type-system.md#str) \| [int](../../common/type-system.md#int) \| [float](../../common/type-system.md#float) \| [bool](../../common/type-system.md#bool)] | `必填` | 传给 [UiControl.setProperties](UiControl.md#setProperties) 的 values 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'properties must be a dictionary'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetPropertyBag`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setProperties(instance, values):
    return instance.setProperties(values)
```

## getProperties {#getProperties}

```python
getProperties() -> dict[str, str | int | float | bool]
```

读取 `getProperties` 操作。参数形态和结果约定如下。

**返回类型：** [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [str](../../common/type-system.md#str) \| [int](../../common/type-system.md#int) \| [float](../../common/type-system.md#float) \| [bool](../../common/type-system.md#bool)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getProperties(instance):
    return instance.getProperties()
```

## bind {#bind}

```python
bind(propertyName: str, state: Observable) -> Callable[[], None]
```

把可写属性绑定到本地状态，返回取消函数。该绑定从状态写入界面；原生输入控件不会自动创建反向绑定，双向输入状态可使用组合表单。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `propertyName` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiControl.bind](UiControl.md#bind) 的 propertyName 参数；结合上方功能说明和下方调用示例使用。 |
| `state` | [Observable](Observable.md) | `必填` | 传给 [UiControl.bind](UiControl.md#bind) 的 state 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Callable](../../common/type-system.md#callable)[[], [None](../../common/type-system.md#none)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'state must be a UI Observable'` |
| [ValueError](../../common/type-system.md#valueerror) | `'The selected control has no writable property: %r' % propertyName` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_bind(instance, propertyName, state):
    return instance.bind(propertyName, state)
```

## animate {#animate}

```python
animate(propertyName: str, to: float | tuple[float, float], options: UiAnimationOptions | None = None) -> UiAnimation
```

运行当前控件拥有的原生属性动画，不创建逐帧的 Python 定时器。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `propertyName` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiControl.animate](UiControl.md#animate) 的 propertyName 参数；结合上方功能说明和下方调用示例使用。 |
| `to` | [float](../../common/type-system.md#float) \| [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] | `必填` | 传给 [UiControl.animate](UiControl.md#animate) 的 to 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [UiAnimationOptions](UiAnimationOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [UiAnimation](UiAnimation.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_animate(instance, propertyName, to):
    return instance.animate(propertyName, to)
```

## getChild {#getChild}

```python
getChild(path: str, kind: Literal['control', 'label', 'button', 'image', 'textField', 'slider', 'toggle', 'scrollView', 'grid', 'stackPanel', 'inputPanel', 'progressBar', 'itemRenderer', 'comboBox', 'selectionWheel', 'miniMap'] = 'control') -> UiControl
```

读取 `getChild` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `path` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiControl.getChild](UiControl.md#getChild) 的 path 参数；结合上方功能说明和下方调用示例使用。 |
| `kind` | [Literal](../../common/type-system.md#literal)['control', 'label', 'button', 'image', 'textField', 'slider', 'toggle', 'scrollView', 'grid', 'stackPanel', 'inputPanel', 'progressBar', 'itemRenderer', 'comboBox', 'selectionWheel', 'miniMap'] | `'control'` | 传给 [UiControl.getChild](UiControl.md#getChild) 的 kind 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [UiControl](UiControl.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Child paths must be relative without .. components'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getChild(instance, path):
    return instance.getChild(path)
```

## remove {#remove}

```python
remove() -> None
```

移除原生子控件，使已经取得的全部子孙控件句柄失效。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `RemoveChildControl`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_remove(instance):
    return instance.remove()
```

## 使用示例


```python
def resize(control):
    control.setLayout({"width": "100%-16px", "height": 32})
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)