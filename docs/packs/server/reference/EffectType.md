---
title: "EffectType"
sidebar_label: "EffectType"
---

# EffectType

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Effect.py`。

可添加到实体的效果类型，例如中毒。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [getName](#getName) | 方法 |

## 构造器 {#constructor}

```python
EffectType(name)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | 由值/所属选项确定 | `必填` | 传给 [EffectType.__init__](EffectType.md#constructor) 的 name 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## getName {#getName}

```python
getName() -> str
```

效果类型的标识名称。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getName(instance):
    return instance.getName()
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 EffectType 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)