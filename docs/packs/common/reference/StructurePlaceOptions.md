---
title: "StructurePlaceOptions"
sidebar_label: "StructurePlaceOptions"
---

# StructurePlaceOptions

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/Structure.py`；声明补充了静态类型信息。

选项通常可直接传 Python 字典；包装类名本身不保证通过模板导出。只使用所属操作已经实现的字段。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `animationMode` | [str](../type-system.md#str) | `运行时返回` |  |
| `animationSeconds` | [str](../type-system.md#str) | `运行时返回` |  |
| `includeBlocks` | [bool](../type-system.md#bool) | `运行时返回` |  |
| `includeEntities` | [bool](../type-system.md#bool) | `运行时返回` |  |
| `integrity` | [float](../type-system.md#float) | `运行时返回` |  |
| `integritySeed` | [int](../type-system.md#int) | `运行时返回` |  |
| `mirror` | [StructureMirrorAxis](StructureMirrorAxis.md) | `运行时返回` |  |
| `rotation` | [StructureRotation](StructureRotation.md) | `运行时返回` |  |
| `waterlogged` | [bool](../type-system.md#bool) | `运行时返回` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 StructurePlaceOptions 对象。
    print(value.animationMode)
    print(value.animationSeconds)
    print(value.includeBlocks)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)