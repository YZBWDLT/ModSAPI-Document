---
title: "Screen"
sidebar_label: "Screen"
---

# Screen

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Screen.py`；声明补充了静态类型信息。

原生屏幕操作；仅在 afterEvents.uiReady 触发后创建屏幕。

## 获取方式

使用 [client.screen](../apis/manager.md#screen)。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [isHud](#isHud) | 只读属性 |
| [top](#top) | 只读属性 |
| [getScreenNode](#getScreenNode) | 方法 |
| [registerUI](#registerUI) | 方法 |
| [pushUI](#pushUI) | 方法 |
| [popUI](#popUI) | 方法 |

## 构造器 {#constructor}

```python
Screen(owner: Any = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `owner` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 传给 [Screen.__init__](Screen.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## isHud {#isHud}

```python
isHud: bool
```

屏幕是否为游戏内主界面。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetTopUI`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isHud
```

## top {#top}

```python
top: Any
```

自定义界面栈顶部的节点，空栈时为 [None](../../common/type-system.md#none)；通过 pushUI/popUI 操作界面栈。

**访问：** 只读。

**返回类型：** [Any](../../common/type-system.md#any)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetTopScreen`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.top
```

## getScreenNode {#getScreenNode}

```python
getScreenNode() -> type
```

返回用于自定义界面实现的原生 [ScreenNode](../../common/type-system.md#screennode) 类。

**返回类型：** [type](../../common/type-system.md#type)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getScreenNode(instance):
    return instance.getScreenNode()
```

## registerUI {#registerUI}

```python
registerUI(identifier: str, uiDef: str, uiClass: str | type) -> None
```

注册界面。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `uiDef` | [str](../../common/type-system.md#str) | `必填` | JSON [UI](../../server_ui/reference/UI.md) 定义路径，例如 example.menu，需已存在于资源包。 |
| `uiClass` | [str](../../common/type-system.md#str) \| [type](../../common/type-system.md#type) | `必填` | [ScreenNode](../../common/type-system.md#screennode) 子类或其完整 Python 类路径。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `"Register UI error! param 'UIClass' should be type str \| ScreenNode, but got %s." % uiClass.__class__.__name__` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `RegisterUI`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_registerUI(instance, identifier, uiDef, uiClass):
    return instance.registerUI(identifier, uiDef, uiClass)
```

## pushUI {#pushUI}

```python
pushUI(identifier: str, extraData: dict[str, Any] | None = None) -> Any
```

将界面压入屏幕栈。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `extraData` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给原生屏幕构造器的附加字典。 |

**返回类型：** [Any](../../common/type-system.md#any)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'extraData must be a dictionary'` |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'PushScreen'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `PushScreen`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_pushUI(instance, identifier):
    return instance.pushUI(identifier)
```

## popUI {#popUI}

```python
popUI() -> None
```

移除顶部界面。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `PopScreen`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_popUI(instance):
    return instance.popUI()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 Screen 对象。
    print(value.isHud)
    print(value.top)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)