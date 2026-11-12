---
title: "UiImageClipDirection"
sidebar_label: "UiImageClipDirection"
---

# UiImageClipDirection

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/constants.py`；声明补充了静态类型信息。

[UiImage.clipDirection](UiImage.md#clipDirection) 接受的裁剪方向常量。

## 获取方式

从 ModSAPI.ui 导入，赋给 [UiImage.clipDirection](UiImage.md#clipDirection)。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `LeftToRight` | [str](../../common/type-system.md#str) | `'fromLeftToRight'` |  |
| `RightToLeft` | [str](../../common/type-system.md#str) | `'fromRightToLeft'` |  |
| `OutsideToInside` | [str](../../common/type-system.md#str) | `'fromOutsideToInside'` |  |
| `TopToBottom` | [str](../../common/type-system.md#str) | `'fromTopToBottom'` |  |
| `BottomToTop` | [str](../../common/type-system.md#str) | `'fromBottomToTop'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
from ModSAPI.ui import UiImageClipDirection

def configure(image):
    image.clipDirection = UiImageClipDirection.LeftToRight
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)