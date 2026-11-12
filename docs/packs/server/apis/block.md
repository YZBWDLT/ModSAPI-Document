---
title: "Block"
sidebar_label: "Block"
---

# Block

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Block.py`；声明补充了静态类型信息。

维度内某个坐标上的方块包装对象。由维度和唯一的 x、y、z 坐标定位，可读取和设置该位置的方块状态。

## 获取方式

使用 `dimension.getBlock(location)`；这是位置包装器，不是不可变方块快照。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [dimension](#dimension) | 只读属性 |
| [location](#location) | 只读属性 |
| [type](#type) | 只读属性 |
| [typeId](#typeId) | 只读属性 |
| [isAir](#isAir) | 只读属性 |
| [isLiquid](#isLiquid) | 只读属性 |
| [isWaterloggeed](#isWaterloggeed) | 只读属性 |
| [permutation](#permutation) | 只读属性 |
| [isWaterlogged](#isWaterlogged) | 只读属性 |
| [x](#x) | 只读属性 |
| [y](#y) | 只读属性 |
| [z](#z) | 只读属性 |
| [above](#above) | 方法 |
| [below](#below) | 方法 |
| [east](#east) | 方法 |
| [west](#west) | 方法 |
| [north](#north) | 方法 |
| [south](#south) | 方法 |
| [bottomCenter](#bottomCenter) | 方法 |
| [setPermutation](#setPermutation) | 方法 |
| [setWaterlogged](#setWaterlogged) | 方法 |
| [getTags](#getTags) | 方法 |
| [hasTag](#hasTag) | 方法 |
| [hasComponent](#hasComponent) | 方法 |
| [getComponent](#getComponent) | 方法 |
| [isValid](#isValid) | 只读属性 |
| [center](#center) | 方法 |
| [offset](#offset) | 方法 |
| [matches](#matches) | 方法 |
| [getItemStack](#getItemStack) | 方法 |
| [getComponents](#getComponents) | 方法 |
| [getLightLevel](#getLightLevel) | 方法 |
| [setType](#setType) | 方法 |

## 构造器 {#constructor}

```python
Block(data)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## dimension {#dimension}

```python
dimension: d.Dimension
```

方块所在的维度。

**访问：** 只读。

