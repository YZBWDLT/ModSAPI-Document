---
title: "ItemStack"
sidebar_label: "ItemStack"
---

# ItemStack

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/ItemStack.py`；声明补充了静态类型信息。

一组同类物品的堆叠。

## 获取方式

从服务端入口导入 [ItemStack](itemStack.md)，或从容器读取物品副本。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `keepOnDeath` | 由运行时值确定 | `` |  |
| `lockMode` | 由运行时值确定 | [ItemLockMode.none](../../common/reference/ItemLockMode.md#字段与常量) |  |
| `nameTag` | 由运行时值确定 | `` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [typeId](#typeId) | 只读属性 |
| [amount](#amount) | 可读写属性 |
| [isStackable](#isStackable) | 只读属性 |
| [type](#type) | 只读属性 |
| [maxAmount](#maxAmount) | 只读属性 |
| [getItemDict](#getItemDict) | 方法 |
| [clone](#clone) | 方法 |
| [isStackableWith](#isStackableWith) | 方法 |
| [getLore](#getLore) | 方法 |
| [setLore](#setLore) | 方法 |
| [hasComponent](#hasComponent) | 方法 |
| [getComponent](#getComponent) | 方法 |
| [getDynamicProperty](#getDynamicProperty) | 方法 |
| [clearDynamicProperties](#clearDynamicProperties) | 方法 |
| [getComponents](#getComponents) | 方法 |
| [getTags](#getTags) | 方法 |
| [hasTag](#hasTag) | 方法 |
| [getRawLore](#getRawLore) | 方法 |
| [getDynamicPropertyIds](#getDynamicPropertyIds) | 方法 |
| [setDynamicProperty](#setDynamicProperty) | 方法 |
| [setDynamicProperties](#setDynamicProperties) | 方法 |

## 构造器 {#constructor}

```python
ItemStack(itemType: str, amount: int = 1, data: dict = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemType` | [str](../../common/type-system.md#str) | `必填` | 传给 [ItemStack.__init__](itemStack.md#constructor) 的 itemType 参数；结合上方功能说明和下方调用示例使用。 |
| `amount` | [int](../../common/type-system.md#int) | `1` | 物品数量；新物品要求 1–255 的整数，并按最大堆叠数限制。 |
| `data` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Invalid item type: %r' % (itemType,)` |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown item type: %s' % self.__typeId` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetItemBasicInfo`, `GetLevelId`。

## typeId {#typeId}

```python
typeId: str
```

堆叠中的物品类型标识；省略命名空间时默认为 minecraft:。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## amount {#amount}

```python
amount
```

读取 `amount` 的当前值。

**访问：** 可读写。

写入方式：`instance.amount = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

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

## type {#type}

```python
type: ItemType
```

物品对应的 [ItemType](../reference/ItemType.md)。

**访问：** 只读。

**返回类型：** [ItemType](../reference/ItemType.md)。静态声明不替代本页的实现限制。

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

物品的最大堆叠数量。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.maxAmount
```

## getItemDict {#getItemDict}

```python
getItemDict() -> dict
```

获取网易物品数据

**返回类型：** [dict](../../common/type-system.md#dict)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getItemDict(instance):
    return instance.getItemDict()
```

## clone {#clone}

```python
clone() -> 'ItemStack'
```

执行 `clone` 操作。参数形态和结果约定如下。

**返回类型：** [ItemStack](itemStack.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clone(instance):
    return instance.clone()
```

## isStackableWith {#isStackableWith}

```python
isStackableWith(other: 'ItemStack') -> bool
```

检查 `isStackableWith` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `other` | [ItemStack](itemStack.md) | `必填` | 传给 [ItemStack.isStackableWith](itemStack.md#isStackableWith) 的 other 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_isStackableWith(instance, other):
    return instance.isStackableWith(other)
```

## getLore {#getLore}

```python
getLore() -> list[str]
```

读取 [ItemStack](itemStack.md) 的附加说明文本。

**返回类型：** [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getLore(instance):
    return instance.getLore()
```

## setLore {#setLore}

```python
setLore(loreList: list[str] = None) -> None
```

设置 [ItemStack](itemStack.md) 的附加说明文本；传入空内容时清空说明，具体接受的参数形式见签名。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `loreList` | [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)] | [None](../../common/type-system.md#none) | 传给 [ItemStack.setLore](itemStack.md#setLore) 的 loreList 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setLore(instance):
    return instance.setLore()
```

## hasComponent {#hasComponent}

```python
hasComponent(componentId: str) -> bool
```

检查此物品堆叠是否具有指定组件。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `componentId` | [str](../../common/type-system.md#str) | `必填` | 传给 [ItemStack.hasComponent](itemStack.md#hasComponent) 的 componentId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasComponent(instance, componentId):
    return instance.hasComponent(componentId)
```

## getComponent {#getComponent}

```python
getComponent(componentId: str) -> None | ItemComponent
```

读取物品堆叠的组件以访问附加能力。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `componentId` | [str](../../common/type-system.md#str) | `必填` | 传给 [ItemStack.getComponent](itemStack.md#getComponent) 的 componentId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none) \| [ItemComponent](../reference/ItemComponent.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getComponent(instance, componentId):
    return instance.getComponent(componentId)
```

## getDynamicProperty {#getDynamicProperty}

```python
getDynamicProperty(identifier: str) -> 0
```

读取属性值。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |

**返回类型：** 0。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getDynamicProperty(instance, identifier):
    return instance.getDynamicProperty(identifier)
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

## getComponents {#getComponents}

```python
getComponents() -> list
```

读取 `getComponents` 操作。参数形态和结果约定如下。

**返回类型：** [list](../../common/type-system.md#list)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getComponents(instance):
    return instance.getComponents()
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
| `tag` | [str](../../common/type-system.md#str) | `必填` | 传给 [ItemStack.hasTag](itemStack.md#hasTag) 的 tag 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasTag(instance, tag):
    return instance.hasTag(tag)
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

## getDynamicPropertyIds {#getDynamicPropertyIds}

```python
getDynamicPropertyIds() -> list[str]
```

返回此实体已使用的动态属性标识集合。

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
setDynamicProperty(identifier: str, value: 0 = None) -> None
```

设置指定动态属性；此操作仅适用于不可堆叠的物品。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `value` | 0 | [None](../../common/type-system.md#none) | 需要写入的值，类型、范围及副本语义见本成员说明。 |

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

批量设置多个动态属性。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `values` | [dict](../../common/type-system.md#dict) | `必填` | 传给 [ItemStack.setDynamicProperties](itemStack.md#setDynamicProperties) 的 values 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setDynamicProperties(instance, values):
    return instance.setDynamicProperties(values)
```

## 使用示例


```python
from ModSAPI.server.beta import ItemStack

item = ItemStack("minecraft:diamond", 3)
item.setLore(["Example reward"])
copy = item.clone()
print(copy.typeId, copy.amount)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)