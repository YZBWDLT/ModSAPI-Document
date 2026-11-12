---
title: "CustomCommandParamType"
sidebar_label: "CustomCommandParamType"
---

# CustomCommandParamType

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/enums/CustomCommand.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| [BlockType](../../server/reference/BlockType.md) | 由运行时值确定 | `'BlockType'` |  |
| `Boolean` | 由运行时值确定 | `'Boolean'` |  |
| `EntitySelector` | 由运行时值确定 | `'EntitySelector'` |  |
| `EntityType` | 由运行时值确定 | `'EntityType'` |  |
| `Enum` | 由运行时值确定 | `'Enum'` |  |
| `Float` | 由运行时值确定 | `'Float'` |  |
| `Integer` | 由运行时值确定 | `'Integer'` |  |
| [ItemType](../../server/reference/ItemType.md) | 由运行时值确定 | `'ItemType'` |  |
| [Location](../../architecture/reference/Location.md) | 由运行时值确定 | `'Location'` |  |
| `PlayerSelector` | 由运行时值确定 | `'PlayerSelector'` |  |
| `String` | 由运行时值确定 | `'String'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 CustomCommandParamType 对象。
    print(value.BlockType)
    print(value.Boolean)
    print(value.EntitySelector)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)