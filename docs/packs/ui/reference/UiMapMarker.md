---
title: "UiMapMarker"
sidebar_label: "UiMapMarker"
---

# UiMapMarker

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/minimap.py`；声明补充了静态类型信息。

由界面管理的图片或文字标记，移除时不影响其他标记。

## 获取方式

由 [UiMiniMap.addMarker](UiMiniMap.md#addMarker) 或 addTextMarker 返回；使用 remove 移除。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [miniMap](#miniMap) | 只读属性 |
| [entity](#entity) | 只读属性 |
| [location](#location) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [remove](#remove) | 方法 |

## miniMap {#miniMap}

```python
miniMap: UiMiniMap
```

拥有当前标记的小地图控件。

**访问：** 只读。

**返回类型：** [UiMiniMap](UiMiniMap.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.miniMap
```

## entity {#entity}

```python
entity: ClientEntity | None
```

被跟踪的客户端实体包装对象；固定标记为 [None](../../common/type-system.md#none)。

**访问：** 只读。

**返回类型：** [ClientEntity](../../client/reference/ClientEntity.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entity
```

## location {#location}

```python
location: Vector3 | None
```

固定标记的位置副本；跟随实体的标记返回 [None](../../common/type-system.md#none)。原生地图只使用 X/Z 坐标，Y 坐标保留在输入快照中。

**访问：** 只读。

**返回类型：** [Vector3](../../server/extra/vector.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.location
```

## isValid {#isValid}

```python
isValid: bool
```

本库拥有的句柄及地图是否仍存活，不包含绕过包装层的外部修改。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## remove {#remove}

```python
remove() -> None
```

仅移除当前标记；原生移除失败时保留句柄，可再次重试。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_remove(instance):
    return instance.remove()
```

## 使用示例


```python
def remove_marker(marker):
    marker.remove()
    marker.remove()
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)