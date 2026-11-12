---
title: "EntityDamageCause"
sidebar_label: "EntityDamageCause"
---

import ApiFieldAnchor from '@docusaurus/Link';

# EntityDamageCause

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/enums/Dimension.py`；声明补充了静态类型信息。

描述实体受到伤害的原因。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-anvil" />`anvil` | 由运行时值确定 | `'anvil'` |  |
| <ApiFieldAnchor id="field-blockExplosion" />`blockExplosion` | 由运行时值确定 | `'block_explosion'` |  |
| <ApiFieldAnchor id="field-charging" />`charging` | 由运行时值确定 | `'charging'` |  |
| <ApiFieldAnchor id="field-contact" />`contact` | 由运行时值确定 | `'contact'` |  |
| <ApiFieldAnchor id="field-drowning" />`drowning` | 由运行时值确定 | `'drowning'` |  |
| <ApiFieldAnchor id="field-entityAttack" />`entityAttack` | 由运行时值确定 | `'entity_attack'` |  |
| <ApiFieldAnchor id="field-entityExplosion" />`entityExplosion` | 由运行时值确定 | `'entity_explosion'` |  |
| <ApiFieldAnchor id="field-fall" />`fall` | 由运行时值确定 | `'fall'` |  |
| <ApiFieldAnchor id="field-fallingBlock" />`fallingBlock` | 由运行时值确定 | `'falling_block'` |  |
| <ApiFieldAnchor id="field-fire" />`fire` | 由运行时值确定 | `'fire'` |  |
| <ApiFieldAnchor id="field-fireTick" />`fireTick` | 由运行时值确定 | `'fire_tick'` |  |
| <ApiFieldAnchor id="field-fireworks" />`fireworks` | 由运行时值确定 | `'fireworks'` |  |
| <ApiFieldAnchor id="field-flyIntoWall" />`flyIntoWall` | 由运行时值确定 | `'fly_into_wall'` |  |
| <ApiFieldAnchor id="field-freezing" />`freezing` | 由运行时值确定 | `'freezing'` |  |
| <ApiFieldAnchor id="field-lava" />`lava` | 由运行时值确定 | `'lava'` |  |
| <ApiFieldAnchor id="field-lightning" />`lightning` | 由运行时值确定 | `'lightning'` |  |
| <ApiFieldAnchor id="field-maceSmash" />`maceSmash` | 由运行时值确定 | `'mace_smash'` |  |
| <ApiFieldAnchor id="field-magic" />`magic` | 由运行时值确定 | `'magic'` |  |
| <ApiFieldAnchor id="field-magma" />`magma` | 由运行时值确定 | `'magma'` |  |
| <ApiFieldAnchor id="field-none" />`none` | 由运行时值确定 | `'none'` |  |
| <ApiFieldAnchor id="field-override" />`override` | 由运行时值确定 | `'override'` |  |
| <ApiFieldAnchor id="field-piston" />`piston` | 由运行时值确定 | `'piston'` |  |
| <ApiFieldAnchor id="field-projectile" />`projectile` | 由运行时值确定 | `'projectile'` |  |
| <ApiFieldAnchor id="field-ramAttack" />`ramAttack` | 由运行时值确定 | `'ram_attack'` |  |
| <ApiFieldAnchor id="field-selfDestruct" />`selfDestruct` | 由运行时值确定 | `'self_destruct'` |  |
| <ApiFieldAnchor id="field-sonicBoom" />`sonicBoom` | 由运行时值确定 | `'sonic_boom'` |  |
| <ApiFieldAnchor id="field-soulCampfire" />`soulCampfire` | 由运行时值确定 | `'soul_campfire'` |  |
| <ApiFieldAnchor id="field-stalactite" />`stalactite` | 由运行时值确定 | `'stalactite'` |  |
| <ApiFieldAnchor id="field-stalagmite" />`stalagmite` | 由运行时值确定 | `'stalagmite'` |  |
| <ApiFieldAnchor id="field-starve" />`starve` | 由运行时值确定 | `'starve'` |  |
| <ApiFieldAnchor id="field-suffocation" />`suffocation` | 由运行时值确定 | `'suffocation'` |  |
| <ApiFieldAnchor id="field-suicide" />`suicide` | 由运行时值确定 | `'suicide'` |  |
| <ApiFieldAnchor id="field-temperature" />`temperature` | 由运行时值确定 | `'temperature'` |  |
| <ApiFieldAnchor id="field-thorns" />`thorns` | 由运行时值确定 | `'thorns'` |  |
| <ApiFieldAnchor id="field-void" />`void` | 由运行时值确定 | `'void'` |  |
| <ApiFieldAnchor id="field-wither" />`wither` | 由运行时值确定 | `'wither'` |  |

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