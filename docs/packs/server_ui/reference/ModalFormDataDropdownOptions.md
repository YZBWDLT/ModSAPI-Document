---
title: "ModalFormDataDropdownOptions"
sidebar_label: "ModalFormDataDropdownOptions"
---

# ModalFormDataDropdownOptions

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/builders.py`；声明补充了静态类型信息。

:::info 字典结构或静态声明
此类型只出现在补全声明中，不是可从模板直接实例化的运行时类。作为选项时使用符合字段约定的 Python 字典。
:::

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `defaultValueIndex` | [int](../../common/type-system.md#int) | `运行时返回` |
| `tooltip` | [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict) | `运行时返回` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_options(options):
    print(options.get('defaultValueIndex'))
    print(options.get('tooltip'))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)