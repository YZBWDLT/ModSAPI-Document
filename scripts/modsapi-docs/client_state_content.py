"""Chinese usage guidance for synchronized client entity and player state."""

CLIENT_STATE_GUIDES = {
    'packs/guides/client-entity-state.md': r'''---
title: 客户端实体、属性与玩家状态
---

# 客户端实体、属性与玩家状态

通过 [client.localPlayer](../client/apis/manager.md#localPlayer) 取得本地 [ClientPlayer](../client/reference/ClientPlayer.md)，通过 [client.getEntity](../client/apis/manager.md#getEntity) 或事件取得已加载的 [ClientEntity](../client/reference/ClientEntity.md)。客户端读取的是本机可见、已同步的状态，不保证与服务端同一时刻的结果一致；跨维度或距离过远的实体可能不再有效。

## 读取生命与移动属性

属性使用组件对象，不要求业务代码记忆网易属性枚举。

```python
from ModSAPI.client.beta import client, ClientEntityComponentTypes

player = client.localPlayer
health = player.getComponent(ClientEntityComponentTypes.Health)
if health is not None:
    print(health.currentValue, health.effectiveMax)

for component in player.getComponents():
    print(component.typeId, component.currentValue)
```

[getComponent](../client/reference/ClientEntity.md#getComponent) 返回只读的 [ClientEntityAttributeComponent](../client/reference/ClientEntityAttributeComponent.md)，支持以下 [ClientEntityComponentTypes](../client/reference/ClientEntityComponentTypes.md)：

| 常量 | 标识符 | 含义 |
| --- | --- | --- |
| Health | minecraft:health | 已同步的生命值 |
| Movement | minecraft:movement | 已同步的基础移动速度 |
| UnderwaterMovement | minecraft:underwater_movement | 已同步的水中移动速度 |
| LavaMovement | minecraft:lava_movement | 已同步的岩浆移动速度 |

也可以使用 `"health"` 或 `"minecraft:health"`。支持的属性在该实体上不存在时返回 [None](../common/type-system.md#none)，零值不会被当作不存在。[hasComponent](../client/reference/ClientEntity.md#hasComponent) 接受同一组标识符；未适配的标识符会抛出 [UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)，不会以 `False` 冒充“不存在”。

[getComponents](../client/reference/ClientEntity.md#getComponents) 只枚举上述可读取属性，不是行为包 JSON 的全部组件清单。整批查询使用一个原生属性组件，并只检查一次实体可见性；返回对象在每次读取值时重新查询，不缓存陈旧数值。

组件保留所属 `entity` 包装对象。实体消失或属性被移除后，`isValid` 变为 `False`，继续读取当前值或最大值会报告失效。组件没有客户端写入方法，也没有伪造默认值、最小值。攻击伤害、击退抗性和跳跃强度没有可靠同步到客户端，因此不在这组接口中。

## 位置、朝向、速度与空气

```python
from ModSAPI.client.beta import client

player = client.localPlayer
position = player.location
rotation = player.getRotation()
velocity = player.getVelocity()
direction = player.getViewDirection()
print(position.x, rotation.y, velocity.y, direction.z)
```

| 读取方式 | 返回值与约定 |
| --- | --- |
| [location](../client/reference/ClientEntity.md#location) | 脚底位置，返回独立 [Vector3](../server/extra/vector.md) |
| [getRotation](../client/reference/ClientEntity.md#getRotation) | 独立 [Vector2](../common/reference/Vector2.md)，x 为俯仰角、y 为偏航角，单位为度 |
| [getViewDirection](../client/reference/ClientEntity.md#getViewDirection) | 按原生头部旋转换算的世界方向 |
| [getVelocity](../client/reference/ClientEntity.md#getVelocity) | 客户端上一帧的原生运动向量，不包含服务端摩擦计算 |
| [bodyRotation](../client/reference/ClientEntity.md#bodyRotation) | 身体偏航角，单位为度；没有身体时原生返回零 |
| [collisionBoxSize](../client/reference/ClientEntity.md#collisionBoxSize) | Vector2，x 为碰撞箱宽度、y 为高度 |
| [airSupplyTicks](../client/reference/ClientEntity.md#airSupplyTicks) | 当前空气储备，以每秒二十个逻辑刻计量，保留可能的负值 |
| [maxAirSupplyTicks](../client/reference/ClientEntity.md#maxAirSupplyTicks) | 同单位的最大空气储备 |

空气值是服务端同步结果；非生物实体可能得到原生默认值，不能用它判断某个行为组件是否存在。[isOnGround](../client/reference/ClientEntity.md#isOnGround) 和 [isInLava](../client/reference/ClientEntity.md#isInLava) 也只反映本机已加载实体。新建本地实体在下一次引擎更新前可能返回默认的着地状态；骑乘中的生物也会被原生接口视为着地。

## 关联实体直接返回对象

```python
from ModSAPI.client.beta import client

ridden = client.localPlayer.getRidingEntity()
if ridden is not None:
    print(ridden.typeId, ridden.location)

def describe_target(entity):
    target = entity.getTarget()
    owner = entity.getOwner()
    return target, owner
```

[getTarget](../client/reference/ClientEntity.md#getTarget)、[getOwner](../client/reference/ClientEntity.md#getOwner) 和 [getRidingEntity](../client/reference/ClientPlayer.md#getRidingEntity) 返回 ClientEntity 或 None，不暴露原生查询返回的标识符和失败哨兵。结果指向本地玩家时复用 `client.localPlayer`；未加载的关联对象返回空值。非本地玩家使用普通客户端实体句柄，不会取得仅适用于本地玩家的写入操作。

坐骑查询优先使用原生骑乘组件，旧客户端缺少该方法时使用兼容查询。原生调用报错时直接报告，不以另一种查询掩盖故障。

## 本地玩家状态与经验

ClientPlayer 提供只读的 `isGliding`、`isInWater`、`isMoving`、`isRiding`、`isSneaking`、`isSprinting`、`isSwimming`、`isInScaffolding`、`isOnLadder` 和 `isFishing`。其中 `isSprinting` 表示正在疾跑，静止时为 False；`isOnLadder` 仅覆盖梯子和藤蔓，不被包装成涵盖所有攀爬情形的属性。

`armorValue` 读取原生护甲显示值，`hunger` 读取饥饿点数，不会据此推算饱和度。

```python
from ModSAPI.client.beta import client

player = client.localPlayer
earned = player.xpEarnedAtCurrentLevel
required = player.totalXpNeededForNextLevel
total = player.getTotalXp()
print(earned, required, total)
```

[xpEarnedAtCurrentLevel](../client/reference/ClientPlayer.md#xpEarnedAtCurrentLevel) 是当前等级内的绝对经验，不是百分比；[totalXpNeededForNextLevel](../client/reference/ClientPlayer.md#totalXpNeededForNextLevel) 是完成当前等级需要的总量，不是还差多少。[getTotalXp](../client/reference/ClientPlayer.md#getTotalXp) 读取原生总经验；原生失败哨兵会转换为错误。没有根据经验反推一个可能不适用的玩家等级，也不把该结果解释为历史上获得过的全部经验。

## 本地写入的作用范围

[ClientPlayer.setVelocity](../client/reference/ClientPlayer.md#setVelocity) 替换本地玩家的运动向量，不是叠加冲量。频繁写入可能与服务端运动计算不一致；多人玩法的权威移动应由服务端处理。[swingArm](../client/reference/ClientPlayer.md#swingArm) 仅播放原版攻击挥手动作，不会实际攻击目标。[setShieldActive](../client/reference/ClientPlayer.md#setShieldActive) 请求本地盾牌状态；没有手持盾牌时返回 False，原生设置失败会抛出错误。

[ClientEntity.teleport](../client/reference/ClientEntity.md#teleport) 和 [setRotation](../client/reference/ClientEntity.md#setRotation) 只接受 `client.spawnEntity` 返回的本地实体句柄。它们不移动服务端实体或本地玩家，也不提供跨维度传送。旋转对象可直接在读取、创建和写入之间传递：

```python
from ModSAPI.client.beta import client

def create_visual(type_id, position):
    visual = client.spawnEntity(type_id, position, {
        "rotation": client.localPlayer.getRotation(),
    })
    visual.setRotation({"x": 0, "y": 90})
    visual.teleport(position)
    return visual
```

调用方需要提供原生支持的实体资源，并在所属流程结束时调用 `visual.remove()`。位置和旋转在写入前校验、复制；布尔值、非有限数、缺失坐标和无效形状会被拒绝。

## 在视图就绪时读取

```python
from ModSAPI.client.beta import client

def ready(event):
    health = client.localPlayer.getComponent("health")
    label = event.view.getControl("/panel/health", "label")
    label.text = u"暂无生命属性" if health is None else unicode(health.currentValue)

client.ui.registerView("demo:status", "demo_ui.screen", {"onReady": ready})
```

示例只在就绪时读取一次，后续刷新由业务事件或按钮交互触发；不会自动按帧轮询所有状态。界面模板、打开时机和清理规则见[界面、控件与生命周期](managed-ui.md)。

原生异常、畸形返回值以及组件创建失败会保留具体操作名称；失效对象报告 [InvalidClientObjectError](../common/reference/InvalidClientObjectError.md)。本页接口已完成离线原生契约和回归测试，平台表现、资源渲染及多人同步仍需游戏实测。完整待补范围见 [ModSDK 功能映射与待补接口](../modsdk-coverage.md)。
''',
}

