---
title: architect.math.mat4
---

# architect.math.mat4

这是核心包的架构辅助模块，不是模板 beta 入口的直接导出。下方示例中的 module 是此模块对象；仅在核心包开发或已经取得模块对象时使用。

## identity {#identity}

```python
identity() -> Matrix
```

执行 identity 架构辅助操作。

返回类型： [Matrix](../../common/type-system.md#matrix).


```python
def use_function(module):
    return module.identity()
```

## lookAt {#lookAt}

```python
lookAt(eye: Vector3, target: Vector3, up: Vector3) -> Matrix
```

执行 lookAt 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `eye` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |
| `target` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |
| `up` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |

返回类型： [Matrix](../../common/type-system.md#matrix).


```python
def use_function(module, eye, target, up):
    return module.lookAt(eye, target, up)
```

## perspective {#perspective}

```python
perspective(fov_degrees: float, aspect: float, near: float, far: float) -> Matrix
```

执行 perspective 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `fov_degrees` | [float](../../common/type-system.md#float) | `必填` |
| `aspect` | [float](../../common/type-system.md#float) | `必填` |
| `near` | [float](../../common/type-system.md#float) | `必填` |
| `far` | [float](../../common/type-system.md#float) | `必填` |

返回类型： [Matrix](../../common/type-system.md#matrix).


```python
def use_function(module, fov_degrees, aspect, near, far):
    return module.perspective(fov_degrees, aspect, near, far)
```

## multiply {#multiply}

```python
multiply(a: Matrix, b: Matrix) -> Matrix
```

执行 multiply 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `a` | [Matrix](../../common/type-system.md#matrix) | `必填` |
| `b` | [Matrix](../../common/type-system.md#matrix) | `必填` |

返回类型： [Matrix](../../common/type-system.md#matrix).


```python
def use_function(module, a, b):
    return module.multiply(a, b)
```

## transpose {#transpose}

```python
transpose(m: Matrix) -> Matrix
```

执行 transpose 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `m` | [Matrix](../../common/type-system.md#matrix) | `必填` |

返回类型： [Matrix](../../common/type-system.md#matrix).


```python
def use_function(module, m):
    return module.transpose(m)
```

## inverse {#inverse}

```python
inverse(m: Matrix) -> Matrix
```

执行 inverse 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `m` | [Matrix](../../common/type-system.md#matrix) | `必填` |

返回类型： [Matrix](../../common/type-system.md#matrix).


```python
def use_function(module, m):
    return module.inverse(m)
```

## translate {#translate}

```python
translate(v: Vector3) -> Matrix
```

执行 translate 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `v` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |

返回类型： [Matrix](../../common/type-system.md#matrix).


```python
def use_function(module, v):
    return module.translate(v)
```

## rotateAxis {#rotateAxis}

```python
rotateAxis(axis: Vector3, angle: float) -> Matrix
```

执行 rotateAxis 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `axis` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |
| `angle` | [float](../../common/type-system.md#float) | `必填` |

返回类型： [Matrix](../../common/type-system.md#matrix).


```python
def use_function(module, axis, angle):
    return module.rotateAxis(axis, angle)
```

## rotateX {#rotateX}

```python
rotateX(angle: float) -> Matrix
```

执行 rotateX 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `angle` | [float](../../common/type-system.md#float) | `必填` |

返回类型： [Matrix](../../common/type-system.md#matrix).


```python
def use_function(module, angle):
    return module.rotateX(angle)
```

## rotateY {#rotateY}

```python
rotateY(angle: float) -> Matrix
```

执行 rotateY 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `angle` | [float](../../common/type-system.md#float) | `必填` |

返回类型： [Matrix](../../common/type-system.md#matrix).


```python
def use_function(module, angle):
    return module.rotateY(angle)
```

## rotateZ {#rotateZ}

```python
rotateZ(angle: float) -> Matrix
```

执行 rotateZ 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `angle` | [float](../../common/type-system.md#float) | `必填` |

返回类型： [Matrix](../../common/type-system.md#matrix).


```python
def use_function(module, angle):
    return module.rotateZ(angle)
```

## rotateXYZ {#rotateXYZ}

```python
rotateXYZ(roll: float, yaw: float, pitch: float) -> Matrix
```

右手系摄像机正方向为 -Z 轴

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `roll` | [float](../../common/type-system.md#float) | `必填` |
| `yaw` | [float](../../common/type-system.md#float) | `必填` |
| `pitch` | [float](../../common/type-system.md#float) | `必填` |

返回类型： [Matrix](../../common/type-system.md#matrix).


```python
def use_function(module, roll, yaw, pitch):
    return module.rotateXYZ(roll, yaw, pitch)
```

## scale {#scale}

```python
scale(s: Vector3) -> Matrix
```

执行 scale 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `s` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |

返回类型： [Matrix](../../common/type-system.md#matrix).


```python
def use_function(module, s):
    return module.scale(s)
```

## transform {#transform}

```python
transform(m: Matrix, t: Vector3, r: Vector3, s: Vector3) -> Matrix
```

标准模型变换矩阵：先缩放(S)，再旋转(R)，最后平移([T](../../common/type-system.md#typevar))
旋转顺序：绕Z轴(r.z)、绕Y轴(r.y)、绕X轴(r.x)（右手系，逆时针为正）
矩阵乘法顺序：M_final = M_parent * [T](../../common/type-system.md#typevar) * R * S
其中 M_parent 为输入矩阵 m（通常为单位矩阵或父节点变换）

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `m` | [Matrix](../../common/type-system.md#matrix) | `必填` |
| `t` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |
| `r` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |
| `s` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |

返回类型： [Matrix](../../common/type-system.md#matrix).


```python
def use_function(module, m, t, r, s):
    return module.transform(m, t, r, s)
```

## transformPoint {#transformPoint}

```python
transformPoint(m: Matrix, point: Vector3) -> Vector3
```

使用矩阵变换一个点（包含平移影响）
将点表示为齐次坐标 [x, y, z, 1] 并进行矩阵乘法
返回变换后的 [Vector3](../../common/type-system.md#nativevector3)

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `m` | [Matrix](../../common/type-system.md#matrix) | `必填` |
| `point` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |

返回类型： [Vector3](../../common/type-system.md#nativevector3).


```python
def use_function(module, m, point):
    return module.transformPoint(m, point)
```

## transformVector {#transformVector}

```python
transformVector(m: Matrix, vector: Vector3) -> Vector3
```

使用矩阵变换一个向量（忽略平移影响）
将向量表示为齐次坐标 [x, y, z, 0] 并进行矩阵乘法
返回变换后的 [Vector3](../../common/type-system.md#nativevector3)，适用于法线、方向等

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `m` | [Matrix](../../common/type-system.md#matrix) | `必填` |
| `vector` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |

返回类型： [Vector3](../../common/type-system.md#nativevector3).


```python
def use_function(module, m, vector):
    return module.transformVector(m, vector)
```

## localToWorld {#localToWorld}

```python
localToWorld(modelMatrix: Matrix, localPoint: Vector3) -> Vector3
```

将模型局部坐标系中的点转换到世界坐标系
modelMatrix: 模型到世界的变换矩阵（即模型的世界矩阵）
localPoint: 在模型局部坐标系中的点
返回世界坐标系中的点

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `modelMatrix` | [Matrix](../../common/type-system.md#matrix) | `必填` |
| `localPoint` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |

返回类型： [Vector3](../../common/type-system.md#nativevector3).


```python
def use_function(module, modelMatrix, localPoint):
    return module.localToWorld(modelMatrix, localPoint)
```

## worldToLocal {#worldToLocal}

```python
worldToLocal(modelMatrix: Matrix, worldPoint: Vector3) -> Vector3
```

将世界坐标系中的点转换到模型局部坐标系
modelMatrix: 模型到世界的变换矩阵（即模型的世界矩阵）
worldPoint: 在世界坐标系中的点
返回模型局部坐标系中的点（相对于模型的本地坐标）

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `modelMatrix` | [Matrix](../../common/type-system.md#matrix) | `必填` |
| `worldPoint` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |

返回类型： [Vector3](../../common/type-system.md#nativevector3).


```python
def use_function(module, modelMatrix, worldPoint):
    return module.worldToLocal(modelMatrix, worldPoint)
```

## worldToScreen {#worldToScreen}

```python
worldToScreen(modelMatrix: Matrix, viewMatrix: Matrix, projectionMatrix: Matrix, viewport: tuple[int, int], worldPoint: Vector3) -> Vector3
```

将世界坐标系中的点转换到屏幕坐标系
modelMatrix: 模型到世界的变换矩阵（即模型的世界矩阵）
viewMatrix: 世界到视图的变换矩阵（即摄像机矩阵）
projectionMatrix: 视图到投影的变换矩阵（即投影矩阵）
viewport: 屏幕视口（即窗口）
worldPoint: 在世界坐标系中的点
返回屏幕坐标系中的点（x, y为屏幕坐标，z为深度值）

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `modelMatrix` | [Matrix](../../common/type-system.md#matrix) | `必填` |
| `viewMatrix` | [Matrix](../../common/type-system.md#matrix) | `必填` |
| `projectionMatrix` | [Matrix](../../common/type-system.md#matrix) | `必填` |
| `viewport` | [tuple](../../common/type-system.md#tuple)[[int](../../common/type-system.md#int), [int](../../common/type-system.md#int)] | `必填` |
| `worldPoint` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |

返回类型： [Vector3](../../common/type-system.md#nativevector3).


```python
def use_function(module, modelMatrix, viewMatrix, projectionMatrix, viewport, worldPoint):
    return module.worldToScreen(modelMatrix, viewMatrix, projectionMatrix, viewport, worldPoint)
```

## screenToWorld {#screenToWorld}

```python
screenToWorld(modelMatrix: Matrix, viewMatrix: Matrix, projectionMatrix: Matrix, viewport: tuple[int, int], screenPoint: Vector3, depth: float) -> Vector3
```

将屏幕坐标系中的点转换到世界坐标系
modelMatrix: 模型到世界的变换矩阵（即模型的世界矩阵）
viewMatrix: 世界到视图的变换矩阵（即摄像机矩阵）
projectionMatrix: 视图到投影的变换矩阵（即投影矩阵）
viewport: 屏幕视口（即窗口）
screenPoint: 在屏幕坐标系中的点（x, y为屏幕坐标，z为深度值）
depth: 深度值（从摄像机到点的距离）
返回世界坐标系中的点

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `modelMatrix` | [Matrix](../../common/type-system.md#matrix) | `必填` |
| `viewMatrix` | [Matrix](../../common/type-system.md#matrix) | `必填` |
| `projectionMatrix` | [Matrix](../../common/type-system.md#matrix) | `必填` |
| `viewport` | [tuple](../../common/type-system.md#tuple)[[int](../../common/type-system.md#int), [int](../../common/type-system.md#int)] | `必填` |
| `screenPoint` | [Vector3](../../common/type-system.md#nativevector3) | `必填` |
| `depth` | [float](../../common/type-system.md#float) | `必填` |

返回类型： [Vector3](../../common/type-system.md#nativevector3).


```python
def use_function(module, modelMatrix, viewMatrix, projectionMatrix, viewport, screenPoint, depth):
    return module.screenToWorld(modelMatrix, viewMatrix, projectionMatrix, viewport, screenPoint, depth)
```