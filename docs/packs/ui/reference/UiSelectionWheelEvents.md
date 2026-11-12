---
title: "UiSelectionWheelEvents"
sidebar_label: "UiSelectionWheelEvents"
---

import ApiFieldAnchor from '@docusaurus/Link';

# UiSelectionWheelEvents

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/choices.py`；声明补充了静态类型信息。

悬浮选项变化与指针完成选择的事件容器。

## 获取方式

使用 [UiSelectionWheel.afterEvents](UiSelectionWheel.md#afterEvents)。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-selectionChange" />`selectionChange` | [UiEventSignal](UiEventSignal.md)[[UiChoiceEvent](UiChoiceEvent.md)] | `运行时返回` |  |
| <ApiFieldAnchor id="field-select" />`select` | [UiEventSignal](UiEventSignal.md)[[UiChoiceEvent](UiChoiceEvent.md)] | `运行时返回` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UiSelectionWheelEvents 对象。
    print(value.selectionChange)
    print(value.select)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)