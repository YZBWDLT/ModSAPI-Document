---
title: "BlockRaycastOptions"
sidebar_label: "BlockRaycastOptions"
---

# BlockRaycastOptions

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/BlockOptions.py`。

选项通常可直接传 Python 字典；包装类名本身不保证通过模板导出。只使用所属操作已经实现的字段。

沿实体视线方向查找首个相交方块的射线选项。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[BlockFilter](BlockFilter.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `includeLiquidBlock` | 由运行时值确定 | `data['includeLiquidBlock'] if 'includeLiquidBlock' in data else True` |  |
| `includePassableBlocks` | 由运行时值确定 | `data['includePassableBlocks'] if 'includePassableBlocks' in data else True` |  |
| `maxDistance` | 由运行时值确定 | `data['maxDistance'] if 'maxDistance' in data else 32` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [excludePermutations](BlockFilter.md#字段与常量) | [BlockFilter](BlockFilter.md) |
| [excludeTags](BlockFilter.md#字段与常量) | [BlockFilter](BlockFilter.md) |
| [excludeTypes](BlockFilter.md#字段与常量) | [BlockFilter](BlockFilter.md) |
| [includePermutations](BlockFilter.md#字段与常量) | [BlockFilter](BlockFilter.md) |
| [includeTags](BlockFilter.md#字段与常量) | [BlockFilter](BlockFilter.md) |
| [includeTypes](BlockFilter.md#字段与常量) | [BlockFilter](BlockFilter.md) |

## 构造器 {#constructor}

```python
BlockRaycastOptions(data)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 BlockRaycastOptions 对象。
    print(value.includeLiquidBlock)
    print(value.includePassableBlocks)
    print(value.maxDistance)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)