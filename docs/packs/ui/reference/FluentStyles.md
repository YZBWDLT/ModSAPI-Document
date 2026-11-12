---
title: "FluentStyles"
sidebar_label: "FluentStyles"
---

import ApiFieldAnchor from '@docusaurus/Link';

# FluentStyles

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/core/general/controls/innerStyles.py`；声明补充了静态类型信息。

Fluent 风格的浅色和深色模板标识。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-LightPanel" />`LightPanel` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:light_panel']] | `'fluent:light_panel'` |  |
| <ApiFieldAnchor id="field-DarkPanel" />`DarkPanel` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_panel']] | `'fluent:dark_panel'` |  |
| <ApiFieldAnchor id="field-PrimaryBtn" />`PrimaryBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:primary_button']] | `'fluent:primary_button'` |  |
| <ApiFieldAnchor id="field-NormalBtn" />`NormalBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:button']] | `'fluent:button'` |  |
| <ApiFieldAnchor id="field-OutlinedBtn" />`OutlinedBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:outlined_button']] | `'fluent:outlined_button'` |  |
| <ApiFieldAnchor id="field-HyperlinkBtn" />`HyperlinkBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:hyperlink_button']] | `'fluent:hyperlink_button'` |  |
| <ApiFieldAnchor id="field-DangerBtn" />`DangerBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:danger_button']] | `'fluent:danger_button'` |  |
| <ApiFieldAnchor id="field-Label" />[Label](Label.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:label']] | `'fluent:label'` |  |
| <ApiFieldAnchor id="field-Divider" />[Divider](Divider.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:divider']] | `'fluent:divider'` |  |
| <ApiFieldAnchor id="field-Toggle" />[Toggle](Toggle.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:toggle']] | `'fluent:toggle'` |  |
| <ApiFieldAnchor id="field-Slider" />[Slider](Slider.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:slider']] | `'fluent:slider'` |  |
| <ApiFieldAnchor id="field-TextField" />[TextField](TextField.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:textfield']] | `'fluent:textfield'` |  |
| <ApiFieldAnchor id="field-Dropdown" />[Dropdown](Dropdown.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dropdown']] | `'fluent:dropdown'` |  |
| <ApiFieldAnchor id="field-ListView" />[ListView](ListView.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:listview']] | `'fluent:listview'` |  |
| <ApiFieldAnchor id="field-DarkListView" />`DarkListView` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_listview']] | `'fluent:dark_listview'` |  |
| <ApiFieldAnchor id="field-DarkPrimaryBtn" />`DarkPrimaryBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_primary_button']] | `'fluent:dark_primary_button'` |  |
| <ApiFieldAnchor id="field-DarkNormalBtn" />`DarkNormalBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_button']] | `'fluent:dark_button'` |  |
| <ApiFieldAnchor id="field-DarkOutlinedBtn" />`DarkOutlinedBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_outlined_button']] | `'fluent:dark_outlined_button'` |  |
| <ApiFieldAnchor id="field-DarkHyperlinkBtn" />`DarkHyperlinkBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_hyperlink_button']] | `'fluent:dark_hyperlink_button'` |  |
| <ApiFieldAnchor id="field-DarkDangerBtn" />`DarkDangerBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_danger_button']] | `'fluent:dark_danger_button'` |  |
| <ApiFieldAnchor id="field-DarkLabel" />`DarkLabel` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_label']] | `'fluent:dark_label'` |  |
| <ApiFieldAnchor id="field-DarkDivider" />`DarkDivider` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_divider']] | `'fluent:dark_divider'` |  |
| <ApiFieldAnchor id="field-DarkToggle" />`DarkToggle` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_toggle']] | `'fluent:dark_toggle'` |  |
| <ApiFieldAnchor id="field-DarkSlider" />`DarkSlider` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_slider']] | `'fluent:dark_slider'` |  |
| <ApiFieldAnchor id="field-DarkTextField" />`DarkTextField` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_textfield']] | `'fluent:dark_textfield'` |  |
| <ApiFieldAnchor id="field-DarkDropdown" />`DarkDropdown` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_dropdown']] | `'fluent:dark_dropdown'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 FluentStyles 对象。
    print(value.LightPanel)
    print(value.DarkPanel)
    print(value.PrimaryBtn)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)