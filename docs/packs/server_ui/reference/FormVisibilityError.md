---
title: "FormVisibilityError"
sidebar_label: "FormVisibilityError"
---

# FormVisibilityError

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/definitions.py`；声明补充了静态类型信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[InvalidFormError](InvalidFormError.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `reason` | [str](../../common/type-system.md#str) | `reason` |  |
| `args` | 由运行时值确定 | `(reason,)` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [formId](InvalidFormError.md#字段与常量) | [InvalidFormError](InvalidFormError.md) |

## 构造器 {#constructor}

```python
FormVisibilityError(formId: int | str, reason: str) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `formId` | [int](../../common/type-system.md#int) \| [str](../../common/type-system.md#str) | `必填` | 传给 [FormVisibilityError.__init__](FormVisibilityError.md#constructor) 的 formId 参数；结合上方功能说明和下方调用示例使用。 |
| `reason` | [str](../../common/type-system.md#str) | `必填` | 传给 [FormVisibilityError.__init__](FormVisibilityError.md#constructor) 的 reason 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 FormVisibilityError 对象。
    print(value.reason)
    print(value.args)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)