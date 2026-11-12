---
title: "StructureManager"
sidebar_label: "StructureManager"
---

# StructureManager

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/managers/StructureManager.py`；声明补充了静态类型信息。

结构管理器，用于创建、获取、放置和删除结构。

## 获取方式

从 [world.structureManager](../apis/world.md#structureManager) 获取。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [createEmpty](#createEmpty) | 方法 |
| [createFromWorld](#createFromWorld) | 方法 |
| [delete](#delete) | 方法 |
| [getAllEditableStructures](#getAllEditableStructures) | 方法 |
| [get](#get) | 方法 |
| [place](#place) | 方法 |

## 构造器 {#constructor}

```python
StructureManager()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## createEmpty {#createEmpty}

```python
createEmpty(identifier: str, size: Vector3, saveMode: str = StructureSaveMode.Memory) -> Structure
```

在内存中创建空 [Structure](Structure.md)。可通过 [Structure.setBlockPermutation](Structure.md#setBlockPermutation) 填充方块，并用 [Structure.saveAs](Structure.md#saveAs) 保存。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `size` | [Vector3](../extra/vector.md) | `必填` | 传给 [StructureManager.createEmpty](StructureManager.md#createEmpty) 的 size 参数；结合上方功能说明和下方调用示例使用。 |
| `saveMode` | [str](../../common/type-system.md#str) | [StructureSaveMode.Memory](../../common/reference/StructureSaveMode.md#字段与常量) | 传给 [StructureManager.createEmpty](StructureManager.md#createEmpty) 的 saveMode 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Structure](Structure.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Structure size must contain positive integers'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createEmpty(instance, identifier, size):
    return instance.createEmpty(identifier, size)
```

## createFromWorld {#createFromWorld}

```python
createFromWorld(identifier: str, dimension: Dimension, From: Vector3, to: Vector3, options: StructureCreateOptions = None) -> Structure
```

从世界中的方块创建 [Structure](Structure.md)，功能对应 /structure save 命令。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `dimension` | [Dimension](../apis/dimension.md) | `必填` | 传给 [StructureManager.createFromWorld](StructureManager.md#createFromWorld) 的 dimension 参数；结合上方功能说明和下方调用示例使用。 |
| `From` | [Vector3](../extra/vector.md) | `必填` | 传给 [StructureManager.createFromWorld](StructureManager.md#createFromWorld) 的 From 参数；结合上方功能说明和下方调用示例使用。 |
| `to` | [Vector3](../extra/vector.md) | `必填` | 传给 [StructureManager.createFromWorld](StructureManager.md#createFromWorld) 的 to 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [StructureCreateOptions](../../common/reference/StructureCreateOptions.md) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [Structure](Structure.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to read structure blocks'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBlockPaletteBetweenPos`, `SerializeBlockPalette`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createFromWorld(instance, identifier, dimension, From, to):
    return instance.createFromWorld(identifier, dimension, From, to)
```

## delete {#delete}

```python
delete(structure: str | Structure) -> None
```

从内存及世界存储中删除指定结构。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `structure` | [str](../../common/type-system.md#str) \| [Structure](Structure.md) | `必填` | 传给 [StructureManager.delete](StructureManager.md#delete) 的 structure 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetCommand`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_delete(instance, structure):
    return instance.delete(structure)
```

## getAllEditableStructures {#getAllEditableStructures}

```python
getAllEditableStructures() -> list[Structure]
```

获取全部可编辑结构。

**返回类型：** [list](../../common/type-system.md#list)[[Structure](Structure.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getAllEditableStructures(instance):
    return instance.getAllEditableStructures()
```

## get {#get}

```python
get(identifier: str) -> Structure | None
```

获取保存在内存或世界中的 [Structure](Structure.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |

**返回类型：** [Structure](Structure.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetStructureSize`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_get(instance, identifier):
    return instance.get(identifier)
```

## place {#place}

```python
place(structure: Structure | str, dimension: Dimension, location: Vector3, options: StructurePlaceOptions = None) -> None
```

将结构放置到世界，功能对应 /structure load 命令。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `structure` | [Structure](Structure.md) \| [str](../../common/type-system.md#str) | `必填` | 传给 [StructureManager.place](StructureManager.md#place) 的 structure 参数；结合上方功能说明和下方调用示例使用。 |
| `dimension` | [Dimension](../apis/dimension.md) | `必填` | 传给 [StructureManager.place](StructureManager.md#place) 的 dimension 参数；结合上方功能说明和下方调用示例使用。 |
| `location` | [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `options` | [StructurePlaceOptions](../../common/reference/StructurePlaceOptions.md) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [InvalidStructureError](../../common/reference/InvalidStructureError.md) | `"Structure '%s' does not exist in memory or the world." % structure` |
| [ValueError](../../common/type-system.md#valueerror) | `'Structure integrity must be between 0 and 1'` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `"Unable to place structure '%s'" % identifier` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to place structure blocks'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `PlaceStructure`, `SetBlockByBlockPalette`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_place(instance, structure, dimension, location):
    return instance.place(structure, dimension, location)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 StructureManager 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)