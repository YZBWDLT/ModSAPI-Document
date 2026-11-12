---
title: "CustomCommandErrorReason"
sidebar_label: "CustomCommandErrorReason"
---

import ApiFieldAnchor from '@docusaurus/Link';

# CustomCommandErrorReason

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/enums/stable.py`；声明补充了静态类型信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-AlreadyRegistered" />`AlreadyRegistered` | [str](../type-system.md#str) | `'AlreadyRegistered'` |  |
| <ApiFieldAnchor id="field-EnumDependencyMissing" />`EnumDependencyMissing` | [str](../type-system.md#str) | `'EnumDependencyMissing'` |  |
| <ApiFieldAnchor id="field-NamespaceMismatch" />`NamespaceMismatch` | [str](../type-system.md#str) | `'NamespaceMismatch'` |  |
| <ApiFieldAnchor id="field-ParameterLimit" />`ParameterLimit` | [str](../type-system.md#str) | `'ParameterLimit'` |  |
| <ApiFieldAnchor id="field-RegistryInvalid" />`RegistryInvalid` | [str](../type-system.md#str) | `'RegistryInvalid'` |  |
| <ApiFieldAnchor id="field-RegistryReadOnly" />`RegistryReadOnly` | [str](../type-system.md#str) | `'RegistryReadOnly'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 CustomCommandErrorReason 对象。
    print(value.AlreadyRegistered)
    print(value.EnumDependencyMissing)
    print(value.NamespaceMismatch)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)