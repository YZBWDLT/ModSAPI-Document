---
title: "DynamicParticlePattern"
sidebar_label: "DynamicParticlePattern"
---

import ApiFieldAnchor from '@docusaurus/Link';

# DynamicParticlePattern

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/ParticleOptions.py`；声明补充了静态类型信息。

这是值对象或结果包装对象，成员通过属性访问；是否接受字典输入由所属操作的签名决定。包装类型不一定是模板入口的直接导出符号。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-x" />`x` | [ExpressionString](../../client/reference/ExpressionString.md) \| [int](../type-system.md#int) \| [float](../type-system.md#float) | `运行时返回` |  |
| <ApiFieldAnchor id="field-y" />`y` | [ExpressionString](../../client/reference/ExpressionString.md) \| [int](../type-system.md#int) \| [float](../type-system.md#float) | `运行时返回` |  |
| <ApiFieldAnchor id="field-z" />`z` | [ExpressionString](../../client/reference/ExpressionString.md) \| [int](../type-system.md#int) \| [float](../type-system.md#float) | `运行时返回` |  |
| <ApiFieldAnchor id="field-color" />`color` | [tuple](../type-system.md#tuple)[[ExpressionString](../../client/reference/ExpressionString.md) \| [float](../type-system.md#float), [ExpressionString](../../client/reference/ExpressionString.md) \| [float](../type-system.md#float), [ExpressionString](../../client/reference/ExpressionString.md) \| [float](../type-system.md#float)] | `运行时返回` | 图案的 [RGB](../../server/reference/RGB.md) 颜色；每个通道为 0～1 的数值，或求值结果在该范围内的表达式字符串。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 DynamicParticlePattern 对象。
    print(value.x)
    print(value.y)
    print(value.z)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)