---
title: 主题表单与响应式状态
---

# 主题表单与响应式状态

[Form](../ui/reference/Form.md) 提供组合表单、主题、网格、下拉框、滚动列表和自定义控件。它在两端使用相同的构建方法；客户端默认显示给本地玩家，服务端明确传入 [Player](../server/apis/player.md) 对象。

## 本地表单

```python
# -*- coding: utf-8 -*-
from ModSAPI.client.beta import client

enabled = client.ui.createState(True)
volume = client.ui.createState(50)
name = client.ui.createState(u"玩家")
form = client.ui.createForm(u"设置", {"theme": "fluent-dark"})
form.toggle(u"启用效果", enabled)
form.slider(u"音量", volume, 0, 100, 5)
form.textField(u"显示名称", name)
form.button(u"完成", lambda player: form.close())

def closed(event):
    event.player.sendToast(u"设置界面已关闭")

session = form.show(onClose=closed)
```

优先通过所属端的 [client.ui](../client/apis/manager.md#ui) 或 [system.ui](../server/reference/System.md#ui) 创建表单和状态。也可以从 `ModSAPI.ui` 导入 [Form](../ui/reference/Form.md)、[Observable](../ui/reference/Observable.md) 后直接创建，但这些便捷入口会在创建时根据当前环境选择运行时，初始化早期应使用明确所属端的服务入口。[FormSession](../ui/reference/FormSession.md) 负责本次显示的关闭监听；它不是 [Promise](../common/reference/Promise.md)。关闭表单后可再次显示，彻底结束该功能时调用 `form.dispose()`，并对不再需要的状态调用 `dispose()`。

表单可以在原生界面初始化前准备和请求显示。客户端会等待初始化、服务端控件注册和通信会话，再创建对应界面。创建等待有超时；失败时关闭结果中的 `closeReason` 为 `error`。

## 服务端表单

```python
# -*- coding: utf-8 -*-
from ModSAPI.server.beta import world, system

form = system.ui.createForm(u"欢迎", {"theme": "oreui"})
form.label(u"这里可以继续添加任务、设置和列表。")
form.button(u"确认", lambda player: player.sendMessage(u"欢迎加入"))

def spawned(event):
    if event.initialSpawn:
        form.show(event.player)

world.afterEvents.playerSpawn.subscribe(spawned)
```

`show(player)` 和 `close(player)` 接受玩家对象或玩家对象集合；不接受裸玩家编号。服务端省略 `close` 的目标时关闭当前受众；省略 `show` 的目标不会隐式广播。关闭结果中的 `event.player` 也是包装对象。

同一表单可以同时面向多个玩家；同一个状态对象在这些玩家间共享。玩家各自的设置应创建各自的表单和状态，不能把共享状态误当作个人状态。

## 所属端与生命周期

表单在创建时绑定所属运行时，之后不再通过全局玩家状态重新判端。即使客户端尚未取得本地玩家、或共享解释器的当前环境发生变化，[client.ui.createForm](../ui/reference/UiService.md#createForm) 仍创建客户端表单，[system.ui.createForm](../ui/reference/UiService.md#createForm) 仍创建服务端表单。

| 行为 | 客户端表单 | 服务端表单 |
| --- | --- | --- |
| 显示、追加控件和关闭 | 交给所属客户端运行时 | 通过所属服务端发送给玩家 |
| 目标类型 | [ClientPlayer](../client/reference/ClientPlayer.md)；显示时可以省略 | [Player](../server/apis/player.md)；显示时必须指定 |
| 按钮回调参数 | 本地 [ClientPlayer](../client/reference/ClientPlayer.md) | 激活按钮的 [Player](../server/apis/player.md) |
| 关闭结果中的 player | 本地 [ClientPlayer](../client/reference/ClientPlayer.md) | 关闭表单的 [Player](../server/apis/player.md) |

类型错误会在发送前报告 [TypeError](../common/type-system.md#typeerror)，不会因全局判端变化而接受另一端的玩家对象。表单编号属于内部通信数据：由各运行时独立、固定方向分配，调用者无需管理，也不应将编号当作玩家或表单对象使用。

界面默认配置和样式同步沿用所属运行时；客户端样式更新不会因为环境变化而变成服务端广播。本地控件输入写入客户端状态管理器，服务端关闭会话仍登记玩家离开监听，玩家离开后释放对应监听和受众记录。

运行时销毁后，工厂与编号分配拒绝继续工作并报告 [RuntimeError](../common/type-system.md#runtimeerror)；已有表单在清理时仍沿用自己的传输端，释放显示会话、回调和管理器记录。表单关闭不会自动销毁应用创建的共享状态，应在状态不再被其他界面使用时单独释放。

这些保证已通过运行时切换、目标校验、关闭回调和销毁路径的离线回归；实际界面渲染和多人消息时序仍需游戏内验证。

## 可观察状态

```python
from __future__ import print_function

def connect_state(state):
    stop = state.watch(lambda value: print(value))
    derived = state.map(lambda value: value * 2)
    state.update(lambda value: value + 1)
    stop()
    derived.dispose()
```

`value` 和 `getValue()` 返回副本，赋值或 `update` 才会发布变化。状态值支持有限数字、布尔值、字符串及嵌套列表和字典等普通数据，不接受循环结构或原生对象。

`watch` 默认立即通知当前值，`subscribe` 只监听后续变化。两者都返回取消函数。回调收到新值时，读取源状态仍可取得更新前的旧值；回调中提出的修改按队列继续执行。一个回调失败不会跳过其他订阅者或已经排队的修改，处理后会向调用者报告首个异常。

派生状态与源状态分别释放。关闭某个控件只取消它拥有的绑定，不会替其他界面销毁共享状态。

## 下拉框与滚动列表

```python
def add_choices(form, ui):
    choice = ui.createState("low")
    form.dropdown(u"质量", [
        {"label": u"低", "value": "low"},
        {"label": u"高", "value": "high"},
    ], choice)
    rows = ui.createState([
        {"label": u"任务一", "value": "quest_1"},
        {"label": u"任务二", "value": "quest_2"},
    ])
    selected = ui.createState(None)
    form.listView(u"任务", rows, selected, {"height": 160, "itemHeight": 32})
    return choice, rows, selected
```

下拉选项的 label/value 是静态数据，选中值可以绑定状态。列表支持整体替换行数据和选中值绑定，每行 value 必须唯一。项目变化时会重建相应列表行；当前实现不承诺虚拟列表的性能特性。

服务端验证玩家会话、表单受众、输入控件的可见性以及数值范围、步长和可选项目。隐藏控件、无关状态和文字标题不能通过输入消息修改。

## 主题与网格

内置主题包括 oreui、flutter、flutter-dark、fluent、fluent-dark，完整名称可从 `Theme.names()` 取得。[Theme](../ui/reference/Theme.md) 支持继承、注册、读取副本和注销。默认主题及默认网格影响随后创建的表单。

```python
def create_grid(ui):
    ui.setGrid([1, 2], [1], {"gap": 8, "padding": 12})
    form = ui.createForm(u"双列设置", {"layout": {"columns": [1, 2], "rows": [1], "gap": 8}})
    form.label(u"名称", grid={"column": 0, "row": 0})
    form.button(u"修改", lambda player: None, grid={"column": 1, "row": 0})
    ui.clearGrid()
    return form
```

布局字段详见 [GridLayout](../ui/reference/GridLayout.md)、[GridPosition](../ui/reference/GridPosition.md)、[FormStyle](../ui/reference/FormStyle.md)、[ControlStyle](../ui/reference/ControlStyle.md) 和 [GroupStyle](../ui/reference/GroupStyle.md)。数字表示像素，尺寸表达式支持百分比、轴向百分比和像素偏移；实际布局依赖控件模板。

通过 [OreUIStyles](../ui/reference/OreUIStyles.md)、[FlutterStyles](../ui/reference/FlutterStyles.md)、[FluentStyles](../ui/reference/FluentStyles.md) 或 [InnerStyles](../ui/reference/InnerStyles.md) 取得具体样式标识。文本输入样式统一使用 [TextField](../ui/reference/TextField.md)、DarkTextField 的命名。