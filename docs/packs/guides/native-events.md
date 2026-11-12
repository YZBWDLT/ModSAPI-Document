---
title: 原生事件全覆盖、取消与清理
---

# 原生事件全覆盖、取消与清理

当前目录对照网易 ModSDK 原生文档索引，提供 **120 个客户端、178 个服务端事件绑定**，覆盖输入、[UI](../server_ui/reference/UI.md)、音效、实体、玩家、物品、方块、区块、天气、模型、物理和平台事件。服务端事件从 `world` 取得；客户端事件从 `client` 取得。

- [客户端全部事件与前提](../client/events.md)
- [服务端全部事件与前提](../server/native-events.md)

## 风格与边界

```python
from ModSAPI.client.beta import client

def on_entity_added(event):
    print(event.entity, event.engineTypeStr, event.dimension)

signal = client.afterEvents.getNativeEvent('AddEntityClientEvent')
signal.subscribe(on_entity_added)

def cleanup():
    signal.unsubscribe(on_entity_added)
```

信号统一采用 `subscribe(callback)` / `unsubscribe(callback)`。重复订阅同一个函数或绑定方法不会重复调用；订阅返回该回调。没有订阅时不注册原生监听器；最后一个订阅移除时释放监听。客户端或世界销毁时关闭所属信号，不再派发迟到回调。

