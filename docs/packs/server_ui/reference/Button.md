---
title: "Button"
sidebar_label: "Button"
---

# Button

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/UI.py`。

按钮控件。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[Control](Control.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `name` | 由运行时值确定 | `name if name else 'control%s' % random.randint(0, 2147483648)` |  |
| `offset` | 由运行时值确定 | `offset` |  |
| `size` | 由运行时值确定 | `size` |  |
| `alpha` | 由运行时值确定 | `alpha` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [callbacks](#callbacks) | 只读属性 |
| [textures](#textures) | 只读属性 |
| [label](#label) | 只读属性 |

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
Button(parent = None, name = None, offset = [0, 0], size = [100, 100], alpha = 1.0, background_color = (255, 255, 255), background_alpha = 0.0, background_texture = 'textures/ui/white_bg', callback_touch_up = None, callback_touch_down = None, callback_touch_cancel = None, callback_touch_move = None, callback_touch_move_in = None, callback_touch_move_out = None, callback_hover_in = None, callback_hover_out = None, callback_screen_exit = None, texture_default = 'textures/netease/common/button/default', texture_hover = 'textures/netease/common/button/hover', texture_pressed = 'textures/netease/common/button/pressed')
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `parent` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [Button.__init__](Button.md#constructor) 的 parent 参数；结合上方功能说明和下方调用示例使用。 |
| `name` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [Button.__init__](Button.md#constructor) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `offset` | 由值/所属选项确定 | `[0, 0]` | 传给 [Button.__init__](Button.md#constructor) 的 offset 参数；结合上方功能说明和下方调用示例使用。 |
| `size` | 由值/所属选项确定 | `[100, 100]` | 传给 [Button.__init__](Button.md#constructor) 的 size 参数；结合上方功能说明和下方调用示例使用。 |
| `alpha` | 由值/所属选项确定 | `1.0` | 传给 [Button.__init__](Button.md#constructor) 的 alpha 参数；结合上方功能说明和下方调用示例使用。 |
| `background_color` | 由值/所属选项确定 | `(255, 255, 255)` | 传给 [Button.__init__](Button.md#constructor) 的 background_color 参数；结合上方功能说明和下方调用示例使用。 |
| `background_alpha` | 由值/所属选项确定 | `0.0` | 传给 [Button.__init__](Button.md#constructor) 的 background_alpha 参数；结合上方功能说明和下方调用示例使用。 |
| `background_texture` | 由值/所属选项确定 | `'textures/ui/white_bg'` | 传给 [Button.__init__](Button.md#constructor) 的 background_texture 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_touch_up` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [Button.__init__](Button.md#constructor) 的 callback_touch_up 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_touch_down` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [Button.__init__](Button.md#constructor) 的 callback_touch_down 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_touch_cancel` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [Button.__init__](Button.md#constructor) 的 callback_touch_cancel 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_touch_move` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [Button.__init__](Button.md#constructor) 的 callback_touch_move 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_touch_move_in` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [Button.__init__](Button.md#constructor) 的 callback_touch_move_in 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_touch_move_out` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [Button.__init__](Button.md#constructor) 的 callback_touch_move_out 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_hover_in` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [Button.__init__](Button.md#constructor) 的 callback_hover_in 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_hover_out` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [Button.__init__](Button.md#constructor) 的 callback_hover_out 参数；结合上方功能说明和下方调用示例使用。 |
| `callback_screen_exit` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [Button.__init__](Button.md#constructor) 的 callback_screen_exit 参数；结合上方功能说明和下方调用示例使用。 |
| `texture_default` | 由值/所属选项确定 | `'textures/netease/common/button/default'` | 传给 [Button.__init__](Button.md#constructor) 的 texture_default 参数；结合上方功能说明和下方调用示例使用。 |
| `texture_hover` | 由值/所属选项确定 | `'textures/netease/common/button/hover'` | 传给 [Button.__init__](Button.md#constructor) 的 texture_hover 参数；结合上方功能说明和下方调用示例使用。 |
| `texture_pressed` | 由值/所属选项确定 | `'textures/netease/common/button/pressed'` | 传给 [Button.__init__](Button.md#constructor) 的 texture_pressed 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## callbacks {#callbacks}

```python
callbacks
```

按钮回调函数

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.callbacks
```

## textures {#textures}

```python
textures
```

贴图集

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.textures
```

## label {#label}

```python
label
```

文本

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.label
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 Button 对象。
    print(value.callbacks)
    print(value.textures)
    print(value.label)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)