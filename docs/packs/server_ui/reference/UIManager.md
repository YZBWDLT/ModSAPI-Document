---
title: "UIManager"
sidebar_label: "UIManager"
---

# UIManager

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/UIManager.py`；声明补充了静态类型信息。

## 获取方式

从 serverui.beta 导入 uiManager 单例；也可获取 [UIManager](UIManager.md) 类型。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [closeAllForms](#closeAllForms) | 方法 |

## closeAllForms {#closeAllForms}

```python
closeAllForms(player: Player) -> None
```

尝试关闭全部匹配的表单，再报告首次关闭失败。

:::note 当前实现说明
尽量关闭全部匹配表单，之后抛出首个关闭错误。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `player` | [Player](../../server/apis/player.md) | `必填` | 目标玩家对象；需要运行时有效且与操作所在端匹配。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `参见本成员的前置条件。` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_closeAllForms(instance, player):
    return instance.closeAllForms(player)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 UIManager 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)