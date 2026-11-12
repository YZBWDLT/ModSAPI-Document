---
title: "UiModelRenderer"
sidebar_label: "UiModelRenderer"
---

# UiModelRenderer

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/renderers.py`；声明补充了静态类型信息。

由当前视图管理的网易模型预览控件。切换预览内容只更新控件，不向世界发起创建实体的请求。省略的选项沿用原生默认值；关闭视图或移除控件时，沿用引擎的界面所有权释放预览。

## 获取方式

使用 view.getControl(path, "modelRenderer")；模板使用网易模型预览渲染器。

基类：[UiControl](UiControl.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [setEntity](#setEntity) | 方法 |
| [setSkeletonModel](#setSkeletonModel) | 方法 |
| [setBlockGeometry](#setBlockGeometry) | 方法 |

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

## setEntity {#setEntity}

```python
setEntity(entity: ClientEntity | str, options: UiEntityRenderOptions | None = None) -> None
```

显示有效的 [ClientEntity](../../client/reference/ClientEntity.md) 或带命名空间的实体定义。实体对象必须属于当前客户端并保持可见；字符串只表示 minecraft:cow 这样的定义，不能传运行时实体编号。变换与深度在渲染前校验；原生拒绝时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `entity` | [ClientEntity](../../client/reference/ClientEntity.md) \| [str](../../common/type-system.md#str) | `必填` | 目标实体句柄；是否接受运行 ID 取决于签名。 |
| `options` | [UiEntityRenderOptions](UiEntityRenderOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Entity definitions require namespace:name syntax'` |
| [TypeError](../../common/type-system.md#typeerror) | `'entity must be a ClientEntity or a namespaced definition'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `RenderEntity`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setEntity(instance, entity):
    return instance.setEntity(entity)
```

## setSkeletonModel {#setSkeletonModel}

```python
setSkeletonModel(model: str, options: UiSkeletonRenderOptions | None = None) -> None
```

显示已注册的网易骨骼模型。支持变换、深度、动画、循环和光照方向；光照各坐标为 -1、0 或 1，并受到自定义材质与设备能力的限制。原生拒绝时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `model` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiModelRenderer.setSkeletonModel](UiModelRenderer.md#setSkeletonModel) 的 model 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [UiSkeletonRenderOptions](UiSkeletonRenderOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `RenderSkeletonModel`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setSkeletonModel(instance, model):
    return instance.setSkeletonModel(model)
```

## setBlockGeometry {#setBlockGeometry}

```python
setBlockGeometry(geometry: str, options: UiModelTransformOptions | None = None) -> None
```

显示已经生成的方块网格体。支持缩放、角度、旋转轴与变量；重新进入世界后需要重新生成该资源。本方法不负责生成或持久化网格体；原生拒绝时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `geometry` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiModelRenderer.setBlockGeometry](UiModelRenderer.md#setBlockGeometry) 的 geometry 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [UiModelTransformOptions](UiModelTransformOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `RenderBlockGeometryModel`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setBlockGeometry(instance, geometry):
    return instance.setBlockGeometry(geometry)
```

## 使用示例


```python
from ModSAPI.client.beta import client

def show_player(view):
    preview = view.getControl("/preview", "modelRenderer")
    preview.setEntity(client.localPlayer, {"scale": 0.8, "rotation": (0, 30, 0)})
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)