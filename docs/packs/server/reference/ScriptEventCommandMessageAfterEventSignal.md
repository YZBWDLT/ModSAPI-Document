---
title: "ScriptEventCommandMessageAfterEventSignal"
sidebar_label: "ScriptEventCommandMessageAfterEventSignal"
---

# ScriptEventCommandMessageAfterEventSignal

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/events/signals/WorldEventSignals.py`；声明补充了静态类型信息。

通过 [GlobalCommandServerEvent](../native-events.md#globalcommandserverevent) 观察完整的 scriptevent 指令字符串，解析标识和消息，不依赖自定义命令的参数数组。回调在原生指令执行前同步触发，不保证引擎执行成功；已取消的指令会被忽略。

## 获取方式

从 [system.afterEvents.scriptEventReceive](SystemAfterEvents.md#scriptEventReceive) 获取信号；使用 subscribe 订阅，用 unsubscribe 注销。

所属信号：[system.afterEvents.scriptEventReceive](SystemAfterEvents.md#scriptEventReceive).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [subscribe](#subscribe) | 方法 |

## 构造器 {#constructor}

```python
ScriptEventCommandMessageAfterEventSignal()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## subscribe {#subscribe}

```python
subscribe(callback: Callable[[ScriptEventCommandMessageAfterEvent], None], options: Optional[Dict[str, Any]] = None) -> Callable[[ScriptEventCommandMessageAfterEvent], None]
```

订阅回调，可传入命名空间筛选条件；注册前复制选项。回调或选项类型不合法时抛出 [TypeError](../../common/type-system.md#typeerror)，未知选项或不合法的命名空间值抛出 [ValueError](../../common/type-system.md#valueerror)，均在注册前校验。省略或传入空命名空间列表时，接收全部有效标识。

:::note 当前实现说明
仅监听 [GlobalCommandServerEvent](../native-events.md#globalcommandserverevent)，不依赖自定义命令注册或参数数组。格式错误或已取消的指令会被忽略；不会改写原生指令和取消标志。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `callback` | [Callable](../../common/type-system.md#callable)[[[ScriptEventCommandMessageAfterEvent](ScriptEventCommandMessageAfterEvent.md)], [None](../../common/type-system.md#none)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |
| `options` | [Optional](../../common/type-system.md#optional)[[Dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [Any](../../common/type-system.md#any)]] | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [Callable](../../common/type-system.md#callable)[[[ScriptEventCommandMessageAfterEvent](ScriptEventCommandMessageAfterEvent.md)], [None](../../common/type-system.md#none)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'options must be a dictionary or ScriptEventMessageFilterOptions'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown script event filter option'` |
| [TypeError](../../common/type-system.md#typeerror) | `'namespaces must be a list or tuple'` |
| [TypeError](../../common/type-system.md#typeerror) | `'namespaces must contain strings'` |
| [ValueError](../../common/type-system.md#valueerror) | `'namespaces must contain nonempty namespace names'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_subscribe(instance, callback):
    return instance.subscribe(callback)
```

## 使用示例


```python
from ModSAPI.server.beta import system

def on_event(event):
    print(event)

system.afterEvents.scriptEventReceive.subscribe(on_event)

def cleanup():
    system.afterEvents.scriptEventReceive.unsubscribe(on_event)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)