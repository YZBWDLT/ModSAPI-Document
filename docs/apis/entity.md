---
sidebar_position: 3
---

# 实体-Entity

包含一系列实体的操作

本页面可能涵盖错误信息

## 属性 {#属性}

### id {#id}
***只读*** 实体的唯一标识符，在世界加载时保持一致，不可解析其结构
<details>
#### 类型：
#### 示例：
```python
```
</details>

### dimension {#dimension}
***只读*** 实体当前所在的维度对象
<details>
#### 类型：
#### 示例：
```python
```
</details>

### isClimbing {#isClimbing}
***只读*** 是否正在攀爬（如接触梯子或墙壁）
<details>
#### 类型：
#### 示例：
```python
```
</details>

### isFalling {#isFalling}
***只读*** 是否处于下落状态（坠落距离>0）
<details>
#### 类型：
#### 示例：
```python
```
</details>

### isInWater {#isInWater}
***只读*** 实体任何部分是否浸入水中
<details>
#### 类型：
#### 示例：
```python
```
</details>

### isOnGround {#isOnGround}
***只读*** 是否站在固体方块上
<details>
#### 类型：
#### 示例：
```python
```
</details>

### isSleeping {#isSleeping}
***只读*** 是否正在睡觉
<details>
#### 类型：
#### 示例：
```python
```
</details>

### isSneaking {#isSneaking}
***只读*** 是否处于潜行状态
<details>
#### 类型：
#### 示例：
```python
```
</details>

### isSprinting {#isSprinting}
***只读*** 是否处于冲刺状态
<details>
#### 类型：
#### 示例：
```python
```
</details>

### isSwimming {#isSwimming}
***只读*** 是否处于游泳状态
<details>
#### 类型：
#### 示例：
```python
```
</details>

### location {#location}
***可读写*** 实体当前位置坐标
<details>
#### 类型：
#### 示例：
```python
```
</details>

### nameTag {#nameTag}
***可读写*** 实体的显示名称
<details>
#### 类型：
#### 示例：
```python
```
</details>

### health {#health}
***可读写*** 实体当前生命值
<details>
#### 类型：
#### 示例：
```python
```
</details>

### typeId {#typeId}
***只读*** 实体类型标识符（如"minecraft:skeleton"）
<details>
#### 类型：
#### 示例：
```python
```
</details>

## 方法 {#方法}

### addEffect {#addEffect}
给实体添加状态效果
<details>
#### 类型：
#### 示例：
```python
```
</details>

### applyDamage {#applyDamage}
对实体造成伤害
<details>
#### 类型：
#### 示例：
```python
```
</details>

### getComponent {#getComponent}
获取实体组件
<details>
#### 类型：
#### 示例：
```python
```
</details>

### teleport {#teleport}
传送实体到指定位置
<details>
#### 类型：
#### 示例：
```python
```
</details>

### getDynamicProperty {#getDynamicProperty}
获取动态属性值
<details>
#### 类型：
#### 示例：
```python
```
</details>

### setDynamicProperty {#setDynamicProperty}
设置动态属性
<details>
#### 类型：
#### 示例：
```python
```
</details>

### kill {#kill}
杀死实体（会掉落物品）
<details>
#### 类型：
#### 示例：
```python
```
</details>

### remove {#remove}
立即移除实体（不会掉落物品）
<details>
#### 类型：
#### 示例：
```python
```
</details>

### getRotation {#getRotation}
获取实体旋转角度
<details>
#### 类型：
#### 示例：
```python
```
</details>

### setRotation {#setRotation}
设置实体旋转角度
<details>
#### 类型：
#### 示例：
```python
```
</details>

### getVelocity {#getVelocity}
获取实体速度向量
<details>
#### 类型：
#### 示例：
```python
```
</details>

### clearVelocity {#clearVelocity}
重置实体速度
<details>
#### 类型：
#### 示例：
```python
```
</details>

### getViewDirection {#getViewDirection}
获取实体视角方向
<details>
#### 类型：
#### 示例：
```python
```
</details>

### addTag {#addTag}
给实体添加标签
<details>
#### 类型：
#### 示例：
```python
```
</details>

### removeTag {#removeTag}
移除实体标签
<details>
#### 类型：
#### 示例：
```python
```
</details>

### getTags {#getTags}
获取实体所有标签
<details>
#### 类型：
#### 示例：
```python
```
</details>

### hasTag {#hasTag}
检查实体是否有指定标签
<details>
#### 类型：
#### 示例：
```python
```
</details>

### triggerEvent {#triggerEvent}
触发实体事件
<details>
#### 类型：
#### 示例：
```python
```
</details>

### runCommand {#runCommand}
以实体身份执行命令
<details>
#### 类型：
#### 示例：
```python
```
</details>