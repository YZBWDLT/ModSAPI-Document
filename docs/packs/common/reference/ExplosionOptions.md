---
title: "ExplosionOptions"
sidebar_label: "ExplosionOptions"
---

# ExplosionOptions

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/WorldOptions.py`；声明补充了静态类型信息。

选项通常可直接传 Python 字典；包装类名本身不保证通过模板导出。只使用所属操作已经实现的字段。

[Dimension.createExplosion](../../server/apis/dimension.md#createExplosion) 的附加配置选项。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [source](#source) | 可读写属性 |
| [allowUnderwater](#allowUnderwater) | 可读写属性 |
| [breaksBlocks](#breaksBlocks) | 可读写属性 |
| [causesFire](#causesFire) | 可读写属性 |

## 构造器 {#constructor}

```python
ExplosionOptions(data: dict) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | [dict](../type-system.md#dict) | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

## source {#source}

```python
source
```

爆炸的来源实体；可以省略。

**访问：** 可读写。

写入方式：`instance.source = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.source

def write_value(instance, value):
    instance.source = value
```

## allowUnderwater {#allowUnderwater}

```python
allowUnderwater: bool
```

爆炸是否也影响水下区域。

**访问：** 可读写。

写入方式：`instance.allowUnderwater = value`。参数类型线索：`(value: bool) -> None`。

写入参数 `value`：[bool](../type-system.md#bool)。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.allowUnderwater

def write_value(instance, value):
    instance.allowUnderwater = value
```

## breaksBlocks {#breaksBlocks}

```python
breaksBlocks: bool
```

爆炸是否破坏范围内的方块。

**访问：** 可读写。

写入方式：`instance.breaksBlocks = value`。参数类型线索：`(value: bool) -> None`。

写入参数 `value`：[bool](../type-system.md#bool)。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.breaksBlocks

def write_value(instance, value):
    instance.breaksBlocks = value
```

## causesFire {#causesFire}

```python
causesFire: bool
```

设为 True 时，爆炸会在影响范围内或附近产生火焰。

**访问：** 可读写。

写入方式：`instance.causesFire = value`。参数类型线索：`(value: bool) -> None`。

写入参数 `value`：[bool](../type-system.md#bool)。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.causesFire

def write_value(instance, value):
    instance.causesFire = value
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ExplosionOptions 对象。
    print(value.source)
    print(value.allowUnderwater)
    print(value.breaksBlocks)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)