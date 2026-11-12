---
title: "ClientEntity"
sidebar_label: "ClientEntity"
---

# ClientEntity

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Entity.py`；声明补充了静态类型信息。

客户端可见实体的包装对象；仅允许移除由本地创建的实体。

## 获取方式

使用 `client.getEntity(id)` 或 `client.spawnEntity(...)`。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [id](#id) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [nameTag](#nameTag) | 只读属性 |
| [location](#location) | 只读属性 |
| [typeId](#typeId) | 只读属性 |
| [getMolangValue](#getMolangValue) | 方法 |
| [setMolangValue](#setMolangValue) | 方法 |
| [getQueryVariable](#getQueryVariable) | 方法 |
| [setQueryVariable](#setQueryVariable) | 方法 |
| [remove](#remove) | 方法 |

## 构造器 {#constructor}

```python
ClientEntity(entityId: str, owner: Any = None, removable: bool = False) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `entityId` | [str](../../common/type-system.md#str) | `必填` | 实体运行 ID；跨回调使用前重新确认实体有效性。 |
| `owner` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 传给 [ClientEntity.__init__](ClientEntity.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |
| `removable` | [bool](../../common/type-system.md#bool) | `False` | 传给 [ClientEntity.__init__](ClientEntity.md#constructor) 的 removable 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## id {#id}

```python
id: str
```

实体运行标识；对象失效后仍可读取。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## isValid {#isValid}

```python
isValid: bool
```

客户端会话与原生可见实体是否均仍有效。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `CreateGame`, `GetEngineCompFactory`, `GetLevelId`, `HasEntity`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## nameTag {#nameTag}

```python
nameTag: str
```

从引擎实时读取的名称，不使用导入时的缓存。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetName`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.nameTag
```

## location {#location}

```python
location: Vector3
```

脚部位置，返回独立的 [Vector3](../../server/extra/vector.md) 副本。

**访问：** 只读。

**返回类型：** [Vector3](../../server/extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.location
```

## typeId {#typeId}

```python
typeId: str
```

带命名空间的原生实体类型。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEngineTypeStr`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## getMolangValue {#getMolangValue}

```python
getMolangValue(molangExpression: str) -> Any
```

求值原生 MoLang 表达式并返回结果。原生结果结构不合法时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)。表达式遵循原生 MoLang 语义，不是 Python 表达式。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `molangExpression` | [str](../../common/type-system.md#str) | `必填` | 传给 [ClientEntity.getMolangValue](ClientEntity.md#getMolangValue) 的 molangExpression 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Any](../../common/type-system.md#any)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'EvalMolangExpression'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `EvalMolangExpression`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getMolangValue(instance, molangExpression):
    return instance.getMolangValue(molangExpression)
```

## setMolangValue {#setMolangValue}

```python
setMolangValue(molang: str, value: float) -> None
```

向 variable.* 或 v.* 写入有限标量，不通过拼接代码赋值。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `molang` | [str](../../common/type-system.md#str) | `必填` | 传给 [ClientEntity.setMolangValue](ClientEntity.md#setMolangValue) 的 molang 参数；结合上方功能说明和下方调用示例使用。 |
| `value` | [float](../../common/type-system.md#float) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Expected a writable MoLang variable name'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setMolangValue(instance, molang, value):
    return instance.setMolangValue(molang, value)
```

## getQueryVariable {#getQueryVariable}

```python
getQueryVariable(name: str) -> float
```

读取已注册的 query.mod.* 节点；注册项由客户端管理。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../../common/type-system.md#str) | `必填` | 传给 [ClientEntity.getQueryVariable](ClientEntity.md#getQueryVariable) 的 name 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `Get`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getQueryVariable(instance, name):
    return instance.getQueryVariable(name)
```

## setQueryVariable {#setQueryVariable}

```python
setQueryVariable(name: str, value: float) -> None
```

为此实体设置已注册的 query.mod.* 节点。原生节点使用单精度浮点数，大整数可能损失精度。须先通过 [client.registerQueryVariable](../apis/manager.md#registerQueryVariable) 注册名称。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../../common/type-system.md#str) | `必填` | 传给 [ClientEntity.setQueryVariable](ClientEntity.md#setQueryVariable) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `value` | [float](../../common/type-system.md#float) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** [Set](../../common/type-system.md#set)。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setQueryVariable(instance, name, value):
    return instance.setQueryVariable(name, value)
```

## remove {#remove}

```python
remove() -> None
```

销毁通过 [client.spawnEntity](../apis/manager.md#spawnEntity) 创建的实体；其他实体对象会拒绝此操作。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md) | `'Only locally spawned entity handles can be removed'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `DestroyClientEntity`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_remove(instance):
    return instance.remove()
```

## 使用示例


```python
from ModSAPI.client.beta import client

entity = client.getEntity(client.localPlayer.id)
if entity is not None and entity.isValid:
    print(entity.typeId, entity.location.getTuple())
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)