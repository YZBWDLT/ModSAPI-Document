---
title: "Container"
sidebar_label: "Container"
---

# Container

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Container.py`；声明补充了静态类型信息。

提供校验读取和写入失败后尽力恢复的服务端容器。

## 获取方式

从玩家、实体或方块的库存组件 container 属性取得。容器和槽位随所属系统及原生对象失效；不要直接构造。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [size](#size) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [getItem](#getItem) | 方法 |
| [getItems](#getItems) | 方法 |
| [emptySlotsCount](#emptySlotsCount) | 只读属性 |
| [firstEmptySlot](#firstEmptySlot) | 方法 |
| [firstItem](#firstItem) | 方法 |
| [getSlot](#getSlot) | 方法 |
| [find](#find) | 方法 |
| [findLast](#findLast) | 方法 |
| [contains](#contains) | 方法 |
| [setItem](#setItem) | 方法 |
| [setItems](#setItems) | 方法 |
| [addItem](#addItem) | 方法 |
| [clearAll](#clearAll) | 方法 |
| [moveItem](#moveItem) | 方法 |
| [swapItems](#swapItems) | 方法 |
| [transferItem](#transferItem) | 方法 |

## size {#size}

```python
size: int
```

读取当前容量；失效容器报告 [InvalidContainerError](../../common/reference/InvalidContainerError.md)。玩家背包使用原生批量列表的长度，个人末影箱为二十七格。SDK 缺少背包批量方法时回退到三十六格。方块与实体容量重新查询，异常值不会被当作空容器。

:::note 当前实现说明
返回当前整数容量；失效时抛出 [InvalidContainerError](../../common/reference/InvalidContainerError.md)，不再返回 [None](../../common/type-system.md#none)。玩家背包原生批量方法缺失时才回退到三十六格；个人末影箱为二十七格。
:::

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.size
```

## isValid {#isValid}

```python
isValid: bool
```

所属会话和原生容器是否仍可使用。明确的原生缺失返回 False，损坏的返回值或缺少的能力仍作为诊断错误报告。

:::note 当前实现说明
明确的对象缺失返回 False；损坏原生值及未适配的特殊容器后端仍会报告错误，不会冒充空箱子。
:::

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## getItem {#getItem}

```python
getItem(slot: int) -> ItemStack | None
```

