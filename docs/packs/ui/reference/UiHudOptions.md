---
title: "UiHudOptions"
sidebar_label: "UiHudOptions"
---

# UiHudOptions

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/service.py`；声明补充了静态类型信息。

:::info 字典结构或静态声明
此类型只出现在补全声明中，不是可从模板直接实例化的运行时类。作为选项时使用符合字段约定的 Python 字典。
:::

## 获取方式

使用普通字典传给 [client.ui.createHud](UiService.md#createHud)。

基类：[UiViewOptions](UiViewOptions.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `entity` | [ClientEntity](../../client/reference/ClientEntity.md) | `运行时返回` |
| `location` | [VectorLike](../../common/type-aliases.md#vectorlike) | `运行时返回` |
| `dimension` | [ClientDimension](../../client/reference/ClientDimension.md) | `运行时返回` |
| `offset` | [VectorLike](../../common/type-aliases.md#vectorlike) | `运行时返回` |
| `autoScale` | [bool](../../common/type-system.md#bool) | `运行时返回` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [data](UiViewOptions.md#字段与常量) | [UiViewOptions](UiViewOptions.md) |

## 使用示例


```python
def inspect_options(options):
    print(options.get('entity'))
    print(options.get('location'))
    print(options.get('dimension'))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)