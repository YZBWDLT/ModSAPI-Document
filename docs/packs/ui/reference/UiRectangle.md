---
title: "UiRectangle"
sidebar_label: "UiRectangle"
---

# UiRectangle

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/display.py`；声明补充了静态类型信息。

原生区域的独立矩形，使用基类画布坐标，四条边界均为只读。

## 获取方式

调用 [client.ui.getNativeArea](UiService.md#getNativeArea) 取得独立矩形；无需自行构造。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [left](#left) | 只读属性 |
| [top](#top) | 只读属性 |
| [right](#right) | 只读属性 |
| [bottom](#bottom) | 只读属性 |
| [position](#position) | 只读属性 |
| [size](#size) | 只读属性 |

## left {#left}

```python
left: float
```

原生横向最小坐标。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.left
```

## top {#top}

```python
top: float
```

原生纵向最小坐标。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.top
```

## right {#right}

```python
right: float
```

原生横向最大坐标。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.right
```

## bottom {#bottom}

```python
bottom: float
```

原生纵向最大坐标。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.bottom
```

## position {#position}

```python
position: Vector2
```

返回独立的二维向量，包含左边界和上边界。

**访问：** 只读。

**返回类型：** [Vector2](../../common/reference/Vector2.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.position
```

## size {#size}

```python
size: Vector2
```

返回独立的二维向量，包含宽度和高度；保留零值。

**访问：** 只读。

**返回类型：** [Vector2](../../common/reference/Vector2.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.size
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UiRectangle 对象。
    print(value.left)
    print(value.top)
    print(value.right)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)