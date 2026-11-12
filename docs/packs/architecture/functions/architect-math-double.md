---
title: architect.math.double
---

# architect.math.double

这是核心包的架构辅助模块，不是模板 beta 入口的直接导出。下方示例中的 module 是此模块对象；仅在核心包开发或已经取得模块对象时使用。

## lerp {#lerp}

```python
lerp(a, b, t)
```

执行 lerp 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `a` | 由值/所属选项确定 | `必填` |
| `b` | 由值/所属选项确定 | `必填` |
| `t` | 由值/所属选项确定 | `必填` |


```python
def use_function(module, a, b, t):
    return module.lerp(a, b, t)
```

## clamp {#clamp}

```python
clamp(x, min, max)
```

执行 clamp 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `x` | 由值/所属选项确定 | `必填` |
| `min` | 由值/所属选项确定 | `必填` |
| `max` | 由值/所属选项确定 | `必填` |


```python
def use_function(module, x, min, max):
    return module.clamp(x, min, max)
```

## smoothstep {#smoothstep}

```python
smoothstep(edge0: float, edge1: float, x: float) -> float
```

执行 smoothstep 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `edge0` | [float](../../common/type-system.md#float) | `必填` |
| `edge1` | [float](../../common/type-system.md#float) | `必填` |
| `x` | [float](../../common/type-system.md#float) | `必填` |

返回类型： [float](../../common/type-system.md#float).


```python
def use_function(module, edge0, edge1, x):
    return module.smoothstep(edge0, edge1, x)
```