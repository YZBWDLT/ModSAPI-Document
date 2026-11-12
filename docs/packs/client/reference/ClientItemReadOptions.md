---
title: "ClientItemReadOptions"
sidebar_label: "ClientItemReadOptions"
---

import ApiFieldAnchor from '@docusaurus/Link';

# ClientItemReadOptions

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Inventory.py`；声明补充了静态类型信息。

:::info 字典结构或静态声明
此类型只出现在补全声明中，不是可从模板直接实例化的运行时类。作为选项时使用符合字段约定的 Python 字典。
:::

原生读取选项，includeUserData 默认 True。

## 获取方式

向客户端物品读取方法传入字典；includeUserData 默认 True，需要轻量结果时显式传入 False。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-includeUserData" />`includeUserData` | [bool](../../common/type-system.md#bool) | `可选字段；省略规则见所属操作` | 是否包含嵌套原生元数据；False 使用更轻量的读取。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_options(options):
    print(options.get('includeUserData'))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)