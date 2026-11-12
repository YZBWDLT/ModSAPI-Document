---
title: "Variables"
sidebar_label: "Variables"
---

# Variables

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/UI.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [ui_age](#ui_age) | 静态/类方法 |

## 构造器 {#constructor}

```python
Variables()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## ui_age {#ui_age}

```python
ui_age(ui: UI) -> Expression
```

界面自创建以来的刻数，每秒 30 刻。尚未显示时返回 -1。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `ui` | [UI](UI.md) | `必填` | 传给 [Variables.ui_age](Variables.md#ui_age) 的 ui 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Expression](../../common/reference/Expression.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_ui_age(type_object, ui):
    return type_object.ui_age(ui)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 Variables 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)