---
sidebar_position: 3
---

# 后事件-AfterEvents

可监听已发生的事件列表

### entityHurt {#entityHurt}

实体受伤事件

<details>

#### 参数:
- damage
    - 受到的伤害值
    - 类型：int
- damageSource
    - 伤害来源，包含攻击者/投掷物，伤害原因（类型）
    - 类型：[*EntityDamageSource*](../extra/info.md#EntityDamageSource)
- hurtEntity
    - 受伤实体
    - 类型：[*Entity*](../apis/entity.md)
    
</details>

### entityHitEntity {#entityHitEntity}

实体攻击实体事件

<details>

#### 参数:
- damagingEntity
    - 攻击者
    - 类型：[*Entity*](../apis/entity.md)
- hitEntity
    - 受伤实体
    - 类型：[*Entity*](../apis/entity.md)
    
</details>
