---
title: "Motion"
sidebar_label: "Motion"
---

# Motion

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/Vector.py`；声明补充了静态类型信息。

选项通常可直接传 Python 字典；包装类名本身不保证通过模板导出。只使用所属操作已经实现的字段。

运动器

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [type](#type) | 只读属性 |
| [id](#id) | 只读属性 |

## 构造器 {#constructor}

```python
Motion(type, id)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| [type](../type-system.md#type) | 由值/所属选项确定 | `必填` | 传给 [Motion.__init__](Motion.md#constructor) 的 [type](../type-system.md#type) 参数；结合上方功能说明和下方调用示例使用。 |
| `id` | 由值/所属选项确定 | `必填` | 运行标识或类型标识，按本成员的说明传入。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## type {#type}

```python
type
```

读取 [type](../type-system.md#type) 的当前值。

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.type
```

## id {#id}

```python
id
```

读取 `id` 的当前值。

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 Motion 对象。
    print(value.type)
    print(value.id)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)