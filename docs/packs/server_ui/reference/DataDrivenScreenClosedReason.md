---
title: "DataDrivenScreenClosedReason"
sidebar_label: "DataDrivenScreenClosedReason"
---

# DataDrivenScreenClosedReason

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/definitions.py`；声明补充了静态类型信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `ClientClosed` | [str](../../common/type-system.md#str) | `'ClientClosed'` |
| `ServerClosed` | [str](../../common/type-system.md#str) | `'ServerClosed'` |
| `UserBusy` | [str](../../common/type-system.md#str) | `'UserBusy'` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 DataDrivenScreenClosedReason 对象。
    print(value.ClientClosed)
    print(value.ServerClosed)
    print(value.UserBusy)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)