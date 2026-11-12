---
title: "DragableButton"
sidebar_label: "DragableButton"
---

# DragableButton

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/UI.py`。

可拖动按钮控件。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[Button](Button.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |

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
| [alpha](Button.md#字段与常量) | [Button](Button.md) |
| [anchor](Control.md#anchor) | [Control](Control.md) |
| [asStaticControl](Control.md#asStaticControl) | [Control](Control.md) |
| [background](Control.md#background) | [Control](Control.md) |
| [callbacks](Button.md#callbacks) | [Button](Button.md) |
| [copy](Control.md#copy) | [Control](Control.md) |
| [label](Button.md#label) | [Button](Button.md) |
| [name](Button.md#字段与常量) | [Button](Button.md) |
| [offset](Button.md#字段与常量) | [Button](Button.md) |
| [parent](Control.md#parent) | [Control](Control.md) |
| [size](Button.md#字段与常量) | [Button](Button.md) |
| [textures](Button.md#textures) | [Button](Button.md) |
| [trace](Control.md#trace) | [Control](Control.md) |

## 构造器 {#constructor}

```python
DragableButton(parent: Control | UI = None, name: str = None, offset: tuple[Expression. Expression] = [0, 0], size: tuple[Expression, Expression] = [100, 100], alpha: Expression = 1.0, background_color: tuple[Expression, Expression, Expression] = (255, 255, 255), background_alpha: Expression = 0.0, background_texture: str = 'textures/ui/white_bg', callback_touch_up: types.FunctionType = None, callback_touch_down: types.FunctionType = None, callback_touch_cancel: types.FunctionType = None, callback_touch_move: types.FunctionType = None, callback_touch_move_in: types.FunctionType = None, callback_touch_move_out: types.FunctionType = None, callback_hover_in: types.FunctionType = None, callback_hover_out: types.FunctionType = None, callback_screen_exit: types.FunctionType = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `parent` | [Control](Control.md) \| [UI](UI.md) | [None](../../common/type-system.md#none) | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 parent 参数；结合上方功能说明和下方调用示例使用。 |
| `name` | [str](../../common/type-system.md#str) | [None](../../common/type-system.md#none) | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `offset` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md). [Expression](../../common/reference/Expression.md)] | `[0, 0]` | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 offset 参数；结合上方功能说明和下方调用示例使用。 |
| `size` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md)] | `[100, 100]` | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 size 参数；结合上方功能说明和下方调用示例使用。 |
| `alpha` | [Expression](../../common/reference/Expression.md) | `1.0` | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 alpha 参数；结合上方功能说明和下方调用示例使用。 |
| `background_color` | [tuple](../../common/type-system.md#tuple)[[Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md), [Expression](../../common/reference/Expression.md)] | `(255, 255, 255)` | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 background_color 参数；结合上方功能说明和下方调用示例使用。 |
| `background_alpha` | [Expression](../../common/reference/Expression.md) | `0.0` | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 background_alpha 参数；结合上方功能说明和下方调用示例使用。 |
| `background_texture` | [str](../../common/type-system.md#str) | `'textures/ui/white_bg'` | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 background_texture 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_touch_up` | [types.FunctionType](../../common/type-system.md#functiontype) | [None](../../common/type-system.md#none) | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 callback_touch_up 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_touch_down` | [types.FunctionType](../../common/type-system.md#functiontype) | [None](../../common/type-system.md#none) | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 callback_touch_down 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_touch_cancel` | [types.FunctionType](../../common/type-system.md#functiontype) | [None](../../common/type-system.md#none) | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 callback_touch_cancel 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_touch_move` | [types.FunctionType](../../common/type-system.md#functiontype) | [None](../../common/type-system.md#none) | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 callback_touch_move 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_touch_move_in` | [types.FunctionType](../../common/type-system.md#functiontype) | [None](../../common/type-system.md#none) | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 callback_touch_move_in 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_touch_move_out` | [types.FunctionType](../../common/type-system.md#functiontype) | [None](../../common/type-system.md#none) | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 callback_touch_move_out 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_hover_in` | [types.FunctionType](../../common/type-system.md#functiontype) | [None](../../common/type-system.md#none) | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 callback_hover_in 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_hover_out` | [types.FunctionType](../../common/type-system.md#functiontype) | [None](../../common/type-system.md#none) | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 callback_hover_out 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_screen_exit` | [types.FunctionType](../../common/type-system.md#functiontype) | [None](../../common/type-system.md#none) | 传给 [DragableButton.__init__](DragableButton.md#constructor) 的 callback_screen_exit 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 DragableButton 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)