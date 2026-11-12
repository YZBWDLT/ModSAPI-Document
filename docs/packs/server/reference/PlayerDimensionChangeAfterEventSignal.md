---
title: "PlayerDimensionChangeAfterEventSignal"
sidebar_label: "PlayerDimensionChangeAfterEventSignal"
---

# PlayerDimensionChangeAfterEventSignal

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/events/signals/PlayerEventSignals.py`；声明补充了静态类型信息。

管理玩家成功切换维度后的回调。

## 获取方式

通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。

所属信号：[world.afterEvents.playerDimensionChange](../events/afterEvents.md#playerDimensionChange).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [subscribe](#subscribe) | 方法 |

## 构造器 {#constructor}

```python
PlayerDimensionChangeAfterEventSignal()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## subscribe {#subscribe}

```python
subscribe(callback: types.FunctionType) -> None
```

订阅玩家切换维度后的回调。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [types.FunctionType](../../common/type-system.md#functiontype) | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_subscribe(instance, callback):
    return instance.subscribe(callback)
```

## 使用示例


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.playerDimensionChange.subscribe(on_event)

def cleanup():
    world.afterEvents.playerDimensionChange.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)