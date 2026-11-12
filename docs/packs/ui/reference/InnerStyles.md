---
title: "InnerStyles"
sidebar_label: "InnerStyles"
---

# InnerStyles

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/core/general/controls/innerStyles.py`；声明补充了静态类型信息。

内置 OreUI、Flutter 和 Fluent 风格的模板标识集合。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `oreui` | [Final](../../common/type-system.md#final)[[OreUIStyles](OreUIStyles.md)] | `OreUIStyles()` |
| `flutter` | [Final](../../common/type-system.md#final)[[FlutterStyles](FlutterStyles.md)] | `FlutterStyles()` |
| `fluent` | [Final](../../common/type-system.md#final)[[FluentStyles](FluentStyles.md)] | `FluentStyles()` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 InnerStyles 对象。
    print(value.oreui)
    print(value.flutter)
    print(value.fluent)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)