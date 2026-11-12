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
| `label` | UiLabel | text、color、textAlignment、lineSpacing、textShadow |
| `button` | UiButton | afterEvents.click、指针和悬浮事件 |
| `image` | UiImage | setImage、setClipRatio、clipDirection、rotate |
| `textField` | UiTextField | value、setMaxLength |
| `slider` | UiSlider | value，范围由模板决定 |
| `toggle` | UiToggle | 布尔类型的 value |
| `scrollView` | UiScrollView | progress、scrollOffset、content |
| `grid` | UiGrid | setDimensions、getItem |
| `stackPanel` | UiStackPanel | orientation |
| `inputPanel` | UiInputPanel | isModal、swallowInput、dragOffset |
| `progressBar` | UiProgressBar | 取值为 0～1 的 setProgress |
| `itemRenderer` | UiItemRenderer | setItem、item |
| `comboBox` | UiComboBox | addOption、selectedIndex、afterEvents |
| `selectionWheel` | UiSelectionWheel | sliceCount、selectedIndex、afterEvents |
| `miniMap` | UiMiniMap | addMarker、addTextMarker、zoomIn、zoomOut |
| `modelRenderer` | UiModelRenderer | setEntity、setSkeletonModel、setBlockGeometry |

锚点、裁剪、网格与物品预览的配套模板见 [布局与常用控件](ui-layout-and-widgets.md)。UiAnchor 和 UiImageClipDirection 提供可直接导入的常量，减少手写原生字符串。

原生下拉框、选择轮盘与小地图见 [选择控件与小地图](ui-choices-and-minimap.md)。小地图视图在 registerView 中传入 miniMap=True，库会保留原生地图基类的初始化和更新逻辑。

实体与模型预览、图片九宫格见 [模型预览与图片适配](ui-models-and-images.md)。模型预览由当前视图管理，无需额外登记系统。

原版状态条、触控按钮、原生界面请求和布局区域读取见 [原生抬头显示与原版界面](ui-native-hud-and-screens.md)。这些入口也通过 client.ui 获取，实际能力由原生平台决定。

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

