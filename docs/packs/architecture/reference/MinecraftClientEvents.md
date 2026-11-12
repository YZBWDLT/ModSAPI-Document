---
title: "MinecraftClientEvents"
sidebar_label: "MinecraftClientEvents"
---

# MinecraftClientEvents

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/event/client.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `globalEvents` | 由运行时值确定 | `{}` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [getOrCreateChain](#getOrCreateChain) | 静态/类方法 |

## getOrCreateChain {#getOrCreateChain}

```python
getOrCreateChain(eventType: str, isCustomEvent: bool = False) -> EventChain
```

读取 `getOrCreateChain` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `eventType` | [str](../../common/type-system.md#str) | `必填` | 传给 [MinecraftClientEvents.getOrCreateChain](MinecraftClientEvents.md#getOrCreateChain) 的 eventType 参数；结合上方功能说明和下方调用示例使用。 |
| `isCustomEvent` | [bool](../../common/type-system.md#bool) | `False` | 传给 [MinecraftClientEvents.getOrCreateChain](MinecraftClientEvents.md#getOrCreateChain) 的 isCustomEvent 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [EventChain](EventChain.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Client subsystem manager is not initialized'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getOrCreateChain(type_object, eventType):
    return type_object.getOrCreateChain(eventType)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 MinecraftClientEvents 对象。
    print(value.globalEvents)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)