---
title: "UiViewport"
sidebar_label: "UiViewport"
---

# UiViewport

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/display.py`；声明补充了静态类型信息。

原生视角的独立只读快照；不执行坐标换算。

## 获取方式

读取 [client.ui.viewport](UiService.md#viewport) 取得独立视角快照；无需自行构造。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [size](#size) | 只读属性 |
| [offset](#offset) | 只读属性 |

## size {#size}

```python
size: Vector2
```

返回独立的二维向量，包含原生视角宽度和高度。

**访问：** 只读。

**返回类型：** [Vector2](../../common/reference/Vector2.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.size
```

## offset {#offset}

```python
offset: Vector2
```

返回独立的二维向量，包含原生视角的横向和纵向偏移。

**访问：** 只读。

**返回类型：** [Vector2](../../common/reference/Vector2.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.offset
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UiViewport 对象。
    print(value.size)
    print(value.offset)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)