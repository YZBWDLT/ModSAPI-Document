---
title: "ScoreboardObjective"
sidebar_label: "ScoreboardObjective"
---

# ScoreboardObjective

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Scoreboard.py`；声明补充了静态类型信息。

计分项的信息。

## 获取方式

通过 world.scoreboard.getObjective(id) 或 addObjective(id, displayName) 获取。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [id](#id) | 只读属性 |
| [displayName](#displayName) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [addScore](#addScore) | 方法 |
| [getScore](#getScore) | 方法 |
| [getScores](#getScores) | 方法 |
| [getParticipants](#getParticipants) | 方法 |

## 构造器 {#constructor}

```python
ScoreboardObjective(Id: str, name: str) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `Id` | [str](../../common/type-system.md#str) | `必填` | 传给 [ScoreboardObjective.__init__](ScoreboardObjective.md#constructor) 的 Id 参数；结合上方功能说明和下方调用示例使用。 |
| `name` | [str](../../common/type-system.md#str) | `必填` | 传给 [ScoreboardObjective.__init__](ScoreboardObjective.md#constructor) 的 name 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

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

## isValid {#isValid}

```python
isValid: bool
```

读取 `isValid` 的当前值。底层调用 `GetAllScoreboardObjects`, `GetLevelId`。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAllScoreboardObjects`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## addScore {#addScore}

```python
addScore(participate: Entity | str, scoreToAdd: int) -> int
```

为指定参与者在此计分项中的分数增加给定值。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `participate` | [Entity](../apis/entity.md) \| [str](../../common/type-system.md#str) | `必填` | 传给 [ScoreboardObjective.addScore](ScoreboardObjective.md#addScore) 的 participate 参数；结合上方功能说明和下方调用示例使用。 |
| `scoreToAdd` | [int](../../common/type-system.md#int) | `必填` | 传给 [ScoreboardObjective.addScore](ScoreboardObjective.md#addScore) 的 scoreToAdd 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to add scoreboard score'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetCommand`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addScore(instance, participate, scoreToAdd):
    return instance.addScore(participate, scoreToAdd)
```

## getScore {#getScore}

```python
getScore(participate: Entity | str | ScoreboardIdentity) -> int | None
```

读取指定参与者的分数。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `participate` | [Entity](../apis/entity.md) \| [str](../../common/type-system.md#str) \| [ScoreboardIdentity](ScoreboardIdentity.md) | `必填` | 传给 [ScoreboardObjective.getScore](ScoreboardObjective.md#getScore) 的 participate 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [int](../../common/type-system.md#int) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAllPlayerScoreboardObjects`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getScore(instance, participate):
    return instance.getScore(participate)
```

## getScores {#getScores}

```python
getScores() -> list[ScoreboardScoreInfo]
```

返回此计分项中全部参与者的分数。

**返回类型：** [list](../../common/type-system.md#list)[[ScoreboardScoreInfo](ScoreboardScoreInfo.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAllPlayerScoreboardObjects`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getScores(instance):
    return instance.getScores()
```

## getParticipants {#getParticipants}

```python
getParticipants() -> list[ScoreboardIdentity]
```

读取 `getParticipants` 操作。参数形态和结果约定如下。

**返回类型：** [list](../../common/type-system.md#list)[[ScoreboardIdentity](ScoreboardIdentity.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getParticipants(instance):
    return instance.getParticipants()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ScoreboardObjective 对象。
    print(value.id)
    print(value.displayName)
    print(value.isValid)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)