清理失败后可再次调用 `animation.dispose()`，只重试尚未成功释放的部分。启动失败且回滚也失败时，异常的 animation 属性保留对应 UiAnimation，cleanupErrors 列出回滚错误。`view.close()` 和 `client.ui.closeAllViews()` 也会重试自己拥有的残留动画注册；界面已经关闭时仍可重试这些清理。

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
    'UiGrid': '使用 view.getControl(path, "grid")，格子由资源包模板创建。',
    'UiStackPanel': '使用 view.getControl(path, "stackPanel")。',
    'UiInputPanel': '使用 view.getControl(path, "inputPanel")。',
    'UiProgressBar': '使用 view.getControl(path, "progressBar")，模板内需要填充图片子控件。',
    'UiItemRenderer': '使用 view.getControl(path, "itemRenderer")，或从 UiGrid.getItem 取得。',
    'UiItem': '从 ModSAPI.ui 导入并构造，或通过 UiItemRenderer.item 读取。',
    'UiItemOptions': '将普通字典传给 UiItem 或 UiItemRenderer.setItem 的字符串重载。',
    'UiAnchor': '从 ModSAPI.ui 导入，作为锚点属性和 setAnchors 的参数。',
    'UiImageClipDirection': '从 ModSAPI.ui 导入，赋给 UiImage.clipDirection。',
    'UiComboBox': '使用 view.getControl(path, "comboBox")；模板继承原生 combo_box.comboBoxPanel。',
    'UiSelectionWheel': '使用 view.getControl(path, "selectionWheel")；扇区由模板决定。',
    'UiMiniMap': '先以 miniMap=True 注册视图，再使用 view.getControl(path, "miniMap")。',
    'UiMapMarker': '由 UiMiniMap.addMarker 或 addTextMarker 返回；使用 remove 移除。',
    'UiChoiceEvent': '从下拉框的 selectionChange 或轮盘的选择回调取得。',
    'UiComboBoxEvents': '使用 UiComboBox.afterEvents。',
    'UiSelectionWheelEvents': '使用 UiSelectionWheel.afterEvents。',
    'UiComboBoxOption': '使用包含可选 icon 字段的字典传给 UiComboBox.addOption。',
    'UiMapMarkerOptions': '将尺寸和实体旋转选项传给 UiMiniMap.addMarker。',
    'UiMapTextMarkerOptions': '将文字缩放选项传给 UiMiniMap.addTextMarker。',
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
    'UiGrid': 'def fill_grid(grid):\n    grid.setDimensions(2, 1)\n    cell = grid.getItem(0, 0, "itemRenderer")\n    if cell is not None:\n        cell.setItem("minecraft:diamond")',
    'UiStackPanel': 'def arrange(stack):\n    stack.orientation = "vertical"',
    'UiInputPanel': 'def modal(panel):\n    panel.isModal = True\n    panel.swallowInput = True\n    panel.dragOffset = (0, 0)',
    'UiProgressBar': 'def update_progress(progress):\n    progress.setProgress(0.65)',
    'UiItemRenderer': 'def show_item(renderer):\n    renderer.setItem("minecraft:diamond", {"isEnchanted": True})',
    'UiItem': 'from ModSAPI.ui import UiItem\n\npreview = UiItem("minecraft:diamond", {"isEnchanted": True})',
    'UiAnchor': 'from ModSAPI.ui import UiAnchor\n\ndef align(control):\n    control.setAnchors(UiAnchor.TopLeft)',
    'UiImageClipDirection': 'from ModSAPI.ui import UiImageClipDirection\n\ndef configure(image):\n    image.clipDirection = UiImageClipDirection.LeftToRight',
    'UiComboBox': 'def configure(combo):\n    combo.addOption(u"低", "low").addOption(u"高", "high")\n    combo.selectedIndex = 0\n    return combo.afterEvents.selectionChange.subscribe(lambda event: print(event.value))',
    'UiSelectionWheel': 'def select_first(wheel):\n    if wheel.sliceCount:\n        wheel.selectedIndex = 0\n    return wheel.afterEvents.select.subscribe(lambda event: print(event.index))',
    'UiMiniMap': 'def mark_location(mini_map):\n    marker = mini_map.addTextMarker((10, 70, 20), u"目标")\n    mini_map.zoomIn(0.1)\n    return marker',
    'UiMapMarker': 'def remove_marker(marker):\n    marker.remove()\n    marker.remove()',
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
- [布局、网格与物品预览](ui-layout-and-widgets.md)
- [原生下拉框、轮盘与小地图](ui-choices-and-minimap.md)
- [自定义模板与控件组](ui-custom-controls.md)

已有的 client.screen 提供直接管理原生 ScreenNode 的兼容入口；通过它创建的节点由调用者管理。需要本库统一释放控件、订阅和动画时，使用 client.ui 管理视图。
'''

UI_GUIDES['packs/guides/ui-layout-and-widgets.md'] = r'''---
title: 布局与常用控件
---

# 布局与常用控件

UiView 负责界面生命周期，UiControl 提供位置、尺寸、锚点、裁剪与状态绑定。需要专用能力时，通过 getControl 的种类参数取得 UiGrid、UiStackPanel、UiItemRenderer 等类型。控件种类必须与资源包模板一致。

## 锚点与尺寸

```python
from ModSAPI.ui import UiAnchor

def arrange(view):
    panel = view.getControl("/panel")
    panel.setAnchors(UiAnchor.TopLeft)
    panel.position = (12, 12)
    panel.setLayout({"width": "100%-24px", "height": 180})
    panel.minimumSize = (120, 80)
    panel.clipsChildren = True
    panel.clipOffset = (0, 0)
```

setAnchors 同时设置父参照点和控件参照点；第二个参数省略时，两者使用相同锚点。若第二步失败，库会尝试恢复原来的两个值，恢复失败附在异常的 rollbackErrors 中。maximumSize 的 `(0, 0)` 沿用原生的无限制语义。

position、size、globalPosition 和 clipOffset 使用界面像素；globalPosition 为只读。布局表达式通过 setLayout 设置。不要把界面像素与世界坐标混用。

## 可直接配套的模板

将以下内容保存为资源包的 `ui/demo_widgets.json`：

