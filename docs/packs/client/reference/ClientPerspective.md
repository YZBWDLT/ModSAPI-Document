---
title: "ClientPerspective"
sidebar_label: "ClientPerspective"
---

# ClientPerspective

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Camera.py`；声明补充了静态类型信息。

[ClientCamera.perspective](ClientCamera.md#perspective) 接受的命名常量。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `FirstPerson` | [str](../../common/type-system.md#str) | `'FirstPerson'` |
| `ThirdPersonBack` | [str](../../common/type-system.md#str) | `'ThirdPersonBack'` |
| `ThirdPersonFront` | [str](../../common/type-system.md#str) | `'ThirdPersonFront'` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
from ModSAPI.client.beta import client, ClientPerspective

client.camera.perspective = ClientPerspective.FirstPerson
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)