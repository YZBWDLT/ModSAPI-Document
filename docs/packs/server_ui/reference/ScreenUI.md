---
title: "ScreenUI"
sidebar_label: "ScreenUI"
---

# ScreenUI

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/UI.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[UI](UI.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [age](#age) | 只读属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [addButton](UI.md#addButton) | [UI](UI.md) |
| [addControl](UI.md#addControl) | [UI](UI.md) |
| [addImage](UI.md#addImage) | [UI](UI.md) |
| [addLabel](UI.md#addLabel) | [UI](UI.md) |
| [addPanel](UI.md#addPanel) | [UI](UI.md) |
| [addScrollPanel](UI.md#addScrollPanel) | [UI](UI.md) |
| [background](UI.md#background) | [UI](UI.md) |
| [onUpdate](UI.md#onUpdate) | [UI](UI.md) |
| [remove](UI.md#remove) | [UI](UI.md) |
| [show](UI.md#show) | [UI](UI.md) |
| [size](UI.md#size) | [UI](UI.md) |

## 构造器 {#constructor}

```python
ScreenUI()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## age {#age}

```python
age: Expression
```

UI寿命(从弹出界面开始),单位: tick(1秒30tick)

未弹出界面时返回-1

支持表达式

**访问：** 只读。

**返回类型：** [Expression](../../common/reference/Expression.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.age
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ScreenUI 对象。
    print(value.age)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)