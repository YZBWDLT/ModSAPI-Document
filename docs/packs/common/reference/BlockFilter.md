---
title: "BlockFilter"
sidebar_label: "BlockFilter"
---

# BlockFilter

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/BlockOptions.py`。

选项通常可直接传 Python 字典；包装类名本身不保证通过模板导出。只使用所属操作已经实现的字段。

根据类型、标签或状态组合包含或排除方块。未设置包含条件时，选择所有未被排除的方块；设置了包含条件时，方块还必须至少匹配一项包含条件。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `excludePermutations` | 由运行时值确定 | `data['excludePermutations'] if 'excludePermutations' in data else None` |  |
| `excludeTags` | 由运行时值确定 | `data['excludeTags'] if 'excludeTags' in data else None` |  |
| `excludeTypes` | 由运行时值确定 | `data['excludeTypes'] if 'excludeTypes' in data else None` |  |
| `includePermutations` | 由运行时值确定 | `data['includePermutations'] if 'includePermutations' in data else None` |  |
| `includeTags` | 由运行时值确定 | `data['includeTags'] if 'includeTags' in data else None` |  |
| `includeTypes` | 由运行时值确定 | `data['includeTypes'] if 'includeTypes' in data else None` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |

## 构造器 {#constructor}

```python
BlockFilter(data)
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
    # value 是上方获取方式取得的 BlockFilter 对象。
    print(value.excludePermutations)
    print(value.excludeTags)
    print(value.excludeTypes)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)