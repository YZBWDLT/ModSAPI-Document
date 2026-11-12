---
title: "ClientControlMode"
sidebar_label: "ClientControlMode"
---

import ApiFieldAnchor from '@docusaurus/Link';

# ClientControlMode

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Input.py`；声明补充了静态类型信息。

明确指定原生触控布局和交互方式。

## 获取方式

从 ModSAPI.client.beta 导入常量，传给 client.input.setControlMode；方向键准星为明确的两步组合请求。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-JoystickTouch" />`JoystickTouch` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'joystickTouch'` | 摇杆移动与点击互动。 |
| <ApiFieldAnchor id="field-JoystickCrosshair" />`JoystickCrosshair` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'joystickCrosshair'` | 摇杆移动与准星瞄准。 |
| <ApiFieldAnchor id="field-DirectionalTouch" />`DirectionalTouch` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'directionalTouch'` | 方向键移动与点击互动。 |
| <ApiFieldAnchor id="field-DirectionalCrosshair" />`DirectionalCrosshair` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'directionalCrosshair'` | 先选择方向键布局，再调用该布局的原生准星开关。此组合请求需要两项原生方法，可用性取决于客户端版本和触控布局；它不是引擎三值控制模式枚举之外可通用的第四个编号。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientControlMode 对象。
    print(value.JoystickTouch)
    print(value.JoystickCrosshair)
    print(value.DirectionalTouch)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)