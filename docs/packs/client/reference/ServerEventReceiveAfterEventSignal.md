---
title: "ServerEventReceiveAfterEventSignal"
sidebar_label: "ServerEventReceiveAfterEventSignal"
---

# ServerEventReceiveAfterEventSignal

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/events/signals/SystemEventSignals.py`；声明补充了静态类型信息。

注册用于接收 /scriptevent 命令的事件处理器。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [subscribe](#subscribe) | 方法 |

## 构造器 {#constructor}

```python
ServerEventReceiveAfterEventSignal()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## subscribe {#subscribe}

```python
subscribe(eventName: str, callback: types.FunctionType, options: dict = {}) -> None
```

注册新的脚本事件处理器。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `eventName` | [str](../../common/type-system.md#str) | `必填` | 事件或请求名称，推荐加入自己的命名空间。 |
| `callback` | [types.FunctionType](../../common/type-system.md#functiontype) | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |
| `options` | [dict](../../common/type-system.md#dict) | `{}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_subscribe(instance, eventName, callback):
    return instance.subscribe(eventName, callback)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 ServerEventReceiveAfterEventSignal 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)