---
title: "ClientInputPermission"
sidebar_label: "ClientInputPermission"
---

# ClientInputPermission

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Input.py`；声明补充了静态类型信息。

网易原生输入通道，与微软输入权限类别的含义和组合规则不同。

## 获取方式

从 ModSAPI.client.beta 导入，使用常量选择网易原生输入通道。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `Attack` | [str](../../common/type-system.md#str) | `'attack'` | 原生攻击输入响应。 |
| `Chat` | [str](../../common/type-system.md#str) | `'chat'` | 原生聊天按钮响应。 |
| `ScreenDrag` | [str](../../common/type-system.md#str) | `'screenDrag'` | 原生输入处理中的屏幕拖动。 |
| `VerticalMovement` | [str](../../common/type-system.md#str) | `'verticalMovement'` | 飞行上升、下降按钮响应；不改变飞行能力。 |
| `Jump` | [str](../../common/type-system.md#str) | `'jump'` | 原生跳跃及游泳上升输入响应。 |
| `Movement` | [str](../../common/type-system.md#str) | `'movement'` | 原生移动按键或摇杆响应。 |
| `Inventory` | [str](../../common/type-system.md#str) | `'inventory'` | 打开物品栏的输入响应；不改变物品栏内容或服务端权限。 |
| `PauseButton` | [str](../../common/type-system.md#str) | `'pauseButton'` | 原生暂停按钮响应。 |
| `PauseScreen` | [str](../../common/type-system.md#str) | `'pauseScreen'` | 打开原生暂停界面的能力。 |
| `Perspective` | [str](../../common/type-system.md#str) | `'perspective'` | 原生视角切换输入响应。 |
| `Screenshot` | [str](../../common/type-system.md#str) | `'screenshot'` | 游戏内截图按钮响应。 |
| `WalkModeSwitch` | [str](../../common/type-system.md#str) | `'walkModeSwitch'` | 原生行走模式切换输入响应。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientInputPermission 对象。
    print(value.Attack)
    print(value.Chat)
    print(value.ScreenDrag)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)