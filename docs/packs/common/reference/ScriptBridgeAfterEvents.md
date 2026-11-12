---
title: "ScriptBridgeAfterEvents"
sidebar_label: "ScriptBridgeAfterEvents"
---

# ScriptBridgeAfterEvents

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/script_bridge.py`；声明补充了静态类型信息。

按 SAPI 风格组织的桥接通知信号集合。

## 获取方式

从 [system.scriptBridge.afterEvents](ScriptBridge.md#afterEvents) 或 [client.scriptBridge.afterEvents](ScriptBridge.md#afterEvents) 获取。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [messageReceive](#messageReceive) | 只读属性 |

## 构造器 {#constructor}

```python
ScriptBridgeAfterEvents(owner)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `owner` | 由值/所属选项确定 | `必填` | 传给 [ScriptBridgeAfterEvents.__init__](ScriptBridgeAfterEvents.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## messageReceive {#messageReceive}

```python
messageReceive: ScriptBridgeMessageSignal
```

接收远端 SAPI 入口发送的通知。

**访问：** 只读。

**返回类型：** [ScriptBridgeMessageSignal](ScriptBridgeMessageSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.messageReceive
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ScriptBridgeAfterEvents 对象。
    print(value.messageReceive)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)