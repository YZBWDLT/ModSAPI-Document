---
title: 原生抬头显示与原版界面
---

# 原生抬头显示与原版界面

[UiService](../ui/reference/UiService.md) 在 [client.ui](../client/apis/manager.md#ui) 下统一提供自定义界面、主题表单及网易原生界面操作。本页操作只作用于本机，不能通过 [system.ui](../server/reference/System.md#ui) 直接修改其他玩家的原生界面。实际原生调用需要等待 [客户端界面就绪事件](../client/reference/ClientUiReadyAfterEvent.md)。自定义界面的完整流程见 [界面、控件与生命周期](managed-ui.md)。

## 按元素隐藏或恢复

```python
from ModSAPI.client.beta import client
from ModSAPI.ui import UiHudElement, HudVisibility

def hide_status_bars():
    client.ui.hud.setHudVisibility(HudVisibility.Hide, [
        UiHudElement.Health,
        UiHudElement.Armor,
        UiHudElement.Hunger,
    ])

def restore_status_bars():
    client.ui.hud.setHudVisibility(HudVisibility.Reset, [
        UiHudElement.Health,
        UiHudElement.Armor,
        UiHudElement.Hunger,
    ])
```

[UiHud](../ui/reference/UiHud.md) 从 [client.ui.hud](../ui/reference/UiService.md#hud) 取得并缓存；句柄可以提前取得，实际操作仍须等界面就绪。[HudVisibility](../common/reference/HudVisibility.md) 的 Hide 表示隐藏，Reset 表示通过对应原生通道恢复显示。显示仍受游戏模式、全局隐藏、平台和原生布局影响。

元素使用 [UiHudElement](../ui/reference/UiHudElement.md)。这是网易扩展常量，不是微软 [HudElement](../common/reference/HudElement.md) 的数字枚举。共支持二十二个通道，覆盖状态条、快捷栏、准心、触控按钮、聊天入口与聊天消息区。`ChatButton` 是聊天入口，`ChatMessages` 是左上角的小消息窗口，二者分别控制。

省略 `hudElements` 时操作全部受支持通道；空列表不写入，但仍检查当前端、生命周期和界面就绪状态。整批元素及方法是否存在会在写入前检查；重复元素只写一次并保留输入顺序。后续原生操作失败仍可能留下先前修改，不提供事务或旧值回滚。

## 全局隐藏与输入权限

若需要配置表情功能本身，应在原生界面初始化之前调用 [UiService.setEmotesEnabled](../ui/reference/UiService.md#setEmotesEnabled)，而不是隐藏已经创建的表情按钮。调用阶段和本地动作示例见 [本地交互与触控布局](client-interaction-and-controls.md)。

```python
def hide_native_hud():
    client.ui.hud.setHidden(True)

def release_global_hiding():
    client.ui.hud.setHidden(False)
```

`setHidden()` 使用类似 F1 的全局隐藏方式，原位置仍可能响应触控；它不会逐一重设所有元素通道。部分按钮通过 `setHudVisibility()` 单独隐藏时，原生接口会同时停止该按钮的触控响应。两种行为不同，库保留原生语义。

如果需要控制移动、攻击或打开背包等输入，请使用 [本地输入与界面权限](input-and-view-permissions.md) 的 [client.input](../client/apis/manager.md#input) 或视图 `inputPermissions`。界面的临时输入权限可以随视图关闭而释放；本页直接 HUD 写入没有原生旧值读取，不会在关闭界面或客户端销毁时猜测并强制全部显示。

## 聊天位置与生命值动画

```python
def position_messages():
    client.ui.hud.setChatPosition({"x": 100, "y": 0})

def show_health_blink():
    client.ui.hud.playHealthBlink()
```

`setChatPosition()` 接受 [Vector2](../common/reference/Vector2.md)、二元序列或含 x、y 的字典，保留零和负偏移。原点在玩家纸娃娃下方，不是物理窗口的左上角；接口没有对应的位置读取和自动恢复。`playHealthBlink()` 只播放原版生命值闪烁，不会给玩家造成伤害。

## 打开原版界面

```python
from ModSAPI.ui import UiNativeScreen

def open_inventory():
    client.ui.openNativeScreen(UiNativeScreen.Inventory, {
        "categoryName": "nature",
        "force": False,
    })

def open_chat():
    client.ui.openNativeScreen(UiNativeScreen.Chat)

def open_product():
    client.ui.openNativeScreen(UiNativeScreen.Store, {
        "categoryName": u"商品分类",
        "itemName": u"商品名称",
    })
```

[UiNativeScreen](../ui/reference/UiNativeScreen.md) 包含 Chat、Inventory、Pause、Emotes、Menu、Report、Store 七种入口。选项类型见 [UiNativeScreenOptions](../ui/reference/UiNativeScreenOptions.md)。

| 界面 | 可用选项 | 行为 |
| --- | --- | --- |
| Chat、Pause | force | 默认 False；已有菜单可能阻止打开 |
| Inventory | categoryName、force | 默认建筑分页 construction；也支持自定义分页名 |
| Emotes、Menu、Report | 无 | 交给原版界面处理 |
| Store | categoryName、itemName | 两项必填；请求打开商品界面，不会自动购买 |

原生打开方法没有可验证的成功返回值，`openNativeScreen()` 返回 [None](../common/type-system.md#none) 仅表示请求没有报告调用错误，不能保证界面已显示。它不创建 [UiView](../ui/reference/UiView.md)，也不伪造关闭事件或由 `closeAllViews()` 管理。需要托管生命周期时仍使用 `openView()` 或主题表单。

打开聊天还会触发原生聊天按钮事件，不要从该事件回调再次打开聊天。本库会拒绝同步重入，避免递归打开；这不能代替正确的事件流程。暂停界面是否暂停世界以及商店是否可用，均由原生环境决定。

## 分辨率、视角与原生区域

```python
from ModSAPI.ui import UiNativeArea

def read_layout_context():
    resolution = client.ui.screenSize
    viewport = client.ui.viewport
    chat = client.ui.getNativeArea(UiNativeArea.ChatButton)
    return {
        "resolution": (resolution.x, resolution.y),
        "viewSize": (viewport.size.x, viewport.size.y),
        "viewOffset": (viewport.offset.x, viewport.offset.y),
        "chatPosition": (chat.left, chat.top),
        "chatSize": (chat.size.x, chat.size.y),
    }
```

`screenSize` 返回当前分辨率的 [Vector2](../common/reference/Vector2.md)，单位为像素。[UiViewport](../ui/reference/UiViewport.md) 包含原生视角宽高和偏移，宽高可能按界面倍率对齐，与分辨率不同。例如原生分辨率为一千七百九十二乘八百二十八时，视角宽度可能为一千七百九十四。库只保留原生结果，不自动计算缩放比例或推断安全区域。

[UiNativeArea](../ui/reference/UiNativeArea.md) 列出四十三种已记录的原生区域名，包括不同触控布局的移动、跳跃、潜行、聊天、交互、划船和提示区域。部分原生枚举尚未列出、但文档允许直接传字符串的区域，也已整理为常量；常量存在不保证当前布局提供该区域。`getNativeArea()` 返回 [UiRectangle](../ui/reference/UiRectangle.md)，包含只读 left、top、right、bottom，以及独立的 position、size 向量。坐标属于原生基类画布，不能直接等同于物理像素。

原生区域不可用时可能返回全零，例如新版聊天取代了旧聊天按钮；库会保留零矩形，不能据此断言按钮可见或可点击。负位置允许保留，倒置边界、非法长度、非有限数值和布尔坐标会报告原生读取错误。

每次读取都会重新查询，返回的几何对象是独立快照；修改取得的向量不会修改快照、界面或后续查询。一次布局计算应复用同一份结果，避免对相同上下文反复查询。

## 平台限制与错误

旧聊天、语音与表情按钮可能被新版聊天扩展替代；部分入口仅适用于手机端。快捷栏的原生层级会连带影响经验条，不能保证隐藏快捷栏同时保留经验条。网易商店入口与商品界面不支持部分服务器环境。接口存在不表示当前平台一定能显示对应元素，以上行为仍需游戏内验证。

参数错误在调用前报告 [TypeError](../common/type-system.md#typeerror) 或 [ValueError](../common/type-system.md#valueerror)。SDK 缺少请求的方法时报告 [UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)；原生异常、失败标记或损坏几何报告 [NativeOperationError](../common/reference/NativeOperationError.md)，保留具体操作名和原因。客户端销毁后，保留的 [UiHud](../ui/reference/UiHud.md) 也不能继续调用。完整能力缺口见 [ModSDK 功能映射与待补接口](../modsdk-coverage.md)。

命名参考 [微软屏幕显示接口文档](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/screendisplay?view=minecraft-bedrock-stable)，原生行为参考 [网易原生界面接口文档](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md)。微软 ScreenDisplay 的真实隐藏状态查询、完整 [HudElement](../common/reference/HudElement.md) 对应、服务端控制及未知旧值恢复仍未具备可靠等价实现；本页没有将本机扩展标为这些接口的完整替代。