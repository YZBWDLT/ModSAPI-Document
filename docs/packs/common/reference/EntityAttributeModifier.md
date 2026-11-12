---
title: "EntityAttributeModifier"
sidebar_label: "EntityAttributeModifier"
---

# EntityAttributeModifier

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/AttributeModifier.py`；声明补充了静态类型信息。

这是值对象或结果包装对象，成员通过属性访问；是否接受字典输入由所属操作的签名决定。包装类型不一定是模板入口的直接导出符号。

只读且独立的属性修饰器快照，通过 [EntityAttributeComponent.getModifiers](../../server/reference/EntityAttributeComponent.md#getModifiers)() 或 getModifier() 取得。不保留实体或原生组件，也不会随引擎后续修改自动更新。修改接口直接接受标识符、数值和选项字典，无需主动构造快照。

## 获取方式

通过 [EntityAttributeComponent.getModifiers](../../server/reference/EntityAttributeComponent.md#getModifiers)() 或 getModifier() 取得只读快照。无需主动构造；快照不持有实体，也不会自动更新。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [id](#id) | 只读属性 |
| [amount](#amount) | 只读属性 |
| [operation](#operation) | 只读属性 |
| [operand](#operand) | 只读属性 |

## id {#id}

```python
id: str
```

引擎中的修饰器标识符；自定义标识符应包含模组命名空间。

**访问：** 只读。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## amount {#amount}

```python
amount: float
```

引擎返回的有限数值。

**访问：** 只读。

**返回类型：** [float](../type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.amount
```

## operation {#operation}

```python
operation: str
```

[AttributeModifierOperation](AttributeModifierOperation.md) 中的一个字符串常量。

**访问：** 只读。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.operation
```

## operand {#operand}

```python
operand: str
```

[AttributeModifierOperand](AttributeModifierOperand.md) 中的一个字符串常量。

**访问：** 只读。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.operand
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EntityAttributeModifier 对象。
    print(value.id)
    print(value.amount)
    print(value.operation)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)