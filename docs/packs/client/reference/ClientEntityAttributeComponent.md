---
title: "ClientEntityAttributeComponent"
sidebar_label: "ClientEntityAttributeComponent"
---

# ClientEntityAttributeComponent

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Attributes.py`；声明补充了静态类型信息。

通过 entity.getComponent() 取得的实时只读客户端属性。仅提供已同步的当前值和最大值；默认值、最小值及权威修改需使用服务端接口。原生客户端未同步权威的攻击伤害、击退抗性和跳跃强度，因此不提供这些属性。

## 获取方式

通过 [ClientEntity](ClientEntity.md) 或 [ClientPlayer](ClientPlayer.md) 的 getComponent(...) 取得，只读并保留所属客户端实体。使用前处理 [None](../../common/type-system.md#none)，后续按需检查 isValid。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [typeId](#typeId) | 只读属性 |
| [entity](#entity) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [currentValue](#currentValue) | 只读属性 |
| [effectiveMax](#effectiveMax) | 只读属性 |

## typeId {#typeId}

```python
typeId: str
```

带命名空间的组件标识符，失效后仍可读取。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## entity {#entity}

```python
entity: ClientEntity
```

拥有此组件的客户端实体包装对象。

**访问：** 只读。

**返回类型：** [ClientEntity](ClientEntity.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.entity
```

## isValid {#isValid}

```python
isValid: bool
```

实体是否可见且已同步属性仍然存在。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAttrValue`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## currentValue {#currentValue}

```python
currentValue: float
```

每次重新读取已同步的当前值；属性消失后报告对象失效。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.currentValue
```

## effectiveMax {#effectiveMax}

```python
effectiveMax: float
```

读取原生已同步的最大值，不伪造默认值。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetAttrMaxValue'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.effectiveMax
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientEntityAttributeComponent 对象。
    print(value.typeId)
    print(value.entity)
    print(value.isValid)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)