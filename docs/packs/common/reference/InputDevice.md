---
title: "InputDevice"
sidebar_label: "InputDevice"
---

# InputDevice

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/event_values.py`；声明补充了静态类型信息。

物理输入设备来源；这些值不对应微软的 [InputMode](InputMode.md) 枚举。

## 获取方式

从 ModSAPI.client.beta 导入，用于输入事件的 devices 筛选。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `Keyboard` | [str](../type-system.md#str) | `'Keyboard'` |  |
| `Gamepad` | [str](../type-system.md#str) | `'Gamepad'` |  |
| `Mouse` | [str](../type-system.md#str) | `'Mouse'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 InputDevice 对象。
    print(value.Keyboard)
    print(value.Gamepad)
    print(value.Mouse)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)