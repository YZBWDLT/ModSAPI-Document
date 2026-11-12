---
title: 自定义控件与组合模板
---

# 自定义控件与组合模板

[Control.register](../ui/reference/Control.md#register) 使用一个统一入口，把 JSON 模板与具有明确字段的描述对象关联。[Button](../ui/reference/Button.md)、[Toggle](../ui/reference/Toggle.md)、[Slider](../ui/reference/Slider.md)、[TextField](../ui/reference/TextField.md)、[Dropdown](../ui/reference/Dropdown.md)、[ListView](../ui/reference/ListView.md)、[Label](../ui/reference/Label.md)、[Divider](../ui/reference/Divider.md)、[ScrollingPanel](../ui/reference/ScrollingPanel.md)、[Custom](../ui/reference/Custom.md) 和 [Group](../ui/reference/Group.md) 都使用这一入口。

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

[CreateArguments](../ui/reference/CreateArguments.md) 提供布局完成后的样式和参数快照。[ObservableUpdateArguments](../ui/reference/ObservableUpdateArguments.md) 提供顶层参数名、新旧值和当前参数快照。嵌套状态已解包，不需要在回调里继续识别传输编号。

这些高级回调同时提供原生控件和屏幕，供封装尚未覆盖的控件特性使用。它们属于明确的原生扩展边界；常规界面应使用 [UiView](../ui/reference/UiView.md)、[UiControl](../ui/reference/UiControl.md) 和状态绑定。

## 控件组

[Group](../ui/reference/Group.md) 定义具名子控件的类型和布局，表单 group 方法提供每次实例自己的数据和回调。

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

以上例子在客户端使用；服务端回调接收 [Player](../server/apis/player.md)，应调用该对象支持的服务端接口。子控件 class 必填，组内百分比相对父组计算。嵌套组通过 children 传递数据，具体字段见 [GroupDefinitions](../common/type-aliases.md#groupdefinitions)、[GroupChildren](../common/type-aliases.md#groupchildren) 和 [GroupChildData](../ui/reference/GroupChildData.md)。

列表、自定义控件和控件组仍需对应资源包模板。缺失模板、错误控件路径及真实布局不能仅靠声明确认，应在目标游戏版本中验证。