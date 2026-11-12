---
title: "FluentStyles"
sidebar_label: "FluentStyles"
---

# FluentStyles

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/core/general/controls/innerStyles.py`；声明补充了静态类型信息。

Fluent 风格的浅色和深色模板标识。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `LightPanel` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:light_panel']] | `'fluent:light_panel'` |  |
| `DarkPanel` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_panel']] | `'fluent:dark_panel'` |  |
| `PrimaryBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:primary_button']] | `'fluent:primary_button'` |  |
| `NormalBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:button']] | `'fluent:button'` |  |
| `OutlinedBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:outlined_button']] | `'fluent:outlined_button'` |  |
| `HyperlinkBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:hyperlink_button']] | `'fluent:hyperlink_button'` |  |
| `DangerBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:danger_button']] | `'fluent:danger_button'` |  |
| [Label](Label.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:label']] | `'fluent:label'` |  |
| [Divider](Divider.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:divider']] | `'fluent:divider'` |  |
| [Toggle](Toggle.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:toggle']] | `'fluent:toggle'` |  |
| [Slider](Slider.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:slider']] | `'fluent:slider'` |  |
| [TextField](TextField.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:textfield']] | `'fluent:textfield'` |  |
| [Dropdown](Dropdown.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dropdown']] | `'fluent:dropdown'` |  |
| [ListView](ListView.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:listview']] | `'fluent:listview'` |  |
| `DarkListView` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_listview']] | `'fluent:dark_listview'` |  |
| `DarkPrimaryBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_primary_button']] | `'fluent:dark_primary_button'` |  |
| `DarkNormalBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_button']] | `'fluent:dark_button'` |  |
| `DarkOutlinedBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_outlined_button']] | `'fluent:dark_outlined_button'` |  |
| `DarkHyperlinkBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_hyperlink_button']] | `'fluent:dark_hyperlink_button'` |  |
| `DarkDangerBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_danger_button']] | `'fluent:dark_danger_button'` |  |
| `DarkLabel` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_label']] | `'fluent:dark_label'` |  |
| `DarkDivider` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_divider']] | `'fluent:dark_divider'` |  |
| `DarkToggle` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_toggle']] | `'fluent:dark_toggle'` |  |
| `DarkSlider` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_slider']] | `'fluent:dark_slider'` |  |
| `DarkTextField` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_textfield']] | `'fluent:dark_textfield'` |  |
| `DarkDropdown` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['fluent:dark_dropdown']] | `'fluent:dark_dropdown'` |  |

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