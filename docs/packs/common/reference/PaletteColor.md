---
title: "PaletteColor"
sidebar_label: "PaletteColor"
---

import ApiFieldAnchor from '@docusaurus/Link';

# PaletteColor

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/enums/stable.py`；声明补充了静态类型信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-White" />`White` | [int](../type-system.md#int) | `0` |  |
| <ApiFieldAnchor id="field-Orange" />`Orange` | [int](../type-system.md#int) | `1` |  |
| <ApiFieldAnchor id="field-Magenta" />`Magenta` | [int](../type-system.md#int) | `2` |  |
| <ApiFieldAnchor id="field-LightBlue" />`LightBlue` | [int](../type-system.md#int) | `3` |  |
| <ApiFieldAnchor id="field-Yellow" />`Yellow` | [int](../type-system.md#int) | `4` |  |
| <ApiFieldAnchor id="field-Lime" />`Lime` | [int](../type-system.md#int) | `5` |  |
| <ApiFieldAnchor id="field-Pink" />`Pink` | [int](../type-system.md#int) | `6` |  |
| <ApiFieldAnchor id="field-Gray" />`Gray` | [int](../type-system.md#int) | `7` |  |
| <ApiFieldAnchor id="field-Silver" />`Silver` | [int](../type-system.md#int) | `8` |  |
| <ApiFieldAnchor id="field-Cyan" />`Cyan` | [int](../type-system.md#int) | `9` |  |
| <ApiFieldAnchor id="field-Purple" />`Purple` | [int](../type-system.md#int) | `10` |  |
| <ApiFieldAnchor id="field-Blue" />`Blue` | [int](../type-system.md#int) | `11` |  |
| <ApiFieldAnchor id="field-Brown" />`Brown` | [int](../type-system.md#int) | `12` |  |
| <ApiFieldAnchor id="field-Green" />`Green` | [int](../type-system.md#int) | `13` |  |
| <ApiFieldAnchor id="field-Red" />`Red` | [int](../type-system.md#int) | `14` |  |
| <ApiFieldAnchor id="field-Black" />`Black` | [int](../type-system.md#int) | `15` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 PaletteColor 对象。
    print(value.White)
    print(value.Orange)
    print(value.Magenta)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)