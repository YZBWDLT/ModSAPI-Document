---
title: 布局与常用控件
---

# 布局与常用控件

[UiView](../ui/reference/UiView.md) 负责界面生命周期，[UiControl](../ui/reference/UiControl.md) 提供位置、尺寸、锚点、裁剪与状态绑定。需要专用能力时，通过 getControl 的种类参数取得 [UiGrid](../ui/reference/UiGrid.md)、[UiStackPanel](../ui/reference/UiStackPanel.md)、[UiItemRenderer](../ui/reference/UiItemRenderer.md) 等类型。控件种类必须与资源包模板一致。

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

网格的格子在渲染阶段创建，onReady 中可能还不存在；getItem 此时返回 [None](../common/type-system.md#none)。示例将首次填充安排到下一次客户端调度，未创建的格子留给后续渲染更新。改变 setDimensions、滚动回收或重新布局后，应重新调用 getItem 取得当前格子，不要长期保存格子路径与序号的对应关系。

滚动网格还应监听 [client.afterEvents.gridComponentSizeChange](../client/reference/ClientAfterEvents.md#gridComponentSizeChange)，按当前数据重新取得并填充格子；该原生事件仅提供 path，不提供本库视图身份，多个视图有同名路径时需要结合自己的打开状态筛选。订阅应在视图关闭时取消。高频刷新只更新变化的项目，避免每帧重建整个网格。

[UiItem](../ui/reference/UiItem.md) 表示渲染快照，设置预览不会修改背包。setItem 接受物品名称、[UiItem](../ui/reference/UiItem.md) 或 [EventItemStack](../common/reference/EventItemStack.md)。读取 item 只能得到原生返回的名称、附加值和附魔显示标记；原生读取接口不返回 userData，因此无法从已有预览恢复这部分数据。

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

[UiScrollView.progress](../ui/reference/UiScrollView.md#progress) 使用 0～1 的滚动比例，scrollOffset 使用原生滚动像素。content 每次查询当前内容控件，适应触控与键鼠模板路径切换。不要自行拼接固定的内容子路径。

[UiInputPanel](../ui/reference/UiInputPanel.md) 的 isModal 限制界面输入范围，swallowInput 控制输入是否穿透到世界。dragOffset 是原生累计拖动位移，与 position 分别存储；JSON 中还需配置 draggable 和 button_mappings 才能接收拖动。

## 错误与释放

错误参数在调用原生接口前抛出 [TypeError](../common/type-system.md#typeerror) 或 [ValueError](../common/type-system.md#valueerror)；控件种类与模板不符时抛出 [UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)；失效视图和控件抛出 [InvalidClientObjectError](../common/reference/InvalidClientObjectError.md)。原生布尔失败、异常及不符合契约的读取结果会报告 [NativeOperationError](../common/reference/NativeOperationError.md)，并保留 operation 等诊断信息。

focus 与 blur 使用引擎的选中控件入口，实际键盘输入能力取决于控件种类。动态创建后若包装失败，库会尝试移除已创建的原生节点；清理失败记录在异常的 cleanupErrors 中。使用完毕后调用 view.close，绑定、按钮订阅和动画由视图释放。