```json
{
  "namespace": "demo_widgets",
  "screen": {
    "type": "screen",
    "is_showing_menu": true,
    "controls": [{"panel": {
      "type": "input_panel",
      "size": [240, 200],
      "modal": true,
      "is_swallow": true,
      "draggable": "both",
      "button_mappings": [{
        "from_button_id": "button.menu_select",
        "to_button_id": "#netease_to_button_id",
        "mapping_type": "pressed"
      }],
      "controls": [
        {"headings": {
          "type": "stack_panel",
          "orientation": "vertical",
          "size": [200, 40],
          "offset": [0, -70],
          "controls": [
            {"title": {"type": "label", "text": "物品预览", "size": [200, 20]}},
            {"hint": {"type": "label", "text": "可拖动面板", "size": [200, 20]}}
          ]
        }},
        {"preview": {
          "type": "custom",
          "renderer": "inventory_item_renderer",
          "property_bag": {"#item_id_aux": 0},
          "size": [48, 48],
          "offset": [-72, -8]
        }},
        {"items": {
          "type": "grid",
          "collection_name": "demo_items",
          "grid_dimensions": [2, 1],
          "grid_item_template": "demo_widgets.item_cell",
          "grid_rescaling_type": "none",
          "size": [96, 48],
          "offset": [28, -8]
        }},
        {"progress": {
          "type": "panel",
          "size": [180, 10],
          "offset": [0, 54],
          "controls": [
            {"empty_progress_bar": {
              "type": "image",
              "texture": "textures/ui/empty_progress_bar",
              "size": ["100%", "100%"],
              "layer": 1
            }},
            {"filled_progress_bar": {
              "type": "image",
              "texture": "textures/ui/filled_progress_bar",
              "size": ["100%", "100%"],
              "clip_direction": "left",
              "clip_ratio": 1,
              "layer": 2
            }}
          ]
        }}
      ]
    }}]
  },
  "item_cell": {
    "type": "custom",
    "renderer": "inventory_item_renderer",
    "property_bag": {"#item_id_aux": 0},
    "size": [48, 48]
  }
}
```

在资源包的 `ui/_ui_defs.json` 中追加文件路径，保留原有条目：

```json
{"ui_defs": ["ui/demo_widgets.json"]}
```

这里的物品数值仅用于空白占位，实际预览通过 setItem 传入名称，避免依赖随游戏和模组变化的数字物品编号。模板结构仍需在目标网易游戏版本中验证；离线测试只校验调用契约。

## 初始化与网格刷新

```python
# -*- coding: utf-8 -*-
from ModSAPI.client.beta import client
from ModSAPI.ui import UiItem

def ready(event):
    view = event.view
    view.getControl("/panel/preview", "itemRenderer").setItem(
        UiItem("minecraft:diamond", {"isEnchanted": True}))
    view.getControl("/panel/progress", "progressBar").setProgress(0.65)
    view.getControl("/panel/headings", "stackPanel").orientation = "vertical"

    def refresh_cells():
        if not view.isReady:
            return
        grid = view.getControl("/panel/items", "grid")
        for column, type_id in enumerate(("minecraft:apple", "minecraft:diamond")):
            cell = grid.getItem(column, 0, "itemRenderer")
            if cell is not None:
                cell.setItem(type_id)

    client.run(refresh_cells)
    grid_path = "/panel/items"

    def grid_changed(changed):
        if changed.path == grid_path:
            refresh_cells()

    signal = client.afterEvents.gridComponentSizeChange
    signal.subscribe(grid_changed)
    view.afterEvents.close.subscribe(lambda closed: signal.unsubscribe(grid_changed))

client.ui.registerView("demo:widgets", "demo_widgets.screen", {"onReady": ready})

def open_widgets(event):
    client.ui.openView("demo:widgets")

client.afterEvents.uiReady.subscribe(open_widgets)
```

网格的格子在渲染阶段创建，onReady 中可能还不存在；getItem 此时返回 None。示例将首次填充安排到下一次客户端调度，未创建的格子留给后续渲染更新。改变 setDimensions、滚动回收或重新布局后，应重新调用 getItem 取得当前格子，不要长期保存格子路径与序号的对应关系。

滚动网格还应监听 `client.afterEvents.gridComponentSizeChange`，按当前数据重新取得并填充格子；该原生事件仅提供 path，不提供本库视图身份，多个视图有同名路径时需要结合自己的打开状态筛选。订阅应在视图关闭时取消。高频刷新只更新变化的项目，避免每帧重建整个网格。

