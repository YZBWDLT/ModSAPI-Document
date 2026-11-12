---
title: "ScreenData"
sidebar_label: "ScreenData"
---

# ScreenData

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/ControlData.py`。

屏幕的数据定义。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `controls` | 由运行时值确定 | `[]` |
| `size` | 由运行时值确定 | `[Expression(size[0]), Expression(size[1])]` |
| `alpha` | 由运行时值确定 | `Expression(1.0)` |
| `background` | 由运行时值确定 | `BackgroundData()` |
| `updateCallback` | 由运行时值确定 | [None](../../common/type-system.md#none) |
| `controlName` | 由运行时值确定 | `'screen'` |
| `inst` | 由运行时值确定 | `inst` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [addControl](#addControl) | 方法 |
| [removeControl](#removeControl) | 方法 |

## 构造器 {#constructor}

```python
ScreenData(inst = None)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `inst` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [ScreenData.__init__](ScreenData.md#constructor) 的 inst 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetScreenSize`, `GetLevelId`, `GetEngineCompFactory`。

## addControl {#addControl}

```python
addControl(controlData: ControlData) -> None
```

向当前控件添加子控件。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `controlData` | [ControlData](ControlData.md) | `必填` | 传给 [ScreenData.addControl](ScreenData.md#addControl) 的 controlData 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addControl(instance, controlData):
    return instance.addControl(controlData)
```

## removeControl {#removeControl}

```python
removeControl(controlData: ControlData) -> bool
```

移除控件；目标控件存在时返回 True。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `controlData` | [ControlData](ControlData.md) | `必填` | 传给 [ScreenData.removeControl](ScreenData.md#removeControl) 的 controlData 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeControl(instance, controlData):
    return instance.removeControl(controlData)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ScreenData 对象。
    print(value.controls)
    print(value.size)
    print(value.alpha)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)