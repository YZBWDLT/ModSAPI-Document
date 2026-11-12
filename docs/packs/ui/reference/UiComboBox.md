---
title: "UiComboBox"
sidebar_label: "UiComboBox"
---

# UiComboBox

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/choices.py`；声明补充了静态类型信息。

本地原生下拉框，与表单中的组合下拉控件分别使用。选项值为普通数据的独立副本；原生读取接口只提供文字和索引，不提供已有选项自定义值的读取方法。

## 获取方式

使用 view.getControl(path, "comboBox")；模板继承原生 combo_box.comboBoxPanel。

基类：[UiControl](UiControl.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [afterEvents](#afterEvents) | 只读属性 |
| [optionCount](#optionCount) | 只读属性 |
| [selectedIndex](#selectedIndex) | 可读写属性 |
| [selectedLabel](#selectedLabel) | 只读属性 |
| [addOption](#addOption) | 方法 |
| [getOptionLabel](#getOptionLabel) | 方法 |
| [findOption](#findOption) | 方法 |
| [selectLabel](#selectLabel) | 方法 |
| [removeOption](#removeOption) | 方法 |
| [clearOptions](#clearOptions) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [anchorFrom](UiControl.md#anchorFrom) | [UiControl](UiControl.md) |
| [anchorTo](UiControl.md#anchorTo) | [UiControl](UiControl.md) |
| [animate](UiControl.md#animate) | [UiControl](UiControl.md) |
| [bind](UiControl.md#bind) | [UiControl](UiControl.md) |
| [blur](UiControl.md#blur) | [UiControl](UiControl.md) |
| [clipOffset](UiControl.md#clipOffset) | [UiControl](UiControl.md) |
| [clipsChildren](UiControl.md#clipsChildren) | [UiControl](UiControl.md) |
| [focus](UiControl.md#focus) | [UiControl](UiControl.md) |
| [getChild](UiControl.md#getChild) | [UiControl](UiControl.md) |
| [getChildren](UiControl.md#getChildren) | [UiControl](UiControl.md) |
| [getProperties](UiControl.md#getProperties) | [UiControl](UiControl.md) |
| [globalPosition](UiControl.md#globalPosition) | [UiControl](UiControl.md) |
| [isValid](UiControl.md#isValid) | [UiControl](UiControl.md) |
| [maximumSize](UiControl.md#maximumSize) | [UiControl](UiControl.md) |
| [minimumSize](UiControl.md#minimumSize) | [UiControl](UiControl.md) |
| [native](UiControl.md#native) | [UiControl](UiControl.md) |
| [path](UiControl.md#path) | [UiControl](UiControl.md) |
| [position](UiControl.md#position) | [UiControl](UiControl.md) |
| [remove](UiControl.md#remove) | [UiControl](UiControl.md) |
| [setAnchors](UiControl.md#setAnchors) | [UiControl](UiControl.md) |
| [setEnabled](UiControl.md#setEnabled) | [UiControl](UiControl.md) |
| [setLayer](UiControl.md#setLayer) | [UiControl](UiControl.md) |
| [setLayout](UiControl.md#setLayout) | [UiControl](UiControl.md) |
| [setOpacity](UiControl.md#setOpacity) | [UiControl](UiControl.md) |
| [setProperties](UiControl.md#setProperties) | [UiControl](UiControl.md) |
| [setVisible](UiControl.md#setVisible) | [UiControl](UiControl.md) |
| [size](UiControl.md#size) | [UiControl](UiControl.md) |
| [view](UiControl.md#view) | [UiControl](UiControl.md) |
| [visible](UiControl.md#visible) | [UiControl](UiControl.md) |

## afterEvents {#afterEvents}

```python
afterEvents: UiComboBoxEvents
```

读取 `afterEvents` 的当前值。

**访问：** 只读。

**返回类型：** [UiComboBoxEvents](UiComboBoxEvents.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.afterEvents
```