UiItem 表示渲染快照，设置预览不会修改背包。setItem 接受物品名称、UiItem 或 EventItemStack。读取 item 只能得到原生返回的名称、附加值和附魔显示标记；原生读取接口不返回 userData，因此无法从已有预览恢复这部分数据。

## 文字、图片与滚动区域

```python
from ModSAPI.ui import UiImageClipDirection

def decorate(view):
    label = view.getControl("/panel/headings/title", "label")
    label.textAlignment = "center"
    label.lineSpacing = 2
    label.textShadow = True
    progress = view.getControl("/panel/progress/filled_progress_bar", "image")
    progress.clipDirection = UiImageClipDirection.LeftToRight
    progress.setClipRatio(0.35)
```

图片支持 rotationPivot、rotate 和 rotateAround；旋转角度使用度数，具体变换沿用原生语义。rotation、orbitPoint 和 orbitRotation 可读取当前结果。progressBar 的 setProgress 使用完成比例，而 image 的 setClipRatio 使用裁剪比例，两者含义不同。

UiScrollView.progress 使用 0～1 的滚动比例，scrollOffset 使用原生滚动像素。content 每次查询当前内容控件，适应触控与键鼠模板路径切换。不要自行拼接固定的内容子路径。

UiInputPanel 的 isModal 限制界面输入范围，swallowInput 控制输入是否穿透到世界。dragOffset 是原生累计拖动位移，与 position 分别存储；JSON 中还需配置 draggable 和 button_mappings 才能接收拖动。

## 错误与释放

错误参数在调用原生接口前抛出 TypeError 或 ValueError；控件种类与模板不符时抛出 UnsupportedFeatureError；失效视图和控件抛出 InvalidClientObjectError。原生布尔失败、异常及不符合契约的读取结果会报告 NativeOperationError，并保留 operation 等诊断信息。

focus 与 blur 使用引擎的选中控件入口，实际键盘输入能力取决于控件种类。动态创建后若包装失败，库会尝试移除已创建的原生节点；清理失败记录在异常的 cleanupErrors 中。使用完毕后调用 view.close，绑定、按钮订阅和动画由视图释放。
'''

UI_GUIDES['packs/guides/ui-choices-and-minimap.md'] = r'''---
title: 选择控件与小地图
---

# 选择控件与小地图

UiComboBox、UiSelectionWheel 与 UiMiniMap 使用原生控件模板，并接入 UiView 的生命周期。它们适合已有资源包界面；只需要组合设置表单时，也可以直接使用 Form.dropdown。

以下模板分别保存到资源包的 `ui` 目录，并将路径追加到 `ui/_ui_defs.json` 的 ui_defs 列表中。三个场景独立使用。原生模板名与真实渲染表现仍需在目标网易游戏版本中验证。

## 原生下拉框

将以下内容保存为 `ui/demo_combo.json`：

```json
{
  "namespace": "demo_combo",
  "screen": {
    "type": "screen",
    "is_showing_menu": true,
    "controls": [{"menu@combo_box.comboBoxPanel": {
      "size": [160, 24],
      "$content_size": [160, 96],
      "$item_size": ["100%", 24]
    }}]
  }
}
```

```python
# -*- coding: utf-8 -*-
from ModSAPI.client.beta import client

def ready(event):
    menu = event.view.getControl("/menu", "comboBox")
    menu.addOption(u"低", {"quality": "low"})
    menu.addOption(u"高", {"quality": "high"}, {"icon": "textures/items/diamond"})
    menu.selectedIndex = 0

    def selected(choice):
        if choice.index is not None:
            choice.player.sendToast(choice.label)
            print(choice.value)

    menu.afterEvents.selectionChange.subscribe(selected)

client.ui.registerView("demo:combo", "demo_combo.screen", {"onReady": ready})
client.afterEvents.uiReady.subscribe(lambda event: client.ui.openView("demo:combo"))
```

selectedIndex 使用零起始索引，没有选中时为 None；赋值 None 会清除选择。findOption 按显示文字查询，未找到时也返回 None。selectLabel 按文字选中，removeOption 接受索引或显示文字，clearOptions 清空所有内容。

