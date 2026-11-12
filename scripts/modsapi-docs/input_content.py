"""Chinese guidance for local input and view-scoped permission ownership."""

INPUT_GUIDES = {
    'packs/guides/input-and-view-permissions.md': r'''---
title: 本地输入与界面权限
---

# 本地输入与界面权限

[Client.input](../client/apis/manager.md#input) 提供当前设备的输入状态和权限操作，返回 [ClientInput](../client/reference/ClientInput.md)。这里的权限控制本地输入响应，不授予飞行能力，也不能代替服务端对玩家行为的校验。

## 用界面管理临时权限

打开菜单时，直接把 `inputPermissions` 传给 [UiService.openView](../ui/reference/UiService.md#openView)。视图持有临时权限，关闭或创建失败时尝试恢复；无需自己写全局的“关闭菜单就允许移动”。[UiService.createHud](../ui/reference/UiService.md#createHud) 也接受同一字段，常驻界面按需选择。

```python
from ModSAPI.client.beta import client, ClientInputPermission

def view_ready(event):
    close_button = event.view.getControl("/panel/close", "button")
    close_button.afterEvents.click.subscribe(lambda clicked: clicked.view.close())

client.ui.registerView("demo:menu", "demo_ui.screen", {"onReady": view_ready})

def ui_ready(event):
    client.ui.openView("demo:menu", {
        "inputPermissions": {
            ClientInputPermission.Movement: False,
            ClientInputPermission.Attack: False,
        },
    })

client.afterEvents.uiReady.subscribe(ui_ready)
```

示例使用自己的 `demo_ui.screen` 资源模板，模板编写与创建时机见[界面、控件与生命周期](managed-ui.md)。字段类型见 [UiViewOptions](../ui/reference/UiViewOptions.md) 和 [UiHudOptions](../ui/reference/UiHudOptions.md)。权限字典会被复制，不会混入 `view.data` 或原生创建参数。

此自动管理针对原生 [UiView](../ui/reference/UiView.md)。主题 [Form](../ui/reference/Form.md) 的显示选项没有此字段；需要在其他流程中临时接管输入时，使用下方的权限句柄，并在所属流程结束时释放。

## 临时覆盖与基础值

```python
from ModSAPI.client.beta import client, ClientInputPermission

channel = ClientInputPermission.Movement
first = client.input.overridePermissions({channel: False})
second = client.input.overridePermissions({channel: False})

first.dispose()   # 第二层仍然有效，不会解锁移动。
second.dispose()  # 恢复覆盖之前的基础值，不会一律设成 True。
```

[overridePermissions](../client/reference/ClientInput.md#overridePermissions) 返回 [ClientInputOverride](../client/reference/ClientInputOverride.md)，通过其 [dispose](../client/reference/ClientInputOverride.md#dispose) 释放。多个覆盖层按创建顺序决定同一通道的有效值，较晚的层优先，也可以不按顺序释放。空字典返回已经释放的空句柄，不调用原生接口。

[setPermission](../client/reference/ClientInput.md#setPermission) 修改本服务持有的基础值；临时层存在时，基础值等该层释放后生效。[getPermission](../client/reference/ClientInput.md#getPermission) 始终读取当前原生有效值，[getPermissions](../client/reference/ClientInput.md#getPermissions) 返回独立字典。以下示例中，读取结果在释放前仍为 `False`。

```python
from ModSAPI.client.beta import client, ClientInputPermission

channel = ClientInputPermission.Attack
lease = client.input.overridePermissions({channel: False})
try:
    client.input.setPermission(channel, True)
    print(client.input.getPermission(channel))
finally:
    lease.dispose()
```

[reset](../client/reference/ClientInput.md#reset) 尝试恢复本服务持有的全部初始值，并释放包括界面在内的所有输入覆盖层。它适合整体退出或错误恢复，可能同时解除仍在显示的界面的输入限制；单个流程结束优先释放自己的句柄。客户端销毁时也会尝试清理。

## 可控制的输入通道

从客户端入口导入 [ClientInputPermission](../client/reference/ClientInputPermission.md)，避免手写通道字符串。

| 常量 | 控制范围 |
| --- | --- |
| Attack | 攻击输入响应 |
| Chat | 聊天按钮响应 |
| ScreenDrag | 原生输入处理中的屏幕拖动 |
| VerticalMovement | 飞行上升、下降按钮响应，不改变飞行能力 |
| Jump | 跳跃及游泳上升输入响应 |
| Movement | 原生移动按键或摇杆响应 |
| Inventory | 打开物品栏的输入响应，不改变物品栏内容 |
| PauseButton | 暂停按钮响应 |
| PauseScreen | 打开暂停界面的能力 |
| Perspective | 视角切换输入响应 |
| Screenshot | 游戏内截图按钮响应 |
| WalkModeSwitch | 行走模式切换输入响应 |

这些通道按照网易原生含义划分，与微软 `InputPermissionCategory` 的类别及组合语义不同，不能互相代用。原生移动权限写入会清空已有输入方向；库避免不必要的相同值写入，但重新允许移动不会重放玩家仍按住的按键。

## 读取方向和指针位置

```python
from ModSAPI.client.beta import client

movement = client.input.getMovementVector()
print(movement.x, movement.y)

mouse = client.input.getMousePosition()
if mouse is not None:
    print(mouse.x, mouse.y)
```

[getMovementVector](../client/reference/ClientInput.md#getMovementVector) 返回 [Vector2](../common/reference/Vector2.md)，正 X 表示向右，正 Y 表示向前。原生第一分量向左为正，适配时会取反。这里读取输入意图，不读取实体速度。

[getMousePosition](../client/reference/ClientInput.md#getMousePosition) 在非电脑平台可能返回 [None](../common/type-system.md#none)；网易仅保证通过原生界面栈打开界面期间能正确取得鼠标位置。结果保留原生屏幕坐标，不自动换算成控件局部坐标。

[getTouchPosition](../client/reference/ClientInput.md#getTouchPosition) 用于点击或长按释放回调内读取触摸位置。[isMouseEmulatingTouch](../client/reference/ClientInput.md#isMouseEmulatingTouch) 读取电脑端鼠标模拟触摸状态，不能据此推断所有平台的输入方式。

## 长按阈值与错误恢复

[holdThresholdMilliseconds](../client/reference/ClientInput.md#holdThresholdMilliseconds) 使用整数毫秒，原生默认值为 400。写入时拒绝布尔值和负数，`reset()` 尝试恢复本服务修改前的值。

```python
from ModSAPI.client.beta import client

client.input.holdThresholdMilliseconds = 500
```

未知通道或非法值在原生写入前报告 [TypeError](../common/type-system.md#typeerror) 或 [ValueError](../common/type-system.md#valueerror)。会话已经失效时抛出 [InvalidClientObjectError](../common/reference/InvalidClientObjectError.md)；原生缺少方法时抛出 [UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)，原生异常、失败结果或不合法的返回数据抛出 [NativeOperationError](../common/reference/NativeOperationError.md)，保留操作名称及原因。

创建覆盖层失败会尝试逐项回滚。释放某一项失败时，仍继续释放其他项，仅保留尚未完成的部分供重试；通过 [ClientInput.overrides](../client/reference/ClientInput.md#overrides) 可以查看仍持有的句柄。视图原生关闭成功但输入恢复失败时，`view.close()` 报告错误，视图已经关闭且关闭事件只触发一次；再次调用 `view.close()` 会重试输入恢复。也可整体调用 `client.input.reset()`。

原生权限接口没有跨模组的所有权标记。释放时若读到其他代码写入了不同值，库会保留该值；相同值的外部写入无法识别。这些操作不是跨模组事务，不能保证在原生接口持续拒绝恢复时仍能解除限制。当前离线测试验证了适配契约、嵌套覆盖和失败重试；各平台及游戏内表现仍待实测。
''',
}

