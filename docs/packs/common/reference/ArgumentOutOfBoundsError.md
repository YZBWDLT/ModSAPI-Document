---
title: "ArgumentOutOfBoundsError"
sidebar_label: "ArgumentOutOfBoundsError"
---

# ArgumentOutOfBoundsError

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/errors/extensions.py`；声明补充了静态类型信息。

数值参数超出了该操作当前的原生边界。

## 获取方式

在参数超出当前原生边界时捕获；它继承 [ValueError](../type-system.md#valueerror)，可继续使用既有 [ValueError](../type-system.md#valueerror) 处理逻辑。

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 ArgumentOutOfBoundsError 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)