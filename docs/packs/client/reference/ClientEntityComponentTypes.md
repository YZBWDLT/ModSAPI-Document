---
title: "ClientEntityComponentTypes"
sidebar_label: "ClientEntityComponentTypes"
---

# ClientEntityComponentTypes

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Attributes.py`；声明补充了静态类型信息。

已支持的只读客户端组件标识符，包括本地背包。

## 获取方式

从 ModSAPI.client.beta 导入；选择本机能够读取的生命及陆地、水中、岩浆移动属性。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `Inventory` | [Literal](../../common/type-system.md#literal)['minecraft:inventory'] | `'minecraft:inventory'` | 只读背包，当前仅支持本地玩家。 |
| `Equippable` | [Literal](../../common/type-system.md#literal)['minecraft:equippable'] | `'minecraft:equippable'` | 只读六槽装备，当前仅支持本地玩家。 |
| `Health` | [Literal](../../common/type-system.md#literal)['minecraft:health'] | `'minecraft:health'` | 已同步的生命值，零是合法的当前值。 |
| `Movement` | [Literal](../../common/type-system.md#literal)['minecraft:movement'] | `'minecraft:movement'` | 已同步的基础移动速度，不是实体的瞬时运动速度。 |
| `UnderwaterMovement` | [Literal](../../common/type-system.md#literal)['minecraft:underwater_movement'] | `'minecraft:underwater_movement'` | 已同步的水中移动速度。 |
| `LavaMovement` | [Literal](../../common/type-system.md#literal)['minecraft:lava_movement'] | `'minecraft:lava_movement'` | 已同步的岩浆中移动速度。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientEntityComponentTypes 对象。
    print(value.Inventory)
    print(value.Equippable)
    print(value.Health)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)