---
title: "EffectChangeEvent"
sidebar_label: "EffectChangeEvent"
---

# EffectChangeEvent

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/event_data.py`；声明补充了静态类型信息。

[EffectChangeEvent](EffectChangeEvent.md) 类型的语义事件参数。可通过 nativeEvent 读取原生详情；对象引用按需创建，容器值均为独立副本。

## 获取方式

通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。

所属信号：[world.afterEvents.effectRefresh](../../server/events/afterEvents.md#effectRefresh).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [effect](#effect) | 只读属性 |
| [changeType](#changeType) | 只读属性 |
| [durationSeconds](#durationSeconds) | 只读属性 |
| [nativeEvent](#nativeEvent) | 只读属性 |
| [nativeEventName](#nativeEventName) | 只读属性 |
| [player](#player) | 只读属性 |
| [entity](#entity) | 只读属性 |
| [dimension](#dimension) | 只读属性 |
| [location](#location) | 只读属性 |
| [blockLocation](#blockLocation) | 只读属性 |
| [block](#block) | 只读属性 |

## effect {#effect}

```python
effect: Optional[Effect]
```

效果快照，包含 typeId、以每秒 20 刻换算的 duration 和 amplifier。

**访问：** 只读。

**返回类型：** [Optional](../type-system.md#optional)[[Effect](../../server/reference/Effect.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.effect
```

## changeType {#changeType}

```python
changeType: str
```

变化类型为 Refresh（刷新）或 Remove（移除）；添加效果使用已有的 effectAdd 事件。

**访问：** 只读。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.changeType
```

## durationSeconds {#durationSeconds}

```python
durationSeconds: Optional[int]
```

原生持续时间，单位为秒，保留原生的特殊标记值。

**访问：** 只读。

**返回类型：** [Optional](../type-system.md#optional)[[int](../type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.durationSeconds
```

## nativeEvent {#nativeEvent}

```python
nativeEvent: NativeEventData
```

底层类型化原生事件，包括其原始同步输出字段。

**访问：** 只读。

**返回类型：** [NativeEventData](NativeEventData.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.nativeEvent
```

## nativeEventName {#nativeEventName}

```python
nativeEventName: str
```

准确的原生来源名称；同一信号可能由多个原生事件提供数据。

**访问：** 只读。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.nativeEventName
```

## player {#player}

```python
player: Optional[Union[Player, ClientEntity]]
```

按需创建的玩家对象。客户端的远端玩家使用 [ClientEntity](../../client/reference/ClientEntity.md) 表示。

**访问：** 只读。

**返回类型：** [Optional](../type-system.md#optional)[[Union](../type-system.md#union)[[Player](../../server/apis/player.md), [ClientEntity](../../client/reference/ClientEntity.md)]]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.player
```

## entity {#entity}

```python
entity: Optional[Union[Entity, ClientEntity]]
```

按需创建的实体对象；执行实时原生操作前须检查 isValid。

**访问：** 只读。

**返回类型：** [Optional](../type-system.md#optional)[[Union](../type-system.md#union)[[Entity](../../server/apis/entity.md), [ClientEntity](../../client/reference/ClientEntity.md)]]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entity
```

## dimension {#dimension}

```python
dimension: Optional[Union[Dimension, ClientDimension]]
```

观察到的 [Dimension](../../server/apis/dimension.md) 或 [ClientDimension](../../client/reference/ClientDimension.md)；原生事件未提供维度时为 [None](../type-system.md#none)。

**访问：** 只读。

**返回类型：** [Optional](../type-system.md#optional)[[Union](../type-system.md#union)[[Dimension](../../server/apis/dimension.md), [ClientDimension](../../client/reference/ClientDimension.md)]]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.dimension
```

## location {#location}

```python
location: Optional[Vector3]
```

原生世界位置的副本；仅在已提供时存在，不会实时查询位置。

**访问：** 只读。

**返回类型：** [Optional](../type-system.md#optional)[[Vector3](../../server/extra/vector.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.location
```

## blockLocation {#blockLocation}

```python
blockLocation: Optional[Vector3]
```

原生方块位置的副本；未提供时不会假定为主世界。

**访问：** 只读。

**返回类型：** [Optional](../type-system.md#optional)[[Vector3](../../server/extra/vector.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.blockLocation
```

## block {#block}

```python
block: Optional[EventBlock]
```

坐标已知时返回独立的方块快照，不调用开发包查询。

**访问：** 只读。

**返回类型：** [Optional](../type-system.md#optional)[[EventBlock](EventBlock.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.block
```

## 使用示例


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.effectRefresh.subscribe(on_event)

def cleanup():
    world.afterEvents.effectRefresh.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)