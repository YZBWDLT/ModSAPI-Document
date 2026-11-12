---
title: "MoreUILayout"
sidebar_label: "MoreUILayout"
---

# MoreUILayout

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/FormData.py`；声明补充了静态类型信息。

布局配置。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [row](#row) | 可读写属性 |
| [column](#column) | 可读写属性 |

## 构造器 {#constructor}

```python
MoreUILayout(layout = {})
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `layout` | 由值/所属选项确定 | `{}` | 布局字典；字段与长度约束见 [FormLayout](FormLayout.md) 或 [MoreUILayout](MoreUILayout.md)。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## row {#row}

```python
row: list[int | float] | tuple[int | float]
```

定义要划分的行数。

接受一个数字型列表。

列表大小即为行数，列表元素值为这一行的宽度比例。

如，设置为[1, 2, 1]，意为3行，行宽度比例为1: 2: 1

**访问：** 可读写。

写入方式：`instance.row = value`。参数类型线索：`(value: list[int \| float] \| tuple[int \| float])`。

写入参数 `value`：[list](../../common/type-system.md#list)[[int](../../common/type-system.md#int) \| [float](../../common/type-system.md#float)] \| [tuple](../../common/type-system.md#tuple)[[int](../../common/type-system.md#int) \| [float](../../common/type-system.md#float)]。

**返回类型：** [list](../../common/type-system.md#list)[[int](../../common/type-system.md#int) \| [float](../../common/type-system.md#float)] \| [tuple](../../common/type-system.md#tuple)[[int](../../common/type-system.md#int) \| [float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'Property row excepted list[int \| float], but got %s' % type(value).__name__` |
| [TypeError](../../common/type-system.md#typeerror) | `'Property row excepted list[int \| float], but got list[%s]' % type(el).__name__` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.row

def write_value(instance, value):
    instance.row = value
```

## column {#column}

```python
column: list[int | float] | tuple[int | float]
```

定义要划分的列数。

接受一个数字型列表。

列表大小即为列数，列表元素值为这一列的宽度比例。

如，设置为[1, 2, 1]，意为3列，列宽度比例为1: 2: 1

**访问：** 可读写。

写入方式：`instance.column = value`。参数类型线索：`(value: list[int \| float] \| tuple[int \| float])`。

写入参数 `value`：[list](../../common/type-system.md#list)[[int](../../common/type-system.md#int) \| [float](../../common/type-system.md#float)] \| [tuple](../../common/type-system.md#tuple)[[int](../../common/type-system.md#int) \| [float](../../common/type-system.md#float)]。

**返回类型：** [list](../../common/type-system.md#list)[[int](../../common/type-system.md#int) \| [float](../../common/type-system.md#float)] \| [tuple](../../common/type-system.md#tuple)[[int](../../common/type-system.md#int) \| [float](../../common/type-system.md#float)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'Property column excepted list[int \| float], but got %s' % type(value).__name__` |
| [TypeError](../../common/type-system.md#typeerror) | `'Property column excepted list[int \| float], but got list[%s]' % type(el).__name__` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.column

def write_value(instance, value):
    instance.column = value
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 MoreUILayout 对象。
    print(value.row)
    print(value.column)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)