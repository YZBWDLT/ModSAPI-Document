---
title: "ItemComponent"
sidebar_label: "ItemComponent"
---

# ItemComponent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/components/ItemComponents.py`；声明补充了静态类型信息。

独立 [ItemStack](../apis/itemStack.md) 上的物品组件基类，不直接写入背包。

## 获取方式

通过 [ItemStack.getComponent](../apis/itemStack.md#getComponent) 或 getComponents 取得，表示独立物品上的组件；不会直接写入背包。

基类：[Component](Component.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [asEnchantableComponent](#asEnchantableComponent) | 方法 |
| [asDurabilityComponent](#asDurabilityComponent) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [isValid](Component.md#isValid) | [Component](Component.md) |
| [typeId](Component.md#typeId) | [Component](Component.md) |

## asEnchantableComponent {#asEnchantableComponent}

```python
asEnchantableComponent() -> ItemEnchantableComponent
```

返回当前附魔组件；拒绝不兼容的组件转换。

**返回类型：** [ItemEnchantableComponent](ItemEnchantableComponent.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'This item component is not enchantable'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_asEnchantableComponent(instance):
    return instance.asEnchantableComponent()
```

## asDurabilityComponent {#asDurabilityComponent}

```python
asDurabilityComponent() -> ItemDurabilityComponent
```

返回当前耐久组件；拒绝不兼容的组件转换。

**返回类型：** [ItemDurabilityComponent](ItemDurabilityComponent.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'This item component has no durability'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_asDurabilityComponent(instance):
    return instance.asDurabilityComponent()
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 ItemComponent 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)