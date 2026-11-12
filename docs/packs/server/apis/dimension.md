---
title: "Dimension"
sidebar_label: "Dimension"
---

# Dimension

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Dimension.py`；声明补充了静态类型信息。

世界中的特定维度，例如末地。

## 获取方式

使用 `world.getDimension("overworld")` 等；对象的维度也可从实体或方块读取。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [id](#id) | 只读属性 |
| [dimId](#dimId) | 只读属性 |
| [getBlock](#getBlock) | 方法 |
| [getEntities](#getEntities) | 方法 |
| [getEntitiesFromRay](#getEntitiesFromRay) | 方法 |
| [getEntitiesAtBlockLocation](#getEntitiesAtBlockLocation) | 方法 |
| [getPlayers](#getPlayers) | 方法 |
| [getPlayer](#getPlayer) | 方法 |
| [runCommand](#runCommand) | 方法 |
| [spawnEntity](#spawnEntity) | 方法 |
| [spawnItem](#spawnItem) | 方法 |
| [spawnParticle](#spawnParticle) | 方法 |
| [createExplosion](#createExplosion) | 方法 |
| [isChunkLoaded](#isChunkLoaded) | 方法 |
| [getBlocks](#getBlocks) | 方法 |
| [containsBlock](#containsBlock) | 方法 |
| [fillBlocks](#fillBlocks) | 方法 |
| [setBlockType](#setBlockType) | 方法 |
| [setBlockPermutation](#setBlockPermutation) | 方法 |
| [getLightLevel](#getLightLevel) | 方法 |

## 构造器 {#constructor}

```python
Dimension(dimId: int | str) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `dimId` | [int](../../common/type-system.md#int) \| [str](../../common/type-system.md#str) | `必填` | 传给 [Dimension.__init__](dimension.md#constructor) 的 dimId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Dimension id must be non-negative'` |
| [TypeError](../../common/type-system.md#typeerror) | `'Dimension id must be a number or name'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## id {#id}

```python
id: str
```

维度标识。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## dimId {#dimId}

```python
dimId: int
```

维度编号。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.dimId
```

## getBlock {#getBlock}

```python
getBlock(location: dict | Vector3) -> __b.Block
```

返回指定位置的方块实例。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [dict](../../common/type-system.md#dict) \| [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |

**返回类型：** [__b.Block](block.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** [Block](block.md)。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getBlock(instance, location):
    return instance.getBlock(location)
```

## getEntities {#getEntities}

```python
getEntities(options: dict | EntityQueryOptions = {}) -> list[Entity]
```

查询此维度中的实体。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [dict](../../common/type-system.md#dict) \| [EntityQueryOptions](../../common/reference/EntityQueryOptions.md) | `{}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [list](../../common/type-system.md#list)[[Entity](entity.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEntities(instance):
    return instance.getEntities()
```

## getEntitiesFromRay {#getEntitiesFromRay}

```python
getEntitiesFromRay(location: Vector3 | dict, direction: Vector3 | dict, options: EntityRaycastOptions | dict | None = None) -> list[EntityRaycastHit]
```

读取 `getEntitiesFromRay` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../extra/vector.md) \| [dict](../../common/type-system.md#dict) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `direction` | [Vector3](../extra/vector.md) \| [dict](../../common/type-system.md#dict) | `必填` | 传给 [Dimension.getEntitiesFromRay](dimension.md#getEntitiesFromRay) 的 direction 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [EntityRaycastOptions](../../common/reference/EntityRaycastOptions.md) \| [dict](../../common/type-system.md#dict) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [list](../../common/type-system.md#list)[[EntityRaycastHit](../../common/reference/EntityRaycastHit.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEntitiesFromRay(instance, location, direction):
    return instance.getEntitiesFromRay(location, direction)
```

## getEntitiesAtBlockLocation {#getEntitiesAtBlockLocation}

```python
getEntitiesAtBlockLocation(location: dict | Vector3) -> list[Entity]
```

查询指定位置的实体集合。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [dict](../../common/type-system.md#dict) \| [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |

**返回类型：** [list](../../common/type-system.md#list)[[Entity](entity.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEntitiesInSquareArea`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEntitiesAtBlockLocation(instance, location):
    return instance.getEntitiesAtBlockLocation(location)
```

## getPlayers {#getPlayers}

```python
getPlayers(options: EntityQueryOptions | dict | None = None) -> list[Player]
```

读取 `getPlayers` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [EntityQueryOptions](../../common/reference/EntityQueryOptions.md) \| [dict](../../common/type-system.md#dict) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [list](../../common/type-system.md#list)[[Player](player.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getPlayers(instance):
    return instance.getPlayers()
```

## getPlayer {#getPlayer}

```python
getPlayer(playerId: int | str) -> Player
```

按运行标识获取玩家。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `playerId` | [int](../../common/type-system.md#int) \| [str](../../common/type-system.md#str) | `必填` | 玩家运行 ID，不是玩家显示名称。 |

**返回类型：** [Player](player.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getPlayer(instance, playerId):
    return instance.getPlayer(playerId)
```

## runCommand {#runCommand}

```python
runCommand(commandString: str) -> CommandResult
```

在此维度的上下文中同步执行命令。ModSDK 仅报告成功或失败，因此成功时 successCount 为 1。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `commandString` | [str](../../common/type-system.md#str) | `必填` | 传给 [Dimension.runCommand](dimension.md#runCommand) 的 commandString 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [CommandResult](../reference/CommandResult.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'Command execution failed! Command: %s' % commandString` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetCommand`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_runCommand(instance, commandString):
    return instance.runCommand(commandString)
```

## spawnEntity {#spawnEntity}

```python
spawnEntity(identifier: str, location: dict | Vector3, options: dict | SpawnEntityOptions = SpawnEntityOptions) -> Dimension.__e.Entity
```

在指定位置生成新实体，例如生物。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `location` | [dict](../../common/type-system.md#dict) \| [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `options` | [dict](../../common/type-system.md#dict) \| [SpawnEntityOptions](../../common/reference/SpawnEntityOptions.md) | [SpawnEntityOptions](../../common/reference/SpawnEntityOptions.md) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [Dimension.__e.Entity](entity.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to spawn entity %s' % identifier` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `TriggerCustomEvent`, `SetPersistent`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_spawnEntity(instance, identifier, location):
    return instance.spawnEntity(identifier, location)
```

## spawnItem {#spawnItem}

```python
spawnItem(itemStack: ItemStack, location: Vector3) -> Entity
```

在指定位置将物品堆叠生成为掉落物实体。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemStack` | [ItemStack](itemStack.md) | `必填` | 物品堆叠对象；不是物品名称字符串。 |
| `location` | [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |

**返回类型：** [Entity](entity.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to spawn item'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_spawnItem(instance, itemStack, location):
    return instance.spawnItem(itemStack, location)
```

## spawnParticle {#spawnParticle}

```python
spawnParticle(effectName: str, location: Vector3, molangVariables: MolangVariableMap | None = None)
```

在世界指定位置创建粒子发射器。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `effectName` | [str](../../common/type-system.md#str) | `必填` | 资源包内存在的粒子效果标识。 |
| `location` | [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `molangVariables` | [MolangVariableMap](../reference/MolangVariableMap.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Dimension.spawnParticle](dimension.md#spawnParticle) 的 molangVariables 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_spawnParticle(instance, effectName, location):
    return instance.spawnParticle(effectName, location)
```

## createExplosion {#createExplosion}

```python
createExplosion(location: Vector3 | dict, radius: float, explosionOptions: dict | ExplosionOptions = {}) -> bool
```

在指定位置创建爆炸。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../extra/vector.md) \| [dict](../../common/type-system.md#dict) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `radius` | [float](../../common/type-system.md#float) | `必填` | 传给 [Dimension.createExplosion](dimension.md#createExplosion) 的 radius 参数；结合上方功能说明和下方调用示例使用。 |
| `explosionOptions` | [dict](../../common/type-system.md#dict) \| [ExplosionOptions](../../common/reference/ExplosionOptions.md) | `{}` | 传给 [Dimension.createExplosion](dimension.md#createExplosion) 的 explosionOptions 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Explosion source must be in this dimension'` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'ModSDK explosion requires a source or player in the target dimension'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLevelId`, `GetPlayerList`, `GetEntityDimensionId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createExplosion(instance, location, radius):
    return instance.createExplosion(location, radius)
```

## isChunkLoaded {#isChunkLoaded}

```python
isChunkLoaded(location: Vector3 | tuple | dict) -> bool
```

检查 `isChunkLoaded` 操作。原生实现使用 `CheckChunkState`, `GetLevelId`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../extra/vector.md) \| [tuple](../../common/type-system.md#tuple) \| [dict](../../common/type-system.md#dict) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `CheckChunkState`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_isChunkLoaded(instance, location):
    return instance.isChunkLoaded(location)
```

## getBlocks {#getBlocks}

```python
getBlocks(volume: BlockVolumeBase, options: dict | None = None, allowUnloadedChunks: bool = False) -> ListBlockVolume
```

读取 `getBlocks` 操作。原生实现使用 [ListBlockVolume](../reference/ListBlockVolume.md)，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `volume` | [BlockVolumeBase](../reference/BlockVolumeBase.md) | `必填` | [BlockVolumeBase](../reference/BlockVolumeBase.md) 或其子类型，端点按方块边界处理。 |
| `options` | [dict](../../common/type-system.md#dict) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |
| `allowUnloadedChunks` | [bool](../../common/type-system.md#bool) | `False` | 传给 [Dimension.getBlocks](dimension.md#getBlocks) 的 allowUnloadedChunks 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ListBlockVolume](../reference/ListBlockVolume.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'closest and farthest cannot be combined'` |
| [ValueError](../../common/type-system.md#valueerror) | `'A positive integer count and location are required'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** [ListBlockVolume](../reference/ListBlockVolume.md)。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getBlocks(instance, volume):
    return instance.getBlocks(volume)
```

## containsBlock {#containsBlock}

```python
containsBlock(volume: BlockVolumeBase, filter: dict, allowUnloadedChunks: bool = False) -> bool
```

检查 `containsBlock` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `volume` | [BlockVolumeBase](../reference/BlockVolumeBase.md) | `必填` | [BlockVolumeBase](../reference/BlockVolumeBase.md) 或其子类型，端点按方块边界处理。 |
| `filter` | [dict](../../common/type-system.md#dict) | `必填` | 传给 [Dimension.containsBlock](dimension.md#containsBlock) 的 filter 参数；结合上方功能说明和下方调用示例使用。 |
| `allowUnloadedChunks` | [bool](../../common/type-system.md#bool) | `False` | 传给 [Dimension.containsBlock](dimension.md#containsBlock) 的 allowUnloadedChunks 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_containsBlock(instance, volume, filter):
    return instance.containsBlock(volume, filter)
```

## fillBlocks {#fillBlocks}

```python
fillBlocks(volume: BlockVolumeBase, block: BlockPermutation | str, options: dict | None = None) -> ListBlockVolume
```

使用指定方块类型填充区域。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `volume` | [BlockVolumeBase](../reference/BlockVolumeBase.md) | `必填` | [BlockVolumeBase](../reference/BlockVolumeBase.md) 或其子类型，端点按方块边界处理。 |
| `block` | [BlockPermutation](../reference/BlockPermutation.md) \| [str](../../common/type-system.md#str) | `必填` | 传给 [Dimension.fillBlocks](dimension.md#fillBlocks) 的 block 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [dict](../../common/type-system.md#dict) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [ListBlockVolume](../reference/ListBlockVolume.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'volume must be a BlockVolumeBase'` |
| [TypeError](../../common/type-system.md#typeerror) | `'Invalid block type'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Invalid block states'` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to deserialize fill palette'` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to fill block volume'` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to fill block at %r' % (position.getIntTuple(),)` |
| [UnloadedChunksError](../../common/reference/UnloadedChunksError.md) | `'Fill volume contains an unloaded chunk'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBlankBlockPalette`, [ListBlockVolume](../reference/ListBlockVolume.md), `GetLevelId`, `DeserializeBlockPalette`, `SetBlockByBlockPalette`, `GetBlockAuxValueFromStates`, `SetBlockNew`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_fillBlocks(instance, volume, block):
    return instance.fillBlocks(volume, block)
```

## setBlockType {#setBlockType}

```python
setBlockType(location: Vector3, blockType: str) -> None
```

设置此维度中指定位置的方块。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `blockType` | [str](../../common/type-system.md#str) | `必填` | 传给 [Dimension.setBlockType](dimension.md#setBlockType) 的 blockType 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetBlockNew`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setBlockType(instance, location, blockType):
    return instance.setBlockType(location, blockType)
```

## setBlockPermutation {#setBlockPermutation}

```python
setBlockPermutation(location: Vector3 | tuple | dict, permutation: BlockPermutation) -> None
```

设置 `setBlockPermutation` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../extra/vector.md) \| [tuple](../../common/type-system.md#tuple) \| [dict](../../common/type-system.md#dict) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `permutation` | [BlockPermutation](../reference/BlockPermutation.md) | `必填` | 传给 [Dimension.setBlockPermutation](dimension.md#setBlockPermutation) 的 permutation 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to set block permutation'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setBlockPermutation(instance, location, permutation):
    return instance.setBlockPermutation(location, permutation)
```

## getLightLevel {#getLightLevel}

```python
getLightLevel(location: Vector3 | tuple | dict) -> int
```

读取 `getLightLevel` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../extra/vector.md) \| [tuple](../../common/type-system.md#tuple) \| [dict](../../common/type-system.md#dict) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getLightLevel(instance, location):
    return instance.getLightLevel(location)
```

## 使用示例


```python
from ModSAPI.server.beta import world

dimension = world.getDimension("overworld")
for entity in dimension.getEntities({"type": "minecraft:pig"}):
    print(entity.id)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)