---
title: "EntityAttributeComponent"
sidebar_label: "EntityAttributeComponent"
---

# EntityAttributeComponent

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/components/EntityComponents.py`；声明补充了静态类型信息。

通过 AttrType 定位的实时服务端属性，不使用 EntityComponentType。写入保留原生默认值，并在写入前拒绝超出当前原生最大值和 NBT 最小值的参数。默认值、最小值来自原生属性 NBT，最大值直接读取引擎。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[EntityComponent](EntityComponent.md).

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `componentId` | 由运行时值确定 | `''` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [isValid](#isValid) | 只读属性 |
| [currentValue](#currentValue) | 只读属性 |
| [defaultValue](#defaultValue) | 只读属性 |
| [effectiveMax](#effectiveMax) | 只读属性 |
| [effectiveMin](#effectiveMin) | 只读属性 |
| [resetToDefaultValue](#resetToDefaultValue) | 方法 |
| [resetToMaxValue](#resetToMaxValue) | 方法 |
| [resetToMinValue](#resetToMinValue) | 方法 |
| [setCurrentValue](#setCurrentValue) | 方法 |
| [setMaxValue](#setMaxValue) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [entity](EntityComponent.md#entity) | [EntityComponent](EntityComponent.md) |
| [typeId](Component.md#typeId) | [Component](Component.md) |

## 构造器 {#constructor}

```python
EntityAttributeComponent(data)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | 由值/所属选项确定 | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md) | `'Native attribute unavailable: ' + attrName` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetMinecraftEnum`。

## isValid {#isValid}

```python
isValid: bool
```

所属实体是否存活且原生属性仍然存在。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetAttrValue`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## currentValue {#currentValue}

```python
currentValue: float
```

读取有限的原生当前值；不能继续使用失效组件。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.currentValue
```

## defaultValue {#defaultValue}

```python
defaultValue: float
```

从属性 NBT 的 Base 读取当前原生定义的默认值。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.defaultValue
```

## effectiveMax {#effectiveMax}

```python
effectiveMax: float
```

读取运行时原生最大值；正无穷是合法的无上限结果。

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.effectiveMax
```

## effectiveMin {#effectiveMin}

```python
effectiveMin: float
```

读取原生 NBT 最小值；没有单独的有效最小值查询接口。

:::note 当前实现说明
目前读取原生属性 NBT 的 Min；没有单独的原生有效最小值查询接口，额外最小值修饰因素尚未完成等价核验。不要将此字段视为已经证明所有环境因素均与微软运行时一致。
:::

**访问：** 只读。

**返回类型：** [float](../../common/type-system.md#float)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.effectiveMin
```

## resetToDefaultValue {#resetToDefaultValue}

```python
resetToDefaultValue() -> None
```

使用原生默认值重置操作，原生失败会报告错误。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `ResetToDefaultValue`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_resetToDefaultValue(instance):
    return instance.resetToDefaultValue()
```

## resetToMaxValue {#resetToMaxValue}

```python
resetToMaxValue() -> None
```

使用原生最大值重置操作。对于从未显式设置过的无穷上限，SDK 恢复默认值，不直接写入正无穷。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `ResetToMaxValue`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_resetToMaxValue(instance):
    return instance.resetToMaxValue()
```

## resetToMinValue {#resetToMinValue}

```python
resetToMinValue() -> None
```

恢复到定义的有限最小值，不改变默认值。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md) | `'Cannot reset an unbounded native minimum'` |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetEntityNBTTags'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetAttrValue`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_resetToMinValue(instance):
    return instance.resetToMinValue()
```

## setCurrentValue {#setCurrentValue}

```python
setCurrentValue(value: float) -> bool
```

在当前上下限内设置有限数值并保留默认值。超界在写入前抛出 [ArgumentOutOfBoundsError](../../common/reference/ArgumentOutOfBoundsError.md)；原生正常拒绝返回 False，畸形结果码及引擎异常抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)。

:::note 当前实现说明
先校验有限数值及当前原生最大值、NBT 最小值，再以保留默认值的方式写入。超界抛出 [ArgumentOutOfBoundsError](../../common/reference/ArgumentOutOfBoundsError.md)，原生正常拒绝返回 False；其他错误保留诊断信息。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `value` | [float](../../common/type-system.md#float) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetEntityNBTTags'` |
| [ArgumentOutOfBoundsError](../../common/reference/ArgumentOutOfBoundsError.md) | `'Attribute value is outside [%r, %r]' % (minimum, maximum)` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetAttrValue`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setCurrentValue(instance, value):
    return instance.setCurrentValue(value)
```

## setMaxValue {#setMaxValue}

```python
setMaxValue(value: float) -> bool
```

设置有限的原生最大值，不改变该属性的默认值。此网易扩展不会扩大原版引擎范围。原生正常拒绝返回 False，原生异常保留诊断信息。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `value` | [float](../../common/type-system.md#float) | `必填` | 需要写入的值，类型、范围及副本语义见本成员说明。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ArgumentOutOfBoundsError](../../common/reference/ArgumentOutOfBoundsError.md) | `'Maximum cannot be smaller than the native minimum'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetAttrMaxValue`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setMaxValue(instance, value):
    return instance.setMaxValue(value)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EntityAttributeComponent 对象。
    print(value.isValid)
    print(value.currentValue)
    print(value.defaultValue)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)