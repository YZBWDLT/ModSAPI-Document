---
title: "ClientCamera"
sidebar_label: "ClientCamera"
---

# ClientCamera

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Camera.py`；声明补充了静态类型信息。

控制本地原生相机，向量须为有限数，角度单位为度。参数不合法时抛出 [TypeError](../../common/type-system.md#typeerror) 或 [ValueError](../../common/type-system.md#valueerror)；原生拒绝操作时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)。改动是临时的，可能在下一渲染帧才可见。

## 获取方式

使用 [client.camera](../apis/manager.md#camera)。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `position` | 由运行时值确定 | `location` |
| `rangeY` | 由运行时值确定 | `pitchLimits` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [location](#location) | 可读写属性 |
| [rotation](#rotation) | 可读写属性 |
| [anchor](#anchor) | 可读写属性 |
| [offset](#offset) | 可读写属性 |
| [fov](#fov) | 可读写属性 |
| [pitchLimits](#pitchLimits) | 可读写属性 |
| [perspective](#perspective) | 可读写属性 |
| [detach](#detach) | 方法 |
| [resetPosition](#resetPosition) | 方法 |
| [lock](#lock) | 方法 |
| [unlock](#unlock) | 方法 |
| [getAllMotions](#getAllMotions) | 方法 |

## 构造器 {#constructor}

```python
ClientCamera(playerId: str | None = None, owner: Any = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `playerId` | [str](../../common/type-system.md#str) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 玩家运行 ID，不是玩家显示名称。 |
| `owner` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 传给 [ClientCamera.__init__](ClientCamera.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## location {#location}

```python
location: Vector3
```

相机中心的世界坐标。赋值前会先解除相机跟随。

:::note 当前实现说明
写入前脱离跟随。后续设置失败不能保证回滚脱离操作。
:::

**访问：** 可读写。

写入方式：`instance.location = value`。参数类型线索：`(value: VectorLike) -> None`。

写入参数 `value`：[VectorLike](../../common/type-aliases.md#vectorlike)。

**返回类型：** [Vector3](../../server/extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.location

def write_value(instance, value):
    instance.location = value
```

## rotation {#rotation}

```python
rotation: Vector3
```

使用原生角度约定，x、y、z 分别表示俯仰、偏航和翻滚，单位为度。

:::note 当前实现说明
x/y/z = pitch/yaw/roll，单位为度，采用网易原生约定。
:::

**访问：** 可读写。

写入方式：`instance.rotation = value`。参数类型线索：`(value: VectorLike) -> None`。

写入参数 `value`：[VectorLike](../../common/type-aliases.md#vectorlike)。

**返回类型：** [Vector3](../../server/extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.rotation

def write_value(instance, value):
    instance.rotation = value
```

## anchor {#anchor}

```python
anchor: Vector3
```

相机环绕中心的偏移，也会影响客户端交互起点。

**访问：** 可读写。

写入方式：`instance.anchor = value`。参数类型线索：`(value: VectorLike) -> None`。

写入参数 `value`：[VectorLike](../../common/type-aliases.md#vectorlike)。

**返回类型：** [Vector3](../../server/extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.anchor

def write_value(instance, value):
    instance.anchor = value
```

## offset {#offset}

```python
offset: Vector3
```

相机相对环绕中心的偏移，使用原生坐标约定。

**访问：** 可读写。

写入方式：`instance.offset = value`。参数类型线索：`(value: VectorLike) -> None`。

写入参数 `value`：[VectorLike](../../common/type-aliases.md#vectorlike)。

**返回类型：** [Vector3](../../server/extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.offset

def write_value(instance, value):
    instance.offset = value
```

## fov {#fov}

```python
fov: float
```

视野角度，取值范围为 30–110 度，包含端点。

:::note 当前实现说明
有限角度，闭区间 30–110 度。
:::

**访问：** 可读写。

写入方式：`instance.fov = value`。参数类型线索：`(value: float) -> None`。

写入参数 `value`：[float](../../common/type-system.md#float)。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetFov`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.fov

def write_value(instance, value):
    instance.fov = value
```

## pitchLimits {#pitchLimits}

```python
pitchLimits: tuple[float, float]
```

相机俯仰角的最小值和最大值，以二元组表示，单位为度。

:::note 当前实现说明
(minimum, maximum)，各自在 -90–90 度内且 minimum &lt;= maximum。
:::

**访问：** 可读写。

写入方式：`instance.pitchLimits = value`。参数类型线索：`(value: tuple[float, float]) -> None`。

写入参数 `value`：[tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'pitchLimits requires a two-value sequence'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Minimum pitch must not exceed maximum pitch'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetCameraPitchLimit`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.pitchLimits

def write_value(instance, value):
    instance.pitchLimits = value
```

## perspective {#perspective}

```python
perspective: str
```

当前 [ClientPerspective](ClientPerspective.md) 值；开发包返回未知值时抛出异常。

**访问：** 可读写。

写入方式：`instance.perspective = value`。参数类型线索：`(value: str) -> None`。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetPerspective'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown ClientPerspective'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPerspective`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.perspective

def write_value(instance, value):
    instance.perspective = value
```

## detach {#detach}

```python
detach() -> None
```

将相机旋转与玩家朝向分离，同时清除原生锁定。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `DepartCamera`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_detach(instance):
    return instance.detach()
```

## resetPosition {#resetPosition}

```python
resetPosition() -> None
```

设置位置后恢复跟随玩家，保留视野角度和偏移。

:::note 当前实现说明
恢复跟随，不自动恢复 FOV、偏移、俯仰限制或视角模式。
:::

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `ResetCameraPos`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_resetPosition(instance):
    return instance.resetPosition()
```

## lock {#lock}

```python
lock(location: VectorLike, rotation: VectorLike) -> None
```

固定视角，不禁用玩家移动。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [VectorLike](../../common/type-aliases.md#vectorlike) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `rotation` | [VectorLike](../../common/type-aliases.md#vectorlike) | `必填` | 旋转角度，具体分量与单位参见成员说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `LockCamera`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_lock(instance, location, rotation):
    return instance.lock(location, rotation)
```

## unlock {#unlock}

```python
unlock() -> None
```

解除原生相机锁定及俯仰、偏航移动锁定。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `UnLockCamera`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_unlock(instance):
    return instance.unlock()
```

## getAllMotions {#getAllMotions}

```python
getAllMotions() -> dict[int, int]
```

返回原生运动标识到运动类型的独立字典副本。

**返回类型：** [dict](../../common/type-system.md#dict)[[int](../../common/type-system.md#int), [int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetCameraMotions'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetCameraMotions`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getAllMotions(instance):
    return instance.getAllMotions()
```

## 使用示例


```python
from ModSAPI.client.beta import client, ClientPerspective

camera = client.camera
camera.perspective = ClientPerspective.ThirdPersonBack
camera.fov = 75
print(camera.pitchLimits)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)