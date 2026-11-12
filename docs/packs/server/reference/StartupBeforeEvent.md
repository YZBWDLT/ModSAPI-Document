---
title: "StartupBeforeEvent"
sidebar_label: "StartupBeforeEvent"
---

# StartupBeforeEvent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/events/core/WorldEvents.py`；声明补充了静态类型信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [customCommandRegistry](#customCommandRegistry) | 只读属性 |

## 构造器 {#constructor}

```python
StartupBeforeEvent()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## customCommandRegistry {#customCommandRegistry}

```python
customCommandRegistry: CustomCommandRegistry
```

读取 `customCommandRegistry` 的当前值。

**访问：** 只读。

**返回类型：** [CustomCommandRegistry](CustomCommandRegistry.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.customCommandRegistry
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 StartupBeforeEvent 对象。
    print(value.customCommandRegistry)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)