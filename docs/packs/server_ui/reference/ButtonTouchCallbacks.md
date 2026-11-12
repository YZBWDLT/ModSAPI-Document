---
title: "ButtonTouchCallbacks"
sidebar_label: "ButtonTouchCallbacks"
---

# ButtonTouchCallbacks

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/ControlData.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [hoverIn](#hoverIn) | 可读写属性 |
| [hoverOut](#hoverOut) | 可读写属性 |
| [screenExit](#screenExit) | 可读写属性 |
| [touchCancel](#touchCancel) | 可读写属性 |
| [touchDown](#touchDown) | 可读写属性 |
| [touchUp](#touchUp) | 可读写属性 |
| [touchMove](#touchMove) | 可读写属性 |
| [touchMoveIn](#touchMoveIn) | 可读写属性 |
| [touchMoveOut](#touchMoveOut) | 可读写属性 |

## 构造器 {#constructor}

```python
ButtonTouchCallbacks() -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## hoverIn {#hoverIn}

```python
hoverIn
```

鼠标挪入按钮区域时触发函数

**访问：** 可读写。

写入方式：`instance.hoverIn = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.hoverIn

def write_value(instance, value):
    instance.hoverIn = value
```

## hoverOut {#hoverOut}

```python
hoverOut
```

鼠标挪出按钮区域时触发函数

**访问：** 可读写。

写入方式：`instance.hoverOut = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.hoverOut

def write_value(instance, value):
    instance.hoverOut = value
```

## screenExit {#screenExit}

```python
screenExit
```

按钮所在画布退出时触发函数

**访问：** 可读写。

写入方式：`instance.screenExit = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.screenExit

def write_value(instance, value):
    instance.screenExit = value
```

## touchCancel {#touchCancel}

```python
touchCancel
```

按下按钮后在按钮区域外抬起时触发函数

**访问：** 可读写。

写入方式：`instance.touchCancel = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.touchCancel

def write_value(instance, value):
    instance.touchCancel = value
```

## touchDown {#touchDown}

```python
touchDown
```

按下按钮（未抬起）时触发函数

**访问：** 可读写。

写入方式：`instance.touchDown = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.touchDown

def write_value(instance, value):
    instance.touchDown = value
```

## touchUp {#touchUp}

```python
touchUp
```

按下按钮并抬起时触发

**访问：** 可读写。

写入方式：`instance.touchUp = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.touchUp

def write_value(instance, value):
    instance.touchUp = value
```

## touchMove {#touchMove}

```python
touchMove
```

手指在按钮区域内挪动时触发

**访问：** 可读写。

写入方式：`instance.touchMove = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.touchMove

def write_value(instance, value):
    instance.touchMove = value
```

## touchMoveIn {#touchMoveIn}

```python
touchMoveIn
```

手指挪入按钮区域时触发函数

**访问：** 可读写。

写入方式：`instance.touchMoveIn = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.touchMoveIn

def write_value(instance, value):
    instance.touchMoveIn = value
```

## touchMoveOut {#touchMoveOut}

```python
touchMoveOut
```

手指挪出按钮区域时触发函数

**访问：** 可读写。

写入方式：`instance.touchMoveOut = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.touchMoveOut

def write_value(instance, value):
    instance.touchMoveOut = value
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ButtonTouchCallbacks 对象。
    print(value.hoverIn)
    print(value.hoverOut)
    print(value.screenExit)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)