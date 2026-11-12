---
title: "ScrollPanel"
sidebar_label: "ScrollPanel"
---

# ScrollPanel

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/UI.py`。

滚动面板（竖向）

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[Control](Control.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `name` | 由运行时值确定 | `name if name else 'scrollpanel%s' % random.randint(0, 2147483648)` |
| `offset` | 由运行时值确定 | `offset` |
| `size` | 由运行时值确定 | `size` |
| `alpha` | 由运行时值确定 | `alpha` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [content](#content) | 只读属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [addButton](Control.md#addButton) | [Control](Control.md) |
| [addControl](Control.md#addControl) | [Control](Control.md) |
| [addImage](Control.md#addImage) | [Control](Control.md) |
| [addLabel](Control.md#addLabel) | [Control](Control.md) |
| [addPanel](Control.md#addPanel) | [Control](Control.md) |
| [addScrollPanel](Control.md#addScrollPanel) | [Control](Control.md) |
| [anchor](Control.md#anchor) | [Control](Control.md) |
| [asStaticControl](Control.md#asStaticControl) | [Control](Control.md) |
| [background](Control.md#background) | [Control](Control.md) |
| [copy](Control.md#copy) | [Control](Control.md) |
| [parent](Control.md#parent) | [Control](Control.md) |
| [trace](Control.md#trace) | [Control](Control.md) |

## 构造器 {#constructor}

```python
ScrollPanel(parent: Control | UI = None, name: str = None, offset: tuple[Expression. Expression] = [0, 0], size: tuple[Expression, Expression] = [100, 100], alpha: Expression = 1, background_color: tuple[Expression, Expression, Expression] = (255, 255, 255), background_alpha: Expression = 1, background_texture: str = 'textures/ui/ScrollRail') -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `parent` | [Control](Control.md) \| [UI](UI.md) | [None](../../common/type-system.md#none) | 传给 [ScrollPanel.__init__](ScrollPanel.md#constructor) 的 parent 参数；结合上方功能说明和下方调用示例使用。 |
| `name` | [str](../../common/type-system.md#str) | [None](../../common/type-system.md#none) | 传给 [ScrollPanel.__init__](ScrollPanel.md#constructor) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `offset` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md). [Expression](../../common/reference/Expression.md)] | `[0, 0]` | 传给 [ScrollPanel.__init__](ScrollPanel.md#constructor) 的 offset 参数；结合上方功能说明和下方调用示例使用。 |
| `size` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md)] | `[100, 100]` | 传给 [ScrollPanel.__init__](ScrollPanel.md#constructor) 的 size 参数；结合上方功能说明和下方调用示例使用。 |
| `alpha` | [Expression](../../common/reference/Expression.md) | `1` | 传给 [ScrollPanel.__init__](ScrollPanel.md#constructor) 的 alpha 参数；结合上方功能说明和下方调用示例使用。 |
| `background_color` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md)] | `(255, 255, 255)` | 传给 [ScrollPanel.__init__](ScrollPanel.md#constructor) 的 background_color 参数；结合上方功能说明和下方调用示例使用。 |
| `background_alpha` | [Expression](../../common/reference/Expression.md) | `1` | 传给 [ScrollPanel.__init__](ScrollPanel.md#constructor) 的 background_alpha 参数；结合上方功能说明和下方调用示例使用。 |
| `background_texture` | [str](../../common/type-system.md#str) | `'textures/ui/ScrollRail'` | 传给 [ScrollPanel.__init__](ScrollPanel.md#constructor) 的 background_texture 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## content {#content}

```python
content
```

滚动面板的内容

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.content
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ScrollPanel 对象。
    print(value.content)
    print(value.name)
    print(value.offset)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)