---
title: "DynamicParticle"
sidebar_label: "DynamicParticle"
---

# DynamicParticle

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/DynamicParticle.py`；声明补充了静态类型信息。

表达式驱动的绘图对象，与原生粒子发射器不同。pattern 接受 x、y、z 和三通道颜色，各项可为数值、[ExpressionString](ExpressionString.md) 或字符串。选项包括 mode（line 或 point）、interval（正数，每单位 1/20 秒）、maxAmount（正整数）和 visible（布尔值）。运行时表达式失败会停止更新、清理图形并设置 lastError。

## 获取方式

由 `client.spawnDynamicParticle(...)` 返回。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [isValid](#isValid) | 只读属性 |
| [lastError](#lastError) | 只读属性 |
| [remove](#remove) | 方法 |
| [show](#show) | 方法 |
| [hide](#hide) | 方法 |

## 构造器 {#constructor}

```python
DynamicParticle(pattern: DynamicParticlePattern, location: VectorLike, options: DynamicParticleOptions | None = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `pattern` | [DynamicParticlePattern](DynamicParticlePattern.md) | `必填` | 传给 [DynamicParticle.__init__](DynamicParticle.md#constructor) 的 pattern 参数；结合上方功能说明和下方调用示例使用。 |
| `location` | [VectorLike](../../common/type-aliases.md#vectorlike) | `必填` | 位置向量；常用 (x, y, z)，维度由接收对象或选项确定。 |
| `options` | [DynamicParticleOptions](DynamicParticleOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'color requires three channels'` |
| [ValueError](../../common/type-system.md#valueerror) | `'mode must be line or point'` |
| [ValueError](../../common/type-system.md#valueerror) | `'interval must be positive'` |
| [ValueError](../../common/type-system.md#valueerror) | `'maxAmount must be a positive integer'` |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'AddRepeatedTimer'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `CreateGame`, `AddRepeatedTimer`, `GetLevelId`, `CreateDrawing`。

## isValid {#isValid}

```python
isValid: bool
```

此绘图是否仍接受更新和可见性修改。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isValid
```

## lastError {#lastError}

```python
lastError: Exception | None
```

最近一次异步更新异常；尚未失败时为 [None](../../common/type-system.md#none)。

**访问：** 只读。

**返回类型：** [Exception](../../common/type-system.md#exception) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.lastError
```

## remove {#remove}

```python
remove() -> None
```

停止更新并移除拥有的绘图对象；清理失败时保留句柄以便重试。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `参见本成员的前置条件。` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `CancelTimer`, `Remove`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_remove(instance):
    return instance.remove()
```

## show {#show}

```python
show() -> None
```

显示已保留及后续创建的图形；拒绝操作已移除的绘图。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_show(instance):
    return instance.show()
```

## hide {#hide}

```python
hide() -> None
```

隐藏已保留及后续创建的图形，不暂停表达式计时。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_hide(instance):
    return instance.hide()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 DynamicParticle 对象。
    print(value.isValid)
    print(value.lastError)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)