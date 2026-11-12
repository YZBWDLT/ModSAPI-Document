---
title: "Scoreboard"
sidebar_label: "Scoreboard"
---

# Scoreboard

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Scoreboard.py`；声明补充了静态类型信息。

计分板及其计分项、参与者。

## 获取方式

从 [world.scoreboard](../apis/world.md#scoreboard) 获取。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [addObjective](#addObjective) | 静态/类方法 |
| [getObjective](#getObjective) | 静态/类方法 |
| [clearObjectiveAtDisplaySlot](#clearObjectiveAtDisplaySlot) | 方法 |
| [getObjectives](#getObjectives) | 静态/类方法 |

## addObjective {#addObjective}

```python
addObjective(objectiveId: str, displayName: str = '') -> ScoreboardObjective
```

向计分板添加新的计分项。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `objectiveId` | [str](../../common/type-system.md#str) | `必填` | 传给 [Scoreboard.addObjective](Scoreboard.md#addObjective) 的 objectiveId 参数；结合上方功能说明和下方调用示例使用。 |
| `displayName` | [str](../../common/type-system.md#str) | `''` | 传给 [Scoreboard.addObjective](Scoreboard.md#addObjective) 的 displayName 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ScoreboardObjective](ScoreboardObjective.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Unable to add scoreboard objective'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetCommand`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addObjective(type_object, objectiveId):
    return type_object.addObjective(objectiveId)
```

## getObjective {#getObjective}

```python
getObjective(objectiveId: str) -> ScoreboardObjective | None
```

按标识读取指定计分项。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `objectiveId` | [str](../../common/type-system.md#str) | `必填` | 传给 [Scoreboard.getObjective](Scoreboard.md#getObjective) 的 objectiveId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ScoreboardObjective](ScoreboardObjective.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAllScoreboardObjects`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getObjective(type_object, objectiveId):
    return type_object.getObjective(objectiveId)
```

## clearObjectiveAtDisplaySlot {#clearObjectiveAtDisplaySlot}

```python
clearObjectiveAtDisplaySlot(displaySlotId: str) -> None
```

清除显示槽位中的计分项。当前仅在清除侧栏时可能返回原计分项对象。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `displaySlotId` | [str](../../common/type-system.md#str) | `必填` | 传给 [Scoreboard.clearObjectiveAtDisplaySlot](Scoreboard.md#clearObjectiveAtDisplaySlot) 的 displaySlotId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetCommand`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clearObjectiveAtDisplaySlot(instance, displaySlotId):
    return instance.clearObjectiveAtDisplaySlot(displaySlotId)
```

## getObjectives {#getObjectives}

```python
getObjectives() -> list[ScoreboardObjective]
```

读取全部已定义的计分项。

**返回类型：** [list](../../common/type-system.md#list)[[ScoreboardObjective](ScoreboardObjective.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAllScoreboardObjects`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getObjectives(type_object):
    return type_object.getObjectives()
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 Scoreboard 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)