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
| [hud](#hud) | 只读属性 |
| [setEmotesEnabled](#setEmotesEnabled) | 方法 |
| [screenSize](#screenSize) | 只读属性 |
| [viewport](#viewport) | 只读属性 |
| [getNativeArea](#getNativeArea) | 方法 |
| [openNativeScreen](#openNativeScreen) | 方法 |
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

## hud {#hud}

```python
hud: UiHud
```

本机原生抬头显示的直接控制入口；不会缓存并推断未知显隐状态。

:::note 当前实现说明
本机原生显隐写入入口；没有原生显隐状态查询，也不会通过缓存冒充实际可见性。详见原生抬头显示与原版界面指南。
:::

**访问：** 只读。

**返回类型：** [UiHud](UiHud.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.hud
```

## setEmotesEnabled {#setEmotesEnabled}

```python
setEmotesEnabled(enabled: bool) -> None
```

在原生界面首次初始化前配置手机端表情功能，与隐藏已经创建的表情按钮不同。应在客户端初始化早期调用，不要放在界面就绪回调中；即使托管表单注册失败，原生初始化事件发生后也不能再配置。保留引擎报告的失败；具体平台支持由引擎决定，尚未实机验证。没有伪造原生读取或旧值自动恢复。

:::note 当前实现说明
仅在客户端、原生界面初始化事件之前配置；不使用 uiReady 回调。表单注册失败也不重新打开初始化窗口。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enabled` | [bool](../../common/type-system.md#bool) | `必填` | 传给 [UiService.setEmotesEnabled](UiService.md#setEmotesEnabled) 的 enabled 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Native emotes must be configured before UI initialization'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetEmoteSwitch`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setEmotesEnabled(instance, enabled):
    return instance.setEmotesEnabled(enabled)
```

## screenSize {#screenSize}

```python
screenSize: Vector2
```

界面就绪后重新读取物理窗口宽度和高度，单位为像素。

**访问：** 只读。

**返回类型：** [Vector2](../../common/reference/Vector2.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.screenSize
```

## viewport {#viewport}

```python
viewport: UiViewport
```

界面就绪后读取原生视角宽高和横纵偏移，返回独立快照。

**访问：** 只读。

**返回类型：** [UiViewport](UiViewport.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.viewport
```

## getNativeArea {#getNativeArea}

```python
getNativeArea(area: str) -> UiRectangle
```

读取 [UiNativeArea](UiNativeArea.md) 指定区域在基类画布中的矩形。区域不可用时保留原生全零结果，不能将其视为控件可见或可点击的保证。

:::note 当前实现说明
返回基类画布矩形；全零保留为原生不可用结果，不视为可见或可点击的证明。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `area` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiService.getNativeArea](UiService.md#getNativeArea) 的 area 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [UiRectangle](UiRectangle.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getNativeArea(instance, area):
    return instance.getNativeArea(area)
```

## openNativeScreen {#openNativeScreen}

```python
openNativeScreen(screen: str, options: UiNativeScreenOptions | None = None) -> None
```

界面就绪后请求打开 [UiNativeScreen](UiNativeScreen.md) 指定的原版界面，返回 [None](../../common/type-system.md#none)。聊天、暂停和背包支持 force，默认 False；背包还支持 categoryName，默认建筑分页 construction，也可使用自定义分页。商店要求 categoryName 和 itemName，其他界面不接受选项。原生无返回值不证明界面已打开，不会伪造托管视图或自动关闭回调。不要从聊天按钮事件再次打开聊天；同步递归请求会被拒绝，失败后会释放重入保护。

:::note 当前实现说明
请求打开七种原版界面。返回 [None](../../common/type-system.md#none) 不证明已显示；不是托管视图，不会伪造 [UiView](UiView.md) 或关闭回调。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `screen` | [str](../../common/type-system.md#str) | `必填` | 传给 [UiService.openNativeScreen](UiService.md#openNativeScreen) 的 screen 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [UiNativeScreenOptions](UiNativeScreenOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_openNativeScreen(instance, screen):
    return instance.openNativeScreen(screen)
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

打开托管界面栈视图，可通过 inputPermissions 临时覆盖本地输入。控件在就绪后可用。输入覆盖在原生创建前应用，关闭或创建失败时释放。准备权限期间取消的视图不会继续创建原生界面。

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

创建绑定当前界面服务运行时的主题表单。客户端显示时可以省略玩家；后续操作、目标校验和回调玩家类型始终沿用表单所属端。

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