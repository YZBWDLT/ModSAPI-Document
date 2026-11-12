---
title: "ExpressionString"
sidebar_label: "ExpressionString"
---

import ApiFieldAnchor from '@docusaurus/Link';

# ExpressionString

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/ExpressionString.py`；声明补充了静态类型信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-expression" />`expression` | [str](../../common/type-system.md#str) | `expression` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [eval](#eval) | 方法 |

## 构造器 {#constructor}

```python
ExpressionString(expression: str)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `expression` | [str](../../common/type-system.md#str) | `必填` | 传给 [ExpressionString.__init__](ExpressionString.md#constructor) 的 expression 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## eval {#eval}

```python
eval(variable: Variable, localVars = {})
```

执行 `eval` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `variable` | [Variable](Variable.md) | `必填` | 传给 [ExpressionString.eval](ExpressionString.md#eval) 的 variable 参数；结合上方功能说明和下方调用示例使用。 |
| `localVars` | 由值/所属选项确定 | `{}` | 传给 [ExpressionString.eval](ExpressionString.md#eval) 的 localVars 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [SafeEvalError](SafeEvalError.md) | `'Unexpected char: %r' % c` |
| [SafeEvalError](SafeEvalError.md) | `'Unexpected token: %r' % (t,)` |
| [SafeEvalError](SafeEvalError.md) | `'Expected %s, got %s' % (typ, t[0])` |
| [SafeEvalError](SafeEvalError.md) | `'Expected %r, got %r' % (val, t[1])` |
| [SafeEvalError](SafeEvalError.md) | `'Name not allowed: %s' % name` |
| [SafeEvalError](SafeEvalError.md) | `'Dunder attribute not allowed: %s' % name` |
| [SafeEvalError](SafeEvalError.md) | `'Only math.xxx(...) or random.xxx(...) calls are allowed'` |
| [SafeEvalError](SafeEvalError.md) | `'Invalid number (two dots)'` |
| [SafeEvalError](SafeEvalError.md) | `'No such attribute: %s' % name` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_eval(instance, variable):
    return instance.eval(variable)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ExpressionString 对象。
    print(value.expression)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)