INPUT_ACQUIRE = {
    'ClientInput': '通过 client.input 取得本地输入服务，无需手动构造或注册系统。权限仅影响当前设备，不代表服务端授权。',
    'ClientInputOverride': '通过 client.input.overridePermissions(...) 取得；流程结束时调用 dispose()，失败后可以重试。不要手动构造。',
    'ClientInputPermission': '从 ModSAPI.client.beta 导入，使用常量选择网易原生输入通道。',
}

INPUT_NOTES = {
    'Client.input': '本地输入服务按需创建。临时覆盖使用可释放句柄；原生视图可通过 inputPermissions 选项自动持有并释放。教程见“本地输入与界面权限”。',
    'ClientInput.reset': '恢复全部由本服务持有的修改，包括尚未关闭的界面的输入覆盖。通常优先释放所属流程自己的句柄。外部不同值会保留，相同值写入无法识别；恢复失败可重试。',
    'ClientInputPermission.Movement': '仅控制网易的移动输入响应，不具有微软 InputPermissionCategory.Movement 的组合语义。写入原生移动权限可能清空现有输入方向。',
    'UiService.openView': '可在 inputPermissions 中传入本地输入通道与布尔值。覆盖在原生创建前应用，视图关闭或创建失败时尝试释放；不影响服务端权限。',
}
