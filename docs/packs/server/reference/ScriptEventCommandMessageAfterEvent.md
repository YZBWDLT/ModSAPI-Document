---
title: "ScriptEventCommandMessageAfterEvent"
sidebar_label: "ScriptEventCommandMessageAfterEvent"
---

# ScriptEventCommandMessageAfterEvent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/events/core/WorldEvents.py`；声明补充了静态类型信息。

从全局指令字符串解析的事件快照，来源信息使用对象引用。id 和 message 均从完整指令读取；消息保留原文，不解析 JSON，也不展开选择器。全局指令钩子不提供非玩家角色对话发起者的信息。

## 获取方式

通过 [system.afterEvents.scriptEventReceive](SystemAfterEvents.md#scriptEventReceive) 的订阅回调取得。具体解析规则和示例见脚本指令事件指南。

所属信号：[system.afterEvents.scriptEventReceive](SystemAfterEvents.md#scriptEventReceive).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [id](#id) | 只读属性 |
| [message](#message) | 只读属性 |
| [initiator](#initiator) | 只读属性 |
| [sourceEntity](#sourceEntity) | 只读属性 |
| [sourceBlock](#sourceBlock) | 只读属性 |
| [sourceType](#sourceType) | 只读属性 |

## 构造器 {#constructor}

```python
ScriptEventCommandMessageAfterEvent(data)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Expected a valid scriptevent command string'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## id {#id}

```python
id: str
```

从执行指令字符串解析出的带命名空间的事件标识。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## message {#message}

```python
message: str
```

消息原文，保留内部空白和末尾空白。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.message
```

## initiator {#initiator}

```python
initiator: Entity | None
```

始终为 [None](../../common/type-system.md#none)；全局指令钩子不提供对话发起者。

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**访问：** 只读。

**返回类型：** [Entity](../apis/entity.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## sourceEntity {#sourceEntity}

```python
sourceEntity: Entity | None
```

命令由实体触发时的来源实体，例如非玩家角色。

**访问：** 只读。

**返回类型：** [Entity](../apis/entity.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.sourceEntity
```

## sourceBlock {#sourceBlock}

```python
sourceBlock: Block | None
```

命令由方块触发时的来源方块，例如命令方块。

**访问：** 只读。

**返回类型：** [Block](../apis/block.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.sourceBlock
```

## sourceType {#sourceType}

```python
sourceType: ScriptEventSource
```

触发命令的来源类型。

**访问：** 只读。

**返回类型：** [ScriptEventSource](../../common/reference/ScriptEventSource.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.sourceType
```

## 使用示例


```python
from ModSAPI.server.beta import system

def on_event(event):
    print(event)

system.afterEvents.scriptEventReceive.subscribe(on_event)

def cleanup():
    system.afterEvents.scriptEventReceive.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)