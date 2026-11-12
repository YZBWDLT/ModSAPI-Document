---
title: "UiMiniMap"
sidebar_label: "UiMiniMap"
---

# UiMiniMap

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/minimap.py`；声明补充了静态类型信息。

显示已加载客户端区块的小地图，可管理固定和跟随实体的标记。显示效果由原生模板与渲染规则决定；标记属于地图当前维度，只渲染 X/Z 坐标。

## 获取方式

先以 miniMap=True 注册视图，再使用 view.getControl(path, "miniMap")。

基类：[UiControl](UiControl.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [markers](#markers) | 只读属性 |
| [addMarker](#addMarker) | 方法 |
| [addTextMarker](#addTextMarker) | 方法 |
| [clearMarkers](#clearMarkers) | 方法 |
| [setHeightLimit](#setHeightLimit) | 方法 |
| [refresh](#refresh) | 方法 |
| [zoomIn](#zoomIn) | 方法 |
| [zoomOut](#zoomOut) | 方法 |
| [resetZoom](#resetZoom) | 方法 |

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

## markers {#markers}

```python
markers: tuple[UiMapMarker, ...]
```

本包装对象拥有的标记元组，不包含通过原生接口自行创建的标记。

**访问：** 只读。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[UiMapMarker](UiMapMarker.md), ...]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.markers
```

## addMarker {#addMarker}

```python
addMarker(target: ClientEntity | VectorLike, texture: str, options: UiMapMarkerOptions | None = None) -> UiMapMarker
```

为三维坐标或客户端实体对象添加图片标记。选项包含 size、rotate 和 flipZ；旋转相关选项仅用于实体标记。固定位置保留 Y 坐标，但地图只使用 X/Z。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `target` | [ClientEntity](../../client/reference/ClientEntity.md) \| [VectorLike](../../common/type-aliases.md#vectorlike) | `必填` | 传给 [UiMiniMap.addMarker](UiMiniMap.md#addMarker) 的 target 参数；结合上方功能说明和下方调用示例使用。 |
| `texture` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiMiniMap.addMarker](UiMiniMap.md#addMarker) 的 texture 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [UiMapMarkerOptions](UiMapMarkerOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [UiMapMarker](UiMapMarker.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Rotation options require an entity marker'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `AddEntityMarker`, `AddStaticMarker`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addMarker(instance, target, texture):
    return instance.addMarker(target, texture)
```

## addTextMarker {#addTextMarker}

```python
addTextMarker(target: ClientEntity | VectorLike, label: str, options: UiMapTextMarkerOptions | None = None) -> UiMapMarker
```

在固定位置或实体处添加格式化文字；选项提供文字缩放比例。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `target` | [ClientEntity](../../client/reference/ClientEntity.md) \| [VectorLike](../../common/type-aliases.md#vectorlike) | `必填` | 传给 [UiMiniMap.addTextMarker](UiMiniMap.md#addTextMarker) 的 target 参数；结合上方功能说明和下方调用示例使用。 |
| `label` | [str](../../common/type-system.md#str) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `options` | [UiMapTextMarkerOptions](UiMapTextMarkerOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [UiMapMarker](UiMapMarker.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `AddEntityTextMarker`, `AddStaticTextMarker`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addTextMarker(instance, target, label):
    return instance.addTextMarker(target, label)
```

## clearMarkers {#clearMarkers}

```python
clearMarkers() -> None
```

尝试移除所有拥有的标记后再报告失败，失败的句柄保留以便重试。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `参见本成员的前置条件。` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clearMarkers(instance):
    return instance.clearMarkers()
```

## setHeightLimit {#setHeightLimit}

```python
setHeightLimit(height: int, repaint: bool = True) -> None
```

设置原生地图绘制的最高 Y，默认同时重绘已有区块。重绘可能较耗时；批量调整可传 repaint=False，最后只调用一次 refresh。高度规则取决于游戏版本。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `height` | [int](../../common/type-system.md#int) | `必填` | 传给 [UiMiniMap.setHeightLimit](UiMiniMap.md#setHeightLimit) 的 height 参数；结合上方功能说明和下方调用示例使用。 |
| `repaint` | [bool](../../common/type-system.md#bool) | `True` | 传给 [UiMiniMap.setHeightLimit](UiMiniMap.md#setHeightLimit) 的 repaint 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetHighestY`, `RepaintMiniMap`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setHeightLimit(instance, height):
    return instance.setHeightLimit(height)
```

## refresh {#refresh}

```python
refresh() -> None
```

请求原生重绘，不会因此加载远处的世界区块。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `RepaintMiniMap`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_refresh(instance):
    return instance.refresh()
```

## zoomIn {#zoomIn}

```python
zoomIn(amount: float = 0.05) -> None
```

以非负有限增量放大原生地图。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `amount` | [float](../../common/type-system.md#float) | `0.05` | 物品数量；新物品要求 1–255 的整数，并按最大堆叠数限制。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `ZoomIn`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_zoomIn(instance):
    return instance.zoomIn()
```

## zoomOut {#zoomOut}

```python
zoomOut(amount: float = 0.05) -> None
```

减小原生地图缩放；缩得过小时可能无法显示未加载的区块或部分标记。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `amount` | [float](../../common/type-system.md#float) | `0.05` | 物品数量；新物品要求 1–255 的整数，并按最大堆叠数限制。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `ZoomOut`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_zoomOut(instance):
    return instance.zoomOut()
```

## resetZoom {#resetZoom}

```python
resetZoom() -> None
```

使用无参数的原生重置操作恢复默认地图缩放。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `ZoomReset`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_resetZoom(instance):
    return instance.resetZoom()
```

## 使用示例


```python
def mark_location(mini_map):
    marker = mini_map.addTextMarker((10, 70, 20), u"目标")
    mini_map.zoomIn(0.1)
    return marker
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)