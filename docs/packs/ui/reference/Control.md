---
title: "Control"
sidebar_label: "Control"
---

# Control

作用域：界面、控件和两端组合表单。

源码：`core_behavior/ModSAPI/_ui/interfaces/base/control.py`；声明补充了静态类型信息。

这是界面模板描述或登记入口，通过 ModSAPI.ui 获取。控件登记需要相应描述对象，不能用普通字典替代。

通过统一入口登记具有明确类型的控件描述。

## 获取方式

从 ModSAPI.ui 导入，通过静态方法 register 登记模板描述。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [register](#register) | 静态/类方法 |

## register {#register}

```python
register(identifier: str, controlPath: str, control: ControlDescriptor) -> None
```

登记描述对象和资源模板，原生回调只在客户端使用。登记时复制实例配置；非法登记在发送消息和修改管理器之前报错，不接受仅类名相同的伪造描述对象。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `identifier` | [str](../../common/type-system.md#str) | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `controlPath` | [str](../../common/type-system.md#str) | `必填` | 传给 [Control.register](Control.md#register) 的 controlPath 参数；结合上方功能说明和下方调用示例使用。 |
| `control` | [ControlDescriptor](ControlDescriptor.md) | `必填` | 传给 [Control.register](Control.md#register) 的 control 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'control must be a supported UI control descriptor'` |
| [TypeError](../../common/type-system.md#typeerror) | `key + ' must be callable or None'` |
| [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md) | `key + ' is available on the client only'` |
| [TypeError](../../common/type-system.md#typeerror) | `key + ' must contain UI paths'` |
| [TypeError](../../common/type-system.md#typeerror) | `key + ' must be a UI path'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_register(type_object, identifier, controlPath, control):
    return type_object.register(identifier, controlPath, control)
```

## 使用示例


```python
from ModSAPI.ui import Control, TextField

Control.register("demo:input", "demo_ui.input", TextField(textFieldPath="/input"))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)