---
title: 语义化事件与筛选
---

# 语义化事件与筛选

ModSAPI 按开发用途提供 55 个事件入口，参考 SAPI 的属性、信号、类型化参数和选项字典设计。多个原生通知可以合并为同一个操作；一个批量原生通知也可以拆成多个有明确用途的回调。

- [客户端语义事件与映射表](../client/semantic-events.md)
- [服务端语义事件与映射表](../server/semantic-events.md)

普通业务优先从这两页查找。已有 SAPI 事件保持标准名称，扩展事件使用 add、remove、change 等动词形式。完整的原生字段、平台条件和检测前提仍可在原生目录查阅，原生入口统一通过 `getNativeEvent` 显式访问。

## 对象引用

回调直接使用 `event.entity`、`event.player`、`event.dimension` 和 `event.otherEntity`，无需再次按 ID 查询。维度未知时为 [None](../common/type-system.md#none)，不会默认成主世界。客户端维度对象提供身份和会话有效性，不提供服务端世界修改能力。

实体卸载或玩家离开时仍返回对象，身份从对象的 `id` 读取；调用实时接口前检查 `isValid`。[EventBlock.dimension](../common/reference/EventBlock.md#dimension) 同样返回维度对象。订阅筛选 `entities` 和 `dimensions` 接收对象列表，拒绝裸 ID 和数字编号。

```python
from ModSAPI.server.beta import world

def on_weather(event):
    if event.dimension is not None:
        print(event.dimension.id, event.newLevel)

world.afterEvents.weatherChange.subscribe(on_weather, {
    "dimensions": [world.getDimension("overworld")],
})
```

## 设计约定

| 常见需求 | 统一入口 | 整理方式 |
| --- | --- | --- |
| 键盘、手柄、自定义按键 | [client.afterEvents.inputButton](../client/reference/ClientAfterEvents.md#inputButton) | 多个来源统一为按钮、设备和 Pressed/Released |
| 只处理按下或抬起 | `inputButtonDown` / `inputButtonUp` | 同一来源按状态拆分 |
| 主操作、副操作、点按、长按 | [client.beforeEvents.pointerAction](../client/reference/ClientBeforeEvents.md#pointerAction) | 保留原生同步取消能力 |
| 手柄摇杆、扳机 | `inputAxis` / `inputStick` / `inputTrigger` | 合并入口和专用入口共存，保留向量与标量区别 |
| 玩家潜行、冲刺等状态 | `playerStateChange` / `playerSneakChange` 等 | 一个动作事件拆为多个具体状态信号 |
| 背包、主手、副手、盔甲 | `playerInventoryItemChange` / `equipmentChange` | 统一前后物品及所属位置 |
| 实体进入、离开 AOI 区域 | `entityEnterArea` / `entityLeaveArea` | 批量原生数据拆成逐实体事件 |
| 碰撞开始、结束，触发器进入、离开 | `physicsContactBegin` 等 | 批量碰撞对拆成逐对事件 |
| 状态效果新增、刷新、移除 | `effectAdd` / `effectRefresh` / `effectRemove` | 新增沿用已有 SAPI 事件，各入口提供 effect 对象 |
| 全局与独立维度天气强度 | [world.afterEvents.weatherChange](../server/events/afterEvents.md#weatherChange) | 保留降雨、雷暴及强度，不猜测未知维度 |
| 实体掉落、箱子战利品、钓鱼掉落 | [world.beforeEvents.lootGenerate](../server/events/beforeEvents.md#lootGenerate) | 统一物品列表写入，自动设置提交标志 |

## 参数类型与关联接口

点击类型名称可查看全部属性、参数、返回值及继承成员。[Optional](../common/type-system.md#optional) 表示允许为空，[Union](../common/type-system.md#union) 表示多个类型之一；事件数据中的嵌套类型也可继续点击查看。

| 用途 | 事件参数或辅助类型 |
| --- | --- |
| 订阅和筛选 | [EventSignal](../common/reference/EventSignal.md)、[EventSubscriptionOptions](../common/reference/EventSubscriptionOptions.md) |
| 按键与手柄轴 | [InputButtonEvent](../common/reference/InputButtonEvent.md)、[InputAxisEvent](../common/reference/InputAxisEvent.md)、[InputDevice](../common/reference/InputDevice.md) |
| 指针交互与释放 | [PointerActionBeforeEvent](../common/reference/PointerActionBeforeEvent.md)、[PointerReleaseEvent](../common/reference/PointerReleaseEvent.md) |
| 玩家状态与实体可见性 | [PlayerStateChangeEvent](../common/reference/PlayerStateChangeEvent.md)、[EntityPresenceEvent](../common/reference/EntityPresenceEvent.md) |
| 库存与装备 | [InventoryChangeEvent](../common/reference/InventoryChangeEvent.md)、[PlayerInventoryItemChangeAfterEvent](../server/reference/PlayerInventoryItemChangeAfterEvent.md) |
| 状态效果 | [EffectAddAfterEvent](../server/reference/EffectAddAfterEvent.md)、[EffectChangeEvent](../common/reference/EffectChangeEvent.md)、[Effect](../server/reference/Effect.md) |
| 物品及方块交互 | [ItemUseAttemptEvent](../common/reference/ItemUseAttemptEvent.md)、[BlockInteractionEvent](../common/reference/BlockInteractionEvent.md) |
| 区域与物理接触 | [EntityAreaEvent](../common/reference/EntityAreaEvent.md)、[PhysicsContactEvent](../common/reference/PhysicsContactEvent.md) |
| 界面栈与关闭 | [ScreenStackChangeEvent](../common/reference/ScreenStackChangeEvent.md)、[ScreenClosingEvent](../common/reference/ScreenClosingEvent.md) |
| 天气和战利品 | [WeatherLevelChangeEvent](../common/reference/WeatherLevelChangeEvent.md)、[LootGenerateBeforeEvent](../common/reference/LootGenerateBeforeEvent.md) |
| 物品与方块快照 | [EventItemStack](../common/reference/EventItemStack.md)、[EventBlock](../common/reference/EventBlock.md) |
| 服务端对象引用 | [Player](../server/apis/player.md)、[Entity](../server/apis/entity.md)、[Dimension](../server/apis/dimension.md) |
| 客户端对象引用 | [ClientPlayer](../client/reference/ClientPlayer.md)、[ClientEntity](../client/reference/ClientEntity.md)、[ClientDimension](../client/reference/ClientDimension.md) |
| 坐标与原生详情 | [Vector3](../server/extra/vector.md)、[NativeEventData](../common/reference/NativeEventData.md)、[NativeEventSignal](../common/reference/NativeEventSignal.md) |

具体事件入口及其参数类型见 [客户端事件目录](../client/semantic-events.md) 和 [服务端事件目录](../server/semantic-events.md)。

## 统一按钮输入与订阅筛选

```python
from ModSAPI.client.beta import client, InputDevice

def on_dash(event):
    print(event.button, event.newButtonState, event.player)

client.afterEvents.customButtonInput.subscribe(on_dash, {
    "buttons": ["example:dash"],
    "state": "Pressed",
    "devices": [InputDevice.Keyboard, InputDevice.Gamepad],
})
```

自定义绑定需先由模组注册。物理按钮的 `button` 是原生编码转成的字符串，自定义按钮则为绑定名称；`key` 保留原始编码。它们没有被强行映射成微软的逻辑 [InputButton](../common/reference/InputButton.md)，因为键位、设备和游戏控制设置可能不同。

```python
from ModSAPI.client.beta import client

def on_press(event):
    print(event.device, event.button, event.isDown)

client.afterEvents.inputButtonDown.subscribe(on_press, {"devices": ["Keyboard"]})
```

主操作可能来自鼠标、触控或手柄，不将它误标成固定物理设备。同步取消写法如下：

```python
from ModSAPI.client.beta import client

def intercept(event):
    event.cancel = True

client.beforeEvents.pointerAction.subscribe(intercept, {"actions": ["Primary", "Tap"]})
```

```python
from ModSAPI.client.beta import client

def on_axis(event):
    if event.controlType == "Stick":
        print(event.key, event.x, event.y)
    else:
        print(event.key, event.value)

client.afterEvents.inputAxis.subscribe(on_axis)
```

扳机没有编造的第二坐标；摇杆也不会被压成标量。需要单一类型时直接订阅 `inputStick` 或 `inputTrigger`。

## 玩家状态

```python
from ModSAPI.server.beta import world

def on_sneak(event):
    print(event.player, event.isEnabled)

world.afterEvents.playerSneakChange.subscribe(on_sneak)
```

客户端提供同名入口。也可只订阅 `playerStateChange` 并传 `{"states": ["sneaking", "sprinting"]}`。已知原生开始、停止动作被解释为新状态；未知动作不会被猜测成某个状态，也不补发订阅前的历史状态。

## 物品变化

```python
from ModSAPI.server.beta import world

def on_inventory(event):
    before = event.beforeItemStack
    after = event.itemStack
    print(event.player, event.inventoryType, event.slot)
    print(before.typeId if before else None, after.amount if after else 0)

world.afterEvents.playerInventoryItemChange.subscribe(on_inventory, {
    "inventoryTypes": ["Inventory"],
    "allowedSlots": [0, 1, 2],
    "includeItems": ["minecraft:diamond"],
    "ignoreQuantityChange": True,
})
```

`includeItems` 和 `excludeItems` 会考虑前后两个物品，所以移除目标物品也能被筛选出来。`ignoreQuantityChange` 仅在提供了旧物品、且除数量之外的原生元数据相同时忽略通知。旧数据未提供时 `hasPreviousItem` 为 False；旧槽位为空但字段已提供时为 True。

`inventoryType` 为 Inventory、Mainhand、Offhand 或 Armor。一次玩家操作可能改变多个存储位置，会保留各位置的通知；封装不按相同时间戳丢掉真实变化。客户端原生主手通知缺少旧物品和槽位时，对应属性保持未知。

[EventItemStack](../common/reference/EventItemStack.md) 提供只读的 `typeId`、`amount`、`clone()`、`withAmount()` 和 `getItemDict()`，保留可用的原生元数据和用户数据。它在两端都不需要查引擎，不会因修改快照而修改背包。新建数量为 1..255；读取已有超量物品保留实际数量。

## 自动处理战利品提交

```python
from ModSAPI.server.beta import world, EventItemStack

def replace_loot(event):
    event.itemStacks = [EventItemStack("minecraft:diamond", 1)]

world.beforeEvents.lootGenerate.subscribe(replace_loot, {
    "lootTypes": ["Entity", "Container", "Fishing"],
})
```

这一个入口接收实体死亡掉落、容器战利品和钓鱼掉落。写入 `itemStacks` 会先校验全部物品，再提交原生 `itemList`，并自动写入正确的 `dirty` 或 `itemChange`。可以传快照、现有服务端 [ItemStack](../server/apis/itemStack.md) 或完整原生物品字典；赋空列表即可清空掉落。

写入只在当前同步回调中有效；不对实体死亡本身进行取消，也不合成不存在的成功后事件。`nativeEvent` 仍保留来源特有字段。

## 交互中的主体、物品与坐标

```python
from ModSAPI.client.beta import client

def inspect_use(event):
    block = event.block
    if block and block.typeId == "example:locked":
        event.cancel = True
    if event.itemStack:
        print(event.itemStack.typeId, event.itemStack.amount)

client.beforeEvents.playerUseItemOnBlock.subscribe(inspect_use)
```

`itemUse` 处理尝试使用物品，`playerUseItemOnBlock` 处理物品对方块的使用，`playerInteractWithBlock` 处理已配置监听的方块交互。它们保留不同的原生触发范围，避免把重叠的钩子合并后对同一次交互重复执行逻辑。

主体通过 `player` / `entity` / `source` 延迟取得；客户端远程玩家是 [ClientEntity](../client/reference/ClientEntity.md)，本地玩家复用 [client.localPlayer](../client/apis/manager.md#localPlayer)。句柄可能已经失效，需检查 `isValid`。所属会话销毁后对象仍可读取身份；客户端对象的 isValid 返回 False。

`block` 是只读 [EventBlock](../common/reference/EventBlock.md)，含 `typeId`、复制的位置和已知维度对象。`blockLocation`、`faceLocation`、`location` 都是复制的 [Vector3](../server/extra/vector.md)。来源没有维度时保留 [None](../common/type-system.md#none)；服务端维度已知时可用 `event.dimension.getBlock(event.blockLocation)` 显式读取当前方块。封装不假定未知方块位于主世界。

## 区域与物理

```python
from ModSAPI.server.beta import world

def entered(event):
    print(event.areaName, event.entity)

world.afterEvents.entityEnterArea.subscribe(entered, {"areaNames": ["example:room"]})
```

区域需要先通过原生 AOI 注册；每个进入/离开的实体分别调用一次回调。原生区域事件只提供区域名和实体 ID，不凭空加入维度。离开时实体可能已经失效；可读取事件实体对象的身份信息进行资源清理。

```python
from ModSAPI.client.beta import client

def contact(event):
    print(event.entity, event.otherEntity, event.location)

client.afterEvents.physicsContactBegin.subscribe(contact, {"entities": [client.localPlayer]})
```

`physicsContactEnd`、`physicsTriggerEnter`、`physicsTriggerLeave` 同样支持逐对处理。`entities` 过滤匹配任一参与者；原生两者顺序不表示固定的触发器/被触发者角色。碰撞细节、检测开关和 物理碰撞掩码 仍由原生配置决定；无详细检测时位置、法线保持 [None](../common/type-system.md#none)。

## 界面与效果

```python
from ModSAPI.client.beta import client

def top_changed(event):
    print(event.operation, event.topScreenName)

client.afterEvents.screenStackChange.subscribe(top_changed)
```

Pop 后原生给出的是新顶层界面，因此使用明确的 `topScreenName` / `topScreenDefinition`。要读即将移除的界面，订阅 [client.beforeEvents.screenClose](../client/reference/ClientBeforeEvents.md#screenClose)，其字段描述 outgoing screen；该通知无法取消关闭。不会把新顶层界面错误标成被关闭的界面。

```python
from ModSAPI.server.beta import world

def effect_changed(event):
    print(event.entity, event.changeType, event.effect.typeId, event.effect.duration)

world.afterEvents.effectRefresh.subscribe(effect_changed, {"effectTypes": ["minecraft:speed"]})
```

效果新增使用原有的 `effectAdd`，读取 `event.effect` 和 `event.entity`。刷新使用 `effectRefresh`，移除使用 `effectRemove`，二者同样返回 effect 对象。`effect.duration` 将原生秒数乘 20 转成名义 SAPI tick 数；刷新、移除事件的 `durationSeconds` 保留原值。原生永久效果的特殊数值仍需按目标引擎判断。

`weatherChange` 统一 Rain / Thunder 及强度变化，提供 `isGlobal`、`dimension`、`previousLevel`、`newLevel`。全局天气不假定某个固定维度，不把强度渐变误解成一次天气切换。

## 筛选、错误与性能

所有语义信号接受 `subscribe(callback, options=None)`。公共筛选为 `entities`、`entityTypes`、`dimensions`；各信号专有选项见目录。`entities` 和 `dimensions` 接收对象，空列表匹配零个事件。传入的筛选会复制，同一回调再次订阅可更新其筛选；保存回调以便注销。

已移除的实体若未由原生事件提供类型，`entityTypes` 可能无法再查询到它，不能据此保证收到卸载通知。需要可靠清理时向 `entities` 传入之前保存的实体对象；此筛选只比较身份，不要求实体仍有效。

不支持的选项、拼写错误和无效枚举会抛出 [ValueError](../common/type-system.md#valueerror)，错误类型抛出 [TypeError](../common/type-system.md#typeerror)。每个用户回调独立处理异常，其他订阅者继续执行。不会因为过滤一个维度或物品而自动开启额外的检测。

多个便利入口复用同一原生源；只在首次订阅时安装引擎监听。ID、已知类型、物品和坐标先从快照筛选，只有显式的 entityTypes 查询可能在原生类型缺失时查引擎。大批量事件逐项派发，退出或注销可立即停止后续回调。

多来源订阅中途失败会回滚已订阅来源。语义信号注销先逻辑禁用回调；若原生注销失败会抛出 [NativeOperationError](../common/reference/NativeOperationError.md)，重复 unsubscribe 可重试残余清理，已禁用回调不再运行。这与原生高级信号保留订阅以便重试的约定不同。销毁会关闭所属信号，保留其他消费者的监听。