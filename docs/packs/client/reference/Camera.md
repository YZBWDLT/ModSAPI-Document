---
title: "Camera"
sidebar_label: "Camera"
---

import ApiFieldAnchor from '@docusaurus/Link';

# Camera

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Camara.py`；声明补充了静态类型信息。

微软相机预设的占位接口；原生相机控制请使用 [client.camera](../apis/manager.md#camera)。未支持的方法会抛出异常。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-playerId" />`playerId` | [str](../../common/type-system.md#str) | `playerId` | 微软相机预设的占位接口；原生相机控制请使用 [client.camera](../apis/manager.md#camera)。未支持的方法会抛出异常。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [clear](#clear) | 方法 |
| [fade](#fade) | 方法 |
| [setCamera](#setCamera) | 方法 |
| [setDefaultCamera](#setDefaultCamera) | 方法 |

## 构造器 {#constructor}

```python
Camera(playerId: str) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `playerId` | [str](../../common/type-system.md#str) | `必填` | 玩家运行 ID，不是玩家显示名称。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## clear {#clear}

```python
clear() -> None
```

尚未实现微软相机的完整重置操作，调用会抛出异常。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md) | `'Microsoft Camera.clear is not implemented'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clear(instance):
    return instance.clear()
```

## fade {#fade}

```python
fade(fadeCameraOptions: Any = None) -> None
```

尚未实现微软相机的全屏渐变操作，调用会抛出异常。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fadeCameraOptions` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 传给 [Camera.fade](Camera.md#fade) 的 fadeCameraOptions 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md) | `'Microsoft Camera.fade is not implemented'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_fade(instance):
    return instance.fade()
```

## setCamera {#setCamera}

```python
setCamera(cameraPreset: str, setOptions: Any = None) -> None
```

尚未实现微软相机预设选择，调用会抛出异常。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `cameraPreset` | [str](../../common/type-system.md#str) | `必填` | 传给 [Camera.setCamera](Camera.md#setCamera) 的 cameraPreset 参数；结合上方功能说明和下方调用示例使用。 |
| `setOptions` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 传给 [Camera.setCamera](Camera.md#setCamera) 的 setOptions 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md) | `'Microsoft Camera.setCamera is not implemented'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setCamera(instance, cameraPreset):
    return instance.setCamera(cameraPreset)
```

## setDefaultCamera {#setDefaultCamera}

```python
setDefaultCamera(cameraPreset: str, easeOptions: Any = None) -> None
```

尚未实现微软默认相机预设，调用会抛出异常。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `cameraPreset` | [str](../../common/type-system.md#str) | `必填` | 传给 [Camera.setDefaultCamera](Camera.md#setDefaultCamera) 的 cameraPreset 参数；结合上方功能说明和下方调用示例使用。 |
| `easeOptions` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 传给 [Camera.setDefaultCamera](Camera.md#setDefaultCamera) 的 easeOptions 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md) | `'Microsoft Camera.setDefaultCamera is not implemented'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setDefaultCamera(instance, cameraPreset):
    return instance.setDefaultCamera(cameraPreset)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 Camera 对象。
    print(value.playerId)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)