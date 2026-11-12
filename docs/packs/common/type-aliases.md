---
title: 类型别名
---

# 类型别名

类型别名只用于静态补全，不是构造函数。[VectorLike](type-aliases.md#vectorlike) 表示接口接受的几种坐标输入；仍要满足各方法的有限值和字段校验。

## UiLength {#uilength}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [UiLength](type-aliases.md#uilength) | [int](type-system.md#int) \| [float](type-system.md#float) \| [str](type-system.md#str) \| [Observable](../ui/reference/Observable.md)[[int](type-system.md#int)] \| [Observable](../ui/reference/Observable.md)[[float](type-system.md#float)] \| [Observable](../ui/reference/Observable.md)[[str](type-system.md#str)] | `core_behavior/ModSAPI/_ui/core/general/interfaces/controls.pyi` |

## UiLengthPair {#uilengthpair}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [UiLengthPair](type-aliases.md#uilengthpair) | [list](type-system.md#list)[[UiLength](type-aliases.md#uilength)] \| [Observable](../ui/reference/Observable.md)[[list](type-system.md#list)[[Any](type-system.md#any)]] | `core_behavior/ModSAPI/_ui/core/general/interfaces/controls.pyi` |

## TextValue {#textvalue}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [TextValue](type-aliases.md#textvalue) | [str](type-system.md#str) \| [Observable](../ui/reference/Observable.md)[[str](type-system.md#str)] | `core_behavior/ModSAPI/_ui/core/general/interfaces/controls.pyi` |

## NumberValue {#numbervalue}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [NumberValue](type-aliases.md#numbervalue) | [int](type-system.md#int) \| [float](type-system.md#float) \| [Observable](../ui/reference/Observable.md)[[int](type-system.md#int)] \| [Observable](../ui/reference/Observable.md)[[float](type-system.md#float)] | `core_behavior/ModSAPI/_ui/core/general/interfaces/controls.pyi` |

## FontSize {#fontsize}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [FontSize](type-aliases.md#fontsize) | [NumberValue](type-aliases.md#numbervalue) \| [Literal](type-system.md#literal)['default'] \| [Observable](../ui/reference/Observable.md)[[str](type-system.md#str)] \| [Observable](../ui/reference/Observable.md)[[int](type-system.md#int) \| [float](type-system.md#float)] \| [Observable](../ui/reference/Observable.md)[[int](type-system.md#int) \| [str](type-system.md#str)] \| [Observable](../ui/reference/Observable.md)[[float](type-system.md#float) \| [str](type-system.md#str)] \| [Observable](../ui/reference/Observable.md)[[int](type-system.md#int) \| [float](type-system.md#float) \| [str](type-system.md#str)] | `core_behavior/ModSAPI/_ui/core/general/interfaces/controls.pyi` |

## BoolValue {#boolvalue}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [BoolValue](type-aliases.md#boolvalue) | [bool](type-system.md#bool) \| [Observable](../ui/reference/Observable.md)[[bool](type-system.md#bool)] | `core_behavior/ModSAPI/_ui/core/general/interfaces/controls.pyi` |

## PlayerCallback {#playercallback}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [PlayerCallback](type-aliases.md#playercallback) | [Callable](type-system.md#callable)[[[Player](../server/apis/player.md) \| [ClientPlayer](../client/reference/ClientPlayer.md)], [None](type-system.md#none)] | `core_behavior/ModSAPI/_ui/core/general/interfaces/controls.pyi` |

## ControlKind {#controlkind}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [ControlKind](type-aliases.md#controlkind) | [Literal](type-system.md#literal)['button', 'panel', 'scrolling_panel', 'toggle', 'label', 'textfield', 'slider', 'dropdown', 'listview', 'custom', 'group', 'divider'] | `core_behavior/ModSAPI/_ui/core/general/interfaces/controls.pyi` |

## ButtonHandler {#buttonhandler}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [ButtonHandler](type-aliases.md#buttonhandler) | [ButtonCallbacks](../ui/reference/ButtonCallbacks.md) \| [PlayerCallback](type-aliases.md#playercallback) | `core_behavior/ModSAPI/_ui/core/general/interfaces/controls.pyi` |

## ListViewItems {#listviewitems}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [ListViewItems](type-aliases.md#listviewitems) | [list](type-system.md#list)[[ListViewItem](../ui/reference/ListViewItem.md)] \| [Observable](../ui/reference/Observable.md)[[list](type-system.md#list)[[ListViewItem](../ui/reference/ListViewItem.md)]] | `core_behavior/ModSAPI/_ui/core/general/interfaces/controls.pyi` |

## ListViewValue {#listviewvalue}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [ListViewValue](type-aliases.md#listviewvalue) | [int](type-system.md#int) \| [str](type-system.md#str) \| [None](type-system.md#none) \| [Observable](../ui/reference/Observable.md)[[int](type-system.md#int) \| [str](type-system.md#str) \| [None](type-system.md#none)] \| [Observable](../ui/reference/Observable.md)[[int](type-system.md#int)] \| [Observable](../ui/reference/Observable.md)[[str](type-system.md#str)] | `core_behavior/ModSAPI/_ui/core/general/interfaces/controls.pyi` |

## GroupDefinitions {#groupdefinitions}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [GroupDefinitions](type-aliases.md#groupdefinitions) | [dict](type-system.md#dict)[[str](type-system.md#str), [GroupControlStyle](../ui/reference/GroupControlStyle.md)] | `core_behavior/ModSAPI/_ui/core/general/interfaces/controls.pyi` |

## GroupChildren {#groupchildren}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [GroupChildren](type-aliases.md#groupchildren) | [dict](type-system.md#dict)[[str](type-system.md#str), [GroupChildData](../ui/reference/GroupChildData.md)] | `core_behavior/ModSAPI/_ui/core/general/interfaces/controls.pyi` |

## FormTheme {#formtheme}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [FormTheme](type-aliases.md#formtheme) | [str](type-system.md#str) | `core_behavior/ModSAPI/_ui/core/general/interfaces/form.pyi` |

## GridTracks {#gridtracks}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [GridTracks](type-aliases.md#gridtracks) | [int](type-system.md#int) \| [list](type-system.md#list)[[int](type-system.md#int) \| [float](type-system.md#float)] \| [tuple](type-system.md#tuple)[[int](type-system.md#int) \| [float](type-system.md#float), ...] | `core_behavior/ModSAPI/_ui/core/general/interfaces/grid.pyi` |

## FormLayout {#formlayout}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [FormLayout](../server_ui/reference/FormLayout.md) | [GridLayout](../ui/reference/GridLayout.md) \| [Literal](type-system.md#literal)[False] | `core_behavior/ModSAPI/_ui/core/general/interfaces/grid.pyi` |

## CreateCallback {#createcallback}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [CreateCallback](type-aliases.md#createcallback) | [Callable](type-system.md#callable)[[[CreateArguments](../ui/reference/CreateArguments.md)], [None](type-system.md#none)] | `core_behavior/ModSAPI/_ui/interfaces/base/controls.pyi` |

## UpdateCallback {#updatecallback}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [UpdateCallback](type-aliases.md#updatecallback) | [Callable](type-system.md#callable)[[[ObservableUpdateArguments](../ui/reference/ObservableUpdateArguments.md)], [None](type-system.md#none)] | `core_behavior/ModSAPI/_ui/interfaces/base/controls.pyi` |

## ControlPaths {#controlpaths}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [ControlPaths](type-aliases.md#controlpaths) | [list](type-system.md#list)[[str](type-system.md#str)] \| [tuple](type-system.md#tuple)[[str](type-system.md#str), ...] | `core_behavior/ModSAPI/_ui/interfaces/base/controls.pyi` |

## LabelPaths {#labelpaths}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [LabelPaths](type-aliases.md#labelpaths) | [str](type-system.md#str) \| [ControlPaths](type-aliases.md#controlpaths) | `core_behavior/ModSAPI/_ui/interfaces/base/controls.pyi` |

## ThemeKind {#themekind}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [ThemeKind](type-aliases.md#themekind) | [Literal](type-system.md#literal)['scrolling_panel', 'button', 'toggle', 'label', 'divider', 'slider', 'textfield', 'dropdown', 'listview'] | `core_behavior/ModSAPI/_ui/interfaces/base/theme.pyi` |

## VectorLike {#vectorlike}

| 名称 | 类型 | 声明来源 |
| --- | --- | --- |
| [VectorLike](type-aliases.md#vectorlike) | [Vector3](../server/extra/vector.md) \| [tuple](type-system.md#tuple)[[float](type-system.md#float), [float](type-system.md#float), [float](type-system.md#float)] \| [dict](type-system.md#dict)[[str](type-system.md#str), [float](type-system.md#float)] | `core_behavior/ModSAPI/modules/client/options.pyi` |