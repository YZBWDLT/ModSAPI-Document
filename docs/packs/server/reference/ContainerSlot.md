---
title: "ContainerSlot"
sidebar_label: "ContainerSlot"
---

# ContainerSlot

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Container.py`；声明补充了静态类型信息。

容器内的一个槽位，例如实体库存中的槽位。

## 获取方式

使用 container.getSlot(index) 取得实时槽位句柄；index 从零开始，空槽仍可能有效。

## 成员索引

| 名称 | 形态 |
| --- | --- |
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

## amount {#amount}

```python
amount: int
```

堆叠中的物品数量。有效输入为 1–255，实际值受物品最大堆叠数限制。

**访问：** 可读写。

写入方式：`instance.amount = value`。参数类型线索：`(value: int) -> None`。

写入参数 `value`：[int](../../common/type-system.md#int)。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Item amount must be an integer between 1 and 255'` |

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

读取当前有效槽位的独立 [ItemStack](../apis/itemStack.md)；空位置返回 [None](../../common/type-system.md#none)。

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
setItem(itemStack: ItemStack | EventItemStack | None = None) -> None
```

替换当前槽位，传入 [None](../../common/type-system.md#none) 清空；恢复不完整时报告错误。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemStack` | [ItemStack](../apis/itemStack.md) \| [EventItemStack](../../common/reference/EventItemStack.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 物品堆叠对象；不是物品名称字符串。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setItem(instance):
    return instance.setItem()
```

## hasItem {#hasItem}

```python
hasItem() -> bool
```

当前有效槽位是否存在非空物品。

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

当前物品的类型标识；空槽读取会报告槽位错误。

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
type: ItemType
```

当前物品的 [ItemType](ItemType.md)；空槽报告 [InvalidContainerSlotError](../../common/reference/InvalidContainerSlotError.md)。

**访问：** 只读。

**返回类型：** [ItemType](ItemType.md)。静态声明不替代本页的实现限制。

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

当前物品的最大数量；槽位必须存在物品。

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
nameTag: str | None
```

当前显示名称或 [None](../../common/type-system.md#none)；新名称最多二百五十五个字符。

**访问：** 可读写。

写入方式：`instance.nameTag = value`。参数类型线索：`(value: str \| None) -> None`。

写入参数 `value`：[str](../../common/type-system.md#str) \| [None](../../common/type-system.md#none)。

**返回类型：** [str](../../common/type-system.md#str) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

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
keepOnDeath: bool
```

当前死亡保留标记；写入要求 [bool](../../common/type-system.md#bool)，槽位必须存在物品。

**访问：** 可读写。

写入方式：`instance.keepOnDeath = value`。参数类型线索：`(value: bool) -> None`。

写入参数 `value`：[bool](../../common/type-system.md#bool)。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

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
lockMode: str
```

当前 [ItemLockMode](../../common/reference/ItemLockMode.md) 值；拒绝未知的锁定模式。

**访问：** 可读写。

写入方式：`instance.lockMode = value`。参数类型线索：`(value: str) -> None`。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

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

从当前槽位物品读取普通文本描述的副本。

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
getRawLore() -> list[dict[str, str]]
```

读取当前物品描述的 RawMessage 文本记录副本。

**返回类型：** [list](../../common/type-system.md#list)[[dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [str](../../common/type-system.md#str)]]。静态声明不替代本页的实现限制。

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

先校验全部普通文本描述，再写回物品。

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

读取当前物品原生定义标签的副本。

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

当前物品定义是否包含指定标签。

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

比较当前物品与 [ItemStack](../apis/itemStack.md)，保留原生元数据参与比较。

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
getDynamicProperty(identifier: str) -> Any
```

读取当前物品属性值的独立副本；缺失时为 [None](../../common/type-system.md#none)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |

**返回类型：** [Any](../../common/type-system.md#any)。静态声明不替代本页的实现限制。

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

读取当前物品属性标识列表的副本。

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
setDynamicProperty(identifier: str, value: Any = None) -> None
```

校验并保存当前物品的一个属性；[None](../../common/type-system.md#none) 删除该属性。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `value` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 需要写入的值，类型、范围及副本语义见本成员说明。 |

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
setDynamicProperties(values: dict[str, Any]) -> None
```

先校验完整属性批次，再写回修改后的物品。

:::note 当前实现说明
先验证完整属性批次，再写回当前物品。保留其他模组的 extraId 和原生标签；写回失败沿用容器恢复错误。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `values` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] | `必填` | 传给 [ContainerSlot.setDynamicProperties](ContainerSlot.md#setDynamicProperties) 的 values 参数；结合上方功能说明和下方调用示例使用。 |

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

清除当前物品的本库属性，保留其他模组的 extraId 数据。

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