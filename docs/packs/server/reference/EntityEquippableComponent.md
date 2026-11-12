---
title: "EntityEquippableComponent"
sidebar_label: "EntityEquippableComponent"
---

import ApiFieldAnchor from '@docusaurus/Link';

# EntityEquippableComponent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/components/EntityComponents.py`；声明补充了静态类型信息。

访问生物的装备槽位。玩家实体具有此组件。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[EntityComponent](EntityComponent.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-componentId" />`componentId` | [Literal](../../common/type-system.md#literal)['minecraft:equippable'] | `'minecraft:equippable'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [totalArmor](#totalArmor) | 只读属性 |
| [totalToughness](#totalToughness) | 只读属性 |
| [getEquipment](#getEquipment) | 方法 |
| [setEquipment](#setEquipment) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [entity](EntityComponent.md#entity) | [EntityComponent](EntityComponent.md) |
| [isValid](Component.md#isValid) | [Component](Component.md) |
| [typeId](Component.md#typeId) | [Component](Component.md) |

## 构造器 {#constructor}

```python
EntityEquippableComponent(data)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## totalArmor {#totalArmor}

```python
totalArmor: int
```

所属实体的总护甲值。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.totalArmor
```

## totalToughness {#totalToughness}

```python
totalToughness: int
```

所属实体的总护甲韧性值。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.totalToughness
```

## getEquipment {#getEquipment}

```python
getEquipment(equipmentSlot: str) -> ItemStack | None
```

读取已支持的装备槽，空槽返回 [None](../../common/type-system.md#none)。未知槽位会被拒绝。SAPI 的 Body 与网易表示胸甲的 BODY 常量不同，没有经过核验的 Body 映射会明确报告不支持。

:::note 当前实现说明
支持 Mainhand、Offhand、Head、Chest、Legs、Feet 六种 [EquipmentSlot](../../common/reference/EquipmentSlot.md) 常量。空槽返回 [None](../../common/type-system.md#none)；SAPI Body 尚无经核验的原生映射，会抛出 [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md)。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `equipmentSlot` | [str](../../common/type-system.md#str) | `必填` | 传给 [EntityEquippableComponent.getEquipment](EntityEquippableComponent.md#getEquipment) 的 equipmentSlot 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ItemStack](../apis/itemStack.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetEntityItem'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEquipment(instance, equipmentSlot):
    return instance.getEquipment(equipmentSlot)
```

## setEquipment {#setEquipment}

```python
setEquipment(equipmentSlot: str, itemStack: ItemStack | EventItemStack | None = None) -> bool
```

使用复制的物品值替换或清除已支持的槽位。接受服务端 [ItemStack](../apis/itemStack.md) 或事件物品快照；[None](../../common/type-system.md#none) 只清除指定槽位。原生正常拒绝返回 False，畸形状态值或引擎异常抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)。

:::note 当前实现说明
接受服务端 [ItemStack](../apis/itemStack.md)、事件 [EventItemStack](../../common/reference/EventItemStack.md) 或 [None](../../common/type-system.md#none)。参数在原生写入前复制；未知槽位与未支持的 Body 不会被映射到头盔或胸甲。原生正常拒绝返回 False。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `equipmentSlot` | [str](../../common/type-system.md#str) | `必填` | 传给 [EntityEquippableComponent.setEquipment](EntityEquippableComponent.md#setEquipment) 的 equipmentSlot 参数；结合上方功能说明和下方调用示例使用。 |
| `itemStack` | [ItemStack](../apis/itemStack.md) \| [EventItemStack](../../common/reference/EventItemStack.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 物品堆叠对象；不是物品名称字符串。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'itemStack must be an ItemStack, event item snapshot, or None'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetEntityItem`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setEquipment(instance, equipmentSlot):
    return instance.setEquipment(equipmentSlot)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EntityEquippableComponent 对象。
    print(value.totalArmor)
    print(value.totalToughness)
    print(value.componentId)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)