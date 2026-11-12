---
sidebar_position: 2
title: 客户端语义事件
---

# 客户端语义事件

本页按开发用途组织 **30 个事件入口**，采用 SAPI 风格的信号、类型化参数和订阅筛选。

可将多个互补的原生通知合并，也可将一个原生批次拆成多个事件。只在需要时注册原生监听；多个入口共享相同原生源，不重复安装引擎监听器。

[推荐用法与完整示例](../guides/semantic-events.md) · [原生事件索引](events.md)

## 事件索引

| 入口 | 参数类型 | 原生源数量 |
| --- | --- | --- |
| [afterEvents.inputButton](#inputbutton) | [InputButtonEvent](../common/reference/InputButtonEvent.md) | 5 |
| [afterEvents.inputButtonDown](#inputbuttondown) | [InputButtonEvent](../common/reference/InputButtonEvent.md) | 5 |
| [afterEvents.inputButtonUp](#inputbuttonup) | [InputButtonEvent](../common/reference/InputButtonEvent.md) | 5 |
| [afterEvents.customButtonInput](#custombuttoninput) | [InputButtonEvent](../common/reference/InputButtonEvent.md) | 2 |
| [beforeEvents.pointerAction](#pointeraction) | [PointerActionBeforeEvent](../common/reference/PointerActionBeforeEvent.md) | 4 |
| [afterEvents.pointerRelease](#pointerrelease) | [PointerReleaseEvent](../common/reference/PointerReleaseEvent.md) | 3 |
| [afterEvents.inputAxis](#inputaxis) | [InputAxisEvent](../common/reference/InputAxisEvent.md) | 2 |
| [afterEvents.inputStick](#inputstick) | [InputAxisEvent](../common/reference/InputAxisEvent.md) | 1 |
| [afterEvents.inputTrigger](#inputtrigger) | [InputAxisEvent](../common/reference/InputAxisEvent.md) | 1 |
| [afterEvents.playerStateChange](#playerstatechange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerSneakChange](#playersneakchange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerSprintChange](#playersprintchange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerGlideChange](#playerglidechange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerSwimChange](#playerswimchange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerCrawlChange](#playercrawlchange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerFlyChange](#playerflychange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerSleepChange](#playersleepchange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerSpinAttackChange](#playerspinattackchange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.entityLoad](#entityload) | [EntityPresenceEvent](../common/reference/EntityPresenceEvent.md) | 2 |
| [afterEvents.entityRemove](#entityremove) | [EntityPresenceEvent](../common/reference/EntityPresenceEvent.md) | 2 |
| [afterEvents.screenStackChange](#screenstackchange) | [ScreenStackChangeEvent](../common/reference/ScreenStackChangeEvent.md) | 2 |
| [beforeEvents.screenClose](#screenclose) | [ScreenClosingEvent](../common/reference/ScreenClosingEvent.md) | 1 |
| [afterEvents.playerInventoryItemChange](#playerinventoryitemchange) | [InventoryChangeEvent](../common/reference/InventoryChangeEvent.md) | 2 |
| [afterEvents.physicsContactBegin](#physicscontactbegin) | [PhysicsContactEvent](../common/reference/PhysicsContactEvent.md) | 1 |
| [afterEvents.physicsContactEnd](#physicscontactend) | [PhysicsContactEvent](../common/reference/PhysicsContactEvent.md) | 1 |
| [afterEvents.physicsTriggerEnter](#physicstriggerenter) | [PhysicsContactEvent](../common/reference/PhysicsContactEvent.md) | 1 |
| [afterEvents.physicsTriggerLeave](#physicstriggerleave) | [PhysicsContactEvent](../common/reference/PhysicsContactEvent.md) | 1 |
| [beforeEvents.itemUse](#itemuse) | [ItemUseAttemptEvent](../common/reference/ItemUseAttemptEvent.md) | 1 |
| [beforeEvents.playerUseItemOnBlock](#playeruseitemonblock) | [BlockInteractionEvent](../common/reference/BlockInteractionEvent.md) | 1 |
| [beforeEvents.playerInteractWithBlock](#playerinteractwithblock) | [BlockInteractionEvent](../common/reference/BlockInteractionEvent.md) | 1 |

## inputButton {#inputbutton}

信号：[client.afterEvents.inputButton](reference/ClientAfterEvents.md#inputButton)；参数：[InputButtonEvent](../common/reference/InputButtonEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `buttons`, `state`, `devices`, `screenNames`。

原生来源：

- [OnKeyPressInGame](events.md#onkeypressingame)
- [OnGamepadKeyPressClientEvent](events.md#ongamepadkeypressclientevent)
- [OnCustomKeyPressInGame](events.md#oncustomkeypressingame)
- [OnCustomGamepadPressInGame](events.md#oncustomgamepadpressingame)
- [OnMouseMiddleDownClientEvent](events.md#onmousemiddledownclientevent)


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.inputButton.subscribe(on_event)

def cleanup():
    client.afterEvents.inputButton.unsubscribe(on_event)
```


## inputButtonDown {#inputbuttondown}

信号：[client.afterEvents.inputButtonDown](reference/ClientAfterEvents.md#inputButtonDown)；参数：[InputButtonEvent](../common/reference/InputButtonEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `buttons`, `state`, `devices`, `screenNames`。

原生来源：

- [OnKeyPressInGame](events.md#onkeypressingame)
- [OnGamepadKeyPressClientEvent](events.md#ongamepadkeypressclientevent)
- [OnCustomKeyPressInGame](events.md#oncustomkeypressingame)
- [OnCustomGamepadPressInGame](events.md#oncustomgamepadpressingame)
- [OnMouseMiddleDownClientEvent](events.md#onmousemiddledownclientevent)

此入口仅保留 `Pressed` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.inputButtonDown.subscribe(on_event)

def cleanup():
    client.afterEvents.inputButtonDown.unsubscribe(on_event)
```


## inputButtonUp {#inputbuttonup}

信号：[client.afterEvents.inputButtonUp](reference/ClientAfterEvents.md#inputButtonUp)；参数：[InputButtonEvent](../common/reference/InputButtonEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `buttons`, `state`, `devices`, `screenNames`。

原生来源：

- [OnKeyPressInGame](events.md#onkeypressingame)
- [OnGamepadKeyPressClientEvent](events.md#ongamepadkeypressclientevent)
- [OnCustomKeyPressInGame](events.md#oncustomkeypressingame)
- [OnCustomGamepadPressInGame](events.md#oncustomgamepadpressingame)
- [OnMouseMiddleDownClientEvent](events.md#onmousemiddledownclientevent)

此入口仅保留 `Released` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.inputButtonUp.subscribe(on_event)

def cleanup():
    client.afterEvents.inputButtonUp.unsubscribe(on_event)
```


## customButtonInput {#custombuttoninput}

信号：[client.afterEvents.customButtonInput](reference/ClientAfterEvents.md#customButtonInput)；参数：[InputButtonEvent](../common/reference/InputButtonEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `buttons`, `state`, `devices`, `screenNames`。

原生来源：

- [OnCustomKeyPressInGame](events.md#oncustomkeypressingame)
- [OnCustomGamepadPressInGame](events.md#oncustomgamepadpressingame)


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.customButtonInput.subscribe(on_event)

def cleanup():
    client.afterEvents.customButtonInput.unsubscribe(on_event)
```


## pointerAction {#pointeraction}

信号：[client.beforeEvents.pointerAction](reference/ClientBeforeEvents.md#pointerAction)；参数：[PointerActionBeforeEvent](../common/reference/PointerActionBeforeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `actions`。

原生来源：

- [LeftClickBeforeClientEvent](events.md#leftclickbeforeclientevent)
- [RightClickBeforeClientEvent](events.md#rightclickbeforeclientevent)
- [TapBeforeClientEvent](events.md#tapbeforeclientevent)
- [HoldBeforeClientEvent](events.md#holdbeforeclientevent)


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.beforeEvents.pointerAction.subscribe(on_event)

def cleanup():
    client.beforeEvents.pointerAction.unsubscribe(on_event)
```


## pointerRelease {#pointerrelease}

信号：[client.afterEvents.pointerRelease](reference/ClientAfterEvents.md#pointerRelease)；参数：[PointerReleaseEvent](../common/reference/PointerReleaseEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `actions`。

原生来源：

- [LeftClickReleaseClientEvent](events.md#leftclickreleaseclientevent)
- [RightClickReleaseClientEvent](events.md#rightclickreleaseclientevent)
- [TapOrHoldReleaseClientEvent](events.md#taporholdreleaseclientevent)


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.pointerRelease.subscribe(on_event)

def cleanup():
    client.afterEvents.pointerRelease.unsubscribe(on_event)
```


## inputAxis {#inputaxis}

信号：[client.afterEvents.inputAxis](reference/ClientAfterEvents.md#inputAxis)；参数：[InputAxisEvent](../common/reference/InputAxisEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `axes`, `controlTypes`。

原生来源：

- [OnGamepadStickClientEvent](events.md#ongamepadstickclientevent)
- [OnGamepadTriggerClientEvent](events.md#ongamepadtriggerclientevent)


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.inputAxis.subscribe(on_event)

def cleanup():
    client.afterEvents.inputAxis.unsubscribe(on_event)
```


## inputStick {#inputstick}

信号：[client.afterEvents.inputStick](reference/ClientAfterEvents.md#inputStick)；参数：[InputAxisEvent](../common/reference/InputAxisEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `axes`, `controlTypes`。

原生来源：

- [OnGamepadStickClientEvent](events.md#ongamepadstickclientevent)

此入口仅保留 `Stick` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.inputStick.subscribe(on_event)

def cleanup():
    client.afterEvents.inputStick.unsubscribe(on_event)
```


## inputTrigger {#inputtrigger}

信号：[client.afterEvents.inputTrigger](reference/ClientAfterEvents.md#inputTrigger)；参数：[InputAxisEvent](../common/reference/InputAxisEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `axes`, `controlTypes`。

原生来源：

- [OnGamepadTriggerClientEvent](events.md#ongamepadtriggerclientevent)

此入口仅保留 `Trigger` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.inputTrigger.subscribe(on_event)

def cleanup():
    client.afterEvents.inputTrigger.unsubscribe(on_event)
```


## playerStateChange {#playerstatechange}

信号：[client.afterEvents.playerStateChange](reference/ClientAfterEvents.md#playerStateChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnLocalPlayerActionClientEvent](events.md#onlocalplayeractionclientevent)


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.playerStateChange.subscribe(on_event)

def cleanup():
    client.afterEvents.playerStateChange.unsubscribe(on_event)
```


## playerSneakChange {#playersneakchange}

信号：[client.afterEvents.playerSneakChange](reference/ClientAfterEvents.md#playerSneakChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnLocalPlayerActionClientEvent](events.md#onlocalplayeractionclientevent)

此入口仅保留 `sneaking` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.playerSneakChange.subscribe(on_event)

def cleanup():
    client.afterEvents.playerSneakChange.unsubscribe(on_event)
```


## playerSprintChange {#playersprintchange}

信号：[client.afterEvents.playerSprintChange](reference/ClientAfterEvents.md#playerSprintChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnLocalPlayerActionClientEvent](events.md#onlocalplayeractionclientevent)

此入口仅保留 `sprinting` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.playerSprintChange.subscribe(on_event)

def cleanup():
    client.afterEvents.playerSprintChange.unsubscribe(on_event)
```


## playerGlideChange {#playerglidechange}

信号：[client.afterEvents.playerGlideChange](reference/ClientAfterEvents.md#playerGlideChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnLocalPlayerActionClientEvent](events.md#onlocalplayeractionclientevent)

此入口仅保留 `gliding` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.playerGlideChange.subscribe(on_event)

def cleanup():
    client.afterEvents.playerGlideChange.unsubscribe(on_event)
```


## playerSwimChange {#playerswimchange}

信号：[client.afterEvents.playerSwimChange](reference/ClientAfterEvents.md#playerSwimChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnLocalPlayerActionClientEvent](events.md#onlocalplayeractionclientevent)

此入口仅保留 `swimming` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.playerSwimChange.subscribe(on_event)

def cleanup():
    client.afterEvents.playerSwimChange.unsubscribe(on_event)
```


## playerCrawlChange {#playercrawlchange}

信号：[client.afterEvents.playerCrawlChange](reference/ClientAfterEvents.md#playerCrawlChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnLocalPlayerActionClientEvent](events.md#onlocalplayeractionclientevent)

此入口仅保留 `crawling` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.playerCrawlChange.subscribe(on_event)

def cleanup():
    client.afterEvents.playerCrawlChange.unsubscribe(on_event)
```


## playerFlyChange {#playerflychange}

信号：[client.afterEvents.playerFlyChange](reference/ClientAfterEvents.md#playerFlyChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnLocalPlayerActionClientEvent](events.md#onlocalplayeractionclientevent)

此入口仅保留 `flying` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.playerFlyChange.subscribe(on_event)

def cleanup():
    client.afterEvents.playerFlyChange.unsubscribe(on_event)
```


## playerSleepChange {#playersleepchange}

信号：[client.afterEvents.playerSleepChange](reference/ClientAfterEvents.md#playerSleepChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnLocalPlayerActionClientEvent](events.md#onlocalplayeractionclientevent)

此入口仅保留 `sleeping` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.playerSleepChange.subscribe(on_event)

def cleanup():
    client.afterEvents.playerSleepChange.unsubscribe(on_event)
```


## playerSpinAttackChange {#playerspinattackchange}

信号：[client.afterEvents.playerSpinAttackChange](reference/ClientAfterEvents.md#playerSpinAttackChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnLocalPlayerActionClientEvent](events.md#onlocalplayeractionclientevent)

此入口仅保留 `spinAttacking` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.playerSpinAttackChange.subscribe(on_event)

def cleanup():
    client.afterEvents.playerSpinAttackChange.unsubscribe(on_event)
```


## entityLoad {#entityload}

信号：[client.afterEvents.entityLoad](reference/ClientAfterEvents.md#entityLoad)；参数：[EntityPresenceEvent](../common/reference/EntityPresenceEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`。

原生来源：

- [AddEntityClientEvent](events.md#addentityclientevent)
- [AddPlayerCreatedClientEvent](events.md#addplayercreatedclientevent)

此入口仅保留 `load` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.entityLoad.subscribe(on_event)

def cleanup():
    client.afterEvents.entityLoad.unsubscribe(on_event)
```


## entityRemove {#entityremove}

信号：[client.afterEvents.entityRemove](reference/ClientAfterEvents.md#entityRemove)；参数：[EntityPresenceEvent](../common/reference/EntityPresenceEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`。

原生来源：

- [RemoveEntityClientEvent](events.md#removeentityclientevent)
- [RemovePlayerAOIClientEvent](events.md#removeplayeraoiclientevent)

此入口仅保留 `unload` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.entityRemove.subscribe(on_event)

def cleanup():
    client.afterEvents.entityRemove.unsubscribe(on_event)
```


## screenStackChange {#screenstackchange}

信号：[client.afterEvents.screenStackChange](reference/ClientAfterEvents.md#screenStackChange)；参数：[ScreenStackChangeEvent](../common/reference/ScreenStackChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `screenNames`。

原生来源：

- [PushScreenEvent](events.md#pushscreenevent)
- [PopScreenAfterClientEvent](events.md#popscreenafterclientevent)


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.screenStackChange.subscribe(on_event)

def cleanup():
    client.afterEvents.screenStackChange.unsubscribe(on_event)
```


## screenClose {#screenclose}

信号：[client.beforeEvents.screenClose](reference/ClientBeforeEvents.md#screenClose)；参数：[ScreenClosingEvent](../common/reference/ScreenClosingEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `screenNames`。

原生来源：

- [PopScreenEvent](events.md#popscreenevent)


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.beforeEvents.screenClose.subscribe(on_event)

def cleanup():
    client.beforeEvents.screenClose.unsubscribe(on_event)
```


## playerInventoryItemChange {#playerinventoryitemchange}

信号：[client.afterEvents.playerInventoryItemChange](reference/ClientAfterEvents.md#playerInventoryItemChange)；参数：[InventoryChangeEvent](../common/reference/InventoryChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `inventoryTypes`, `allowedSlots`, `includeItems`, `excludeItems`, `ignoreQuantityChange`。

原生来源：

- [InventoryItemChangedClientEvent](events.md#inventoryitemchangedclientevent)
- [OnCarriedNewItemChangedClientEvent](events.md#oncarriednewitemchangedclientevent)


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.playerInventoryItemChange.subscribe(on_event)

def cleanup():
    client.afterEvents.playerInventoryItemChange.unsubscribe(on_event)
```


## physicsContactBegin {#physicscontactbegin}

信号：[client.afterEvents.physicsContactBegin](reference/ClientAfterEvents.md#physicsContactBegin)；参数：[PhysicsContactEvent](../common/reference/PhysicsContactEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`。

原生来源：

- [PhysxTouchClientEvent](events.md#physxtouchclientevent)

此入口仅保留 `touch` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.physicsContactBegin.subscribe(on_event)

def cleanup():
    client.afterEvents.physicsContactBegin.unsubscribe(on_event)
```


## physicsContactEnd {#physicscontactend}

信号：[client.afterEvents.physicsContactEnd](reference/ClientAfterEvents.md#physicsContactEnd)；参数：[PhysicsContactEvent](../common/reference/PhysicsContactEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`。

原生来源：

- [PhysxTouchClientEvent](events.md#physxtouchclientevent)

此入口仅保留 `lost` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.physicsContactEnd.subscribe(on_event)

def cleanup():
    client.afterEvents.physicsContactEnd.unsubscribe(on_event)
```


## physicsTriggerEnter {#physicstriggerenter}

信号：[client.afterEvents.physicsTriggerEnter](reference/ClientAfterEvents.md#physicsTriggerEnter)；参数：[PhysicsContactEvent](../common/reference/PhysicsContactEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`。

原生来源：

- [PhysxTriggerClientEvent](events.md#physxtriggerclientevent)

此入口仅保留 `found` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.physicsTriggerEnter.subscribe(on_event)

def cleanup():
    client.afterEvents.physicsTriggerEnter.unsubscribe(on_event)
```


## physicsTriggerLeave {#physicstriggerleave}

信号：[client.afterEvents.physicsTriggerLeave](reference/ClientAfterEvents.md#physicsTriggerLeave)；参数：[PhysicsContactEvent](../common/reference/PhysicsContactEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`。

原生来源：

- [PhysxTriggerClientEvent](events.md#physxtriggerclientevent)

此入口仅保留 `lost` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.afterEvents.physicsTriggerLeave.subscribe(on_event)

def cleanup():
    client.afterEvents.physicsTriggerLeave.unsubscribe(on_event)
```


## itemUse {#itemuse}

信号：[client.beforeEvents.itemUse](reference/ClientBeforeEvents.md#itemUse)；参数：[ItemUseAttemptEvent](../common/reference/ItemUseAttemptEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `includeItems`, `excludeItems`。

原生来源：

- [ClientItemTryUseEvent](events.md#clientitemtryuseevent)


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.beforeEvents.itemUse.subscribe(on_event)

def cleanup():
    client.beforeEvents.itemUse.unsubscribe(on_event)
```


## playerUseItemOnBlock {#playeruseitemonblock}

信号：[client.beforeEvents.playerUseItemOnBlock](reference/ClientBeforeEvents.md#playerUseItemOnBlock)；参数：[BlockInteractionEvent](../common/reference/BlockInteractionEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `includeItems`, `excludeItems`, `blockTypes`。

原生来源：

- [ClientItemUseOnEvent](events.md#clientitemuseonevent)


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.beforeEvents.playerUseItemOnBlock.subscribe(on_event)

def cleanup():
    client.beforeEvents.playerUseItemOnBlock.unsubscribe(on_event)
```


## playerInteractWithBlock {#playerinteractwithblock}

信号：[client.beforeEvents.playerInteractWithBlock](reference/ClientBeforeEvents.md#playerInteractWithBlock)；参数：[BlockInteractionEvent](../common/reference/BlockInteractionEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `blockTypes`。

原生来源：

- [ClientBlockUseEvent](events.md#clientblockuseevent)


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.beforeEvents.playerInteractWithBlock.subscribe(on_event)

def cleanup():
    client.beforeEvents.playerInteractWithBlock.unsubscribe(on_event)
```