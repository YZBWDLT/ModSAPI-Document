---
title: "LabelData"
sidebar_label: "LabelData"
---

import ApiFieldAnchor from '@docusaurus/Link';

# LabelData

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/ControlData.py`。

文本标签的数据定义。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[ControlData](ControlData.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-text" />`text` | 由运行时值确定 | `''` |  |
| <ApiFieldAnchor id="field-align" />`align` | 由运行时值确定 | `'center'` |  |
| <ApiFieldAnchor id="field-fontSize" />`fontSize` | 由运行时值确定 | `Expression(1.0)` |  |
| <ApiFieldAnchor id="field-linePadding" />`linePadding` | 由运行时值确定 | `Expression(0.0)` |  |
| <ApiFieldAnchor id="field-color" />`color` | 由运行时值确定 | `(Expression(255), Expression(255), Expression(255))` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [addControl](ControlData.md#addControl) | [ControlData](ControlData.md) |
| [alpha](ControlData.md#field-alpha) | [ControlData](ControlData.md) |
| [anchor](ControlData.md#field-anchor) | [ControlData](ControlData.md) |
| [background](ControlData.md#field-background) | [ControlData](ControlData.md) |
| [controlName](ControlData.md#field-controlName) | [ControlData](ControlData.md) |
| [controls](ControlData.md#field-controls) | [ControlData](ControlData.md) |
| [copy](ControlData.md#copy) | [ControlData](ControlData.md) |
| [inst](ControlData.md#field-inst) | [ControlData](ControlData.md) |
| [isStatic](ControlData.md#field-isStatic) | [ControlData](ControlData.md) |
| [offset](ControlData.md#field-offset) | [ControlData](ControlData.md) |
| [parent](ControlData.md#field-parent) | [ControlData](ControlData.md) |
| [path](ControlData.md#path) | [ControlData](ControlData.md) |
| [removeControl](ControlData.md#removeControl) | [ControlData](ControlData.md) |
| [shouldTrace](ControlData.md#field-shouldTrace) | [ControlData](ControlData.md) |
| [size](ControlData.md#field-size) | [ControlData](ControlData.md) |
| [visible](ControlData.md#field-visible) | [ControlData](ControlData.md) |

## 构造器 {#constructor}

```python
LabelData(parentData = None, inst = None)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `parentData` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [LabelData.__init__](LabelData.md#constructor) 的 parentData 参数；结合上方功能说明和下方调用示例使用。 |
| `inst` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [LabelData.__init__](LabelData.md#constructor) 的 inst 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 LabelData 对象。
    print(value.text)
    print(value.align)
    print(value.fontSize)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)