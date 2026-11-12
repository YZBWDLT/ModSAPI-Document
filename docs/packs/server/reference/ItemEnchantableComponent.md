---
title: "ItemEnchantableComponent"
sidebar_label: "ItemEnchantableComponent"
---

# ItemEnchantableComponent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/components/ItemComponents.py`；声明补充了静态类型信息。

根据当前原生定义编辑复制后的附魔值。槽位与冲突校验采用 primary_slots 和 incompatible 字段；整批使用一次当前目录，所有项目通过后才提交。编辑后的物品需要另行写回容器。

## 获取方式

通过 item.getComponent("enchantable") 或 [ItemEnchantableComponent.componentId](ItemEnchantableComponent.md#字段与常量) 取得；不具备该组件时为 [None](../../common/type-system.md#none)。

基类：[ItemComponent](ItemComponent.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `componentId` | [Final](../../common/type-system.md#final) | `'minecraft:enchantable'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [slots](#slots) | 只读属性 |
| [canAddEnchantment](#canAddEnchantment) | 方法 |
| [addEnchantment](#addEnchantment) | 方法 |
| [addEnchantments](#addEnchantments) | 方法 |
| [getEnchantment](#getEnchantment) | 方法 |
| [getEnchantments](#getEnchantments) | 方法 |
| [hasEnchantment](#hasEnchantment) | 方法 |
| [removeEnchantment](#removeEnchantment) | 方法 |
| [removeAllEnchantments](#removeAllEnchantments) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [asDurabilityComponent](ItemComponent.md#asDurabilityComponent) | [ItemComponent](ItemComponent.md) |
| [asEnchantableComponent](ItemComponent.md#asEnchantableComponent) | [ItemComponent](ItemComponent.md) |
| [isValid](Component.md#isValid) | [Component](Component.md) |
| [typeId](Component.md#typeId) | [Component](Component.md) |

## slots {#slots}

```python
slots: list[str]
```

返回槽位名称副本；不会猜测尚未识别的原生位。

**访问：** 只读。

**返回类型：** [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md) | `'Native enchantment slots contain unmapped bits'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.slots
```

## canAddEnchantment {#canAddEnchantment}

```python
canAddEnchantment(enchantment: Enchantment | dict[str, Any]) -> bool
```

检查槽位与附魔冲突；非法标识和等级仍会报告错误。

:::note 当前实现说明
槽位或冲突不兼容返回 False；非法等级、未知标识、无法核验旧附魔及原生故障仍会报告错误。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchantment` | [Enchantment](../../common/reference/Enchantment.md) \| [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] | `必填` | 传给 [ItemEnchantableComponent.canAddEnchantment](ItemEnchantableComponent.md#canAddEnchantment) 的 enchantment 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_canAddEnchantment(instance, enchantment):
    return instance.canAddEnchantment(enchantment)
```

## addEnchantment {#addEnchantment}

```python
addEnchantment(enchantment: Enchantment | dict[str, Any]) -> None
```

添加或替换一个附魔副本；不兼容时报告错误。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchantment` | [Enchantment](../../common/reference/Enchantment.md) \| [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] | `必填` | 传给 [ItemEnchantableComponent.addEnchantment](ItemEnchantableComponent.md#addEnchantment) 的 enchantment 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addEnchantment(instance, enchantment):
    return instance.addEnchantment(enchantment)
```

## addEnchantments {#addEnchantments}

```python
addEnchantments(enchantments: list[Enchantment | dict[str, Any]]) -> None
```

使用一次目录读取校验整批内容，之后才改变任何附魔。

:::note 当前实现说明
整批使用一次原生目录读取，在全部校验通过后才修改独立物品；实际背包写回另行调用 setItem。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchantments` | [list](../../common/type-system.md#list)[[Enchantment](../../common/reference/Enchantment.md) \| [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)]] | `必填` | 传给 [ItemEnchantableComponent.addEnchantments](ItemEnchantableComponent.md#addEnchantments) 的 enchantments 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'enchantments must be a sequence of enchantment values'` |
| [EnchantmentTypeNotCompatibleError](../../common/reference/EnchantmentTypeNotCompatibleError.md) | `'Enchantment is incompatible with this item or its enchantments'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addEnchantments(instance, enchantments):
    return instance.addEnchantments(enchantments)
```

## getEnchantment {#getEnchantment}

```python
getEnchantment(enchantmentType: str | EnchantmentType) -> Enchantment | None
```

返回独立的带等级附魔值或 [None](../../common/type-system.md#none)；接受类型对象或字符串。

:::note 当前实现说明
返回独立值或 [None](../../common/type-system.md#none)，修改查询值不会改变组件；需要再次调用添加方法提交。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchantmentType` | [str](../../common/type-system.md#str) \| [EnchantmentType](../../common/reference/EnchantmentType.md) | `必填` | 传给 [ItemEnchantableComponent.getEnchantment](ItemEnchantableComponent.md#getEnchantment) 的 enchantmentType 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Enchantment](../../common/reference/Enchantment.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEnchantment(instance, enchantmentType):
    return instance.getEnchantment(enchantmentType)
```

## getEnchantments {#getEnchantments}

```python
getEnchantments() -> list[Enchantment]
```

返回独立附魔值，不额外查询定义或重写旧数据。

**返回类型：** [list](../../common/type-system.md#list)[[Enchantment](../../common/reference/Enchantment.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEnchantments(instance):
    return instance.getEnchantments()
```

## hasEnchantment {#hasEnchantment}

```python
hasEnchantment(enchantmentType: str | EnchantmentType) -> bool
```

物品是否包含该规范类型；会校验未知标识。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchantmentType` | [str](../../common/type-system.md#str) \| [EnchantmentType](../../common/reference/EnchantmentType.md) | `必填` | 传给 [ItemEnchantableComponent.hasEnchantment](ItemEnchantableComponent.md#hasEnchantment) 的 enchantmentType 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasEnchantment(instance, enchantmentType):
    return instance.hasEnchantment(enchantmentType)
```

## removeEnchantment {#removeEnchantment}

```python
removeEnchantment(enchantmentType: str | EnchantmentType) -> None
```

移除指定规范类型的所有条目，保留其他原生数据。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchantmentType` | [str](../../common/type-system.md#str) \| [EnchantmentType](../../common/reference/EnchantmentType.md) | `必填` | 传给 [ItemEnchantableComponent.removeEnchantment](ItemEnchantableComponent.md#removeEnchantment) 的 enchantmentType 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeEnchantment(instance, enchantmentType):
    return instance.removeEnchantment(enchantmentType)
```

## removeAllEnchantments {#removeAllEnchantments}

```python
removeAllEnchantments() -> None
```

明确清除已知、自定义以及不透明的原生附魔。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeAllEnchantments(instance):
    return instance.removeAllEnchantments()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ItemEnchantableComponent 对象。
    print(value.slots)
    print(value.componentId)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)