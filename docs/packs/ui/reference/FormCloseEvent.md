---
title: "FormCloseEvent"
sidebar_label: "FormCloseEvent"
---

# FormCloseEvent

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/core/utils/type.py`；声明补充了静态类型信息。

## 获取方式

通过 [Form.show](Form.md#show) 的关闭回调取得，player 按表单所属端包装为 [Player](../../server/apis/player.md) 或本地 [ClientPlayer](../../client/reference/ClientPlayer.md)。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [closeReason](#closeReason) | 只读属性 |
| [player](#player) | 只读属性 |

## closeReason {#closeReason}

```python
closeReason: str
```

读取 `closeReason` 的当前值。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.closeReason
```

## player {#player}

```python
player: Player | ClientPlayer
```

界面已关闭的玩家，按表单所属端包装为对应玩家对象。

**访问：** 只读。

**返回类型：** [Player](../../server/apis/player.md) \| [ClientPlayer](../../client/reference/ClientPlayer.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.player
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 FormCloseEvent 对象。
    print(value.closeReason)
    print(value.player)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)