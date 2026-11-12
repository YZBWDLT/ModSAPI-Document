---
title: "Scheduler"
sidebar_label: "Scheduler"
---

# Scheduler

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/scheduler.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `scheduleSequence` | 由运行时值确定 | `('BeforeUpdate', 'Update', 'AfterUpdate')` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [execute](#execute) | 方法 |
| [executeAsync](#executeAsync) | 方法 |
| [addTask](#addTask) | 方法 |
| [addSuspendableTask](#addSuspendableTask) | 方法 |
| [removeTask](#removeTask) | 方法 |
| [executeSequence](#executeSequence) | 方法 |
| [executeSequenceAsync](#executeSequenceAsync) | 方法 |
| [runTimer](#runTimer) | 方法 |
| [run](#run) | 方法 |

## 构造器 {#constructor}

```python
Scheduler()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## execute {#execute}

```python
execute(scheduleName)
```

执行 `execute` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `scheduleName` | 由值/所属选项确定 | `必填` | 传给 [Scheduler.execute](Scheduler.md#execute) 的 scheduleName 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_execute(instance, scheduleName):
    return instance.execute(scheduleName)
```

## executeAsync {#executeAsync}

```python
executeAsync(scheduleName: str) -> Future
```

执行 `executeAsync` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `scheduleName` | [str](../../common/type-system.md#str) | `必填` | 传给 [Scheduler.executeAsync](Scheduler.md#executeAsync) 的 scheduleName 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Future](Future.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_executeAsync(instance, scheduleName):
    return instance.executeAsync(scheduleName)
```

## addTask {#addTask}

```python
addTask(scheduleName: str, fn: FunctionType) -> int
```

创建或登记 `addTask` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `scheduleName` | [str](../../common/type-system.md#str) | `必填` | 传给 [Scheduler.addTask](Scheduler.md#addTask) 的 scheduleName 参数；结合上方功能说明和下方调用示例使用。 |
| `fn` | [FunctionType](../../common/type-system.md#functiontype) | `必填` | 传给 [Scheduler.addTask](Scheduler.md#addTask) 的 fn 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addTask(instance, scheduleName, fn):
    return instance.addTask(scheduleName, fn)
```

## addSuspendableTask {#addSuspendableTask}

```python
addSuspendableTask(scheduleName: str, generator: GeneratorType) -> int
```

创建或登记 `addSuspendableTask` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `scheduleName` | [str](../../common/type-system.md#str) | `必填` | 传给 [Scheduler.addSuspendableTask](Scheduler.md#addSuspendableTask) 的 scheduleName 参数；结合上方功能说明和下方调用示例使用。 |
| `generator` | [GeneratorType](../../common/type-system.md#generatortype) | `必填` | 可迭代的生成器任务；每一步应及时 yield。 |

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addSuspendableTask(instance, scheduleName, generator):
    return instance.addSuspendableTask(scheduleName, generator)
```

## removeTask {#removeTask}

```python
removeTask(scheduleName: str, taskId: int = -1) -> None
```

移除或清理 `removeTask` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `scheduleName` | [str](../../common/type-system.md#str) | `必填` | 传给 [Scheduler.removeTask](Scheduler.md#removeTask) 的 scheduleName 参数；结合上方功能说明和下方调用示例使用。 |
| `taskId` | [int](../../common/type-system.md#int) | `-1` | 传给 [Scheduler.removeTask](Scheduler.md#removeTask) 的 taskId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeTask(instance, scheduleName):
    return instance.removeTask(scheduleName)
```

## executeSequence {#executeSequence}

```python
executeSequence()
```

返回 [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [int](../../common/type-system.md#int)]，依次为时间增量 deltaTime 和跳过的更新次数 skippedUpdates。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_executeSequence(instance):
    return instance.executeSequence()
```

## executeSequenceAsync {#executeSequenceAsync}

```python
executeSequenceAsync() -> Future[tuple[float, int], Exception]
```

执行 `executeSequenceAsync` 操作。参数形态和结果约定如下。

**返回类型：** [Future](Future.md)[[tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [int](../../common/type-system.md#int)], [Exception](../../common/type-system.md#exception)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_executeSequenceAsync(instance):
    return instance.executeSequenceAsync()
```

## runTimer {#runTimer}

```python
runTimer(fn, ticks = 1, interval = False)
```

执行 `runTimer` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fn` | 由值/所属选项确定 | `必填` | 传给 [Scheduler.runTimer](Scheduler.md#runTimer) 的 fn 参数；结合上方功能说明和下方调用示例使用。 |
| `ticks` | 由值/所属选项确定 | `1` | 等待请求单位，正整数；每单位换算 0.05 秒。 |
| `interval` | 由值/所属选项确定 | `False` | 传给 [Scheduler.runTimer](Scheduler.md#runTimer) 的 interval 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_runTimer(instance, fn):
    return instance.runTimer(fn)
```

## run {#run}

```python
run(fn)
```

执行 `run` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fn` | 由值/所属选项确定 | `必填` | 传给 [Scheduler.run](Scheduler.md#run) 的 fn 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_run(instance, fn):
    return instance.run(fn)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 Scheduler 对象。
    print(value.scheduleSequence)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)