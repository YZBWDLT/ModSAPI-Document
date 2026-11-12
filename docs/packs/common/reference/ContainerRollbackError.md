---
title: "ContainerRollbackError"
sidebar_label: "ContainerRollbackError"
---

# ContainerRollbackError

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/errors/container.py`；声明补充了静态类型信息。

修改失败，且至少一个槽位无法恢复。cause 保留最初故障，failures 为只读诊断记录；恢复会继续尝试所有受影响槽位。此错误不表示原生背包具备事务能力，也不保证内容未变。

## 获取方式

捕获容器修改抛出的恢复错误；cause 为最初故障，failures 为尚未确认恢复的槽位记录。

基类：[ExtensionError](ExtensionError.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [operation](#operation) | 只读属性 |
| [cause](#cause) | 只读属性 |
| [failures](#failures) | 只读属性 |

## operation {#operation}

```python
operation: str
```

恢复未完成的公共容器操作名称。

**访问：** 只读。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.operation
```

## cause {#cause}

```python
cause: Exception
```

最初的修改故障，与各槽位恢复错误分别保留。

**访问：** 只读。

**返回类型：** [Exception](../type-system.md#exception)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.cause
```

## failures {#failures}

```python
failures: tuple[ContainerRollbackFailure, ...]
```

尚未确认恢复的 [ContainerRollbackFailure](ContainerRollbackFailure.md) 记录元组副本。

**访问：** 只读。

**返回类型：** [tuple](../type-system.md#tuple)[[ContainerRollbackFailure](ContainerRollbackFailure.md), ...]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.failures
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ContainerRollbackError 对象。
    print(value.operation)
    print(value.cause)
    print(value.failures)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)