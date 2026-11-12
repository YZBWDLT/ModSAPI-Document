---
title: "ScriptBridgeMessageSignal"
sidebar_label: "ScriptBridgeMessageSignal"
---

# ScriptBridgeMessageSignal

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/script_bridge.py`；声明补充了静态类型信息。

桥接通知信号；订阅时复制按完整标识筛选的条件。

## 获取方式

从 scriptBridge.afterEvents.messageReceive 获取，使用 subscribe 和 unsubscribe 管理订阅。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [subscribe](#subscribe) | 方法 |
| [unsubscribe](#unsubscribe) | 方法 |

## 构造器 {#constructor}

```python
ScriptBridgeMessageSignal(owner)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `owner` | 由值/所属选项确定 | `必填` | 传给 [ScriptBridgeMessageSignal.__init__](ScriptBridgeMessageSignal.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## subscribe {#subscribe}

```python
subscribe(callback: Callable[[ScriptBridgeMessage], None], options: Optional[dict] = None) -> Callable[[ScriptBridgeMessage], None]
```

订阅并返回回调，复制可选的完整标识筛选条件。

:::note 当前实现说明
ids 按完整标识匹配，空列表不匹配任何通知；绑定方法可使用同一对象的新方法引用注销。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../type-system.md#callable)[[[ScriptBridgeMessage](ScriptBridgeMessage.md)], [None](../type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |
| `options` | [Optional](../type-system.md#optional)[[dict](../type-system.md#dict)] | [None](../type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [Callable](../type-system.md#callable)[[[ScriptBridgeMessage](ScriptBridgeMessage.md)], [None](../type-system.md#none)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../type-system.md#typeerror) | `'callback must be callable'` |
| [TypeError](../type-system.md#typeerror) | `'options may contain only ids'` |
| [TypeError](../type-system.md#typeerror) | `'ids must be a list or tuple'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_subscribe(instance, callback):
    return instance.subscribe(callback)
```

## unsubscribe {#unsubscribe}

```python
unsubscribe(callback: Callable[[ScriptBridgeMessage], None]) -> None
```

移除回调；也支持同一绑定方法的新引用。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../type-system.md#callable)[[[ScriptBridgeMessage](ScriptBridgeMessage.md)], [None](../type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_unsubscribe(instance, callback):
    return instance.unsubscribe(callback)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 ScriptBridgeMessageSignal 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)