---
title: "EntityQueryPropertyOptions"
sidebar_label: "EntityQueryPropertyOptions"
---

# EntityQueryPropertyOptions

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/EntityOptions.py`；声明补充了静态类型信息。

选项通常可直接传 Python 字典；包装类名本身不保证通过模板导出。只使用所属操作已经实现的字段。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `exclude` | [bool](../type-system.md#bool) | `data.get('exclude', data.get('exlude', False))` |
| `exlude` | [bool](../type-system.md#bool) | `self.exclude` |
| `propertyId` | [str](../type-system.md#str) | `data['propertyId']` |
| `value` | [bool](../type-system.md#bool) \| [str](../type-system.md#str) \| [EqualsComparison](EqualsComparison.md) \| [GreaterThanComparison](GreaterThanComparison.md) \| [LessThanComparison](LessThanComparison.md) \| [GreaterThanOrEqualsComparison](GreaterThanOrEqualsComparison.md) \| [LessThanOrEqualsComparison](LessThanOrEqualsComparison.md) \| [NotEqualsComparison](NotEqualsComparison.md) \| [RangeComparison](RangeComparison.md) | `data.get('value', None)` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |

## 构造器 {#constructor}

```python
EntityQueryPropertyOptions(data: dict)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | [dict](../type-system.md#dict) | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EntityQueryPropertyOptions 对象。
    print(value.exclude)
    print(value.exlude)
    print(value.propertyId)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)