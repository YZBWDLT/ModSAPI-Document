---
title: "EntityDamageSource"
sidebar_label: "EntityDamageSource"
---

# EntityDamageSource

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/Sources.py`；声明补充了静态类型信息。

选项通常可直接传 Python 字典；包装类名本身不保证通过模板导出。只使用所属操作已经实现的字段。

实体受到伤害的来源信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [cause](#cause) | 可读写属性 |
| [damagingEntity](#damagingEntity) | 可读写属性 |
| [damagingProjectile](#damagingProjectile) | 可读写属性 |
| [customTag](#customTag) | 可读写属性 |

## 构造器 {#constructor}

```python
EntityDamageSource(data: dict) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | [dict](../type-system.md#dict) | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## cause {#cause}

```python
cause: str
```

伤害原因枚举值。

**访问：** 可读写。

写入方式：`instance.cause = value`。参数类型线索：`(data)`。

写入参数 `data`：由值/所属选项确定。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.cause

def write_value(instance, value):
    instance.cause = value
```

## damagingEntity {#damagingEntity}

```python
damagingEntity: Entity
```

造成伤害的实体；可能不存在。

**访问：** 可读写。

写入方式：`instance.damagingEntity = value`。参数类型线索：`(data)`。

写入参数 `data`：由值/所属选项确定。

**返回类型：** [Entity](../../server/apis/entity.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.damagingEntity

def write_value(instance, value):
    instance.damagingEntity = value
```

## damagingProjectile {#damagingProjectile}

```python
damagingProjectile: Entity
```

造成伤害的投射物实体；可能不存在。

**访问：** 可读写。

写入方式：`instance.damagingProjectile = value`。参数类型线索：`(data)`。

写入参数 `data`：由值/所属选项确定。

**返回类型：** [Entity](../../server/apis/entity.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.damagingProjectile

def write_value(instance, value):
    instance.damagingProjectile = value
```

## customTag {#customTag}

```python
customTag: str
```

自定义伤害标签。

**访问：** 可读写。

写入方式：`instance.customTag = value`。参数类型线索：`(data: str) -> None`。

写入参数 `data`：[str](../type-system.md#str)。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.customTag

def write_value(instance, value):
    instance.customTag = value
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EntityDamageSource 对象。
    print(value.cause)
    print(value.damagingEntity)
    print(value.damagingProjectile)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)