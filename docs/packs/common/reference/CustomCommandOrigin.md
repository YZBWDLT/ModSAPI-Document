---
title: "CustomCommandOrigin"
sidebar_label: "CustomCommandOrigin"
---

# CustomCommandOrigin

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/CustomCommand.py`；声明补充了静态类型信息。

这是值对象或结果包装对象，成员通过属性访问；是否接受字典输入由所属操作的签名决定。包装类型不一定是模板入口的直接导出符号。

命令触发来源的详细信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [initiator](#initiator) | 只读属性 |
| [sourceBlock](#sourceBlock) | 只读属性 |
| [sourceEntity](#sourceEntity) | 只读属性 |
| [sourceType](#sourceType) | 只读属性 |

## 构造器 {#constructor}

```python
CustomCommandOrigin(data)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## initiator {#initiator}

```python
initiator: Entity
```

命令通过非玩家角色触发时，返回发起该角色对话的实体。

**访问：** 只读。

**返回类型：** [Entity](../../server/apis/entity.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.initiator
```

## sourceBlock {#sourceBlock}

```python
sourceBlock: Block
```

命令由方块触发时的来源方块，例如命令方块。

**访问：** 只读。

**返回类型：** [Block](../../server/apis/block.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.sourceBlock
```

## sourceEntity {#sourceEntity}

```python
sourceEntity: Entity
```

命令由实体触发时的来源实体，例如非玩家角色。

**访问：** 只读。

**返回类型：** [Entity](../../server/apis/entity.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.sourceEntity
```

## sourceType {#sourceType}

```python
sourceType: CustomCommandSource
```

触发命令的来源类型。

**访问：** 只读。

**返回类型：** [CustomCommandSource](CustomCommandSource.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.sourceType
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 CustomCommandOrigin 对象。
    print(value.initiator)
    print(value.sourceBlock)
    print(value.sourceEntity)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)