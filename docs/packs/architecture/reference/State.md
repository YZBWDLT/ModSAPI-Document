---
title: "State"
sidebar_label: "State"
---

# State

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/fsm/deprecated.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `entityId` | 由运行时值确定 | `fsm.entityId` |  |
| `fsm` | 由运行时值确定 | `fsm` |  |
| `stateTime` | 由运行时值确定 | `0` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [onEnter](#onEnter) | 方法 |
| [onExit](#onExit) | 方法 |
| [onUpdate](#onUpdate) | 方法 |
| [canEnter](#canEnter) | 方法 |
| [getFsm](#getFsm) | 方法 |
| [markVariant](#markVariant) | 方法 |
| [movement](#movement) | 方法 |
| [camera](#camera) | 方法 |

## 构造器 {#constructor}

```python
State(fsm)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fsm` | 由值/所属选项确定 | `必填` | 传给 [State.__init__](State.md#constructor) 的 fsm 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## onEnter {#onEnter}

```python
onEnter()
```

当前没有功能性实现，不应依赖此成员完成操作。

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## onExit {#onExit}

```python
onExit()
```

当前没有功能性实现，不应依赖此成员完成操作。

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## onUpdate {#onUpdate}

```python
onUpdate()
```

当前没有功能性实现，不应依赖此成员完成操作。

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## canEnter {#canEnter}

```python
canEnter()
```

执行 `canEnter` 操作。参数形态和结果约定如下。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_canEnter(instance):
    return instance.canEnter()
```

## getFsm {#getFsm}

```python
getFsm()
```

读取 `getFsm` 操作。参数形态和结果约定如下。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getFsm(instance):
    return instance.getFsm()
```

## markVariant {#markVariant}

```python
markVariant(value = None)
```

执行 `markVariant` 操作。原生实现使用 `GetMarkVariant`, `SetMarkVariant`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `value` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetMarkVariant`, `SetMarkVariant`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_markVariant(instance):
    return instance.markVariant()
```

## movement {#movement}

```python
movement(enabled = True)
```

执行 `movement` 操作。原生实现使用 `SetCommand`, `TriggerCustomEvent`, `GetEngineType`, `ResetToDefaultValue`, `SetAttrValue`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enabled` | 由值/所属选项确定 | `True` | 传给 [State.movement](State.md#movement) 的 enabled 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetCommand`, `TriggerCustomEvent`, `GetEngineType`, `ResetToDefaultValue`, `SetAttrValue`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_movement(instance):
    return instance.movement()
```

## camera {#camera}

```python
camera(enabled = True)
```

执行 `camera` 操作。原生实现使用 `SetCommand`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enabled` | 由值/所属选项确定 | `True` | 传给 [State.camera](State.md#camera) 的 enabled 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetCommand`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_camera(instance):
    return instance.camera()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 State 对象。
    print(value.entityId)
    print(value.fsm)
    print(value.stateTime)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)