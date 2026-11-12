---
title: "UiModelTransformOptions"
sidebar_label: "UiModelTransformOptions"
---

# UiModelTransformOptions

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/renderers.py`；声明补充了静态类型信息。

:::info 字典结构或静态声明
此类型只出现在补全声明中，不是可从模板直接实例化的运行时类。作为选项时使用符合字段约定的 Python 字典。
:::

三类模型预览共用的独立变换参数。

## 获取方式

将普通字典传给模型预览方法，设置缩放、角度、旋转轴和变量。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `scale` | [float](../../common/type-system.md#float) | `可选字段；省略规则见所属操作` | 有限数值缩放；原生默认值为 1.0。 |
| `rotation` | [VectorLike](../../common/type-aliases.md#vectorlike) | `可选字段；省略规则见所属操作` | 初始 X、Y、Z 欧拉角，单位为度。 |
| `rotationAxis` | [VectorLike](../../common/type-aliases.md#vectorlike) | `可选字段；省略规则见所属操作` | 原生手势旋转轴；模板需要启用 freedom_gesture。 |
| `variables` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [float](../../common/type-system.md#float)] | `可选字段；省略规则见所属操作` | 独立复制的变量名称与有限数值。 |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_options(options):
    print(options.get('scale'))
    print(options.get('rotation'))
    print(options.get('rotationAxis'))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)