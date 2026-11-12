---
title: "InvalidContainerSlotError"
sidebar_label: "InvalidContainerSlotError"
---

# InvalidContainerSlotError

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/errors/container.py`；声明补充了静态类型信息。

槽位下标非法，或需要物品的操作遇到了空槽。

## 获取方式

捕获非法槽位下标或需要物品却遇到空槽的操作；同时属于 [IndexError](../type-system.md#indexerror)。

基类：[ExtensionError](ExtensionError.md).

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 InvalidContainerSlotError 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)