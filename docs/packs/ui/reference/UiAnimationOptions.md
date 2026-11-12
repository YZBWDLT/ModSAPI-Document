---
title: "UiAnimationOptions"
sidebar_label: "UiAnimationOptions"
---

# UiAnimationOptions

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/animations.py`；声明补充了静态类型信息。

:::info 字典结构或静态声明
此类型只出现在补全声明中，不是可从模板直接实例化的运行时类。作为选项时使用符合字段约定的 Python 字典。
:::

## 获取方式

使用普通选项字典传给 [UiControl.animate](UiControl.md#animate)；各字段是否需要提供取决于动画属性。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `from` | [float](../../common/type-system.md#float) \| [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] | `运行时返回` |
| `duration` | [float](../../common/type-system.md#float) | `运行时返回` |
| `onComplete` | [Callable](../../common/type-system.md#callable)[[[UiAnimationEvent](UiAnimationEvent.md)], [None](../../common/type-system.md#none)] | `运行时返回` |
| `onError` | [Callable](../../common/type-system.md#callable)[[[UiAnimationEvent](UiAnimationEvent.md)], [None](../../common/type-system.md#none)] | `运行时返回` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_options(options):
    print(options.get('from'))
    print(options.get('duration'))
    print(options.get('onComplete'))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)