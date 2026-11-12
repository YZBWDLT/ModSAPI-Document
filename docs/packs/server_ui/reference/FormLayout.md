---
title: "FormLayout"
sidebar_label: "FormLayout"
---

# FormLayout

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/FormData.py`；声明补充了静态类型信息。

表单样式设置。

需要先在MoreUI样式中定义网格，以此排布ui位置、大小等。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [position](#position) | 可读写属性 |
| [offset](#offset) | 可读写属性 |
| [size](#size) | 可读写属性 |
| [margin](#margin) | 可读写属性 |

## 构造器 {#constructor}

```python
FormLayout(layout = {})
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `layout` | 由值/所属选项确定 | `{}` | 布局字典；字段与长度约束见 [FormLayout](FormLayout.md) 或 [MoreUILayout](MoreUILayout.md)。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## position {#position}

```python
position: list[int | Observable[int]]
```

表单所处的位置(x, y)。

以屏幕左上角为坐标原点(0, 0)。

如，定义MoreUI布局后为2行2列，此属性设置为[0, 1]，即会将表单设置在第一列第二行的位置。

**访问：** 可读写。

写入方式：`instance.position = value`。参数类型线索：`(value: list[int \| Observable[int]])`。

写入参数 `value`：[list](../../common/type-system.md#list)[[int](../../common/type-system.md#int) \| [Observable](Observable.md)[[int](../../common/type-system.md#int)]]。

**返回类型：** [list](../../common/type-system.md#list)[[int](../../common/type-system.md#int) \| [Observable](Observable.md)[[int](../../common/type-system.md#int)]]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'Set position failed! Position must be a tuple or a list.'` |
| [Exception](../../common/type-system.md#exception) | `'Set position failed! Position must has at least 2 elements.'` |
| [Exception](../../common/type-system.md#exception) | `'Set position failed! Elements must be int.'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.position

def write_value(instance, value):
    instance.position = value
```

## offset {#offset}

```python
offset: list[float | Observable[float]]
```

表单的偏移量(x, y)，单位: 像素。

**访问：** 可读写。

写入方式：`instance.offset = value`。参数类型线索：`(value: list[float \| Observable[float]])`。

写入参数 `value`：[list](../../common/type-system.md#list)[[float](../../common/type-system.md#float) \| [Observable](Observable.md)[[float](../../common/type-system.md#float)]]。

**返回类型：** [list](../../common/type-system.md#list)[[float](../../common/type-system.md#float) \| [Observable](Observable.md)[[float](../../common/type-system.md#float)]]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'Set offset failed! Offset must be a tuple or a list.'` |
| [Exception](../../common/type-system.md#exception) | `'Set offset failed! Offset must has at least 2 elements.'` |
| [Exception](../../common/type-system.md#exception) | `'Set offset failed! Elements must be float.'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.offset

def write_value(instance, value):
    instance.offset = value
```

## size {#size}

```python
size: list[int | Observable[int]]
```

表单大小(x, y)。

**访问：** 可读写。

写入方式：`instance.size = value`。参数类型线索：`(value: list[int \| Observable[int]])`。

写入参数 `value`：[list](../../common/type-system.md#list)[[int](../../common/type-system.md#int) \| [Observable](Observable.md)[[int](../../common/type-system.md#int)]]。

**返回类型：** [list](../../common/type-system.md#list)[[int](../../common/type-system.md#int) \| [Observable](Observable.md)[[int](../../common/type-system.md#int)]]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'Set size failed! Size must be a tuple or a list.'` |
| [Exception](../../common/type-system.md#exception) | `'Set size failed! Size must has at least 2 elements.'` |
| [Exception](../../common/type-system.md#exception) | `'Set size failed! Elements must be int.'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.size

def write_value(instance, value):
    instance.size = value
```

## margin {#margin}

```python
margin: list[float | Observable[float]]
```

表单内边距（上，右，下，左），单位: 像素

**访问：** 可读写。

写入方式：`instance.margin = value`。参数类型线索：`(value: list[float \| Observable[float]])`。

写入参数 `value`：[list](../../common/type-system.md#list)[[float](../../common/type-system.md#float) \| [Observable](Observable.md)[[float](../../common/type-system.md#float)]]。

**返回类型：** [list](../../common/type-system.md#list)[[float](../../common/type-system.md#float) \| [Observable](Observable.md)[[float](../../common/type-system.md#float)]]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `'Set margin failed! Margin must be a tuple or a list.'` |
| [Exception](../../common/type-system.md#exception) | `'Set margin failed! Margin must has at least 2 elements.'` |
| [Exception](../../common/type-system.md#exception) | `'Set margin failed! Elements must be float.'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.margin

def write_value(instance, value):
    instance.margin = value
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 FormLayout 对象。
    print(value.position)
    print(value.offset)
    print(value.size)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)