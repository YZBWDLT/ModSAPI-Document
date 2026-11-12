---
title: "Variable"
sidebar_label: "Variable"
---

# Variable

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/ExpressionString.py`；声明补充了静态类型信息。

使用注入时钟的表达式上下文；导入模块时不会创建计时器。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [emmiter_age](#emmiter_age) | 只读属性 |
| [emitter_age](#emitter_age) | 只读属性 |

## 构造器 {#constructor}

```python
Variable(startTick: float = -1, clock: Callable[[], float] | None = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `startTick` | [float](../../common/type-system.md#float) | `-1` | 传给 [Variable.__init__](Variable.md#constructor) 的 startTick 参数；结合上方功能说明和下方调用示例使用。 |
| `clock` | [Callable](../../common/type-system.md#callable)[[], [float](../../common/type-system.md#float)] \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Variable.__init__](Variable.md#constructor) 的 clock 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## emmiter_age {#emmiter_age}

```python
emmiter_age
```

emitter_age 的历史拼写，为兼容已有表达式而保留。

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.emmiter_age
```

## emitter_age {#emitter_age}

```python
emitter_age: int
```

自此表达式上下文创建以来经过的时钟单位数。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.emitter_age
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 Variable 对象。
    print(value.emmiter_age)
    print(value.emitter_age)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)