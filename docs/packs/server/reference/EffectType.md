---
title: "EffectType"
sidebar_label: "EffectType"
---

# EffectType

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/Effect.py`；声明补充了静态类型信息。

可添加到实体的效果类型，例如中毒。

## 获取方式

效果类型的内部标识符对象，使用 id 读取标准标识符。通常直接把效果标识符字符串传给实体效果操作；模板入口未直接导出该构造器。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [id](#id) | 只读属性 |
| [getName](#getName) | 方法 |

## 构造器 {#constructor}

```python
EffectType(name: str) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../../common/type-system.md#str) | `必填` | 传给 [EffectType.__init__](EffectType.md#constructor) 的 name 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## id {#id}

```python
id: str
```

此值对象保存的效果标识符。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## getName {#getName}

```python
getName() -> str
```

效果类型的标识名称。

:::note 当前实现说明
保留原有获取方式以兼容已有调用；新代码优先读取标准 id 属性。
:::

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
    # value 是上方获取方式取得的 EffectType 对象。
    print(value.id)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)