---
title: "CreateArguments"
sidebar_label: "CreateArguments"
---

# CreateArguments

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/core/utils/type.py`；声明补充了静态类型信息。

## 获取方式

通过客户端自定义控件的 onCreate 回调取得。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [screenNode](#screenNode) | 只读属性 |
| [control](#control) | 只读属性 |
| [params](#params) | 只读属性 |
| [style](#style) | 只读属性 |

## screenNode {#screenNode}

```python
screenNode: ScreenNode
```

读取 `screenNode` 的当前值。

**访问：** 只读。

**返回类型：** [ScreenNode](../../common/type-system.md#screennode)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.screenNode
```

## control {#control}

```python
control: BaseUIControl
```

读取 `control` 的当前值。

**访问：** 只读。

**返回类型：** [BaseUIControl](../../common/type-system.md#baseuicontrol)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.control
```

## params {#params}

```python
params: dict[str, Any]
```

当前实例参数的独立副本，绑定状态已经解包为实际值。

**访问：** 只读。

**返回类型：** [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.params
```

## style {#style}

```python
style: dict[str, Any]
```

当前实例样式的独立副本，绑定状态已经解包为实际值。

**访问：** 只读。

**返回类型：** [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.style
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 CreateArguments 对象。
    print(value.screenNode)
    print(value.control)
    print(value.params)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)