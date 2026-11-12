---
title: "ScreenManager"
sidebar_label: "ScreenManager"
---

# ScreenManager

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/ScreenManager.py`。

屏幕管理器。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [top](#top) | 可读写属性 |
| [pushUI](#pushUI) | 方法 |
| [popUI](#popUI) | 方法 |

## top {#top}

```python
top
```

此屏幕顶部的界面对象。

**访问：** 可读写。

写入方式：`instance.top = value`。参数类型线索：`(newScreen: UI) -> None`。

写入参数 `newScreen`：[UI](../../server_ui/reference/UI.md)。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetTopScreen`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.top

def write_value(instance, value):
    instance.top = value
```

## pushUI {#pushUI}

```python
pushUI(customUI: UI) -> None
```

向玩家显示自定义界面。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `customUI` | [UI](../../server_ui/reference/UI.md) | `必填` | 传给 [ScreenManager.pushUI](ScreenManager.md#pushUI) 的 customUI 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_pushUI(instance, customUI):
    return instance.pushUI(customUI)
```

## popUI {#popUI}

```python
popUI()
```

移除顶部界面。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

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
    # value 是上方获取方式取得的 ScreenManager 对象。
    print(value.top)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)