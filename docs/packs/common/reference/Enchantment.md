---
title: "Enchantment"
sidebar_label: "Enchantment"
---

# Enchantment

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/Enchant.py`；声明补充了静态类型信息。

这是值对象或结果包装对象，成员通过属性访问；是否接受字典输入由所属操作的签名决定。包装类型不一定是模板入口的直接导出符号。

独立的带等级附魔值；组件方法复制传入和返回的对象。[type](../type-system.md#type) 是 [EnchantmentType](EnchantmentType.md) 引用，typeId 保留原生名称兼容入口。公开等级必须为正整数，注册上限由物品操作校验，不在读取旧原生数据时强制改写。

## 获取方式

从服务端入口创建附魔值，或从附魔组件的查询结果取得副本。[type](../type-system.md#type) 提供包装后的 [EnchantmentType](EnchantmentType.md)。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [type](#type) | 可读写属性 |
| [typeId](#typeId) | 可读写属性 |
| [level](#level) | 可读写属性 |

## 构造器 {#constructor}

```python
Enchantment(typeId: str | EnchantmentType, level: int) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `typeId` | [str](../type-system.md#str) \| [EnchantmentType](EnchantmentType.md) | `必填` | 带命名空间的实体、物品或资源类型名称。 |
| `level` | [int](../type-system.md#int) | `必填` | 传给 [Enchantment.__init__](Enchantment.md#constructor) 的 level 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## type {#type}

```python
type: EnchantmentType
```

包装后的附魔类型；修改仅影响当前独立值。

:::note 当前实现说明
返回 [EnchantmentType](EnchantmentType.md) 对象，使用 value.type.id 取得规范名称。类型引用的 maxLevel 可能按需查询当前服务端目录。
:::

**访问：** 可读写。

写入方式：`instance.type = value`。参数类型线索：`(value: str \| EnchantmentType) -> None`。

写入参数 `value`：[str](../type-system.md#str) \| [EnchantmentType](EnchantmentType.md)。

**返回类型：** [EnchantmentType](EnchantmentType.md)。静态声明不替代本页的实现限制。

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

原生名称兼容入口；原版名称不含 minecraft: 前缀。

**访问：** 可读写。

写入方式：`instance.typeId = value`。参数类型线索：`(value: str \| EnchantmentType) -> None`。

写入参数 `value`：[str](../type-system.md#str) \| [EnchantmentType](EnchantmentType.md)。

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

当前独立附魔值的等级；公开编辑要求正整数。

**访问：** 可读写。

写入方式：`instance.level = value`。参数类型线索：`(value: int) -> None`。

写入参数 `value`：[int](../type-system.md#int)。

**返回类型：** [int](../type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../type-system.md#typeerror) | `'An enchantment level must be an integer'` |
| [EnchantmentLevelOutOfBoundsError](EnchantmentLevelOutOfBoundsError.md) | `'An enchantment level must be positive'` |

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