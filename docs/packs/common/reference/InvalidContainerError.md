---
title: "InvalidContainerError"
sidebar_label: "InvalidContainerError"
---

# InvalidContainerError

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/errors/container.py`；声明补充了静态类型信息。

容器或所属会话已不可使用。

## 获取方式

捕获失效容器或所属会话的访问错误。

基类：[ExtensionError](ExtensionError.md).

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 InvalidContainerError 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)