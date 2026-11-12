---
title: "UiSkeletonRenderOptions"
sidebar_label: "UiSkeletonRenderOptions"
---

import ApiFieldAnchor from '@docusaurus/Link';

# UiSkeletonRenderOptions

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/renderers.py`；声明补充了静态类型信息。

:::info 字典结构或静态声明
此类型只出现在补全声明中，不是可从模板直接实例化的运行时类。作为选项时使用符合字段约定的 Python 字典。
:::

骨骼预览的变换、动画播放和原生光照选项。

## 获取方式

传给 [UiModelRenderer.setSkeletonModel](UiModelRenderer.md#setSkeletonModel)，包含变换、深度、动画和光照。

基类：[UiEntityRenderOptions](UiEntityRenderOptions.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-scale" />`scale` | [float](../../common/type-system.md#float) | `可选字段；省略规则见所属操作` | 有限数值缩放；原生默认值为 1.0。 |
| <ApiFieldAnchor id="field-rotation" />`rotation` | [VectorLike](../../common/type-aliases.md#vectorlike) | `可选字段；省略规则见所属操作` | 初始 X、Y、Z 欧拉角，单位为度。 |
| <ApiFieldAnchor id="field-rotationAxis" />`rotationAxis` | [VectorLike](../../common/type-aliases.md#vectorlike) | `可选字段；省略规则见所属操作` | 原生手势旋转轴；模板需要启用 freedom_gesture。 |
| <ApiFieldAnchor id="field-variables" />`variables` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [float](../../common/type-system.md#float)] | `可选字段；省略规则见所属操作` | 独立复制的变量名称与有限数值。 |
| <ApiFieldAnchor id="field-depth" />`depth` | [int](../../common/type-system.md#int) | `可选字段；省略规则见所属操作` | 原生整数渲染深度；省略时沿用原生默认值。 |
| <ApiFieldAnchor id="field-animation" />`animation` | [str](../../common/type-system.md#str) | `可选字段；省略规则见所属操作` | 网易骨骼动画名称；原生默认值为 idle。 |
| <ApiFieldAnchor id="field-loop" />`loop` | [bool](../../common/type-system.md#bool) | `可选字段；省略规则见所属操作` | 是否循环播放骨骼动画；原生默认值为 True。 |
| <ApiFieldAnchor id="field-lightDirection" />`lightDirection` | [VectorLike](../../common/type-aliases.md#vectorlike) | `可选字段；省略规则见所属操作` | 光照的 X、Y、Z 坐标，各为 -1、0 或 1，受原生材质限制。 |

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