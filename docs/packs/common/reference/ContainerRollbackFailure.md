---
title: "ContainerRollbackFailure"
sidebar_label: "ContainerRollbackFailure"
---

# ContainerRollbackFailure

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/errors/container.py`；声明补充了静态类型信息。

一个在恢复后仍无法确认内容还原的槽位记录。

## 获取方式

从 [ContainerRollbackError.failures](ContainerRollbackError.md#failures) 读取；记录包含容器对象、槽位下标和恢复故障，无需主动构造。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [container](#container) | 只读属性 |
| [slotIndex](#slotIndex) | 只读属性 |
| [cause](#cause) | 只读属性 |

## container {#container}

```python
container: Container
```

该恢复故障关联的服务端容器包装对象。

**访问：** 只读。

**返回类型：** [Container](../../server/apis/container.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.container
```

## slotIndex {#slotIndex}

```python
slotIndex: int
```

受影响槽位从零开始的下标，无需再次查询可能已经失效的槽位。

**访问：** 只读。

**返回类型：** [int](../type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.slotIndex
```

## cause {#cause}

```python
cause: Exception
```

导致无法确认恢复的原生写入或读回故障。

**访问：** 只读。

**返回类型：** [Exception](../type-system.md#exception)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.cause
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ContainerRollbackFailure 对象。
    print(value.container)
    print(value.slotIndex)
    print(value.cause)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)