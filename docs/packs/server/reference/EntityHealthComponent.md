---
title: "EntityHealthComponent"
sidebar_label: "EntityHealthComponent"
---

# EntityHealthComponent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/components/EntityComponents.py`；声明补充了静态类型信息。

实体的生命值属性。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[EntityAttributeComponent](EntityAttributeComponent.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `componentId` | [Literal](../../common/type-system.md#literal)['minecraft:health'] | `'minecraft:health'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [currentValue](EntityAttributeComponent.md#currentValue) | [EntityAttributeComponent](EntityAttributeComponent.md) |
| [defaultValue](EntityAttributeComponent.md#defaultValue) | [EntityAttributeComponent](EntityAttributeComponent.md) |
| [effectiveMax](EntityAttributeComponent.md#effectiveMax) | [EntityAttributeComponent](EntityAttributeComponent.md) |
| [effectiveMin](EntityAttributeComponent.md#effectiveMin) | [EntityAttributeComponent](EntityAttributeComponent.md) |
| [entity](EntityComponent.md#entity) | [EntityComponent](EntityComponent.md) |
| [isValid](EntityAttributeComponent.md#isValid) | [EntityAttributeComponent](EntityAttributeComponent.md) |
| [resetToDefaultValue](EntityAttributeComponent.md#resetToDefaultValue) | [EntityAttributeComponent](EntityAttributeComponent.md) |
| [resetToMaxValue](EntityAttributeComponent.md#resetToMaxValue) | [EntityAttributeComponent](EntityAttributeComponent.md) |
| [resetToMinValue](EntityAttributeComponent.md#resetToMinValue) | [EntityAttributeComponent](EntityAttributeComponent.md) |
| [setCurrentValue](EntityAttributeComponent.md#setCurrentValue) | [EntityAttributeComponent](EntityAttributeComponent.md) |
| [setMaxValue](EntityAttributeComponent.md#setMaxValue) | [EntityAttributeComponent](EntityAttributeComponent.md) |
| [typeId](Component.md#typeId) | [Component](Component.md) |

## 构造器 {#constructor}

```python
EntityHealthComponent(data)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EntityHealthComponent 对象。
    print(value.componentId)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)