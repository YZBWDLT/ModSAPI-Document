---
title: "UiViewEvents"
sidebar_label: "UiViewEvents"
---

# UiViewEvents

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/events.py`；声明补充了静态类型信息。

单个视图的就绪、更新和关闭生命周期信号。

## 获取方式

使用 view.afterEvents。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `ready` | [UiEventSignal](UiEventSignal.md)[[UiEvent](UiEvent.md)] | `UiEventSignal(view)` |  |
| `update` | [UiEventSignal](UiEventSignal.md)[[UiEvent](UiEvent.md)] | `UiEventSignal(view)` |  |
| `close` | [UiEventSignal](UiEventSignal.md)[[UiEvent](UiEvent.md)] | `UiEventSignal(view)` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UiViewEvents 对象。
    print(value.ready)
    print(value.update)
    print(value.close)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)