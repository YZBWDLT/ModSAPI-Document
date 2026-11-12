---
title: "UiHudElement"
sidebar_label: "UiHudElement"
---

# UiHudElement

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/display.py`；声明补充了静态类型信息。

网易原生抬头显示通道，与微软 [HudElement](../../common/reference/HudElement.md) 枚举不同。可用性取决于平台、控制布局和聊天实现。原生接口没有显隐读取；常量不是实际可见性快照，也不会在所属客户端退出时自动恢复。

## 获取方式

从 ModSAPI.ui 导入常量，传给 [UiHud.setHudVisibility](UiHud.md#setHudVisibility)；不使用微软 [HudElement](../../common/reference/HudElement.md) 的数字值。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `AirBubbles` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'airBubbles'` | 本地玩家氧气值显示。 |
| `Armor` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'armor'` | 抬头显示中的护甲值。 |
| `PerspectiveButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'perspectiveButton'` | 人称切换按钮；隐藏时也会停止该按钮的触控响应。 |
| `ChatButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'chatButton'` | 旧版聊天入口按钮；新版聊天扩展使用其他入口。 |
| `Crosshair` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'crosshair'` | 准心可见性；不修改原生瞄准模式。 |
| `EmoteButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'emoteButton'` | 手机端旧版表情按钮；部分聊天实现中不可用。 |
| `ProgressBar` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'progressBar'` | 非创造模式下的经验条显示。 |
| `MenuButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'menuButton'` | 原版下拉菜单按钮。 |
| `Health` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'health'` | 抬头显示中的本地玩家生命值。 |
| `HorseHealth` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'horseHealth'` | 抬头显示中的坐骑生命值。 |
| `Hunger` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'hunger'` | 抬头显示中的本地玩家饥饿值。 |
| `InteractButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'interactButton'` | 触控交互按钮；隐藏时也会停止其响应。 |
| `JumpButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'jumpButton'` | 触控跳跃按钮；隐藏时也会停止其响应。 |
| `MovementButtons` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'movementButtons'` | 触控移动按钮；隐藏时也会停止其响应。 |
| `StoreButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'storeButton'` | 网易商店入口；不支持山头服环境。 |
| `PauseButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'pauseButton'` | 原版暂停按钮。 |
| `Hotbar` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'hotbar'` | 快捷栏；其原生层级会连带影响经验条。 |
| `SneakButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'sneakButton'` | 触控潜行按钮；隐藏时也会停止其响应。 |
| `SwimButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'swimButton'` | 触控浮潜按钮；隐藏时也会停止其响应。 |
| `VoiceButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'voiceButton'` | 旧版语音按钮；新版聊天扩展可能不响应此通道。 |
| `WalkModeButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'walkModeButton'` | 触控走跑切换按钮；隐藏时也会停止其响应。 |
| `ChatMessages` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'chatMessages'` | 抬头显示中的小消息窗口，与聊天打开按钮分别控制。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UiHudElement 对象。
    print(value.AirBubbles)
    print(value.Armor)
    print(value.PerspectiveButton)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)