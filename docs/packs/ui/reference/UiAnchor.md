---
title: "UiAnchor"
sidebar_label: "UiAnchor"
---

import ApiFieldAnchor from '@docusaurus/Link';

# UiAnchor

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/constants.py`；声明补充了静态类型信息。

anchorFrom、anchorTo 和 setAnchors 接受的锚点常量。

## 获取方式

从 ModSAPI.ui 导入，作为锚点属性和 setAnchors 的参数。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-TopLeft" />`TopLeft` | [str](../../common/type-system.md#str) | `'top_left'` |  |
| <ApiFieldAnchor id="field-TopCenter" />`TopCenter` | [str](../../common/type-system.md#str) | `'top_middle'` |  |
| <ApiFieldAnchor id="field-TopRight" />`TopRight` | [str](../../common/type-system.md#str) | `'top_right'` |  |
| <ApiFieldAnchor id="field-CenterLeft" />`CenterLeft` | [str](../../common/type-system.md#str) | `'left_middle'` |  |
| <ApiFieldAnchor id="field-Center" />`Center` | [str](../../common/type-system.md#str) | `'center'` |  |
| <ApiFieldAnchor id="field-CenterRight" />`CenterRight` | [str](../../common/type-system.md#str) | `'right_middle'` |  |
| <ApiFieldAnchor id="field-BottomLeft" />`BottomLeft` | [str](../../common/type-system.md#str) | `'bottom_left'` |  |
| <ApiFieldAnchor id="field-BottomCenter" />`BottomCenter` | [str](../../common/type-system.md#str) | `'bottom_middle'` |  |
| <ApiFieldAnchor id="field-BottomRight" />`BottomRight` | [str](../../common/type-system.md#str) | `'bottom_right'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
from ModSAPI.ui import UiAnchor

def align(control):
    control.setAnchors(UiAnchor.TopLeft)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)