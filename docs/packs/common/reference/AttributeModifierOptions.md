---
title: "AttributeModifierOptions"
sidebar_label: "AttributeModifierOptions"
---

# AttributeModifierOptions

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/AttributeModifier.py`；声明补充了静态类型信息。

:::info 字典结构或静态声明
此类型只出现在补全声明中，不是可从模板直接实例化的运行时类。作为选项时使用符合字段约定的 Python 字典。
:::

原生修饰器选项；省略字段时使用 Addition 运算和 Maximum 操作数。

## 获取方式

添加或更新修饰器时传入字典；可设置 operation 和 operand，默认分别为 Addition 和 Maximum。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `operation` | [str](../type-system.md#str) | `可选字段；省略规则见所属操作` | [AttributeModifierOperation](AttributeModifierOperation.md) 中支持的字符串常量。 |
| `operand` | [str](../type-system.md#str) | `可选字段；省略规则见所属操作` | [AttributeModifierOperand](AttributeModifierOperand.md) 中支持的字符串常量。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_options(options):
    print(options.get('operation'))
    print(options.get('operand'))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)