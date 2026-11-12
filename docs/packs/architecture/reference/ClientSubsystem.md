---
title: "ClientSubsystem"
sidebar_label: "ClientSubsystem"
---

# ClientSubsystem

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/subsystem.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[Subsystem](Subsystem.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [sendServer](#sendServer) | 方法 |
| [spawnEntity](#spawnEntity) | 方法 |
| [destroyEntity](#destroyEntity) | 方法 |
| [createSfx](#createSfx) | 方法 |
| [createParticle](#createParticle) | 方法 |
| [createEffectBind](#createEffectBind) | 方法 |
| [destroySfx](#destroySfx) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [broadcast](Subsystem.md#broadcast) | [Subsystem](Subsystem.md) |
| [canTick](Subsystem.md#field-canTick) | [Subsystem](Subsystem.md) |
| [engine](Subsystem.md#field-engine) | [Subsystem](Subsystem.md) |
| [getEngine](Subsystem.md#getEngine) | [Subsystem](Subsystem.md) |
| [getInstance](Subsystem.md#getInstance) | [Subsystem](Subsystem.md) |
| [getSysName](Subsystem.md#getSysName) | [Subsystem](Subsystem.md) |
| [getSystem](Subsystem.md#getSystem) | [Subsystem](Subsystem.md) |
| [listen](Subsystem.md#listen) | [Subsystem](Subsystem.md) |
| [off](Subsystem.md#off) | [Subsystem](Subsystem.md) |
| [on](Subsystem.md#on) | [Subsystem](Subsystem.md) |
| [onDestroy](Subsystem.md#onDestroy) | [Subsystem](Subsystem.md) |
| [onInit](Subsystem.md#onInit) | [Subsystem](Subsystem.md) |
| [onReady](Subsystem.md#onReady) | [Subsystem](Subsystem.md) |
| [onUpdate](Subsystem.md#onUpdate) | [Subsystem](Subsystem.md) |
| [sysName](Subsystem.md#field-sysName) | [Subsystem](Subsystem.md) |
| [system](Subsystem.md#field-system) | [Subsystem](Subsystem.md) |
| [ticks](Subsystem.md#field-ticks) | [Subsystem](Subsystem.md) |
| [unlisten](Subsystem.md#unlisten) | [Subsystem](Subsystem.md) |

## sendServer {#sendServer}

```python
sendServer(eventName, eventData)
```

执行 `sendServer` 操作。原生实现使用 `NotifyToServer`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `eventName` | 由值/所属选项确定 | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |
| `eventData` | 由值/所属选项确定 | `必填` | 传给 [ClientSubsystem.sendServer](ClientSubsystem.md#sendServer) 的 eventData 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `NotifyToServer`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_sendServer(instance, eventName, eventData):
    return instance.sendServer(eventName, eventData)
```

## spawnEntity {#spawnEntity}

```python
spawnEntity(typeStr, pos, rot)
```

创建或登记 `spawnEntity` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `typeStr` | 由值/所属选项确定 | `必填` | 传给 [ClientSubsystem.spawnEntity](ClientSubsystem.md#spawnEntity) 的 typeStr 参数；结合上方功能说明和下方调用示例使用。 |
| `pos` | 由值/所属选项确定 | `必填` | 传给 [ClientSubsystem.spawnEntity](ClientSubsystem.md#spawnEntity) 的 pos 参数；结合上方功能说明和下方调用示例使用。 |
| `rot` | 由值/所属选项确定 | `必填` | 传给 [ClientSubsystem.spawnEntity](ClientSubsystem.md#spawnEntity) 的 rot 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_spawnEntity(instance, typeStr, pos, rot):
    return instance.spawnEntity(typeStr, pos, rot)
```

## destroyEntity {#destroyEntity}

```python
destroyEntity(entityId)
```

执行 `destroyEntity` 操作。原生实现使用 `DestroyClientEntity`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` | 实体运行 ID；跨回调使用前重新确认实体有效性。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `DestroyClientEntity`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_destroyEntity(instance, entityId):
    return instance.destroyEntity(entityId)
```

## createSfx {#createSfx}

```python
createSfx(path, pos = None, rot = None, scale = None)
```

创建或登记 `createSfx` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `path` | 由值/所属选项确定 | `必填` | 传给 [ClientSubsystem.createSfx](ClientSubsystem.md#createSfx) 的 path 参数；结合上方功能说明和下方调用示例使用。 |
| `pos` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [ClientSubsystem.createSfx](ClientSubsystem.md#createSfx) 的 pos 参数；结合上方功能说明和下方调用示例使用。 |
| `rot` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [ClientSubsystem.createSfx](ClientSubsystem.md#createSfx) 的 rot 参数；结合上方功能说明和下方调用示例使用。 |
| `scale` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [ClientSubsystem.createSfx](ClientSubsystem.md#createSfx) 的 scale 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createSfx(instance, path):
    return instance.createSfx(path)
```

## createParticle {#createParticle}

```python
createParticle(path, pos)
```

创建或登记 `createParticle` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `path` | 由值/所属选项确定 | `必填` | 传给 [ClientSubsystem.createParticle](ClientSubsystem.md#createParticle) 的 path 参数；结合上方功能说明和下方调用示例使用。 |
| `pos` | 由值/所属选项确定 | `必填` | 传给 [ClientSubsystem.createParticle](ClientSubsystem.md#createParticle) 的 pos 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createParticle(instance, path, pos):
    return instance.createParticle(path, pos)
```

## createEffectBind {#createEffectBind}

```python
createEffectBind(path, bindEntity, aniName)
```

创建或登记 `createEffectBind` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `path` | 由值/所属选项确定 | `必填` | 传给 [ClientSubsystem.createEffectBind](ClientSubsystem.md#createEffectBind) 的 path 参数；结合上方功能说明和下方调用示例使用。 |
| `bindEntity` | 由值/所属选项确定 | `必填` | 传给 [ClientSubsystem.createEffectBind](ClientSubsystem.md#createEffectBind) 的 bindEntity 参数；结合上方功能说明和下方调用示例使用。 |
| `aniName` | 由值/所属选项确定 | `必填` | 传给 [ClientSubsystem.createEffectBind](ClientSubsystem.md#createEffectBind) 的 aniName 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createEffectBind(instance, path, bindEntity, aniName):
    return instance.createEffectBind(path, bindEntity, aniName)
```

## destroySfx {#destroySfx}

```python
destroySfx(entityId)
```

执行 `destroySfx` 操作。原生实现使用 `DestroyEntity`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` | 实体运行 ID；跨回调使用前重新确认实体有效性。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `DestroyEntity`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_destroySfx(instance, entityId):
    return instance.destroySfx(entityId)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 ClientSubsystem 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)