---
title: "EnchantmentTypeUnknownIdError"
sidebar_label: "EnchantmentTypeUnknownIdError"
---

# EnchantmentTypeUnknownIdError

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/errors/enchant.py`；声明补充了静态类型信息。

当前原生附魔目录中没有该标识。

## 获取方式

捕获未注册附魔标识的查询或修改错误；目录 get 未找到时返回 [None](../type-system.md#none)。

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 EnchantmentTypeUnknownIdError 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)