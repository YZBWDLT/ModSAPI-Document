---
title: 属性修饰器
---

# 属性修饰器

修饰器由已有的 [EntityAttributeComponent](../server/reference/EntityAttributeComponent.md) 管理，不需要再创建服务或注册系统。生命、移动速度等已支持的服务端属性组件均继承这一组接口。这些方法属于网易扩展；微软稳定版属性组件尚无同名成员。

## 增加生命上限

```python
from ModSAPI.server.beta import AttributeModifierOperation, AttributeModifierOperand

def add_health_bonus(entity):
    health = entity.getComponent("health")
    if health is None:
        return False
    return health.addModifier("demo:health_bonus", 10, {
        "operation": AttributeModifierOperation.Addition,
        "operand": AttributeModifierOperand.Maximum,
    })
```

传入实体或玩家包装对象即可，不需要接触原生组件或实体标识符。修饰器自己的标识符是业务资源名，建议使用模组命名空间，以免与其他模组冲突。添加默认使用加法和最大值，因此也可以写成 `health.addModifier("demo:health_bonus", 10)`。

修改最大值不等于填满当前生命，也不改变本库中定义默认值的写入规则。若另行设置当前值，需要处理该方法的布尔结果和当前边界；不要把上限加成当成一次治疗。

## 查询、更新和移除

| 方法 | 返回结果 | 适用场景 |
| --- | --- | --- |
| addModifier | 布尔值 | 添加指定标识符的修饰器 |
| updateModifier | 布尔值 | 更新已有修饰器的全部字段 |
| getModifiers | [EntityAttributeModifier](../common/reference/EntityAttributeModifier.md) 列表 | 查看此属性的所有修饰器 |
| getModifier | [EntityAttributeModifier](../common/reference/EntityAttributeModifier.md) 或 [None](../common/type-system.md#none) | 读取指定修饰器的完整快照 |
| hasModifier | 布尔值 | 只检查是否存在，无需读取列表 |
| removeModifier | 布尔值 | 只移除自己的指定修饰器 |

```python
def inspect_bonus(health):
    modifier = health.getModifier("demo:health_bonus")
    if modifier is None:
        return None
    return modifier.amount, modifier.operation, modifier.operand

def update_bonus(health, amount):
    return health.updateModifier("demo:health_bonus", amount)

def remove_bonus(health):
    return health.removeModifier("demo:health_bonus")
```

更新接口的选项是完整的新配置。省略 operation、operand 会恢复为 Addition、Maximum，不会自动沿用旧字段。添加不会自动更新已有修饰器，更新也不承诺在不存在时创建；两者都保留引擎返回的正常拒绝结果。存在检查和之后的写入不是事务，业务逻辑仍应处理 False。

[EntityAttributeModifier](../common/reference/EntityAttributeModifier.md) 包含只读的 id、amount、operation、operand。它不保留原生字典或实体引用。引擎中的修饰器改变后，旧快照保持原值；重新查询才能取得新值。`getModifier()` 只执行一次原生列表查询；只需存在性时使用 `hasModifier()`。

## 运算和操作数

[AttributeModifierOptions](../common/reference/AttributeModifierOptions.md) 使用 [AttributeModifierOperation](../common/reference/AttributeModifierOperation.md) 和 [AttributeModifierOperand](../common/reference/AttributeModifierOperand.md) 中的字符串常量，业务层无需填写网易原生数字枚举。

| 运算 | 原生含义 |
| --- | --- |
| Addition | 加法 |
| MultiplyBase | 基础值乘法 |
| MultiplyTotal | 总值乘法 |
| Cap | 上限运算 |

| 操作数 | 影响对象 |
| --- | --- |
| Minimum | 原生最小值 |
| Maximum | 原生最大值 |
| Current | 原生当前值 |

库仅负责校验和映射，由引擎执行运算，不在 Python 中重算整组修饰器。不同运算的叠加次序、基础值含义和 Cap 的具体行为仍需实机核对，不能直接套用 Java 版属性公式。amount 必须为有限数值，可以为零或负值；不接受布尔值、字符串数字、无穷或 NaN。

## 错误和能力边界

错误类型的参数、拼错的选项和未知常量在查询实体或写入引擎前报告。实体或组件失效时拒绝访问；缺少原生方法时抛出 [UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)，原生异常、异常返回类型或损坏的列表数据抛出 [NativeOperationError](../common/reference/NativeOperationError.md)。正常的原生布尔拒绝仍返回 False，不会伪装为成功。

`effectiveMax` 使用原生最大值查询；`effectiveMin` 目前读取 NBT 的 Min，尚未证明其包含所有最小值修饰因素。设置当前值时的预检查也以这个已知最小值为依据。使用 Minimum 修饰器时不能把该读数当成已验证的微软等价结果，实际边界与写入效果仍待实测。

修饰器跨存档、重载和实体卸载后的保留规则尚未核验。网易 `SaveAttr` 属于自定义属性存储，并不是此处的修饰器保存接口，因此库没有增加会造成误解的“保存修饰器”方法。

本页接口已进行离线原生契约检查；多人、持久化和具体运算结果仍待网易游戏实测。其他待补能力见 [ModSDK 功能映射与待补接口](../modsdk-coverage.md)。