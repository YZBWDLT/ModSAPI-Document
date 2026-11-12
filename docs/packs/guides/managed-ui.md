---
title: 界面、控件与生命周期
---

# 界面、控件与生命周期

界面以视图对象为中心。通过 [client.ui](../client/apis/manager.md#ui) 声明模板，再打开 [UiView](../ui/reference/UiView.md)，从视图取得控件，绑定状态和交互事件，最后关闭视图。该入口与 [client.camera](../client/apis/manager.md#camera)、[client.audio](../client/apis/manager.md#audio) 采用相同的对象和选项字典风格。

| 需要完成的操作 | 使用入口 | 结果 |
| --- | --- | --- |
| 打开自己的界面模板 | `client.ui.openView(...)` | 管理界面栈中的 [UiView](../ui/reference/UiView.md) |
| 创建常驻或跟随实体的界面 | `client.ui.createHud(...)` | 不加入界面栈的 [UiView](../ui/reference/UiView.md) |
| 在本地组合表单 | `client.ui.createForm(...)` | [Form](../ui/reference/Form.md)，省略目标即可显示给本地玩家 |
| 从服务端向玩家显示表单 | `system.ui.createForm(...)` | [Form](../ui/reference/Form.md)，显示时传入 [Player](../server/apis/player.md) 对象 |
| 使用标准表单构建器 | [ActionFormData](../server_ui/reference/ActionFormData.md)、[ModalFormData](../server_ui/reference/ModalFormData.md)、[MessageFormData](../server_ui/reference/MessageFormData.md) | 具有标准返回结果的表单 |

公共类型位于 `ModSAPI.ui`。[UiService](../ui/reference/UiService.md) 由现有客户端和服务端系统提供，使用时无需再注册系统。

## 创建时机

`registerView` 可以在客户端入口加载时声明模板，首次打开时才注册原生界面。打开界面需要等待 [client.afterEvents.uiReady](../client/reference/ClientAfterEvents.md#uiReady)。`openView` 返回时，原生控件可能尚未创建，因此将初始化操作放在注册选项的 `onReady` 回调中。

```python
# -*- coding: utf-8 -*-
from ModSAPI.client.beta import client

def ready(event):
    view = event.view
    title = client.ui.createState(u"欢迎")
    view.afterEvents.close.subscribe(lambda closed: title.dispose())
    view.getControl("/panel/title", "label").bind("text", title)
    close_button = view.getControl("/panel/close", "button")
    close_button.afterEvents.click.subscribe(lambda clicked: clicked.view.close())

client.ui.registerView("demo:settings", "demo_ui.screen", {"onReady": ready})

def ui_ready(event):
    client.ui.openView("demo:settings", {"data": {"section": "general"}})

client.afterEvents.uiReady.subscribe(ui_ready)
```

若在就绪事件触发之后才执行打开逻辑，可以检查 [client.ui.isReady](../ui/reference/UiService.md#isReady)。业务数据从 `view.data` 读取，每次返回独立副本；改变该副本不会修改视图或引擎状态。

原生节点返回后若十五秒内仍未发出创建完成回调，视图会尝试关闭，关闭原因为 creationFailed。等待不采用反复查询；正常创建或主动关闭时会取消这次等待。

此示例依赖自己的资源包模板。将下面的文件加入资源包的界面定义清单，即可对应到 `demo_ui.screen`：

```json
{
  "namespace": "demo_ui",
  "screen": {
    "type": "screen",
    "is_showing_menu": true,
    "controls": [
      {"panel": {
        "type": "panel",
        "size": [240, 120],
        "controls": [
          {"title": {"type": "label", "text": "欢迎", "offset": [0, -20]}},
          {"close": {
            "type": "button",
            "size": [100, 24],
            "offset": [0, 20],
            "controls": [{"label": {"type": "label", "text": "关闭"}}]
          }}
        ]
      }}
    ]
  }
}
```

`namespace:name` 是库内视图标识；`namespace.control` 是资源包中的模板路径。两者含义不同，均由注册接口校验。

## 按控件类型取得接口

```python
def configure(view):
    label = view.getControl("/panel/title", "label")
    label.text = u"设置"
    label.color = (0.3, 0.8, 1.0)
    label.setLayout({"width": "100%-16px", "height": 24})
    label.position = (8, 4)
```

| 控件种类 | 返回类型 | 常用成员 |
| --- | --- | --- |
| `control` | [UiControl](../ui/reference/UiControl.md) | visible、position、size、setLayout、bind、remove |
| `label` | [UiLabel](../ui/reference/UiLabel.md) | text、color、setFontScale |
| `button` | [UiButton](../ui/reference/UiButton.md) | afterEvents.click、指针和悬浮事件 |
| `image` | [UiImage](../ui/reference/UiImage.md) | setImage、setClipRatio |
| `textField` | [UiTextField](../ui/reference/UiTextField.md) | value、setMaxLength |
| `slider` | [UiSlider](../ui/reference/UiSlider.md) | value，范围由模板决定 |
| `toggle` | [UiToggle](../ui/reference/UiToggle.md) | 布尔类型的 value |
| `scrollView` | [UiScrollView](../ui/reference/UiScrollView.md) | 取值为 0～1 的 progress |

种类必须与模板实际控件相符。控件路径不存在时抛出 [KeyError](../common/type-system.md#keyerror)；视图已关闭或控件已移除时抛出 [InvalidClientObjectError](../common/reference/InvalidClientObjectError.md)。`isValid` 用于检查存活情况，仍需处理检查之后发生的原生失败。

`getControl` 使用绝对路径，`getChild` 使用相对路径。`createControl` 从模板动态创建子控件；移除父控件时，会使已经取得的子孙控件句柄一并失效。

## 状态与事件

`control.bind("text", state)` 是从状态到控件的单向绑定，返回可重复调用的取消函数；视图关闭或控件移除也会释放绑定。原生输入控件不会自动生成反向绑定，需要组合输入和状态时可使用 [主题表单](themed-forms.md)。

`subscribe` 返回取消订阅函数，也可使用同一个回调调用 `unsubscribe`。原生按钮监听按需开启。事件提供 `player`、`view`、`control` 以及可用时的二维触点位置，不公开传输层的玩家或实体编号。

视图提供 ready、update、close 三类生命周期信号。只有需要逐帧逻辑时才订阅 update；常规文字更新使用状态绑定，动画使用原生动画接口。

## 关闭与释放

`view.close()` 删除自己拥有的界面节点，同时释放控件绑定、交互回调和动画。它不依赖当前栈顶是不是这个界面，因此不会弹出后来打开的其他界面。重复关闭没有副作用。

引擎移除视图时也会执行相同清理。`closeReason` 可用于区分主动关闭、用户关闭、创建失败和运行时销毁。原生删除失败时会抛出 [NativeOperationError](../common/reference/NativeOperationError.md)，视图保留有效状态以便重试。

[client.ui.views](../ui/reference/UiService.md#views) 返回本库拥有的视图快照，`currentView` 仅在栈顶属于本库时返回对应视图；其他界面在顶层时返回 [None](../common/type-system.md#none)。`closeAllViews()` 会尝试关闭所有拥有的视图后，再报告首个失败。

`native` 是明确的原生访问入口。通过它自行注册的原生资源不自动成为本库管理的绑定或订阅，使用者需按对应接口清理。