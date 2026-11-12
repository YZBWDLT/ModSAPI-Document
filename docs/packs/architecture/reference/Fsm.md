---
title: "Fsm"
sidebar_label: "Fsm"
---

# Fsm

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/fsm/deprecated.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[Unreliable](Unreliable.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `states` | 由运行时值确定 | `{name: defaultState}` |
| `defaultState` | 由运行时值确定 | `defaultState` |
| `currentState` | 由运行时值确定 | `defaultState` |
| `currentStateName` | 由运行时值确定 | `name` |
| `defaultStateName` | 由运行时值确定 | `name` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [addState](#addState) | 方法 |
| [addStateMapping](#addStateMapping) | 方法 |
| [getState](#getState) | 方法 |
| [transitionTo](#transitionTo) | 方法 |
| [callUpdate](#callUpdate) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [onError](Unreliable.md#onError) | [Unreliable](Unreliable.md) |
| [tryCall](Unreliable.md#tryCall) | [Unreliable](Unreliable.md) |

## 构造器 {#constructor}

```python
Fsm(defaultState, name = 'default')
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `defaultState` | 由值/所属选项确定 | `必填` | 传给 [Fsm.__init__](Fsm.md#constructor) 的 defaultState 参数；结合上方功能说明和下方调用示例使用。 |
| `name` | 由值/所属选项确定 | `'default'` | 传给 [Fsm.__init__](Fsm.md#constructor) 的 name 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## addState {#addState}

```python
addState(name, stateCls)
```

创建或登记 `addState` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | 由值/所属选项确定 | `必填` | 传给 [Fsm.addState](Fsm.md#addState) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `stateCls` | 由值/所属选项确定 | `必填` | 传给 [Fsm.addState](Fsm.md#addState) 的 stateCls 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addState(instance, name, stateCls):
    return instance.addState(name, stateCls)
```

## addStateMapping {#addStateMapping}

```python
addStateMapping(states)
```

创建或登记 `addStateMapping` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `states` | 由值/所属选项确定 | `必填` | 方块状态字典；不等价于物品 aux 或方块实体数据。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addStateMapping(instance, states):
    return instance.addStateMapping(states)
```

## getState {#getState}

```python
getState(name)
```

读取 `getState` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | 由值/所属选项确定 | `必填` | 传给 [Fsm.getState](Fsm.md#getState) 的 name 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getState(instance, name):
    return instance.getState(name)
```

## transitionTo {#transitionTo}

```python
transitionTo(name)
```

执行 `transitionTo` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | 由值/所属选项确定 | `必填` | 传给 [Fsm.transitionTo](Fsm.md#transitionTo) 的 name 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_transitionTo(instance, name):
    return instance.transitionTo(name)
```

## callUpdate {#callUpdate}

```python
callUpdate()
```

执行 `callUpdate` 操作。参数形态和结果约定如下。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_callUpdate(instance):
    return instance.callUpdate()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 Fsm 对象。
    print(value.states)
    print(value.defaultState)
    print(value.currentState)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)