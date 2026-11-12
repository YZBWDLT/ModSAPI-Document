---
title: "UiService"
sidebar_label: "UiService"
---

# UiService

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/service.py`；声明补充了静态类型信息。

管理本地视图以及组合表单、状态工厂。原生视图在客户端操作；服务端创建表单并向玩家对象显示，不能直接读取远端原生界面树。

## 获取方式

通过 [client.ui](../../client/apis/manager.md#ui) 或 [system.ui](../../server/reference/System.md#ui) 获取。原生视图方法只在客户端可用。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [isReady](#isReady) | 只读属性 |
| [views](#views) | 只读属性 |
| [currentView](#currentView) | 只读属性 |
| [registerView](#registerView) | 方法 |
| [openView](#openView) | 方法 |
| [createHud](#createHud) | 方法 |
| [closeAllViews](#closeAllViews) | 方法 |
| [createForm](#createForm) | 方法 |
| [createState](#createState) | 方法 |
| [setGrid](#setGrid) | 方法 |
| [clearGrid](#clearGrid) | 方法 |
| [setTheme](#setTheme) | 方法 |
| [closeAllForms](#closeAllForms) | 方法 |

## isReady {#isReady}

```python
isReady: bool
```

界面运行时是否可用；客户端还需要原生界面已经初始化。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isReady
```

## views {#views}

```python
views: tuple[UiView, ...]
```

本运行时拥有的待创建和已就绪视图，返回独立元组。

**访问：** 只读。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[UiView](UiView.md), ...]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.views
```

## currentView {#currentView}

```python
currentView: UiView | None
```

当前由本库拥有的栈顶视图；其他界面位于顶层时返回 [None](../../common/type-system.md#none)。

**访问：** 只读。

**返回类型：** [UiView](UiView.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetTopScreen`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.currentView
```

## registerView {#registerView}

```python
registerView(name: str, template: str, options: UiViewCallbacks | None = None) -> UiViewDefinition
```

声明带生命周期回调和可选小地图支持的 JSON 界面。可在界面初始化前声明，首次在 uiReady 后打开时才注册原生界面。miniMap=True 会使用原生小地图基类，并保留该基类的生命周期方法。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiService.registerView](UiService.md#registerView) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `template` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiService.registerView](UiService.md#registerView) 的 template 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [UiViewCallbacks](UiViewCallbacks.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [UiViewDefinition](UiViewDefinition.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'A view with this identifier is already declared: ' + name` |
| [TypeError](../../common/type-system.md#typeerror) | `option + ' must be callable'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_registerView(instance, name, template):
    return instance.registerView(name, template)
```

## openView {#openView}

```python
openView(name: str, options: UiViewOptions | None = None) -> UiView
```

打开托管的界面栈视图，可通过 inputPermissions 指定所属视图的临时输入权限。控件在就绪回调中可用；输入覆盖在原生创建前应用，并在关闭或创建失败时尝试释放。

:::note 当前实现说明
可在 inputPermissions 中传入本地输入通道与布尔值。覆盖在原生创建前应用，视图关闭或创建失败时尝试释放；不影响服务端权限。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiService.openView](UiService.md#openView) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [UiViewOptions](UiViewOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [UiView](UiView.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_openView(instance, name):
    return instance.openView(name)
```

## createHud {#createHud}

```python
createHud(name: str, options: UiHudOptions | None = None) -> UiView
```

为一个注册标识创建常驻视图，可绑定实体。实体和维度使用客户端包装对象；实体目标与世界位置互斥，渲染距离由引擎决定。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiService.createHud](UiService.md#createHud) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [UiHudOptions](UiHudOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [UiView](UiView.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createHud(instance, name):
    return instance.createHud(name)
```

## closeAllViews {#closeAllViews}

```python
closeAllViews() -> None
```

尝试关闭所有拥有的视图，全部尝试后报告首个原生失败。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `参见本成员的前置条件。` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_closeAllViews(instance):
    return instance.closeAllViews()
```

## createForm {#createForm}

```python
createForm(title: str | Observable, options: dict[str, Any] | None = None) -> Form
```

创建主题表单；客户端显示时可以省略玩家目标。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `title` | [str](../../common/type-system.md#str) \| [Observable](Observable.md) | `必填` | 标题文本，动态表单也可接受相应 [Observable](Observable.md)。 |
| `options` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [Form](Form.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createForm(instance, title):
    return instance.createForm(title)
```

## createState {#createState}

```python
createState(value: Any) -> Observable
```

创建属于当前端界面运行时的响应式状态。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `value` | [Any](../../common/type-system.md#any) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [Observable](Observable.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_createState(instance, value):
    return instance.createState(value)
```

## setGrid {#setGrid}

```python
setGrid(columns: int | list[float] = 1, rows: int | list[float] = 1, options: dict[str, Any] | None = None) -> None
```

设置带权重的行列布局，可指定间距和内边距。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `columns` | [int](../../common/type-system.md#int) \| [list](../../common/type-system.md#list)[[float](../../common/type-system.md#float)] | `1` | 传给 [UiService.setGrid](UiService.md#setGrid) 的 columns 参数；结合上方功能说明和下方调用示例使用。 |
| `rows` | [int](../../common/type-system.md#int) \| [list](../../common/type-system.md#list)[[float](../../common/type-system.md#float)] | `1` | 传给 [UiService.setGrid](UiService.md#setGrid) 的 rows 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setGrid(instance):
    return instance.setGrid()
```

## clearGrid {#clearGrid}

```python
clearGrid() -> None
```

为随后创建的表单恢复默认顺序布局。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clearGrid(instance):
    return instance.clearGrid()
```

## setTheme {#setTheme}

```python
setTheme(name: str | None) -> None
```

设置随后创建的表单使用的内置或自定义主题。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../../common/type-system.md#str) \| [None](../../common/type-system.md#none) | `必填` | 传给 [UiService.setTheme](UiService.md#setTheme) 的 name 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setTheme(instance, name):
    return instance.setTheme(name)
```

## closeAllForms {#closeAllForms}

```python
closeAllForms(player: Player | ClientPlayer | list[Player] | None = None) -> None
```

为指定玩家对象关闭表单；省略目标时关闭此运行时管理的全部显示实例。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | [Player](../../server/apis/player.md) \| [ClientPlayer](../../client/reference/ClientPlayer.md) \| [list](../../common/type-system.md#list)[[Player](../../server/apis/player.md)] \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `参见本成员的前置条件。` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_closeAllForms(instance):
    return instance.closeAllForms()
```

## 使用示例


```python
from ModSAPI.client.beta import client

def has_ui():
    return client.ui.isReady
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)