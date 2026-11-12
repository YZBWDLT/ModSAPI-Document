---
title: "ControlDescriptor"
sidebar_label: "ControlDescriptor"
---

# ControlDescriptor

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/interfaces/base/controls.py`；声明补充了静态类型信息。

这是界面模板描述或登记入口，通过 ModSAPI.ui 获取。控件登记需要相应描述对象，不能用普通字典替代。

控件模板描述基类；创建回调在客户端执行。

## 获取方式

从 ModSAPI.ui 导入具体描述类型，传给 [Control.register](Control.md#register)。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `onCreate` | [CreateCallback](../../common/type-aliases.md#createcallback) \| [None](../../common/type-system.md#none) | `onCreate` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |

## 构造器 {#constructor}

```python
ControlDescriptor(onCreate: CreateCallback | None = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `onCreate` | [CreateCallback](../../common/type-aliases.md#createcallback) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [ControlDescriptor.__init__](ControlDescriptor.md#constructor) 的 onCreate 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'onCreate must be callable or None'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ControlDescriptor 对象。
    print(value.onCreate)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)