---
title: "SuspendableTask"
sidebar_label: "SuspendableTask"
---

# SuspendableTask

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/scheduler.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `fn` | 由运行时值确定 | `generator` |
| `gen` | 由运行时值确定 | `generator() if callable(generator) else iter(generator)` |
| `id` | 由运行时值确定 | [Task.taskId](Task.md#字段与常量) |
| `finished` | 由运行时值确定 | `False` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [callOnce](#callOnce) | 方法 |

## 构造器 {#constructor}

```python
SuspendableTask(generator)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `generator` | 由值/所属选项确定 | `必填` | 可迭代的生成器任务；每一步应及时 yield。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## callOnce {#callOnce}

```python
callOnce()
```

执行 `callOnce` 操作。参数形态和结果约定如下。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_callOnce(instance):
    return instance.callOnce()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 SuspendableTask 对象。
    print(value.fn)
    print(value.gen)
    print(value.id)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)