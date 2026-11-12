---
title: "Observable"
sidebar_label: "Observable"
---

# Observable

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/FormData.py`；声明补充了静态类型信息。

可被观察的数据，主要用于界面更新。

## 获取方式

从 ModSAPI.ui 导入，或使用 [client.ui.createState](../../ui/reference/UiService.md#createState) / [system.ui.createState](../../ui/reference/UiService.md#createState)。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `ID` | 由运行时值确定 | `0` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [typeId](#typeId) | 只读属性 |
| [getData](#getData) | 方法 |
| [setData](#setData) | 方法 |
| [subscribe](#subscribe) | 方法 |
| [unsubscribe](#unsubscribe) | 方法 |
| [dispose](#dispose) | 方法 |
| [create](#create) | 静态/类方法 |

## 构造器 {#constructor}

```python
Observable(data, options)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |
| `options` | 由值/所属选项确定 | `必填` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'Create observable failed! Options should be a dict, but got %s' % type(options).__name__` |
| [TypeError](../../common/type-system.md#typeerror) | `'Create observable failed! Expected type int \| float \| str \| bool, but got %s' % type(data).__name__` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## typeId {#typeId}

```python
typeId: type[T]
```

读取 `typeId` 的当前值。

**访问：** 只读。

**返回类型：** [type](../../common/type-system.md#type)[[T](../../common/type-system.md#typevar)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## getData {#getData}

```python
getData() -> T
```

读取 `getData` 操作。参数形态和结果约定如下。

**返回类型：** [T](../../common/type-system.md#typevar)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getData(instance):
    return instance.getData()
```

## setData {#setData}

```python
setData(data: T, bit = False) -> None
```

设置 `setData` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | [T](../../common/type-system.md#typevar) | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |
| `bit` | 由值/所属选项确定 | `False` | 传给 [Observable.setData](Observable.md#setData) 的 bit 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'Observable expected data of type %s, but got %s' % (type(self.__data).__name__, type(data).__name__)` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setData(instance, data):
    return instance.setData(data)
```

## subscribe {#subscribe}

```python
subscribe(callback: Callable[[T], None]) -> Callable[[T], None]
```

执行 `subscribe` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../../common/type-system.md#callable)[[[T](../../common/type-system.md#typevar)], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [Callable](../../common/type-system.md#callable)[[[T](../../common/type-system.md#typevar)], [None](../../common/type-system.md#none)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_subscribe(instance, callback):
    return instance.subscribe(callback)
```

## unsubscribe {#unsubscribe}

```python
unsubscribe(callback: Callable[[T], None]) -> bool
```

执行 `unsubscribe` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../../common/type-system.md#callable)[[[T](../../common/type-system.md#typevar)], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_unsubscribe(instance, callback):
    return instance.unsubscribe(callback)
```

## dispose {#dispose}

```python
dispose()
```

移除或清理 `dispose` 操作。参数形态和结果约定如下。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_dispose(instance):
    return instance.dispose()
```

## create {#create}

```python
create(data: str, options: ObservableOptions = {'clientWritable': False}) -> Observable[str]
```

创建或登记 `create` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | [str](../../common/type-system.md#str) | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |
| `options` | [ObservableOptions](ObservableOptions.md) | `{'clientWritable': False}` | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [Observable](Observable.md)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_create(type_object, data):
    return type_object.create(data)
```

## 使用示例


```python
from __future__ import print_function

from ModSAPI.client.beta import client

state = client.ui.createState(0)
stop = state.watch(lambda value: print(value))
state.update(lambda value: value + 1)
stop()
state.dispose()
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)