---
title: "EasingType"
sidebar_label: "EasingType"
---

import ApiFieldAnchor from '@docusaurus/Link';

# EasingType

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/enums/stable.py`；声明补充了静态类型信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-InBack" />`InBack` | [str](../type-system.md#str) | `'InBack'` |  |
| <ApiFieldAnchor id="field-InBounce" />`InBounce` | [str](../type-system.md#str) | `'InBounce'` |  |
| <ApiFieldAnchor id="field-InCirc" />`InCirc` | [str](../type-system.md#str) | `'InCirc'` |  |
| <ApiFieldAnchor id="field-InCubic" />`InCubic` | [str](../type-system.md#str) | `'InCubic'` |  |
| <ApiFieldAnchor id="field-InElastic" />`InElastic` | [str](../type-system.md#str) | `'InElastic'` |  |
| <ApiFieldAnchor id="field-InExpo" />`InExpo` | [str](../type-system.md#str) | `'InExpo'` |  |
| <ApiFieldAnchor id="field-InOutBack" />`InOutBack` | [str](../type-system.md#str) | `'InOutBack'` |  |
| <ApiFieldAnchor id="field-InOutBounce" />`InOutBounce` | [str](../type-system.md#str) | `'InOutBounce'` |  |
| <ApiFieldAnchor id="field-InOutCirc" />`InOutCirc` | [str](../type-system.md#str) | `'InOutCirc'` |  |
| <ApiFieldAnchor id="field-InOutCubic" />`InOutCubic` | [str](../type-system.md#str) | `'InOutCubic'` |  |
| <ApiFieldAnchor id="field-InOutElastic" />`InOutElastic` | [str](../type-system.md#str) | `'InOutElastic'` |  |
| <ApiFieldAnchor id="field-InOutExpo" />`InOutExpo` | [str](../type-system.md#str) | `'InOutExpo'` |  |
| <ApiFieldAnchor id="field-InOutQuad" />`InOutQuad` | [str](../type-system.md#str) | `'InOutQuad'` |  |
| <ApiFieldAnchor id="field-InOutQuart" />`InOutQuart` | [str](../type-system.md#str) | `'InOutQuart'` |  |
| <ApiFieldAnchor id="field-InOutQuint" />`InOutQuint` | [str](../type-system.md#str) | `'InOutQuint'` |  |
| <ApiFieldAnchor id="field-InOutSine" />`InOutSine` | [str](../type-system.md#str) | `'InOutSine'` |  |
| <ApiFieldAnchor id="field-InQuad" />`InQuad` | [str](../type-system.md#str) | `'InQuad'` |  |
| <ApiFieldAnchor id="field-InQuart" />`InQuart` | [str](../type-system.md#str) | `'InQuart'` |  |
| <ApiFieldAnchor id="field-InQuint" />`InQuint` | [str](../type-system.md#str) | `'InQuint'` |  |
| <ApiFieldAnchor id="field-InSine" />`InSine` | [str](../type-system.md#str) | `'InSine'` |  |
| <ApiFieldAnchor id="field-Linear" />`Linear` | [str](../type-system.md#str) | `'Linear'` |  |
| <ApiFieldAnchor id="field-OutBack" />`OutBack` | [str](../type-system.md#str) | `'OutBack'` |  |
| <ApiFieldAnchor id="field-OutBounce" />`OutBounce` | [str](../type-system.md#str) | `'OutBounce'` |  |
| <ApiFieldAnchor id="field-OutCirc" />`OutCirc` | [str](../type-system.md#str) | `'OutCirc'` |  |
| <ApiFieldAnchor id="field-OutCubic" />`OutCubic` | [str](../type-system.md#str) | `'OutCubic'` |  |
| <ApiFieldAnchor id="field-OutElastic" />`OutElastic` | [str](../type-system.md#str) | `'OutElastic'` |  |
| <ApiFieldAnchor id="field-OutExpo" />`OutExpo` | [str](../type-system.md#str) | `'OutExpo'` |  |
| <ApiFieldAnchor id="field-OutQuad" />`OutQuad` | [str](../type-system.md#str) | `'OutQuad'` |  |
| <ApiFieldAnchor id="field-OutQuart" />`OutQuart` | [str](../type-system.md#str) | `'OutQuart'` |  |
| <ApiFieldAnchor id="field-OutQuint" />`OutQuint` | [str](../type-system.md#str) | `'OutQuint'` |  |
| <ApiFieldAnchor id="field-OutSine" />`OutSine` | [str](../type-system.md#str) | `'OutSine'` |  |
| <ApiFieldAnchor id="field-Spring" />`Spring` | [str](../type-system.md#str) | `'Spring'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EasingType 对象。
    print(value.InBack)
    print(value.InBounce)
    print(value.InCirc)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)