---
title: "ClientControlModeOptions"
sidebar_label: "ClientControlModeOptions"
---

import ApiFieldAnchor from '@docusaurus/Link';

# ClientControlModeOptions

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Input.py`；声明补充了静态类型信息。

:::info 字典结构或静态声明
此类型只出现在补全声明中，不是可从模板直接实例化的运行时类。作为选项时使用符合字段约定的 Python 字典。
:::

可选的原生模式锁定配置，在请求布局之后应用。

## 获取方式

向 client.input.setControlMode 传入字典，locked 为可选布尔值；未传入时不修改锁定状态。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-locked" />`locked` | [bool](../../common/type-system.md#bool) | `可选字段；省略规则见所属操作` | 在布局请求成功后锁定或解除控制模式设置。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_options(options):
    print(options.get('locked'))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)