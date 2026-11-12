---
title: "CustomCommandRegistry"
sidebar_label: "CustomCommandRegistry"
---

# CustomCommandRegistry

作用域：服务端。

源码：`core_behavior/ModSAPI/modules/server/registries/customCommand.py`；声明补充了静态类型信息。

自定义命令注册功能。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [registerCommand](#registerCommand) | 方法 |

## 构造器 {#constructor}

```python
CustomCommandRegistry()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## registerCommand {#registerCommand}

```python
registerCommand(customCommand: CustomCommand, callback: Callable[..., None | CustomCommandResult])
```

绑定命令回调；引擎命令定义与权限需要通过 netease_commands 配置文件提供。

:::note 当前实现说明
只绑定脚本回调；命令声明、参数和权限还需要网易 netease_commands JSON。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `customCommand` | [CustomCommand](../../common/reference/CustomCommand.md) | `必填` | 传给 [CustomCommandRegistry.registerCommand](CustomCommandRegistry.md#registerCommand) 的 customCommand 参数；结合上方功能说明和下方调用示例使用。 |
| `callback` | [Callable](../../common/type-system.md#callable)[..., [None](../../common/type-system.md#none) \| [CustomCommandResult](../../common/reference/CustomCommandResult.md)] | `必填` | 回调函数；保存引用以便注销，回调参数见所属事件或操作的说明。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'A command requires a name and a callable callback'` |
| [ValueError](../../common/type-system.md#valueerror) | `'Command is already registered: %s' % name` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetSystem`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_registerCommand(instance, customCommand, callback):
    return instance.registerCommand(customCommand, callback)
```

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 CustomCommandRegistry 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)