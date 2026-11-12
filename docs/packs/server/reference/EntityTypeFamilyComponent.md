---
title: "EntityTypeFamilyComponent"
sidebar_label: "EntityTypeFamilyComponent"
---

import ApiFieldAnchor from '@docusaurus/Link';

# EntityTypeFamilyComponent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/components/EntityComponents.py`；声明补充了静态类型信息。

从引擎读取实体当前的类型族集合。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[EntityComponent](EntityComponent.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-componentId" />`componentId` | 由运行时值确定 | `'minecraft:type_family'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [getTypeFamilies](#getTypeFamilies) | 方法 |
| [hasTypeFamily](#hasTypeFamily) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [entity](EntityComponent.md#entity) | [EntityComponent](EntityComponent.md) |
| [isValid](Component.md#isValid) | [Component](Component.md) |
| [typeId](Component.md#typeId) | [Component](Component.md) |

## getTypeFamilies {#getTypeFamilies}

```python
getTypeFamilies() -> list[str]
```

读取 `getTypeFamilies` 操作。原生实现使用 `GetTypeFamily`，行为受网易运行环境约束。

**返回类型：** [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetTypeFamily`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getTypeFamilies(instance):
    return instance.getTypeFamilies()
```

## hasTypeFamily {#hasTypeFamily}

```python
hasTypeFamily(typeFamily: str) -> bool
```

检查 `hasTypeFamily` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `typeFamily` | [str](../../common/type-system.md#str) | `必填` | 传给 [EntityTypeFamilyComponent.hasTypeFamily](EntityTypeFamilyComponent.md#hasTypeFamily) 的 typeFamily 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasTypeFamily(instance, typeFamily):
    return instance.hasTypeFamily(typeFamily)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EntityTypeFamilyComponent 对象。
    print(value.componentId)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)