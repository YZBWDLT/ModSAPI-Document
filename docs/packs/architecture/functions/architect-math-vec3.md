---
title: architect.math.vec3
---

# architect.math.vec3

这是核心包的架构辅助模块，不是模板 beta 入口的直接导出。下方示例中的 module 是此模块对象；仅在核心包开发或已经取得模块对象时使用。

## vec {#vec}

```python
vec(tup)
```

执行 vec 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `tup` | 由值/所属选项确定 | `必填` |


```python
def use_function(module, tup):
    return module.vec(tup)
```

## add {#add}

```python
add(a: Vector3, b: Vector3) -> Vector3
```

执行 add 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `a` | [Vector3](../../server/extra/vector.md) | `必填` |
| `b` | [Vector3](../../server/extra/vector.md) | `必填` |

返回类型： [Vector3](../../server/extra/vector.md).


```python
def use_function(module, a, b):
    return module.add(a, b)
```

## sub {#sub}

```python
sub(a: Vector3, b: Vector3) -> Vector3
```

执行 sub 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `a` | [Vector3](../../server/extra/vector.md) | `必填` |
| `b` | [Vector3](../../server/extra/vector.md) | `必填` |

返回类型： [Vector3](../../server/extra/vector.md).


```python
def use_function(module, a, b):
    return module.sub(a, b)
```

## mul {#mul}

```python
mul(a: Vector3, b: float | int) -> Vector3
```

执行 mul 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `a` | [Vector3](../../server/extra/vector.md) | `必填` |
| `b` | [float](../../common/type-system.md#float) \| [int](../../common/type-system.md#int) | `必填` |

返回类型： [Vector3](../../server/extra/vector.md).


```python
def use_function(module, a, b):
    return module.mul(a, b)
```

## div {#div}

```python
div(a: Vector3, b: float | int) -> Vector3
```

执行 div 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `a` | [Vector3](../../server/extra/vector.md) | `必填` |
| `b` | [float](../../common/type-system.md#float) \| [int](../../common/type-system.md#int) | `必填` |

返回类型： [Vector3](../../server/extra/vector.md).


```python
def use_function(module, a, b):
    return module.div(a, b)
```

## dot {#dot}

```python
dot(a: Vector3, b: Vector3) -> float
```

执行 dot 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `a` | [Vector3](../../server/extra/vector.md) | `必填` |
| `b` | [Vector3](../../server/extra/vector.md) | `必填` |

返回类型： [float](../../common/type-system.md#float).


```python
def use_function(module, a, b):
    return module.dot(a, b)
```

## cross {#cross}

```python
cross(a: Vector3, b: Vector3) -> Vector3
```

执行 cross 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `a` | [Vector3](../../server/extra/vector.md) | `必填` |
| `b` | [Vector3](../../server/extra/vector.md) | `必填` |

返回类型： [Vector3](../../server/extra/vector.md).


```python
def use_function(module, a, b):
    return module.cross(a, b)
```

## modulo {#modulo}

```python
modulo(a: Vector3) -> float
```

执行 modulo 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `a` | [Vector3](../../server/extra/vector.md) | `必填` |

返回类型： [float](../../common/type-system.md#float).


```python
def use_function(module, a):
    return module.modulo(a)
```

## moduloSqrt {#moduloSqrt}

```python
moduloSqrt(a: Vector3) -> float
```

执行 moduloSqrt 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `a` | [Vector3](../../server/extra/vector.md) | `必填` |

返回类型： [float](../../common/type-system.md#float).


```python
def use_function(module, a):
    return module.moduloSqrt(a)
```

## normalize {#normalize}

```python
normalize(a: Vector3) -> Vector3
```

执行 normalize 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `a` | [Vector3](../../server/extra/vector.md) | `必填` |

返回类型： [Vector3](../../server/extra/vector.md).


```python
def use_function(module, a):
    return module.normalize(a)
```

## compare {#compare}

```python
compare(a: Vector3, b: Vector3) -> float
```

a 大于 b 时为 Greater，小于时为 Less，相等时为 Equal。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `a` | [Vector3](../../server/extra/vector.md) | `必填` |
| `b` | [Vector3](../../server/extra/vector.md) | `必填` |

返回类型： [float](../../common/type-system.md#float).


```python
def use_function(module, a, b):
    return module.compare(a, b)
```

## clamp {#clamp}

```python
clamp(v: Vector3, min: float, max: float) -> Vector3
```

执行 clamp 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `v` | [Vector3](../../server/extra/vector.md) | `必填` |
| `min` | [float](../../common/type-system.md#float) | `必填` |
| `max` | [float](../../common/type-system.md#float) | `必填` |

返回类型： [Vector3](../../server/extra/vector.md).

显式异常：[ValueError](../../common/type-system.md#valueerror): `'Vector length bounds must satisfy 0 <= min <= max'`


```python
def use_function(module, v, min, max):
    return module.clamp(v, min, max)
```

## lerp {#lerp}

```python
lerp(a: Vector3, b: Vector3, t: float) -> Vector3
```

执行 lerp 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `a` | [Vector3](../../server/extra/vector.md) | `必填` |
| `b` | [Vector3](../../server/extra/vector.md) | `必填` |
| `t` | [float](../../common/type-system.md#float) | `必填` |

返回类型： [Vector3](../../server/extra/vector.md).


```python
def use_function(module, a, b, t):
    return module.lerp(a, b, t)
```

## nlerp {#nlerp}

```python
nlerp(a: Vector3, b: Vector3, t: float) -> Vector3
```

a和b应为单位向量，否则插值不经过起点和终点

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `a` | [Vector3](../../server/extra/vector.md) | `必填` |
| `b` | [Vector3](../../server/extra/vector.md) | `必填` |
| `t` | [float](../../common/type-system.md#float) | `必填` |

返回类型： [Vector3](../../server/extra/vector.md).


```python
def use_function(module, a, b, t):
    return module.nlerp(a, b, t)
```