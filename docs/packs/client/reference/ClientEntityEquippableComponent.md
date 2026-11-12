---
title: "ClientEntityEquippableComponent"
sidebar_label: "ClientEntityEquippableComponent"
---

import ApiFieldAnchor from '@docusaurus/Link';

# ClientEntityEquippableComponent

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Inventory.py`；声明补充了静态类型信息。

本地玩家只读六槽装备，实际写入应在服务端完成。

## 获取方式

通过本地玩家 getComponent([ClientEntityComponentTypes.Equippable](ClientEntityComponentTypes.md#field-Equippable)) 取得；无需主动构造。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-componentId" />`componentId` | 由运行时值确定 | `'minecraft:equippable'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [typeId](#typeId) | 只读属性 |
| [entity](#entity) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [getEquipment](#getEquipment) | 方法 |
| [getEquipmentSlot](#getEquipmentSlot) | 方法 |
| [getEquipmentItems](#getEquipmentItems) | 方法 |

## typeId {#typeId}

```python
typeId: str
```

命名空间化的组件标识符，失效后仍可读取。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## entity {#entity}

```python
entity: ClientEntity
```

所属本地客户端实体包装对象。

**访问：** 只读。

**返回类型：** [ClientEntity](ClientEntity.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entity
```

## isValid {#isValid}

```python
isValid: bool
```

所属实体是否可见且仍为本地玩家。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## getEquipment {#getEquipment}

```python
getEquipment(equipmentSlot: str, options: ClientItemReadOptions | None = None) -> ItemStackSnapshot | None
```

读取装备物品的独立元数据快照或 [None](../../common/type-system.md#none)。支持六种标准 [EquipmentSlot](../../common/reference/EquipmentSlot.md) 字符串。Body 明确不支持；网易盔甲 BODY 位置表示胸甲，并非微软 Body。includeUserData 默认 True，错误槽位不会自动选择替代位置。

:::note 当前实现说明
仅支持已列出的六个 [EquipmentSlot](../../common/reference/EquipmentSlot.md) 常量。Body 明确拒绝；本批仍仅面向本地玩家。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `equipmentSlot` | [str](../../common/type-system.md#str) | `必填` | 传给 [ClientEntityEquippableComponent.getEquipment](ClientEntityEquippableComponent.md#getEquipment) 的 equipmentSlot 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [ClientItemReadOptions](ClientItemReadOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [ItemStackSnapshot](../../common/reference/ItemStackSnapshot.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetCarriedItem`, `GetOffhandItem`, `GetPlayerItem`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEquipment(instance, equipmentSlot):
    return instance.getEquipment(equipmentSlot)
```

## getEquipmentSlot {#getEquipmentSlot}

```python
getEquipmentSlot(equipmentSlot: str) -> ClientContainerSlot
```

取得实时只读槽位句柄，不替换装备。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `equipmentSlot` | [str](../../common/type-system.md#str) | `必填` | 传给 [ClientEntityEquippableComponent.getEquipmentSlot](ClientEntityEquippableComponent.md#getEquipmentSlot) 的 equipmentSlot 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ClientContainerSlot](ClientContainerSlot.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEquipmentSlot(instance, equipmentSlot):
    return instance.getEquipmentSlot(equipmentSlot)
```

## getEquipmentItems {#getEquipmentItems}

```python
getEquipmentItems(options: ClientItemReadOptions | None = None) -> dict[str, ItemStackSnapshot | None]
```

通过一次盔甲批量查询和两次主副手查询读取六个位置。返回以 [EquipmentSlot](../../common/reference/EquipmentSlot.md) 常量为键的独立字典，空位置为 [None](../../common/type-system.md#none)。多次原生调用不构成原子快照。includeUserData 默认 True。

:::note 当前实现说明
三次原生调用读取六个位置，结果按 [EquipmentSlot](../../common/reference/EquipmentSlot.md) 常量索引；不承诺跨调用的原子性。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [ClientItemReadOptions](ClientItemReadOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [ItemStackSnapshot](../../common/reference/ItemStackSnapshot.md) \| [None](../../common/type-system.md#none)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetPlayerAllItems'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerAllItems`, `GetCarriedItem`, `GetOffhandItem`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEquipmentItems(instance):
    return instance.getEquipmentItems()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientEntityEquippableComponent 对象。
    print(value.typeId)
    print(value.entity)
    print(value.isValid)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)