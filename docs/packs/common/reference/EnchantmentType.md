---
title: "EnchantmentType"
sidebar_label: "EnchantmentType"
---

# EnchantmentType

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/Enchant.py`；声明补充了静态类型信息。

这是值对象或结果包装对象，成员通过属性访问；是否接受字典输入由所属操作的签名决定。包装类型不一定是模板入口的直接导出符号。

已注册附魔类型，提供规范标识和等级上限。构造时查询当前服务端目录；原生物品使用按需解析的类型引用，避免仅为读取或克隆就额外查询目录，也保留已有未知附魔数据。

## 获取方式

从 [EnchantmentTypes](../../server/reference/EnchantmentTypes.md) 查询，或使用注册标识创建。id 与 maxLevel 只读；原生旧物品的类型引用按需解析。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [id](#id) | 只读属性 |
| [maxLevel](#maxLevel) | 只读属性 |

## 构造器 {#constructor}

```python
EnchantmentType(enchantmentType: str) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchantmentType` | [str](../type-system.md#str) | `必填` | 传给 [EnchantmentType.__init__](EnchantmentType.md#constructor) 的 enchantmentType 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## id {#id}

```python
id: str
```

规范的命名空间标识；原版名称使用 minecraft: 前缀。

**访问：** 只读。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## maxLevel {#maxLevel}

```python
maxLevel: int
```

注册的等级上限；物品中的按需类型引用首次访问时解析。

**访问：** 只读。

**返回类型：** [int](../type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.maxLevel
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EnchantmentType 对象。
    print(value.id)
    print(value.maxLevel)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)