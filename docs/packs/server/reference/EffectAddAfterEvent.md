---
title: "EffectAddAfterEvent"
sidebar_label: "EffectAddAfterEvent"
---

# EffectAddAfterEvent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/events/core/EntityEvents.py`；声明补充了静态类型信息。

向实体添加状态效果时的信息，例如添加中毒效果。

## 获取方式

通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。

所属信号：[world.afterEvents.effectAdd](../events/afterEvents.md#effectAdd).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [effect](#effect) | 只读属性 |
| [entity](#entity) | 只读属性 |

## 构造器 {#constructor}

```python
EffectAddAfterEvent(data)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## effect {#effect}

```python
effect: Effect
```

效果的属性及详细信息。

**访问：** 只读。

**返回类型：** [Effect](Effect.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.effect
```

## entity {#entity}

```python
entity: Entity
```

正在被添加效果的实体。

**访问：** 只读。

**返回类型：** [Entity](../apis/entity.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entity
```

## 使用示例


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.effectAdd.subscribe(on_event)

def cleanup():
    world.afterEvents.effectAdd.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)