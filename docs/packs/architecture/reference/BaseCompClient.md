---
title: "BaseCompClient"
sidebar_label: "BaseCompClient"
---

# BaseCompClient

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/component/index.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [onCreate](#onCreate) | 方法 |
| [loadData](#loadData) | 方法 |

## onCreate {#onCreate}

```python
onCreate(entityId)
```

当前没有功能性实现，不应依赖此成员完成操作。

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` | 实体运行 ID；跨回调使用前重新确认实体有效性。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## loadData {#loadData}

```python
loadData(entityId)
```

当前没有功能性实现，不应依赖此成员完成操作。

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` | 实体运行 ID；跨回调使用前重新确认实体有效性。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 BaseCompClient 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)