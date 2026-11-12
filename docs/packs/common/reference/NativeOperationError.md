---
title: "NativeOperationError"
sidebar_label: "NativeOperationError"
---

# NativeOperationError

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/errors/extensions.py`；声明补充了静态类型信息。

原生操作失败。可读取 operation、code 和 cause 诊断原因。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[ExtensionError](ExtensionError.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `operation` | [str](../type-system.md#str) | `operation` |
| `code` | [Any](../type-system.md#any) | `code` |
| `cause` | [Exception](../type-system.md#exception) \| [None](../type-system.md#none) | `cause` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |

## 构造器 {#constructor}

```python
NativeOperationError(operation: str, code: Any = None, cause: Exception | None = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `operation` | [str](../type-system.md#str) | `必填` | 传给 [NativeOperationError.__init__](NativeOperationError.md#constructor) 的 operation 参数；结合上方功能说明和下方调用示例使用。 |
| `code` | [Any](../type-system.md#any) | [None](../type-system.md#none) | 传给 [NativeOperationError.__init__](NativeOperationError.md#constructor) 的 code 参数；结合上方功能说明和下方调用示例使用。 |
| `cause` | [Exception](../type-system.md#exception) \| [None](../type-system.md#none) | [None](../type-system.md#none) | 传给 [NativeOperationError.__init__](NativeOperationError.md#constructor) 的 cause 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 NativeOperationError 对象。
    print(value.operation)
    print(value.code)
    print(value.cause)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)