addOption 会复制普通数据；事件中的 UiChoiceEvent.value 每次读取也返回副本。原生读取接口不提供已有选项自定义值的读取能力，因此库只提供 selectedIndex、selectedLabel 和 getOptionLabel，不虚构可恢复全部选项数据的属性。

afterEvents.open 与 close 表示下拉菜单展开和收起，不是整个视图的打开和关闭。selectionChange 对应原生选项通知，提供 index、label、value，以及继承的 player、view 和 control 对象。

## 选择轮盘

将以下内容保存为 `ui/demo_wheel.json`。示例使用文字显示状态，正式界面的圆环和图标可自行替换；响应区域仍由轮盘的半径和尺寸决定。

```json
{
  "namespace": "demo_wheel",
  "content": {
    "type": "panel",
    "controls": [
      {"idle": {"type": "label", "text": "请选择"}},
      {"first": {"type": "label", "text": "选项一"}},
      {"second": {"type": "label", "text": "选项二"}},
      {"third": {"type": "label", "text": "选项三"}}
    ]
  },
  "screen": {
    "type": "screen",
    "is_showing_menu": true,
    "gamepad_cursor_deflection_mode": true,
    "controls": [{"wheel@common_selection_wheels.base_selection_wheel": {
      "size": [200, 200],
      "inner_radius": 0.35,
      "outer_radius": 1,
      "slice_count": 3,
      "initial_button_slice": -1,
      "$content": "demo_wheel.content",
      "state_controls": ["idle", "first", "second", "third"]
    }}]
  }
}
```

```python
# -*- coding: utf-8 -*-
from ModSAPI.client.beta import client

def ready(event):
    wheel = event.view.getControl("/wheel", "selectionWheel")

    def chosen(choice):
        if choice.index is not None:
            choice.player.sendToast(u"选择：%s" % choice.index)
            choice.view.close()

    wheel.afterEvents.select.subscribe(chosen)

client.ui.registerView("demo:wheel", "demo_wheel.screen", {"onReady": ready})
client.afterEvents.uiReady.subscribe(lambda event: client.ui.openView("demo:wheel"))
```

sliceCount 来自模板，selectedIndex 没有选中时为 None。selectionChange 读取原生悬浮通知中的当前索引，仅在观察到索引变化时通知，过滤重复的进入和离开通知；select 表示指针按下并抬起，允许 index 为 None。UiChoiceEvent 的 label 和 value 在轮盘中为 None。

轮盘通过 openView 加入界面栈，可沿用原生栈界面的贴图预加载行为；创建常驻轮盘时应另外处理首次加载贴图的表现。

## 小地图与标记

将以下内容保存为 `ui/demo_map.json`：

```json
{
  "namespace": "demo_map",
  "screen": {
    "type": "screen",
    "controls": [{"mainPanel@mini_map.mini_map_wrapper": {
      "anchor_from": "top_right",
      "anchor_to": "top_right",
      "size": [140, 140],
      "offset": [-12, 12],
      "$enable_live_update": false,
      "$live_update_interval": 5,
      "$use_default_face_icon": true
    }}]
  }
}
```

```python
# -*- coding: utf-8 -*-
from ModSAPI.client.beta import client

def ready(event):
    mini_map = event.view.getControl("/mainPanel/netease_mini_map", "miniMap")
    mini_map.addMarker(client.localPlayer, "textures/items/diamond", {"rotate": True})
    destination = mini_map.addTextMarker((10, 70, 20), u"目标", {"scale": 0.8})
    mini_map.zoomIn(0.1)
    # 目标完成时可调用 destination.remove()

client.ui.registerView("demo:map", "demo_map.screen", {"onReady": ready, "miniMap": True})
client.afterEvents.uiReady.subscribe(lambda event: client.ui.createHud("demo:map"))
```

miniMap=True 使库使用网易的小地图界面基类，并调用该基类的创建、更新和销毁方法。它是注册选项，不需要自行继承或登记第二套系统；没有该原生能力的 SDK 会明确报错。

addMarker 和 addTextMarker 接受三维位置或客户端实体对象，返回 UiMapMarker。固定位置只把 X/Z 交给地图；Y 保留在 location 的输入副本中。实体标记的 entity 是包装对象，固定标记的 entity 为 None。相同实体的图片与文字可同时存在，同一种标记重复添加会报错，以免旧句柄误删新标记。

