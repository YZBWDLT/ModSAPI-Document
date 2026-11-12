---
title: "ObservableUIRawMessage"
sidebar_label: "ObservableUIRawMessage"
---

# ObservableUIRawMessage

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/observables.py`；声明补充了静态类型信息。

## 获取方式

通过 `from ModSAPI.serverui.beta import ObservableUIRawMessage` 导入；当前仅支持字面 RawMessage 结构。

基类：[Observable](Observable.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [setData](#setData) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [ID](Observable.md#field-ID) | [Observable](Observable.md) |
| [create](Observable.md#create) | [Observable](Observable.md) |
| [dispose](Observable.md#dispose) | [Observable](Observable.md) |
| [getData](Observable.md#getData) | [Observable](Observable.md) |
| [subscribe](Observable.md#subscribe) | [Observable](Observable.md) |
| [typeId](Observable.md#typeId) | [Observable](Observable.md) |
| [unsubscribe](Observable.md#unsubscribe) | [Observable](Observable.md) |

## 构造器 {#constructor}

```python
ObservableUIRawMessage(data: dict, options: ObservableOptions | None = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | [dict](../../common/type-system.md#dict) | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |
| `options` | [ObservableOptions](ObservableOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## setData {#setData}

```python
setData(data, bit = False)
```

设置 `setData` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |
| `bit` | 由值/所属选项确定 | `False` | 传给 [ObservableUIRawMessage.setData](ObservableUIRawMessage.md#setData) 的 bit 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setData(instance, data):
    return instance.setData(data)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 ObservableUIRawMessage 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)