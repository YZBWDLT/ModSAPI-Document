---
title: "InvalidEntityError"
sidebar_label: "InvalidEntityError"
---

# InvalidEntityError

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/errors/extensions.py`；声明补充了静态类型信息。

服务端实体已经失效；保留的身份信息仍可读取。

## 获取方式

在服务端操作失效实体时捕获。id 和 [type](../type-system.md#type) 为已捕获的诊断身份；尚未捕获类型时 [type](../type-system.md#type) 为空字符串。无需主动构造。

基类：[ExtensionError](ExtensionError.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [id](#id) | 只读属性 |
| [type](#type) | 只读属性 |

## id {#id}

```python
id: str
```

保留失效实体标识符，读取时不再查询引擎。

**访问：** 只读。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## type {#type}

```python
type: str
```

最后捕获的实体类型；尚未取得类型时为空字符串。

**访问：** 只读。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.type
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 InvalidEntityError 对象。
    print(value.id)
    print(value.type)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)