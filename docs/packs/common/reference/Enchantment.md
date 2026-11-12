---
title: "Enchantment"
sidebar_label: "Enchantment"
---

# Enchantment

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/Enchant.py`；声明补充了静态类型信息。

这是值对象或结果包装对象，成员通过属性访问；是否接受字典输入由所属操作的签名决定。包装类型不一定是模板入口的直接导出符号。

应用于物品的附魔及其等级。

## 获取方式

通过物品的附魔组件读取附魔值；它包含类型标识符和等级。不要假定模板入口直接导出该构造器。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [type](#type) | 可读写属性 |
| [typeId](#typeId) | 可读写属性 |
| [level](#level) | 可读写属性 |

## 构造器 {#constructor}

```python
Enchantment(typeId: str, level: int) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `typeId` | [str](../type-system.md#str) | `必填` | 带命名空间的实体、物品或资源类型名称。 |
| `level` | [int](../type-system.md#int) | `必填` | 传给 [Enchantment.__init__](Enchantment.md#constructor) 的 level 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## type {#type}

```python
type: str
```

读取 [type](../type-system.md#type) 的当前值。

**访问：** 可读写。

写入方式：`instance.type = value`。参数类型线索：`(value: str) -> None`。

写入参数 `value`：[str](../type-system.md#str)。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.type

def write_value(instance, value):
    instance.type = value
```

## typeId {#typeId}

```python
typeId: str
```

读取 `typeId` 的当前值。

**访问：** 可读写。

写入方式：`instance.typeId = value`。参数类型线索：`(value: str) -> None`。

写入参数 `value`：[str](../type-system.md#str)。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId

def write_value(instance, value):
    instance.typeId = value
```

## level {#level}

```python
level: int
```

读取 `level` 的当前值。

**访问：** 可读写。

写入方式：`instance.level = value`。参数类型线索：`(value: int) -> None`。

写入参数 `value`：[int](../type-system.md#int)。

**返回类型：** [int](../type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.level

def write_value(instance, value):
    instance.level = value
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 Enchantment 对象。
    print(value.type)
    print(value.typeId)
    print(value.level)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)