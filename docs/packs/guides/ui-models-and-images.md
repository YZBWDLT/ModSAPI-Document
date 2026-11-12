---
title: 模型预览与图片适配
---

# 模型预览与图片适配

[UiModelRenderer](../ui/reference/UiModelRenderer.md) 将实体、网易骨骼模型和生成的方块网格体统一为视图控件。取得控件后直接设置预览内容，沿用 [UiControl](../ui/reference/UiControl.md) 的位置、尺寸、锚点、显示、动画和移除流程。

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

setEntity 接受 [ClientEntity](../client/reference/ClientEntity.md) 或 [ClientPlayer](../client/reference/ClientPlayer.md) 对象，校验所属客户端和实体是否仍可见。传入字符串时，字符串表示 `minecraft:cow` 这样的实体定义，必须包含命名空间。运行时实体身份通过对象传入，公开选项不接受 entity_id 或 entity_identifier。

```python
def show_cow(preview):
    preview.setEntity("minecraft:cow", {"scale": 0.6})
```

预览操作只更新当前原生控件，不向世界发起创建实体的请求。关闭 [UiView](../ui/reference/UiView.md) 或移除控件后，原包装对象不能继续渲染。

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

完整字段见 [UiModelTransformOptions](../ui/reference/UiModelTransformOptions.md)、[UiEntityRenderOptions](../ui/reference/UiEntityRenderOptions.md) 和 [UiSkeletonRenderOptions](../ui/reference/UiSkeletonRenderOptions.md)。rotation 支持 [Vector3](../server/extra/vector.md)、三元素序列或包含 x、y、z 的字典。库校验数值是否有限，不自动改写缩放和角度。零值或负缩放的实际效果由原生渲染器决定。

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

[UiImageFit](../ui/reference/UiImageFit.md) 提供 Normal、Filled、NineSlice 和 LegacyNineSlice。普通与填充模式保持图片宽高比；九宫格模式需要 [UiImageInsets](../ui/reference/UiImageInsets.md) 字典，四个边距全部填写且为非负有限数值。Normal 和 Filled 不接受边距。没有虚构读取当前适配方式的属性。

## 错误与当前限制

未知选项、错误类型、无穷或 NaN 参数在调用渲染器前报告。原生布尔结果失败时抛出 [NativeOperationError](../common/reference/NativeOperationError.md)，保留对应原生操作；当前 SDK 缺少控件方法时抛出 [UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)。视图关闭、控件移除或目标实体失效时会拒绝继续操作。

调用成功只表示原生接口接受了请求，不能据此确认资源已经可见。骨骼挂接、预览模型句柄与挂骨特效尚未形成统一公开接口，当前不应将它们计作已封装能力，详见 [ModSDK 功能映射与待补接口](../modsdk-coverage.md)。