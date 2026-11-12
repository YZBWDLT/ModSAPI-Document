---
title: "EnchantmentTypes"
sidebar_label: "EnchantmentTypes"
---

# EnchantmentTypes

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Enchantments.py`；声明补充了静态类型信息。

查询当前原生附魔定义；每次调用重新读取一次目录。

## 获取方式

从服务端入口导入后直接调用静态 get 或 getAll，无需实例化。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [get](#get) | 静态/类方法 |
| [getAll](#getAll) | 静态/类方法 |

## get {#get}

```python
get(enchantmentId: str) -> EnchantmentType | None
```

返回 [EnchantmentType](../../common/reference/EnchantmentType.md) 快照；未注册的标识返回 [None](../../common/type-system.md#none)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enchantmentId` | [str](../../common/type-system.md#str) | `必填` | 传给 [EnchantmentTypes.get](EnchantmentTypes.md#get) 的 enchantmentId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [EnchantmentType](../../common/reference/EnchantmentType.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_get(type_object, enchantmentId):
    return type_object.get(enchantmentId)
```

## getAll {#getAll}

```python
getAll() -> list[EnchantmentType]
```

使用一次原生定义查询返回独立的类型快照列表。

**返回类型：** [list](../../common/type-system.md#list)[[EnchantmentType](../../common/reference/EnchantmentType.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getAll(type_object):
    return type_object.getAll()
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 EnchantmentTypes 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)