CLIENT_STATE_ACQUIRE = {
    'ClientEntityAttributeComponent': '通过 ClientEntity 或 ClientPlayer 的 getComponent(...) 取得，只读并保留所属客户端实体。使用前处理 None，后续按需检查 isValid。',
    'ClientEntityComponentTypes': '从 ModSAPI.client.beta 导入；选择本机能够读取的生命及陆地、水中、岩浆移动属性。',
}

CLIENT_STATE_NOTES = {
    'ClientEntity.getComponents': '只列出当前适配的四类已同步属性，不是行为包 JSON 的完整组件清单。一次查询复用一个原生属性组件，不会通过结果伪造其他组件的存在性。',
    'ClientEntity.getComponent': '支持 health、movement、underwater_movement 和 lava_movement，可带 minecraft: 前缀。已支持但不存在时返回 None，未支持的标识符抛出 UnsupportedFeatureError。客户端组件只读。',
    'ClientEntity.teleport': '仅修改 client.spawnEntity 返回的本地实体；其他句柄抛出 UnsupportedFeatureError。原生位置约定保持不变，不提供服务端或跨维度传送。',
    'Client.spawnEntity': 'rotation 同时接受 getRotation() 返回的 Vector2、两个分量的序列或包含 x、y 的字典，统一复制为原生俯仰、偏航元组。',
}
