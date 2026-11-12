---
title: architect.math.utilsServer
---

# architect.math.utilsServer

这是核心包的架构辅助模块，不是模板 beta 入口的直接导出。下方示例中的 module 是此模块对象；仅在核心包开发或已经取得模块对象时使用。

## pointInBox {#pointInBox}

```python
pointInBox(point: tuple[float, float, float], box: tuple[float, float, float]) -> bool
```

执行 pointInBox 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `point` | [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] | `必填` |
| `box` | [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] | `必填` |

返回类型： [bool](../../common/type-system.md#bool).


```python
def use_function(module, point, box):
    return module.pointInBox(point, box)
```

## boxOverlap3dServer {#boxOverlap3dServer}

```python
boxOverlap3dServer(pos: tuple[float, float, float], rot: tuple[float, float, float], size: tuple[float, float, float], dim: int) -> list[str]
```

执行 boxOverlap3dServer 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `pos` | [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] | `必填` |
| `rot` | [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] | `必填` |
| `size` | [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] | `必填` |
| `dim` | [int](../../common/type-system.md#int) | `必填` |

返回类型： [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)].


```python
def use_function(module, pos, rot, size, dim):
    return module.boxOverlap3dServer(pos, rot, size, dim)
```

## boxOverlap3dForward {#boxOverlap3dForward}

```python
boxOverlap3dForward(entityId, size)
```

执行 boxOverlap3dForward 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` |
| `size` | 由值/所属选项确定 | `必填` |


```python
def use_function(module, entityId, size):
    return module.boxOverlap3dForward(entityId, size)
```

## facing {#facing}

```python
facing(entityId)
```

执行 facing 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` |


```python
def use_function(module, entityId):
    return module.facing(entityId)
```

## forward {#forward}

```python
forward(entityId)
```

执行 forward 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` |


```python
def use_function(module, entityId):
    return module.forward(entityId)
```