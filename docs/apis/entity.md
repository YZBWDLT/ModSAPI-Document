---
sidebar_position: 3
---

# 实体-Entity

包含一系列实体的操作

注：星号（*）标注的为ModSAPI新增的属性/方法，而SAPI没有

## 属性 {#属性}

### id {#id}
- ***只读*** 实体的唯一标识符
- 类型：str

### dimension {#dimension}
- ***只读*** 实体当前所在的维度对象
<details>

- 类型：[*Dimension*](dimension.md)

#### 示例：
```python
entity.dimension.runCommnad("say 1")
```

</details>

### isClimbing {#isClimbing}
- ***只读*** 是否正在攀爬（如接触梯子或墙壁）

- 类型：bool


### isFalling {#isFalling}
- ***只读*** 是否处于下落状态（坠落距离大于0）

- 类型：bool

### isInWater {#isInWater}
- ***只读*** 实体是否在水中

-  类型：bool

### isOnGround {#isOnGround}
- ***只读*** 是否站在地面上

- 类型：bool

### isSleeping {#isSleeping}
- ***只读*** 是否正在睡觉

- 类型：bool

### isSneaking {#isSneaking}
- ***只读*** 是否处于潜行状态

- 类型：bool

### isSprinting {#isSprinting}
- ***只读*** 是否处于冲刺状态

- 类型：bool

### isSwimming {#isSwimming}
- ***只读*** 是否处于游泳状态

- 类型：bool

### location {#location}
***可读写*** 实体当前位置坐标
<details>

#### 类型：[*Vector3*](../extra/vector.md#Vector3)
#### 示例：
```python
print(entity.location)
```

</details>

### nameTag {#nameTag}
***可读写*** 实体的显示名称
<details>

#### 类型：str
#### 示例：
```python
if not entity.nameTag:
    entity.nameTag = "xxx"
```
</details>

### typeId {#typeId}
- ***只读*** 实体类型（如"minecraft:skeleton"）

- 类型：str

### *health {#health}
***可读写*** 实体生命值
<details>

#### 类型：int
#### 示例：
```python
if entity.health == 1:
    entity.health = 2
```
</details>

## 方法 {#方法}

### addEffect {#addEffect}

添加状态效果

<details>

`addEffect(effectType, duration, options?)`

#### 参数：
- effectType
    - 要添加的状态效果名称
    - 类型：str
- duration
    - 持续时间（单位：刻）
    - 类型：int
- options?
    - 状态选项，包含是否显示粒子效果等信息
    - 类型：[*EntityEffectOptions*](../extra/options.md)

#### 示例：
```python
entity.addEffect("minecraft:night_vision", 300, {"amplifier": 0, "showParticle": True})
```
</details>

### applyDamage {#applyDamage}

对实体造成伤害

<details>

`applyDamage(amount, options?)`

#### 参数：
- amount
    - 伤害值
    - 类型：int
- options?
    - 状态选项，包含伤害类型等信息
    - 类型：[*EntityApplyDamageByProjectileOptions | EntityApplyDamageOptions*](../extra/options.md)

#### 示例：
```python
entity.addEffect("minecraft:night_vision", 300, {"amplifier": 0, "showParticle": True})
```
</details>

### getComponent {#getComponent}

获取实体组件
<details>

#### 类型：
`getComponent(componentId)`
#### 参数：
- componentId
    - 组件ID
    - 类型：str
#### 示例：
```python
```
</details>

### teleport {#teleport}

传送实体到指定位置

<details>

#### 类型：
`teleport(location, teleportOptions?)`
#### 参数：
- location
    - 目标位置
    - 类型：Vector3
- teleportOptions
    - 传送选项
    - 类型：[*TeleportOptions*]
#### 示例：
```python
```
</details>

### getDynamicProperty {#getDynamicProperty}
获取动态属性值
<details>
#### 类型：
`getDynamicProperty(identifier)`
#### 参数：
- identifier
    - 属性标识符
    - 类型：str
#### 示例：
```python
```
</details>

### setDynamicProperty {#setDynamicProperty}
设置动态属性
<details>
#### 类型：
`setDynamicProperty(identifier, value)`
#### 参数：
- identifier
    - 属性标识符
    - 类型：str
- value
    - 属性值
    - 类型：Any
#### 示例：
```python
```
</details>

### kill {#kill}
杀死实体（会掉落物品）
<details>
#### 类型：
`kill()`
#### 参数：无
#### 示例：
```python
```
</details>

### remove {#remove}
立即移除实体（不会掉落物品）
<details>
#### 类型：
`remove()`
#### 参数：无
#### 示例：
```python
```
</details>

### getRotation {#getRotation}
获取实体旋转角度
<details>
#### 类型：
`getRotation()`
#### 参数：无
#### 示例：
```python
```
</details>

### setRotation {#setRotation}
设置实体旋转角度
<details>
#### 类型：
`setRotation(rotation)`
#### 参数：
- rotation
    - 旋转角度
    - 类型：Union[str, Vector2]
#### 示例：
```python
```
</details>

### getVelocity {#getVelocity}
获取实体速度向量
<details>
#### 类型：
`getVelocity()`
#### 参数：无
#### 示例：
```python
```
</details>

### clearVelocity {#clearVelocity}
重置实体速度
<details>
#### 类型：
`clearVelocity()`
#### 参数：无
#### 示例：
```python
```
</details>

### getViewDirection {#getViewDirection}
获取实体视角方向
<details>
#### 类型：
`getViewDirection()`
#### 参数：无
#### 示例：
```python
```
</details>

### addTag {#addTag}
给实体添加标签
<details>
#### 类型：
`addTag(tag)`
#### 参数：
- tag
    - 要添加的标签
    - 类型：str
#### 示例：
```python
```
</details>

### removeTag {#removeTag}
移除实体标签
<details>
#### 类型：
`removeTag(tag)`
#### 参数：
- tag
    - 要移除的标签
    - 类型：str
#### 示例：
```python
```
</details>

### getTags {#getTags}
获取实体所有标签
<details>
#### 类型：
`getTags()`
#### 参数：无
#### 示例：
```python
```
</details>

### hasTag {#hasTag}
检查实体是否有指定标签
<details>
#### 类型：
`hasTag(tag)`
#### 参数：
- tag
    - 要检查的标签
    - 类型：str
#### 示例：
```python
```
</details>

### triggerEvent {#triggerEvent}
触发实体事件
<details>
#### 类型：
`triggerEvent(eventName)`
#### 参数：
- eventName
    - 事件名称
    - 类型：str
#### 示例：
```python
```
</details>

### runCommand {#runCommand}
以实体身份执行命令
<details>
#### 类型：
`runCommand(commandString)`
#### 参数：
- commandString
    - 要执行的命令
    - 类型：str
#### 示例：
```python
```
</details>
