---
title: "OreUIStyles"
sidebar_label: "OreUIStyles"
---

# OreUIStyles

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/core/general/controls/innerStyles.py`；声明补充了静态类型信息。

内置 OreUI 风格表单和控件的模板标识。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `GreenBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:green_btn_thin']] | `'oreui:green_btn_thin'` |
| `GreenBtnBold` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:green_btn']] | `'oreui:green_btn'` |
| `RedBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:red_btn_thin']] | `'oreui:red_btn_thin'` |
| `RedBtnBold` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:red_btn']] | `'oreui:red_btn'` |
| `NormalBtn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:normal_btn_thin']] | `'oreui:normal_btn_thin'` |
| `NormalBtnBold` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:normal_btn']] | `'oreui:normal_btn'` |
| `LightPanel` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:light_panel_thin']] | `'oreui:light_panel_thin'` |
| [Label](Label.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:label']] | `'oreui:label'` |
| `DividerIn` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:divider_in']] | `'oreui:divider_in'` |
| `DividerOut` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:divider_out']] | `'oreui:divider_out'` |
| `DividerDark` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:divider_dark']] | `'oreui:divider_dark'` |
| `DividerLight` | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:divider_light']] | `'oreui:divider_light'` |
| [Slider](Slider.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:slider']] | `'oreui:slider'` |
| [TextField](TextField.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:textfield']] | `'oreui:textfield'` |
| [Dropdown](Dropdown.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:dropdown']] | `'oreui:dropdown'` |
| [ListView](ListView.md) | [Final](../../common/type-system.md#final)[[Literal](../../common/type-system.md#literal)['oreui:listview']] | `'oreui:listview'` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 OreUIStyles 对象。
    print(value.GreenBtn)
    print(value.GreenBtnBold)
    print(value.RedBtn)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)