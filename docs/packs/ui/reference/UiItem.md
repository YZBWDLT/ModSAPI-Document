---
title: "UiItem"
sidebar_label: "UiItem"
---

# UiItem

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/widgets.py`；声明补充了静态类型信息。

只读的物品显示值，与背包和堆叠数量无关。特殊物品可通过 userData 提供渲染数据；原生预览读取接口不返回这部分数据，因此不能从现有控件恢复。此值不导入或查询服务端组件。

## 获取方式

从 ModSAPI.ui 导入并构造，或通过 [UiItemRenderer.item](UiItemRenderer.md#item) 读取。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [typeId](#typeId) | 只读属性 |
| [auxValue](#auxValue) | 只读属性 |
| [isEnchanted](#isEnchanted) | 只读属性 |
| [userData](#userData) | 只读属性 |

## 构造器 {#constructor}

```python
UiItem(typeId: str, options: UiItemOptions | None = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `typeId` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的实体、物品或资源类型名称。 |
| `options` | [UiItemOptions](UiItemOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'userData must be a dictionary'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## typeId {#typeId}

```python
typeId: str
```

此预览显示的物品类型标识。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.typeId
```

## auxValue {#auxValue}

```python
auxValue: int
```

原生附加值，与方块状态排列分别使用。

**访问：** 只读。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.auxValue
```

## isEnchanted {#isEnchanted}

```python
isEnchanted: bool
```

物品预览是否显示附魔光效。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isEnchanted
```

## userData {#userData}

```python
userData: dict[str, Any] | None
```

可选渲染数据的独立字典副本。

**访问：** 只读。

**返回类型：** [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)] \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.userData
```

## 使用示例


```python
from ModSAPI.ui import UiItem

preview = UiItem("minecraft:diamond", {"isEnchanted": True})
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)