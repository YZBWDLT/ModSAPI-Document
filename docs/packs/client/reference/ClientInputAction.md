---
title: "ClientInputAction"
sidebar_label: "ClientInputAction"
---

import ApiFieldAnchor from '@docusaurus/Link';

# ClientInputAction

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Input.py`；声明补充了静态类型信息。

一次本地原生动作请求，不表示持续按住键盘或按钮。

## 获取方式

从 ModSAPI.client.beta 导入常量，传给 client.input.triggerAction。它们是一次本地请求，不是持续按键状态。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-Jump" />`Jump` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'jump'` | 请求原生跳跃动作，不保证玩家实际跳起。 |
| <ApiFieldAnchor id="field-ToggleSneak" />`ToggleSneak` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'toggleSneak'` | 请求原生潜行切换，不是将潜行设置为指定布尔状态。 |
| <ApiFieldAnchor id="field-Interact" />`Interact` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'interact'` | 请求当前情景交互按钮，不传入目标标识。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientInputAction 对象。
    print(value.Jump)
    print(value.ToggleSneak)
    print(value.Interact)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)