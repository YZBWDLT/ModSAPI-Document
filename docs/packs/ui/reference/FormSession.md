---
title: "FormSession"
sidebar_label: "FormSession"
---

# FormSession

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/core/general/form.py`；声明补充了静态类型信息。

本次显示的表单会话；目标玩家关闭或离线时释放相应监听。

## 获取方式

由 [Form.show](Form.md#show) 返回，使用 onClose 设置关闭回调。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [onClose](#onClose) | 方法 |

## onClose {#onClose}

```python
onClose(callback: Callable[[FormCloseEvent], None] | None) -> FormSession
```

设置关闭回调，每个显示目标关闭时接收一次玩家包装对象。玩家离线只清理目标和监听，不触发关闭回调；返回当前会话以便继续调用。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../../common/type-system.md#callable)[[[FormCloseEvent](FormCloseEvent.md)], [None](../../common/type-system.md#none)] \| [None](../../common/type-system.md#none) | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回类型：** [FormSession](FormSession.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'onClose must be callable or None'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_onClose(instance, callback):
    return instance.onClose(callback)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 FormSession 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)