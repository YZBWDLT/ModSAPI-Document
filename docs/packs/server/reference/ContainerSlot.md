---
title: "ContainerSlot"
sidebar_label: "ContainerSlot"
---

# ContainerSlot

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Container.py`；声明补充了静态类型信息。

容器内的一个槽位，例如实体库存中的槽位。

## 获取方式

使用 `container.getSlot(index)`，index 从零开始。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [amount](#amount) | 可读写属性 |
| [isStackable](#isStackable) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [getItem](#getItem) | 方法 |
| [setItem](#setItem) | 方法 |
| [hasItem](#hasItem) | 方法 |
| [typeId](#typeId) | 只读属性 |
| [type](#type) | 只读属性 |
| [maxAmount](#maxAmount) | 只读属性 |
| [nameTag](#nameTag) | 可读写属性 |
| [keepOnDeath](#keepOnDeath) | 可读写属性 |
| [lockMode](#lockMode) | 可读写属性 |
| [getLore](#getLore) | 方法 |
| [getRawLore](#getRawLore) | 方法 |
| [setLore](#setLore) | 方法 |
| [getTags](#getTags) | 方法 |
| [hasTag](#hasTag) | 方法 |
| [isStackableWith](#isStackableWith) | 方法 |
| [getDynamicProperty](#getDynamicProperty) | 方法 |
| [getDynamicPropertyIds](#getDynamicPropertyIds) | 方法 |
| [setDynamicProperty](#setDynamicProperty) | 方法 |
| [setDynamicProperties](#setDynamicProperties) | 方法 |
| [clearDynamicProperties](#clearDynamicProperties) | 方法 |

## 构造器 {#constructor}

```python
ContainerSlot(container: Container, slotId: int) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `container` | [Container](../apis/container.md) | `必填` | 传给 [ContainerSlot.__init__](ContainerSlot.md#constructor) 的 container 参数；结合上方功能说明和下方调用示例使用。 |
| `slotId` | [int](../../common/type-system.md#int) | `必填` | 传给 [ContainerSlot.__init__](ContainerSlot.md#constructor) 的 slotId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## amount {#amount}

```python
amount: int
```

堆叠中的物品数量。有效输入为 1–255，实际值受物品最大堆叠数限制。

**访问：** 可读写。

写入方式：`instance.amount = value`。参数类型线索：`(value: int)`。

写入参数 `value`：[int](../../common/type-system.md#int)。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.amount

def write_value(instance, value):
    instance.amount = value
```

## isStackable {#isStackable}

```python
isStackable: bool
```

物品是否可堆叠。最大堆叠数大于一，且不含自定义数据或属性时，视为可堆叠。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isStackable
```

## isValid {#isValid}

```python
isValid: bool
```

槽位是否有效：所属容器须存在且已加载，槽位索引也须有效。

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
getItem() -> ItemStack | None
```

读取此槽位的 [ItemStack](../apis/itemStack.md)；槽位为空时返回 [None](../../common/type-system.md#none)。

**返回类型：** [ItemStack](../apis/itemStack.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getItem(instance):
    return instance.getItem()
```

## setItem {#setItem}

```python
setItem(itemStack: ItemStack | None)
```

设置此槽位的 [ItemStack](../apis/itemStack.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemStack` | [ItemStack](../apis/itemStack.md) \| [None](../../common/type-system.md#none) | `必填` | 物品堆叠对象；不是物品名称字符串。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setItem(instance, itemStack):
    return instance.setItem(itemStack)
```

## hasItem {#hasItem}

```python
hasItem() -> bool
```

检查 `hasItem` 操作。参数形态和结果约定如下。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasItem(instance):
    return instance.hasItem()
```

## typeId {#typeId}

```python
typeId: str
```

读取 `typeId` 的当前值。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## type {#type}

```python
type
```

读取 [type](../../common/type-system.md#type) 的当前值。

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.type
```

## maxAmount {#maxAmount}

```python
maxAmount: int
```

读取 `maxAmount` 的当前值。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.maxAmount
```

## nameTag {#nameTag}

```python
nameTag
```

读取 `nameTag` 的当前值。

**访问：** 可读写。

写入方式：`instance.nameTag = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.nameTag

def write_value(instance, value):
    instance.nameTag = value
```

## keepOnDeath {#keepOnDeath}

```python
keepOnDeath
```

读取 `keepOnDeath` 的当前值。

**访问：** 可读写。

写入方式：`instance.keepOnDeath = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.keepOnDeath

def write_value(instance, value):
    instance.keepOnDeath = value
```

## lockMode {#lockMode}

```python
lockMode
```

读取 `lockMode` 的当前值。

**访问：** 可读写。

写入方式：`instance.lockMode = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.lockMode

def write_value(instance, value):
    instance.lockMode = value
```

## getLore {#getLore}

```python
getLore() -> list[str]
```

读取 `getLore` 操作。参数形态和结果约定如下。

**返回类型：** [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getLore(instance):
    return instance.getLore()
```

## getRawLore {#getRawLore}

```python
getRawLore() -> list[dict]
```

读取 `getRawLore` 操作。参数形态和结果约定如下。

**返回类型：** [list](../../common/type-system.md#list)[[dict](../../common/type-system.md#dict)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getRawLore(instance):
    return instance.getRawLore()
```

## setLore {#setLore}

```python
setLore(loreList: list[str] | None = None) -> None
```

设置 `setLore` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `loreList` | [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)] \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [ContainerSlot.setLore](ContainerSlot.md#setLore) 的 loreList 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setLore(instance):
    return instance.setLore()
```

## getTags {#getTags}

```python
getTags() -> list[str]
```

读取 `getTags` 操作。参数形态和结果约定如下。

**返回类型：** [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getTags(instance):
    return instance.getTags()
```

## hasTag {#hasTag}

```python
hasTag(tag: str) -> bool
```

检查 `hasTag` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `tag` | [str](../../common/type-system.md#str) | `必填` | 传给 [ContainerSlot.hasTag](ContainerSlot.md#hasTag) 的 tag 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasTag(instance, tag):
    return instance.hasTag(tag)
```

## isStackableWith {#isStackableWith}

```python
isStackableWith(itemStack: ItemStack) -> bool
```

检查 `isStackableWith` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemStack` | [ItemStack](../apis/itemStack.md) | `必填` | 物品堆叠对象；不是物品名称字符串。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_isStackableWith(instance, itemStack):
    return instance.isStackableWith(itemStack)
```

## getDynamicProperty {#getDynamicProperty}

```python
getDynamicProperty(identifier: str)
```

读取 `getDynamicProperty` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDynamicProperty(instance, identifier):
    return instance.getDynamicProperty(identifier)
```

## getDynamicPropertyIds {#getDynamicPropertyIds}

```python
getDynamicPropertyIds() -> list[str]
```

读取 `getDynamicPropertyIds` 操作。参数形态和结果约定如下。

**返回类型：** [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDynamicPropertyIds(instance):
    return instance.getDynamicPropertyIds()
```

## setDynamicProperty {#setDynamicProperty}

```python
setDynamicProperty(identifier: str, value = None) -> None
```

设置 `setDynamicProperty` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `value` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setDynamicProperty(instance, identifier):
    return instance.setDynamicProperty(identifier)
```

## setDynamicProperties {#setDynamicProperties}

```python
setDynamicProperties(values: dict) -> None
```

设置 `setDynamicProperties` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `values` | [dict](../../common/type-system.md#dict) | `必填` | 传给 [ContainerSlot.setDynamicProperties](ContainerSlot.md#setDynamicProperties) 的 values 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setDynamicProperties(instance, values):
    return instance.setDynamicProperties(values)
```

## clearDynamicProperties {#clearDynamicProperties}

```python
clearDynamicProperties() -> None
```

移除或清理 `clearDynamicProperties` 操作。参数形态和结果约定如下。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clearDynamicProperties(instance):
    return instance.clearDynamicProperties()
```

## 使用示例


```python
from ModSAPI.server.beta import world

for player in world.getAllPlayers():
    inventory = player.getComponent("minecraft:inventory")
    if inventory is not None:
        slot = inventory.container.getSlot(0)
        item = slot.getItem()
        if item is not None:
            print(item.typeId)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)