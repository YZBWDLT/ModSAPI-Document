---
title: "ScrollingPanel"
sidebar_label: "ScrollingPanel"
---

# ScrollingPanel

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/interfaces/base/controls.py`；声明补充了静态类型信息。

这是界面模板描述或登记入口，通过 ModSAPI.ui 获取。控件登记需要相应描述对象，不能用普通字典替代。

表单面板模板描述，包含滚动区域、标题和关闭按钮路径。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[ControlDescriptor](ControlDescriptor.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `scrollingPanelPath` | [str](../../common/type-system.md#str) | `scrollingPanelPath` |
| `titlePath` | [str](../../common/type-system.md#str) | `titlePath` |
| `closeButtonPath` | [str](../../common/type-system.md#str) | `closeButtonPath` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [onCreate](ControlDescriptor.md#字段与常量) | [ControlDescriptor](ControlDescriptor.md) |

## 构造器 {#constructor}

```python
ScrollingPanel(onCreate: CreateCallback | None = None, scrollingPanelPath: str = '', titlePath: str = '', closeButtonPath: str = '') -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `onCreate` | [CreateCallback](../../common/type-aliases.md#createcallback) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [ScrollingPanel.__init__](ScrollingPanel.md#constructor) 的 onCreate 参数；结合上方功能说明和下方调用示例使用。 |
| `scrollingPanelPath` | [str](../../common/type-system.md#str) | `''` | 传给 [ScrollingPanel.__init__](ScrollingPanel.md#constructor) 的 scrollingPanelPath 参数；结合上方功能说明和下方调用示例使用。 |
| `titlePath` | [str](../../common/type-system.md#str) | `''` | 传给 [ScrollingPanel.__init__](ScrollingPanel.md#constructor) 的 titlePath 参数；结合上方功能说明和下方调用示例使用。 |
| `closeButtonPath` | [str](../../common/type-system.md#str) | `''` | 传给 [ScrollingPanel.__init__](ScrollingPanel.md#constructor) 的 closeButtonPath 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ScrollingPanel 对象。
    print(value.scrollingPanelPath)
    print(value.titlePath)
    print(value.closeButtonPath)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)