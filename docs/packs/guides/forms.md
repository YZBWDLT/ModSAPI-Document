---
title: Action、Modal 与 Message 表单
---

# Action、Modal 与 Message 表单

三种构建器都在服务端使用，最终由本库客户端 JSON [UI](../server_ui/reference/UI.md) 渲染。返回本库 [Promise](../common/reference/Promise.md)，成功响应也可能是用户取消；异步失败走 `catch()`。

[ActionFormData](../server_ui/reference/ActionFormData.md) 用于选择操作，[ModalFormData](../server_ui/reference/ModalFormData.md) 收集输入，[MessageFormData](../server_ui/reference/MessageFormData.md) 处理双按钮确认。它们在 `show(player)` 时指定接收玩家。[CustomForm](../server_ui/reference/CustomForm.md) 和 [MessageBox](../server_ui/reference/MessageBox.md) 在构造时绑定玩家，适合需要主动关闭、重复展示或动态更新的界面。需要定制客户端控件和布局时，使用 [client.screen](../client/apis/manager.md#screen) 注册和打开 JSON 界面。

```python
from __future__ import print_function

from ModSAPI.server.beta import world
from ModSAPI.serverui.beta import ActionFormData

def show_menu(player):
    form = ActionFormData().title("Example").body("Choose an action")
    form.button("Start").button("Help")
    response = form.show(player)
    def complete(result):
        if result.canceled:
            print(result.cancelationReason)
            return
        print(result.selection)
    response.then(complete)
    response.catch(lambda error: print(error))

players = world.getAllPlayers()
if players:
    show_menu(players[0])
```

## 输入表单

```python
from __future__ import print_function

from ModSAPI.serverui.beta import ModalFormData

def show_settings(player):
    form = ModalFormData().title("Settings")
    form.toggle("Enabled", {"defaultValue": True})
    form.slider("Volume", 0, 100, {"valueStep": 5, "defaultValue": 50})
    form.dropdown("Mode", ["Easy", "Hard"], {"defaultValueIndex": 0})
    form.textField("Name", "Input name", {"defaultValue": "Player"})
    response = form.show(player)
    def complete(result):
        if not result.canceled:
            enabled, volume, mode_index, name = result.formValues
            print(enabled, volume, mode_index, name)
    response.then(complete)
    response.catch(lambda error: print(error))
```

滑块上下限和步长必须有限，最小值不大于最大值，步长为正；下拉初始索引从零开始。`header`、`label`、`divider` 等非输入元素在本实现的 `formValues` 对应位置为 [None](../common/type-system.md#none)，不要在混排后仍按纯输入位置解包。

## 双按钮确认

```python
from __future__ import print_function

from ModSAPI.serverui.beta import MessageFormData

def confirm(player):
    form = MessageFormData().title("Confirm").body("Continue?")
    form.button1("Yes").button2("No")
    response = form.show(player)
    response.then(lambda result: print(result.canceled, result.selection))
    response.catch(lambda error: print(error))
```

`selection` 为零起始按钮索引；取消时先检查 `canceled`。支持的 RawMessage 仅限字面 `text/rawtext`；`translate`、`score`、`selector` 和完整微软文本过滤没有实现。`tooltip`、`description`、输入占位符和原生聊天/背包忙碌状态检测仍有缺口，不能仅因参数可传入就认为已经渲染。