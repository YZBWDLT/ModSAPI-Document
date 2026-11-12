---
title: "EntityDamageCause"
sidebar_label: "EntityDamageCause"
---

# EntityDamageCause

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/enums/Dimension.py`；声明补充了静态类型信息。

描述实体受到伤害的原因。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `anvil` | 由运行时值确定 | `'anvil'` |  |
| `blockExplosion` | 由运行时值确定 | `'block_explosion'` |  |
| `charging` | 由运行时值确定 | `'charging'` |  |
| `contact` | 由运行时值确定 | `'contact'` |  |
| `drowning` | 由运行时值确定 | `'drowning'` |  |
| `entityAttack` | 由运行时值确定 | `'entity_attack'` |  |
| `entityExplosion` | 由运行时值确定 | `'entity_explosion'` |  |
| `fall` | 由运行时值确定 | `'fall'` |  |
| `fallingBlock` | 由运行时值确定 | `'falling_block'` |  |
| `fire` | 由运行时值确定 | `'fire'` |  |
| `fireTick` | 由运行时值确定 | `'fire_tick'` |  |
| `fireworks` | 由运行时值确定 | `'fireworks'` |  |
| `flyIntoWall` | 由运行时值确定 | `'fly_into_wall'` |  |
| `freezing` | 由运行时值确定 | `'freezing'` |  |
| `lava` | 由运行时值确定 | `'lava'` |  |
| `lightning` | 由运行时值确定 | `'lightning'` |  |
| `maceSmash` | 由运行时值确定 | `'mace_smash'` |  |
| `magic` | 由运行时值确定 | `'magic'` |  |
| `magma` | 由运行时值确定 | `'magma'` |  |
| `none` | 由运行时值确定 | `'none'` |  |
| `override` | 由运行时值确定 | `'override'` |  |
| `piston` | 由运行时值确定 | `'piston'` |  |
| `projectile` | 由运行时值确定 | `'projectile'` |  |
| `ramAttack` | 由运行时值确定 | `'ram_attack'` |  |
| `selfDestruct` | 由运行时值确定 | `'self_destruct'` |  |
| `sonicBoom` | 由运行时值确定 | `'sonic_boom'` |  |
| `soulCampfire` | 由运行时值确定 | `'soul_campfire'` |  |
| `stalactite` | 由运行时值确定 | `'stalactite'` |  |
| `stalagmite` | 由运行时值确定 | `'stalagmite'` |  |
| `starve` | 由运行时值确定 | `'starve'` |  |
| `suffocation` | 由运行时值确定 | `'suffocation'` |  |
| `suicide` | 由运行时值确定 | `'suicide'` |  |
| `temperature` | 由运行时值确定 | `'temperature'` |  |
| `thorns` | 由运行时值确定 | `'thorns'` |  |
| `void` | 由运行时值确定 | `'void'` |  |
| `wither` | 由运行时值确定 | `'wither'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EntityDamageCause 对象。
    print(value.anvil)
    print(value.blockExplosion)
    print(value.charging)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)