---
title: "UiImageFit"
sidebar_label: "UiImageFit"
---

import ApiFieldAnchor from '@docusaurus/Link';

# UiImageFit

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/constants.py`；声明补充了静态类型信息。

[UiImage.setImageFit](UiImage.md#setImageFit) 接受的图片适配方式。

## 获取方式

从 ModSAPI.ui 导入，作为 [UiImage.setImageFit](UiImage.md#setImageFit) 的适配方式。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-Normal" />`Normal` | [str](../../common/type-system.md#str) | `'normal'` |  |
| <ApiFieldAnchor id="field-Filled" />`Filled` | [str](../../common/type-system.md#str) | `'filled'` |  |
| <ApiFieldAnchor id="field-NineSlice" />`NineSlice` | [str](../../common/type-system.md#str) | `'nineSlice'` |  |
| <ApiFieldAnchor id="field-LegacyNineSlice" />`LegacyNineSlice` | [str](../../common/type-system.md#str) | `'legacyNineSlice'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
from ModSAPI.ui import UiImageFit

def fit_background(image):
    image.setImageFit(UiImageFit.NineSlice, {"left": 4, "right": 4, "top": 4, "bottom": 4})
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)