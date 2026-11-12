---
title: "InvalidObservableError"
sidebar_label: "InvalidObservableError"
---

# InvalidObservableError

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/definitions.py`；声明补充了静态类型信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 InvalidObservableError 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)