---
title: "Effect"
sidebar_label: "Effect"
---

# Effect

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Effect.py`；声明补充了静态类型信息。

已添加到实体的状态效果，例如中毒。

## 获取方式

从 entity.getEffect、entity.getEffects 或效果事件取得；没有指定效果时，getEffect 返回 [None](../../common/type-system.md#none)。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [amplifier](#amplifier) | 只读属性 |
| [displayName](#displayName) | 只读属性 |
| [duration](#duration) | 只读属性 |
| [typeId](#typeId) | 只读属性 |

## 构造器 {#constructor}

```python
Effect(typeId: str, duration: int, amplifier: int = 0) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `typeId` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的实体、物品或资源类型名称。 |
| `duration` | [int](../../common/type-system.md#int) | `必填` | 传给 [Effect.__init__](Effect.md#constructor) 的 duration 参数；结合上方功能说明和下方调用示例使用。 |
| `amplifier` | [int](../../common/type-system.md#int) | `0` | 传给 [Effect.__init__](Effect.md#constructor) 的 amplifier 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## amplifier {#amplifier}

```python
amplifier: int
```

效果的强度级别，常见值为 0–4。例如跳跃提升二级对应 amplifier 为 1。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.amplifier
```

## displayName {#displayName}

```python
displayName: str
```

用于向玩家显示的效果名称。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.displayName
```

## duration {#duration}

```python
duration: int
```

效果的总持续时间，单位为刻，每秒 20 刻。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.duration
```

## typeId {#typeId}

```python
typeId: str
```

效果的类型标识。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 Effect 对象。
    print(value.amplifier)
    print(value.displayName)
    print(value.duration)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)