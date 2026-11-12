---
title: "FlutterStyles"
sidebar_label: "FlutterStyles"
---

# FlutterStyles

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/core/general/controls/innerStyles.py`；声明补充了静态类型信息。

Flutter／Material 风格的浅色和深色模板标识。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `LightPanel` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:light_panel']] | `'flutter:light_panel'` |  |
| `DarkPanel` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:dark_panel']] | `'flutter:dark_panel'` |  |
| `FilledBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:filled_button']] | `'flutter:filled_button'` |  |
| `TonalBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:tonal_button']] | `'flutter:tonal_button'` |  |
| `OutlinedBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:outlined_button']] | `'flutter:outlined_button'` |  |
| `TextBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:text_button']] | `'flutter:text_button'` |  |
| `DangerBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:danger_button']] | `'flutter:danger_button'` |  |
| [Label](Label.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:label']] | `'flutter:label'` |  |
| [Divider](Divider.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:divider']] | `'flutter:divider'` |  |
| [Toggle](Toggle.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:toggle']] | `'flutter:toggle'` |  |
| [Slider](Slider.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:slider']] | `'flutter:slider'` |  |
| [TextField](TextField.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:textfield']] | `'flutter:textfield'` |  |
| [Dropdown](Dropdown.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:dropdown']] | `'flutter:dropdown'` |  |
| [ListView](ListView.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:listview']] | `'flutter:listview'` |  |
| `DarkListView` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:dark_listview']] | `'flutter:dark_listview'` |  |
| `DarkFilledBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:dark_filled_button']] | `'flutter:dark_filled_button'` |  |
| `DarkTonalBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:dark_tonal_button']] | `'flutter:dark_tonal_button'` |  |
| `DarkOutlinedBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:dark_outlined_button']] | `'flutter:dark_outlined_button'` |  |
| `DarkTextBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:dark_text_button']] | `'flutter:dark_text_button'` |  |
| `DarkDangerBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:dark_danger_button']] | `'flutter:dark_danger_button'` |  |
| `DarkLabel` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:dark_label']] | `'flutter:dark_label'` |  |
| `DarkDivider` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:dark_divider']] | `'flutter:dark_divider'` |  |
| `DarkToggle` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:dark_toggle']] | `'flutter:dark_toggle'` |  |
| `DarkSlider` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:dark_slider']] | `'flutter:dark_slider'` |  |
| `DarkTextField` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:dark_textfield']] | `'flutter:dark_textfield'` |  |
| `DarkDropdown` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['flutter:dark_dropdown']] | `'flutter:dark_dropdown'` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 FlutterStyles 对象。
    print(value.LightPanel)
    print(value.DarkPanel)
    print(value.FilledBtn)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)