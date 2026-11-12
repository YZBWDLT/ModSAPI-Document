---
title: "UiNativeArea"
sidebar_label: "UiNativeArea"
---

# UiNativeArea

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/display.py`；声明补充了静态类型信息。

使用原生基类画布坐标的已记录区域名称。

## 获取方式

从 ModSAPI.ui 导入常量，传给 [client.ui.getNativeArea](UiService.md#getNativeArea)。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `MoveUpButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.move_up'` | 方向键布局的上移按钮。 |
| `MoveDownButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.move_down'` | 方向键布局的下移按钮。 |
| `MoveLeftButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.move_left'` | 方向键布局的左移按钮。 |
| `MoveRightButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.move_right'` | 方向键布局的右移按钮。 |
| `SneakButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.sneak'` | 经典触控布局的潜行按钮。 |
| `JoystickSneakButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.sneak_new_controls'` | 摇杆触控布局的潜行或下降按钮。 |
| `JumpButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.jump'` | 经典触控布局的跳跃按钮。 |
| `JoystickJumpButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.jump_new_controls'` | 摇杆触控布局的跳跃或上升按钮。 |
| `SprintButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.sprint'` | 疾跑切换按钮。 |
| `AscendButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.ascend'` | 飞行上升按钮。 |
| `DescendButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.descend'` | 飞行下降按钮。 |
| `PauseButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.pause'` | 暂停按钮。 |
| `ChatButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.chat'` | 旧版聊天按钮；区域不可用时可能返回全零。 |
| `MenuButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.fold_menu'` | 下拉菜单按钮。 |
| `PerspectiveButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.camera_view'` | 摄像机视角切换按钮。 |
| `AttackButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.destroy_or_attack'` | 破坏或攻击按钮。 |
| `InteractButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.build_or_interact'` | 建造或交互按钮。 |
| `MovementJoystick` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.default_move_stick_area'` | 移动摇杆区域。 |
| `WalkState` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.walkstate'` | 方向键布局的强制疾跑按钮。 |
| `StatusEffects` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.mobeffects'` | 状态效果区域。 |
| `EmoteButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.emote'` | 表情按钮。 |
| `TurnInteract` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.turn_interact'` | 文档支持但原生枚举尚未列出的转向交互区域。 |
| `DirectionalInteract` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.dpad_no_turn_interact'` | 方向键布局中不转向的交互区域。 |
| `DisabledJumpButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.disable_jump'` | 已禁用跳跃按钮的区域。 |
| `DisabledSneakButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.disable_sneak'` | 已禁用潜行按钮的区域。 |
| `InputPassthrough` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.gui_passthrough'` | 原生界面的输入穿透区域。 |
| `FlightHeight` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.changing_flight_height'` | 飞行高度调整区域。 |
| `InvisibleMoveUpButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.move_up_invisible'` | 隐藏的向上移动按钮区域。 |
| `DirectionalHeightPanel` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.middle_right'` | 方向键布局的上升和下降面板。 |
| `CodeBuilderButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.code_builder'` | 原生客户端提供时的教育版编程按钮。 |
| `MoveUpLeftButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.move_up_left'` | 方向键布局的左上移动按钮。 |
| `MoveUpRightButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.move_up_right'` | 方向键布局的右上移动按钮。 |
| `PlayerEffects` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.player_effects'` | 玩家效果区域，与旧版状态效果区域不同。 |
| `RightPaddleButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.paddle_right'` | 右侧划船按钮。 |
| `RightPaddleBorder` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.paddle_right_border'` | 右侧划船按钮边界。 |
| `LeftPaddleButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.paddle_left'` | 左侧划船按钮。 |
| `LeftPaddleBorder` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.paddle_left_border'` | 左侧划船按钮边界。 |
| `Toast` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.toast'` | 原生提示区域。 |
| `KeyJoystick` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.keyjoy'` | 原生按键或摇杆区域。 |
| `KeyJoystickSneak` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.sneak_jk'` | 按键或摇杆布局的潜行按钮。 |
| `StoreButton` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.store'` | 商店按钮区域。 |
| `ViewState` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.vstate0'` | 原生视图状态区域，是否提供由当前布局决定。 |
| `VoiceTranscription` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'binding.area.voice_trans'` | 语音转文字区域；被好友入口替代时可能不存在。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UiNativeArea 对象。
    print(value.MoveUpButton)
    print(value.MoveDownButton)
    print(value.MoveLeftButton)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)