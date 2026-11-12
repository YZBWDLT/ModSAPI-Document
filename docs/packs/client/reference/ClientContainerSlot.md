---
title: "ClientContainerSlot"
sidebar_label: "ClientContainerSlot"
---

# ClientContainerSlot

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Inventory.py`；声明补充了静态类型信息。

实时只读的背包或装备槽位，空槽位仍然有效。

## 获取方式

通过 [ClientContainer.getSlot](ClientContainer.md#getSlot)() 或装备组件 getEquipmentSlot() 取得实时只读槽位。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [isValid](#isValid) | 只读属性 |
| [getItem](#getItem) | 方法 |
| [hasItem](#hasItem) | 方法 |
| [amount](#amount) | 只读属性 |
| [typeId](#typeId) | 只读属性 |

## isValid {#isValid}

```python
isValid: bool
```

所属实体是否有效，背包下标是否仍处于当前范围内。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## getItem {#getItem}

```python
getItem(options: ClientItemReadOptions | None = None) -> ItemStackSnapshot | None
```

重新检查实时来源，读取独立物品快照或 [None](../../common/type-system.md#none)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [ClientItemReadOptions](ClientItemReadOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [ItemStackSnapshot](../../common/reference/ItemStackSnapshot.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getItem(instance):
    return instance.getItem()
```

## hasItem {#hasItem}

```python
hasItem() -> bool
```

当前轻量读取中是否有物品。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasItem(instance):
    return instance.hasItem()
```

## amount {#amount}

```python
amount: int
```

当前数量，空槽时为零；该属性只读。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.amount
```

## typeId {#typeId}

```python
typeId: str
```

当前物品标识符；空槽读取会抛出 [RuntimeError](../../common/type-system.md#runtimeerror)。

:::note 当前实现说明
空槽读取该属性会报告错误；空槽仍可为有效句柄，先检查 hasItem 或 getItem 的可空结果。
:::

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'The client slot is empty'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientContainerSlot 对象。
    print(value.isValid)
    print(value.amount)
    print(value.typeId)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)