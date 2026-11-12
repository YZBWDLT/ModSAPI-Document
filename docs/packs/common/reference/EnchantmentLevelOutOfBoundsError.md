---
title: "EnchantmentLevelOutOfBoundsError"
sidebar_label: "EnchantmentLevelOutOfBoundsError"
---

# EnchantmentLevelOutOfBoundsError

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/errors/enchant.py`；声明补充了静态类型信息。

请求等级超出该附魔的注册范围。

## 获取方式

捕获附魔值或组件操作中等级为非正值、超出注册上限的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 EnchantmentLevelOutOfBoundsError 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)