## optionCount {#optionCount}

```python
optionCount: int
```

原生下拉框当前的选项数量。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.optionCount
```

## selectedIndex {#selectedIndex}

```python
selectedIndex: int | None
```

选中的零起始选项索引；没有选中时为 [None](../../common/type-system.md#none)，赋值 [None](../../common/type-system.md#none) 可清除选择。

**访问：** 可读写。

写入方式：`instance.selectedIndex = value`。参数类型线索：`(value: int \| None) -> None`。

写入参数 `value`：[int](../../common/type-system.md#int) \| [None](../../common/type-system.md#none)。

**返回类型：** [int](../../common/type-system.md#int) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.selectedIndex

def write_value(instance, value):
    instance.selectedIndex = value
```

## selectedLabel {#selectedLabel}

```python
selectedLabel: str | None
```

原生选中项的显示文字；没有选中时为 [None](../../common/type-system.md#none)。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.selectedLabel
```

## addOption {#addOption}

```python
addOption(label: str, value: Any = None, options: UiComboBoxOption | None = None) -> UiComboBox
```

追加选项，复制自定义值并可设置图标；返回当前下拉框，支持连续调用。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |
| `value` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 需要写入的值，类型、范围及副本语义见本成员说明。 |
| `options` | [UiComboBoxOption](UiComboBoxOption.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [UiComboBox](UiComboBox.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `AddOption`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addOption(instance, label):
    return instance.addOption(label)
```

## getOptionLabel {#getOptionLabel}

```python
getOptionLabel(index: int) -> str
```

按有效的零起始索引读取当前选项文字。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `index` | [int](../../common/type-system.md#int) | `必填` | 传给 [UiComboBox.getOptionLabel](UiComboBox.md#getOptionLabel) 的 index 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetOptionShowNameByIndex'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetOptionShowNameByIndex`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getOptionLabel(instance, index):
    return instance.getOptionLabel(index)
```

## findOption {#findOption}

```python
findOption(label: str) -> int | None
```

按显示文字查找选项，未找到时返回 [None](../../common/type-system.md#none)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |

**返回类型：** [int](../../common/type-system.md#int) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetOptionIndexByShowName'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetOptionIndexByShowName`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_findOption(instance, label):
    return instance.findOption(label)
```

## selectLabel {#selectLabel}

```python
selectLabel(label: str) -> None
```

按显示文字选中选项；文字不存在时抛出 [KeyError](../../common/type-system.md#keyerror)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `label` | [str](../../common/type-system.md#str) | `必填` | 控件标签；是否支持 [Observable](Observable.md) 见当前方法签名。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [KeyError](../../common/type-system.md#keyerror) | `label` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetSelectOptionByShowName`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_selectLabel(instance, label):
    return instance.selectLabel(label)
```

## removeOption {#removeOption}

```python
removeOption(indexOrLabel: int | str) -> None
```

按索引或原生显示文字移除选项；文字不存在时抛出 [KeyError](../../common/type-system.md#keyerror)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `indexOrLabel` | [int](../../common/type-system.md#int) \| [str](../../common/type-system.md#str) | `必填` | 传给 [UiComboBox.removeOption](UiComboBox.md#removeOption) 的 indexOrLabel 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [KeyError](../../common/type-system.md#keyerror) | `label` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `RemoveOptionByShowName`, `RemoveOptionByIndex`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_removeOption(instance, indexOrLabel):
    return instance.removeOption(indexOrLabel)
```

## clearOptions {#clearOptions}

```python
clearOptions() -> None
```

通过原生下拉框接口清空所有选项。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `ClearOptions`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clearOptions(instance):
    return instance.clearOptions()
```

## 使用示例


```python
from __future__ import print_function

def configure(combo):
    combo.addOption(u"低", "low").addOption(u"高", "high")
    combo.selectedIndex = 0
    return combo.afterEvents.selectionChange.subscribe(lambda event: print(event.value))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)