---
title: "EventSubscriptionOptions"
sidebar_label: "EventSubscriptionOptions"
---

import ApiFieldAnchor from '@docusaurus/Link';

# EventSubscriptionOptions

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/utils/event_facade.py`；声明补充了静态类型信息。

:::info 字典结构或静态声明
此类型只出现在补全声明中，不是可从模板直接实例化的运行时类。作为选项时使用符合字段约定的 Python 字典。
:::

筛选条件的副本。每个信号仅接受其目录中列出的选项键。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-entities" />`entities` | [list](../type-system.md#list)[[Union](../type-system.md#union)[[Entity](../../server/apis/entity.md), [ClientEntity](../../client/reference/ClientEntity.md)]] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-entityTypes" />`entityTypes` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-dimensions" />`dimensions` | [list](../type-system.md#list)[[Union](../type-system.md#union)[[Dimension](../../server/apis/dimension.md), [ClientDimension](../../client/reference/ClientDimension.md)]] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-buttons" />`buttons` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-actions" />`actions` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-axes" />`axes` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-controlTypes" />`controlTypes` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-state" />`state` | [str](../type-system.md#str) | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-devices" />`devices` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-screenNames" />`screenNames` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-states" />`states` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-inventoryTypes" />`inventoryTypes` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-allowedSlots" />`allowedSlots` | [list](../type-system.md#list)[[int](../type-system.md#int)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-includeItems" />`includeItems` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-excludeItems" />`excludeItems` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-ignoreQuantityChange" />`ignoreQuantityChange` | [bool](../type-system.md#bool) | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-areaNames" />`areaNames` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-effectTypes" />`effectTypes` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-changeTypes" />`changeTypes` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-weatherTypes" />`weatherTypes` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-lootTypes" />`lootTypes` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |
| <ApiFieldAnchor id="field-blockTypes" />`blockTypes` | [list](../type-system.md#list)[[str](../type-system.md#str)] | `可选字段；省略规则见所属操作` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_options(options):
    print(options.get('entities'))
    print(options.get('entityTypes'))
    print(options.get('dimensions'))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)