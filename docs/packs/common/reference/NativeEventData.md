---
title: "NativeEventData"
sidebar_label: "NativeEventData"
---

# NativeEventData

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/native_events.py`；声明补充了静态类型信息。

引擎事件快照，只允许文档明确规定的同步输出。可选字段或随开发包版本变化的字段缺失时返回 [None](../type-system.md#none)。读取容器值时返回副本，修改后须重新赋值才能提交输出。实体、玩家和维度字段返回对象引用；准确原生标识仅通过显式的 getNativeData 或 getNativeValue 读取。事件参数由适配器创建，请勿自行实例化。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [nativeEventName](#nativeEventName) | 只读属性 |
| [getNativeData](#getNativeData) | 方法 |
| [getNativeValue](#getNativeValue) | 方法 |
| [setNativeValue](#setNativeValue) | 方法 |

## 构造器 {#constructor}

```python
NativeEventData(data, owner = None)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |
| `owner` | 由值/所属选项确定 | [None](../type-system.md#none) | 传给 [NativeEventData.__init__](NativeEventData.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../type-system.md#typeerror) | `'Native event data must be a dictionary'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## nativeEventName {#nativeEventName}

```python
nativeEventName: str
```

区分大小写的准确 ModSDK 事件名称。

**访问：** 只读。

**返回类型：** [str](../type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.nativeEventName
```

## getNativeData {#getNativeData}

```python
getNativeData() -> dict[str, Any]
```

返回原生数据的容器副本，包括当前事件目录尚未识别的字段。

**返回类型：** [dict](../type-system.md#dict)[[str](../type-system.md#str), [Any](../type-system.md#any)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getNativeData(instance):
    return instance.getNativeData()
```

## getNativeValue {#getNativeValue}

```python
getNativeValue(name: str, defaultValue: Any = None) -> Any
```

按准确原生字段名读取值，也支持 from 等 Python 关键字。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../type-system.md#str) | `必填` | 传给 [NativeEventData.getNativeValue](NativeEventData.md#getNativeValue) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `defaultValue` | [Any](../type-system.md#any) | [None](../type-system.md#none) | 缺省值；具体是缺失键、初始控件值还是原生默认值取决于所属接口。 |

**返回类型：** [Any](../type-system.md#any)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getNativeValue(instance, name):
    return instance.getNativeValue(name)
```

## setNativeValue {#setNativeValue}

```python
setNativeValue(name: str, value: Any) -> None
```

同步写入文档规定的输出，拒绝未知或只读字段。只读字段抛出 [AttributeError](../type-system.md#attributeerror)，分发结束后写入抛出 [RuntimeError](../type-system.md#runtimeerror)，类型错误抛出 [TypeError](../type-system.md#typeerror)，非有限值或超出范围抛出 [ValueError](../type-system.md#valueerror)。同时校验 cancelable、canChange 等原生条件。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../type-system.md#str) | `必填` | 传给 [NativeEventData.setNativeValue](NativeEventData.md#setNativeValue) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `value` | [Any](../type-system.md#any) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [AttributeError](../type-system.md#attributeerror) | `'Native field is read-only: %s' % name` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Native event output is no longer writable'` |
| [RuntimeError](../type-system.md#runtimeerror) | `'This native action cannot be cancelled'` |
| [ValueError](../type-system.md#valueerror) | `'Chat prefix colors must be in [0, 1]'` |
| [ValueError](../type-system.md#valueerror) | `'pickupDelay must be nonnegative'` |
| [ValueError](../type-system.md#valueerror) | `'isValid must be 0 or 1'` |
| [RuntimeError](../type-system.md#runtimeerror) | `'This durability change cannot be overridden'` |
| [ValueError](../type-system.md#valueerror) | `'durability must be in [-32768, 32767)'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setNativeValue(instance, name, value):
    return instance.setNativeValue(name, value)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 NativeEventData 对象。
    print(value.nativeEventName)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)