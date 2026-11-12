---
title: "AttributeModifierOperation"
sidebar_label: "AttributeModifierOperation"
---

# AttributeModifierOperation

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/AttributeModifier.py`；声明补充了静态类型信息。

这是值对象或结果包装对象，成员通过属性访问；是否接受字典输入由所属操作的签名决定。包装类型不一定是模板入口的直接导出符号。

网易原生属性修饰器支持的运算类型，使用含义明确的字符串。运算次序和各运算的具体计算规则由引擎决定，本库不自行重算。

## 获取方式

从 ModSAPI.server.beta 导入，向属性组件的 addModifier() 或 updateModifier() 传递运算常量。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `Addition` | 由运行时值确定 | `'Addition'` |  |
| `MultiplyBase` | 由运行时值确定 | `'MultiplyBase'` |  |
| `MultiplyTotal` | 由运行时值确定 | `'MultiplyTotal'` |  |
| `Cap` | 由运行时值确定 | `'Cap'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 AttributeModifierOperation 对象。
    print(value.Addition)
    print(value.MultiplyBase)
    print(value.MultiplyTotal)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)