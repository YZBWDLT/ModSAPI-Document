---
title: "UiButtonEvents"
sidebar_label: "UiButtonEvents"
---

# UiButtonEvents

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/controls.py`；声明补充了静态类型信息。

按需启用的原生按钮订阅，事件参数使用包装对象。

## 获取方式

使用 button.afterEvents。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `click` | [UiEventSignal](UiEventSignal.md)[[UiEvent](UiEvent.md)] | `运行时返回` |  |
| `pointerDown` | [UiEventSignal](UiEventSignal.md)[[UiEvent](UiEvent.md)] | `运行时返回` |  |
| `pointerMove` | [UiEventSignal](UiEventSignal.md)[[UiEvent](UiEvent.md)] | `运行时返回` |  |
| `pointerCancel` | [UiEventSignal](UiEventSignal.md)[[UiEvent](UiEvent.md)] | `运行时返回` |  |
| `pointerEnter` | [UiEventSignal](UiEventSignal.md)[[UiEvent](UiEvent.md)] | `运行时返回` |  |
| `pointerLeave` | [UiEventSignal](UiEventSignal.md)[[UiEvent](UiEvent.md)] | `运行时返回` |  |
| `hoverEnter` | [UiEventSignal](UiEventSignal.md)[[UiEvent](UiEvent.md)] | `运行时返回` |  |
| `hoverLeave` | [UiEventSignal](UiEventSignal.md)[[UiEvent](UiEvent.md)] | `运行时返回` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UiButtonEvents 对象。
    print(value.click)
    print(value.pointerDown)
    print(value.pointerMove)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)