marker.remove 只移除当前标记，成功后重复调用无副作用。clearMarkers 会尝试所有标记，保留失败句柄，并在异常的 cleanupErrors 中列出错误；随后可以重试。关闭视图或移除地图控件也会使相关句柄失效。

setHeightLimit 默认重绘已有区块；多次调整时可传 repaint=False，最后只调用一次 refresh。zoomIn 和 zoomOut 接受非负增量，resetZoom 恢复默认缩放。小地图不会因此加载远处区块，过度缩小可能影响标记显示；不要每帧重绘整个地图。

## 回调与释放约定

业务回调始终接收包装事件。库负责将下拉框和轮盘的原生通知绑定到界面节点，再分发到对应控件；同一视图中的多个控件互不覆盖。subscribe 返回取消函数，关闭视图或移除控件会释放订阅。

原生回调替换失败时，保留清理信息以便重试；重新订阅会重新建立回调，过期的回调不会通知新订阅者。注册后回滚失败的错误记录在 cleanupErrors 中。原生读取结果不符合约定时抛出 NativeOperationError，参数错误在写入前报告。
'''


UI_ACQUIRE.update({
    'UiModelRenderer': '使用 view.getControl(path, "modelRenderer")；模板使用网易模型预览渲染器。',
    'UiModelTransformOptions': '将普通字典传给模型预览方法，设置缩放、角度、旋转轴和变量。',
    'UiEntityRenderOptions': '传给 UiModelRenderer.setEntity，包含通用变换与深度。',
    'UiSkeletonRenderOptions': '传给 UiModelRenderer.setSkeletonModel，包含变换、深度、动画和光照。',
    'UiImageFit': '从 ModSAPI.ui 导入，作为 UiImage.setImageFit 的适配方式。',
    'UiImageInsets': '向 UiImage.setImageFit 传入包含 left、right、top 和 bottom 的字典。',
})

UI_EXAMPLES.update({
    'UiModelRenderer': 'from ModSAPI.client.beta import client\n\ndef show_player(view):\n    preview = view.getControl("/preview", "modelRenderer")\n    preview.setEntity(client.localPlayer, {"scale": 0.8, "rotation": (0, 30, 0)})',
    'UiImageFit': 'from ModSAPI.ui import UiImageFit\n\ndef fit_background(image):\n    image.setImageFit(UiImageFit.NineSlice, {"left": 4, "right": 4, "top": 4, "bottom": 4})',
})

UI_GUIDES['packs/guides/ui-models-and-images.md'] = r'''---
title: 模型预览与图片适配
---

# 模型预览与图片适配

UiModelRenderer 将实体、网易骨骼模型和生成的方块网格体统一为视图控件。取得控件后直接设置预览内容，沿用 UiControl 的位置、尺寸、锚点、显示、动画和移除流程。

## 定义预览模板

将以下内容保存为资源包的 `ui/demo_model.json`：

```json
{
  "namespace": "demo_model",
  "screen": {
    "type": "screen",
    "is_showing_menu": true,
    "controls": [{"panel": {
      "type": "panel",
      "size": [220, 200],
      "controls": [
        {"background": {
          "type": "image",
          "texture": "textures/modsapi_ui/ui/fluent/window",
          "size": [220, 200],
          "layer": 0
        }},
        {"preview": {
          "type": "custom",
          "renderer": "netease_paper_doll_renderer",
          "size": [160, 160],
          "screen_scale": 1.0,
          "rotation": "none",
          "enable_scissor_test": false,
          "layer": 1
        }}
      ]
    }}]
  }
}
```

将 `ui/demo_model.json` 追加到资源包 `_ui_defs.json` 的原有 `ui_defs` 列表。背景图片来自已整合的 ModSAPI 资源包。模板的 renderer 决定控件能力，取得时使用 `modelRenderer`。

## 显示当前玩家或实体定义

