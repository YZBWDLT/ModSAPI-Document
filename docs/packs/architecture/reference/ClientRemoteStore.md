---
title: "ClientRemoteStore"
sidebar_label: "ClientRemoteStore"
---

# ClientRemoteStore

作用域：架构辅助接口。

源码：`core_behavior/ModSAPI/architect/remoteStore.py`。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

基类：[ClientSubsystem](ClientSubsystem.md).

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [broadcast](Subsystem.md#broadcast) | [Subsystem](Subsystem.md) |
| [canTick](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [createEffectBind](ClientSubsystem.md#createEffectBind) | [ClientSubsystem](ClientSubsystem.md) |
| [createParticle](ClientSubsystem.md#createParticle) | [ClientSubsystem](ClientSubsystem.md) |
| [createSfx](ClientSubsystem.md#createSfx) | [ClientSubsystem](ClientSubsystem.md) |
| [destroyEntity](ClientSubsystem.md#destroyEntity) | [ClientSubsystem](ClientSubsystem.md) |
| [destroySfx](ClientSubsystem.md#destroySfx) | [ClientSubsystem](ClientSubsystem.md) |
| [engine](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [getEngine](Subsystem.md#getEngine) | [Subsystem](Subsystem.md) |
| [getInstance](Subsystem.md#getInstance) | [Subsystem](Subsystem.md) |
| [getSysName](Subsystem.md#getSysName) | [Subsystem](Subsystem.md) |
| [getSystem](Subsystem.md#getSystem) | [Subsystem](Subsystem.md) |
| [listen](Subsystem.md#listen) | [Subsystem](Subsystem.md) |
| [off](Subsystem.md#off) | [Subsystem](Subsystem.md) |
| [on](Subsystem.md#on) | [Subsystem](Subsystem.md) |
| [onDestroy](Subsystem.md#onDestroy) | [Subsystem](Subsystem.md) |
| [onInit](Subsystem.md#onInit) | [Subsystem](Subsystem.md) |
| [onReady](Subsystem.md#onReady) | [Subsystem](Subsystem.md) |
| [onUpdate](Subsystem.md#onUpdate) | [Subsystem](Subsystem.md) |
| [sendServer](ClientSubsystem.md#sendServer) | [ClientSubsystem](ClientSubsystem.md) |
| [spawnEntity](ClientSubsystem.md#spawnEntity) | [ClientSubsystem](ClientSubsystem.md) |
| [sysName](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [system](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [ticks](Subsystem.md#字段与常量) | [Subsystem](Subsystem.md) |
| [unlisten](Subsystem.md#unlisten) | [Subsystem](Subsystem.md) |

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 ClientRemoteStore 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)