---
title: "CustomCommandParamType"
sidebar_label: "CustomCommandParamType"
---

import ApiFieldAnchor from '@docusaurus/Link';

# CustomCommandParamType

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/enums/CustomCommand.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-BlockType" />[BlockType](../../server/reference/BlockType.md) | 由运行时值确定 | `'BlockType'` |  |
| <ApiFieldAnchor id="field-Boolean" />`Boolean` | 由运行时值确定 | `'Boolean'` |  |
| <ApiFieldAnchor id="field-EntitySelector" />`EntitySelector` | 由运行时值确定 | `'EntitySelector'` |  |
| <ApiFieldAnchor id="field-EntityType" />`EntityType` | 由运行时值确定 | `'EntityType'` |  |
| <ApiFieldAnchor id="field-Enum" />`Enum` | 由运行时值确定 | `'Enum'` |  |
| <ApiFieldAnchor id="field-Float" />`Float` | 由运行时值确定 | `'Float'` |  |
| <ApiFieldAnchor id="field-Integer" />`Integer` | 由运行时值确定 | `'Integer'` |  |
| <ApiFieldAnchor id="field-ItemType" />[ItemType](../../server/reference/ItemType.md) | 由运行时值确定 | `'ItemType'` |  |
| <ApiFieldAnchor id="field-Location" />[Location](../../architecture/reference/Location.md) | 由运行时值确定 | `'Location'` |  |
| <ApiFieldAnchor id="field-PlayerSelector" />`PlayerSelector` | 由运行时值确定 | `'PlayerSelector'` |  |
| <ApiFieldAnchor id="field-String" />`String` | 由运行时值确定 | `'String'` |  |

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