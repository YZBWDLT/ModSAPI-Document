---
title: "EventItemStack"
sidebar_label: "EventItemStack"
---

# EventItemStack

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/event_values.py`；声明补充了静态类型信息。

两端均可使用的只读物品快照，无需引擎查询即可读取 SAPI 风格的 typeId、amount 和完整原生元数据。可从事件中读取，也可创建用于编辑战利品。此类型不同于服务端可修改的 [ItemStack](../../server/apis/itemStack.md)。getItemDict 保留 userData；缺失的原生数据无法凭空恢复。

## 获取方式

从语义化事件读取，或从对应端 beta 导入并创建待写入战利品的值。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [typeId](#typeId) | 只读属性 |
| [amount](#amount) | 只读属性 |
| [getItemDict](#getItemDict) | 方法 |
| [clone](#clone) | 方法 |
| [withAmount](#withAmount) | 方法 |

## 构造器 {#constructor}

```python
EventItemStack(typeId: str, amount: int = 1, data: Optional[dict] = None) -> None
```

校验并创建独立的物品值，不调用开发包。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `typeId` | [str](../type-system.md#str) | `必填` | 带命名空间的实体、物品或资源类型名称。 |
| `amount` | [int](../type-system.md#int) | `1` | 物品数量；新物品要求 1–255 的整数，并按最大堆叠数限制。 |
| `data` | [Optional](../type-system.md#optional)[[dict](../type-system.md#dict)] | [None](../type-system.md#none) | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../type-system.md#valueerror) | `'Create nonempty item snapshots; use an empty loot list to clear drops'` |
| [TypeError](../type-system.md#typeerror) | `'amount must be an integer'` |
| [ValueError](../type-system.md#valueerror) | `'amount must be in [1, 255]'` |
| [TypeError](../type-system.md#typeerror) | `'data must be a dictionary'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## typeId {#typeId}

```python
typeId: str
```

带命名空间的物品标识，例如 minecraft:diamond。

**访问：** 只读。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## amount {#amount}

```python
amount: int
```

原生物品数量，即使已有堆叠超过常规上限也原样保留。

**访问：** 只读。

**返回类型：** [int](../type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.amount
```

## getItemDict {#getItemDict}

```python
getItemDict() -> dict
```

返回原生物品元数据的副本，以便显式调用开发包。

**返回类型：** [dict](../type-system.md#dict)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getItemDict(instance):
    return instance.getItemDict()
```

## clone {#clone}

```python
clone() -> EventItemStack
```

返回另一份独立快照，保留全部原生元数据。

**返回类型：** [EventItemStack](EventItemStack.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clone(instance):
    return instance.clone()
```

## withAmount {#withAmount}

```python
withAmount(amount: int) -> EventItemStack
```

返回数量为 1–255 的新快照，不会修改库存槽位。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `amount` | [int](../type-system.md#int) | `必填` | 物品数量；新物品要求 1–255 的整数，并按最大堆叠数限制。 |

**返回类型：** [EventItemStack](EventItemStack.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_withAmount(instance, amount):
    return instance.withAmount(amount)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EventItemStack 对象。
    print(value.typeId)
    print(value.amount)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)