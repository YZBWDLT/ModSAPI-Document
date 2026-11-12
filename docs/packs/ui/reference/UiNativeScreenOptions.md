---
title: "UiNativeScreenOptions"
sidebar_label: "UiNativeScreenOptions"
---

# UiNativeScreenOptions

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/display.py`；声明补充了静态类型信息。

:::info 字典结构或静态声明
此类型只出现在补全声明中，不是可从模板直接实例化的运行时类。作为选项时使用符合字段约定的 Python 字典。
:::

原版界面的专用选项；必填字段由所选界面决定。

## 获取方式

向 [client.ui.openNativeScreen](UiService.md#openNativeScreen) 传入字典；不同界面的可用字段与必填项不同。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `force` | [bool](../../common/type-system.md#bool) | `可选字段；省略规则见所属操作` | 请求在已有菜单时也打开界面；仅聊天、暂停和背包支持。 |
| `categoryName` | [str](../../common/type-system.md#str) | `可选字段；省略规则见所属操作` | 背包分页名，或商店必填的分类名。背包默认使用建筑分页 construction。 |
| `itemName` | [str](../../common/type-system.md#str) | `可选字段；省略规则见所属操作` | 商店必填的商品名称；其他界面不接受此字段。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_options(options):
    print(options.get('force'))
    print(options.get('categoryName'))
    print(options.get('itemName'))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)