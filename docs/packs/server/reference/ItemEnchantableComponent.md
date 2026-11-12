---
title: "ItemEnchantableComponent"
sidebar_label: "ItemEnchantableComponent"
---

# ItemEnchantableComponent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/components/ItemComponents.py`；声明补充了静态类型信息。

具有此组件的物品可以附魔。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[ItemComponent](ItemComponent.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [slots](#slots) | 只读属性 |
| [canAddEnchantment](#canAddEnchantment) | 方法 |
| [addEnchantment](#addEnchantment) | 方法 |
| [addEnchantments](#addEnchantments) | 方法 |
| [getEnchantment](#getEnchantment) | 方法 |
| [getEnchantments](#getEnchantments) | 方法 |
| [hasEnchantment](#hasEnchantment) | 方法 |
| [removeAllEnchantments](#removeAllEnchantments) | 方法 |
| [removeEnchantment](#removeEnchantment) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [asDurabilityComponent](ItemComponent.md#asDurabilityComponent) | [ItemComponent](ItemComponent.md) |
| [asEnchantableComponent](ItemComponent.md#asEnchantableComponent) | [ItemComponent](ItemComponent.md) |
| [isValid](Component.md#isValid) | [Component](Component.md) |
| [typeId](Component.md#typeId) | [Component](Component.md) |

## 构造器 {#constructor}

```python
ItemEnchantableComponent(data)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## slots {#slots}

```python
slots: list[str]
```

读取 `slots` 的当前值。

**访问：** 只读。

**返回类型：** [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.slots
```

## canAddEnchantment {#canAddEnchantment}

```python
canAddEnchantment(enchantment: Enchantment | dict) -> bool
```

检查指定附魔是否可以添加到物品堆叠。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchantment` | [Enchantment](../../common/reference/Enchantment.md) \| [dict](../../common/type-system.md#dict) | `必填` | 传给 [ItemEnchantableComponent.canAddEnchantment](ItemEnchantableComponent.md#canAddEnchantment) 的 enchantment 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAllEnchantsInfo`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_canAddEnchantment(instance, enchantment):
    return instance.canAddEnchantment(enchantment)
```

## addEnchantment {#addEnchantment}

```python
addEnchantment(enchantment: dict | Enchantment) -> None
```

向物品堆叠添加附魔。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchantment` | [dict](../../common/type-system.md#dict) \| [Enchantment](../../common/reference/Enchantment.md) | `必填` | 传给 [ItemEnchantableComponent.addEnchantment](ItemEnchantableComponent.md#addEnchantment) 的 enchantment 参数；结合上方功能说明和下方调用示例使用。 |

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
addEnchantments(enchantments: list[dict | Enchantment]) -> None
```

向物品堆叠添加一组附魔。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchantments` | [list](../../common/type-system.md#list)[[dict](../../common/type-system.md#dict) \| [Enchantment](../../common/reference/Enchantment.md)] | `必填` | 传给 [ItemEnchantableComponent.addEnchantments](ItemEnchantableComponent.md#addEnchantments) 的 enchantments 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addEnchantments(instance, enchantments):
    return instance.addEnchantments(enchantments)
```

## getEnchantment {#getEnchantment}

```python
getEnchantment(enchantmentType: str) -> Enchantment
```

从物品堆叠读取指定类型的附魔。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchantmentType` | [str](../../common/type-system.md#str) | `必填` | 传给 [ItemEnchantableComponent.getEnchantment](ItemEnchantableComponent.md#getEnchantment) 的 enchantmentType 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Enchantment](../../common/reference/Enchantment.md)。静态声明不替代本页的实现限制。

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

读取物品堆叠的全部附魔。

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
hasEnchantment(enchantmentType: str) -> bool
```

检查物品堆叠是否具有指定类型的附魔。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchantmentType` | [str](../../common/type-system.md#str) | `必填` | 传给 [ItemEnchantableComponent.hasEnchantment](ItemEnchantableComponent.md#hasEnchantment) 的 enchantmentType 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasEnchantment(instance, enchantmentType):
    return instance.hasEnchantment(enchantmentType)
```

## removeAllEnchantments {#removeAllEnchantments}

```python
removeAllEnchantments()
```

移除物品堆叠的全部附魔。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeAllEnchantments(instance):
    return instance.removeAllEnchantments()
```

## removeEnchantment {#removeEnchantment}

```python
removeEnchantment(enchantmentType: str) -> None
```

移除指定类型的附魔。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchantmentType` | [str](../../common/type-system.md#str) | `必填` | 传给 [ItemEnchantableComponent.removeEnchantment](ItemEnchantableComponent.md#removeEnchantment) 的 enchantmentType 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeEnchantment(instance, enchantmentType):
    return instance.removeEnchantment(enchantmentType)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ItemEnchantableComponent 对象。
    print(value.slots)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)