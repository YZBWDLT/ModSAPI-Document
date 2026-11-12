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

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [typeId](#typeId) | 只读属性 |
| [amount](#amount) | 可读写属性 |
| [auxValue](#auxValue) | 只读属性 |
| [keepOnDeath](#keepOnDeath) | 可读写属性 |
| [lockMode](#lockMode) | 可读写属性 |
| [nameTag](#nameTag) | 可读写属性 |
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
ItemStack(itemType: str | ItemType, amount: int = 1, data: dict[str, Any] | None = None) -> None
```

创建独立物品；公开数量为一到二百五十五，并按类型最大数量限制。data 是用于保留原生内容进行读取和克隆的网易扩展，原生已有数量和显示元数据不会被裁剪。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemType` | [str](../../common/type-system.md#str) \| [ItemType](../reference/ItemType.md) | `必填` | 传给 [ItemStack.__init__](itemStack.md#constructor) 的 itemType 参数；结合上方功能说明和下方调用示例使用。 |
| `amount` | [int](../../common/type-system.md#int) | `1` | 物品数量；新物品要求 1–255 的整数，并按最大堆叠数限制。 |
| `data` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'data must be a native item dictionary'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Native item aux value must be an integer'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown item type: %s' % self.__typeId` |
| [ValueError](../../common/type-system.md#valueerror) | `'An ItemStack must contain a nonempty item'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Item amount must be an integer between 1 and 255'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

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
amount: int
```

物品数量；编辑时要求一到二百五十五，并按类型最大数量限制。读取和克隆保留原生已有超量堆叠，不丢弃物品。

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

## auxValue {#auxValue}

```python
auxValue: int
```

网易扩展的原生变种值，用于基础定义与标签查询。

:::note 当前实现说明
网易原生变种，优先 newAuxValue；定义与标签查询都使用它，不能将该值一律当作耐久。
:::

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.auxValue
```

## keepOnDeath {#keepOnDeath}

```python
keepOnDeath: bool
```

是否死亡保留；写入要求真正的 [bool](../../common/type-system.md#bool)。

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

使用 [ItemLockMode.none](../../common/reference/ItemLockMode.md#字段与常量)、inventory 或 slot，拒绝未支持的值。

**访问：** 可读写。

写入方式：`instance.lockMode = value`。参数类型线索：`(value: str) -> None`。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'lockMode must be none, inventory or slot'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.lockMode

def write_value(instance, value):
    instance.lockMode = value
```

## nameTag {#nameTag}

```python
nameTag: str | None
```

显示名称或 [None](../../common/type-system.md#none)；新名称最多二百五十五个字符。

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

## isStackable {#isStackable}

```python
isStackable: bool
```

该物品类型是否允许堆叠且不包含自定义元数据。

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
getItemDict() -> dict[str, Any]
```

返回原生物品数据的副本，保留外部元数据和当前字段。

**返回类型：** [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getItemDict(instance):
    return instance.getItemDict()
```

## clone {#clone}

```python
clone() -> ItemStack
```

复制当前物品，保留数量、外部原生标签和属性。

:::note 当前实现说明
克隆保留原生数量和外部元数据；不会重写或删除其他模组的 extraId。
:::

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
isStackableWith(other: ItemStack) -> bool
```

比较类型和完整堆叠元数据，忽略物品数量。

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
setLore(loreList: list[str] | None = None) -> None
```

设置最多二十行普通文本，每行最多五十个字符。[None](../../common/type-system.md#none)、空字符串或空列表清除描述；尚未支持完整 RawMessage 格式。替换前先校验所有行。

:::note 当前实现说明
当前仅支持普通文本，最多二十行、每行五十个字符。RawMessage 写入未实现；原生已有超长描述在读取和克隆时保留。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `loreList` | [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)] \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [ItemStack.setLore](itemStack.md#setLore) 的 loreList 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Item lore is limited to 20 lines'` |
| [TypeError](../../common/type-system.md#typeerror) | `'loreList must be a list of plain text lines or None'` |

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
getComponent(componentId: str) -> ItemComponent | None
```

读取物品堆叠的组件以访问附加能力。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `componentId` | [str](../../common/type-system.md#str) | `必填` | 传给 [ItemStack.getComponent](itemStack.md#getComponent) 的 componentId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ItemComponent](../reference/ItemComponent.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getComponent(instance, componentId):
    return instance.getComponent(componentId)
```

## getDynamicProperty {#getDynamicProperty}

```python
getDynamicProperty(identifier: str) -> Any
```

返回属性值的独立副本；标识不存在时为 [None](../../common/type-system.md#none)。

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

## clearDynamicProperties {#clearDynamicProperties}

```python
clearDynamicProperties() -> None
```

清除本库属性，保留外部原生标签及 extraId 原文。

:::note 当前实现说明
仅清除本库属性视图。兼容读取的旧字面字典也不会被删除；独立空标记防止旧属性再次出现。
:::

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
getComponents() -> list[ItemComponent]
```

返回当前独立物品上已支持的可修改组件。

**返回类型：** [list](../../common/type-system.md#list)[[ItemComponent](../reference/ItemComponent.md)]。静态声明不替代本页的实现限制。

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

使用 GetItemTags 和当前原生变种读取定义标签副本。

:::note 当前实现说明
通过 GetItemTags 查询当前类型及变种的定义标签，返回独立列表；不是从 GetItemBasicInfo 的非标准 tags 字段读取。
:::

**返回类型：** [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetItemTags'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetItemTags`, `GetLevelId`。

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

物品定义是否包含指定的非空标签标识。

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
getRawLore() -> list[dict[str, str]]
```

将每行普通描述转换为独立的 RawMessage 文本记录。

**返回类型：** [list](../../common/type-system.md#list)[[dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [str](../../common/type-system.md#str)]]。静态声明不替代本页的实现限制。

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

返回当前物品的属性标识列表副本，不承诺顺序。

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

保存经过校验的属性副本，[None](../../common/type-system.md#none) 删除；不会重写 extraId。标量和 [Vector3](../extra/vector.md) 沿用 SAPI 命名，嵌套 JSON 数据是本库扩展。版本化载荷最多三万二千七百六十七个 UTF-8 字节，包含格式开销；修改独立物品后需要写回槽位。

:::note 当前实现说明
标量和 [Vector3](../extra/vector.md) 外另支持嵌套 JSON 数据；[None](../../common/type-system.md#none) 删除，零和 False 保留。独立原生标签载荷最多三万二千七百六十七字节，含格式开销；不是微软原生字节计量。
:::

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

先校验完整批次，再应用属性变更；[None](../../common/type-system.md#none) 删除。非法标识、不支持的对象、循环、非有限数字、过深嵌套或超量载荷不会改变任何已有值。读取到损坏的本库原生标签时报告 [StorageDataError](../../common/reference/StorageDataError.md)。

:::note 当前实现说明
校验完整批次后才改动。循环、无穷值、非法编码和超限数据不会造成半批写入；不再覆盖 extraId。实机保存和跨版本迁移仍待核验。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `values` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] | `必填` | 传给 [ItemStack.setDynamicProperties](itemStack.md#setDynamicProperties) 的 values 参数；结合上方功能说明和下方调用示例使用。 |

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