---
title: "UiSubsystem"
sidebar_label: "UiSubsystem"
---

# UiSubsystem

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/subsystem.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[ClientSubsystem](ClientSubsystem.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `ns` | 由运行时值确定 | `'xxx_roninUi_xxx'` |  |
| `inst` | 由运行时值确定 | [None](../../common/type-system.md#none) |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [Destroy](#Destroy) | 方法 |
| [defineUi](#defineUi) | 静态/类方法 |
| [getOrCreate](#getOrCreate) | 静态/类方法 |
| [create](#create) | 静态/类方法 |
| [pushScreen](#pushScreen) | 静态/类方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [broadcast](Subsystem.md#broadcast) | [Subsystem](Subsystem.md) |
| [canTick](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [createEffectBind](ClientSubsystem.md#createEffectBind) | [ClientSubsystem](ClientSubsystem.md) |
| [createParticle](ClientSubsystem.md#createParticle) | [ClientSubsystem](ClientSubsystem.md) |
| [createSfx](ClientSubsystem.md#createSfx) | [ClientSubsystem](ClientSubsystem.md) |
| [destroyEntity](ClientSubsystem.md#destroyEntity) | [ClientSubsystem](ClientSubsystem.md) |
| [destroySfx](ClientSubsystem.md#destroySfx) | [ClientSubsystem](ClientSubsystem.md) |
| [engine](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
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
| [sendServer](ClientSubsystem.md#sendServer) | [ClientSubsystem](ClientSubsystem.md) |
| [spawnEntity](ClientSubsystem.md#spawnEntity) | [ClientSubsystem](ClientSubsystem.md) |
| [sysName](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [system](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [ticks](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [unlisten](Subsystem.md#unlisten) | [Subsystem](Subsystem.md) |

## 构造器 {#constructor}

```python
UiSubsystem(engine, system, params)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `engine` | 由值/所属选项确定 | `必填` | 传给 [UiSubsystem.__init__](UiSubsystem.md#constructor) 的 engine 参数；结合上方功能说明和下方调用示例使用。 |
| `system` | 由值/所属选项确定 | `必填` | 传给 [UiSubsystem.__init__](UiSubsystem.md#constructor) 的 system 参数；结合上方功能说明和下方调用示例使用。 |
| `params` | 由值/所属选项确定 | `必填` | 传给 [UiSubsystem.__init__](UiSubsystem.md#constructor) 的 params 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## Destroy {#Destroy}

```python
Destroy()
```

释放此界面的订阅，仅清除属于自身的实例缓存。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_Destroy(instance):
    return instance.Destroy()
```

## defineUi {#defineUi}

```python
defineUi(uiDef)
```

执行 `defineUi` 操作。原生实现使用 `RegisterUI`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `uiDef` | 由值/所属选项确定 | `必填` | JSON [UI](../../server_ui/reference/UI.md) 定义路径，例如 example.menu，需已存在于资源包。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `RegisterUI`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_defineUi(type_object, uiDef):
    return type_object.defineUi(uiDef)
```

## getOrCreate {#getOrCreate}

```python
getOrCreate(**params)
```

读取 `getOrCreate` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `**params` | 可变参数 | `可省略` | 传给 [UiSubsystem.getOrCreate](UiSubsystem.md#getOrCreate) 的 **params 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getOrCreate(type_object, **params):
    return type_object.getOrCreate(**params)
```

## create {#create}

```python
create(**params)
```

创建或登记 `create` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `**params` | 可变参数 | `可省略` | 传给 [UiSubsystem.create](UiSubsystem.md#create) 的 **params 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_create(type_object, **params):
    return type_object.create(**params)
```

## pushScreen {#pushScreen}

```python
pushScreen(**params)
```

执行 `pushScreen` 操作。原生实现使用 `PushScreen`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `**params` | 可变参数 | `可省略` | 传给 [UiSubsystem.pushScreen](UiSubsystem.md#pushScreen) 的 **params 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `PushScreen`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_pushScreen(type_object, **params):
    return type_object.pushScreen(**params)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UiSubsystem 对象。
    print(value.ns)
    print(value.inst)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)