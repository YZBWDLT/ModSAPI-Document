---
title: "BlockEventOptions"
sidebar_label: "BlockEventOptions"
---

# BlockEventOptions

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/BlockOptions.py`；声明补充了静态类型信息。

选项通常可直接传 Python 字典；包装类名本身不保证通过模板导出。只使用所属操作已经实现的字段。

方块事件订阅的可选参数。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [permutations](#permutations) | 可读写属性 |
| [blockTypes](#blockTypes) | 可读写属性 |

## 构造器 {#constructor}

```python
BlockEventOptions(data: dict) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | [dict](../type-system.md#dict) | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## permutations {#permutations}

```python
permutations: list[BlockPermutation]
```

设置后，仅当受影响方块的状态组合匹配此条件时触发事件。

**访问：** 可读写。

写入方式：`instance.permutations = value`。参数类型线索：`(data: list[BlockPermutation]) -> None`。

写入参数 `data`：[list](../type-system.md#list)[[BlockPermutation](../../server/reference/BlockPermutation.md)]。

**返回类型：** [list](../type-system.md#list)[[BlockPermutation](../../server/reference/BlockPermutation.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.permutations

def write_value(instance, value):
    instance.permutations = value
```

## blockTypes {#blockTypes}

```python
blockTypes: list[str]
```

设置后，仅当受影响方块的类型匹配此条件时触发事件。

**访问：** 可读写。

写入方式：`instance.blockTypes = value`。参数类型线索：`(data: list[str]) -> None`。

写入参数 `data`：[list](../type-system.md#list)[[str](../type-system.md#str)]。

**返回类型：** [list](../type-system.md#list)[[str](../type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.blockTypes

def write_value(instance, value):
    instance.blockTypes = value
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 BlockEventOptions 对象。
    print(value.permutations)
    print(value.blockTypes)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)