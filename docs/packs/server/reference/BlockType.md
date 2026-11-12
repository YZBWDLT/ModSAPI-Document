---
title: "BlockType"
sidebar_label: "BlockType"
---

# BlockType

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Block.py`；声明补充了静态类型信息。

方块的类型或模板；除类型标识外，不包含具体状态组合数据。

## 获取方式

通常从 [block.type](../../common/type-system.md#type) 或 [block.permutation.type](../../common/type-system.md#type) 读取。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [id](#id) | 只读属性 |
| [aux](#aux) | 只读属性 |

## 构造器 {#constructor}

```python
BlockType(id: str, aux: int = 0) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `id` | [str](../../common/type-system.md#str) | `必填` | 运行标识或类型标识，按本成员的说明传入。 |
| `aux` | [int](../../common/type-system.md#int) | `0` | 传给 [BlockType.__init__](BlockType.md#constructor) 的 aux 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## id {#id}

```python
id: str
```

方块类型名称。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## aux {#aux}

```python
aux: int
```

读取 `aux` 的当前值。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.aux
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 BlockType 对象。
    print(value.id)
    print(value.aux)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)