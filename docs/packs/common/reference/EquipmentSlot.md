---
title: "EquipmentSlot"
sidebar_label: "EquipmentSlot"
---

import ApiFieldAnchor from '@docusaurus/Link';

# EquipmentSlot

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/enums/Entity.py`；声明补充了静态类型信息。

生物的装备槽位，包括护甲、副手和主手。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-Body" />`Body` | 由运行时值确定 | `'Body'` |  |
| <ApiFieldAnchor id="field-Head" />`Head` | 由运行时值确定 | `'Head'` |  |
| <ApiFieldAnchor id="field-Chest" />`Chest` | 由运行时值确定 | `'Chest'` |  |
| <ApiFieldAnchor id="field-Legs" />`Legs` | 由运行时值确定 | `'Legs'` |  |
| <ApiFieldAnchor id="field-Feet" />`Feet` | 由运行时值确定 | `'Feet'` |  |
| <ApiFieldAnchor id="field-Offhand" />`Offhand` | 由运行时值确定 | `'Offhand'` |  |
| <ApiFieldAnchor id="field-Mainhand" />`Mainhand` | 由运行时值确定 | `'Mainhand'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EquipmentSlot 对象。
    print(value.Body)
    print(value.Head)
    print(value.Chest)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)