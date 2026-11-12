"""Reviewed Chinese guides for managed views and integrated themed forms."""

UI_GUIDES = {
    'packs/guides/managed-ui.md': r'''---
title: 界面、控件与生命周期
---

# 界面、控件与生命周期

界面以视图对象为中心。通过 `client.ui` 声明模板，再打开 `UiView`，从视图取得控件，绑定状态和交互事件，最后关闭视图。该入口与 `client.camera`、`client.audio` 采用相同的对象和选项字典风格。

| 需要完成的操作 | 使用入口 | 结果 |
| --- | --- | --- |
| 打开自己的界面模板 | `client.ui.openView(...)` | 管理界面栈中的 UiView |
| 创建常驻或跟随实体的界面 | `client.ui.createHud(...)` | 不加入界面栈的 UiView |
| 在本地组合表单 | `client.ui.createForm(...)` | Form，省略目标即可显示给本地玩家 |
| 从服务端向玩家显示表单 | `system.ui.createForm(...)` | Form，显示时传入 Player 对象 |
| 使用标准表单构建器 | `ActionFormData`、`ModalFormData`、`MessageFormData` | 具有标准返回结果的表单 |

公共类型位于 `ModSAPI.ui`。`UiService` 由现有客户端和服务端系统提供，使用时无需再注册系统。

## 创建时机

`registerView` 可以在客户端入口加载时声明模板，首次打开时才注册原生界面。打开界面需要等待 `client.afterEvents.uiReady`。`openView` 返回时，原生控件可能尚未创建，因此将初始化操作放在注册选项的 `onReady` 回调中。

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

若在就绪事件触发之后才执行打开逻辑，可以检查 `client.ui.isReady`。业务数据从 `view.data` 读取，每次返回独立副本；改变该副本不会修改视图或引擎状态。

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
| `control` | UiControl | visible、position、size、setLayout、bind、remove |
| `label` | UiLabel | text、color、setFontScale |
| `button` | UiButton | afterEvents.click、指针和悬浮事件 |
| `image` | UiImage | setImage、setClipRatio |
| `textField` | UiTextField | value、setMaxLength |
| `slider` | UiSlider | value，范围由模板决定 |
| `toggle` | UiToggle | 布尔类型的 value |
| `scrollView` | UiScrollView | 取值为 0～1 的 progress |

种类必须与模板实际控件相符。控件路径不存在时抛出 KeyError；视图已关闭或控件已移除时抛出 InvalidClientObjectError。`isValid` 用于检查存活情况，仍需处理检查之后发生的原生失败。

`getControl` 使用绝对路径，`getChild` 使用相对路径。`createControl` 从模板动态创建子控件；移除父控件时，会使已经取得的子孙控件句柄一并失效。

## 状态与事件

`control.bind("text", state)` 是从状态到控件的单向绑定，返回可重复调用的取消函数；视图关闭或控件移除也会释放绑定。原生输入控件不会自动生成反向绑定，需要组合输入和状态时可使用 [主题表单](themed-forms.md)。

`subscribe` 返回取消订阅函数，也可使用同一个回调调用 `unsubscribe`。原生按钮监听按需开启。事件提供 `player`、`view`、`control` 以及可用时的二维触点位置，不公开传输层的玩家或实体编号。

视图提供 ready、update、close 三类生命周期信号。只有需要逐帧逻辑时才订阅 update；常规文字更新使用状态绑定，动画使用原生动画接口。

## 关闭与释放

`view.close()` 删除自己拥有的界面节点，同时释放控件绑定、交互回调和动画。它不依赖当前栈顶是不是这个界面，因此不会弹出后来打开的其他界面。重复关闭没有副作用。

引擎移除视图时也会执行相同清理。`closeReason` 可用于区分主动关闭、用户关闭、创建失败和运行时销毁。原生删除失败时会抛出 NativeOperationError，视图保留有效状态以便重试。

`client.ui.views` 返回本库拥有的视图快照，`currentView` 仅在栈顶属于本库时返回对应视图；其他界面在顶层时返回 None。`closeAllViews()` 会尝试关闭所有拥有的视图后，再报告首个失败。

`native` 是明确的原生访问入口。通过它自行注册的原生资源不自动成为本库管理的绑定或订阅，使用者需按对应接口清理。
''',
    'packs/guides/themed-forms.md': r'''---
title: 主题表单与响应式状态
---

# 主题表单与响应式状态

Form 提供组合表单、主题、网格、下拉框、滚动列表和自定义控件。它在两端使用相同的构建方法；客户端默认显示给本地玩家，服务端明确传入 Player 对象。

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

也可以从 `ModSAPI.ui` 导入 Form、Observable 后直接创建。FormSession 负责本次显示的关闭监听；它不是 Promise。关闭表单后可再次显示，彻底结束该功能时调用 `form.dispose()`，并对不再需要的状态调用 `dispose()`。

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

## 可观察状态

```python
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

内置主题包括 oreui、flutter、flutter-dark、fluent、fluent-dark，完整名称可从 `Theme.names()` 取得。Theme 支持继承、注册、读取副本和注销。默认主题及默认网格影响随后创建的表单。

```python
def create_grid(ui):
    ui.setGrid([1, 2], [1], {"gap": 8, "padding": 12})
    form = ui.createForm(u"双列设置", {"layout": {"columns": [1, 2], "rows": [1], "gap": 8}})
    form.label(u"名称", grid={"column": 0, "row": 0})
    form.button(u"修改", lambda player: None, grid={"column": 1, "row": 0})
    ui.clearGrid()
    return form
```

布局字段详见 GridLayout、GridPosition、FormStyle、ControlStyle 和 GroupStyle。数字表示像素，尺寸表达式支持百分比、轴向百分比和像素偏移；实际布局依赖控件模板。

通过 OreUIStyles、FlutterStyles、FluentStyles 或 InnerStyles 取得具体样式标识。文本输入样式统一使用 TextField、DarkTextField 的命名。
''',
    'packs/guides/ui-animation-and-hud.md': r'''---
title: 界面动画与跟随界面
---

# 界面动画与跟随界面

## 原生属性动画

`UiControl.animate` 创建 UiAnimation，动画由引擎推进。可用属性包括 opacity、position、size，以及图片控件的 clipRatio。

```python
def fade_in(view):
    image = view.getControl("/image", "image")
    animation = image.animate("opacity", 1, {"from": 0, "duration": 0.3})
    animation.afterEvents.complete.subscribe(lambda event: print(event.animation.state))
    return animation
```

duration 以秒计，不是游戏刻。opacity 和 clipRatio 的范围为 0～1；原生接口没有这两个属性的可靠读取入口，因此必须明确提供 from。位置和尺寸在省略 from 时读取当前值。

```python
def control_animation(animation):
    animation.pause()
    animation.play()
    animation.cancel()
```

同一个控件同一属性的新动画会取消它先前拥有的动画。完成后会写入目标值，释放动画通道、结束回调和临时注册；视图关闭时也会释放。cancel 释放本次动画，不停止其他属性上的动画，也不承诺恢复初始值。

启动失败会抛出 NativeOperationError 并尝试清理已经取得的资源。异步结束时的失败由 `animation.afterEvents.error` 或创建选项 onError 接收，`animation.error` 保留异常。

## 常驻界面

先用 `registerView` 声明模板，再在原生界面就绪后创建：

```python
def create_status(client):
    client.ui.registerView("demo:status", "demo_ui.status")
    return client.ui.createHud("demo:status")
```

HUD 不加入本库管理的界面栈。它仍使用 UiView，可以取得控件、绑定状态和关闭。一个注册标识同一时刻只能有一个存活的 HUD；重复创建前应关闭旧实例。

## 跟随实体

```python
def create_nameplate(client):
    client.ui.registerView("demo:nameplate", "demo_ui.nameplate")
    return client.ui.createHud("demo:nameplate", {
        "entity": client.localPlayer,
        "offset": (0, 2, 0),
        "autoScale": True,
    })
```

entity 使用 ClientEntity 或 ClientPlayer，不传实体编号。绑定对象必须有效，并属于当前客户端会话。offset 表示相对实体的三维偏移，autoScale 决定是否按距离缩放。

## 固定世界位置

```python
def create_world_label(client):
    client.ui.registerView("demo:world_label", "demo_ui.world_label")
    return client.ui.createHud("demo:world_label", {
        "location": (10, 70, 10),
        "dimension": client.localPlayer.dimension,
        "autoScale": True,
    })
```

dimension 使用 ClientDimension，省略时取本地玩家当前显示的维度；切换维度期间原生结果不可用时会明确报错。location 与 entity 互斥，实体偏移不用于固定世界位置。缩放表现及可见距离仍取决于原生界面模板和游戏渲染规则。
''',
    'packs/guides/ui-custom-controls.md': r'''---
title: 自定义控件与组合模板
---

# 自定义控件与组合模板

Control.register 使用一个统一入口，把 JSON 模板与具有明确字段的描述对象关联。Button、Toggle、Slider、TextField、Dropdown、ListView、Label、Divider、ScrollingPanel、Custom 和 Group 都使用这一入口。

```python
from ModSAPI.ui import Control, TextField

Control.register("demo:search", "demo_ui.search", TextField(
    textFieldPath="/input",
    labelPaths=["/caption"],
))
```

随后构建表单时，通过样式中的 class 字段选择模板：

```python
def add_search(form, state):
    form.textField(u"查找", state, {"class": "demo:search"})
    return form
```

描述对象会被复制，非法描述、错误路径类型和错误回调会在登记前报错。注册名使用 namespace:name，模板路径使用 namespace.control。

## 创建和状态更新回调

onCreate 和 onObservableUpdate 在客户端执行，服务端不能把 Python 函数发送给客户端。服务端可以登记没有本地回调的纯数据模板。

```python
from ModSAPI.ui import Control, Custom

def created(args):
    print(args.params.get("caption"))

def updated(args):
    print(args.key, args.oldValue, args.newValue)

Control.register("demo:custom", "demo_ui.custom", Custom(
    onCreate=created,
    onObservableUpdate=updated,
))

def add_custom(form, caption):
    return form.custom({"caption": caption}, {"class": "demo:custom"})
```

CreateArguments 提供布局完成后的样式和参数快照。ObservableUpdateArguments 提供顶层参数名、新旧值和当前参数快照。嵌套状态已解包，不需要在回调里继续识别传输编号。

这些高级回调同时提供原生控件和屏幕，供封装尚未覆盖的控件特性使用。它们属于明确的原生扩展边界；常规界面应使用 UiView、UiControl 和状态绑定。

## 控件组

Group 定义具名子控件的类型和布局，表单 group 方法提供每次实例自己的数据和回调。

```python
from ModSAPI.ui import Control, Group, OreUIStyles

Control.register("demo:row", "demo_ui.row", Group({
    "caption": {"class": OreUIStyles.Label, "width": "50%", "height": 24},
    "button": {"class": OreUIStyles.NormalBtn, "width": "50%", "height": 24, "offsetX": "50%"},
}))

def add_row(form):
    return form.group({
        "caption": {"label": u"任务状态"},
        "button": {"label": u"查看", "callbacks": lambda player: player.sendToast(u"已选择")},
    }, {"class": "demo:row", "height": 24})
```

以上例子在客户端使用；服务端回调接收 Player，应调用该对象支持的服务端接口。子控件 class 必填，组内百分比相对父组计算。嵌套组通过 children 传递数据，具体字段见 GroupDefinitions、GroupChildren 和 GroupChildData。

列表、自定义控件和控件组仍需对应资源包模板。缺失模板、错误控件路径及真实布局不能仅靠声明确认，应在目标游戏版本中验证。
''',
}

