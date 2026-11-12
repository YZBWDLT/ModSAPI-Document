---
title: "PlayerBreakBlockBeforeEvent"
sidebar_label: "PlayerBreakBlockBeforeEvent"
---

# PlayerBreakBlockBeforeEvent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/events/core/BlockEvents.py`；声明补充了静态类型信息。

玩家破坏方块前的事件信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[BlockEvent](BlockEvent.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [player](#player) | 只读属性 |
| [brokenBlockPermutation](#brokenBlockPermutation) | 只读属性 |
| [itemStackBeforeBreak](#itemStackBeforeBreak) | 只读属性 |
| [cancel](#cancel) | 可读写属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [block](BlockEvent.md#block) | [BlockEvent](BlockEvent.md) |
| [dimension](BlockEvent.md#dimension) | [BlockEvent](BlockEvent.md) |

## 构造器 {#constructor}

```python
PlayerBreakBlockBeforeEvent(data)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBlockStatesFromAuxValue`, `GetLevelId`。

## player {#player}

```python
player: Player
```

破坏此方块的玩家。

**访问：** 只读。

**返回类型：** [Player](../apis/player.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.player
```

## brokenBlockPermutation {#brokenBlockPermutation}

```python
brokenBlockPermutation
```

方块被破坏前的状态组合。

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.brokenBlockPermutation
```

## itemStackBeforeBreak {#itemStackBeforeBreak}

```python
itemStackBeforeBreak
```

破坏方块前用于破坏的物品堆叠；空手时为 [None](../../common/type-system.md#none)。

**访问：** 只读。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.itemStackBeforeBreak
```

## cancel {#cancel}

```python
cancel
```

读取 `cancel` 的当前值。

**访问：** 可读写。

写入方式：`instance.cancel = value`。参数类型线索：`(value: bool) -> None`。

写入参数 `value`：[bool](../../common/type-system.md#bool)。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.cancel

def write_value(instance, value):
    instance.cancel = value
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 PlayerBreakBlockBeforeEvent 对象。
    print(value.player)
    print(value.brokenBlockPermutation)
    print(value.itemStackBeforeBreak)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)