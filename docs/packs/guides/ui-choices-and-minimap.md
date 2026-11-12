---
title: 选择控件与小地图
---

# 选择控件与小地图

[UiComboBox](../ui/reference/UiComboBox.md)、[UiSelectionWheel](../ui/reference/UiSelectionWheel.md) 与 [UiMiniMap](../ui/reference/UiMiniMap.md) 使用原生控件模板，并接入 [UiView](../ui/reference/UiView.md) 的生命周期。它们适合已有资源包界面；只需要组合设置表单时，也可以直接使用 [Form.dropdown](../ui/reference/Form.md#dropdown)。

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

selectedIndex 使用零起始索引，没有选中时为 [None](../common/type-system.md#none)；赋值 [None](../common/type-system.md#none) 会清除选择。findOption 按显示文字查询，未找到时也返回 [None](../common/type-system.md#none)。selectLabel 按文字选中，removeOption 接受索引或显示文字，clearOptions 清空所有内容。

addOption 会复制普通数据；事件中的 [UiChoiceEvent.value](../ui/reference/UiChoiceEvent.md#value) 每次读取也返回副本。原生读取接口不提供已有选项自定义值的读取能力，因此库只提供 selectedIndex、selectedLabel 和 getOptionLabel，不虚构可恢复全部选项数据的属性。

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

sliceCount 来自模板，selectedIndex 没有选中时为 [None](../common/type-system.md#none)。selectionChange 读取原生悬浮通知中的当前索引，仅在观察到索引变化时通知，过滤重复的进入和离开通知；select 表示指针按下并抬起，允许 index 为 [None](../common/type-system.md#none)。[UiChoiceEvent](../ui/reference/UiChoiceEvent.md) 的 label 和 value 在轮盘中为 [None](../common/type-system.md#none)。

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

addMarker 和 addTextMarker 接受三维位置或客户端实体对象，返回 [UiMapMarker](../ui/reference/UiMapMarker.md)。固定位置只把 X/Z 交给地图；Y 保留在 location 的输入副本中。实体标记的 entity 是包装对象，固定标记的 entity 为 [None](../common/type-system.md#none)。相同实体的图片与文字可同时存在，同一种标记重复添加会报错，以免旧句柄误删新标记。

marker.remove 只移除当前标记，成功后重复调用无副作用。clearMarkers 会尝试所有标记，保留失败句柄，并在异常的 cleanupErrors 中列出错误；随后可以重试。关闭视图或移除地图控件也会使相关句柄失效。

setHeightLimit 默认重绘已有区块；多次调整时可传 repaint=False，最后只调用一次 refresh。zoomIn 和 zoomOut 接受非负增量，resetZoom 恢复默认缩放。小地图不会因此加载远处区块，过度缩小可能影响标记显示；不要每帧重绘整个地图。

## 回调与释放约定

业务回调始终接收包装事件。库负责将下拉框和轮盘的原生通知绑定到界面节点，再分发到对应控件；同一视图中的多个控件互不覆盖。subscribe 返回取消函数，关闭视图或移除控件会释放订阅。

原生回调替换失败时，保留清理信息以便重试；重新订阅会重新建立回调，过期的回调不会通知新订阅者。注册后回滚失败的错误记录在 cleanupErrors 中。原生读取结果不符合约定时抛出 [NativeOperationError](../common/reference/NativeOperationError.md)，参数错误在写入前报告。