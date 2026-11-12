---
title: "WorldEntityLootAfterEvent"
sidebar_label: "WorldEntityLootAfterEvent"
---

# WorldEntityLootAfterEvent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/NativeEventTypes.py`；声明补充了静态类型信息。

此类型由运行时事件契约创建，并通过对应端的 `beta` 导出。通过 `subscribe` 回调取得实例；不要自行构造事件参数。

[EntityDieLoottableAfterServerEvent](../native-events.md#entitydieloottableafterserverevent) 的事件参数；同步分发结束后不能再写入输出字段。

## 获取方式

通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。

所属信号：[world.afterEvents.entityLoot](../events/afterEvents.md#entityLoot).

基类：[NativeEventData](../../common/reference/NativeEventData.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [deadEntity](#deadEntity) | 只读属性 |
| [attacker](#attacker) | 只读属性 |
| [itemList](#itemList) | 只读属性 |
| [itemEntities](#itemEntities) | 只读属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [getNativeData](../../common/reference/NativeEventData.md#getNativeData) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [getNativeValue](../../common/reference/NativeEventData.md#getNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [nativeEventName](../../common/reference/NativeEventData.md#nativeEventName) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [setNativeValue](../../common/reference/NativeEventData.md#setNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |

## deadEntity {#deadEntity}

```python
deadEntity: Optional[Entity]
```

数据来源为原生字段 `dieEntityId`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
死亡实体的entityId；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[Entity](../apis/entity.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## attacker {#attacker}

```python
attacker: Optional[Entity]
```

数据来源为原生字段 `attacker`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
伤害来源的entityId；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[Entity](../apis/entity.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## itemList {#itemList}

```python
itemList: Optional[list]
```

数据来源为原生字段 `itemList`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
掉落物品列表，每个元素为一个itemDict，格式可参考物品信息字典；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[list](../../common/type-system.md#list)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## itemEntities {#itemEntities}

```python
itemEntities: Optional[tuple[Entity, ...]]
```

数据来源为原生字段 `itemEntityIdList`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
掉落物品entityId列表；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[tuple](../../common/type-system.md#tuple)[[Entity](../apis/entity.md), ...]]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
from ModSAPI.server.beta import world

def on_event(event):
    print(event)

world.afterEvents.entityLoot.subscribe(on_event)

def cleanup():
    world.afterEvents.entityLoot.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)