**返回类型：** [d.Dimension](dimension.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.dimension
```

## location {#location}

```python
location: Vector3
```

此方块的坐标。

**访问：** 只读。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.location
```

## type {#type}

```python
type: BlockType
```

读取方块类型。

:::note 当前实现说明
每次读取一个原生快照；aux 为网易扩展信息。失效/未加载位置读取会报错。
:::

**访问：** 只读。

**返回类型：** [BlockType](../reference/BlockType.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.type
```

## typeId {#typeId}

```python
typeId: str
```

读取方块类型。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## isAir {#isAir}

```python
isAir: bool
```

方块是否为空气。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isAir
```

## isLiquid {#isLiquid}

```python
isLiquid: bool
```

方块是否为液体方块。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLiquidBlock`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isLiquid
```

## isWaterloggeed {#isWaterloggeed}

```python
isWaterloggeed: bool
```

读取或设置此方块是否含水。

:::note 当前实现说明
拼写兼容别名。新代码使用 isWaterlogged。
:::

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLiquidBlock`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isWaterloggeed
```

## permutation {#permutation}

```python
permutation: BlockPermutation
```

描述此方块的附加配置数据。

**访问：** 只读。

**返回类型：** [BlockPermutation](../reference/BlockPermutation.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.permutation
```

## isWaterlogged {#isWaterlogged}

```python
isWaterlogged: bool
```

读取 `isWaterlogged` 的当前值。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isWaterlogged
```

## x {#x}

```python
x: int
```

方块的 x 坐标。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.x
```

## y {#y}

```python
y: int
```

方块的 y 坐标。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.y
```

## z {#z}

```python
z: int
```

方块的 z 坐标。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.z
```

## above {#above}

```python
above(steps: int = 1) -> Block
```

返回此方块上方的 [Block](block.md)，即 y 轴正方向。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `steps` | [int](../../common/type-system.md#int) | `1` | 传给 [Block.above](block.md#above) 的 steps 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Block](block.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_above(instance):
    return instance.above()
```

## below {#below}

```python
below(steps: int = 1) -> Block
```

返回此方块下方的 [Block](block.md)，即 y 轴负方向。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `steps` | [int](../../common/type-system.md#int) | `1` | 传给 [Block.below](block.md#below) 的 steps 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Block](block.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_below(instance):
    return instance.below()
```

## east {#east}

```python
east(steps: int = 1) -> Block | None
```

返回此方块东侧的 [Block](block.md)，即 x 轴正方向。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `steps` | [int](../../common/type-system.md#int) | `1` | 传给 [Block.east](block.md#east) 的 steps 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Block](block.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_east(instance):
    return instance.east()
```

## west {#west}

```python
west(steps = 1)
```

返回此方块西侧的 [Block](block.md)，即 x 轴负方向。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `steps` | 由值/所属选项确定 | `1` | 传给 [Block.west](block.md#west) 的 steps 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_west(instance):
    return instance.west()
```

## north {#north}

```python
north(steps = 1)
```

返回此方块北侧的 [Block](block.md)，即 z 轴负方向。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `steps` | 由值/所属选项确定 | `1` | 传给 [Block.north](block.md#north) 的 steps 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_north(instance):
    return instance.north()
```

## south {#south}

```python
south(steps = 1)
```

返回此方块南侧的 [Block](block.md)，即 z 轴正方向。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `steps` | 由值/所属选项确定 | `1` | 传给 [Block.south](block.md#south) 的 steps 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_south(instance):
    return instance.south()
```

## bottomCenter {#bottomCenter}

```python
bottomCenter() -> Vector3
```

返回此方块在 x、z 轴上的中心位置，类型为 [Vector3](../extra/vector.md)。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_bottomCenter(instance):
    return instance.bottomCenter()
```

## setPermutation {#setPermutation}

```python
setPermutation(permutation: BlockPermutation) -> None
```

将维度中的此方块设置为指定状态组合。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `permutation` | [BlockPermutation](../reference/BlockPermutation.md) | `必填` | 传给 [Block.setPermutation](block.md#setPermutation) 的 permutation 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'permutation must be a BlockPermutation'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Invalid block states'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBlockAuxValueFromStates`, `SetBlockNew`, `GetLevelId`, `SetBlockStates`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setPermutation(instance, permutation):
    return instance.setPermutation(permutation)
```

## setWaterlogged {#setWaterlogged}

```python
setWaterlogged(waterlogged: bool) -> None
```

设置此方块是否含水。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `waterlogged` | [bool](../../common/type-system.md#bool) | `必填` | 传给 [Block.setWaterlogged](block.md#setWaterlogged) 的 waterlogged 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetLiquidBlock`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setWaterlogged(instance, waterlogged):
    return instance.setWaterlogged(waterlogged)
```

## getTags {#getTags}

```python
getTags() -> list[str]
```

读取方块的标签集合。

**返回类型：** [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBlockTags`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getTags(instance):
    return instance.getTags()
```

## hasTag {#hasTag}

```python
hasTag(tag: str) -> bool
```

检查此方块状态组合是否具有指定标签。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `tag` | [str](../../common/type-system.md#str) | `必填` | 传给 [Block.hasTag](block.md#hasTag) 的 tag 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasTag(instance, tag):
    return instance.hasTag(tag)
```

## hasComponent {#hasComponent}

```python
hasComponent(componentId: str) -> bool
```

检查此方块是否具有指定组件。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `componentId` | [str](../../common/type-system.md#str) | `必填` | 传给 [Block.hasComponent](block.md#hasComponent) 的 componentId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** [Container](container.md)。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasComponent(instance, componentId):
    return instance.hasComponent(componentId)
```

## getComponent {#getComponent}

```python
getComponent(componentId: str) -> BlockComponent
```

读取实体组件，以访问实体的附加能力。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `componentId` | [str](../../common/type-system.md#str) | `必填` | 传给 [Block.getComponent](block.md#getComponent) 的 componentId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [BlockComponent](../reference/BlockComponent.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getComponent(instance, componentId):
    return instance.getComponent(componentId)
```

## isValid {#isValid}

```python
isValid: bool
```

读取 `isValid` 的当前值。底层调用 `GetBlockNew`, `GetLevelId`。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBlockNew`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## center {#center}

```python
center() -> Vector3
```

执行 `center` 操作。参数形态和结果约定如下。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_center(instance):
    return instance.center()
```

## offset {#offset}

```python
offset(offset: Vector3 | tuple | dict) -> Block | None
```

执行 `offset` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `offset` | [Vector3](../extra/vector.md) \| [tuple](../../common/type-system.md#tuple) \| [dict](../../common/type-system.md#dict) | `必填` | 传给 [Block.offset](block.md#offset) 的 offset 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Block](block.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_offset(instance, offset):
    return instance.offset(offset)
```

## matches {#matches}

```python
matches(blockName: str, states: dict | None = None) -> bool
```

检查 `matches` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `blockName` | [str](../../common/type-system.md#str) | `必填` | 方块类型标识，例如 minecraft:stone。 |
| `states` | [dict](../../common/type-system.md#dict) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 方块状态字典；不等价于物品 aux 或方块实体数据。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_matches(instance, blockName):
    return instance.matches(blockName)
```

## getItemStack {#getItemStack}

```python
getItemStack(amount: int = 1, withData: bool = False) -> ItemStack | None
```

读取 `getItemStack` 操作。参数形态和结果约定如下。

:::note 当前实现说明
withData=True 会明确拒绝；没有无损方块实体到物品转换。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `amount` | [int](../../common/type-system.md#int) | `1` | 物品数量；新物品要求 1–255 的整数，并按最大堆叠数限制。 |
| `withData` | [bool](../../common/type-system.md#bool) | `False` | 传给 [Block.getItemStack](block.md#getItemStack) 的 withData 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ItemStack](itemStack.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NotImplementedError](../../common/type-system.md#notimplementederror) | `'ModSDK does not expose a lossless block-to-item conversion'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getItemStack(instance):
    return instance.getItemStack()
```

## getComponents {#getComponents}

```python
getComponents() -> list
```

读取 `getComponents` 操作。参数形态和结果约定如下。

**返回类型：** [list](../../common/type-system.md#list)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getComponents(instance):
    return instance.getComponents()
```

## getLightLevel {#getLightLevel}

```python
getLightLevel() -> int
```

读取 `getLightLevel` 操作。原生实现使用 `GetBlockLightLevel`, `GetLevelId`，行为受网易运行环境约束。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBlockLightLevel`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getLightLevel(instance):
    return instance.getLightLevel()
```

## setType {#setType}

```python
setType(blockType: str | BlockType) -> None
```

设置 `setType` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `blockType` | [str](../../common/type-system.md#str) \| [BlockType](../reference/BlockType.md) | `必填` | 传给 [Block.setType](block.md#setType) 的 blockType 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to change block type'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setType(instance, blockType):
    return instance.setType(blockType)
```

## 使用示例


```python
from ModSAPI.server.beta import world

block = world.getDimension("overworld").getBlock((0, 64, 0))
if block.isValid:
    print(block.typeId, block.permutation.getAllStates())
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)