属性名采用 lowerCamelCase。实体、玩家和维度引用直接返回 [Entity](../server/apis/entity.md) / [Player](../server/apis/player.md) / [Dimension](../server/apis/dimension.md)，客户端对应 [ClientEntity](../client/reference/ClientEntity.md) / [ClientPlayer](../client/reference/ClientPlayer.md) / [ClientDimension](../client/reference/ClientDimension.md)；远程玩家使用只含客户端实体能力的 [ClientEntity](../client/reference/ClientEntity.md)。未知引用返回 [None](../common/type-system.md#none)。原生数字编号和字符串 ID 只通过显式的 `getNativeData()` / `getNativeValue()` 读取。资源名、枚举和物品字典保留其数据语义；Python 保留字 `from` 对应 `fromValue`。

已有 SAPI 事件优先沿用标准名称和参数类型，例如 `effectAdd`、`playerInventoryItemChange`、`itemUse`。不再建立表示同一观察的第二个属性入口。需要检查原生编码时调用 `getNativeEvent(...)`；例如原生滚轮方向仍为 0/1，而 `mouseWheel.direction` 为 -1/+1。

## 查找事件

```python
from ModSAPI.client.beta import client

print(client.beforeEvents.getEventNames())
print(client.afterEvents.getNativeEventNames())

signal = client.beforeEvents.getNativeEvent("ClientItemUseOnEvent")
print(signal.nativeEventName)
```

查询只接受当前端、当前集合目录中的准确原生名；未知名称或错误的 before/after 集合抛出 [KeyError](../common/type-system.md#keyerror)，不会偷偷创建一个永远不触发的信号。属性入口和 `getNativeEvent` 返回同一个信号。

## 客户端拦截输入与界面

```python
from ModSAPI.client.beta import client

def block_creative_inventory(event):
    if event.isCreative:
        event.cancel = True

def disable_jump(event):
    event.cancel = True

client.beforeEvents.getNativeEvent('ClientPlayerInventoryOpenEvent').subscribe(block_creative_inventory)
client.beforeEvents.getNativeEvent('ClientJumpButtonPressDownEvent').subscribe(disable_jump)
```

`jumpButtonPress.cancel = True` 写入原生 `continueJump = False`；`itemUseOn.cancel = True` 写入原生 `ret = True`。原生字段仍可直接读写。`cancelShears` 只取消剪刀特殊效果，`cancelDrop` 只取消掉落，不会被误包装成取消整个动作。

自定义键位和手柄事件保持原生编码，`isDown` 可能是字符串 `"1"` / `"0"`：

```python
from ModSAPI.client.beta import client

def on_custom_key(event):
    if event.name == "example:action" and event.isDown == "1":
        print("action pressed", event.key)

def on_gamepad_stick(event):
    print(event.key, event.x, event.y)

client.afterEvents.getNativeEvent('OnCustomKeyPressInGame').subscribe(on_custom_key)
client.afterEvents.getNativeEvent('OnGamepadStickClientEvent').subscribe(on_gamepad_stick)
```

键位需要先由模组注册。[UI](../server_ui/reference/UI.md) 事件可用于响应屏幕尺寸和原生 HUD 按钮布局变化：

```python
from ModSAPI.client.beta import client

def on_resize(event):
    print(event.beforeX, event.beforeY, event.afterX, event.afterY)

def on_hud_change(event):
    for button in event.changedList or ():
        print(button.get("areaEnum"), button.get("afterSize"))

client.afterEvents.getNativeEvent('ScreenSizeChangedClientEvent').subscribe(on_resize)
client.afterEvents.getNativeEvent('HudButtonChangedClientEvent').subscribe(on_hud_change)
```

## 客户端音效拦截

```python
from ModSAPI.client.beta import client

def filter_sound(event):
    if event.name == "example:muted_sound":
        event.cancel = True

client.beforeEvents.getNativeEvent('PlaySoundClientEvent').subscribe(filter_sound)
```

此事件只影响本机音效播放，不修改服务端状态。播放、停止音乐和场景声音使用不同的原生事件，不应拿音乐定义 ID 当作场景音效实例 ID。

## 服务端伤害、物品与掉落

```python
from ModSAPI.server.beta import world

def cap_damage(event):
    if event.damage is not None and event.damage > 10:
        event.damage = 10.0

def prevent_pickup(event):
    item = event.itemDict or {}
    if item.get("newItemName") == "example:restricted":
        event.cancel = True
        event.pickupDelay = 30

world.beforeEvents.getNativeEvent('DamageEvent').subscribe(cap_damage)
world.beforeEvents.getNativeEvent('ServerPlayerTryTouchEvent').subscribe(prevent_pickup)
```

[DamageEvent](../server/native-events.md#damageevent) 是吸收计算前的伤害，[ActuallyHurtServerEvent](../server/native-events.md#actuallyhurtserverevent) 是吸收后的可写伤害，[ActorHurtServerEvent](../server/native-events.md#actorhurtserverevent) 的最终伤害只读。客户端攻击通知也只读；服务端 `playerAttackEntity` 设置伤害后还需设置 `isValid = 1`。这些原生条件不会因接口名字相似而消失。

掉落列表读取返回副本；修改后必须重新赋值，并设置原生要求的提交标志：

```python
from ModSAPI.server.beta import world

def change_loot(event):
    items = event.itemList or []
    for item in items:
        if item.get("newItemName") == "minecraft:diamond":
            item["count"] = 1
    event.itemList = items
    event.dirty = True

world.beforeEvents.getNativeEvent('EntityDieLoottableServerEvent').subscribe(change_loot)
```

容器战利品使用 `containerLoot` 与 `dirty`；钓鱼使用 `playerFishing` 与 `itemChange`；附魔台选项使用 `itemPutInEnchantingModel` 与 `change`。返回的嵌套容器也不会因原地修改而自动回写。物品 UserData 是否存在取决于原生配置，封装不会修改全局扩展设置。

## 方块与高频事件

```python
from ModSAPI.server.beta import world

def on_block_tick(event):
    if event.blockName == "example:machine":
        print(event.dimension, event.posX, event.posY, event.posZ)

def on_chunk_loaded(event):
    print(event.dimension, event.chunkPosX, event.chunkPosZ)

world.afterEvents.getNativeEvent('ServerBlockEntityTickEvent').subscribe(on_block_tick)
world.afterEvents.getNativeEvent('ChunkLoadedServerEvent').subscribe(on_chunk_loaded)
```

`blockEntityTick` 需要方块配置 `netease:block_entity` 且 `tick = true`，并处于模拟距离或 tickingarea。`entityTick` 需要实体白名单；碰撞、AOI、刚体触发器、方块内部/踩踏事件也需要原生注册或 JSON 开关，逐项见目录。订阅不会自动开启所有检测。

脚本 `tick` 为网易原生每秒 30 次，渲染 `render` 随帧率变化，部分实体/方块 tick 为每秒 20 次。它们与 `runInterval` 的 0.05 秒请求单位不同。在高频回调中优先检查 ID/类型，只处理目标对象；批处理昂贵的全世界扫描，不要每帧创建 [UI](../server_ui/reference/UI.md)、读取存档或打印日志。

## 同步写入、平台和失败处理

before 表示 pending action 或仍接受输出的原生钩子，不等于微软的限制执行阶段。部分原生名称含 After 的钩子仍接受后续力学计算参数，会放在 before 集合；最终事件目录是准确入口。只有 SDK 明确接受的输出可写，不能从 before 名称推断所有字段都可写。

取消、掉落列表和力学参数必须在当前同步回调中写完。回调结束或所属对象销毁后，写入抛出 [RuntimeError](../common/type-system.md#runtimeerror)；此时仍可读取快照。`getNativeData()` 返回容器副本并保留新版引擎的未知字段，`setNativeValue()` 仍只允许文档确认的输出。原生句柄与任意用户对象保留身份及其原生生命周期，不能把它们当作深度冻结或永久有效的数据。

```python
from ModSAPI.client.beta import client, NativeOperationError

def on_inventory_close(event):
    print(event.nativeEventName)

try:
    client.afterEvents.getNativeEvent('ClientPlayerInventoryCloseEvent').subscribe(on_inventory_close)
except NativeOperationError as error:
    print(error.operation, error.code, error.cause)
```

非函数回调或错误字段类型抛出 [TypeError](../common/type-system.md#typeerror)；非有限数或已知越界值抛出 [ValueError](../common/type-system.md#valueerror)；只读/未知字段写入抛出 [AttributeError](../common/type-system.md#attributeerror)；失效客户端、世界或事件集合抛出 [InvalidClientObjectError](../common/reference/InvalidClientObjectError.md)。原生订阅/注销失败抛出 [NativeOperationError](../common/reference/NativeOperationError.md)，普通注销失败保留订阅以便重试；销毁时即使原生注销失败也先逻辑关闭，避免迟到回调继续操作状态。单个回调异常会被记录，其余订阅者继续执行，已写入原生的输出不会回滚。

某些动作需要客户端和服务端同时取消，例如停止骑乘、开始挖掘、扑灭火焰、释放蓄力物品和剪断绊线。客户端取消不能代替服务端权限校验。`cancelable = False` 的盾牌事件和 `canChange = False` 的耐久事件会拒绝相应写入。

Apollo 旋转攻击、商城、联机大厅、成就等事件仅在对应环境/系统启用后触发。一次性加载事件必须在加载完成前订阅，封装不补发历史事件。旧引擎可能静默忽略新事件，订阅调用成功不代表该事件在当前版本可用；需要按目标引擎和资源做实机验证。本轮未以空实现占位任何目录事件，也没有合成引擎不存在的 after 通知。


## 更便捷的业务入口

优先使用 [语义化事件与筛选](semantic-events.md)，从按键、玩家状态、库存变化、战利品和区域等需求出发；本页继续提供准确的原生映射与约束。