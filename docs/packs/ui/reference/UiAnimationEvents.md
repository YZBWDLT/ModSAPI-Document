---
title: "UiAnimationEvents"
sidebar_label: "UiAnimationEvents"
---

# UiAnimationEvents

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/animations.py`；声明补充了静态类型信息。

动画原生完成及适配失败信号，不通过轮询检测完成。

## 获取方式

使用 animation.afterEvents。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `complete` | [UiEventSignal](UiEventSignal.md)[[UiAnimationEvent](UiAnimationEvent.md)] | `UiEventSignal(animation)` |  |
| `error` | [UiEventSignal](UiEventSignal.md)[[UiAnimationEvent](UiAnimationEvent.md)] | `UiEventSignal(animation)` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UiAnimationEvents 对象。
    print(value.complete)
    print(value.error)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)