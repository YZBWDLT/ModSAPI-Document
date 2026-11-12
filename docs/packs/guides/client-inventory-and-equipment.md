---
title: 客户端背包与装备
---

# 客户端背包与装备

客户端沿用组件、容器、槽位和物品值的对象关系，不需要额外注册系统。通过 [client.localPlayer](../client/apis/manager.md#localPlayer) 取得本地玩家，再使用 [ClientEntityComponentTypes](../client/reference/ClientEntityComponentTypes.md) 中的 Inventory 或 Equippable。

本页组件目前仅面向本地玩家。读取前应确认玩家已经加载；失效时会报告错误，不返回缓存的旧物品。客户端读取本机同步数据，不负责修改服务端背包，也不保证与服务端同一时刻的数据完全一致。

## 一次读取整个背包

```python
from ModSAPI.client.beta import client, ClientEntityComponentTypes

def describe_inventory():
    inventory = client.localPlayer.getComponent(ClientEntityComponentTypes.Inventory)
    items = inventory.container.getItems({"includeUserData": False})
    return [
        (index, stack.typeId, stack.amount)
        for index, stack in enumerate(items)
        if stack is not None
    ]
```

[ClientEntityInventoryComponent](../client/reference/ClientEntityInventoryComponent.md) 的 container 返回 [ClientContainer](../client/reference/ClientContainer.md)。`getItems()` 一次调用原生批量读取，保留槽位顺序，空位置仍为 [None](../common/type-system.md#none)；不要先过滤空位置，再把过滤后的下标当作真实槽位。

`includeUserData` 默认 True，用于读取收纳袋、容器物品等嵌套原生数据。只显示类型和数量时传入 False，可减少数据量。省略的数据不会在之后访问快照时自动补齐。全部选项见 [ClientItemReadOptions](../client/reference/ClientItemReadOptions.md)。

容量由原生列表长度决定，不缓存为固定的三十六格。`size`、`emptySlotsCount`、`firstItem()`、`firstEmptySlot()` 都会查询当前状态；后两项返回槽位下标，未找到时为 [None](../common/type-system.md#none)。

## 单格读取与槽位句柄

```python
def inspect_selected_item():
    player = client.localPlayer
    container = player.getComponent("inventory").container
    selected = player.selectedSlotIndex
    return container.getItem(selected)

def watch_slot_once(index):
    container = client.localPlayer.getComponent("inventory").container
    slot = container.getSlot(index)
    return slot.hasItem(), slot.amount
```

`getItem()` 返回独立的 [ItemStackSnapshot](../common/reference/ItemStackSnapshot.md) 或 [None](../common/type-system.md#none)。完整读取会先用不含 userData 的批量结果检查当前边界，再查询指定槽位；传入 False 时复用边界查询结果，只调用一次原生接口。检查许多格子时优先使用 `getItems()`，不要对每格反复调用 `getItem()`。

[ClientContainerSlot](../client/reference/ClientContainerSlot.md) 是实时读取入口，不是内容快照。空格子仍可为有效槽位，amount 为零；读取空格子的 typeId 会报告错误，应先检查 `hasItem()` 或读取 `getItem()` 的可空结果。容器失效或容量缩小后，旧槽位句柄不能继续越界读取。类型错误、布尔槽位和负数下标会在原生物品读取前报告。

`selectedSlotIndex` 是只读快捷栏下标，范围为零到八。库保留零值；异常原生值不会强制转成有效下标。

## 主副手与装备

```python
from ModSAPI.client.beta import EquipmentSlot

def read_held_item():
    equipment = client.localPlayer.getComponent(ClientEntityComponentTypes.Equippable)
    return equipment.getEquipment(EquipmentSlot.Mainhand)

def describe_equipment():
    equipment = client.localPlayer.getComponent("equippable")
    items = equipment.getEquipmentItems({"includeUserData": False})
    return {slot: None if item is None else item.typeId for slot, item in items.items()}
```

[ClientEntityEquippableComponent](../client/reference/ClientEntityEquippableComponent.md) 使用 [EquipmentSlot](../common/reference/EquipmentSlot.md) 常量。支持 Mainhand、Offhand、Head、Chest、Legs、Feet 六个位置，空位置返回 [None](../common/type-system.md#none)。`getEquipmentSlot()` 返回同样只读的实时槽位句柄。

`getEquipmentItems()` 用一次四格盔甲批量查询和两次手持物查询取得六个位置，避免逐格查询六次。它返回以 [EquipmentSlot](../common/reference/EquipmentSlot.md) 常量为键的字典；这三次原生查询不是事务，不保证跨调用的原子快照。

Body 暂不支持。网易盔甲枚举中的 BODY 表示胸甲，不能直接对应微软 Body 槽；错误槽位不会自动落到头盔或胸甲。库也没有伪造客户端装备写入或尚未核验的完整防御统计。

## 快照、元数据与界面显示

```python
def show_held_item(view):
    stack = read_held_item()
    renderer = view.getControl("/panel/held_item", "itemRenderer")
    renderer.visible = stack is not None
    if stack is not None:
        renderer.setItem(stack)
```

此处需要自己的界面模板，控件用法见 [布局与常用控件](ui-layout-and-widgets.md)。[UiItemRenderer](../ui/reference/UiItemRenderer.md) 可以直接接受 [ItemStackSnapshot](../common/reference/ItemStackSnapshot.md)；无需把它拆回字典。

快照继承通用物品快照行为，包含只读 typeId、amount、auxValue，以及 `clone()`、`withAmount()` 和返回独立副本的 `getItemDict()`。auxValue 是原生变种值，不应一律解释为耐久值。修改副本、克隆或创建新数量的快照都不会改变背包；实际写入应在服务端完成。

原生已有的超量堆叠按实际数量保留，不能悄悄裁剪。`withAmount()` 创建新值时仍按一到二百五十五的范围校验。原生返回 False、字符串、非法数量或缺失必要字段会报告错误，不再把错误数据当作空物品。

## 当前限制与错误

参数错误分别报告 [TypeError](../common/type-system.md#typeerror)、[ValueError](../common/type-system.md#valueerror) 或 [ArgumentOutOfBoundsError](../common/reference/ArgumentOutOfBoundsError.md)。原生异常、损坏的列表或物品数据会转换为 [NativeOperationError](../common/reference/NativeOperationError.md)，保留实际读取操作；SDK 不具备对应方法时报告 [UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)。实体或客户端失效后，缓存的原生代理也不能继续读取。

网易原生接口支持部分其他玩家的装备读取，但本批组件尚未开放该范围，不能把它视为已封装能力；其他玩家的完整背包本就不受客户端查询支持。客户端物品写入、完整装备属性、平台差异和多人同步时序仍待进一步适配或实测。完整待补列表见 [ModSDK 功能映射与待补接口](../modsdk-coverage.md)。