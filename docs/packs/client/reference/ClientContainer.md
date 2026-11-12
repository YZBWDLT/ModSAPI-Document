---
title: "ClientContainer"
sidebar_label: "ClientContainer"
---

# ClientContainer

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Inventory.py`；声明补充了静态类型信息。

实时只读的本地玩家背包，容量来自原生结果。不长期缓存物品或容量。检查多个槽位时优先使用 getItems，一次完成批量读取；单格完整读取先查询轻量边界，再使用 GetPlayerItem 获取目标格数据。

## 获取方式

通过本地玩家的背包组件 container 属性取得。只读，不提供客户端写入方法。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [isValid](#isValid) | 只读属性 |
| [size](#size) | 只读属性 |
| [emptySlotsCount](#emptySlotsCount) | 只读属性 |
| [getItem](#getItem) | 方法 |
| [getItems](#getItems) | 方法 |
| [getSlot](#getSlot) | 方法 |
| [firstEmptySlot](#firstEmptySlot) | 方法 |
| [firstItem](#firstItem) | 方法 |

## isValid {#isValid}

```python
isValid: bool
```

所属实体是否可见且仍为本地玩家。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## size {#size}

```python
size: int
```

通过不包含 userData 的原生批量结果读取当前槽位数量。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.size
```

## emptySlotsCount {#emptySlotsCount}

```python
emptySlotsCount: int
```

使用一次轻量原生批量查询统计空槽位。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.emptySlotsCount
```

## getItem {#getItem}

```python
getItem(slot: int, options: ClientItemReadOptions | None = None) -> ItemStackSnapshot | None
```

读取一个独立物品或 [None](../../common/type-system.md#none)，查询前检查当前边界。includeUserData 默认 True；False 复用轻量边界查询，避免第二次原生调用。空槽正常返回 [None](../../common/type-system.md#none)，原生数据损坏时报告 [NativeOperationError](../../common/reference/NativeOperationError.md)，不会把错误数据当作空槽。

:::note 当前实现说明
完整读取先执行轻量边界查询，再取目标格的完整元数据；轻量读取复用边界查询。需要多个槽位时应使用 getItems。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `slot` | [int](../../common/type-system.md#int) | `必填` | 零起始槽位索引，必须在容器容量内。 |
| `options` | [ClientItemReadOptions](ClientItemReadOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [ItemStackSnapshot](../../common/reference/ItemStackSnapshot.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetPlayerItem`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getItem(instance, slot):
    return instance.getItem(slot)
```

## getItems {#getItems}

```python
getItems(options: ClientItemReadOptions | None = None) -> list[ItemStackSnapshot | None]
```

一次读取全部槽位，返回独立列表并保留 [None](../../common/type-system.md#none) 和槽位顺序。includeUserData 默认 True；不需要嵌套原生数据时可传入 False。结果为快照，不是实时容器，也不与之后的背包读取构成事务。

:::note 当前实现说明
一次原生批量查询，保留 [None](../../common/type-system.md#none) 和真实槽位顺序。includeUserData=False 可省略嵌套数据，不会在以后自动恢复。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `options` | [ClientItemReadOptions](ClientItemReadOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [list](../../common/type-system.md#list)[[ItemStackSnapshot](../../common/reference/ItemStackSnapshot.md) \| [None](../../common/type-system.md#none)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getItems(instance):
    return instance.getItems()
```

## getSlot {#getSlot}

```python
getSlot(slot: int) -> ClientContainerSlot
```

校验当前边界后取得实时只读槽位句柄。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `slot` | [int](../../common/type-system.md#int) | `必填` | 零起始槽位索引，必须在容器容量内。 |

**返回类型：** [ClientContainerSlot](ClientContainerSlot.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getSlot(instance, slot):
    return instance.getSlot(slot)
```

## firstEmptySlot {#firstEmptySlot}

```python
firstEmptySlot() -> int | None
```

使用一次轻量批量查询返回首个空槽下标，未找到返回 [None](../../common/type-system.md#none)。

**返回类型：** [int](../../common/type-system.md#int) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_firstEmptySlot(instance):
    return instance.firstEmptySlot()
```

## firstItem {#firstItem}

```python
firstItem() -> int | None
```

使用一次轻量批量查询返回首个有物品的槽位下标，未找到返回 [None](../../common/type-system.md#none)。

**返回类型：** [int](../../common/type-system.md#int) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_firstItem(instance):
    return instance.firstItem()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientContainer 对象。
    print(value.isValid)
    print(value.size)
    print(value.emptySlotsCount)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)