UI_ACQUIRE = {
    'UiService': '通过 client.ui 或 system.ui 获取。原生视图方法只在客户端可用。',
    'UiViewDefinition': '由 client.ui.registerView 返回，无需自行构造。',
    'UiView': '由 client.ui.openView 或 client.ui.createHud 返回。',
    'UiControl': '由 UiView.getControl、UiView.createControl 或 UiControl.getChild 返回。',
    'UiLabel': '使用 view.getControl(path, "label")。',
    'UiButton': '使用 view.getControl(path, "button")。',
    'UiImage': '使用 view.getControl(path, "image")。',
    'UiTextField': '使用 view.getControl(path, "textField")。',
    'UiSlider': '使用 view.getControl(path, "slider")。',
    'UiToggle': '使用 view.getControl(path, "toggle")。',
    'UiScrollView': '使用 view.getControl(path, "scrollView")。',
    'UiAnimation': '由 UiControl.animate 返回；使用 pause、play、cancel 和 dispose 管理。',
    'UiEvent': '从视图生命周期或按钮交互的订阅回调取得。',
    'UiEventSignal': '通过拥有它的 afterEvents 容器获取。subscribe 返回取消函数。',
    'UiViewEvents': '使用 view.afterEvents。',
    'UiButtonEvents': '使用 button.afterEvents。',
    'UiAnimationEvent': '通过动画完成或失败的回调取得。',
    'UiAnimationEvents': '使用 animation.afterEvents。',
    'Form': '从 ModSAPI.ui 导入 Form，或使用 client.ui.createForm / system.ui.createForm。',
    'FormSession': '由 Form.show 返回，使用 onClose 设置关闭回调。',
    'FormCloseEvent': '通过 Form.show 的关闭回调取得，player 为当前端的玩家包装对象。',
    'Observable': '从 ModSAPI.ui 导入，或使用 client.ui.createState / system.ui.createState。',
    'Control': '从 ModSAPI.ui 导入，通过静态方法 register 登记模板描述。',
    'Theme': '从 ModSAPI.ui 导入，使用静态方法管理主题。',
    'ControlDescriptor': '从 ModSAPI.ui 导入具体描述类型，传给 Control.register。',
    'CreateArguments': '通过客户端自定义控件的 onCreate 回调取得。',
    'ObservableUpdateArguments': '通过客户端自定义控件的 onObservableUpdate 回调取得。',
    'UiAnimationOptions': '使用普通选项字典传给 UiControl.animate；各字段是否需要提供取决于动画属性。',
    'UiViewOptions': '使用普通字典传给 client.ui.openView。',
    'UiHudOptions': '使用普通字典传给 client.ui.createHud。',
    'UiViewCallbacks': '使用普通字典传给 client.ui.registerView，回调接收 UiEvent。',
}

