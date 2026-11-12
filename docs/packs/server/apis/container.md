---
title: "Container"
sidebar_label: "Container"
---

# Container

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Container.py`；声明补充了静态类型信息。

容纳多组物品的容器，可属于玩家、运输矿车、羊驼等实体。

## 获取方式

从实体/方块的库存组件读取 container。不要直接构造与引擎脱离的容器。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [emptySlotsCount](#emptySlotsCount) | 只读属性 |
| [size](#size) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [addItem](#addItem) | 方法 |
| [clearAll](#clearAll) | 方法 |
| [getSlot](#getSlot) | 方法 |
| [firstEmptySlot](#firstEmptySlot) | 方法 |
| [firstItem](#firstItem) | 方法 |
| [find](#find) | 方法 |
| [findLast](#findLast) | 方法 |
| [contains](#contains) | 方法 |
| [getItem](#getItem) | 方法 |
| [moveItem](#moveItem) | 方法 |
| [setItem](#setItem) | 方法 |
| [swapItems](#swapItems) | 方法 |
| [transferItem](#transferItem) | 方法 |

## 构造器 {#constructor}

```python
Container(location: tuple = None, entityId: str = None, dimId: int = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [tuple](../../common/type-system.md#tuple) | [None](../../common/type-system.md#none) | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `entityId` | [str](../../common/type-system.md#str) | [None](../../common/type-system.md#none) | 实体运行 ID；跨回调使用前重新确认实体有效性。 |
| `dimId` | [int](../../common/type-system.md#int) | [None](../../common/type-system.md#none) | 传给 [Container.__init__](container.md#constructor) 的 dimId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEngineTypeStr`。

## emptySlotsCount {#emptySlotsCount}

```python
emptySlotsCount: int
```

容器中空槽位的数量。容器无效时返回 [None](../../common/type-system.md#none)。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLevelId`, `GetPlayerItem`, `GetEntityItem`, `GetContainerItem`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.emptySlotsCount
```

## size {#size}

```python
size: int | None
```

容器的槽位总数。例如单个箱子为 27；玩家库存为 36，包括 9 个快捷栏槽位和 27 个背包槽位。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBlockNew`, `GetContainerSize`, `GetLevelId`, `GetComponents`。

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

容器及其关联实体或方块是否仍可在当前上下文中使用。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsEntityAlive`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## addItem {#addItem}

```python
addItem(itemStack: ItemStack) -> ItemStack | None
```

添加物品堆叠的副本，返回无法放入的剩余部分。

:::note 当前实现说明
返回未能放入的剩余 [ItemStack](itemStack.md)；全部放入时为 [None](../../common/type-system.md#none)。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemStack` | [ItemStack](itemStack.md) | `必填` | 物品堆叠对象；不是物品名称字符串。 |

**返回类型：** [ItemStack](itemStack.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Container is no longer available'` |

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

通过开发包清空容器，同时更新引擎库存状态。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Container is no longer available'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clearAll(instance):
    return instance.clearAll()
```

## getSlot {#getSlot}

```python
getSlot(slot: int) -> ContainerSlot
```

读取 `getSlot` 操作。参数形态和结果约定如下。

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

## firstEmptySlot {#firstEmptySlot}

```python
firstEmptySlot() -> int | None
```

执行 `firstEmptySlot` 操作。参数形态和结果约定如下。

**返回类型：** [int](../../common/type-system.md#int) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Container is no longer available'` |

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

执行 `firstItem` 操作。参数形态和结果约定如下。

**返回类型：** [int](../../common/type-system.md#int) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Container is no longer available'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_firstItem(instance):
    return instance.firstItem()
```

## find {#find}

```python
find(itemStack: ItemStack) -> int | None
```

执行 `find` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemStack` | [ItemStack](itemStack.md) | `必填` | 物品堆叠对象；不是物品名称字符串。 |

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
findLast(itemStack: ItemStack) -> int | None
```

执行 `findLast` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemStack` | [ItemStack](itemStack.md) | `必填` | 物品堆叠对象；不是物品名称字符串。 |

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
contains(itemStack: ItemStack) -> bool
```

检查 `contains` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemStack` | [ItemStack](itemStack.md) | `必填` | 物品堆叠对象；不是物品名称字符串。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_contains(instance, itemStack):
    return instance.contains(itemStack)
```

## getItem {#getItem}

```python
getItem(slot: int) -> ItemStack | None
```

读取指定槽位的 [ItemStack](itemStack.md)；空槽位返回 [None](../../common/type-system.md#none)。读取不会修改或清空槽位。需要槽位引用时使用 [Container.getSlot](container.md#getSlot)。

:::note 当前实现说明
返回物品副本，修改后要 setItem 回写；空槽为 [None](../../common/type-system.md#none)。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `slot` | [int](../../common/type-system.md#int) | `必填` | 零起始槽位索引，必须在容器容量内。 |

**返回类型：** [ItemStack](itemStack.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerItem`, `GetLevelId`, `GetEntityItem`, `GetContainerItem`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getItem(instance, slot):
    return instance.getItem(slot)
```

## moveItem {#moveItem}

```python
moveItem(fromSlot: int, toSlot: int, toContainer: Container = None) -> None
```

将物品从一个槽位移至另一个槽位，可以跨容器操作。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fromSlot` | [int](../../common/type-system.md#int) | `必填` | 传给 [Container.moveItem](container.md#moveItem) 的 fromSlot 参数；结合上方功能说明和下方调用示例使用。 |
| `toSlot` | [int](../../common/type-system.md#int) | `必填` | 传给 [Container.moveItem](container.md#moveItem) 的 toSlot 参数；结合上方功能说明和下方调用示例使用。 |
| `toContainer` | [Container](container.md) | [None](../../common/type-system.md#none) | 传给 [Container.moveItem](container.md#moveItem) 的 toContainer 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_moveItem(instance, fromSlot, toSlot):
    return instance.moveItem(fromSlot, toSlot)
```

## setItem {#setItem}

```python
setItem(slot: int, itemStack: ItemStack = None) -> None
```

设置指定槽位的物品堆叠。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `slot` | [int](../../common/type-system.md#int) | `必填` | 零起始槽位索引，必须在容器容量内。 |
| `itemStack` | [ItemStack](itemStack.md) | [None](../../common/type-system.md#none) | 物品堆叠对象；不是物品名称字符串。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Could not write inventory slot'` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Could not write container slot'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetInvItemNum`, `SpawnItemToPlayerInv`, `SetEntityItem`, `GetLevelId`, `SpawnItemToContainer`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setItem(instance, slot):
    return instance.setItem(slot)
```

## swapItems {#swapItems}

```python
swapItems(slot: int, otherSlot: int, otherContainer: Container = None) -> None
```

交换两个容器槽位中的物品。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `slot` | [int](../../common/type-system.md#int) | `必填` | 零起始槽位索引，必须在容器容量内。 |
| `otherSlot` | [int](../../common/type-system.md#int) | `必填` | 传给 [Container.swapItems](container.md#swapItems) 的 otherSlot 参数；结合上方功能说明和下方调用示例使用。 |
| `otherContainer` | [Container](container.md) | [None](../../common/type-system.md#none) | 传给 [Container.swapItems](container.md#swapItems) 的 otherContainer 参数；结合上方功能说明和下方调用示例使用。 |

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
transferItem(fromSlot: int, toContainer: Container) -> ItemStack
```

将物品移至其他容器，或当前容器中首个可用槽位。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fromSlot` | [int](../../common/type-system.md#int) | `必填` | 传给 [Container.transferItem](container.md#transferItem) 的 fromSlot 参数；结合上方功能说明和下方调用示例使用。 |
| `toContainer` | [Container](container.md) | `必填` | 传给 [Container.transferItem](container.md#transferItem) 的 toContainer 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ItemStack](itemStack.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Destination container is no longer available'` |

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