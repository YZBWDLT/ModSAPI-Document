---
title: "UiHud"
sidebar_label: "UiHud"
---

# UiHud

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/display.py`；声明补充了静态类型信息。

由有效本机界面服务持有的原生抬头显示写入入口。调用需要界面就绪。原生接口没有显隐读取，因此不能恢复未知旧状态、推断真实可见性或隔离其他模组；客户端退出时不会隐式全局重置。

## 获取方式

从 [client.ui.hud](UiService.md#hud) 取得本地原生抬头显示控制句柄；实际调用需要界面就绪。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [setHudVisibility](#setHudVisibility) | 方法 |
| [setHidden](#setHidden) | 方法 |
| [setChatPosition](#setChatPosition) | 方法 |
| [playHealthBlink](#playHealthBlink) | 方法 |

## setHudVisibility {#setHudVisibility}

```python
setHudVisibility(visibility: int, hudElements: list[str] | tuple[str, ...] | None = None) -> None
```

隐藏或恢复 [UiHudElement](UiHudElement.md) 的指定原生抬头显示通道，使用 [HudVisibility](../../common/reference/HudVisibility.md) 的 Hide 或 Reset。省略元素时操作全部二十二个受支持通道，空序列不写入。写入前检查全部参数和方法是否存在；重复通道按首次出现顺序处理一次。后续原生失败可能保留先前修改，没有显隐快照用于回滚。

:::note 当前实现说明
省略元素时操作全部二十二个已支持通道；空列表不写入。先校验整批参数与方法是否存在，但不提供失败回滚或跨模组隔离。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `visibility` | [int](../../common/type-system.md#int) | `必填` | 传给 [UiHud.setHudVisibility](UiHud.md#setHudVisibility) 的 visibility 参数；结合上方功能说明和下方调用示例使用。 |
| `hudElements` | [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)] \| [tuple](../../common/type-system.md#tuple)[[str](../../common/type-system.md#str), ...] \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [UiHud.setHudVisibility](UiHud.md#setHudVisibility) 的 hudElements 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'visibility must be HudVisibility.Hide or Reset'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown HUD visibility'` |
| [TypeError](../../common/type-system.md#typeerror) | `'hudElements must be a sequence of UiHudElement values'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown native HUD element: ' + element` |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `method` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setHudVisibility(instance, visibility):
    return instance.setHudVisibility(visibility)
```

## setHidden {#setHidden}

```python
setHidden(hidden: bool) -> None
```

应用类似 F1 的全局抬头显示隐藏；隐藏位置仍可能响应触控。此入口操作全局开关，传入 False 时释放该开关，不会逐项调用元素重置。

:::note 当前实现说明
类似 F1 的全局隐藏，原位置可能继续响应输入；不会逐项调用元素重置。输入限制请使用 [client.input](../../client/apis/manager.md#input)。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `hidden` | [bool](../../common/type-system.md#bool) | `必填` | 传给 [UiHud.setHidden](UiHud.md#setHidden) 的 hidden 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setHidden(instance, hidden):
    return instance.setHidden(hidden)
```

## setChatPosition {#setChatPosition}

```python
setChatPosition(position: Vector2 | tuple[float, float] | list[float] | dict[str, float]) -> None
```

以有限的二维坐标移动抬头显示中的小消息窗口。原点在玩家纸娃娃下方，不是物理窗口原点；保留负坐标和零值。此原生接口不提供位置读取或自动恢复。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `position` | [Vector2](../../common/reference/Vector2.md) \| [tuple](../../common/type-system.md#tuple)[[float](../../common/type-system.md#float), [float](../../common/type-system.md#float)] \| [list](../../common/type-system.md#list)[[float](../../common/type-system.md#float)] \| [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [float](../../common/type-system.md#float)] | `必填` | 位置或坐标；采用本接口所属的原生坐标约定。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setChatPosition(instance, position):
    return instance.setChatPosition(position)
```

## playHealthBlink {#playHealthBlink}

```python
playHealthBlink() -> None
```

播放原版受伤生命值闪烁动画，不会给玩家造成伤害。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_playHealthBlink(instance):
    return instance.playHealthBlink()
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 UiHud 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)