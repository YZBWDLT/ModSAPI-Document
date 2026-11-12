---
title: "ProtectedEntityRegistry"
sidebar_label: "ProtectedEntityRegistry"
---

# ProtectedEntityRegistry

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/registries/protectedEntity.py`；声明补充了静态类型信息。

受保护实体的注册表；此类实体不能被命令杀死。实际支持情况见当前实现限制。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [register](#register) | 方法 |

## 构造器 {#constructor}

```python
ProtectedEntityRegistry()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## register {#register}

```python
register(typeId: str, condition: Callable[[Entity], bool] = lambda entity: True) -> None
```

注册受保护的实体类型。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `typeId` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的实体、物品或资源类型名称。 |
| `condition` | [Callable](../../common/type-system.md#callable)[[[Entity](../apis/entity.md)], [bool](../../common/type-system.md#bool)] | `lambda entity: True` | 传给 [ProtectedEntityRegistry.register](ProtectedEntityRegistry.md#register) 的 condition 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetSystem`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_register(instance, typeId):
    return instance.register(typeId)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 ProtectedEntityRegistry 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)