检查当前槽位边界后读取独立 [ItemStack](itemStack.md) 或 [None](../../common/type-system.md#none)。请求完整原生 userData，异常数据保留实际读取操作，不会被当作空格。

:::note 当前实现说明
返回物品副本，修改后要 setItem 回写；空槽为 [None](../../common/type-system.md#none)。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `slot` | [int](../../common/type-system.md#int) | `必填` | 零起始槽位索引，必须在容器容量内。 |

**返回类型：** [ItemStack](itemStack.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getItem(instance, slot):
    return instance.getItem(slot)
```

## getItems {#getItems}

```python
getItems(options: ContainerReadOptions | None = None) -> list[ItemStack | None]
```

批量读取独立 [ItemStack](itemStack.md)，保留 [None](../../common/type-system.md#none) 和槽位顺序。includeUserData 默认 True；玩家优先使用一次原生批量查询，其他容器在一次容量检查后逐格读取。这些读取不是原生事务。

:::note 当前实现说明
本库批量扩展，保留 [None](../../common/type-system.md#none) 与真实槽位顺序。关闭 includeUserData 的部分结果不应直接用于保留数据的写回。多次原生读取不是事务。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [ContainerReadOptions](../reference/ContainerReadOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [list](../../common/type-system.md#list)[[ItemStack](itemStack.md) \| [None](../../common/type-system.md#none)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getItems(instance):
    return instance.getItems()
```

## emptySlotsCount {#emptySlotsCount}

```python
emptySlotsCount: int
```

使用一次轻量扫描统计空槽；所属对象失效时报告错误。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.emptySlotsCount
```

## firstEmptySlot {#firstEmptySlot}

```python
firstEmptySlot() -> int | None
```

使用一次轻量扫描取得第一个空位置的下标，未找到时为 [None](../../common/type-system.md#none)。

**返回类型：** [int](../../common/type-system.md#int) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_firstEmptySlot(instance):
    return instance.firstEmptySlot()
```

## firstItem {#firstItem}

```python
firstItem() -> int | None
```

使用一次轻量扫描取得第一个有物品的位置下标，未找到时为 [None](../../common/type-system.md#none)。

**返回类型：** [int](../../common/type-system.md#int) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_firstItem(instance):
    return instance.firstItem()
```

## getSlot {#getSlot}

```python
getSlot(slot: int) -> ContainerSlot
```

检查下标及所属对象后返回实时 [ContainerSlot](../reference/ContainerSlot.md) 句柄。

:::note 当前实现说明
返回槽位包装器；支持的属性修改会回写原生容器。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `slot` | [int](../../common/type-system.md#int) | `必填` | 零起始槽位索引，必须在容器容量内。 |

**返回类型：** [ContainerSlot](../reference/ContainerSlot.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getSlot(instance, slot):
    return instance.getSlot(slot)
```

## find {#find}

```python
find(itemStack: ItemStack | EventItemStack) -> int | None
```

查找第一个匹配物品，忽略数量并保留原生元数据参与比较。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemStack` | [ItemStack](itemStack.md) \| [EventItemStack](../../common/reference/EventItemStack.md) | `必填` | 物品堆叠对象；不是物品名称字符串。 |

**返回类型：** [int](../../common/type-system.md#int) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_find(instance, itemStack):
    return instance.find(itemStack)
```

## findLast {#findLast}

```python
findLast(itemStack: ItemStack | EventItemStack) -> int | None
```

使用一次完整原生数据扫描查找最后一个匹配物品。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemStack` | [ItemStack](itemStack.md) \| [EventItemStack](../../common/reference/EventItemStack.md) | `必填` | 物品堆叠对象；不是物品名称字符串。 |

**返回类型：** [int](../../common/type-system.md#int) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_findLast(instance, itemStack):
    return instance.findLast(itemStack)
```

## contains {#contains}

```python
contains(itemStack: ItemStack | EventItemStack) -> bool
```

使用完整原生数据扫描判断是否包含指定物品值。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemStack` | [ItemStack](itemStack.md) \| [EventItemStack](../../common/reference/EventItemStack.md) | `必填` | 物品堆叠对象；不是物品名称字符串。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_contains(instance, itemStack):
    return instance.contains(itemStack)
```

## setItem {#setItem}

```python
setItem(slot: int, itemStack: ItemStack | EventItemStack | None = None) -> None
```

替换一个槽位；只有 itemStack 为 [None](../../common/type-system.md#none) 时清空，返回 [None](../../common/type-system.md#none)。接受服务端 [ItemStack](itemStack.md) 和独立物品快照。失败会读回并尽力恢复原内容；仍无法确认恢复时抛出带诊断信息的 [ContainerRollbackError](../../common/reference/ContainerRollbackError.md)。

:::note 当前实现说明
返回 [None](../../common/type-system.md#none)。仅 [None](../../common/type-system.md#none) 表示清空；其他非法空值明确拒绝。失败会核对并尝试恢复，恢复不完整时抛出 [ContainerRollbackError](../../common/reference/ContainerRollbackError.md)。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `slot` | [int](../../common/type-system.md#int) | `必填` | 零起始槽位索引，必须在容器容量内。 |
| `itemStack` | [ItemStack](itemStack.md) \| [EventItemStack](../../common/reference/EventItemStack.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 物品堆叠对象；不是物品名称字符串。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setItem(instance, slot):
    return instance.setItem(slot)
```

## setItems {#setItems}

```python
setItems(items: dict[int, ItemStack | EventItemStack | None]) -> None
```

按槽位到物品的字典替换指定位置，[None](../../common/type-system.md#none) 清空。完整复制与校验输入后才查询引擎；玩家背包优先使用一次原生批量写入，缺少批量能力或其他容器使用逐格写入。逐槽结果为 False、缺失或损坏时视为失败；即使原生已经部分改动，也会核对并恢复所有已尝试槽位，恢复不完整时报告 [ContainerRollbackError](../../common/reference/ContainerRollbackError.md)。

:::note 当前实现说明
本库批量扩展：只修改字典中的槽位。先校验整批参数，玩家优先一次原生批量写入并逐槽检查返回值；失败核对并恢复所有请求槽位，不承诺原子事务。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `items` | [dict](../../common/type-system.md#dict)[[int](../../common/type-system.md#int), [ItemStack](itemStack.md) \| [EventItemStack](../../common/reference/EventItemStack.md) \| [None](../../common/type-system.md#none)] | `必填` | 下拉选项集合；标准构建器使用文本列表，[CustomForm](../../server_ui/reference/CustomForm.md) 使用 label/value 字典列表。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'items must be a slot-to-item dictionary'` |
| [InvalidContainerSlotError](../../common/reference/InvalidContainerSlotError.md) | `'A batch slot is outside the current container bounds'` |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'SetPlayerAllItems'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setItems(instance, items):
    return instance.setItems(items)
```

## addItem {#addItem}

```python
addItem(itemStack: ItemStack | EventItemStack | None) -> ItemStack | None
```

插入输入物品的副本，仅对空间不足返回余量。对有效容器传入 [None](../../common/type-system.md#none) 保持兼容的空操作；原生失败是错误，不代表空间不足。失败后尝试恢复所有已触及的槽位，恢复不完整时报告 [ContainerRollbackError](../../common/reference/ContainerRollbackError.md)。

:::note 当前实现说明
返回因容量不足未能放入的剩余 [ItemStack](itemStack.md)，全部放入时为 [None](../../common/type-system.md#none)。原生写入失败会报告错误并尝试恢复，不会冒充空间不足。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemStack` | [ItemStack](itemStack.md) \| [EventItemStack](../../common/reference/EventItemStack.md) \| [None](../../common/type-system.md#none) | `必填` | 物品堆叠对象；不是物品名称字符串。 |

**返回类型：** [ItemStack](itemStack.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addItem(instance, itemStack):
    return instance.addItem(itemStack)
```

## clearAll {#clearAll}

```python
clearAll() -> None
```

清空有物品的槽位；原生写入失败时尽力恢复。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clearAll(instance):
    return instance.clearAll()
```

## moveItem {#moveItem}

```python
moveItem(fromSlot: int, toSlot: int, toContainer: Container | None = None) -> None
```

移动到经过校验的目标槽位；失败后尝试恢复两个已触及的槽位。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fromSlot` | [int](../../common/type-system.md#int) | `必填` | 传给 [Container.moveItem](container.md#moveItem) 的 fromSlot 参数；结合上方功能说明和下方调用示例使用。 |
| `toSlot` | [int](../../common/type-system.md#int) | `必填` | 传给 [Container.moveItem](container.md#moveItem) 的 toSlot 参数；结合上方功能说明和下方调用示例使用。 |
| `toContainer` | [Container](container.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Container.moveItem](container.md#moveItem) 的 toContainer 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_moveItem(instance, fromSlot, toSlot):
    return instance.moveItem(fromSlot, toSlot)
```

## swapItems {#swapItems}

```python
swapItems(slot: int, otherSlot: int, otherContainer: Container | None = None) -> None
```

交换经过校验的两个槽位，保留最初故障和恢复结果。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `slot` | [int](../../common/type-system.md#int) | `必填` | 零起始槽位索引，必须在容器容量内。 |
| `otherSlot` | [int](../../common/type-system.md#int) | `必填` | 传给 [Container.swapItems](container.md#swapItems) 的 otherSlot 参数；结合上方功能说明和下方调用示例使用。 |
| `otherContainer` | [Container](container.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Container.swapItems](container.md#swapItems) 的 otherContainer 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_swapItems(instance, slot, otherSlot):
    return instance.swapItems(slot, otherSlot)
```

## transferItem {#transferItem}

```python
transferItem(fromSlot: int, toContainer: Container | None) -> ItemStack | None
```

转移到可用槽位，也可转移到当前容器的其他位置。返回尚未转入的余量或 [None](../../common/type-system.md#none)；同容器转移跳过来源格。原生失败时恢复所有已触及的写入，多次读写不是原生事务。

:::note 当前实现说明
同容器转移跳过来源格，返回尚未转入的余量或 [None](../../common/type-system.md#none)。多次读写不是原生事务，不能保证其他模组不会在中途改变内容。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fromSlot` | [int](../../common/type-system.md#int) | `必填` | 传给 [Container.transferItem](container.md#transferItem) 的 fromSlot 参数；结合上方功能说明和下方调用示例使用。 |
| `toContainer` | [Container](container.md) \| [None](../../common/type-system.md#none) | `必填` | 传给 [Container.transferItem](container.md#transferItem) 的 toContainer 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ItemStack](itemStack.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_transferItem(instance, fromSlot, toContainer):
    return instance.transferItem(fromSlot, toContainer)
```

## 使用示例


```python
from ModSAPI.server.beta import world, ItemStack

for player in world.getAllPlayers():
    inventory = player.getComponent("minecraft:inventory")
    if inventory is not None and inventory.container.isValid:
        remaining = inventory.container.addItem(ItemStack("minecraft:apple", 1))
        print(remaining)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)