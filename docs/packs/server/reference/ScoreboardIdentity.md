---
title: "ScoreboardIdentity"
sidebar_label: "ScoreboardIdentity"
---

# ScoreboardIdentity

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Scoreboard.py`；声明补充了静态类型信息。

计分板参与者的身份信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [displayName](#displayName) | 只读属性 |
| [id](#id) | 只读属性 |
| [type](#type) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [getEntity](#getEntity) | 方法 |

## 构造器 {#constructor}

```python
ScoreboardIdentity(scoreboard: ScoreboardObjective, entityId: str, name: str = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `scoreboard` | [ScoreboardObjective](ScoreboardObjective.md) | `必填` | 传给 [ScoreboardIdentity.__init__](ScoreboardIdentity.md#constructor) 的 scoreboard 参数；结合上方功能说明和下方调用示例使用。 |
| `entityId` | [str](../../common/type-system.md#str) | `必填` | 实体运行 ID；跨回调使用前重新确认实体有效性。 |
| `name` | [str](../../common/type-system.md#str) | [None](../../common/type-system.md#none) | 传给 [ScoreboardIdentity.__init__](ScoreboardIdentity.md#constructor) 的 name 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEngineTypeStr`。

## displayName {#displayName}

```python
displayName: str
```

读取 `displayName` 的当前值。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.displayName
```

## id {#id}

```python
id: str
```

读取 `id` 的当前值。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## type {#type}

```python
type: str
```

读取 [type](../../common/type-system.md#type) 的当前值。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.type
```

## isValid {#isValid}

```python
isValid: bool
```

读取 `isValid` 的当前值。底层调用 `GetAllPlayerScoreboardObjects`, `GetLevelId`。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAllPlayerScoreboardObjects`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## getEntity {#getEntity}

```python
getEntity() -> Entity | None
```

读取 `getEntity` 操作。参数形态和结果约定如下。

**返回类型：** [Entity](../apis/entity.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getEntity(instance):
    return instance.getEntity()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ScoreboardIdentity 对象。
    print(value.displayName)
    print(value.id)
    print(value.type)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)