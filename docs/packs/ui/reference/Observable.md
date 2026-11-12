---
title: "Observable"
sidebar_label: "Observable"
---

# Observable

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/core/general/observable.py`；声明补充了静态类型信息。

具有独立数据副本、顺序更新队列和可释放派生值的状态对象。运算符生成派生状态；布尔转换读取当前值，取得普通结果时使用 value 或 getValue。

## 获取方式

从 ModSAPI.ui 导入，或使用 [client.ui.createState](UiService.md#createState) / [system.ui.createState](UiService.md#createState)。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `''` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [create](#create) | 静态/类方法 |
| [getData](#getData) | 方法 |
| [setData](#setData) | 方法 |
| [getValue](#getValue) | 方法 |
| [value](#value) | 可读写属性 |
| [dispose](#dispose) | 方法 |
| [setValue](#setValue) | 方法 |
| [update](#update) | 方法 |
| [subscribe](#subscribe) | 方法 |
| [watch](#watch) | 方法 |
| [map](#map) | 方法 |
| [unsubscribe](#unsubscribe) | 方法 |

## 构造器 {#constructor}

```python
Observable(value: _T, manager = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `value` | [_T](../../common/type-system.md#typevar) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |
| `manager` | 由值/所属选项确定 | [None](../../common/type-system.md#none) | 传给 [Observable.__init__](Observable.md#constructor) 的 manager 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## create {#create}

```python
create(value: _T) -> Observable[_T]
```

创建并登记到当前界面运行时的可观察状态。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `value` | [_T](../../common/type-system.md#typevar) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [Observable](Observable.md)[[_T](../../common/type-system.md#typevar)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_create(type_object, value):
    return type_object.create(value)
```

## getData {#getData}

```python
getData() -> _T
```

读取 `getData` 操作。参数形态和结果约定如下。

**返回类型：** [_T](../../common/type-system.md#typevar)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getData(instance):
    return instance.getData()
```

## setData {#setData}

```python
setData(v: _T) -> None
```

设置 `setData` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `v` | [_T](../../common/type-system.md#typevar) | `必填` | 传给 [Observable.setData](Observable.md#setData) 的 v 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setData(instance, v):
    return instance.setData(v)
```

## getValue {#getValue}

```python
getValue() -> _T
```

读取 `getValue` 操作。参数形态和结果约定如下。

**返回类型：** [_T](../../common/type-system.md#typevar)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'The UI state has been disposed'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getValue(instance):
    return instance.getValue()
```

## value {#value}

```python
value: _T
```

当前值的独立副本；需要发布修改时重新赋值或调用 update。

**访问：** 可读写。

写入方式：`instance.value = value`。参数类型线索：`(value: _T) -> None`。

写入参数 `value`：[_T](../../common/type-system.md#typevar)。

**返回类型：** [_T](../../common/type-system.md#typevar)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.value

def write_value(instance, value):
    instance.value = value
```

## dispose {#dispose}

```python
dispose() -> None
```

释放当前状态的派生绑定和订阅，不销毁其他状态。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_dispose(instance):
    return instance.dispose()
```

## setValue {#setValue}

```python
setValue(v: _T) -> None
```

设置 `setValue` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `v` | [_T](../../common/type-system.md#typevar) | `必填` | 传给 [Observable.setValue](Observable.md#setValue) 的 v 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setValue(instance, v):
    return instance.setValue(v)
```

## update {#update}

```python
update(updater: Callable[[_T], _T]) -> None
```

根据当前值副本计算新值，并保持回调内再次修改时的队列顺序。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `updater` | [Callable](../../common/type-system.md#callable)[[[_T](../../common/type-system.md#typevar)], [_T](../../common/type-system.md#typevar)] | `必填` | 传给 [Observable.update](Observable.md#update) 的 updater 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'updater must be callable'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_update(instance, updater):
    return instance.update(updater)
```

## subscribe {#subscribe}

```python
subscribe(callback: Callable[[_T], None]) -> Callable[[], None]
```

监听后续变化并返回取消函数。回调接收新值副本时，getValue 仍返回旧值；处理完其他订阅者和已经排队的修改后，再报告首个异常。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../../common/type-system.md#callable)[[[_T](../../common/type-system.md#typevar)], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [Callable](../../common/type-system.md#callable)[[], [None](../../common/type-system.md#none)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'The UI state has been disposed'` |
| [TypeError](../../common/type-system.md#typeerror) | `'subscriber must be callable'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_subscribe(instance, callback):
    return instance.subscribe(callback)
```

## watch {#watch}

```python
watch(callback: Callable[[_T], None], immediate: bool = True) -> Callable[[], None]
```

监听状态变化，默认立即接收一次当前值。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../../common/type-system.md#callable)[[[_T](../../common/type-system.md#typevar)], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |
| `immediate` | [bool](../../common/type-system.md#bool) | `True` | 传给 [Observable.watch](Observable.md#watch) 的 immediate 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Callable](../../common/type-system.md#callable)[[], [None](../../common/type-system.md#none)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'watch callback must be callable'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_watch(instance, callback):
    return instance.watch(callback)
```

## map {#map}

```python
map(transform: Callable[[_T], _U]) -> Observable[_U]
```

使用无副作用的转换创建派生状态，派生绑定可独立释放。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `transform` | [Callable](../../common/type-system.md#callable)[[[_T](../../common/type-system.md#typevar)], [_U](../../common/type-system.md#typevar)] | `必填` | 传给 [Observable.map](Observable.md#map) 的 transform 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [Observable](Observable.md)[[_U](../../common/type-system.md#typevar)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'transform must be callable'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_map(instance, transform):
    return instance.map(transform)
```

## unsubscribe {#unsubscribe}

```python
unsubscribe(callback: Callable[[_T], None]) -> None
```

移除一个匹配的订阅，重复移除没有副作用。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../../common/type-system.md#callable)[[[_T](../../common/type-system.md#typevar)], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_unsubscribe(instance, callback):
    return instance.unsubscribe(callback)
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