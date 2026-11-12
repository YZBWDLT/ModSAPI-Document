---
title: "BackgroundData"
sidebar_label: "BackgroundData"
---

# BackgroundData

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/ControlData.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [texture](#texture) | 可读写属性 |
| [color](#color) | 可读写属性 |
| [alpha](#alpha) | 可读写属性 |

## 构造器 {#constructor}

```python
BackgroundData()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## texture {#texture}

```python
texture
```

背景图片，默认为'textures/ui/white_bg'

**访问：** 可读写。

写入方式：`instance.texture = value`。参数类型线索：`(value: str) -> None`。

写入参数 `value`：[str](../../common/type-system.md#str)。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.texture

def write_value(instance, value):
    instance.texture = value
```

## color {#color}

```python
color
```

颜色，使用rgb格式，默认为(255, 255, 255)

支持表达式

**访问：** 可读写。

写入方式：`instance.color = value`。参数类型线索：`(value: tuple[int \| Expression] \| list[int \| Expression]) -> None`。

写入参数 `value`：[tuple](../../common/type-system.md#tuple)[[int](../../common/type-system.md#int) \| [Expression](../../common/reference/Expression.md)] \| [list](../../common/type-system.md#list)[[int](../../common/type-system.md#int) \| [Expression](../../common/reference/Expression.md)]。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.color

def write_value(instance, value):
    instance.color = value
```

## alpha {#alpha}

```python
alpha
```

透明度，默认为0.0

支持表达式

**访问：** 可读写。

写入方式：`instance.alpha = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.alpha

def write_value(instance, value):
    instance.alpha = value
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 BackgroundData 对象。
    print(value.texture)
    print(value.color)
    print(value.alpha)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)