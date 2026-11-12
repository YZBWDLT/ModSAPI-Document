---
title: "ProjectileHitEntityAfterEvent"
sidebar_label: "ProjectileHitEntityAfterEvent"
---

# ProjectileHitEntityAfterEvent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/events/core/ProjectileEvents.py`；声明补充了静态类型信息。

投射物命中实体的事件信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [dimension](#dimension) | 只读属性 |
| [hitVector](#hitVector) | 只读属性 |
| [location](#location) | 只读属性 |
| [projectile](#projectile) | 只读属性 |
| [source](#source) | 只读属性 |
| [getEntityHit](#getEntityHit) | 方法 |

## 构造器 {#constructor}

```python
ProjectileHitEntityAfterEvent(data)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetDirFromRot`, `GetEntityDimensionId`, `GetRot`。

## dimension {#dimension}

```python
dimension: Dimension
```

投射物命中发生的维度。

**访问：** 只读。

**返回类型：** [Dimension](../apis/dimension.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.dimension
```

## hitVector {#hitVector}

```python
hitVector: Vector3
```

投射物命中方块时的方向向量。

**访问：** 只读。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.hitVector
```

## location {#location}

```python
location: Vector3
```

投射物命中的位置。

**访问：** 只读。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.location
```

## projectile {#projectile}

```python
projectile: Entity
```

命中方块的投射物实体。

**访问：** 只读。

**返回类型：** [Entity](../apis/entity.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.projectile
```

## source {#source}

```python
source: Entity | None
```

发射投射物的来源实体；可能不存在。

**访问：** 只读。

**返回类型：** [Entity](../apis/entity.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.source
```

## getEntityHit {#getEntityHit}

```python
getEntityHit() -> EntityHitInformation
```

被命中实体的附加信息。

**返回类型：** [EntityHitInformation](../../common/reference/EntityHitInformation.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEntityHit(instance):
    return instance.getEntityHit()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ProjectileHitEntityAfterEvent 对象。
    print(value.dimension)
    print(value.hitVector)
    print(value.location)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)