```python
from ModSAPI.client.beta import client
from ModSAPI.ui import UiImageFit

def ready(event):
    view = event.view
    background = view.getControl("/panel/background", "image")
    background.setImageFit(UiImageFit.NineSlice, {
        "left": 4, "right": 4, "top": 4, "bottom": 4,
    })
    preview = view.getControl("/panel/preview", "modelRenderer")
    preview.setEntity(client.localPlayer, {
        "scale": 0.8,
        "rotation": (0, 30, 0),
        "depth": -50,
    })

client.ui.registerView("demo:model", "demo_model.screen", {"onReady": ready})

def open_preview(event=None):
    client.ui.openView("demo:model")

if client.ui.isReady:
    open_preview()
else:
    client.afterEvents.uiReady.subscribe(open_preview)
```

setEntity 接受 ClientEntity 或 ClientPlayer 对象，校验所属客户端和实体是否仍可见。传入字符串时，字符串表示 `minecraft:cow` 这样的实体定义，必须包含命名空间。运行时实体身份通过对象传入，公开选项不接受 entity_id 或 entity_identifier。

```python
def show_cow(preview):
    preview.setEntity("minecraft:cow", {"scale": 0.6})
```

预览操作只更新当前原生控件，不向世界发起创建实体的请求。关闭 UiView 或移除控件后，原包装对象不能继续渲染。

## 骨骼动画与方块网格体

```python
def show_skeleton(preview, skeleton_model):
    preview.setSkeletonModel(skeleton_model, {
        "animation": "idle",
        "loop": True,
        "lightDirection": (1, 0, 1),
        "rotation": (0, 45, 0),
        "scale": 1,
    })

def show_geometry(preview, geometry_name):
    preview.setBlockGeometry(geometry_name, {
        "rotation": (15, 45, 0),
        "scale": 0.5,
        "variables": {"variable.example": 1},
    })
```

skeleton_model 需要替换为项目实际存在的网易骨骼模型名称，animation 同样需要该模型具有对应动画。geometry_name 来自已经生成的方块网格体；本方法负责显示，不负责生成或持久化网格体。重新进入世界后，需要先重新生成该资源。

| 参数 | 含义 | 支持范围 |
| --- | --- | --- |
| scale | 有限数值缩放，省略时沿用原生默认值 | 三种预览 |
| rotation | 初始 X、Y、Z 欧拉角，单位为度 | 三种预览 |
| rotationAxis | 原生手势旋转轴 | 三种预览，模板需要 freedom_gesture 并配置输入面板 |
| variables | 独立复制的变量名称与有限数值字典 | 三种预览 |
| depth | 整数渲染深度 | 实体、骨骼 |
| animation | 动画名称，省略时沿用原生默认值 | 骨骼 |
| loop | 是否循环，必须为布尔值 | 骨骼 |
| lightDirection | X、Y、Z 每个值为 -1、0 或 1 | 骨骼 |

完整字段见 UiModelTransformOptions、UiEntityRenderOptions 和 UiSkeletonRenderOptions。rotation 支持 Vector3、三元素序列或包含 x、y、z 的字典。库校验数值是否有限，不自动改写缩放和角度。零值或负缩放的实际效果由原生渲染器决定。

lightDirection 沿用网易的材质与设备限制：自定义材质以及部分低端设备可能不支持该选项。depth 可用于调整预览遮挡，不能用它控制世界中实体的位置。

## 图片适配和九宫格

```python
from ModSAPI.ui import UiImageFit

def configure_images(ordinary, frame):
    ordinary.setImageFit(UiImageFit.Normal)
    frame.setImageFit(UiImageFit.NineSlice, {
        "left": 4, "right": 4, "top": 6, "bottom": 6,
    })
```

UiImageFit 提供 Normal、Filled、NineSlice 和 LegacyNineSlice。普通与填充模式保持图片宽高比；九宫格模式需要 UiImageInsets 字典，四个边距全部填写且为非负有限数值。Normal 和 Filled 不接受边距。没有虚构读取当前适配方式的属性。

## 错误与当前限制

未知选项、错误类型、无穷或 NaN 参数在调用渲染器前报告。原生布尔结果失败时抛出 NativeOperationError，保留对应原生操作；当前 SDK 缺少控件方法时抛出 UnsupportedFeatureError。视图关闭、控件移除或目标实体失效时会拒绝继续操作。

调用成功只表示原生接口接受了请求，不能据此确认资源已经可见。骨骼挂接、预览模型句柄与挂骨特效尚未形成统一公开接口，当前不应将它们计作已封装能力，详见 [ModSDK 功能映射与待补接口](../modsdk-coverage.md)。
'''
