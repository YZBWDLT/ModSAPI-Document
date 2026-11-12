---
title: "BlockPermutation"
sidebar_label: "BlockPermutation"
---

# BlockPermutation

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Block.py`；声明补充了静态类型信息。

描述方块的 [BlockType](BlockType.md) 与属性组合，属性也称方块状态。此对象不绑定到世界中的具体 [Block](../apis/block.md)。

## 获取方式

从 `block.permutation` 读取，或从服务端入口导入 [BlockPermutation](BlockPermutation.md) 并 resolve。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [type](#type) | 只读属性 |
| [getAllStates](#getAllStates) | 方法 |
| [getItemStack](#getItemStack) | 方法 |
| [getState](#getState) | 方法 |
| [getTags](#getTags) | 方法 |
| [hasTag](#hasTag) | 方法 |
| [matches](#matches) | 方法 |
| [resolve](#resolve) | 静态/类方法 |
| [withState](#withState) | 方法 |
| [hasState](#hasState) | 方法 |
| [setState](#setState) | 方法 |

## 构造器 {#constructor}

```python
BlockPermutation(block: Block = None, blockName: str = None, states: dict = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `block` | [Block](../apis/block.md) | [None](../../common/type-system.md#none) | 传给 [BlockPermutation.__init__](BlockPermutation.md#constructor) 的 block 参数；结合上方功能说明和下方调用示例使用。 |
| `blockName` | [str](../../common/type-system.md#str) | [None](../../common/type-system.md#none) | 方块类型标识，例如 minecraft:stone。 |
| `states` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 方块状态字典；不等价于物品 aux 或方块实体数据。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBlockStates`, `GetBlockStatesFromAuxValue`, `GetLevelId`。

## type {#type}

```python
type: BlockType
```

方块类型名称。

**访问：** 只读。

**返回类型：** [BlockType](BlockType.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.type
```

## getAllStates {#getAllStates}

```python
getAllStates() -> dict[str, 0]
```

返回此方块状态组合的全部状态。

**返回类型：** [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), 0]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getAllStates(instance):
    return instance.getAllStates()
```

## getItemStack {#getItemStack}

```python
getItemStack(amount: int = 1) -> ItemStack
```

根据此方块状态组合创建物品堆叠原型，可用于 [Container](../apis/container.md) 和 [ContainerSlot](ContainerSlot.md) 接口。

:::note 当前实现说明
只保留类型和数量，不能保证将状态完整转换成物品 aux/颜色变种。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `amount` | [int](../../common/type-system.md#int) | `1` | 物品数量；新物品要求 1–255 的整数，并按最大堆叠数限制。 |

**返回类型：** [ItemStack](../apis/itemStack.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getItemStack(instance):
    return instance.getItemStack()
```

## getState {#getState}

```python
getState(stateName: str) -> 0
```

读取状态组合中的指定状态。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `stateName` | [str](../../common/type-system.md#str) | `必填` | 方块状态名称。 |

**返回类型：** 0。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getState(instance, stateName):
    return instance.getState(stateName)
```

## getTags {#getTags}

```python
getTags() -> list[str]
```

读取此状态组合的全部标签。

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

检查此状态组合是否具有指定标签。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `tag` | [str](../../common/type-system.md#str) | `必填` | 传给 [BlockPermutation.hasTag](BlockPermutation.md#hasTag) 的 tag 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasTag(instance, tag):
    return instance.hasTag(tag)
```

## matches {#matches}

```python
matches(blockName: str, states: dict = None) -> bool
```

检查指定类型和状态是否匹配当前组合。未提供 states 时，仅按方块类型进行匹配。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `blockName` | [str](../../common/type-system.md#str) | `必填` | 方块类型标识，例如 minecraft:stone。 |
| `states` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 方块状态字典；不等价于物品 aux 或方块实体数据。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_matches(instance, blockName):
    return instance.matches(blockName)
```

## resolve {#resolve}

```python
resolve(blockName: str, states: dict = None) -> BlockPermutation
```

根据类型标识和可选状态生成 [BlockPermutation](BlockPermutation.md)，可传给其他方块接口，例如 block.setPermutation。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `blockName` | [str](../../common/type-system.md#str) | `必填` | 方块类型标识，例如 minecraft:stone。 |
| `states` | [dict](../../common/type-system.md#dict) | [None](../../common/type-system.md#none) | 方块状态字典；不等价于物品 aux 或方块实体数据。 |

**返回类型：** [BlockPermutation](BlockPermutation.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_resolve(type_object, blockName):
    return type_object.resolve(blockName)
```

## withState {#withState}

```python
withState(stateName: str, value: 0) -> BlockPermutation
```

返回修改指定属性后派生的新 [BlockPermutation](BlockPermutation.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `stateName` | [str](../../common/type-system.md#str) | `必填` | 方块状态名称。 |
| `value` | 0 | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [BlockPermutation](BlockPermutation.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_withState(instance, stateName, value):
    return instance.withState(stateName, value)
```

## hasState {#hasState}

```python
hasState(stateName: str) -> bool
```

检查此方块是否具有指定状态。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `stateName` | [str](../../common/type-system.md#str) | `必填` | 方块状态名称。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasState(instance, stateName):
    return instance.hasState(stateName)
```

## setState {#setState}

```python
setState(stateName: str, value: 0) -> bool
```

设置状态值。此方法直接修改当前对象，不返回新的 [BlockPermutation](BlockPermutation.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `stateName` | [str](../../common/type-system.md#str) | `必填` | 方块状态名称。 |
| `value` | 0 | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setState(instance, stateName, value):
    return instance.setState(stateName, value)
```

## 使用示例


```python
from ModSAPI.server.beta import BlockPermutation

permutation = BlockPermutation.resolve("minecraft:stone")
print(permutation.type.id, permutation.getAllStates())
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)