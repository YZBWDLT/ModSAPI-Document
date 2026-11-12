---
title: "ClientInputOverride"
sidebar_label: "ClientInputOverride"
---

# ClientInputOverride

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Input.py`；声明补充了静态类型信息。

持有独立所有权的权限覆盖层；所属界面关闭时应释放。重叠通道由较晚创建的层优先控制。原生释放失败后可重试，不会释放其他层持有的权限。

## 获取方式

通过 client.input.overridePermissions(...) 取得；流程结束时调用 dispose()，失败后可以重试。不要手动构造。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [permissions](#permissions) | 只读属性 |
| [isDisposed](#isDisposed) | 只读属性 |
| [dispose](#dispose) | 方法 |

## permissions {#permissions}

```python
permissions: dict[str, bool]
```

本覆盖层所请求权限值的独立快照。

**访问：** 只读。

**返回类型：** [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [bool](../../common/type-system.md#bool)]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.permissions
```

## isDisposed {#isDisposed}

```python
isDisposed: bool
```

本句柄持有的全部通道是否均已成功释放。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isDisposed
```

## dispose {#dispose}

```python
dispose() -> None
```

尝试释放全部通道，报告遇到的第一个错误，保留尚未完成的部分供重试。

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_dispose(instance):
    return instance.dispose()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientInputOverride 对象。
    print(value.permissions)
    print(value.isDisposed)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)