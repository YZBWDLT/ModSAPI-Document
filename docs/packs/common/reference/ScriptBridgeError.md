---
title: "ScriptBridgeError"
sidebar_label: "ScriptBridgeError"
---

import ApiFieldAnchor from '@docusaurus/Link';

# ScriptBridgeError

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/bridge_protocol.py`；声明补充了静态类型信息。

桥接失败异常，包含稳定的 code 和可选的远端异常名称 remoteName。

## 获取方式

从模板入口导入以识别桥接失败；code 表示稳定错误码，remoteName 保留远端异常名称。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-code" />`code` | [str](../type-system.md#str) | `code` |  |
| <ApiFieldAnchor id="field-remoteName" />`remoteName` | [Optional](../type-system.md#optional)[[str](../type-system.md#str)] | `remoteName` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |

## 构造器 {#constructor}

```python
ScriptBridgeError(message: str, code: str = 'BRIDGE_ERROR', remoteName: Optional[str] = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `message` | [str](../type-system.md#str) | `必填` | 传给 [ScriptBridgeError.__init__](ScriptBridgeError.md#constructor) 的 message 参数；结合上方功能说明和下方调用示例使用。 |
| `code` | [str](../type-system.md#str) | `'BRIDGE_ERROR'` | 传给 [ScriptBridgeError.__init__](ScriptBridgeError.md#constructor) 的 code 参数；结合上方功能说明和下方调用示例使用。 |
| `remoteName` | [Optional](../type-system.md#optional)[[str](../type-system.md#str)] | [None](../type-system.md#none) | 传给 [ScriptBridgeError.__init__](ScriptBridgeError.md#constructor) 的 remoteName 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ScriptBridgeError 对象。
    print(value.code)
    print(value.remoteName)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)