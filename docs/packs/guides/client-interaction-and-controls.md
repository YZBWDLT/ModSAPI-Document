---
title: 本地交互与触控布局
---

# 本地交互与触控布局

[ClientInput](../client/reference/ClientInput.md) 从 [client.input](../client/apis/manager.md#input) 取得，统一处理本机输入读取、动作请求与控制配置。它不授予服务端权限，不代替服务端验证，也不代表所有平台采用相同的触控布局。临时菜单输入限制优先使用 [本地输入与界面权限](input-and-view-permissions.md) 的可释放句柄。

## 用一个入口请求本地动作

```python
from ModSAPI.client.beta import client, ClientInputAction

def request_jump():
    client.input.triggerAction(ClientInputAction.Jump)

def request_sneak_toggle():
    client.input.triggerAction(ClientInputAction.ToggleSneak)

def request_context_interaction():
    client.input.triggerAction(ClientInputAction.Interact)
```

[ClientInputAction](../client/reference/ClientInputAction.md) 将跳跃、潜行切换和当前情景交互整理到 `triggerAction()`。它只发出一次请求，不模拟持续按住按键，也不推断目标实体或方块。

潜行是切换请求，不能把它当作“设置为潜行”；动作能否完成由当前游戏条件决定。交互使用原生情景按钮，可能对应骑乘、喂食、钓鱼、交易或装备等行为，不是任意目标交互接口。

原生方法没有动作完成结果，返回 [None](../common/type-system.md#none) 不保证玩家已跳起或交互已发生。同步回调中再次触发动作会被拒绝，防止递归请求；动作成功与否不能根据“没有抛出异常”推断。

## 读取当前行走模式

```python
from ModSAPI.client.beta import ClientWalkMode

def uses_running_mode():
    return client.input.walkMode == ClientWalkMode.Sprint
```

[ClientWalkMode](../client/reference/ClientWalkMode.md) 提供 Walk、Sneak、Sprint 三个常量。`walkMode` 每次重新读取原生模式，不缓存为实际运动状态。原生编号一、二、三分别转换为这些名称；未知编号、布尔值和损坏结果会报告错误。

需要判断玩家是否实际移动、疾跑或潜行时，读取 [ClientPlayer](../client/reference/ClientPlayer.md) 的相应状态或速度。行走模式和当前运动不是同一件事。

## 明确选择触控布局与瞄准方式

```python
from ModSAPI.client.beta import ClientControlMode

def select_crosshair_joystick():
    client.input.setControlMode(ClientControlMode.JoystickCrosshair, {
        "locked": True,
    })

def allow_control_settings():
    client.input.setControlModeLocked(False)
```

[ClientControlMode](../client/reference/ClientControlMode.md) 提供四种请求，避免直接面对含义随布局变化的原生布尔开关。

| 常量 | 目标布局 | 原生请求 |
| --- | --- | --- |
| JoystickTouch | 摇杆移动、点击互动 | 一次控制模式设置 |
| JoystickCrosshair | 摇杆移动、准星瞄准 | 一次控制模式设置 |
| DirectionalTouch | 方向键移动、点击互动 | 一次控制模式设置 |
| DirectionalCrosshair | 方向键移动，再启用该布局的准星开关 | 两步组合请求，取决于版本和布局支持 |

方向键准星不是引擎控制模式的第四个编号。库先选择方向键布局，再调用对应的原生准星开关；不会凭空传入编号三。两步都具备方法时才开始写入，但后续原生失败仍可能保留第一步修改，不提供事务或旧值回滚。其实际界面效果尚待游戏验证。

[ClientControlModeOptions](../client/reference/ClientControlModeOptions.md) 的 locked 为可选布尔字段，在布局请求成功后应用；整批参数及方法是否存在会在写入前校验。没有传入 locked 时不修改锁定状态。`setControlModeLocked()` 只调整设置是否可改变，不重新选择布局。

这些接口配置触控布局，不重新映射物理键盘或手柄按键。目前没有已核验的布局及锁定旧值读取，`reset()` 不会猜测它们原先的值。不要把此处的直接设置当作 [ClientInputOverride](../client/reference/ClientInputOverride.md) 的可释放覆盖层。

## 原生点击响应与临时权限

```python
def configure_native_response(enabled):
    client.input.setNativeResponseEnabled(enabled)
```

`setNativeResponseEnabled()` 调整原生点击响应，包括点击屏幕破坏方块或攻击实体。它不承诺禁用所有设备、所有按键或自定义界面。原生接口没有对应的已核验读取，因此没有伪造状态属性，也不会在 `reset()` 或客户端销毁时一律写回 True。

需要打开菜单期间限制移动、攻击或背包输入时，优先使用 `inputPermissions` 或 `overridePermissions()`。这些具备读取和所有权管理，含义与直接控制原生点击响应不同。

## 电脑端鼠标模拟触控

```python
def enter_mouse_ui_mode():
    client.input.isMouseEmulatingTouch = True

def restore_owned_input_changes():
    client.input.reset()
```

`isMouseEmulatingTouch` 的读取始终查询当前原生状态；写入对应电脑端类似 F11 的鼠标界面模式。它不是通用的输入设备检测接口。参数必须为布尔值；相同状态的写入不创建原生游戏组件，也不取得恢复所有权。

首次实际修改会保留可读取的初始值。`reset()` 和客户端销毁会尝试恢复本库持有的修改；读取到不同的外部写入时保留外部值。原生写入失败可能已经部分生效，因此会保留未确认的清理状态，供后续重试。无法识别其他代码写入相同值的情况，也不提供跨模组隔离。

鼠标恢复与普通权限恢复分别尝试。一项权限或组件获取失败，不会阻止另一项恢复；失败部分继续保留。`reset()` 会同时释放仍在显示的视图所持有的输入权限，单个菜单结束应优先关闭自己的视图或释放自己的句柄。

## 表情功能必须在原生界面初始化前配置

```python
def configure_before_native_ui():
    client.ui.setEmotesEnabled(False)
```

[UiService.setEmotesEnabled](../ui/reference/UiService.md#setEmotesEnabled) 对应原生手机端表情功能配置。在客户端初始化阶段、原生界面初始化事件之前调用；不要放进 `uiReady` 回调。它与 [UiHudElement.EmoteButton](../ui/reference/UiHudElement.md#field-EmoteButton) 的“隐藏已经创建的按钮”不同。

库记录原生初始化事件是否已发生。即使表单注册随后失败、`isReady` 仍为 False，也会拒绝迟到的表情配置，不把“托管表单尚未就绪”误认为“原生界面尚未初始化”。此方法仅支持客户端，具体平台能力和执行效果由引擎决定；没有伪造配置读取或旧值恢复。

## 同步回调、取消与错误

原生调用可能在返回之前触发同步回调。若回调销毁客户端，输入服务先停止接收新操作，等正在进行的写入返回后再清理所持有的状态，避免提前清空恢复数据。终止清理失败仍会记录原生错误，并保留调用者最初遇到的异常。

视图在准备输入权限时被取消，不会继续调用原生创建。所属客户端失效也会在创建之前重新检查。引擎已经开始创建、但还没有返回或附加可关闭句柄的阶段仍受原生时序限制；不能保证任何时刻都能立即关闭。损坏的创建返回值会报告对应创建操作，并清理已经出现的部分视图和输入资源。

参数错误分别报告 [TypeError](../common/type-system.md#typeerror) 或 [ValueError](../common/type-system.md#valueerror)；会话失效报告 [InvalidClientObjectError](../common/reference/InvalidClientObjectError.md)。SDK 缺少方法报告 [UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)；原生异常、失败标记或损坏结果报告 [NativeOperationError](../common/reference/NativeOperationError.md)，保留实际操作及原因。

本批离线回归验证了调用形状、参数、恢复、同步回调与错误传播；实际动作、触控布局、平台差异和多人时序仍需游戏验证。原生抬头显示、原版界面请求及布局几何另见 [原生抬头显示与原版界面](ui-native-hud-and-screens.md)。

原生调用约定参考 [网易原生界面文档](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md) 与 [网易控制接口文档](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md)。适配器公开名称、组合方式及恢复语义以本页说明为准。