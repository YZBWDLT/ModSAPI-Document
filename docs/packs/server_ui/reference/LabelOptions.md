---
title: "LabelOptions"
sidebar_label: "LabelOptions"
---

# LabelOptions

作用域：服务端表单 / 客户端 [UI](UI.md) 底层类型。

源码：`core_behavior/ModSAPI/modules/server_ui/FormData.py`；声明补充了静态类型信息。

:::info 字典结构或静态声明
此类型只出现在补全声明中，不是可从模板直接实例化的运行时类。作为选项时使用符合字段约定的 Python 字典。
:::

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[Options](Options.md).

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [description](Options.md#字段与常量) | [Options](Options.md) |
| [disabled](Options.md#字段与常量) | [Options](Options.md) |
| [tooltip](Options.md#字段与常量) | [Options](Options.md) |
| [visible](Options.md#字段与常量) | [Options](Options.md) |

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 LabelOptions 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)