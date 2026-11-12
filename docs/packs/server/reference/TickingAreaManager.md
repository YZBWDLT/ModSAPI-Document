---
title: "TickingAreaManager"
sidebar_label: "TickingAreaManager"
---

# TickingAreaManager

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/managers/TickingAreaManager.py`；声明补充了静态类型信息。

管理某维度中由本管理器创建的临时常加载区域，可添加、移除或查询。容量限制独立于命令限制，不能查询或修改其他模组及命令创建的区域。游戏关闭时移除这些区域。当前原生能力仅保证加载，逻辑更新限制见具体方法。

## 获取方式

从 [world.tickingAreaManager](../apis/world.md#tickingAreaManager) 获取。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [chunkCount](#chunkCount) | 只读属性 |
| [maxChunkCount](#maxChunkCount) | 只读属性 |
| [hasCapacity](#hasCapacity) | 方法 |
| [createTickingArea](#createTickingArea) | 方法 |
| [getAllTickingAreas](#getAllTickingAreas) | 方法 |
| [getTickingArea](#getTickingArea) | 方法 |
| [hasTickingArea](#hasTickingArea) | 方法 |
| [removeTickingArea](#removeTickingArea) | 方法 |
| [removeAllTickingAreas](#removeAllTickingAreas) | 方法 |

## 构造器 {#constructor}

```python
TickingAreaManager()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## chunkCount {#chunkCount}

```python
chunkCount: int
```

此管理器当前占用的区块数量。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.chunkCount
```

## maxChunkCount {#maxChunkCount}

```python
maxChunkCount: int
```

允许的最大区块数量；重叠区域的区块也计入总量。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.maxChunkCount
```

## hasCapacity {#hasCapacity}

```python
hasCapacity(options: dict) -> bool
```

检查是否有足够的区块容量；区域长度或宽度超过 255 个区块时也返回 False。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [dict](../../common/type-system.md#dict) | `必填` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasCapacity(instance, options):
    return instance.hasCapacity(options)
```

## createTickingArea {#createTickingArea}

```python
createTickingArea(identifier: str, options: TickingAreaOptions | dict) -> None
```

保持区块加载，就绪后完成不携带结果参数的 [Promise](../../common/reference/Promise.md)。ModSDK 的 SetAddArea 无法启用实体、方块实体或随机刻更新。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `options` | [TickingAreaOptions](../../common/reference/TickingAreaOptions.md) \| [dict](../../common/type-system.md#dict) | `必填` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Ticking area identifier already exists: %s' % identifier` |
| [ValueError](../../common/type-system.md#valueerror) | `"Ticking area exceeds this manager's chunk capacity"` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Failed to create ticking area: %s' % identifier` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLevelId`, `SetAddArea`, `DoTaskOnChunkAsync`, `GetAllAreaKeys`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createTickingArea(instance, identifier, options):
    return instance.createTickingArea(identifier, options)
```

## getAllTickingAreas {#getAllTickingAreas}

```python
getAllTickingAreas() -> list[TickingArea]
```

获取此管理器添加的全部区域。

**返回类型：** [list](../../common/type-system.md#list)[[TickingArea](../../common/reference/TickingArea.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLevelId`, `GetAllAreaKeys`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getAllTickingAreas(instance):
    return instance.getAllTickingAreas()
```

## getTickingArea {#getTickingArea}

```python
getTickingArea(identifier: str) -> TickingArea
```

尝试按标识获取指定区域。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |

**返回类型：** [TickingArea](../../common/reference/TickingArea.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getTickingArea(instance, identifier):
    return instance.getTickingArea(identifier)
```

## hasTickingArea {#hasTickingArea}

```python
hasTickingArea(identifier: str) -> bool
```

检查此管理器是否已包含指定标识。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasTickingArea(instance, identifier):
    return instance.hasTickingArea(identifier)
```

## removeTickingArea {#removeTickingArea}

```python
removeTickingArea(identifier: str) -> None
```

按唯一标识移除指定区域。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Failed to remove ticking area: %s' % identifier` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLevelId`, `DeleteArea`, `GetAllAreaKeys`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeTickingArea(instance, identifier):
    return instance.removeTickingArea(identifier)
```

## removeAllTickingAreas {#removeAllTickingAreas}

```python
removeAllTickingAreas()
```

移除此管理器添加的全部区域。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeAllTickingAreas(instance):
    return instance.removeAllTickingAreas()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 TickingAreaManager 对象。
    print(value.chunkCount)
    print(value.maxChunkCount)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)