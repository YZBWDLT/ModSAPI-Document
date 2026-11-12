---
title: "UiChoiceEvent"
sidebar_label: "UiChoiceEvent"
---

# UiChoiceEvent

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/choices.py`；声明补充了静态类型信息。

选择事件的独立快照，不公开原生事件字典中的其他字段。

## 获取方式

从下拉框的 selectionChange 或轮盘的选择回调取得。

基类：[UiEvent](UiEvent.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [index](#index) | 只读属性 |
| [label](#label) | 只读属性 |
| [value](#value) | 只读属性 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [control](UiEvent.md#control) | [UiEvent](UiEvent.md) |
| [player](UiEvent.md#player) | [UiEvent](UiEvent.md) |
| [position](UiEvent.md#position) | [UiEvent](UiEvent.md) |
| [reason](UiEvent.md#reason) | [UiEvent](UiEvent.md) |
| [view](UiEvent.md#view) | [UiEvent](UiEvent.md) |

## index {#index}

```python
index: int | None
```

事件记录的零起始索引；没有选中时为 [None](../../common/type-system.md#none)。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.index
```

## label {#label}

```python
label: str | None
```

下拉框事件记录的选项文字；轮盘不提供文字。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.label
```

## value {#value}

```python
value: Any
```

选项自定义值的独立副本；轮盘事件返回 [None](../../common/type-system.md#none)。

**访问：** 只读。

**返回类型：** [Any](../../common/type-system.md#any)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.value
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UiChoiceEvent 对象。
    print(value.index)
    print(value.label)
    print(value.value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)