---
title: "UiNativeScreen"
sidebar_label: "UiNativeScreen"
---

# UiNativeScreen

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/display.py`；声明补充了静态类型信息。

原版界面的请求名称；请求不会返回托管视图。

## 获取方式

从 ModSAPI.ui 导入常量，传给 [client.ui.openNativeScreen](UiService.md#openNativeScreen)。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `Chat` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'chat'` | 原版聊天界面；打开时也会触发原生聊天按钮事件。 |
| `Inventory` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'inventory'` | 原版背包界面，支持内置或模组定义的分页名称。 |
| `Pause` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'pause'` | 原版暂停界面；打开界面不保证暂停多人世界。 |
| `Emotes` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'emotes'` | 原版表情选择界面。 |
| `Menu` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'menu'` | 原版下拉菜单。 |
| `Report` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'report'` | 原版举报界面，是否支持由游戏平台决定。 |
| `Store` | [Final](../../common/type-system.md#final)[[str](../../common/type-system.md#str)] | `'store'` | 网易商品购买界面；打开界面不会自动购买商品。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UiNativeScreen 对象。
    print(value.Chat)
    print(value.Inventory)
    print(value.Pause)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)