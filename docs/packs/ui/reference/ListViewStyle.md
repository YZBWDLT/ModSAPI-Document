---
title: "ListViewStyle"
sidebar_label: "ListViewStyle"
---

# ListViewStyle

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/core/general/interfaces/controls.pyi`；声明补充了静态类型信息。

:::info 字典结构或静态声明
此类型只出现在补全声明中，不是可从模板直接实例化的运行时类。作为选项时使用符合字段约定的 Python 字典。
:::

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[ControlStyle](ControlStyle.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `itemHeight` | [NumberValue](../../common/type-aliases.md#numbervalue) | `运行时返回` |
| `emptyText` | [TextValue](../../common/type-aliases.md#textvalue) | `运行时返回` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [class](ControlStyle.md#字段与常量) | [ControlStyle](ControlStyle.md) |
| [fontSize](ControlStyle.md#字段与常量) | [ControlStyle](ControlStyle.md) |
| [grid](ControlStyle.md#字段与常量) | [ControlStyle](ControlStyle.md) |
| [height](ControlStyle.md#字段与常量) | [ControlStyle](ControlStyle.md) |
| [offsetX](ControlStyle.md#字段与常量) | [ControlStyle](ControlStyle.md) |
| [offsetY](ControlStyle.md#字段与常量) | [ControlStyle](ControlStyle.md) |
| [visible](ControlStyle.md#字段与常量) | [ControlStyle](ControlStyle.md) |
| [width](ControlStyle.md#字段与常量) | [ControlStyle](ControlStyle.md) |

## 使用示例


```python
def inspect_options(options):
    print(options.get('itemHeight'))
    print(options.get('emptyText'))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)