---
title: "AttributeModifierOperand"
sidebar_label: "AttributeModifierOperand"
---

import ApiFieldAnchor from '@docusaurus/Link';

# AttributeModifierOperand

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/AttributeModifier.py`；声明补充了静态类型信息。

这是值对象或结果包装对象，成员通过属性访问；是否接受字典输入由所属操作的签名决定。包装类型不一定是模板入口的直接导出符号。

修饰器所影响的原生属性值。

## 获取方式

从 ModSAPI.server.beta 导入，选择修饰原生最小值、最大值或当前值。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-Minimum" />`Minimum` | 由运行时值确定 | `'Minimum'` |  |
| <ApiFieldAnchor id="field-Maximum" />`Maximum` | 由运行时值确定 | `'Maximum'` |  |
| <ApiFieldAnchor id="field-Current" />`Current` | 由运行时值确定 | `'Current'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 AttributeModifierOperand 对象。
    print(value.Minimum)
    print(value.Maximum)
    print(value.Current)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)