---
title: 坐标对象、选项与空结果
---

# 坐标对象、选项与空结果

## 选择坐标对象

| 类型 | 使用场景 | 获取方式 |
| --- | --- | --- |
| [Vector3](../server/extra/vector.md) | 三维位置、方向和偏移 | 从服务端入口导入构造器，或从实体位置等属性读取 |
| [Vector2](../common/reference/Vector2.md) | 二维坐标或俯仰、偏航角 | 读取相关操作的返回值；构造器接受二维字典、序列或同类对象 |
| [VectorXZ](../common/reference/VectorXZ.md) | 水平面上的两个分量 | 按相关操作的约定传入 `{"x": 数值, "z": 数值}`；包装对象具有 `x`、`z` 属性 |
| [DimensionLocation](../common/reference/DimensionLocation.md) | 同时保存维度和三维坐标 | 从服务端入口导入构造器，传入维度对象和坐标 |

这些类型具有对象属性，不等同于只能按键访问的字典。接受选项字典的操作与接受位置的操作各有自己的输入约定，以签名为准。向量构造器负责复制坐标；具体操作仍可能对坐标范围、加载状态等另行校验。

```python
from ModSAPI.server.beta import world, Vector3, DimensionLocation

dimension = world.getDimension("overworld")
original = Vector3((10, 64, 20))
point = DimensionLocation(dimension, original)

original.x = 99
print(point.x)  # 输出 10，坐标已经复制。

point.y = 70
print(point.dimension.id, point.y)
```

修改 [DimensionLocation](../common/reference/DimensionLocation.md) 只改变该值对象，不会移动实体、传送玩家或更改世界。它保留传入的维度对象，不会在每次读取坐标时重新查询维度。

构造和写入坐标时拒绝布尔值、非数值以及无穷大、非数字等非有限数。类型不合法时抛出 [TypeError](../common/type-system.md#typeerror)，非有限数抛出 [ValueError](../common/type-system.md#valueerror)；写入失败保留原坐标。

## 处理没有结果的查询

找不到目标不一定是错误。返回类型含有 [None](../common/type-system.md#none) 时，先判断结果，再读取属性。

```python
def read_speed_duration(entity):
    effect = entity.getEffect("speed")
    if effect is None:
        return 0
    return effect.duration
```

[Entity.getEffect](../server/apis/entity.md#getEffect) 在没有指定效果时返回空值。效果的持续时间单位为刻，可从 [Effect.duration](../server/reference/Effect.md#duration) 读取；类型对象的标准标识符属性为 [EffectType.id](../server/reference/EffectType.md#id)。效果相关操作通常直接接受效果标识符字符串，不需要自行构造内部类型对象。

视线查询没有命中方块时，同样需要处理空结果。部分方块命中的表面方向无法可靠推导，此时 [BlockRaycastHit.face](../common/reference/BlockRaycastHit.md#face) 也可能为空；不要据此伪造一个方向。当前方块视线查询只支持 `maxDistance`；液体、可穿过方块及类型、标签、状态筛选尚未实现，显式设置这些字段会抛出 [UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)。

## 选项字典只填写需要改变的字段

可选字段可以省略。字段是否支持空值、默认行为是什么，由所属操作决定；省略字段与显式传入 [None](../common/type-system.md#none) 并不总是相同。

```python
from ModSAPI.client.beta import client

client.audio.playSound("random.orb", {"volume": 0.5, "pitch": 1.0})
```

该操作播放当前客户端的本地声音；参数与返回句柄见 [Audio.playSound](../client/reference/Audio.md#playSound)。跨模块传递实体、玩家、维度等引用时，使用对应端的包装对象，不把客户端对象当成服务端对象。