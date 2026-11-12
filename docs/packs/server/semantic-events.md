---
sidebar_position: 2
title: 服务端语义事件
---

# 服务端语义事件

本页按开发用途组织 **25 个事件入口**，采用 SAPI 风格的信号、类型化参数和订阅筛选。

可将多个互补的原生通知合并，也可将一个原生批次拆成多个事件。只在需要时注册原生监听；多个入口共享相同原生源，不重复安装引擎监听器。

[推荐用法与完整示例](../guides/semantic-events.md) · [原生事件索引](native-events.md)

## 事件索引

| 入口 | 参数类型 | 原生源数量 |
| --- | --- | --- |
| [afterEvents.playerStateChange](#playerstatechange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerSneakChange](#playersneakchange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerSprintChange](#playersprintchange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerGlideChange](#playerglidechange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerSwimChange](#playerswimchange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerCrawlChange](#playercrawlchange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerFlyChange](#playerflychange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerSleepChange](#playersleepchange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerSpinAttackChange](#playerspinattackchange) | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md) | 1 |
| [afterEvents.playerInventoryItemChange](#playerinventoryitemchange) | [PlayerInventoryItemChangeAfterEvent](reference/PlayerInventoryItemChangeAfterEvent.md) | 1 |
| [afterEvents.equipmentChange](#equipmentchange) | [InventoryChangeEvent](../common/reference/InventoryChangeEvent.md) | 3 |
| [afterEvents.physicsContactBegin](#physicscontactbegin) | [PhysicsContactEvent](../common/reference/PhysicsContactEvent.md) | 1 |
| [afterEvents.physicsContactEnd](#physicscontactend) | [PhysicsContactEvent](../common/reference/PhysicsContactEvent.md) | 1 |
| [afterEvents.physicsTriggerEnter](#physicstriggerenter) | [PhysicsContactEvent](../common/reference/PhysicsContactEvent.md) | 1 |
| [afterEvents.physicsTriggerLeave](#physicstriggerleave) | [PhysicsContactEvent](../common/reference/PhysicsContactEvent.md) | 1 |
| [afterEvents.entityEnterArea](#entityenterarea) | [EntityAreaEvent](../common/reference/EntityAreaEvent.md) | 1 |
| [afterEvents.entityLeaveArea](#entityleavearea) | [EntityAreaEvent](../common/reference/EntityAreaEvent.md) | 1 |
| [afterEvents.effectAdd](#effectadd) | [EffectAddAfterEvent](reference/EffectAddAfterEvent.md) | 1 |
| [afterEvents.effectRefresh](#effectrefresh) | [EffectChangeEvent](../common/reference/EffectChangeEvent.md) | 1 |
| [afterEvents.effectRemove](#effectremove) | [EffectChangeEvent](../common/reference/EffectChangeEvent.md) | 1 |
| [afterEvents.weatherChange](#weatherchange) | [WeatherLevelChangeEvent](../common/reference/WeatherLevelChangeEvent.md) | 4 |
| [beforeEvents.itemUse](#itemuse) | [ItemUseAttemptEvent](../common/reference/ItemUseAttemptEvent.md) | 1 |
| [beforeEvents.playerUseItemOnBlock](#playeruseitemonblock) | [BlockInteractionEvent](../common/reference/BlockInteractionEvent.md) | 1 |
| [beforeEvents.playerInteractWithBlock](#playerinteractwithblock) | [BlockInteractionEvent](../common/reference/BlockInteractionEvent.md) | 1 |
| [beforeEvents.lootGenerate](#lootgenerate) | [LootGenerateBeforeEvent](../common/reference/LootGenerateBeforeEvent.md) | 3 |

## playerStateChange {#playerstatechange}

信号：[world.afterEvents.playerStateChange](events/afterEvents.md#playerStateChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnPlayerActionServerEvent](native-events.md#onplayeractionserverevent)


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.playerStateChange.subscribe(on_event)

def cleanup():
    world.afterEvents.playerStateChange.unsubscribe(on_event)
```


## playerSneakChange {#playersneakchange}

信号：[world.afterEvents.playerSneakChange](events/afterEvents.md#playerSneakChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnPlayerActionServerEvent](native-events.md#onplayeractionserverevent)

此入口仅保留 `sneaking` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.playerSneakChange.subscribe(on_event)

def cleanup():
    world.afterEvents.playerSneakChange.unsubscribe(on_event)
```


## playerSprintChange {#playersprintchange}

信号：[world.afterEvents.playerSprintChange](events/afterEvents.md#playerSprintChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnPlayerActionServerEvent](native-events.md#onplayeractionserverevent)

此入口仅保留 `sprinting` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.playerSprintChange.subscribe(on_event)

def cleanup():
    world.afterEvents.playerSprintChange.unsubscribe(on_event)
```


## playerGlideChange {#playerglidechange}

信号：[world.afterEvents.playerGlideChange](events/afterEvents.md#playerGlideChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnPlayerActionServerEvent](native-events.md#onplayeractionserverevent)

此入口仅保留 `gliding` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.playerGlideChange.subscribe(on_event)

def cleanup():
    world.afterEvents.playerGlideChange.unsubscribe(on_event)
```


## playerSwimChange {#playerswimchange}

信号：[world.afterEvents.playerSwimChange](events/afterEvents.md#playerSwimChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnPlayerActionServerEvent](native-events.md#onplayeractionserverevent)

此入口仅保留 `swimming` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.playerSwimChange.subscribe(on_event)

def cleanup():
    world.afterEvents.playerSwimChange.unsubscribe(on_event)
```


## playerCrawlChange {#playercrawlchange}

信号：[world.afterEvents.playerCrawlChange](events/afterEvents.md#playerCrawlChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnPlayerActionServerEvent](native-events.md#onplayeractionserverevent)

此入口仅保留 `crawling` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.playerCrawlChange.subscribe(on_event)

def cleanup():
    world.afterEvents.playerCrawlChange.unsubscribe(on_event)
```


## playerFlyChange {#playerflychange}

信号：[world.afterEvents.playerFlyChange](events/afterEvents.md#playerFlyChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnPlayerActionServerEvent](native-events.md#onplayeractionserverevent)

此入口仅保留 `flying` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.playerFlyChange.subscribe(on_event)

def cleanup():
    world.afterEvents.playerFlyChange.unsubscribe(on_event)
```


## playerSleepChange {#playersleepchange}

信号：[world.afterEvents.playerSleepChange](events/afterEvents.md#playerSleepChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnPlayerActionServerEvent](native-events.md#onplayeractionserverevent)

此入口仅保留 `sleeping` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.playerSleepChange.subscribe(on_event)

def cleanup():
    world.afterEvents.playerSleepChange.unsubscribe(on_event)
```


## playerSpinAttackChange {#playerspinattackchange}

信号：[world.afterEvents.playerSpinAttackChange](events/afterEvents.md#playerSpinAttackChange)；参数：[PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `states`。

原生来源：

- [OnPlayerActionServerEvent](native-events.md#onplayeractionserverevent)

此入口仅保留 `spinAttacking` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.playerSpinAttackChange.subscribe(on_event)

def cleanup():
    world.afterEvents.playerSpinAttackChange.unsubscribe(on_event)
```


## playerInventoryItemChange {#playerinventoryitemchange}

信号：[world.afterEvents.playerInventoryItemChange](events/afterEvents.md#playerInventoryItemChange)；参数：[PlayerInventoryItemChangeAfterEvent](reference/PlayerInventoryItemChangeAfterEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `inventoryTypes`, `allowedSlots`, `includeItems`, `excludeItems`, `ignoreQuantityChange`。

原生来源：

- [InventoryItemChangedServerEvent](native-events.md#inventoryitemchangedserverevent)


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.playerInventoryItemChange.subscribe(on_event)

def cleanup():
    world.afterEvents.playerInventoryItemChange.unsubscribe(on_event)
```


## equipmentChange {#equipmentchange}

信号：[world.afterEvents.equipmentChange](events/afterEvents.md#equipmentChange)；参数：[InventoryChangeEvent](../common/reference/InventoryChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `inventoryTypes`, `allowedSlots`, `includeItems`, `excludeItems`, `ignoreQuantityChange`。

原生来源：

- [OnCarriedNewItemChangedServerEvent](native-events.md#oncarriednewitemchangedserverevent)
- [OnOffhandItemChangedServerEvent](native-events.md#onoffhanditemchangedserverevent)
- [OnNewArmorExchangeServerEvent](native-events.md#onnewarmorexchangeserverevent)


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.equipmentChange.subscribe(on_event)

def cleanup():
    world.afterEvents.equipmentChange.unsubscribe(on_event)
```


## physicsContactBegin {#physicscontactbegin}

信号：[world.afterEvents.physicsContactBegin](events/afterEvents.md#physicsContactBegin)；参数：[PhysicsContactEvent](../common/reference/PhysicsContactEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`。

原生来源：

- [PhysxTouchServerEvent](native-events.md#physxtouchserverevent)

此入口仅保留 `touch` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.physicsContactBegin.subscribe(on_event)

def cleanup():
    world.afterEvents.physicsContactBegin.unsubscribe(on_event)
```


## physicsContactEnd {#physicscontactend}

信号：[world.afterEvents.physicsContactEnd](events/afterEvents.md#physicsContactEnd)；参数：[PhysicsContactEvent](../common/reference/PhysicsContactEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`。

原生来源：

- [PhysxTouchServerEvent](native-events.md#physxtouchserverevent)

此入口仅保留 `lost` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.physicsContactEnd.subscribe(on_event)

def cleanup():
    world.afterEvents.physicsContactEnd.unsubscribe(on_event)
```


## physicsTriggerEnter {#physicstriggerenter}

信号：[world.afterEvents.physicsTriggerEnter](events/afterEvents.md#physicsTriggerEnter)；参数：[PhysicsContactEvent](../common/reference/PhysicsContactEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`。

原生来源：

- [PhysxTriggerServerEvent](native-events.md#physxtriggerserverevent)

此入口仅保留 `found` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.physicsTriggerEnter.subscribe(on_event)

def cleanup():
    world.afterEvents.physicsTriggerEnter.unsubscribe(on_event)
```


## physicsTriggerLeave {#physicstriggerleave}

信号：[world.afterEvents.physicsTriggerLeave](events/afterEvents.md#physicsTriggerLeave)；参数：[PhysicsContactEvent](../common/reference/PhysicsContactEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`。

原生来源：

- [PhysxTriggerServerEvent](native-events.md#physxtriggerserverevent)

此入口仅保留 `lost` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.physicsTriggerLeave.subscribe(on_event)

def cleanup():
    world.afterEvents.physicsTriggerLeave.unsubscribe(on_event)
```


## entityEnterArea {#entityenterarea}

信号：[world.afterEvents.entityEnterArea](events/afterEvents.md#entityEnterArea)；参数：[EntityAreaEvent](../common/reference/EntityAreaEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `areaNames`。

原生来源：

- [NewOnEntityAreaEvent](native-events.md#newonentityareaevent)

此入口仅保留 `enteredEntities` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.entityEnterArea.subscribe(on_event)

def cleanup():
    world.afterEvents.entityEnterArea.unsubscribe(on_event)
```


## entityLeaveArea {#entityleavearea}

信号：[world.afterEvents.entityLeaveArea](events/afterEvents.md#entityLeaveArea)；参数：[EntityAreaEvent](../common/reference/EntityAreaEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `areaNames`。

原生来源：

- [NewOnEntityAreaEvent](native-events.md#newonentityareaevent)

此入口仅保留 `leftEntities` 对应的观察；其他入口仍可独立接收同一原生源。


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.entityLeaveArea.subscribe(on_event)

def cleanup():
    world.afterEvents.entityLeaveArea.unsubscribe(on_event)
```


## effectAdd {#effectadd}

信号：[world.afterEvents.effectAdd](events/afterEvents.md#effectAdd)；参数：[EffectAddAfterEvent](reference/EffectAddAfterEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `effectTypes`。

原生来源：

- [AddEffectServerEvent](native-events.md#addeffectserverevent)


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.effectAdd.subscribe(on_event)

def cleanup():
    world.afterEvents.effectAdd.unsubscribe(on_event)
```


## effectRefresh {#effectrefresh}

信号：[world.afterEvents.effectRefresh](events/afterEvents.md#effectRefresh)；参数：[EffectChangeEvent](../common/reference/EffectChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `effectTypes`, `changeTypes`。

原生来源：

- [RefreshEffectServerEvent](native-events.md#refresheffectserverevent)


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.effectRefresh.subscribe(on_event)

def cleanup():
    world.afterEvents.effectRefresh.unsubscribe(on_event)
```


## effectRemove {#effectremove}

信号：[world.afterEvents.effectRemove](events/afterEvents.md#effectRemove)；参数：[EffectChangeEvent](../common/reference/EffectChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `effectTypes`, `changeTypes`。

原生来源：

- [RemoveEffectServerEvent](native-events.md#removeeffectserverevent)


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.effectRemove.subscribe(on_event)

def cleanup():
    world.afterEvents.effectRemove.unsubscribe(on_event)
```


## weatherChange {#weatherchange}

信号：[world.afterEvents.weatherChange](events/afterEvents.md#weatherChange)；参数：[WeatherLevelChangeEvent](../common/reference/WeatherLevelChangeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `weatherTypes`。

原生来源：

- [OnRainLevelChangeServerEvent](native-events.md#onrainlevelchangeserverevent)
- [OnLightningLevelChangeServerEvent](native-events.md#onlightninglevelchangeserverevent)
- [OnLocalRainLevelChangeServerEvent](native-events.md#onlocalrainlevelchangeserverevent)
- [OnLocalLightningLevelChangeServerEvent](native-events.md#onlocallightninglevelchangeserverevent)


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.weatherChange.subscribe(on_event)

def cleanup():
    world.afterEvents.weatherChange.unsubscribe(on_event)
```


## itemUse {#itemuse}

信号：[world.beforeEvents.itemUse](events/beforeEvents.md#itemUse)；参数：[ItemUseAttemptEvent](../common/reference/ItemUseAttemptEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `includeItems`, `excludeItems`。

原生来源：

- [ServerItemTryUseEvent](native-events.md#serveritemtryuseevent)


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.beforeEvents.itemUse.subscribe(on_event)

def cleanup():
    world.beforeEvents.itemUse.unsubscribe(on_event)
```


## playerUseItemOnBlock {#playeruseitemonblock}

信号：[world.beforeEvents.playerUseItemOnBlock](events/beforeEvents.md#playerUseItemOnBlock)；参数：[BlockInteractionEvent](../common/reference/BlockInteractionEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `includeItems`, `excludeItems`, `blockTypes`。

原生来源：

- [ServerItemUseOnEvent](native-events.md#serveritemuseonevent)


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.beforeEvents.playerUseItemOnBlock.subscribe(on_event)

def cleanup():
    world.beforeEvents.playerUseItemOnBlock.unsubscribe(on_event)
```


## playerInteractWithBlock {#playerinteractwithblock}

信号：[world.beforeEvents.playerInteractWithBlock](events/beforeEvents.md#playerInteractWithBlock)；参数：[BlockInteractionEvent](../common/reference/BlockInteractionEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `blockTypes`。

原生来源：

- [ServerBlockUseEvent](native-events.md#serverblockuseevent)


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.beforeEvents.playerInteractWithBlock.subscribe(on_event)

def cleanup():
    world.beforeEvents.playerInteractWithBlock.unsubscribe(on_event)
```


## lootGenerate {#lootgenerate}

信号：[world.beforeEvents.lootGenerate](events/beforeEvents.md#lootGenerate)；参数：[LootGenerateBeforeEvent](../common/reference/LootGenerateBeforeEvent.md)。

支持筛选：`entities`, `entityTypes`, `dimensions`, `lootTypes`。

原生来源：

- [EntityDieLoottableServerEvent](native-events.md#entitydieloottableserverevent)
- [OnContainerFillLoottableServerEvent](native-events.md#oncontainerfillloottableserverevent)
- [PlayerFishingServerEvent](native-events.md#playerfishingserverevent)


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.beforeEvents.lootGenerate.subscribe(on_event)

def cleanup():
    world.beforeEvents.lootGenerate.unsubscribe(on_event)
```