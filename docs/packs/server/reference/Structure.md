---
title: "Structure"
sidebar_label: "Structure"
---

# Structure

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Structure.py`；声明补充了静态类型信息。

已加载的结构模板，对应 .mcstructure 文件。可通过 /structure 命令或 [StructureManager](StructureManager.md) 将其放置到世界。

## 获取方式

通过结构管理器创建或读取；原生只读结构不一定支持编辑。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `getIsWaterlogged` | 由运行时值确定 | `getIsWaterLogged` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [id](#id) | 只读属性 |
| [entities](#entities) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [size](#size) | 只读属性 |
| [isEditable](#isEditable) | 只读属性 |
| [getBlockPermutation](#getBlockPermutation) | 方法 |
| [getIsWaterLogged](#getIsWaterLogged) | 方法 |
| [saveAs](#saveAs) | 方法 |
| [saveToWorld](#saveToWorld) | 方法 |
| [setBlockPermutation](#setBlockPermutation) | 方法 |
| [getBlockPalette](#getBlockPalette) | 方法 |
| [getEntities](#getEntities) | 方法 |
| [setEntity](#setEntity) | 方法 |

## 构造器 {#constructor}

```python
Structure(data: dict) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | [dict](../../common/type-system.md#dict) | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## id {#id}

```python
id: str
```

结构名称，必须包含命名空间。通过 /structure 命令或结构方块创建时，默认命名空间为 mystructure。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## entities {#entities}

```python
entities: dict
```

读取 `entities` 的当前值。

**访问：** 只读。

**返回类型：** [dict](../../common/type-system.md#dict)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entities
```

## isValid {#isValid}

```python
isValid: bool
```

[Structure](Structure.md) 是否有效；删除后可能失效。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## size {#size}

```python
size: Vector3
```

结构的三维尺寸。例如单方块结构的大小为 x、y、z 均为 1。

**访问：** 只读。

**返回类型：** [Vector3](../extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.size
```

## isEditable {#isEditable}

```python
isEditable: bool
```

此 [Structure](Structure.md) 是否可编辑。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [InvalidStructureError](../../common/reference/InvalidStructureError.md) | `"Structure '%s' has been deleted." % self.__id` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isEditable
```

## getBlockPermutation {#getBlockPermutation}

```python
getBlockPermutation(location: Vector3) -> BlockPermutation
```

读取结构内指定位置的 [BlockPermutation](BlockPermutation.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |

**返回类型：** [BlockPermutation](BlockPermutation.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [StructureUneditableError](../../common/reference/StructureUneditableError.md) | `"Structure '%s' cannot be edited." % self.__id` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBlockStatesFromAuxValue`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getBlockPermutation(instance, location):
    return instance.getBlockPermutation(location)
```

## getIsWaterLogged {#getIsWaterLogged}

```python
getIsWaterLogged(location: Vector3) -> bool
```

读取结构内指定位置的方块是否含水。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [StructureUneditableError](../../common/reference/StructureUneditableError.md) | `"Structure '%s' cannot be edited." % self.__id` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getIsWaterLogged(instance, location):
    return instance.getIsWaterLogged(location)
```

## saveAs {#saveAs}

```python
saveAs(identifier: str, saveMode: StructureSaveMode = StructureSaveMode.World) -> None
```

复制 [Structure](Structure.md)，并以新名称保存。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `saveMode` | [StructureSaveMode](../../common/reference/StructureSaveMode.md) | [StructureSaveMode.World](../apis/world.md) | 传给 [Structure.saveAs](Structure.md#saveAs) 的 saveMode 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [StructureUneditableError](../../common/reference/StructureUneditableError.md) | `"Structure '%s' cannot be edited." % self.__id` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_saveAs(instance, identifier):
    return instance.saveAs(identifier)
```

## saveToWorld {#saveToWorld}

```python
saveToWorld()
```

将修改后的 [Structure](Structure.md) 保存到世界文件。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [StructureUneditableError](../../common/reference/StructureUneditableError.md) | `"Structure '%s' cannot be edited." % self.__id` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_saveToWorld(instance):
    return instance.saveToWorld()
```

## setBlockPermutation {#setBlockPermutation}

```python
setBlockPermutation(location: Vector3, blockPermutation: BlockPermutation = None, waterlogged: bool = False) -> None
```

将结构内指定位置的方块设置为给定 [BlockPermutation](BlockPermutation.md)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `blockPermutation` | [BlockPermutation](BlockPermutation.md) | [None](../../common/type-system.md#none) | 传给 [Structure.setBlockPermutation](Structure.md#setBlockPermutation) 的 blockPermutation 参数；结合上方功能说明和下方调用示例使用。 |
| `waterlogged` | [bool](../../common/type-system.md#bool) | `False` | 传给 [Structure.setBlockPermutation](Structure.md#setBlockPermutation) 的 waterlogged 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [StructureUneditableError](../../common/reference/StructureUneditableError.md) | `"Structure '%s' cannot be edited." % self.__id` |
| [ValueError](../../common/type-system.md#valueerror) | `'Location is outside the structure'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBlockAuxValueFromStates`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setBlockPermutation(instance, location):
    return instance.setBlockPermutation(location)
```

## getBlockPalette {#getBlockPalette}

```python
getBlockPalette(options: StructurePlaceOptions) -> blockPaletteComp.BlockPaletteComponent
```

读取 `getBlockPalette` 操作。原生实现使用 `GetBlankBlockPalette`, `DeserializeBlockPalette`, `GetLevelId`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [StructurePlaceOptions](../../common/reference/StructurePlaceOptions.md) | `必填` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [blockPaletteComp.BlockPaletteComponent](../../common/type-system.md#blockpalettecomponent)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [StructureUneditableError](../../common/reference/StructureUneditableError.md) | `"Structure '%s' cannot be edited." % self.__id` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBlankBlockPalette`, `DeserializeBlockPalette`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getBlockPalette(instance, options):
    return instance.getBlockPalette(options)
```

## getEntities {#getEntities}

```python
getEntities(options: StructurePlaceOptions) -> dict
```

读取 `getEntities` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [StructurePlaceOptions](../../common/reference/StructurePlaceOptions.md) | `必填` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [dict](../../common/type-system.md#dict)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [StructureUneditableError](../../common/reference/StructureUneditableError.md) | `"Structure '%s' cannot be edited." % self.__id` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEntities(instance, options):
    return instance.getEntities(options)
```

## setEntity {#setEntity}

```python
setEntity(location: Vector3, entity: any) -> None
```

在结构内指定位置设置需要包含的实体。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../extra/vector.md) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `entity` | [any](../../common/type-system.md#any) | `必填` | 目标实体句柄；是否接受运行 ID 取决于签名。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [StructureUneditableError](../../common/reference/StructureUneditableError.md) | `"Structure '%s' cannot be edited." % self.__id` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setEntity(instance, location, entity):
    return instance.setEntity(location, entity)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 Structure 对象。
    print(value.id)
    print(value.entities)
    print(value.isValid)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)