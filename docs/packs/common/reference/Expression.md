---
title: "Expression"
sidebar_label: "Expression"
---

# Expression

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/expression.py`。

表达式

## 获取方式

底层数值表达式对象，可从相关算术或界面变量操作取得。它不是文本表达式 [ExpressionString](../../client/reference/ExpressionString.md)，也不是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [staticValue](#staticValue) | 只读属性 |

## 构造器 {#constructor}

```python
Expression(value: float | Expression = 0, op: int = None, next: Expression = 0) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `value` | [float](../type-system.md#float) \| [Expression](Expression.md) | `0` | 需要写入的值，类型、范围及副本语义见本成员说明。 |
| `op` | [int](../type-system.md#int) | [None](../type-system.md#none) | 传给 [Expression.__init__](Expression.md#constructor) 的 op 参数；结合上方功能说明和下方调用示例使用。 |
| `next` | [Expression](Expression.md) | `0` | 传给 [Expression.__init__](Expression.md#constructor) 的 next 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## staticValue {#staticValue}

```python
staticValue: float
```

获取静态值

**访问：** 只读。

**返回类型：** [float](../type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.staticValue
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 Expression 对象。
    print(value.staticValue)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)