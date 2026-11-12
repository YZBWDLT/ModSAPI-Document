---
title: "Theme"
sidebar_label: "Theme"
---

# Theme

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/interfaces/base/theme.py`；声明补充了静态类型信息。

这是界面模板描述或登记入口，通过 ModSAPI.ui 获取。控件登记需要相应描述对象，不能用普通字典替代。

在创建表单的一端登记静态主题样式。

## 获取方式

从 ModSAPI.ui 导入，使用静态方法管理主题。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [register](#register) | 静态/类方法 |
| [get](#get) | 静态/类方法 |
| [names](#names) | 静态/类方法 |
| [unregister](#unregister) | 静态/类方法 |

## register {#register}

```python
register(name: str, styles: dict[ThemeKind, str | dict[str, Any]], base: str | None = 'oreui', replace: bool = False) -> None
```

创建或登记 `register` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../../common/type-system.md#str) | `必填` | 传给 [Theme.register](Theme.md#register) 的 name 参数；结合上方功能说明和下方调用示例使用。 |
| `styles` | [dict](../../common/type-system.md#dict)[[ThemeKind](../../common/type-aliases.md#themekind), [str](../../common/type-system.md#str) \| [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)]] | `必填` | 传给 [Theme.register](Theme.md#register) 的 styles 参数；结合上方功能说明和下方调用示例使用。 |
| `base` | [str](../../common/type-system.md#str) \| [None](../../common/type-system.md#none) | `'oreui'` | 传给 [Theme.register](Theme.md#register) 的 base 参数；结合上方功能说明和下方调用示例使用。 |
| `replace` | [bool](../../common/type-system.md#bool) | `False` | 传给 [Theme.register](Theme.md#register) 的 replace 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_register(type_object, name, styles):
    return type_object.register(name, styles)
```

## get {#get}

```python
get(name: str) -> dict[str, dict[str, Any]]
```

读取 `get` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../../common/type-system.md#str) | `必填` | 传给 [Theme.get](Theme.md#get) 的 name 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)]]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_get(type_object, name):
    return type_object.get(name)
```

## names {#names}

```python
names() -> list[str]
```

执行 `names` 操作。参数形态和结果约定如下。

**返回类型：** [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_names(type_object):
    return type_object.names()
```

## unregister {#unregister}

```python
unregister(name: str) -> None
```

执行 `unregister` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | [str](../../common/type-system.md#str) | `必填` | 传给 [Theme.unregister](Theme.md#unregister) 的 name 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Clear the default theme before unregistering it'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_unregister(type_object, name):
    return type_object.unregister(name)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 Theme 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)