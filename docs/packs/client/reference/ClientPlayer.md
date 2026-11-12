---
title: "ClientPlayer"
sidebar_label: "ClientPlayer"
---

# ClientPlayer

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Player.py`；声明补充了静态类型信息。

本地玩家的可读状态及本地显示控制。

## 获取方式

使用 [client.localPlayer](../apis/manager.md#localPlayer)。

基类：[ClientEntity](ClientEntity.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [name](#name) | 只读属性 |
| [dimension](#dimension) | 只读属性 |
| [sendToast](#sendToast) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [getMolangValue](ClientEntity.md#getMolangValue) | [ClientEntity](ClientEntity.md) |
| [getQueryVariable](ClientEntity.md#getQueryVariable) | [ClientEntity](ClientEntity.md) |
| [id](ClientEntity.md#id) | [ClientEntity](ClientEntity.md) |
| [isValid](ClientEntity.md#isValid) | [ClientEntity](ClientEntity.md) |
| [location](ClientEntity.md#location) | [ClientEntity](ClientEntity.md) |
| [nameTag](ClientEntity.md#nameTag) | [ClientEntity](ClientEntity.md) |
| [remove](ClientEntity.md#remove) | [ClientEntity](ClientEntity.md) |
| [setMolangValue](ClientEntity.md#setMolangValue) | [ClientEntity](ClientEntity.md) |
| [setQueryVariable](ClientEntity.md#setQueryVariable) | [ClientEntity](ClientEntity.md) |
| [typeId](ClientEntity.md#typeId) | [ClientEntity](ClientEntity.md) |

## 构造器 {#constructor}

```python
ClientPlayer(owner: Any = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `owner` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 传给 [ClientPlayer.__init__](ClientPlayer.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLocalPlayerId`。

## name {#name}

```python
name: str
```

当前玩家名称，每次读取均从引擎刷新。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.name
```

## dimension {#dimension}

```python
dimension: ClientDimension
```

本地玩家当前显示的维度包装对象。

**访问：** 只读。

**返回类型：** [ClientDimension](ClientDimension.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetCurrentDimension'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `CreateGame`, `GetCurrentDimension`, `GetEngineCompFactory`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.dimension
```

## sendToast {#sendToast}

```python
sendToast(message: str, title: str = '') -> None
```

显示本地提示，参数顺序与服务端扩展一致。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `message` | [str](../../common/type-system.md#str) | `必填` | 传给 [ClientPlayer.sendToast](ClientPlayer.md#sendToast) 的 message 参数；结合上方功能说明和下方调用示例使用。 |
| `title` | [str](../../common/type-system.md#str) | `''` | 标题文本，动态表单也可接受相应 [Observable](../../ui/reference/Observable.md)。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'title must be text without NUL'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `CreateGame`, `SetPopupNotice`, `GetEngineCompFactory`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_sendToast(instance, message):
    return instance.sendToast(message)
```

## 使用示例


```python
from ModSAPI.client.beta import client

player = client.localPlayer
print(player.id, player.location.getTuple())
player.sendToast("Ready", "Example")
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)