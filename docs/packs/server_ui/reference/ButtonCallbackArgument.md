---
title: "ButtonCallbackArgument"
sidebar_label: "ButtonCallbackArgument"
---

import ApiFieldAnchor from '@docusaurus/Link';

# ButtonCallbackArgument

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/UI.py`。

按钮回调函数参数

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-button" />`button` | 由运行时值确定 | `button` |  |
| <ApiFieldAnchor id="field-ui" />`ui` | 由运行时值确定 | `ui` |  |
| <ApiFieldAnchor id="field-pos" />`pos` | 由运行时值确定 | `Vector2(pos)` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |

## 构造器 {#constructor}

```python
ButtonCallbackArgument(button: Button, ui: UI, pos: tuple = (0, 0)) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `button` | [Button](Button.md) | `必填` | 传给 [ButtonCallbackArgument.__init__](ButtonCallbackArgument.md#constructor) 的 button 参数；结合上方功能说明和下方调用示例使用。 |
| `ui` | [UI](UI.md) | `必填` | 传给 [ButtonCallbackArgument.__init__](ButtonCallbackArgument.md#constructor) 的 ui 参数；结合上方功能说明和下方调用示例使用。 |
| `pos` | [tuple](../../common/type-system.md#tuple) | `(0, 0)` | 传给 [ButtonCallbackArgument.__init__](ButtonCallbackArgument.md#constructor) 的 pos 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ButtonCallbackArgument 对象。
    print(value.button)
    print(value.ui)
    print(value.pos)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)