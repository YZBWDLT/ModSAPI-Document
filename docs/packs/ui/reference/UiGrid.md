---
title: "UiGrid"
sidebar_label: "UiGrid"
---

# UiGrid

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/widgets.py`；声明补充了静态类型信息。

由原生模板驱动的网格控件，与表单的权重布局分别使用。

## 获取方式

使用 view.getControl(path, "grid")，格子由资源包模板创建。

基类：[UiControl](UiControl.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [setDimensions](#setDimensions) | 方法 |
| [getItem](#getItem) | 方法 |

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

## setDimensions {#setDimensions}

```python
setDimensions(columns: int, rows: int) -> None
```

设置非负的原生列数和行数；网格项可能重建。调整后应重新通过 getItem 获取控件；具体创建方式和存在的项目由网格模板决定。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `columns` | [int](../../common/type-system.md#int) | `必填` | 传给 [UiGrid.setDimensions](UiGrid.md#setDimensions) 的 columns 参数；结合上方功能说明和下方调用示例使用。 |
| `rows` | [int](../../common/type-system.md#int) | `必填` | 传给 [UiGrid.setDimensions](UiGrid.md#setDimensions) 的 rows 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetGridDimension`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setDimensions(instance, columns, rows):
    return instance.setDimensions(columns, rows)
```

## getItem {#getItem}

```python
getItem(column: int, row: int, kind: Literal['control', 'label', 'button', 'image', 'textField', 'slider', 'toggle', 'scrollView', 'grid', 'stackPanel', 'inputPanel', 'progressBar', 'itemRenderer', 'comboBox', 'selectionWheel', 'miniMap', 'modelRenderer'] = 'control') -> UiControl | None
```

按从零开始的行列坐标获取网格项，并返回包装后的控件；不存在时返回 [None](../../common/type-system.md#none)。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `column` | [int](../../common/type-system.md#int) | `必填` | 传给 [UiGrid.getItem](UiGrid.md#getItem) 的 column 参数；结合上方功能说明和下方调用示例使用。 |
| `row` | [int](../../common/type-system.md#int) | `必填` | 传给 [UiGrid.getItem](UiGrid.md#getItem) 的 row 参数；结合上方功能说明和下方调用示例使用。 |
| `kind` | [Literal](../../common/type-system.md#literal)['control', 'label', 'button', 'image', 'textField', 'slider', 'toggle', 'scrollView', 'grid', 'stackPanel', 'inputPanel', 'progressBar', 'itemRenderer', 'comboBox', 'selectionWheel', 'miniMap', 'modelRenderer'] | `'control'` | 传给 [UiGrid.getItem](UiGrid.md#getItem) 的 kind 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [UiControl](UiControl.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown UI control kind'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGridItem`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getItem(instance, column, row):
    return instance.getItem(column, row)
```

## 使用示例


```python
def fill_grid(grid):
    grid.setDimensions(2, 1)
    cell = grid.getItem(0, 0, "itemRenderer")
    if cell is not None:
        cell.setItem("minecraft:diamond")
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)