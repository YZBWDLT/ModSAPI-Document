---
title: "ItemDurabilityComponent"
sidebar_label: "ItemDurabilityComponent"
---

# ItemDurabilityComponent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/components/ItemComponents.py`；声明补充了静态类型信息。

独立物品上的损耗与剩余耐久；编辑不会直接写入槽位。

## 获取方式

通过 item.getComponent("durability") 或 [ItemDurabilityComponent.componentId](ItemDurabilityComponent.md#字段与常量) 取得；编辑后将物品写回容器。

基类：[ItemComponent](ItemComponent.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `componentId` | [Final](../../common/type-system.md#final) | `'minecraft:durability'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [maxDurability](#maxDurability) | 只读属性 |
| [remain](#remain) | 可读写属性 |
| [damage](#damage) | 可读写属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [asDurabilityComponent](ItemComponent.md#asDurabilityComponent) | [ItemComponent](ItemComponent.md) |
| [asEnchantableComponent](ItemComponent.md#asEnchantableComponent) | [ItemComponent](ItemComponent.md) |
| [isValid](Component.md#isValid) | [Component](Component.md) |
| [typeId](Component.md#typeId) | [Component](Component.md) |

## maxDurability {#maxDurability}

```python
maxDurability: int
```

当前物品类型的正整数原生耐久上限。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.maxDurability
```

## remain {#remain}

```python
remain: int
```

网易扩展的剩余耐久；公开编辑要求零到 maxDurability。原生已有越界值保持可读，不自动裁剪。

:::note 当前实现说明
网易扩展。公开编辑限制在零到最大值；已有原生非标准值只读保留，不在克隆时裁剪。
:::

**访问：** 可读写。

写入方式：`instance.remain = value`。参数类型线索：`(value: int) -> None`。

写入参数 `value`：[int](../../common/type-system.md#int)。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.remain

def write_value(instance, value):
    instance.remain = value
```

## damage {#damage}

```python
damage: int
```

已经损耗的耐久；公开编辑要求零到 maxDurability 之间的整数。

**访问：** 可读写。

写入方式：`instance.damage = value`。参数类型线索：`(value: int) -> None`。

写入参数 `value`：[int](../../common/type-system.md#int)。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.damage

def write_value(instance, value):
    instance.damage = value
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ItemDurabilityComponent 对象。
    print(value.maxDurability)
    print(value.remain)
    print(value.damage)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)