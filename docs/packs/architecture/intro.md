---
sidebar_position: 1
title: 架构辅助接口
---

# 架构辅助接口

[场景与完整示例](../examples.md) · [支持情况与差异](../compatibility.md)

<div className="modsapi-table-scroll" tabIndex={0} aria-label="接口表格，可横向滚动">

| 类型 | 说明 |
| --- | --- |
| [AnnotationHelper](reference/AnnotationHelper.md) | 签名、字段、属性、方法与调用示例 |
| [BaseCompClient](reference/BaseCompClient.md) | 签名、字段、属性、方法与调用示例 |
| [BaseCompServer](reference/BaseCompServer.md) | 签名、字段、属性、方法与调用示例 |
| [ChainedEvent](reference/ChainedEvent.md) | 签名、字段、属性、方法与调用示例 |
| [ClientKVDatabase](reference/ClientKVDatabase.md) | 签名、字段、属性、方法与调用示例 |
| [ClientRemoteStore](reference/ClientRemoteStore.md) | 签名、字段、属性、方法与调用示例 |
| [ClientSubsystem](reference/ClientSubsystem.md) | 签名、字段、属性、方法与调用示例 |
| [DatabaseArrayView](reference/DatabaseArrayView.md) | 列表视图：读取时返回副本，写入时读取最新数据，并支持负数索引。 |
| [DatabaseView](reference/DatabaseView.md) | 字典视图，保留其他视图实例已写入的修改。cache 是独立快照；为兼容原有行为，get 在键缺失或值为 [None](../common/type-system.md#none) 时会保存默认值。读取嵌套值时返回副本。批量回调修改独立的工作字典，仅在成功后保存一次。 |
| [DBSource](reference/DBSource.md) | 签名、字段、属性、方法与调用示例 |
| [Delegate](reference/Delegate.md) | 签名、字段、属性、方法与调用示例 |
| [EventChain](reference/EventChain.md) | 签名、字段、属性、方法与调用示例 |
| [EventSignal](reference/EventSignal.md) | 签名、字段、属性、方法与调用示例 |
| [EventTarget](reference/EventTarget.md) | 签名、字段、属性、方法与调用示例 |
| [Fsm](reference/Fsm.md) | 签名、字段、属性、方法与调用示例 |
| [Future](reference/Future.md) | 签名、字段、属性、方法与调用示例 |
| [LevelClient](reference/LevelClient.md) | 签名、字段、属性、方法与调用示例 |
| [LevelServer](reference/LevelServer.md) | 签名、字段、属性、方法与调用示例 |
| [Location](reference/Location.md) | 签名、字段、属性、方法与调用示例 |
| [ManagedStorage](reference/ManagedStorage.md) | 签名、字段、属性、方法与调用示例 |
| [MinecraftClientEvents](reference/MinecraftClientEvents.md) | 签名、字段、属性、方法与调用示例 |
| [MinecraftServerEvents](reference/MinecraftServerEvents.md) | 签名、字段、属性、方法与调用示例 |
| [QueryCache](reference/QueryCache.md) | 签名、字段、属性、方法与调用示例 |
| [QueryClient](reference/QueryClient.md) | 签名、字段、属性、方法与调用示例 |
| [QueryServer](reference/QueryServer.md) | 签名、字段、属性、方法与调用示例 |
| [Ref](reference/Ref.md) | 签名、字段、属性、方法与调用示例 |
| [Scheduler](reference/Scheduler.md) | 签名、字段、属性、方法与调用示例 |
| [ServerKVDatabase](reference/ServerKVDatabase.md) | 签名、字段、属性、方法与调用示例 |
| [ServerSubsystem](reference/ServerSubsystem.md) | 签名、字段、属性、方法与调用示例 |
| [State](reference/State.md) | 签名、字段、属性、方法与调用示例 |
| [Subsystem](reference/Subsystem.md) | 签名、字段、属性、方法与调用示例 |
| [SubsystemManager](reference/SubsystemManager.md) | 签名、字段、属性、方法与调用示例 |
| [SuspendableTask](reference/SuspendableTask.md) | 签名、字段、属性、方法与调用示例 |
| [Task](reference/Task.md) | 签名、字段、属性、方法与调用示例 |
| [UiSubsystem](reference/UiSubsystem.md) | 签名、字段、属性、方法与调用示例 |
| [Unreliable](reference/Unreliable.md) | 签名、字段、属性、方法与调用示例 |

</div>


## 模块函数

- [architect.basic](functions/architect-basic.md)
- [architect.component.index](functions/architect-component-index.md)
- [architect.event.client](functions/architect-event-client.md)
- [architect.event.server](functions/architect-event-server.md)
- [architect.math.double](functions/architect-math-double.md)
- [architect.math.mat4](functions/architect-math-mat4.md)
- [architect.math.utils](functions/architect-math-utils.md)
- [architect.math.utilsServer](functions/architect-math-utilsServer.md)
- [architect.math.vec3](functions/architect-math-vec3.md)
- [architect.profiler](functions/architect-profiler.md)
- [architect.query.cache](functions/architect-query-cache.md)
- [architect.query.queryClient](functions/architect-query-queryClient.md)
- [architect.query.queryServer](functions/architect-query-queryServer.md)
- [architect.subsystem](functions/architect-subsystem.md)
- [architect.utils.server](functions/architect-utils-server.md)