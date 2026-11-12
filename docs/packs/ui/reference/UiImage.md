---
title: "UiImage"
sidebar_label: "UiImage"
---

# UiImage

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/controls.py`；声明补充了静态类型信息。

图片控件，支持贴图、裁剪，以及围绕自身锚点或全局位置的原生旋转。

## 获取方式

使用 view.getControl(path, "image")。

基类：[UiControl](UiControl.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [setImageFit](#setImageFit) | 方法 |
| [clipDirection](#clipDirection) | 可读写属性 |
| [rotation](#rotation) | 只读属性 |
| [rotationPivot](#rotationPivot) | 可读写属性 |
| [orbitPoint](#orbitPoint) | 只读属性 |
| [orbitRotation](#orbitRotation) | 只读属性 |
| [rotate](#rotate) | 方法 |
| [rotateAround](#rotateAround) | 方法 |
| [setClipRatio](#setClipRatio) | 方法 |
| [setImage](#setImage) | 方法 |

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

## setImageFit {#setImageFit}

```python
setImageFit(fit: str, borders: UiImageInsets | None = None) -> None
```

设置 [UiImageFit](UiImageFit.md) 适配方式并检查原生结果。NineSlice 与 LegacyNineSlice 必须传入包含 left、right、top、bottom 的非负有限边距字典；其他模式不接受边距。原生 API 没有提供读取当前适配方式的能力。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fit` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiImage.setImageFit](UiImage.md#setImageFit) 的 fit 参数；结合上方功能说明和下方调用示例使用。 |
| `borders` | [UiImageInsets](UiImageInsets.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [UiImage.setImageFit](UiImage.md#setImageFit) 的 borders 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'borders must be a dictionary'` |
| [ValueError](../../common/type-system.md#valueerror) | `'borders requires left, right, top and bottom'` |
| [ValueError](../../common/type-system.md#valueerror) | `'borders require a nine-slice fitting mode'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetImageAdaptionType`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setImageFit(instance, fit):
    return instance.setImageFit(fit)
```

## clipDirection {#clipDirection}

```python
clipDirection: str
```

原生裁剪方向，使用 [UiImageClipDirection](UiImageClipDirection.md) 常量。

**访问：** 可读写。

写入方式：`instance.clipDirection = value`。参数类型线索：`(value: str) -> None`。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.clipDirection

def write_value(instance, value):
    instance.clipDirection = value
```

## rotation {#rotation}

```python
rotation: float
```

图片围绕自身相对锚点的原生旋转角度，单位为度。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.rotation
```

## rotationPivot {#rotationPivot}

```python
rotationPivot: tuple[float, float]
```

相对旋转锚点坐标；原生默认值为 (0.5, 0.5)。

**访问：** 可读写。

写入方式：`instance.rotationPivot = value`。参数类型线索：`(value: tuple[float, float]) -> None`。

写入参数 `value`：[tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.rotationPivot

def write_value(instance, value):
    instance.rotationPivot = value
```

## orbitPoint {#orbitPoint}

```python
orbitPoint: tuple[float, float]
```

最近一次通过 rotateAround 设置的全局界面位置。

**访问：** 只读。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.orbitPoint
```

## orbitRotation {#orbitRotation}

```python
orbitRotation: float
```

最近一次通过 rotateAround 设置的全局锚点旋转角度。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.orbitRotation
```

## rotate {#rotate}

```python
rotate(angle: float) -> None
```

以 rotationPivot 为锚点，向原生接口传入旋转角度，单位为度。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `angle` | [float](../../common/type-system.md#float) | `必填` | 传给 [UiImage.rotate](UiImage.md#rotate) 的 angle 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `Rotate`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_rotate(instance, angle):
    return instance.rotate(angle)
```

## rotateAround {#rotateAround}

```python
rotateAround(point: tuple[float, float], angle: float) -> None
```

围绕固定的全局界面位置旋转，采用原生角度约定。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `point` | [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] | `必填` | 传给 [UiImage.rotateAround](UiImage.md#rotateAround) 的 point 参数；结合上方功能说明和下方调用示例使用。 |
| `angle` | [float](../../common/type-system.md#float) | `必填` | 传给 [UiImage.rotateAround](UiImage.md#rotateAround) 的 angle 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `RotateAround`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_rotateAround(instance, point, angle):
    return instance.rotateAround(point, angle)
```

## setClipRatio {#setClipRatio}

```python
setClipRatio(value: float) -> None
```

设置 `setClipRatio` 操作。原生实现使用 `SetSpriteClipRatio`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `value` | [float](../../common/type-system.md#float) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetSpriteClipRatio`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setClipRatio(instance, value):
    return instance.setClipRatio(value)
```

## setImage {#setImage}

```python
setImage(texture: str, options: dict[str, Any] | None = None) -> None
```

设置 `setImage` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `texture` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiImage.setImage](UiImage.md#setImage) 的 texture 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setImage(instance, texture):
    return instance.setImage(texture)
```

## 使用示例


```python
def set_icon(image):
    image.setImage("textures/items/diamond")
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)