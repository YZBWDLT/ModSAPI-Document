---
title: 界面动画与跟随界面
---

# 界面动画与跟随界面

## 原生属性动画

[UiControl.animate](../ui/reference/UiControl.md#animate) 创建 [UiAnimation](../ui/reference/UiAnimation.md)，动画由引擎推进。可用属性包括 opacity、position、size，以及图片控件的 clipRatio。

```python
from __future__ import print_function

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

启动失败会抛出 [NativeOperationError](../common/reference/NativeOperationError.md) 并尝试清理已经取得的资源。异步结束时的失败由 `animation.afterEvents.error` 或创建选项 onError 接收，`animation.error` 保留异常。

清理失败后可再次调用 `animation.dispose()`，只重试尚未成功释放的部分。启动失败且回滚也失败时，异常的 animation 属性保留对应 [UiAnimation](../ui/reference/UiAnimation.md)，cleanupErrors 列出回滚错误。`view.close()` 和 `client.ui.closeAllViews()` 也会重试自己拥有的残留动画注册；界面已经关闭时仍可重试这些清理。

## 常驻界面

先用 `registerView` 声明模板，再在原生界面就绪后创建：

```python
def create_status(client):
    client.ui.registerView("demo:status", "demo_ui.status")
    return client.ui.createHud("demo:status")
```

HUD 不加入本库管理的界面栈。它仍使用 [UiView](../ui/reference/UiView.md)，可以取得控件、绑定状态和关闭。一个注册标识同一时刻只能有一个存活的 HUD；重复创建前应关闭旧实例。

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

entity 使用 [ClientEntity](../client/reference/ClientEntity.md) 或 [ClientPlayer](../client/reference/ClientPlayer.md)，不传实体编号。绑定对象必须有效，并属于当前客户端会话。offset 表示相对实体的三维偏移，autoScale 决定是否按距离缩放。

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

dimension 使用 [ClientDimension](../client/reference/ClientDimension.md)，省略时取本地玩家当前显示的维度；切换维度期间原生结果不可用时会明确报错。location 与 entity 互斥，实体偏移不用于固定世界位置。缩放表现及可见距离仍取决于原生界面模板和游戏渲染规则。