---
title: "ClientEntityInventoryComponent"
sidebar_label: "ClientEntityInventoryComponent"
---

# ClientEntityInventoryComponent

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Inventory.py`；声明补充了静态类型信息。

本地玩家只读背包入口，不提供全部背包 JSON 配置。

## 获取方式

通过本地玩家 getComponent([ClientEntityComponentTypes.Inventory](ClientEntityComponentTypes.md#字段与常量)) 取得；无需主动构造。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `componentId` | 由运行时值确定 | `'minecraft:inventory'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [typeId](#typeId) | 只读属性 |
| [entity](#entity) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [container](#container) | 只读属性 |
| [inventorySize](#inventorySize) | 只读属性 |

## typeId {#typeId}

```python
typeId: str
```

命名空间化的组件标识符，失效后仍可读取。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## entity {#entity}

```python
entity: ClientEntity
```

所属本地客户端实体包装对象。

**访问：** 只读。

**返回类型：** [ClientEntity](ClientEntity.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entity
```

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

## container {#container}

```python
container: ClientContainer
```

取得缓存的只读容器，所属玩家必须仍然有效。

**访问：** 只读。

**返回类型：** [ClientContainer](ClientContainer.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.container
```

## inventorySize {#inventorySize}

```python
inventorySize: int
```

当前原生槽位数量，不假设为固定的原版容量。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.inventorySize
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientEntityInventoryComponent 对象。
    print(value.typeId)
    print(value.entity)
    print(value.isValid)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)