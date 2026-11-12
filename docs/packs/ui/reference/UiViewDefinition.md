---
title: "UiViewDefinition"
sidebar_label: "UiViewDefinition"
---

# UiViewDefinition

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/ui/views.py`；声明补充了静态类型信息。

一个界面注册标识及其资源模板和生命周期回调配置。

## 获取方式

由 [client.ui.registerView](UiService.md#registerView) 返回，无需自行构造。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [identifier](#identifier) | 只读属性 |
| [template](#template) | 只读属性 |

## identifier {#identifier}

```python
identifier: str
```

读取 `identifier` 的当前值。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.identifier
```

## template {#template}

```python
template: str
```

读取 `template` 的当前值。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.template
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 UiViewDefinition 对象。
    print(value.identifier)
    print(value.template)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)