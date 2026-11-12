---
title: "ClientDimension"
sidebar_label: "ClientDimension"
---

# ClientDimension

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Dimension.py`；声明补充了静态类型信息。

客户端观察到的维度，身份信息在会话结束后仍可读取。此对象描述被观察的维度，不一定是当前可见维度；不会赋予访问未加载区块或服务端的能力。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [id](#id) | 只读属性 |
| [isValid](#isValid) | 只读属性 |

## 构造器 {#constructor}

```python
ClientDimension(dimensionId: int, owner = None) -> None
```

校验原生维度编号，不调用任一端的开发包。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `dimensionId` | [int](../../common/type-system.md#int) | `必填` | 传给 [ClientDimension.__init__](ClientDimension.md#constructor) 的 dimensionId 参数；结合上方功能说明和下方调用示例使用。 |
| `owner` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [ClientDimension.__init__](ClientDimension.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'dimensionId must be an integer'` |
| [ValueError](../../common/type-system.md#valueerror) | `'dimensionId must be nonnegative'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## id {#id}

```python
id: str
```

原版维度使用带命名空间的标识，自定义维度使用 dmN。

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

所属客户端会话是否仍活跃；不表示区块是否存在。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientDimension 对象。
    print(value.id)
    print(value.isValid)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)