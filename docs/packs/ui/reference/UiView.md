---
title: "UiView"
sidebar_label: "UiView"
---

# UiView

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/views.py`；声明补充了静态类型信息。

本地界面或常驻视图；视图关闭时，它拥有的控件和绑定随之失效。

## 获取方式

由 [client.ui.openView](UiService.md#openView) 或 [client.ui.createHud](UiService.md#createHud) 返回。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [identifier](#identifier) | 只读属性 |
| [player](#player) | 只读属性 |
| [data](#data) | 只读属性 |
| [isHud](#isHud) | 只读属性 |
| [isValid](#isValid) | 只读属性 |
| [isReady](#isReady) | 只读属性 |
| [closeReason](#closeReason) | 只读属性 |
| [afterEvents](#afterEvents) | 只读属性 |
| [native](#native) | 只读属性 |
| [getControl](#getControl) | 方法 |
| [createControl](#createControl) | 方法 |
| [refresh](#refresh) | 方法 |
| [setVisible](#setVisible) | 方法 |
| [close](#close) | 方法 |

## identifier {#identifier}

```python
identifier: str
```

读取 `identifier` 的当前值。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.identifier
```

## player {#player}

```python
player: ClientPlayer
```

读取 `player` 的当前值。

**访问：** 只读。

**返回类型：** [ClientPlayer](../../client/reference/ClientPlayer.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.player
```

## data {#data}

```python
data: dict[str, Any]
```

打开界面或创建常驻视图时传入的业务数据副本。

**访问：** 只读。

**返回类型：** [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.data
```

## isHud {#isHud}

```python
isHud: bool
```

读取 `isHud` 的当前值。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isHud
```

## isValid {#isValid}

```python
isValid: bool
```

读取 `isValid` 的当前值。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## isReady {#isReady}

```python
isReady: bool
```

读取 `isReady` 的当前值。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isReady
```

## closeReason {#closeReason}

```python
closeReason: str | None
```

读取 `closeReason` 的当前值。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.closeReason
```

## afterEvents {#afterEvents}

```python
afterEvents: UiViewEvents
```

读取 `afterEvents` 的当前值。

**访问：** 只读。

**返回类型：** [UiViewEvents](UiViewEvents.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.afterEvents
```

## native {#native}

```python
native: Any
```

明确取得原生屏幕节点，供封装之外的引擎操作使用。

**访问：** 只读。

**返回类型：** [Any](../../common/type-system.md#any)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.native
```

## getControl {#getControl}

```python
getControl(path: str, kind: Literal['control', 'label', 'button', 'image', 'textField', 'slider', 'toggle', 'scrollView', 'grid', 'stackPanel', 'inputPanel', 'progressBar', 'itemRenderer', 'comboBox', 'selectionWheel', 'miniMap', 'modelRenderer'] = 'control') -> UiControl
```

通过现有界面绝对路径获取指定类型的控件对象。kind 支持网格、堆叠面板、输入面板、物品预览和进度条等控件；类型必须与模板匹配。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `path` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiView.getControl](UiView.md#getControl) 的 path 参数；结合上方功能说明和下方调用示例使用。 |
| `kind` | [Literal](../../common/type-system.md#literal)['control', 'label', 'button', 'image', 'textField', 'slider', 'toggle', 'scrollView', 'grid', 'stackPanel', 'inputPanel', 'progressBar', 'itemRenderer', 'comboBox', 'selectionWheel', 'miniMap', 'modelRenderer'] | `'control'` | 传给 [UiView.getControl](UiView.md#getControl) 的 kind 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [UiControl](UiControl.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown UI control kind'` |
| [KeyError](../../common/type-system.md#keyerror) | `'UI control not found: ' + path` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetBaseUIControl`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getControl(instance, path):
    return instance.getControl(path)
```

## createControl {#createControl}

```python
createControl(template: str, name: str, parent: UiControl | None = None, kind: str = 'control') -> UiControl
```

从已登记的界面模板动态创建子控件。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `template` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiView.createControl](UiView.md#createControl) 的 template 参数；结合上方功能说明和下方调用示例使用。 |
| `name` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiView.createControl](UiView.md#createControl) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `parent` | [UiControl](UiControl.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [UiView.createControl](UiView.md#createControl) 的 parent 参数；结合上方功能说明和下方调用示例使用。 |
| `kind` | [str](../../common/type-system.md#str) | `'control'` | 传给 [UiView.createControl](UiView.md#createControl) 的 kind 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [UiControl](UiControl.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'A control name must be a single path component'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown UI control kind'` |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'CreateChildControl'` |
| [TypeError](../../common/type-system.md#typeerror) | `'parent must be a UiControl'` |
| [ValueError](../../common/type-system.md#valueerror) | `'The parent belongs to a different UI view'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `RemoveChildControl`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createControl(instance, template, name):
    return instance.createControl(template, name)
```

## refresh {#refresh}

```python
refresh() -> None
```

通过原生屏幕节点刷新批量可见性和布局修改。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `UpdateScreen`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_refresh(instance):
    return instance.refresh()
```

## setVisible {#setVisible}

```python
setVisible(visible: bool) -> None
```

设置 `setVisible` 操作。原生实现使用 `SetScreenVisible`，行为受网易运行环境约束。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `visible` | [bool](../../common/type-system.md#bool) | `必填` | 传给 [UiView.setVisible](UiView.md#setVisible) 的 visible 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetScreenVisible`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setVisible(instance, visible):
    return instance.setVisible(visible)
```

## close {#close}

```python
close() -> None
```

删除当前视图自己的界面节点，并释放它拥有的回调和绑定。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_close(instance):
    return instance.close()
```

## 使用示例


```python
def close_view(view):
    if view.isValid:
        view.close()
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)