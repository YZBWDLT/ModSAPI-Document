---
title: "Particle"
sidebar_label: "Particle"
---

# Particle

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Particle.py`；声明补充了静态类型信息。

单个粒子发射器。原生调用失败会抛出异常；已移除对象拒绝修改。

## 获取方式

客户端发射器由 `client.spawnParticle(...)` 返回。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [id](#id) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [location](#location) | 只读属性 |
| [isBinding](#isBinding) | 只读属性 |
| [bindToEntity](#bindToEntity) | 方法 |
| [getMolang](#getMolang) | 方法 |
| [setMolang](#setMolang) | 方法 |
| [emit](#emit) | 方法 |
| [pause](#pause) | 方法 |
| [resume](#resume) | 方法 |
| [remove](#remove) | 方法 |

## 构造器 {#constructor}

```python
Particle(parId: int, owner: Any = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `parId` | [int](../../common/type-system.md#int) | `必填` | 传给 [Particle.__init__](Particle.md#constructor) 的 parId 参数；结合上方功能说明和下方调用示例使用。 |
| `owner` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 传给 [Particle.__init__](Particle.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## id {#id}

```python
id: int
```

原生发射器标识，移除后仍保留。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## isValid {#isValid}

```python
isValid: bool
```

所属会话是否有效且原生发射器是否仍存在。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `Exist`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## location {#location}

```python
location: Vector3
```

发射器当前位置，返回独立的 [Vector3](../../server/extra/vector.md) 副本。

**访问：** 只读。

**返回类型：** [Vector3](../../server/extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.location
```

## isBinding {#isBinding}

```python
isBinding: bool
```

此发射器是否已绑定到实体。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBindingID`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isBinding
```

## bindToEntity {#bindToEntity}

```python
bindToEntity(entity: ClientEntity | str, options: ClientParticleBindOptions | None = None) -> bool
```

绑定到实体，支持 bone、offset、rotation 选项，rotate 为旧别名。空骨骼名称选择原生根骨骼；不能同时提供两个旋转选项名。为兼容旧调用，成功时返回 True。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `entity` | [ClientEntity](ClientEntity.md) \| [str](../../common/type-system.md#str) | `必填` | 目标实体句柄；是否接受运行 ID 取决于签名。 |
| `options` | [ClientParticleBindOptions](ClientParticleBindOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Specify only rotation or rotate'` |
| [TypeError](../../common/type-system.md#typeerror) | `'bone must be a string without NUL'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `BindEntity`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_bindToEntity(instance, entity):
    return instance.bindToEntity(entity)
```

## getMolang {#getMolang}

```python
getMolang(molangExpression: str) -> float
```

读取具名发射器变量；未知名称由开发包返回零。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `molangExpression` | [str](../../common/type-system.md#str) | `必填` | 传给 [Particle.getMolang](Particle.md#getMolang) 的 molangExpression 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetVariable`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getMolang(instance, molangExpression):
    return instance.getMolang(molangExpression)
```

## setMolang {#setMolang}

```python
setMolang(molang: str, value: float) -> None
```

写入有限数值的发射器变量。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `molang` | [str](../../common/type-system.md#str) | `必填` | 传给 [Particle.setMolang](Particle.md#setMolang) 的 molang 参数；结合上方功能说明和下方调用示例使用。 |
| `value` | [float](../../common/type-system.md#float) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetVariable`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setMolang(instance, molang, value):
    return instance.setMolang(molang, value)
```

## emit {#emit}

```python
emit() -> None
```

让使用 minecraft:emitter_rate_manual 的发射器发射一次。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `EmitManually`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_emit(instance):
    return instance.emit()
```

## pause {#pause}

```python
pause() -> None
```

暂停逻辑更新，同时保留发射器渲染。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `Pause`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_pause(instance):
    return instance.pause()
```

## resume {#resume}

```python
resume() -> None
```

恢复被 pause() 暂停的逻辑更新。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `Resume`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_resume(instance):
    return instance.resume()
```

## remove {#remove}

```python
remove() -> None
```

移除此发射器；重复移除或自然到期后调用不会产生额外影响。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `Exist`, `Remove`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_remove(instance):
    return instance.remove()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 Particle 对象。
    print(value.id)
    print(value.isValid)
    print(value.location)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)