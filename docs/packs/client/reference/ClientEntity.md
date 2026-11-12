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
| [isOnGround](#isOnGround) | 只读属性 |
| [isInLava](#isInLava) | 只读属性 |
| [bodyRotation](#bodyRotation) | 只读属性 |
| [collisionBoxSize](#collisionBoxSize) | 只读属性 |
| [airSupplyTicks](#airSupplyTicks) | 只读属性 |
| [maxAirSupplyTicks](#maxAirSupplyTicks) | 只读属性 |
| [getRotation](#getRotation) | 方法 |
| [getViewDirection](#getViewDirection) | 方法 |
| [getVelocity](#getVelocity) | 方法 |
| [getTarget](#getTarget) | 方法 |
| [getOwner](#getOwner) | 方法 |
| [getComponent](#getComponent) | 方法 |
| [hasComponent](#hasComponent) | 方法 |
| [getComponents](#getComponents) | 方法 |
| [teleport](#teleport) | 方法 |
| [setRotation](#setRotation) | 方法 |
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

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'HasEntity'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `HasEntity`。

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

独立的原生脚底坐标 [Vector3](../../server/extra/vector.md)；睡眠姿态保留原生坐标例外。

:::note 当前实现说明
保留 GetFootPos 的原生坐标约定；睡眠姿态例外同样适用。
:::

**访问：** 只读。

**返回类型：** [Vector3](../../server/extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetFootPos`。

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

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetEngineTypeStr'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetEngineTypeStr`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## isOnGround {#isOnGround}

```python
isOnGround: bool
```

已加载的客户端实体是否着地，骑乘也包含在内。新建本地实体在下一次引擎更新前可能返回原生默认值 True；不能用它作为服务端权威判定。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `isEntityOnGround`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isOnGround
```

## isInLava {#isInLava}

```python
isInLava: bool
```

本机已加载实体是否在岩浆中。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `isEntityInLava`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isInLava
```

## bodyRotation {#bodyRotation}

```python
bodyRotation: float
```

身体偏航角，单位为度；没有身体的实体由原生接口返回零。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBodyRot`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.bodyRotation
```

## collisionBoxSize {#collisionBoxSize}

```python
collisionBoxSize: Vector2
```

独立的 [Vector2](../../common/reference/Vector2.md)，x 为碰撞箱宽度，y 为高度。

**访问：** 只读。

**返回类型：** [Vector2](../../common/reference/Vector2.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetSize`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.collisionBoxSize
```

## airSupplyTicks {#airSupplyTicks}

```python
airSupplyTicks: int
```

已同步的空气储备，以每秒二十个逻辑刻计量；非生物实体保留原生默认值。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetCurrentAirSupply`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.airSupplyTicks
```

## maxAirSupplyTicks {#maxAirSupplyTicks}

```python
maxAirSupplyTicks: int
```

已同步的最大空气储备，以每秒二十个逻辑刻计量。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetMaxAirSupply`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.maxAirSupplyTicks
```

## getRotation {#getRotation}

```python
getRotation() -> Vector2
```

独立的 [Vector2](../../common/reference/Vector2.md)，x 为头部俯仰角，y 为偏航角，单位为度。

**返回类型：** [Vector2](../../common/reference/Vector2.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetRot`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getRotation(instance):
    return instance.getRotation()
```

## getViewDirection {#getViewDirection}

```python
getViewDirection() -> Vector3
```

将当前原生头部旋转换算为独立的世界方向向量。

**返回类型：** [Vector3](../../server/extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetDirFromRot`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getViewDirection(instance):
    return instance.getViewDirection()
```

## getVelocity {#getVelocity}

```python
getVelocity() -> Vector3
```

读取客户端上一帧的原生运动向量，返回独立的 [Vector3](../../server/extra/vector.md)。客户端不包含服务端摩擦计算，结果可能与服务端速度不同。原生失败或向量数据畸形时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)。

**返回类型：** [Vector3](../../server/extra/vector.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetMotion`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getVelocity(instance):
    return instance.getVelocity()
```

## getTarget {#getTarget}

```python
getTarget() -> ClientEntity | None
```

返回已加载的攻击目标对象；没有目标或目标不可见时返回 [None](../../common/type-system.md#none)。

**返回类型：** [ClientEntity](ClientEntity.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAttackTarget`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getTarget(instance):
    return instance.getTarget()
```

## getOwner {#getOwner}

```python
getOwner() -> ClientEntity | None
```

返回已加载的驯服主人对象；不存在或不可见时返回 [None](../../common/type-system.md#none)。

**返回类型：** [ClientEntity](ClientEntity.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetOwnerId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getOwner(instance):
    return instance.getOwner()
```

## getComponent {#getComponent}

```python
getComponent(componentId: str) -> ClientEntityAttributeComponent | ClientEntityInventoryComponent | ClientEntityEquippableComponent | None
```

取得已支持的只读组件；受支持属性不存在时返回 [None](../../common/type-system.md#none)。生命和陆地、水中、岩浆移动速度读取已同步属性；背包和装备组件当前仅支持本地玩家。其他标识符及不能访问的远端背包抛出 [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md)，不会伪装成原生行为组件不存在。

:::note 当前实现说明
已支持四种同步属性；本地玩家另支持 inventory 和 equippable。其他实体的背包与装备当前不由这两个客户端组件提供，会抛出 [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md)，不能把不支持的范围当作不存在。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `componentId` | [str](../../common/type-system.md#str) | `必填` | 传给 [ClientEntity.getComponent](ClientEntity.md#getComponent) 的 componentId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ClientEntityAttributeComponent](ClientEntityAttributeComponent.md) \| [ClientEntityInventoryComponent](ClientEntityInventoryComponent.md) \| [ClientEntityEquippableComponent](ClientEntityEquippableComponent.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md) | `'Unsupported client component: ' + identifier` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getComponent(instance, componentId):
    return instance.getComponent(componentId)
```

## hasComponent {#hasComponent}

```python
hasComponent(componentId: str) -> bool
```

检查已支持的可读组件；不能访问的范围会明确报告错误。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `componentId` | [str](../../common/type-system.md#str) | `必填` | 传给 [ClientEntity.hasComponent](ClientEntity.md#hasComponent) 的 componentId 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hasComponent(instance, componentId):
    return instance.hasComponent(componentId)
```

## getComponents {#getComponents}

```python
getComponents() -> list[ClientEntityAttributeComponent | ClientEntityInventoryComponent | ClientEntityEquippableComponent]
```

列出已支持属性及本地背包、装备组件。属性使用一个原生代理；背包和装备句柄延迟创建，不在此处读取物品数据。这是已开放的可读组件目录，不是行为包 JSON 中每个组件的完整清单。

:::note 当前实现说明
本地玩家的目录包括已支持属性、背包和装备句柄；创建后两种句柄时不读取物品。并非行为包 JSON 的完整组件清单。
:::

**返回类型：** [list](../../common/type-system.md#list)[[ClientEntityAttributeComponent](ClientEntityAttributeComponent.md) \| [ClientEntityInventoryComponent](ClientEntityInventoryComponent.md) \| [ClientEntityEquippableComponent](ClientEntityEquippableComponent.md)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLocalPlayerId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getComponents(instance):
    return instance.getComponents()
```

## teleport {#teleport}

```python
teleport(location: Vector3 | dict[str, float] | tuple[float, float, float]) -> None
```

移动 [client.spawnEntity](../apis/manager.md#spawnEntity) 创建的本地实体，不移动服务端实体。保留原生位置约定；本地玩家传送和跨维度移动应使用服务端操作。

:::note 当前实现说明
仅修改 [client.spawnEntity](../apis/manager.md#spawnEntity) 返回的本地实体；其他句柄抛出 [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md)。原生位置约定保持不变，不提供服务端或跨维度传送。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `location` | [Vector3](../../server/extra/vector.md) \| [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [float](../../common/type-system.md#float)] \| [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetPosForClientEntity`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_teleport(instance, location):
    return instance.teleport(location)
```

## setRotation {#setRotation}

```python
setRotation(rotation: Vector2 | dict[str, float] | tuple[float, float]) -> None
```

复制二维旋转并设置本地创建实体的俯仰角、偏航角，单位为度。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `rotation` | [Vector2](../../common/reference/Vector2.md) \| [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [float](../../common/type-system.md#float)] \| [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] | `必填` | 旋转角度，具体分量与单位参见成员说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetRotForClientEntity`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setRotation(instance, rotation):
    return instance.setRotation(rotation)
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