UI_EXAMPLES = {
    'UiService': 'from ModSAPI.client.beta import client\n\ndef has_ui():\n    return client.ui.isReady',
    'UiView': 'def close_view(view):\n    if view.isValid:\n        view.close()',
    'UiControl': 'def resize(control):\n    control.setLayout({"width": "100%-16px", "height": 32})',
    'UiLabel': 'def set_title(label):\n    label.text = u"欢迎"\n    label.color = (1, 1, 1)',
    'UiButton': 'def connect(button):\n    return button.afterEvents.click.subscribe(lambda event: event.view.close())',
    'UiImage': 'def set_icon(image):\n    image.setImage("textures/items/diamond")',
    'UiTextField': 'def clear_input(field):\n    field.value = ""\n    field.setMaxLength(32)',
    'UiSlider': 'def read_slider(slider):\n    return slider.value',
    'UiToggle': 'def enable(toggle):\n    toggle.value = True',
    'UiScrollView': 'def scroll_to_top(scroll):\n    scroll.progress = 0',
    'UiAnimation': 'def stop_animation(animation):\n    animation.cancel()',
    'Form': 'from ModSAPI.client.beta import client\n\ndef create_form():\n    form = client.ui.createForm(u"设置", {"theme": "fluent"})\n    form.button(u"关闭", lambda player: form.close())\n    return form',
    'Observable': 'from ModSAPI.client.beta import client\n\nstate = client.ui.createState(0)\nstop = state.watch(lambda value: print(value))\nstate.update(lambda value: value + 1)\nstop()\nstate.dispose()',
    'Control': 'from ModSAPI.ui import Control, TextField\n\nControl.register("demo:input", "demo_ui.input", TextField(textFieldPath="/input"))',
}

UI_GUIDES['packs/guides/custom-screen.md'] = '''---
title: 界面流程与原生扩展
---

# 界面流程与原生扩展

使用 client.ui 声明和打开视图，通过 UiView 获取控件、绑定状态并处理交互。主题组合表单同时支持客户端与服务端。

- [完整视图流程与模板示例](managed-ui.md)
- [主题表单与响应式状态](themed-forms.md)
- [动画、常驻和跟随界面](ui-animation-and-hud.md)
- [自定义模板与控件组](ui-custom-controls.md)

已有的 client.screen 提供直接管理原生 ScreenNode 的兼容入口；通过它创建的节点由调用者管理。需要本库统一释放控件、订阅和动画时，使用 client.ui 管理视图。
'''
