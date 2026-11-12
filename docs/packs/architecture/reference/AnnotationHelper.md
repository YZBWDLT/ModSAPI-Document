---
title: "AnnotationHelper"
sidebar_label: "AnnotationHelper"
---

# AnnotationHelper

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/annotation.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [addAnnotation](#addAnnotation) | 静态/类方法 |
| [getAnnotation](#getAnnotation) | 静态/类方法 |
| [findAnnotatedMethods](#findAnnotatedMethods) | 静态/类方法 |
| [findAnnotatedClasses](#findAnnotatedClasses) | 静态/类方法 |
| [findAnnotatedAttributes](#findAnnotatedAttributes) | 静态/类方法 |

## addAnnotation {#addAnnotation}

```python
addAnnotation(target, key, value)
```

创建或登记 `addAnnotation` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `target` | 由值/所属选项确定 | `必填` | 传给 [AnnotationHelper.addAnnotation](AnnotationHelper.md#addAnnotation) 的 target 参数；结合上方功能说明和下方调用示例使用。 |
| `key` | 由值/所属选项确定 | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |
| `value` | 由值/所属选项确定 | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_addAnnotation(type_object, target, key, value):
    return type_object.addAnnotation(target, key, value)
```

## getAnnotation {#getAnnotation}

```python
getAnnotation(target, key)
```

读取 `getAnnotation` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `target` | 由值/所属选项确定 | `必填` | 传给 [AnnotationHelper.getAnnotation](AnnotationHelper.md#getAnnotation) 的 target 参数；结合上方功能说明和下方调用示例使用。 |
| `key` | 由值/所属选项确定 | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getAnnotation(type_object, target, key):
    return type_object.getAnnotation(target, key)
```

## findAnnotatedMethods {#findAnnotatedMethods}

```python
findAnnotatedMethods(target, key)
```

执行 `findAnnotatedMethods` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `target` | 由值/所属选项确定 | `必填` | 传给 [AnnotationHelper.findAnnotatedMethods](AnnotationHelper.md#findAnnotatedMethods) 的 target 参数；结合上方功能说明和下方调用示例使用。 |
| `key` | 由值/所属选项确定 | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_findAnnotatedMethods(type_object, target, key):
    return type_object.findAnnotatedMethods(target, key)
```

## findAnnotatedClasses {#findAnnotatedClasses}

```python
findAnnotatedClasses(target, key)
```

执行 `findAnnotatedClasses` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `target` | 由值/所属选项确定 | `必填` | 传给 [AnnotationHelper.findAnnotatedClasses](AnnotationHelper.md#findAnnotatedClasses) 的 target 参数；结合上方功能说明和下方调用示例使用。 |
| `key` | 由值/所属选项确定 | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_findAnnotatedClasses(type_object, target, key):
    return type_object.findAnnotatedClasses(target, key)
```

## findAnnotatedAttributes {#findAnnotatedAttributes}

```python
findAnnotatedAttributes(target, key)
```

执行 `findAnnotatedAttributes` 操作。参数形态和结果约定如下。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `target` | 由值/所属选项确定 | `必填` | 传给 [AnnotationHelper.findAnnotatedAttributes](AnnotationHelper.md#findAnnotatedAttributes) 的 target 参数；结合上方功能说明和下方调用示例使用。 |
| `key` | 由值/所属选项确定 | `必填` | 当前命名空间中的键名；存储接口要求非空字符串。 |

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_findAnnotatedAttributes(type_object, target, key):
    return type_object.findAnnotatedAttributes(target, key)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 AnnotationHelper 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)