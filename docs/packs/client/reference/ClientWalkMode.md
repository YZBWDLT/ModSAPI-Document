---
title: "ClientWalkMode"
sidebar_label: "ClientWalkMode"
---

import ApiFieldAnchor from '@docusaurus/Link';

# ClientWalkMode

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Input.py`；声明补充了静态类型信息。

原生选择的行走模式，与实际玩家速度分别读取。

## 获取方式

从 ModSAPI.client.beta 导入常量，与 client.input.walkMode 的当前结果比较。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-Walk" />`Walk` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'walk'` | 原生普通行走模式。 |
| <ApiFieldAnchor id="field-Sneak" />`Sneak` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'sneak'` | 原生潜行模式。 |
| <ApiFieldAnchor id="field-Sprint" />`Sprint` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'sprint'` | 原生跑步模式；玩家当前没有移动时也可能保持此模式。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientWalkMode 对象。
    print(value.Walk)
    print(value.Sneak)
    print(value.Sprint)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)