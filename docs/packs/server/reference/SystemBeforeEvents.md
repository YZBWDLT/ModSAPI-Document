---
title: "SystemBeforeEvents"
sidebar_label: "SystemBeforeEvents"
---

# SystemBeforeEvents

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/SystemEvents.py`；声明补充了静态类型信息。

实际操作发生前的事件集合，部分事件允许取消或修改待执行操作。可写字段和执行限制以各事件的原生契约为准；不能直接套用微软受限执行阶段的规则。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [startup](#startup) | 只读属性 |

## 构造器 {#constructor}

```python
SystemBeforeEvents()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## startup {#startup}

```python
startup: StartupBeforeEventSignal
```

读取 `startup` 的当前值。

**访问：** 只读。

**返回类型：** [StartupBeforeEventSignal](StartupBeforeEventSignal.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.startup
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 SystemBeforeEvents 对象。
    print(value.startup)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)