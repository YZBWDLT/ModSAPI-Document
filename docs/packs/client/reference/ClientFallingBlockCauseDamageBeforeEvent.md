---
title: "ClientFallingBlockCauseDamageBeforeEvent"
sidebar_label: "ClientFallingBlockCauseDamageBeforeEvent"
---

# ClientFallingBlockCauseDamageBeforeEvent

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/NativeEventTypes.py`；声明补充了静态类型信息。

此类型由运行时事件契约创建，并通过对应端的 `beta` 导出。通过 `subscribe` 回调取得实例；不要自行构造事件参数。

[FallingBlockCauseDamageBeforeClientEvent](../events.md#fallingblockcausedamagebeforeclientevent) 的事件参数；同步分发结束后不能再写入输出字段。

## 获取方式

通过下方所属信号的回调参数取得；类型可从对应端 beta 导入，用于识别事件类型。

所属信号：[client.beforeEvents.fallingBlockCauseDamage](ClientBeforeEvents.md#fallingBlockCauseDamage).

基类：[NativeEventData](../../common/reference/NativeEventData.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [fallingBlock](#fallingBlock) | 只读属性 |
| [fallingBlockX](#fallingBlockX) | 只读属性 |
| [fallingBlockY](#fallingBlockY) | 只读属性 |
| [fallingBlockZ](#fallingBlockZ) | 只读属性 |
| [blockName](#blockName) | 只读属性 |
| [dimension](#dimension) | 只读属性 |
| [collidingEntities](#collidingEntities) | 只读属性 |
| [fallTickAmount](#fallTickAmount) | 只读属性 |
| [fallDistance](#fallDistance) | 只读属性 |
| [isHarmful](#isHarmful) | 只读属性 |
| [fallDamage](#fallDamage) | 只读属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [getNativeData](../../common/reference/NativeEventData.md#getNativeData) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [getNativeValue](../../common/reference/NativeEventData.md#getNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [nativeEventName](../../common/reference/NativeEventData.md#nativeEventName) | [NativeEventData](../../common/reference/NativeEventData.md) |
| [setNativeValue](../../common/reference/NativeEventData.md#setNativeValue) | [NativeEventData](../../common/reference/NativeEventData.md) |

## fallingBlock {#fallingBlock}

```python
fallingBlock: Optional[ClientEntity]
```

数据来源为原生字段 `fallingBlockId`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
下落的方块实体id；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[ClientEntity](ClientEntity.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fallingBlockX {#fallingBlockX}

```python
fallingBlockX: Optional[float]
```

数据来源为原生字段 `fallingBlockX`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
下落的方块实体位置x；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fallingBlockY {#fallingBlockY}

```python
fallingBlockY: Optional[float]
```

数据来源为原生字段 `fallingBlockY`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
下落的方块实体位置y；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fallingBlockZ {#fallingBlockZ}

```python
fallingBlockZ: Optional[float]
```

数据来源为原生字段 `fallingBlockZ`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
下落的方块实体位置z；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## blockName {#blockName}

```python
blockName: Optional[str]
```

数据来源为原生字段 `blockName`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
重力方块的identifier，包含命名空间及名称；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## dimension {#dimension}

```python
dimension: Optional[ClientDimension]
```

数据来源为原生字段 `dimensionId`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
下落的方块实体维度id；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[ClientDimension](ClientDimension.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## collidingEntities {#collidingEntities}

```python
collidingEntities: Optional[tuple[ClientEntity, ...]]
```

数据来源为原生字段 `collidingEntitys`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
当前碰撞到的实体列表id（客户端只能获取到玩家），如果没有的话是[None](../../common/type-system.md#none)；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[tuple](../../common/type-system.md#tuple)[[ClientEntity](ClientEntity.md), ...]]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fallTickAmount {#fallTickAmount}

```python
fallTickAmount: Optional[int]
```

数据来源为原生字段 `fallTickAmount`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
下落的方块实体持续下落了多少tick；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fallDistance {#fallDistance}

```python
fallDistance: Optional[float]
```

数据来源为原生字段 `fallDistance`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
下落的方块实体持续下落了多少距离；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## isHarmful {#isHarmful}

```python
isHarmful: Optional[bool]
```

数据来源为原生字段 `isHarmful`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
客户端始终为false，因为客户端不会计算伤害值；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[bool](../../common/type-system.md#bool)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## fallDamage {#fallDamage}

```python
fallDamage: Optional[int]
```

数据来源为原生字段 `fallDamage`；只读。字段缺失时返回 [None](../../common/type-system.md#none)。公开类型及对象包装以本成员的返回类型为准。

:::note 当前实现说明
对实体的伤害；只读。
:::

**访问：** 只读。

**返回类型：** [Optional](../../common/type-system.md#optional)[[int](../../common/type-system.md#int)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
from ModSAPI.client.beta import client

def on_event(event):
    print(event)

client.beforeEvents.fallingBlockCauseDamage.subscribe(on_event)

def cleanup():
    client.beforeEvents.fallingBlockCauseDamage.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)