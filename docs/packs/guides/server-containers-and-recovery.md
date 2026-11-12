---
title: 服务端容器与物品数据
---

# 服务端容器与物品数据

通过玩家、实体或方块的库存组件取得 [Container](../server/apis/container.md)，通过 `getSlot()` 取得 [ContainerSlot](../server/reference/ContainerSlot.md)。容器和槽位是实时入口；[ItemStack](../server/apis/itemStack.md) 则是独立物品值。修改读取到的物品后，需要明确写回槽位才会生效。

## 取得容器并读取多格

```python
from ModSAPI.server.beta import world

def describe_inventory(player):
    inventory = player.getComponent("inventory")
    if inventory is None:
        return []
    container = inventory.container
    values = container.getItems({"includeUserData": False})
    return [(index, item.typeId, item.amount)
            for index, item in enumerate(values) if item is not None]

def get_chest_container(dimension, location):
    block = dimension.getBlock(location)
    if block is None:
        return None
    inventory = block.getComponent("inventory")
    return None if inventory is None else inventory.container
```

`getItems()` 保留真实槽位顺序和空位置的 [None](../common/type-system.md#none)。玩家背包优先使用一次原生批量读取；其他容器在一次容量校验后逐格读取。`emptySlotsCount`、`firstItem()`、`firstEmptySlot()` 使用轻量扫描，不为统计用途创建完整物品组件。后两项返回下标，未找到时为 [None](../common/type-system.md#none)。

[ContainerReadOptions](../server/reference/ContainerReadOptions.md) 的 includeUserData 默认 True。只显示类型和数量时可以关闭，减少嵌套数据；这种结果是有意省略元数据的物品值，不能直接写回原槽位以保留全部内容。需要编辑时重新使用完整的 `getItem()` 或默认 `getItems()`。

`size` 查询当前容量，玩家采用原生列表长度；只有旧版 SDK 完全缺少批量方法时才回退到三十六格。原生方法存在但返回异常值时会报告错误，不走回退。方块或实体容量也不缓存为永久值。

容器失效时 `isValid` 返回 False，`size`、`emptySlotsCount` 以及读写操作报告 [InvalidContainerError](../common/reference/InvalidContainerError.md)。原生返回损坏数据时仍报告 [NativeOperationError](../common/reference/NativeOperationError.md)，不会把故障当作空容器。所属系统销毁或世界切换后，旧容器不能继续访问。

## 编辑与清空

```python
from ModSAPI.server.beta import ItemStack

def rename_first_item(container):
    item = container.getItem(0)
    if item is None:
        return False
    item.nameTag = u"纪念物品"
    item.setLore([u"通过活动获得", u"请妥善保管"])
    container.setItem(0, item)
    return True

def give_reward(container):
    remaining = container.addItem(ItemStack("minecraft:diamond", 3))
    return remaining

def clear_first_slot(container):
    container.setItem(0)
```

`setItem()` 返回 [None](../common/type-system.md#none)；只有 [None](../common/type-system.md#none) 表示清空，False、零、空字符串、字典或列表都不是清空命令。也可以写入 [EventItemStack](../common/reference/EventItemStack.md) 或其子类 [ItemStackSnapshot](../common/reference/ItemStackSnapshot.md)，输入会复制后传给原生接口。

`addItem()` 全部放入时返回 [None](../common/type-system.md#none)，空间不足时返回尚未放入的 [ItemStack](../server/apis/itemStack.md)；原生写入失败会抛出错误，不会冒充“背包已满”。输入物品不会被扣除数量。兼容的 `addItem(None)` 对有效容器不执行写入。

`moveItem()` 按目标槽覆盖，`swapItems()` 交换两格；省略目标容器时使用当前容器。同格操作仍检查有效性和下标。`transferItem()` 按可用空间放入并返回余量，也支持传入当前容器，此时跳过来源格，避免重复计入来源内容。

`find()`、`findLast()` 和 `contains()` 比较物品类型及完整原生元数据，忽略数量。名称、附加值、附魔、描述或自定义数据不同的物品不会被仅按类型误认为相同。

## 同时修改多格

```python
def replace_reward_slots(player):
    player.container.setItems({
        0: ItemStack("minecraft:diamond", 3),
        1: None,
        2: ItemStack("minecraft:apple", 8),
    })
```

`setItems()` 是本库扩展，接收槽位下标到物品值的字典。只有列出的槽位会被替换；[None](../common/type-system.md#none) 清空，返回 [None](../common/type-system.md#none)。整批参数先复制并校验，非法物品、布尔下标或越界位置不会造成前面几格已经写入的情况。空字典不执行写入，但仍会检查容器是否可用。

玩家背包优先使用一次原生批量写入，修改前复用一次完整批量读取取得请求槽位的原内容；没有请求的槽位不创建物品组件。SDK 完全缺少批量写入方法时，才改用逐格写入。方块、实体和末影箱沿用各自的逐格后端。

原生批量结果会逐槽检查：False、缺失状态、非法状态类型或不属于本次请求的键，都视为失败。即使原生方法抛出异常或返回失败，它也可能已经修改了一部分内容，因此所有请求槽位都会纳入恢复核对。恢复不完整时沿用下文的 [ContainerRollbackError](../common/reference/ContainerRollbackError.md)。一次原生批量调用仍不等于事务，不能据此承诺跨模组隔离。

## 个人末影箱

```python
def store_reward_in_ender_chest(player):
    storage = player.enderChest
    remaining = storage.addItem(ItemStack("minecraft:diamond", 1))
    return remaining

def move_first_slot_to_ender_chest(player):
    player.container.moveItem(0, 0, player.enderChest)
```

[Player.enderChest](../server/apis/player.md#enderChest) 返回同一个玩家绑定的 [Container](../server/apis/container.md) 句柄，容量为二十七格。无需提供末影箱方块的位置，不能从世界中某个末影箱方块推断它属于哪个玩家。

读取、槽位句柄、添加、转移、交换、清空、批量设置以及失败恢复都沿用同一组容器方法。末影箱和背包的相同下标是不同槽位，不会把 `moveItem(0, 0, player.enderChest)` 错判为同格空操作。末影箱读取包含 userData 的选择；全部读取需要逐格查询，不伪称一次原生批量快照。

句柄按需创建并缓存，操作时重新检查玩家、所属会话和在线状态。玩家断开后不能继续读取；损坏的在线列表或物品数据仍报告真实原生错误。

## 快捷栏与主手

```python
def select_first_hotbar_slot(player):
    player.selectedSlotIndex = 0
    return player.mainHand
```

[Player.selectedSlotIndex](../server/apis/player.md#selectedSlotIndex) 可在服务端读取和设置零到八的快捷栏位置。零不会被当作未提供；布尔值、浮点数、字符串和越界下标都拒绝。读取到原生错误标记时保留 GetSelectSlotId 操作名称，设置失败保留 ChangeSelectSlot，不再静默忽略失败。

[Player.mainHand](../server/apis/player.md#mainHand) 返回当前选中槽位的独立 [ItemStack](../server/apis/itemStack.md) 或 [None](../common/type-system.md#none)；设置 [None](../common/type-system.md#none) 清空该位置。读取和写入都会使用经过校验的当前快捷栏下标。

## 实时槽位

```python
def mark_current_item(container):
    slot = container.getSlot(0)
    if not slot.hasItem():
        return False
    slot.setDynamicProperty("demo:marked", True)
    slot.keepOnDeath = True
    return True
```

槽位方法每次读取当前内容，修改方法会写回；不会长期保存之前读取到的物品。空位置可以是有效槽位，`amount` 返回零、`isStackable` 返回 False；读取类型、名称、描述或动态属性，以及修改空槽物品字段，会报告 [InvalidContainerSlotError](../common/reference/InvalidContainerSlotError.md)。应先用 `hasItem()` 或处理 `getItem()` 的可空结果。

下标必须为非负整数，布尔值不能代替下标；容量缩小后旧句柄也不能越界使用。[InvalidContainerSlotError](../common/reference/InvalidContainerSlotError.md) 同时属于 Python 的 [IndexError](../common/type-system.md#indexerror)，可按公共错误类型或索引错误处理。

## 写入失败与恢复

```python
from ModSAPI.server.beta import ContainerRollbackError, NativeOperationError

def move_with_diagnostics(source, destination):
    try:
        source.moveItem(0, 0, destination)
        return {"ok": True}
    except ContainerRollbackError as error:
        return {
            "ok": False,
            "operation": error.operation,
            "cause": error.cause,
            "unresolved": [(entry.container, entry.slotIndex, entry.cause)
                           for entry in error.failures],
        }
    except NativeOperationError as error:
        return {"ok": False, "nativeOperation": error.operation, "cause": error.cause}
```

写入前会保存各受影响槽位的原内容。即使第一次原生写入返回失败，也会检查并尝试恢复，因为引擎可能已经部分改动。批量添加、清空、移动、交换和转移失败时，恢复会按反向顺序继续尝试所有已触及的槽位，并读回核对。

全部恢复成功时重新抛出原始故障；恢复仍不完整时抛出 [ContainerRollbackError](../common/reference/ContainerRollbackError.md)。其 cause 保留最初的写入故障，failures 是只读的 [ContainerRollbackFailure](../common/reference/ContainerRollbackFailure.md) 记录元组，包含容器对象、slotIndex 和各自的恢复故障。槽位下标在这里是定位诊断，不需要再次访问可能已经失效的槽位。

这不是原生事务。多次读取或写入之间，其他监听、玩法逻辑或引擎状态仍可能变化；来源内容在目标写入后变动时会报告错误，不能保证跨模组隔离或绝对原子性。恢复也可能失败，应根据诊断进行后续核对，不应无条件重试整个转移并假定物品未移动。

## 名称、描述和数量

公开编辑会先校验完整输入：nameTag 最多二百五十五个字符，[None](../common/type-system.md#none) 或空字符串移除名称；keepOnDeath 仅接受 [bool](../common/type-system.md#bool)；lockMode 使用 [ItemLockMode](../common/reference/ItemLockMode.md) 的 none、inventory 或 slot。

`setLore()` 支持最多二十行普通文本，每行最多五十个字符；[None](../common/type-system.md#none)、空字符串或空列表清空。中文按字符计数，Python 2 字节串按 UTF-8 解析。当前尚不支持写入完整 [RawMessage 格式](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/rawmessage?view=minecraft-bedrock-stable)；`getRawLore()` 只返回 text 记录。非法替换不会先破坏已有名称或描述。

新建或编辑 amount 时校验一到二百五十五，并按物品类型的最大数量限制；读取和克隆原生已有的超量堆叠、超长名称或描述时保留已有内容，不悄悄裁剪造成数据损失。

## 动态属性与其他模组的数据

```python
from ModSAPI.server.beta import Vector3

def write_item_properties(container):
    item = container.getItem(0)
    if item is None:
        return False
    item.setDynamicProperties({
        "demo:uses": 0,
        "demo:enabled": False,
        "demo:origin": Vector3((1, 64, 2)),
        "demo:details": {"visits": [1, 2]},
    })
    container.setItem(0, item)
    return True
```

支持字符串、布尔值、有限数字和 [Vector3](../server/extra/vector.md)；字典与列表是本库扩展，用于嵌套的可序列化数据。[None](../common/type-system.md#none) 删除对应属性，零和 False 都会保留。读取值和写入输入会复制，批量写入会在修改任何属性前校验整批内容。

属性存入本库独立的原生标签，不再占用其他模组的 extraId。普通读取和克隆保留原始数据；旧格式的字面字典可以兼容读取，首次显式修改时写入独立标签。清空旧属性也会保留 extraId 原文，并用独立标记避免下次克隆重新读回已经清空的旧值。其他模组的标签和不透明 extraId 不会被删除。

本库自定义属性的版本化载荷最多为三万二千七百六十七个 UTF-8 字节，包含键和值及格式开销；这是适配器限制，不是微软原生存储大小的等价计量。循环引用、超过三十二层的嵌套、不支持的对象、无穷值和非法编码都会拒绝。损坏的本库标签报告 [StorageDataError](../common/reference/StorageDataError.md)，不会自动清空或覆盖。

这一机制是网易原生物品数据适配，不能据此承诺与微软所有可堆叠物品限制、存档持久化和第三方处理链完全等价。添加自定义数据后，本库将物品视为不可自动堆叠。自定义标签的实机保存、跨版本迁移和多人同步仍待实测。

## 尚未提供的能力

熔炉、烟熏炉、高炉和酿造台尚未接入统一的全槽容器后端。网易为它们提供专用接口，不能套用通用箱子读写并把无结果当作空槽；当前会明确报告 [UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)。合成界面和网易共享临时槽位也尚未作为普通容器开放，它们的上下文、槽位限制和原物品回退规则需要另行适配。

容器规则、重量、虚拟容器、完整冒险模式放置与破坏限制，以及原生动态属性总字节计量尚未完成可靠适配。当前没有伪造这些值；完整差异见 [接口覆盖与待补能力](../compatibility.md) 和 [ModSDK 功能映射](../modsdk-coverage.md)。

接口对照：[微软容器文档](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/container?view=minecraft-bedrock-stable)、[微软物品文档](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/itemstack?view=minecraft-bedrock-stable)。本页所述错误恢复、批量读取和 JSON 属性属于本库适配行为。