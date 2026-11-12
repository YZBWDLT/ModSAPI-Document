---
sidebar_position: 5
title: ModSDK 功能映射与待补接口
---

# ModSDK 功能映射与待补接口

本页按网易官方接口索引逐项保留执行端、原生文档和当前适配记录。原生列表共 1629 条执行端绑定；同名接口在不同类别或两端出现时分别计算。

**目前不能确认本库已覆盖绝大多数 ModSDK 功能。** 名称匹配只用于定位候选调用；已有离线核验路径也只证明列出的功能子集，不表示支持原生接口的全部参数、平台或游戏时序。

| 当前记录 | 数量 | 含义 |
| --- | --- | --- |
| 已有离线核验路径 | 285 | 已核对公开入口并有具体契约测试；仍需游戏验证。 |
| 发现原生调用，待核对 | 270 | 源码出现了相同原生调用名，不能据此判断功能覆盖。 |
| 尚未建立映射 | 1074 | 尚未建立可追溯记录；不能直接解释为原生能力不存在或无法封装。 |

常用界面流程见 [界面、控件与生命周期](guides/managed-ui.md)、[主题表单](guides/themed-forms.md)、[选择控件与小地图](guides/ui-choices-and-minimap.md) 和 [模型预览与图片适配](guides/ui-models-and-images.md)。模型高级挂接、专有渲染和平台能力仍有大量接口待适配。使用 native 访问原生对象，不会自动使这些能力成为本库已实现的接口。

微软接口的对照与已知限制另见 [官方对照与当前支持情况](compatibility.md)。以下列表中的 Apollo 标记保留原文的服务端平台限制。

[网易官方接口索引](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/Api%E7%B4%A2%E5%BC%95%E8%A1%A8.md)

## 物理

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddBoxGeometry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#addboxgeometry) | 服务端 | 尚未建立映射 | — |
| [AddBoxTrigger](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#addboxtrigger) | 服务端 | 尚未建立映射 | — |
| [AddCapsuleGeometry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#addcapsulegeometry) | 服务端 | 尚未建立映射 | — |
| [AddForce](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#addforce) | 服务端 | 尚未建立映射 | — |
| [AddForceAtPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#addforceatpos) | 服务端 | 尚未建立映射 | — |
| [AddForceAtPosLocal](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#addforceatposlocal) | 服务端 | 尚未建立映射 | — |
| [AddSphereGeometry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#addspheregeometry) | 服务端 | 尚未建立映射 | — |
| [CreatePxActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#createpxactor) | 服务端 | 尚未建立映射 | — |
| [GetQuaternion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#getquaternion) | 服务端 | 尚未建立映射 | — |
| [GetQuaternion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#getquaternion) | 客户端 | 尚未建立映射 | — |
| [Raycast](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#raycast) | 服务端 | 尚未建立映射 | — |
| [Raycast](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#raycast) | 客户端 | 尚未建立映射 | — |
| [SetActorFlag](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#setactorflag) | 服务端 | 尚未建立映射 | — |
| [SetGlobalPose](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#setglobalpose) | 服务端 | 尚未建立映射 | — |
| [SetKinematicTarget](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#setkinematictarget) | 服务端 | 尚未建立映射 | — |
| [SetRigidBodyFlag](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#setrigidbodyflag) | 服务端 | 尚未建立映射 | — |
| [SetRigidDynamicLockFlags](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E7%90%86.md#setrigiddynamiclockflags) | 服务端 | 尚未建立映射 | — |

</div>

## 通用 / Component

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CreateComponent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/Component.md#createcomponent) | 服务端 | 发现原生调用，待核对 | — |
| [CreateComponent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/Component.md#createcomponent) | 客户端 | 发现原生调用，待核对 | — |
| [DestroyComponent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/Component.md#destroycomponent) | 服务端 | 发现原生调用，待核对 | — |
| [DestroyComponent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/Component.md#destroycomponent) | 客户端 | 发现原生调用，待核对 | — |
| [GetComponent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/Component.md#getcomponent) | 服务端 | 尚未建立映射 | — |
| [GetComponent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/Component.md#getcomponent) | 客户端 | 尚未建立映射 | — |
| [GetComponentCls](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/Component.md#getcomponentcls) | 服务端 | 发现原生调用，待核对 | — |
| [GetComponentCls](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/Component.md#getcomponentcls) | 客户端 | 发现原生调用，待核对 | — |
| [GetEngineCompFactory](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/Component.md#getenginecompfactory) | 服务端 | 发现原生调用，待核对 | — |
| [GetEngineCompFactory](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/Component.md#getenginecompfactory) | 客户端 | 发现原生调用，待核对 | — |
| [RegisterComponent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/Component.md#registercomponent) | 服务端 | 发现原生调用，待核对 | — |
| [RegisterComponent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/Component.md#registercomponent) | 客户端 | 发现原生调用，待核对 | — |

</div>

## 通用 / System

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetClientSystemCls](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/System.md#getclientsystemcls) | 客户端 | 发现原生调用，待核对 | — |
| [GetServerSystemCls](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/System.md#getserversystemcls) | 服务端 | 发现原生调用，待核对 | — |
| [GetSystem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/System.md#getsystem) | 服务端 | 发现原生调用，待核对 | — |
| [GetSystem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/System.md#getsystem) | 客户端 | 发现原生调用，待核对 | — |
| [RegisterSystem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/System.md#registersystem) | 服务端 | 发现原生调用，待核对 | — |
| [RegisterSystem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/System.md#registersystem) | 客户端 | 发现原生调用，待核对 | — |

</div>

## 通用 / 事件

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [BroadcastEvent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#broadcastevent) | 客户端 | 发现原生调用，待核对 | — |
| [BroadcastEvent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#broadcastevent) | 服务端 | 发现原生调用，待核对 | — |
| [BroadcastToAllClient](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#broadcasttoallclient) | 服务端 | 发现原生调用，待核对 | — |
| [CreateEventData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#createeventdata) | 客户端 | 尚未建立映射 | — |
| [CreateEventData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#createeventdata) | 服务端 | 尚未建立映射 | — |
| [GetEngineNamespace](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#getenginenamespace) | 服务端 | 发现原生调用，待核对 | — |
| [GetEngineNamespace](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#getenginenamespace) | 客户端 | 发现原生调用，待核对 | — |
| [GetEngineSystemName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#getenginesystemname) | 服务端 | 发现原生调用，待核对 | — |
| [GetEngineSystemName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#getenginesystemname) | 客户端 | 发现原生调用，待核对 | — |
| [ListenForEvent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#listenforevent) | 客户端 | 发现原生调用，待核对 | — |
| [ListenForEvent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#listenforevent) | 服务端 | 发现原生调用，待核对 | — |
| [NotifyToClient](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#notifytoclient) | 服务端 | 发现原生调用，待核对 | — |
| [NotifyToMultiClients](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#notifytomulticlients) | 服务端 | 发现原生调用，待核对 | — |
| [NotifyToServer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#notifytoserver) | 客户端 | 发现原生调用，待核对 | — |
| [UnListenAllEvents](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#unlistenallevents) | 客户端 | 尚未建立映射 | — |
| [UnListenAllEvents](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#unlistenallevents) | 服务端 | 尚未建立映射 | — |
| [UnListenForEvent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#unlistenforevent) | 客户端 | 发现原生调用，待核对 | — |
| [UnListenForEvent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E4%BA%8B%E4%BB%B6.md#unlistenforevent) | 服务端 | 发现原生调用，待核对 | — |

</div>

## 通用 / 本地设备

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetEngineVersion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%9C%AC%E5%9C%B0%E8%AE%BE%E5%A4%87.md#getengineversion) | 客户端 | 尚未建立映射 | — |
| [GetIP](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%9C%AC%E5%9C%B0%E8%AE%BE%E5%A4%87.md#getip) | 客户端 | 尚未建立映射 | — |
| [GetMinecraftVersion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%9C%AC%E5%9C%B0%E8%AE%BE%E5%A4%87.md#getminecraftversion) | 服务端 | 尚未建立映射 | — |
| [GetMinecraftVersion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%9C%AC%E5%9C%B0%E8%AE%BE%E5%A4%87.md#getminecraftversion) | 客户端 | 尚未建立映射 | — |
| [GetPlatform](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%9C%AC%E5%9C%B0%E8%AE%BE%E5%A4%87.md#getplatform) | 服务端 | 尚未建立映射 | — |
| [GetPlatform](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%9C%AC%E5%9C%B0%E8%AE%BE%E5%A4%87.md#getplatform) | 客户端 | 尚未建立映射 | — |
| [IsInApollo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%9C%AC%E5%9C%B0%E8%AE%BE%E5%A4%87.md#isinapollo) | 服务端 | 尚未建立映射 | — |
| [IsInServer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%9C%AC%E5%9C%B0%E8%AE%BE%E5%A4%87.md#isinserver) | 服务端 | 尚未建立映射 | — |

</div>

## 通用 / 本地存储

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetConfigData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%9C%AC%E5%9C%B0%E5%AD%98%E5%82%A8.md#getconfigdata) | 客户端 | 已有离线核验路径 | [Client.getStorage](client/apis/manager.md#getStorage), [KeyValueStorage](common/reference/KeyValueStorage.md) |
| [SetConfigData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%9C%AC%E5%9C%B0%E5%AD%98%E5%82%A8.md#setconfigdata) | 客户端 | 已有离线核验路径 | [Client.getStorage](client/apis/manager.md#getStorage), [KeyValueStorage](common/reference/KeyValueStorage.md) |

</div>

## 通用 / 数学

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetDirFromRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%95%B0%E5%AD%A6.md#getdirfromrot) | 服务端 | 发现原生调用，待核对 | — |
| [GetDirFromRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%95%B0%E5%AD%A6.md#getdirfromrot) | 客户端 | 已有离线核验路径 | [ClientEntity.getViewDirection](client/reference/ClientEntity.md#getViewDirection) |
| [GetIntPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%95%B0%E5%AD%A6.md#getintpos) | 服务端 | 尚未建立映射 | — |
| [GetIntPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%95%B0%E5%AD%A6.md#getintpos) | 客户端 | 尚未建立映射 | — |
| [GetLocalPosFromWorld](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%95%B0%E5%AD%A6.md#getlocalposfromworld) | 服务端 | 尚未建立映射 | — |
| [GetLocalPosFromWorld](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%95%B0%E5%AD%A6.md#getlocalposfromworld) | 客户端 | 尚未建立映射 | — |
| [GetRotFromDir](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%95%B0%E5%AD%A6.md#getrotfromdir) | 服务端 | 尚未建立映射 | — |
| [GetRotFromDir](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%95%B0%E5%AD%A6.md#getrotfromdir) | 客户端 | 尚未建立映射 | — |
| [GetWorldPosFromLocal](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%95%B0%E5%AD%A6.md#getworldposfromlocal) | 服务端 | 尚未建立映射 | — |
| [GetWorldPosFromLocal](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E6%95%B0%E5%AD%A6.md#getworldposfromlocal) | 客户端 | 尚未建立映射 | — |

</div>

## 通用 / 工具

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddRepeatedTimer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#addrepeatedtimer) | 服务端 | 发现原生调用，待核对 | — |
| [AddRepeatedTimer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#addrepeatedtimer) | 客户端 | 发现原生调用，待核对 | — |
| [AddTimer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#addtimer) | 服务端 | 发现原生调用，待核对 | — |
| [AddTimer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#addtimer) | 客户端 | 发现原生调用，待核对 | — |
| [CancelTimer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#canceltimer) | 服务端 | 发现原生调用，待核对 | — |
| [CancelTimer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#canceltimer) | 客户端 | 发现原生调用，待核对 | — |
| [CheckNameValid](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#checknamevalid) | 服务端 | 尚未建立映射 | — |
| [CheckNameValid](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#checknamevalid) | 客户端 | 尚未建立映射 | — |
| [CheckWordsValid](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#checkwordsvalid) | 服务端 | 尚未建立映射 | — |
| [CheckWordsValid](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#checkwordsvalid) | 客户端 | 尚未建立映射 | — |
| [GetChinese](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#getchinese) | 服务端 | 尚未建立映射 | — |
| [GetChinese](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#getchinese) | 客户端 | 尚未建立映射 | — |
| [GetClipboardContent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#getclipboardcontent) | 客户端 | 尚未建立映射 | — |
| [GetFps](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#getfps) | 客户端 | 尚未建立映射 | — |
| [GetHostPlayerId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#gethostplayerid) | 服务端 | 尚未建立映射 | — |
| [GetHostPlayerId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#gethostplayerid) | 客户端 | 尚未建立映射 | — |
| [GetMinecraftEnum](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#getminecraftenum) | 服务端 | 发现原生调用，待核对 | — |
| [GetMinecraftEnum](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#getminecraftenum) | 客户端 | 发现原生调用，待核对 | — |
| [GetModConfigJson](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#getmodconfigjson) | 服务端 | 尚未建立映射 | — |
| [GetModConfigJson](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#getmodconfigjson) | 客户端 | 尚未建立映射 | — |
| [GetServerTickTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#getserverticktime) | 服务端 | 发现原生调用，待核对 | — |
| [ImportModule](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#importmodule) | 服务端 | 尚未建立映射 | — |
| [ImportModule](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#importmodule) | 客户端 | 尚未建立映射 | — |
| [SetClipboardContent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#setclipboardcontent) | 客户端 | 尚未建立映射 | — |
| [StartCoroutine](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#startcoroutine) | 服务端 | 尚未建立映射 | — |
| [StartCoroutine](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#startcoroutine) | 客户端 | 尚未建立映射 | — |
| [StopCoroutine](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#stopcoroutine) | 服务端 | 尚未建立映射 | — |
| [StopCoroutine](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E5%B7%A5%E5%85%B7.md#stopcoroutine) | 客户端 | 尚未建立映射 | — |

</div>

## 通用 / 调试

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetEnableReconnectNetgame](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#getenablereconnectnetgame) | 客户端 | 尚未建立映射 | — |
| [GetKeepResourceWhenTransfer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#getkeepresourcewhentransfer) | 客户端 | 尚未建立映射 | — |
| [GetMcpModLogCanPostDump](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#getmcpmodlogcanpostdump) | 服务端 | 尚未建立映射 | — |
| [GetMcpModLogCanPostDump](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#getmcpmodlogcanpostdump) | 客户端 | 尚未建立映射 | — |
| [GetResourceFastload](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#getresourcefastload) | 客户端 | 尚未建立映射 | — |
| [PostMcpModDump](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#postmcpmoddump) | 服务端 | 尚未建立映射 | — |
| [PostMcpModDump](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#postmcpmoddump) | 客户端 | 尚未建立映射 | — |
| [ReloadAllMaterials](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#reloadallmaterials) | 客户端 | 尚未建立映射 | — |
| [ReloadAllShaders](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#reloadallshaders) | 客户端 | 尚未建立映射 | — |
| [ReloadOneShader](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#reloadoneshader) | 客户端 | 尚未建立映射 | — |
| [SetEnableReconnectNetgame](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#setenablereconnectnetgame) | 客户端 | 尚未建立映射 | — |
| [SetKeepResourceWhenTransfer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#setkeepresourcewhentransfer) | 客户端 | 尚未建立映射 | — |
| [SetMcpModLogCanPostDump](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#setmcpmodlogcanpostdump) | 服务端 | 尚未建立映射 | — |
| [SetMcpModLogCanPostDump](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#setmcpmodlogcanpostdump) | 客户端 | 尚未建立映射 | — |
| [SetResourceFastload](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#setresourcefastload) | 客户端 | 尚未建立映射 | — |
| [StartMemProfile](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#startmemprofile) | 服务端 | 尚未建立映射 | — |
| [StartMemProfile](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#startmemprofile) | 客户端 | 尚未建立映射 | — |
| [StartMultiProfile](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#startmultiprofile) | 服务端 | 尚未建立映射 | — |
| [StartMultiProfile](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#startmultiprofile) | 客户端 | 尚未建立映射 | — |
| [StartProfile](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#startprofile) | 服务端 | 尚未建立映射 | — |
| [StartProfile](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#startprofile) | 客户端 | 尚未建立映射 | — |
| [StartRecordEvent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#startrecordevent) | 服务端（Apollo） | 尚未建立映射 | — |
| [StartRecordPacket](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#startrecordpacket) | 服务端（Apollo） | 尚未建立映射 | — |
| [StopMemProfile](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#stopmemprofile) | 服务端 | 尚未建立映射 | — |
| [StopMemProfile](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#stopmemprofile) | 客户端 | 尚未建立映射 | — |
| [StopMultiProfile](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#stopmultiprofile) | 服务端 | 尚未建立映射 | — |
| [StopMultiProfile](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#stopmultiprofile) | 客户端 | 尚未建立映射 | — |
| [StopProfile](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#stopprofile) | 服务端 | 尚未建立映射 | — |
| [StopProfile](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#stopprofile) | 客户端 | 尚未建立映射 | — |
| [StopRecordEvent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#stoprecordevent) | 服务端（Apollo） | 尚未建立映射 | — |
| [StopRecordPacket](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%80%9A%E7%94%A8/%E8%B0%83%E8%AF%95.md#stoprecordpacket) | 服务端（Apollo） | 尚未建立映射 | — |

</div>

## 世界 / 地图

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CanSee](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#cansee) | 服务端 | 尚未建立映射 | — |
| [CanSee](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#cansee) | 客户端 | 尚未建立映射 | — |
| [CheckBlockToPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#checkblocktopos) | 服务端 | 尚未建立映射 | — |
| [CheckChunkState](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#checkchunkstate) | 服务端 | 发现原生调用，待核对 | — |
| [CreateDimension](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#createdimension) | 服务端 | 发现原生调用，待核对 | — |
| [CreateExplosion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#createexplosion) | 服务端 | 发现原生调用，待核对 | — |
| [DeleteAllArea](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#deleteallarea) | 服务端 | 尚未建立映射 | — |
| [DeleteArea](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#deletearea) | 服务端 | 发现原生调用，待核对 | — |
| [DetectStructure](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#detectstructure) | 服务端 | 尚未建立映射 | — |
| [DoTaskOnChunkAsync](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#dotaskonchunkasync) | 服务端 | 发现原生调用，待核对 | — |
| [GetAllAreaKeys](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getallareakeys) | 服务端 | 发现原生调用，待核对 | — |
| [GetBiomeInfo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getbiomeinfo) | 服务端 | 尚未建立映射 | — |
| [GetBiomeName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getbiomename) | 服务端 | 尚未建立映射 | — |
| [GetBiomeName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getbiomename) | 客户端 | 尚未建立映射 | — |
| [GetBlockLightLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getblocklightlevel) | 服务端 | 发现原生调用，待核对 | — |
| [GetChunkEntites](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getchunkentites) | 服务端 | 尚未建立映射 | — |
| [GetChunkMaxPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getchunkmaxpos) | 服务端 | 尚未建立映射 | — |
| [GetChunkMinPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getchunkminpos) | 服务端 | 尚未建立映射 | — |
| [GetChunkMobNum](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getchunkmobnum) | 服务端 | 尚未建立映射 | — |
| [GetChunkPosFromBlockPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getchunkposfromblockpos) | 服务端 | 尚未建立映射 | — |
| [GetChunkPosFromBlockPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getchunkposfromblockpos) | 客户端 | 尚未建立映射 | — |
| [GetCurrentDimension](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getcurrentdimension) | 客户端 | 发现原生调用，待核对 | — |
| [GetEntitiesAround](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getentitiesaround) | 服务端 | 尚未建立映射 | — |
| [GetEntitiesAround](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getentitiesaround) | 客户端 | 尚未建立映射 | — |
| [GetEntitiesAroundByType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getentitiesaroundbytype) | 服务端 | 尚未建立映射 | — |
| [GetEntitiesAroundByType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getentitiesaroundbytype) | 客户端 | 尚未建立映射 | — |
| [GetEntitiesAroundForClientEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getentitiesaroundforcliententity) | 客户端 | 尚未建立映射 | — |
| [GetEntitiesInSquareArea](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getentitiesinsquarearea) | 服务端 | 发现原生调用，待核对 | — |
| [GetEntitiesInSquareArea](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getentitiesinsquarearea) | 客户端 | 发现原生调用，待核对 | — |
| [GetEntitiesInSquareAreaForClientEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getentitiesinsquareareaforcliententity) | 客户端 | 尚未建立映射 | — |
| [GetLevelId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getlevelid) | 服务端 | 发现原生调用，待核对 | — |
| [GetLevelId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getlevelid) | 客户端 | 发现原生调用，待核对 | — |
| [GetLoadedChunks](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getloadedchunks) | 服务端 | 尚未建立映射 | — |
| [GetSpawnDimension](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getspawndimension) | 服务端 | 尚未建立映射 | — |
| [GetSpawnPosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getspawnposition) | 服务端 | 发现原生调用，待核对 | — |
| [GetStructureSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#getstructuresize) | 服务端 | 发现原生调用，待核对 | — |
| [IsChunkGenerated](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#ischunkgenerated) | 服务端 | 尚未建立映射 | — |
| [IsSlimeChunk](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#isslimechunk) | 服务端 | 尚未建立映射 | — |
| [LocateNeteaseFeatureRule](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#locateneteasefeaturerule) | 服务端 | 尚未建立映射 | — |
| [LocateStructureFeature](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#locatestructurefeature) | 服务端 | 尚未建立映射 | — |
| [MayPlace](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#mayplace) | 服务端 | 尚未建立映射 | — |
| [MayPlaceOn](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#mayplaceon) | 服务端 | 尚未建立映射 | — |
| [MirrorDimension](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#mirrordimension) | 服务端 | 尚未建立映射 | — |
| [OpenClientChunkGeneration](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#openclientchunkgeneration) | 服务端 | 尚未建立映射 | — |
| [PlaceFeature](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#placefeature) | 服务端 | 尚未建立映射 | — |
| [PlaceNeteaseLargeFeature](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#placeneteaselargefeature) | 服务端 | 尚未建立映射 | — |
| [PlaceStructure](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#placestructure) | 服务端 | 发现原生调用，待核对 | — |
| [SetAddArea](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#setaddarea) | 服务端 | 发现原生调用，待核对 | — |
| [SetBiomeByPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#setbiomebypos) | 服务端 | 尚未建立映射 | — |
| [SetBiomeByPosList](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#setbiomebyposlist) | 服务端 | 尚未建立映射 | — |
| [SetBiomeByVolume](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#setbiomebyvolume) | 服务端 | 尚未建立映射 | — |
| [SetBiomeInfo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#setbiomeinfo) | 服务端 | 尚未建立映射 | — |
| [SetMergeSpawnItemRadius](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#setmergespawnitemradius) | 服务端 | 尚未建立映射 | — |
| [SetSpawnDimensionAndPosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#setspawndimensionandposition) | 服务端 | 尚未建立映射 | — |
| [UpgradeMapDimensionVersion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%9C%B0%E5%9B%BE.md#upgrademapdimensionversion) | 服务端 | 尚未建立映射 | — |

</div>

## 世界 / 实体管理

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CreateClientEntityByTypeStr](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#createcliententitybytypestr) | 客户端 | 发现原生调用，待核对 | — |
| [CreateEngineEntityByNBT](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#createengineentitybynbt) | 服务端 | 发现原生调用，待核对 | — |
| [CreateEngineEntityByTypeStr](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#createengineentitybytypestr) | 服务端 | 发现原生调用，待核对 | — |
| [CreateEngineItemEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#createengineitementity) | 服务端 | 发现原生调用，待核对 | — |
| [CreateEntityAOI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#createentityaoi) | 服务端 | 尚未建立映射 | — |
| [CreateExperienceOrb](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#createexperienceorb) | 服务端 | 尚未建立映射 | — |
| [CreateProjectileEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#createprojectileentity) | 服务端 | 尚未建立映射 | — |
| [DeleteEntityAOI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#deleteentityaoi) | 服务端 | 尚未建立映射 | — |
| [DestroyClientEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#destroycliententity) | 客户端 | 发现原生调用，待核对 | — |
| [DestroyEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#destroyentity) | 服务端 | 发现原生调用，待核对 | — |
| [GetDroppedItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#getdroppeditem) | 服务端 | 尚未建立映射 | — |
| [GetEngineActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#getengineactor) | 服务端 | 尚未建立映射 | — |
| [GetEngineActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#getengineactor) | 客户端 | 尚未建立映射 | — |
| [GetLocalPlayerId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#getlocalplayerid) | 客户端 | 发现原生调用，待核对 | — |
| [GetLootItems](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#getlootitems) | 服务端 | 尚未建立映射 | — |
| [GetPlayerList](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#getplayerlist) | 服务端 | 发现原生调用，待核对 | — |
| [GetPlayerList](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#getplayerlist) | 客户端 | 发现原生调用，待核对 | — |
| [HasEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#hasentity) | 客户端 | 已有离线核验路径 | [ClientEntity.isValid](client/reference/ClientEntity.md#isValid), [Client.getEntity](client/apis/manager.md#getEntity) |
| [IsEntityAlive](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#isentityalive) | 服务端 | 已有离线核验路径 | [Entity.isValid](server/apis/entity.md#isValid) |
| [IsEntityAlive](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#isentityalive) | 客户端 | 发现原生调用，待核对 | — |
| [KillEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#killentity) | 服务端 | 发现原生调用，待核对 | — |
| [SpawnLootTable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#spawnloottable) | 服务端 | 尚未建立映射 | — |
| [SpawnLootTableWithActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#spawnloottablewithactor) | 服务端 | 尚未建立映射 | — |
| [SpawnResources](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#spawnresources) | 服务端 | 尚未建立映射 | — |
| [SpawnResourcesSilkTouched](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#spawnresourcessilktouched) | 服务端 | 尚未建立映射 | — |
| [getEntitiesOrBlockFromRay](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#getentitiesorblockfromray) | 服务端 | 发现原生调用，待核对 | — |
| [getEntitiesOrBlockFromRay](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%AE%9E%E4%BD%93%E7%AE%A1%E7%90%86.md#getentitiesorblockfromray) | 客户端 | 发现原生调用，待核对 | — |

</div>

## 世界 / 方块管理

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetBlock](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#getblock) | 客户端 | 尚未建立映射 | — |
| [GetBlockClip](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#getblockclip) | 服务端 | 尚未建立映射 | — |
| [GetBlockClip](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#getblockclip) | 客户端 | 尚未建立映射 | — |
| [GetBlockCollision](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#getblockcollision) | 服务端 | 尚未建立映射 | — |
| [GetBlockCollision](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#getblockcollision) | 客户端 | 尚未建立映射 | — |
| [GetBlockNew](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#getblocknew) | 服务端 | 发现原生调用，待核对 | — |
| [GetDestroyTotalTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#getdestroytotaltime) | 服务端 | 尚未建立映射 | — |
| [GetDestroyTotalTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#getdestroytotaltime) | 客户端 | 尚未建立映射 | — |
| [GetLiquidBlock](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#getliquidblock) | 服务端 | 发现原生调用，待核对 | — |
| [GetTopBlockHeight](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#gettopblockheight) | 服务端 | 尚未建立映射 | — |
| [GetTopBlockHeight](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#gettopblockheight) | 客户端 | 尚未建立映射 | — |
| [SetBlockNew](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#setblocknew) | 服务端 | 发现原生调用，待核对 | — |
| [SetJigsawBlock](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#setjigsawblock) | 服务端 | 尚未建立映射 | — |
| [SetLiquidBlock](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#setliquidblock) | 服务端 | 发现原生调用，待核对 | — |
| [SetSnowBlock](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%AE%A1%E7%90%86.md#setsnowblock) | 服务端 | 尚未建立映射 | — |

</div>

## 世界 / 生物生成

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetEntityLimit](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E7%94%9F%E7%89%A9%E7%94%9F%E6%88%90.md#getentitylimit) | 服务端 | 尚未建立映射 | — |
| [SetEntityLimit](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E7%94%9F%E7%89%A9%E7%94%9F%E6%88%90.md#setentitylimit) | 服务端 | 尚未建立映射 | — |
| [SpawnCustomModule](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E7%94%9F%E7%89%A9%E7%94%9F%E6%88%90.md#spawncustommodule) | 服务端 | 尚未建立映射 | — |

</div>

## 世界 / 配方

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddBrewingRecipes](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E9%85%8D%E6%96%B9.md#addbrewingrecipes) | 服务端 | 尚未建立映射 | — |
| [AddRecipe](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E9%85%8D%E6%96%B9.md#addrecipe) | 服务端 | 尚未建立映射 | — |
| [GetRecipeByRecipeId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E9%85%8D%E6%96%B9.md#getrecipebyrecipeid) | 服务端 | 尚未建立映射 | — |
| [GetRecipeByRecipeId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E9%85%8D%E6%96%B9.md#getrecipebyrecipeid) | 客户端 | 尚未建立映射 | — |
| [GetRecipeResult](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E9%85%8D%E6%96%B9.md#getreciperesult) | 服务端 | 尚未建立映射 | — |
| [GetRecipesByInput](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E9%85%8D%E6%96%B9.md#getrecipesbyinput) | 服务端 | 尚未建立映射 | — |
| [GetRecipesByInput](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E9%85%8D%E6%96%B9.md#getrecipesbyinput) | 客户端 | 尚未建立映射 | — |
| [GetRecipesByResult](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E9%85%8D%E6%96%B9.md#getrecipesbyresult) | 服务端 | 尚未建立映射 | — |
| [GetRecipesByResult](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E9%85%8D%E6%96%B9.md#getrecipesbyresult) | 客户端 | 尚未建立映射 | — |
| [RemoveRecipe](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E9%85%8D%E6%96%B9.md#removerecipe) | 服务端 | 尚未建立映射 | — |

</div>

## 世界 / 方块组合

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CreateMicroBlockResStr](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%BB%84%E5%90%88.md#createmicroblockresstr) | 服务端 | 尚未建立映射 | — |
| [GetBlankBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%BB%84%E5%90%88.md#getblankblockpalette) | 服务端 | 发现原生调用，待核对 | — |
| [GetBlankBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%BB%84%E5%90%88.md#getblankblockpalette) | 客户端 | 发现原生调用，待核对 | — |
| [GetBlockPaletteBetweenPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%BB%84%E5%90%88.md#getblockpalettebetweenpos) | 服务端 | 发现原生调用，待核对 | — |
| [GetBlockPaletteBetweenPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%BB%84%E5%90%88.md#getblockpalettebetweenpos) | 客户端 | 发现原生调用，待核对 | — |
| [GetBlockPaletteFromPosList](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%BB%84%E5%90%88.md#getblockpalettefromposlist) | 服务端 | 尚未建立映射 | — |
| [GetBlockPaletteFromPosList](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%BB%84%E5%90%88.md#getblockpalettefromposlist) | 客户端 | 尚未建立映射 | — |
| [RegisterBlockPatterns](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%BB%84%E5%90%88.md#registerblockpatterns) | 服务端 | 尚未建立映射 | — |
| [SetBlockByBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%96%B9%E5%9D%97%E7%BB%84%E5%90%88.md#setblockbyblockpalette) | 服务端 | 发现原生调用，待核对 | — |

</div>

## 世界 / 渲染

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddTerrainDestroyParticleEffect](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#addterraindestroyparticleeffect) | 客户端 | 尚未建立映射 | — |
| [AddUseItemParticleEffect](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#adduseitemparticleeffect) | 客户端 | 尚未建立映射 | — |
| [GetAmbientBrightness](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getambientbrightness) | 客户端 | 尚未建立映射 | — |
| [GetFogColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getfogcolor) | 客户端 | 尚未建立映射 | — |
| [GetFogLength](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getfoglength) | 客户端 | 尚未建立映射 | — |
| [GetMoonRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getmoonrot) | 客户端 | 尚未建立映射 | — |
| [GetSkyColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getskycolor) | 客户端 | 尚未建立映射 | — |
| [GetSkyTextures](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getskytextures) | 客户端 | 尚未建立映射 | — |
| [GetStarBrightness](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getstarbrightness) | 客户端 | 尚未建立映射 | — |
| [GetSunRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getsunrot) | 客户端 | 尚未建立映射 | — |
| [GetUseAmbientBrightness](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getuseambientbrightness) | 客户端 | 尚未建立映射 | — |
| [GetUseFogColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getusefogcolor) | 客户端 | 尚未建立映射 | — |
| [GetUseFogLength](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getusefoglength) | 客户端 | 尚未建立映射 | — |
| [GetUseMoonRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getusemoonrot) | 客户端 | 尚未建立映射 | — |
| [GetUseSkyColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getuseskycolor) | 客户端 | 尚未建立映射 | — |
| [GetUseStarBrightness](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getusestarbrightness) | 客户端 | 尚未建立映射 | — |
| [GetUseSunRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#getusesunrot) | 客户端 | 尚未建立映射 | — |
| [HideNameTag](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#hidenametag) | 客户端 | 尚未建立映射 | — |
| [IsHideNameTag](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#ishidenametag) | 客户端 | 尚未建立映射 | — |
| [RemoveTerrainDestroyParticleEffect](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#removeterraindestroyparticleeffect) | 客户端 | 尚未建立映射 | — |
| [RemoveUseItemParticleEffect](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#removeuseitemparticleeffect) | 客户端 | 尚未建立映射 | — |
| [ResetAmbientBrightness](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#resetambientbrightness) | 客户端 | 尚未建立映射 | — |
| [ResetFogColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#resetfogcolor) | 客户端 | 尚未建立映射 | — |
| [ResetFogLength](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#resetfoglength) | 客户端 | 尚未建立映射 | — |
| [ResetMoonRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#resetmoonrot) | 客户端 | 尚未建立映射 | — |
| [ResetSkyColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#resetskycolor) | 客户端 | 尚未建立映射 | — |
| [ResetSkyTextures](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#resetskytextures) | 客户端 | 尚未建立映射 | — |
| [ResetStarBrightness](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#resetstarbrightness) | 客户端 | 尚未建立映射 | — |
| [ResetSunRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#resetsunrot) | 客户端 | 尚未建立映射 | — |
| [SetAmbientBrightness](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#setambientbrightness) | 客户端 | 尚未建立映射 | — |
| [SetFogColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#setfogcolor) | 客户端 | 尚未建立映射 | — |
| [SetFogLength](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#setfoglength) | 客户端 | 尚未建立映射 | — |
| [SetMoonRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#setmoonrot) | 客户端 | 尚未建立映射 | — |
| [SetSkyColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#setskycolor) | 客户端 | 尚未建立映射 | — |
| [SetSkyTextures](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#setskytextures) | 客户端 | 尚未建立映射 | — |
| [SetStarBrightness](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#setstarbrightness) | 客户端 | 尚未建立映射 | — |
| [SetSunRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#setsunrot) | 客户端 | 尚未建立映射 | — |
| [SkyTextures](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B2%E6%9F%93.md#skytextures) | 客户端 | 尚未建立映射 | — |

</div>

## 世界 / 时间

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetLocalDoDayNightCycle](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%97%B6%E9%97%B4.md#getlocaldodaynightcycle) | 服务端 | 尚未建立映射 | — |
| [GetLocalTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%97%B6%E9%97%B4.md#getlocaltime) | 服务端 | 尚未建立映射 | — |
| [GetLocalTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%97%B6%E9%97%B4.md#getlocaltime) | 客户端 | 尚未建立映射 | — |
| [GetTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%97%B6%E9%97%B4.md#gettime) | 服务端 | 已有离线核验路径 | [World.getAbsoluteTime](server/apis/world.md#getAbsoluteTime), [World.getTimeOfDay](server/apis/world.md#getTimeOfDay), [World.getDay](server/apis/world.md#getDay), [World.getMoonPhase](server/apis/world.md#getMoonPhase) |
| [GetTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%97%B6%E9%97%B4.md#gettime) | 客户端 | 发现原生调用，待核对 | — |
| [GetUseLocalTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%97%B6%E9%97%B4.md#getuselocaltime) | 服务端 | 尚未建立映射 | — |
| [SetLocalDoDayNightCycle](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%97%B6%E9%97%B4.md#setlocaldodaynightcycle) | 服务端 | 尚未建立映射 | — |
| [SetLocalTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%97%B6%E9%97%B4.md#setlocaltime) | 服务端 | 尚未建立映射 | — |
| [SetLocalTimeOfDay](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%97%B6%E9%97%B4.md#setlocaltimeofday) | 服务端 | 尚未建立映射 | — |
| [SetTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%97%B6%E9%97%B4.md#settime) | 服务端 | 已有离线核验路径 | [World.setAbsoluteTime](server/apis/world.md#setAbsoluteTime) |
| [SetTimeOfDay](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%97%B6%E9%97%B4.md#settimeofday) | 服务端 | 已有离线核验路径 | [World.setTimeOfDay](server/apis/world.md#setTimeOfDay) |
| [SetUseLocalTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%97%B6%E9%97%B4.md#setuselocaltime) | 服务端 | 尚未建立映射 | — |

</div>

## 世界 / 天气

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetDimensionLocalWeatherInfo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%A4%A9%E6%B0%94.md#getdimensionlocalweatherinfo) | 服务端 | 尚未建立映射 | — |
| [GetDimensionUseLocalWeather](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%A4%A9%E6%B0%94.md#getdimensionuselocalweather) | 服务端 | 尚未建立映射 | — |
| [IsRaining](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%A4%A9%E6%B0%94.md#israining) | 服务端 | 尚未建立映射 | — |
| [IsThunder](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%A4%A9%E6%B0%94.md#isthunder) | 服务端 | 尚未建立映射 | — |
| [SetDimensionLocalDoWeatherCycle](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%A4%A9%E6%B0%94.md#setdimensionlocaldoweathercycle) | 服务端 | 尚未建立映射 | — |
| [SetDimensionLocalRain](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%A4%A9%E6%B0%94.md#setdimensionlocalrain) | 服务端 | 尚未建立映射 | — |
| [SetDimensionLocalThunder](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%A4%A9%E6%B0%94.md#setdimensionlocalthunder) | 服务端 | 尚未建立映射 | — |
| [SetDimensionUseLocalWeather](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%A4%A9%E6%B0%94.md#setdimensionuselocalweather) | 服务端 | 尚未建立映射 | — |
| [SetRaining](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%A4%A9%E6%B0%94.md#setraining) | 服务端 | 尚未建立映射 | — |
| [SetThunder](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E5%A4%A9%E6%B0%94.md#setthunder) | 服务端 | 尚未建立映射 | — |

</div>

## 世界 / 游戏规则

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddBannedItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#addbanneditem) | 服务端 | 尚未建立映射 | — |
| [AddBlockProtectField](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#addblockprotectfield) | 服务端（Apollo） | 尚未建立映射 | — |
| [CleanBlockProtectField](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#cleanblockprotectfield) | 服务端（Apollo） | 尚未建立映射 | — |
| [ClearBannedItems](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#clearbanneditems) | 服务端 | 尚未建立映射 | — |
| [DisableVineBlockSpread](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#disablevineblockspread) | 服务端 | 尚未建立映射 | — |
| [ForbidLiquidFlow](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#forbidliquidflow) | 服务端 | 尚未建立映射 | — |
| [GetBannedItemList](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#getbanneditemlist) | 服务端 | 尚未建立映射 | — |
| [GetGameDiffculty](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#getgamediffculty) | 服务端 | 发现原生调用，待核对 | — |
| [GetGameRulesInfoServer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#getgamerulesinfoserver) | 服务端 | 发现原生调用，待核对 | — |
| [GetGameType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#getgametype) | 服务端 | 尚未建立映射 | — |
| [GetLevelGravity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#getlevelgravity) | 服务端 | 尚未建立映射 | — |
| [GetPistonMaxInteractionCount](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#getpistonmaxinteractioncount) | 服务端 | 尚未建立映射 | — |
| [GetPistonMaxInteractionCount](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#getpistonmaxinteractioncount) | 客户端 | 尚未建立映射 | — |
| [GetSeed](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#getseed) | 服务端 | 发现原生调用，待核对 | — |
| [IsDisableCommandMinecart](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#isdisablecommandminecart) | 服务端 | 尚未建立映射 | — |
| [IsLockDifficulty](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#islockdifficulty) | 服务端 | 尚未建立映射 | — |
| [IsLockGameRulesInfo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#islockgamerulesinfo) | 服务端 | 尚未建立映射 | — |
| [IsLockGameType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#islockgametype) | 服务端 | 尚未建立映射 | — |
| [LockDifficulty](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#lockdifficulty) | 服务端 | 尚未建立映射 | — |
| [LockGameRulesInfo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#lockgamerulesinfo) | 服务端 | 尚未建立映射 | — |
| [LockGameType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#lockgametype) | 服务端 | 尚未建立映射 | — |
| [OpenCityProtect](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#opencityprotect) | 服务端（Apollo） | 尚未建立映射 | — |
| [RemoveBannedItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#removebanneditem) | 服务端 | 尚未建立映射 | — |
| [RemoveBlockProtectField](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#removeblockprotectfield) | 服务端（Apollo） | 尚未建立映射 | — |
| [SetCanActorSetOnFireByLightning](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#setcanactorsetonfirebylightning) | 服务端 | 尚未建立映射 | — |
| [SetCanBlockSetOnFireByLightning](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#setcanblocksetonfirebylightning) | 服务端 | 尚未建立映射 | — |
| [SetDefaultGameType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#setdefaultgametype) | 服务端 | 尚未建立映射 | — |
| [SetDisableCommandMinecart](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#setdisablecommandminecart) | 服务端 | 尚未建立映射 | — |
| [SetDisableContainers](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#setdisablecontainers) | 服务端 | 尚未建立映射 | — |
| [SetDisableDropItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#setdisabledropitem) | 服务端 | 尚未建立映射 | — |
| [SetDisableGravityInLiquid](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#setdisablegravityinliquid) | 服务端 | 尚未建立映射 | — |
| [SetDisableHunger](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#setdisablehunger) | 服务端 | 尚未建立映射 | — |
| [SetGameDifficulty](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#setgamedifficulty) | 服务端 | 发现原生调用，待核对 | — |
| [SetGameRulesInfoServer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#setgamerulesinfoserver) | 服务端 | 发现原生调用，待核对 | — |
| [SetHurtCD](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#sethurtcd) | 服务端 | 尚未建立映射 | — |
| [SetLevelGravity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#setlevelgravity) | 服务端 | 尚未建立映射 | — |
| [SetPistonMaxInteractionCount](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B8%B8%E6%88%8F%E8%A7%84%E5%88%99.md#setpistonmaxinteractioncount) | 服务端 | 尚未建立映射 | — |

</div>

## 世界 / 自定义数据

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CleanExtraData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%B0%E6%8D%AE.md#cleanextradata) | 服务端 | 已有离线核验路径 | [Entity.setDynamicProperties](server/apis/entity.md#setDynamicProperties), [World.setDynamicProperties](server/apis/world.md#setDynamicProperties) |
| [GetExtraData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%B0%E6%8D%AE.md#getextradata) | 服务端 | 已有离线核验路径 | [Entity.getDynamicProperty](server/apis/entity.md#getDynamicProperty), [World.getDynamicProperty](server/apis/world.md#getDynamicProperty) |
| [GetWholeExtraData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%B0%E6%8D%AE.md#getwholeextradata) | 服务端 | 已有离线核验路径 | [Entity.getDynamicPropertyIds](server/apis/entity.md#getDynamicPropertyIds), [World.getDynamicPropertyIds](server/apis/world.md#getDynamicPropertyIds) |
| [SaveExtraData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%B0%E6%8D%AE.md#saveextradata) | 服务端 | 已有离线核验路径 | [Entity.setDynamicProperties](server/apis/entity.md#setDynamicProperties), [World.setDynamicProperties](server/apis/world.md#setDynamicProperties) |
| [SetExtraData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%B0%E6%8D%AE.md#setextradata) | 服务端 | 已有离线核验路径 | [Entity.setDynamicProperties](server/apis/entity.md#setDynamicProperties), [World.setDynamicProperties](server/apis/world.md#setDynamicProperties) |

</div>

## 世界 / 指令

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetCommandPermissionLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%8C%87%E4%BB%A4.md#getcommandpermissionlevel) | 服务端 | 尚未建立映射 | — |
| [GetDefaultPlayerPermissionLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%8C%87%E4%BB%A4.md#getdefaultplayerpermissionlevel) | 服务端 | 尚未建立映射 | — |
| [SetCommand](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%8C%87%E4%BB%A4.md#setcommand) | 服务端 | 发现原生调用，待核对 | — |
| [SetCommandPermissionLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%8C%87%E4%BB%A4.md#setcommandpermissionlevel) | 服务端 | 尚未建立映射 | — |
| [SetDefaultPlayerPermissionLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%8C%87%E4%BB%A4.md#setdefaultplayerpermissionlevel) | 服务端 | 尚未建立映射 | — |

</div>

## 世界 / 消息

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [NotifyOneMessage](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B6%88%E6%81%AF.md#notifyonemessage) | 服务端 | 发现原生调用，待核对 | — |
| [SendMsg](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B6%88%E6%81%AF.md#sendmsg) | 服务端 | 尚未建立映射 | — |
| [SendMsgToPlayer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B6%88%E6%81%AF.md#sendmsgtoplayer) | 服务端 | 尚未建立映射 | — |
| [SetLeftCornerNotify](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B6%88%E6%81%AF.md#setleftcornernotify) | 客户端 | 尚未建立映射 | — |
| [SetNotifyMsg](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B6%88%E6%81%AF.md#setnotifymsg) | 服务端 | 尚未建立映射 | — |
| [SetOnePopupNotice](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B6%88%E6%81%AF.md#setonepopupnotice) | 服务端 | 尚未建立映射 | — |
| [SetOneTipMessage](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B6%88%E6%81%AF.md#setonetipmessage) | 服务端 | 尚未建立映射 | — |
| [SetPopupNotice](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B6%88%E6%81%AF.md#setpopupnotice) | 服务端 | 发现原生调用，待核对 | — |
| [SetPopupNotice](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B6%88%E6%81%AF.md#setpopupnotice) | 客户端 | 发现原生调用，待核对 | — |
| [SetPopupState](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B6%88%E6%81%AF.md#setpopupstate) | 客户端 | 尚未建立映射 | — |
| [SetTipMessage](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B6%88%E6%81%AF.md#settipmessage) | 服务端 | 尚未建立映射 | — |
| [SetTipMessage](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E6%B6%88%E6%81%AF.md#settipmessage) | 客户端 | 尚未建立映射 | — |

</div>

## 世界 / 记分板

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetAllPlayerScoreboardObjects](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E8%AE%B0%E5%88%86%E6%9D%BF.md#getallplayerscoreboardobjects) | 服务端 | 发现原生调用，待核对 | — |
| [GetAllPlayerScoreboardObjects](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E8%AE%B0%E5%88%86%E6%9D%BF.md#getallplayerscoreboardobjects) | 客户端 | 发现原生调用，待核对 | — |
| [GetAllScoreboardObjects](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E8%AE%B0%E5%88%86%E6%9D%BF.md#getallscoreboardobjects) | 服务端 | 发现原生调用，待核对 | — |
| [GetAllScoreboardObjects](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E8%AE%B0%E5%88%86%E6%9D%BF.md#getallscoreboardobjects) | 客户端 | 发现原生调用，待核对 | — |

</div>

## 世界 / 行为

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [UseItemAttackEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E8%A1%8C%E4%B8%BA.md#useitemattackentity) | 服务端 | 尚未建立映射 | — |
| [UseItemToEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E8%A1%8C%E4%B8%BA.md#useitemtoentity) | 服务端 | 尚未建立映射 | — |
| [UseItemToPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E4%B8%96%E7%95%8C/%E8%A1%8C%E4%B8%BA.md#useitemtopos) | 服务端 | 尚未建立映射 | — |

</div>

## 实体 / 实体类型

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetEngineType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%9E%E4%BD%93%E7%B1%BB%E5%9E%8B.md#getenginetype) | 服务端 | 发现原生调用，待核对 | — |
| [GetEngineType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%9E%E4%BD%93%E7%B1%BB%E5%9E%8B.md#getenginetype) | 客户端 | 发现原生调用，待核对 | — |
| [GetEngineTypeStr](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%9E%E4%BD%93%E7%B1%BB%E5%9E%8B.md#getenginetypestr) | 服务端 | 已有离线核验路径 | [Entity.getOwner](server/apis/entity.md#getOwner) |
| [GetEngineTypeStr](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%9E%E4%BD%93%E7%B1%BB%E5%9E%8B.md#getenginetypestr) | 客户端 | 已有离线核验路径 | [ClientEntity.typeId](client/reference/ClientEntity.md#typeId) |
| [GetEntityDefinitions](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%9E%E4%BD%93%E7%B1%BB%E5%9E%8B.md#getentitydefinitions) | 服务端 | 尚未建立映射 | — |
| [GetEntityNBTTags](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%9E%E4%BD%93%E7%B1%BB%E5%9E%8B.md#getentitynbttags) | 服务端 | 已有离线核验路径 | [EntityAttributeComponent.defaultValue](server/reference/EntityAttributeComponent.md#defaultValue), [EntityAttributeComponent.effectiveMin](server/reference/EntityAttributeComponent.md#effectiveMin) |

</div>

## 实体 / 附加值

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetAuxValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E9%99%84%E5%8A%A0%E5%80%BC.md#getauxvalue) | 服务端 | 尚未建立映射 | — |
| [GetAuxValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E9%99%84%E5%8A%A0%E5%80%BC.md#getauxvalue) | 客户端 | 尚未建立映射 | — |

</div>

## 实体 / 属性

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddModifier](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#addmodifier) | 服务端 | 尚未建立映射 | — |
| [ChangeEntityDimension](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#changeentitydimension) | 服务端 | 发现原生调用，待核对 | — |
| [GetAllComponentsName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getallcomponentsname) | 服务端 | 发现原生调用，待核对 | — |
| [GetAllModifiers](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getallmodifiers) | 服务端 | 尚未建立映射 | — |
| [GetAttrMaxValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getattrmaxvalue) | 服务端 | 已有离线核验路径 | [EntityAttributeComponent.effectiveMax](server/reference/EntityAttributeComponent.md#effectiveMax), [EntityAttributeComponent.setCurrentValue](server/reference/EntityAttributeComponent.md#setCurrentValue) |
| [GetAttrMaxValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getattrmaxvalue) | 客户端 | 已有离线核验路径 | [ClientEntityAttributeComponent.effectiveMax](client/reference/ClientEntityAttributeComponent.md#effectiveMax) |
| [GetAttrValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getattrvalue) | 服务端 | 已有离线核验路径 | [EntityAttributeComponent.currentValue](server/reference/EntityAttributeComponent.md#currentValue), [EntityAttributeComponent.isValid](server/reference/EntityAttributeComponent.md#isValid), [Entity.health](server/apis/entity.md#health) |
| [GetAttrValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getattrvalue) | 客户端 | 已有离线核验路径 | [ClientEntity.getComponent](client/reference/ClientEntity.md#getComponent), [ClientEntity.getComponents](client/reference/ClientEntity.md#getComponents), [ClientEntityAttributeComponent.currentValue](client/reference/ClientEntityAttributeComponent.md#currentValue), [ClientEntityAttributeComponent.effectiveMax](client/reference/ClientEntityAttributeComponent.md#effectiveMax), [ClientEntityAttributeComponent.isValid](client/reference/ClientEntityAttributeComponent.md#isValid) |
| [GetBodyRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getbodyrot) | 客户端 | 已有离线核验路径 | [ClientEntity.bodyRotation](client/reference/ClientEntity.md#bodyRotation) |
| [GetCurrentAirSupply](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getcurrentairsupply) | 服务端 | 发现原生调用，待核对 | — |
| [GetCurrentAirSupply](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getcurrentairsupply) | 客户端 | 已有离线核验路径 | [ClientEntity.airSupplyTicks](client/reference/ClientEntity.md#airSupplyTicks) |
| [GetDeathTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getdeathtime) | 服务端 | 已有离线核验路径 | [Entity.deathTimeTicks](server/apis/entity.md#deathTimeTicks) |
| [GetEntitiesBySelector](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getentitiesbyselector) | 服务端 | 发现原生调用，待核对 | — |
| [GetEntityDamage](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getentitydamage) | 服务端 | 尚未建立映射 | — |
| [GetEntityDimensionId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getentitydimensionid) | 服务端 | 发现原生调用，待核对 | — |
| [GetEntityFallDistance](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getentityfalldistance) | 服务端 | 发现原生调用，待核对 | — |
| [GetEntityLinksTag](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getentitylinkstag) | 服务端 | 尚未建立映射 | — |
| [GetEntityOwner](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getentityowner) | 服务端 | 已有离线核验路径 | [Entity.getOwner](server/apis/entity.md#getOwner) |
| [GetFootPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getfootpos) | 服务端 | 发现原生调用，待核对 | — |
| [GetFootPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getfootpos) | 客户端 | 已有离线核验路径 | [ClientEntity.location](client/reference/ClientEntity.md#location) |
| [GetGravity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getgravity) | 服务端 | 尚未建立映射 | — |
| [GetLoadActors](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getloadactors) | 服务端 | 尚未建立映射 | — |
| [GetMarkVariant](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getmarkvariant) | 服务端 | 已有离线核验路径 | [Entity.markVariant](server/apis/entity.md#markVariant) |
| [GetMaxAirSupply](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getmaxairsupply) | 服务端 | 发现原生调用，待核对 | — |
| [GetMaxAirSupply](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getmaxairsupply) | 客户端 | 已有离线核验路径 | [ClientEntity.maxAirSupplyTicks](client/reference/ClientEntity.md#maxAirSupplyTicks) |
| [GetMobColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getmobcolor) | 服务端 | 已有离线核验路径 | [Entity.color](server/apis/entity.md#color) |
| [GetMobStrength](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getmobstrength) | 服务端 | 已有离线核验路径 | [Entity.strength](server/apis/entity.md#strength) |
| [GetMobStrengthMax](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getmobstrengthmax) | 服务端 | 已有离线核验路径 | [Entity.maxStrength](server/apis/entity.md#maxStrength) |
| [GetName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getname) | 服务端 | 发现原生调用，待核对 | — |
| [GetName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getname) | 客户端 | 已有离线核验路径 | [ClientEntity.nameTag](client/reference/ClientEntity.md#nameTag) |
| [GetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getpos) | 服务端 | 发现原生调用，待核对 | — |
| [GetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getpos) | 客户端 | 发现原生调用，待核对 | — |
| [GetRiderId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getriderid) | 客户端 | 已有离线核验路径 | [ClientPlayer.getRidingEntity](client/reference/ClientPlayer.md#getRidingEntity) |
| [GetRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getrot) | 服务端 | 发现原生调用，待核对 | — |
| [GetRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getrot) | 客户端 | 已有离线核验路径 | [ClientEntity.getRotation](client/reference/ClientEntity.md#getRotation) |
| [GetSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getsize) | 服务端 | 发现原生调用，待核对 | — |
| [GetSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getsize) | 客户端 | 已有离线核验路径 | [ClientEntity.collisionBoxSize](client/reference/ClientEntity.md#collisionBoxSize) |
| [GetTradeLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#gettradelevel) | 服务端 | 已有离线核验路径 | [Entity.tradeLevel](server/apis/entity.md#tradeLevel) |
| [GetTypeFamily](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#gettypefamily) | 服务端 | 发现原生调用，待核对 | — |
| [GetUnitBubbleAirSupply](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getunitbubbleairsupply) | 服务端 | 尚未建立映射 | — |
| [GetVariant](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#getvariant) | 服务端 | 已有离线核验路径 | [Entity.variant](server/apis/entity.md#variant) |
| [HasChest](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#haschest) | 服务端 | 已有离线核验路径 | [Entity.isChested](server/apis/entity.md#isChested) |
| [HasComponent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#hascomponent) | 服务端 | 发现原生调用，待核对 | — |
| [HasModifier](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#hasmodifier) | 服务端 | 尚未建立映射 | — |
| [HasSaddle](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#hassaddle) | 服务端 | 已有离线核验路径 | [Entity.isSaddled](server/apis/entity.md#isSaddled) |
| [IsAngry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#isangry) | 服务端 | 已有离线核验路径 | [Entity.isAngry](server/apis/entity.md#isAngry) |
| [IsBaby](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#isbaby) | 服务端 | 已有离线核验路径 | [Entity.isBaby](server/apis/entity.md#isBaby) |
| [IsConsumingAirSupply](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#isconsumingairsupply) | 服务端 | 尚未建立映射 | — |
| [IsIllagerCaptain](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#isillagercaptain) | 服务端 | 已有离线核验路径 | [Entity.isIllagerCaptain](server/apis/entity.md#isIllagerCaptain) |
| [IsNaturallySpawned](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#isnaturallyspawned) | 服务端 | 发现原生调用，待核对 | — |
| [IsOutOfControl](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#isoutofcontrol) | 服务端 | 已有离线核验路径 | [Entity.isOutOfControl](server/apis/entity.md#isOutOfControl) |
| [IsPregnant](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#ispregnant) | 服务端 | 已有离线核验路径 | [Entity.isPregnant](server/apis/entity.md#isPregnant) |
| [IsSheared](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#issheared) | 服务端 | 已有离线核验路径 | [Entity.isSheared](server/apis/entity.md#isSheared) |
| [IsSitting](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#issitting) | 服务端 | 已有离线核验路径 | [Entity.isSitting](server/apis/entity.md#isSitting) |
| [IsTamed](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#istamed) | 服务端 | 已有离线核验路径 | [Entity.isTamed](server/apis/entity.md#isTamed) |
| [LockLocalPlayerRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#locklocalplayerrot) | 客户端 | 尚未建立映射 | — |
| [PromoteToIllagerCaptain](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#promotetoillagercaptain) | 服务端 | 已有离线核验路径 | [Entity.promoteToIllagerCaptain](server/apis/entity.md#promoteToIllagerCaptain) |
| [RemoveModifier](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#removemodifier) | 服务端 | 尚未建立映射 | — |
| [ResetToDefaultValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#resettodefaultvalue) | 服务端 | 已有离线核验路径 | [EntityAttributeComponent.resetToDefaultValue](server/reference/EntityAttributeComponent.md#resetToDefaultValue) |
| [ResetToMaxValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#resettomaxvalue) | 服务端 | 已有离线核验路径 | [EntityAttributeComponent.resetToMaxValue](server/reference/EntityAttributeComponent.md#resetToMaxValue) |
| [SetAngry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setangry) | 服务端 | 已有离线核验路径 | [Entity.setAngry](server/apis/entity.md#setAngry) |
| [SetAsAdult](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setasadult) | 服务端 | 已有离线核验路径 | [Entity.growUp](server/apis/entity.md#growUp) |
| [SetAttrMaxValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setattrmaxvalue) | 服务端 | 已有离线核验路径 | [EntityAttributeComponent.setMaxValue](server/reference/EntityAttributeComponent.md#setMaxValue) |
| [SetAttrValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setattrvalue) | 服务端 | 已有离线核验路径 | [EntityAttributeComponent.setCurrentValue](server/reference/EntityAttributeComponent.md#setCurrentValue), [EntityAttributeComponent.resetToMinValue](server/reference/EntityAttributeComponent.md#resetToMinValue), [Entity.health](server/apis/entity.md#health) |
| [SetChest](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setchest) | 服务端 | 已有离线核验路径 | [Entity.setChested](server/apis/entity.md#setChested) |
| [SetCurrentAirSupply](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setcurrentairsupply) | 服务端 | 尚未建立映射 | — |
| [SetEntityLookAtPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setentitylookatpos) | 服务端 | 尚未建立映射 | — |
| [SetEntityOwner](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setentityowner) | 服务端 | 已有离线核验路径 | [Entity.setOwner](server/apis/entity.md#setOwner) |
| [SetFootPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setfootpos) | 服务端 | 发现原生调用，待核对 | — |
| [SetGravity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setgravity) | 服务端 | 尚未建立映射 | — |
| [SetMarkVariant](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setmarkvariant) | 服务端 | 已有离线核验路径 | [Entity.setMarkVariant](server/apis/entity.md#setMarkVariant) |
| [SetMaxAirSupply](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setmaxairsupply) | 服务端 | 尚未建立映射 | — |
| [SetMobColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setmobcolor) | 服务端 | 已有离线核验路径 | [Entity.setColor](server/apis/entity.md#setColor) |
| [SetMobStrength](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setmobstrength) | 服务端 | 已有离线核验路径 | [Entity.setStrength](server/apis/entity.md#setStrength) |
| [SetMobStrengthMax](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setmobstrengthmax) | 服务端 | 已有离线核验路径 | [Entity.setMaxStrength](server/apis/entity.md#setMaxStrength) |
| [SetName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setname) | 服务端 | 发现原生调用，待核对 | — |
| [SetOutOfControl](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setoutofcontrol) | 服务端 | 已有离线核验路径 | [Entity.setOutOfControl](server/apis/entity.md#setOutOfControl) |
| [SetPersistent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setpersistent) | 服务端 | 发现原生调用，待核对 | — |
| [SetPlayerLookAtPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setplayerlookatpos) | 客户端 | 尚未建立映射 | — |
| [SetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setpos) | 服务端 | 尚未建立映射 | — |
| [SetPosForClientEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setposforcliententity) | 客户端 | 已有离线核验路径 | [ClientEntity.teleport](client/reference/ClientEntity.md#teleport) |
| [SetRecoverTotalAirSupplyTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setrecovertotalairsupplytime) | 服务端 | 尚未建立映射 | — |
| [SetRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setrot) | 服务端 | 发现原生调用，待核对 | — |
| [SetRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setrot) | 客户端 | 发现原生调用，待核对 | — |
| [SetRotForClientEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setrotforcliententity) | 客户端 | 已有离线核验路径 | [ClientEntity.setRotation](client/reference/ClientEntity.md#setRotation) |
| [SetSheared](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setsheared) | 服务端 | 已有离线核验路径 | [Entity.setSheared](server/apis/entity.md#setSheared) |
| [SetSitting](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setsitting) | 服务端 | 已有离线核验路径 | [Entity.setSitting](server/apis/entity.md#setSitting) |
| [SetSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setsize) | 服务端 | 发现原生调用，待核对 | — |
| [SetTradeLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#settradelevel) | 服务端 | 已有离线核验路径 | [Entity.setTradeLevel](server/apis/entity.md#setTradeLevel) |
| [SetVariant](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#setvariant) | 服务端 | 已有离线核验路径 | [Entity.setVariant](server/apis/entity.md#setVariant) |
| [UpdateModifier](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#updatemodifier) | 服务端 | 尚未建立映射 | — |
| [isEntityInLava](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#isentityinlava) | 客户端 | 已有离线核验路径 | [ClientEntity.isInLava](client/reference/ClientEntity.md#isInLava) |
| [isEntityOnGround](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%B1%9E%E6%80%A7.md#isentityonground) | 客户端 | 已有离线核验路径 | [ClientEntity.isOnGround](client/reference/ClientEntity.md#isOnGround) |

</div>

## 实体 / 行为

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddActorComponent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#addactorcomponent) | 服务端 | 尚未建立映射 | — |
| [AddActorComponentGroup](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#addactorcomponentgroup) | 服务端 | 尚未建立映射 | — |
| [AddEntityAroundEntityMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#addentityaroundentitymotion) | 服务端 | 尚未建立映射 | — |
| [AddEntityAroundPointMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#addentityaroundpointmotion) | 服务端 | 尚未建立映射 | — |
| [AddEntitySeat](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#addentityseat) | 服务端 | 尚未建立映射 | — |
| [AddEntityTrackMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#addentitytrackmotion) | 服务端 | 尚未建立映射 | — |
| [AddEntityVelocityMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#addentityvelocitymotion) | 服务端 | 尚未建立映射 | — |
| [ChangeRiderSeat](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#changeriderseat) | 服务端 | 尚未建立映射 | — |
| [DeleteEntitySeat](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#deleteentityseat) | 服务端 | 尚未建立映射 | — |
| [GetAttackTarget](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#getattacktarget) | 服务端 | 发现原生调用，待核对 | — |
| [GetAttackTarget](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#getattacktarget) | 客户端 | 已有离线核验路径 | [ClientEntity.getTarget](client/reference/ClientEntity.md#getTarget) |
| [GetBlockControlAi](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#getblockcontrolai) | 服务端 | 尚未建立映射 | — |
| [GetComponents](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#getcomponents) | 服务端 | 发现原生调用，待核对 | — |
| [GetCustomGoalCls](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#getcustomgoalcls) | 服务端 | 发现原生调用，待核对 | — |
| [GetEntityMotions](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#getentitymotions) | 服务端 | 尚未建立映射 | — |
| [GetJumpPower](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#getjumppower) | 服务端 | 尚未建立映射 | — |
| [GetLeashHolder](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#getleashholder) | 服务端 | 尚未建立映射 | — |
| [GetMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#getmotion) | 服务端 | 发现原生调用，待核对 | — |
| [GetMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#getmotion) | 客户端 | 已有离线核验路径 | [ClientEntity.getVelocity](client/reference/ClientEntity.md#getVelocity) |
| [GetOwnerId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#getownerid) | 服务端 | 发现原生调用，待核对 | — |
| [GetOwnerId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#getownerid) | 客户端 | 已有离线核验路径 | [ClientEntity.getOwner](client/reference/ClientEntity.md#getOwner) |
| [GetRiders](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#getriders) | 服务端 | 尚未建立映射 | — |
| [GetStepHeight](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#getstepheight) | 服务端 | 尚未建立映射 | — |
| [Hurt](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#hurt) | 服务端 | 发现原生调用，待核对 | — |
| [ImmuneDamage](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#immunedamage) | 服务端 | 尚未建立映射 | — |
| [IsEating](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#iseating) | 服务端 | 尚未建立映射 | — |
| [IsEntityOnFire](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#isentityonfire) | 服务端 | 发现原生调用，待核对 | — |
| [IsLootDropped](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#islootdropped) | 服务端 | 尚未建立映射 | — |
| [IsPersistent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#ispersistent) | 服务端 | 尚未建立映射 | — |
| [IsRoaring](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#isroaring) | 服务端 | 尚未建立映射 | — |
| [IsStunned](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#isstunned) | 服务端 | 尚未建立映射 | — |
| [RemoveActorComponent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#removeactorcomponent) | 服务端 | 尚未建立映射 | — |
| [RemoveActorComponentGroup](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#removeactorcomponentgroup) | 服务端 | 尚未建立映射 | — |
| [RemoveEntityMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#removeentitymotion) | 服务端 | 尚未建立映射 | — |
| [ResetAttackTarget](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#resetattacktarget) | 服务端 | 尚未建立映射 | — |
| [ResetMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#resetmotion) | 服务端 | 尚未建立映射 | — |
| [ResetStepHeight](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#resetstepheight) | 服务端 | 尚未建立映射 | — |
| [SetActorCollidable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setactorcollidable) | 服务端 | 尚未建立映射 | — |
| [SetActorPushable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setactorpushable) | 服务端 | 尚未建立映射 | — |
| [SetAttackTarget](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setattacktarget) | 服务端 | 尚未建立映射 | — |
| [SetBlockControlAi](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setblockcontrolai) | 服务端 | 尚未建立映射 | — |
| [SetCanOtherPlayerRide](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setcanotherplayerride) | 服务端 | 尚未建立映射 | — |
| [SetControl](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setcontrol) | 服务端 | 尚未建立映射 | — |
| [SetEntityInteractFilter](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setentityinteractfilter) | 服务端 | 尚未建立映射 | — |
| [SetEntityLockRider](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setentitylockrider) | 服务端 | 尚未建立映射 | — |
| [SetEntityOnFire](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setentityonfire) | 服务端 | 发现原生调用，待核对 | — |
| [SetEntityRide](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setentityride) | 服务端 | 尚未建立映射 | — |
| [SetEntitySeat](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setentityseat) | 服务端 | 尚未建立映射 | — |
| [SetEntityShareablesItems](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setentityshareablesitems) | 服务端 | 尚未建立映射 | — |
| [SetEntityTamed](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setentitytamed) | 服务端 | 尚未建立映射 | — |
| [SetJumpPower](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setjumppower) | 服务端 | 尚未建立映射 | — |
| [SetLeashHolder](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setleashholder) | 服务端 | 尚未建立映射 | — |
| [SetLootDropped](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setlootdropped) | 服务端 | 尚未建立映射 | — |
| [SetMobKnockback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setmobknockback) | 服务端 | 发现原生调用，待核对 | — |
| [SetMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setmotion) | 服务端 | 发现原生调用，待核对 | — |
| [SetMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setmotion) | 客户端 | 已有离线核验路径 | [ClientPlayer.setVelocity](client/reference/ClientPlayer.md#setVelocity) |
| [SetMoveSetting](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setmovesetting) | 服务端 | 尚未建立映射 | — |
| [SetPersistence](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setpersistence) | 服务端 | 尚未建立映射 | — |
| [SetRidePos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setridepos) | 服务端 | 尚未建立映射 | — |
| [SetRiderRideEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setriderrideentity) | 服务端 | 尚未建立映射 | — |
| [SetStepHeight](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#setstepheight) | 服务端 | 尚未建立映射 | — |
| [StartEntityMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#startentitymotion) | 服务端 | 尚未建立映射 | — |
| [StopEntityMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#stopentitymotion) | 服务端 | 尚未建立映射 | — |
| [StopEntityRiding](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#stopentityriding) | 服务端 | 尚未建立映射 | — |
| [TriggerCustomEvent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%A1%8C%E4%B8%BA.md#triggercustomevent) | 服务端 | 发现原生调用，待核对 | — |

</div>

## 实体 / 状态效果

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddEffectToEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E7%8A%B6%E6%80%81%E6%95%88%E6%9E%9C.md#addeffecttoentity) | 服务端 | 发现原生调用，待核对 | — |
| [GetAllEffects](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E7%8A%B6%E6%80%81%E6%95%88%E6%9E%9C.md#getalleffects) | 服务端 | 发现原生调用，待核对 | — |
| [GetAllEffects](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E7%8A%B6%E6%80%81%E6%95%88%E6%9E%9C.md#getalleffects) | 客户端 | 发现原生调用，待核对 | — |
| [GetLoadEffects](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E7%8A%B6%E6%80%81%E6%95%88%E6%9E%9C.md#getloadeffects) | 服务端 | 尚未建立映射 | — |
| [HasEffect](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E7%8A%B6%E6%80%81%E6%95%88%E6%9E%9C.md#haseffect) | 服务端 | 尚未建立映射 | — |
| [HasEffect](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E7%8A%B6%E6%80%81%E6%95%88%E6%9E%9C.md#haseffect) | 客户端 | 尚未建立映射 | — |
| [RemoveEffectFromEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E7%8A%B6%E6%80%81%E6%95%88%E6%9E%9C.md#removeeffectfromentity) | 服务端 | 发现原生调用，待核对 | — |

</div>

## 实体 / 渲染

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddActorAnimation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addactoranimation) | 客户端 | 尚未建立映射 | — |
| [AddActorAnimationController](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addactoranimationcontroller) | 客户端 | 尚未建立映射 | — |
| [AddActorBlockGeometry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addactorblockgeometry) | 客户端 | 尚未建立映射 | — |
| [AddActorGeometry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addactorgeometry) | 客户端 | 尚未建立映射 | — |
| [AddActorParticleEffect](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addactorparticleeffect) | 客户端 | 尚未建立映射 | — |
| [AddActorRenderController](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addactorrendercontroller) | 客户端 | 尚未建立映射 | — |
| [AddActorRenderControllerArray](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addactorrendercontrollerarray) | 客户端 | 尚未建立映射 | — |
| [AddActorRenderMaterial](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addactorrendermaterial) | 客户端 | 尚未建立映射 | — |
| [AddActorScriptAnimate](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addactorscriptanimate) | 客户端 | 尚未建立映射 | — |
| [AddActorSoundEffect](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addactorsoundeffect) | 客户端 | 尚未建立映射 | — |
| [AddActorTexture](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addactortexture) | 客户端 | 尚未建立映射 | — |
| [AddAnimationControllerToOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addanimationcontrollertooneactor) | 客户端 | 尚未建立映射 | — |
| [AddAnimationToOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addanimationtooneactor) | 客户端 | 尚未建立映射 | — |
| [AddGeometryToOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addgeometrytooneactor) | 客户端 | 尚未建立映射 | — |
| [AddParticleEffectToOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addparticleeffecttooneactor) | 客户端 | 尚未建立映射 | — |
| [AddRenderControllerToOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addrendercontrollertooneactor) | 客户端 | 尚未建立映射 | — |
| [AddRenderMaterialToOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addrendermaterialtooneactor) | 客户端 | 尚未建立映射 | — |
| [AddScriptAnimateToOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addscriptanimatetooneactor) | 客户端 | 尚未建立映射 | — |
| [AddSoundEffectToOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addsoundeffecttooneactor) | 客户端 | 尚未建立映射 | — |
| [AddTextureToOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#addtexturetooneactor) | 客户端 | 尚未建立映射 | — |
| [BindEntityToEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#bindentitytoentity) | 客户端 | 尚未建立映射 | — |
| [ClearActorBlockGeometry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#clearactorblockgeometry) | 客户端 | 尚未建立映射 | — |
| [CopyActorGeometryFromPlayer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#copyactorgeometryfromplayer) | 客户端 | 尚未建立映射 | — |
| [CopyActorRenderMaterialFromPlayer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#copyactorrendermaterialfromplayer) | 客户端 | 尚未建立映射 | — |
| [CopyActorTextureFromPlayer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#copyactortexturefromplayer) | 客户端 | 尚未建立映射 | — |
| [CopyPlayerGeometryToOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#copyplayergeometrytooneactor) | 客户端 | 尚未建立映射 | — |
| [CopyPlayerRenderMaterialToOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#copyplayerrendermaterialtooneactor) | 客户端 | 尚未建立映射 | — |
| [CopyPlayerTextureToOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#copyplayertexturetooneactor) | 客户端 | 尚未建立映射 | — |
| [DeleteActorBlockGeometry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#deleteactorblockgeometry) | 客户端 | 尚未建立映射 | — |
| [GetActorRenderParams](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#getactorrenderparams) | 客户端 | 尚未建立映射 | — |
| [GetEntityExtraUniforms](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#getentityextrauniforms) | 客户端 | 尚未建立映射 | — |
| [GetEntityRenderDistance](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#getentityrenderdistance) | 客户端 | 尚未建立映射 | — |
| [GetEntityUIExtraUniforms](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#getentityuiextrauniforms) | 客户端 | 尚未建立映射 | — |
| [GetNotRenderAtAll](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#getnotrenderatall) | 客户端 | 尚未建立映射 | — |
| [GetQueryableBoneOrientation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#getqueryableboneorientation) | 客户端 | 尚未建立映射 | — |
| [IsShowName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#isshowname) | 客户端 | 尚未建立映射 | — |
| [RebuildActorRender](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#rebuildactorrender) | 客户端 | 尚未建立映射 | — |
| [RebuildRenderForOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#rebuildrenderforoneactor) | 客户端 | 尚未建立映射 | — |
| [RemoveActorAnimationController](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#removeactoranimationcontroller) | 客户端 | 尚未建立映射 | — |
| [RemoveActorGeometry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#removeactorgeometry) | 客户端 | 尚未建立映射 | — |
| [RemoveActorRenderController](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#removeactorrendercontroller) | 客户端 | 尚未建立映射 | — |
| [RemoveActorTexture](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#removeactortexture) | 客户端 | 尚未建立映射 | — |
| [RemoveAnimationControllerForOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#removeanimationcontrollerforoneactor) | 客户端 | 尚未建立映射 | — |
| [RemoveGeometryForOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#removegeometryforoneactor) | 客户端 | 尚未建立映射 | — |
| [RemoveRenderControllerForOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#removerendercontrollerforoneactor) | 客户端 | 尚未建立映射 | — |
| [RemoveTextureForOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#removetextureforoneactor) | 客户端 | 尚未建立映射 | — |
| [ResetActorRender](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#resetactorrender) | 客户端 | 尚未建立映射 | — |
| [ResetBindEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#resetbindentity) | 客户端 | 尚未建立映射 | — |
| [ResetEntityExtraSkin](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#resetentityextraskin) | 客户端 | 尚未建立映射 | — |
| [ResetRenderForOneActor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#resetrenderforoneactor) | 客户端 | 尚未建立映射 | — |
| [SetActorAllBlockGeometryVisible](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#setactorallblockgeometryvisible) | 客户端 | 尚未建立映射 | — |
| [SetActorBlockGeometryVisible](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#setactorblockgeometryvisible) | 客户端 | 尚未建立映射 | — |
| [SetAlwaysShowName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#setalwaysshowname) | 客户端 | 尚未建立映射 | — |
| [SetColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#setcolor) | 客户端 | 发现原生调用，待核对 | — |
| [SetEntityExtraUniforms](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#setentityextrauniforms) | 客户端 | 尚未建立映射 | — |
| [SetEntityRenderDistance](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#setentityrenderdistance) | 客户端 | 尚未建立映射 | — |
| [SetEntityUIExtraUniforms](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#setentityuiextrauniforms) | 客户端 | 尚未建立映射 | — |
| [SetHealthBarDeviation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#sethealthbardeviation) | 客户端 | 尚未建立映射 | — |
| [SetNameDeeptest](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#setnamedeeptest) | 客户端 | 尚未建立映射 | — |
| [SetNotRenderAtAll](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#setnotrenderatall) | 客户端 | 尚未建立映射 | — |
| [SetRenderLocalPlayer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#setrenderlocalplayer) | 客户端 | 尚未建立映射 | — |
| [SetShowName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#setshowname) | 客户端 | 尚未建立映射 | — |
| [ShowHealth](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#showhealth) | 客户端 | 尚未建立映射 | — |
| [ShowHealthBar](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%B8%B2%E6%9F%93.md#showhealthbar) | 客户端 | 尚未建立映射 | — |

</div>

## 实体 / 背包

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetEntityItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%83%8C%E5%8C%85.md#getentityitem) | 服务端 | 已有离线核验路径 | [EntityEquippableComponent.getEquipment](server/reference/EntityEquippableComponent.md#getEquipment) |
| [GetEquItemEnchant](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%83%8C%E5%8C%85.md#getequitemenchant) | 服务端 | 尚未建立映射 | — |
| [GetEquItemModEnchant](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%83%8C%E5%8C%85.md#getequitemmodenchant) | 服务端 | 尚未建立映射 | — |
| [SetEntityItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%83%8C%E5%8C%85.md#setentityitem) | 服务端 | 已有离线核验路径 | [EntityEquippableComponent.setEquipment](server/reference/EntityEquippableComponent.md#setEquipment) |

</div>

## 实体 / 自定义属性

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetAttr](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%B1%9E%E6%80%A7.md#getattr) | 服务端 | 尚未建立映射 | — |
| [GetAttr](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%B1%9E%E6%80%A7.md#getattr) | 客户端 | 尚未建立映射 | — |
| [RegisterUpdateFunc](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%B1%9E%E6%80%A7.md#registerupdatefunc) | 客户端 | 尚未建立映射 | — |
| [SaveAttr](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%B1%9E%E6%80%A7.md#saveattr) | 服务端 | 尚未建立映射 | — |
| [SetAttr](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%B1%9E%E6%80%A7.md#setattr) | 服务端 | 尚未建立映射 | — |
| [SetAttr](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%B1%9E%E6%80%A7.md#setattr) | 客户端 | 尚未建立映射 | — |
| [UnRegisterUpdateFunc](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%B1%9E%E6%80%A7.md#unregisterupdatefunc) | 客户端 | 尚未建立映射 | — |

</div>

## 实体 / 自定义数据

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CleanExtraData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%B0%E6%8D%AE.md#cleanextradata) | 服务端 | 已有离线核验路径 | [Entity.setDynamicProperties](server/apis/entity.md#setDynamicProperties), [World.setDynamicProperties](server/apis/world.md#setDynamicProperties) |
| [GetExtraData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%B0%E6%8D%AE.md#getextradata) | 服务端 | 已有离线核验路径 | [Entity.getDynamicProperty](server/apis/entity.md#getDynamicProperty), [World.getDynamicProperty](server/apis/world.md#getDynamicProperty) |
| [GetWholeExtraData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%B0%E6%8D%AE.md#getwholeextradata) | 服务端 | 已有离线核验路径 | [Entity.getDynamicPropertyIds](server/apis/entity.md#getDynamicPropertyIds), [World.getDynamicPropertyIds](server/apis/world.md#getDynamicPropertyIds) |
| [SaveExtraData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%B0%E6%8D%AE.md#saveextradata) | 服务端 | 已有离线核验路径 | [Entity.setDynamicProperties](server/apis/entity.md#setDynamicProperties), [World.setDynamicProperties](server/apis/world.md#setDynamicProperties) |
| [SetExtraData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%95%B0%E6%8D%AE.md#setextradata) | 服务端 | 已有离线核验路径 | [Entity.setDynamicProperties](server/apis/entity.md#setDynamicProperties), [World.setDynamicProperties](server/apis/world.md#setDynamicProperties) |

</div>

## 实体 / molang

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [EvalMolangExpression](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/molang.md#evalmolangexpression) | 服务端 | 发现原生调用，待核对 | — |
| [EvalMolangExpression](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/molang.md#evalmolangexpression) | 客户端 | 发现原生调用，待核对 | — |
| [Get](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/molang.md#get) | 客户端 | 发现原生调用，待核对 | — |
| [GetAllProperties](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/molang.md#getallproperties) | 服务端 | 发现原生调用，待核对 | — |
| [GetMolangValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/molang.md#getmolangvalue) | 客户端 | 尚未建立映射 | — |
| [GetStringHash64](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/molang.md#getstringhash64) | 客户端 | 尚未建立映射 | — |
| [Register](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/molang.md#register) | 客户端 | 发现原生调用，待核对 | — |
| [Set](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/molang.md#set) | 客户端 | 发现原生调用，待核对 | — |
| [SetPropertyValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/molang.md#setpropertyvalue) | 服务端 | 发现原生调用，待核对 | — |
| [UnRegister](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/molang.md#unregister) | 客户端 | 发现原生调用，待核对 | — |

</div>

## 实体 / 标签

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddEntityTag](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%A0%87%E7%AD%BE.md#addentitytag) | 服务端 | 发现原生调用，待核对 | — |
| [EntityHasTag](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%A0%87%E7%AD%BE.md#entityhastag) | 服务端 | 发现原生调用，待核对 | — |
| [GetEntityTags](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%A0%87%E7%AD%BE.md#getentitytags) | 服务端 | 发现原生调用，待核对 | — |
| [RemoveEntityTag](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%A0%87%E7%AD%BE.md#removeentitytag) | 服务端 | 发现原生调用，待核对 | — |

</div>

## 实体 / 抛射物

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetSourceEntityId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E6%8A%9B%E5%B0%84%E7%89%A9.md#getsourceentityid) | 服务端 | 尚未建立映射 | — |

</div>

## 实体 / 经验球

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetOrbExperience](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E7%BB%8F%E9%AA%8C%E7%90%83.md#getorbexperience) | 服务端 | 尚未建立映射 | — |
| [SetOrbExperience](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E7%BB%8F%E9%AA%8C%E7%90%83.md#setorbexperience) | 服务端 | 尚未建立映射 | — |

</div>

## 实体 / 官方伙伴

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [Disable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%98%E6%96%B9%E4%BC%99%E4%BC%B4.md#disable) | 服务端 | 尚未建立映射 | — |
| [Enable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%98%E6%96%B9%E4%BC%99%E4%BC%B4.md#enable) | 服务端 | 尚未建立映射 | — |

</div>

## 实体 / 官方聊天扩展

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddCommonPhrases](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%98%E6%96%B9%E8%81%8A%E5%A4%A9%E6%89%A9%E5%B1%95.md#addcommonphrases) | 服务端 | 尚未建立映射 | — |
| [Disable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%98%E6%96%B9%E8%81%8A%E5%A4%A9%E6%89%A9%E5%B1%95.md#disable) | 服务端 | 尚未建立映射 | — |
| [Enable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%98%E6%96%B9%E8%81%8A%E5%A4%A9%E6%89%A9%E5%B1%95.md#enable) | 服务端 | 尚未建立映射 | — |
| [RegisterChatPrefix](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%98%E6%96%B9%E8%81%8A%E5%A4%A9%E6%89%A9%E5%B1%95.md#registerchatprefix) | 服务端 | 尚未建立映射 | — |
| [RemoveCommonPhrases](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%98%E6%96%B9%E8%81%8A%E5%A4%A9%E6%89%A9%E5%B1%95.md#removecommonphrases) | 服务端 | 尚未建立映射 | — |
| [SetShowOfficialPhrases](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%98%E6%96%B9%E8%81%8A%E5%A4%A9%E6%89%A9%E5%B1%95.md#setshowofficialphrases) | 服务端 | 尚未建立映射 | — |
| [SetShowSocialNearbyInfo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E5%AE%98%E6%96%B9%E8%81%8A%E5%A4%A9%E6%89%A9%E5%B1%95.md#setshowsocialnearbyinfo) | 服务端 | 尚未建立映射 | — |

</div>

## 实体 / 魔法指令

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [Disable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E9%AD%94%E6%B3%95%E6%8C%87%E4%BB%A4.md#disable) | 服务端 | 尚未建立映射 | — |
| [Enable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%AE%9E%E4%BD%93/%E9%AD%94%E6%B3%95%E6%8C%87%E4%BB%A4.md#enable) | 服务端 | 尚未建立映射 | — |

</div>

## 玩家 / 属性

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddPlayerExperience](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#addplayerexperience) | 服务端 | 尚未建立映射 | — |
| [AddPlayerLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#addplayerlevel) | 服务端 | 发现原生调用，待核对 | — |
| [CollectOnlineClientData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#collectonlineclientdata) | 服务端 | 尚未建立映射 | — |
| [GetArmorValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getarmorvalue) | 客户端 | 已有离线核验路径 | [ClientPlayer.armorValue](client/reference/ClientPlayer.md#armorValue) |
| [GetEnchantmentSeed](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getenchantmentseed) | 服务端 | 尚未建立映射 | — |
| [GetPlayerCurLevelExp](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getplayercurlevelexp) | 客户端 | 已有离线核验路径 | [ClientPlayer.totalXpNeededForNextLevel](client/reference/ClientPlayer.md#totalXpNeededForNextLevel) |
| [GetPlayerCurrentExhaustionValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getplayercurrentexhaustionvalue) | 服务端 | 尚未建立映射 | — |
| [GetPlayerExp](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getplayerexp) | 服务端 | 发现原生调用，待核对 | — |
| [GetPlayerExp](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getplayerexp) | 客户端 | 已有离线核验路径 | [ClientPlayer.xpEarnedAtCurrentLevel](client/reference/ClientPlayer.md#xpEarnedAtCurrentLevel) |
| [GetPlayerHealthLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getplayerhealthlevel) | 服务端 | 尚未建立映射 | — |
| [GetPlayerHealthTick](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getplayerhealthtick) | 服务端 | 尚未建立映射 | — |
| [GetPlayerHunger](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getplayerhunger) | 服务端 | 发现原生调用，待核对 | — |
| [GetPlayerHunger](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getplayerhunger) | 客户端 | 已有离线核验路径 | [ClientPlayer.hunger](client/reference/ClientPlayer.md#hunger) |
| [GetPlayerLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getplayerlevel) | 服务端 | 发现原生调用，待核对 | — |
| [GetPlayerMaxExhaustionValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getplayermaxexhaustionvalue) | 服务端 | 尚未建立映射 | — |
| [GetPlayerStarveLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getplayerstarvelevel) | 服务端 | 尚未建立映射 | — |
| [GetPlayerStarveTick](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getplayerstarvetick) | 服务端 | 尚未建立映射 | — |
| [GetPlayerTotalExp](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getplayertotalexp) | 服务端 | 发现原生调用，待核对 | — |
| [GetPlayerTotalExp](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getplayertotalexp) | 客户端 | 已有离线核验路径 | [ClientPlayer.getTotalXp](client/reference/ClientPlayer.md#getTotalXp) |
| [IsHighLevelMultiJointOfficialSkin](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#ishighlevelmultijointofficialskin) | 客户端 | 尚未建立映射 | — |
| [IsHighLevelOfficialSkin](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#ishighlevelofficialskin) | 客户端 | 尚未建立映射 | — |
| [IsMultiJointOfficialSkin](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#ismultijointofficialskin) | 客户端 | 尚未建立映射 | — |
| [IsOfficialSkin](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#isofficialskin) | 客户端 | 尚未建立映射 | — |
| [IsPlayerNaturalRegen](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#isplayernaturalregen) | 服务端 | 尚未建立映射 | — |
| [IsPlayerNaturalStarve](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#isplayernaturalstarve) | 服务端 | 尚未建立映射 | — |
| [SetEnchantmentSeed](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#setenchantmentseed) | 服务端 | 尚未建立映射 | — |
| [SetPlayerCurrentExhaustionValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#setplayercurrentexhaustionvalue) | 服务端 | 尚未建立映射 | — |
| [SetPlayerHealthLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#setplayerhealthlevel) | 服务端 | 尚未建立映射 | — |
| [SetPlayerHealthTick](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#setplayerhealthtick) | 服务端 | 尚未建立映射 | — |
| [SetPlayerHunger](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#setplayerhunger) | 服务端 | 尚未建立映射 | — |
| [SetPlayerMaxExhaustionValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#setplayermaxexhaustionvalue) | 服务端 | 尚未建立映射 | — |
| [SetPlayerNaturalRegen](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#setplayernaturalregen) | 服务端 | 尚未建立映射 | — |
| [SetPlayerNaturalStarve](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#setplayernaturalstarve) | 服务端 | 尚未建立映射 | — |
| [SetPlayerPrefixAndSuffixName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#setplayerprefixandsuffixname) | 服务端 | 尚未建立映射 | — |
| [SetPlayerStarveLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#setplayerstarvelevel) | 服务端 | 尚未建立映射 | — |
| [SetPlayerStarveTick](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#setplayerstarvetick) | 服务端 | 尚未建立映射 | — |
| [SetPlayerTotalExp](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#setplayertotalexp) | 服务端 | 发现原生调用，待核对 | — |
| [Swing](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#swing) | 客户端 | 已有离线核验路径 | [ClientPlayer.swingArm](client/reference/ClientPlayer.md#swingArm) |
| [getUid](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%B1%9E%E6%80%A7.md#getuid) | 客户端 | 尚未建立映射 | — |

</div>

## 玩家 / 行为

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddPlayerAroundEntityMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#addplayeraroundentitymotion) | 服务端 | 尚未建立映射 | — |
| [AddPlayerAroundPointMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#addplayeraroundpointmotion) | 服务端 | 尚未建立映射 | — |
| [AddPlayerTrackMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#addplayertrackmotion) | 服务端 | 尚未建立映射 | — |
| [AddPlayerVelocityMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#addplayervelocitymotion) | 服务端 | 尚未建立映射 | — |
| [BeginSprinting](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#beginsprinting) | 客户端 | 尚未建立映射 | — |
| [ChangePlayerDimension](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#changeplayerdimension) | 服务端 | 发现原生调用，待核对 | — |
| [ChangePlayerFlyState](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#changeplayerflystate) | 服务端 | 尚未建立映射 | — |
| [EnableKeepInventory](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#enablekeepinventory) | 服务端 | 尚未建立映射 | — |
| [EndSprinting](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#endsprinting) | 客户端 | 尚未建立映射 | — |
| [GetEntityRider](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getentityrider) | 服务端 | 发现原生调用，待核对 | — |
| [GetEntityRider](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getentityrider) | 客户端 | 已有离线核验路径 | [ClientPlayer.getRidingEntity](client/reference/ClientPlayer.md#getRidingEntity) |
| [GetInteracteCenterOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getinteractecenteroffset) | 服务端 | 尚未建立映射 | — |
| [GetIsBlocking](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getisblocking) | 服务端 | 尚未建立映射 | — |
| [GetPickCenterOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getpickcenteroffset) | 客户端 | 尚未建立映射 | — |
| [GetPickRange](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getpickrange) | 客户端 | 尚未建立映射 | — |
| [GetPlayerDestroyTotalTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getplayerdestroytotaltime) | 服务端 | 尚未建立映射 | — |
| [GetPlayerDestroyTotalTime](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getplayerdestroytotaltime) | 客户端 | 尚未建立映射 | — |
| [GetPlayerExhaustionRatioByType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getplayerexhaustionratiobytype) | 服务端 | 尚未建立映射 | — |
| [GetPlayerInteracteRange](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getplayerinteracterange) | 服务端 | 尚未建立映射 | — |
| [GetPlayerIsFishing](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getplayerisfishing) | 服务端 | 发现原生调用，待核对 | — |
| [GetPlayerIsFishing](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getplayerisfishing) | 客户端 | 已有离线核验路径 | [ClientPlayer.isFishing](client/reference/ClientPlayer.md#isFishing) |
| [GetPlayerMotions](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getplayermotions) | 服务端 | 尚未建立映射 | — |
| [GetPlayerRespawnPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getplayerrespawnpos) | 服务端 | 发现原生调用，待核对 | — |
| [GetRelevantPlayer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#getrelevantplayer) | 服务端 | 尚未建立映射 | — |
| [IsEntityRiding](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#isentityriding) | 服务端 | 尚未建立映射 | — |
| [IsInScaffolding](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#isinscaffolding) | 客户端 | 已有离线核验路径 | [ClientPlayer.isInScaffolding](client/reference/ClientPlayer.md#isInScaffolding) |
| [IsOnLadder](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#isonladder) | 客户端 | 已有离线核验路径 | [ClientPlayer.isOnLadder](client/reference/ClientPlayer.md#isOnLadder) |
| [IsPlayerCanFly](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#isplayercanfly) | 服务端 | 尚未建立映射 | — |
| [IsPlayerFlying](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#isplayerflying) | 服务端 | 发现原生调用，待核对 | — |
| [OpenNeteaseContainer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#openneteasecontainer) | 服务端 | 尚未建立映射 | — |
| [OpenWorkBench](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#openworkbench) | 服务端 | 尚未建立映射 | — |
| [PickUpItemEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#pickupitementity) | 服务端 | 尚未建立映射 | — |
| [PlayerAttackEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#playerattackentity) | 服务端 | 尚未建立映射 | — |
| [PlayerDestroyBlock](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#playerdestroyblock) | 服务端 | 尚未建立映射 | — |
| [PlayerUseItemToEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#playeruseitemtoentity) | 服务端 | 尚未建立映射 | — |
| [PlayerUseItemToPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#playeruseitemtopos) | 服务端 | 尚未建立映射 | — |
| [RemovePlayerMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#removeplayermotion) | 服务端 | 尚未建立映射 | — |
| [SetBanPlayerFishing](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setbanplayerfishing) | 服务端 | 尚未建立映射 | — |
| [SetInteracteCenterOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setinteractecenteroffset) | 服务端 | 尚未建立映射 | — |
| [SetPickCenterOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setpickcenteroffset) | 客户端 | 尚未建立映射 | — |
| [SetPickRange](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setpickrange) | 客户端 | 尚未建立映射 | — |
| [SetPickUpArea](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setpickuparea) | 服务端 | 尚未建立映射 | — |
| [SetPlayerAttackSpeedAmplifier](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setplayerattackspeedamplifier) | 服务端 | 尚未建立映射 | — |
| [SetPlayerExhaustionRatioByType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setplayerexhaustionratiobytype) | 服务端 | 尚未建立映射 | — |
| [SetPlayerInteracteRange](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setplayerinteracterange) | 服务端 | 尚未建立映射 | — |
| [SetPlayerJumpable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setplayerjumpable) | 服务端 | 尚未建立映射 | — |
| [SetPlayerMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setplayermotion) | 服务端 | 发现原生调用，待核对 | — |
| [SetPlayerMovable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setplayermovable) | 服务端 | 尚未建立映射 | — |
| [SetPlayerRespawnPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setplayerrespawnpos) | 服务端 | 尚未建立映射 | — |
| [StartPlayerMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#startplayermotion) | 服务端 | 尚未建立映射 | — |
| [StopPlayerMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#stopplayermotion) | 服务端 | 尚未建立映射 | — |
| [isGliding](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#isgliding) | 客户端 | 已有离线核验路径 | [ClientPlayer.isGliding](client/reference/ClientPlayer.md#isGliding) |
| [isInWater](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#isinwater) | 客户端 | 已有离线核验路径 | [ClientPlayer.isInWater](client/reference/ClientPlayer.md#isInWater) |
| [isMoving](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#ismoving) | 客户端 | 已有离线核验路径 | [ClientPlayer.isMoving](client/reference/ClientPlayer.md#isMoving) |
| [isRiding](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#isriding) | 客户端 | 已有离线核验路径 | [ClientPlayer.isRiding](client/reference/ClientPlayer.md#isRiding) |
| [isSneaking](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#issneaking) | 服务端 | 发现原生调用，待核对 | — |
| [isSneaking](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#issneaking) | 客户端 | 已有离线核验路径 | [ClientPlayer.isSneaking](client/reference/ClientPlayer.md#isSneaking) |
| [isSprinting](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#issprinting) | 客户端 | 已有离线核验路径 | [ClientPlayer.isSprinting](client/reference/ClientPlayer.md#isSprinting) |
| [isSwimming](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#isswimming) | 服务端 | 发现原生调用，待核对 | — |
| [isSwimming](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#isswimming) | 客户端 | 已有离线核验路径 | [ClientPlayer.isSwimming](client/reference/ClientPlayer.md#isSwimming) |
| [setMoving](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setmoving) | 客户端 | 尚未建立映射 | — |
| [setSneaking](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setsneaking) | 客户端 | 尚未建立映射 | — |
| [setSprinting](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setsprinting) | 客户端 | 尚未建立映射 | — |
| [setUsingShield](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%A1%8C%E4%B8%BA.md#setusingshield) | 客户端 | 已有离线核验路径 | [ClientPlayer.setShieldActive](client/reference/ClientPlayer.md#setShieldActive) |

</div>

## 玩家 / 渲染

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddPlayerAnimation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#addplayeranimation) | 客户端 | 尚未建立映射 | — |
| [AddPlayerAnimationController](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#addplayeranimationcontroller) | 客户端 | 尚未建立映射 | — |
| [AddPlayerAnimationIntoState](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#addplayeranimationintostate) | 客户端 | 尚未建立映射 | — |
| [AddPlayerGeometry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#addplayergeometry) | 客户端 | 尚未建立映射 | — |
| [AddPlayerParticleEffect](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#addplayerparticleeffect) | 客户端 | 尚未建立映射 | — |
| [AddPlayerRenderController](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#addplayerrendercontroller) | 客户端 | 尚未建立映射 | — |
| [AddPlayerRenderMaterial](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#addplayerrendermaterial) | 客户端 | 尚未建立映射 | — |
| [AddPlayerScriptAnimate](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#addplayerscriptanimate) | 客户端 | 尚未建立映射 | — |
| [AddPlayerSoundEffect](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#addplayersoundeffect) | 客户端 | 尚未建立映射 | — |
| [AddPlayerTexture](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#addplayertexture) | 客户端 | 尚未建立映射 | — |
| [RebuildPlayerRender](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#rebuildplayerrender) | 客户端 | 尚未建立映射 | — |
| [RemovePlayerAnimationController](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#removeplayeranimationcontroller) | 客户端 | 尚未建立映射 | — |
| [RemovePlayerGeometry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#removeplayergeometry) | 客户端 | 尚未建立映射 | — |
| [RemovePlayerRenderController](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#removeplayerrendercontroller) | 客户端 | 尚未建立映射 | — |
| [ResetSkin](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#resetskin) | 客户端 | 尚未建立映射 | — |
| [SetPlayerItemInHandVisible](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#setplayeriteminhandvisible) | 客户端 | 尚未建立映射 | — |
| [SetSkin](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B2%E6%9F%93.md#setskin) | 客户端 | 尚未建立映射 | — |

</div>

## 玩家 / 背包

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddEnchantToInvItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#addenchanttoinvitem) | 服务端 | 尚未建立映射 | — |
| [AddModEnchantToInvItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#addmodenchanttoinvitem) | 服务端 | 尚未建立映射 | — |
| [ChangePlayerItemTipsAndExtraId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#changeplayeritemtipsandextraid) | 服务端 | 尚未建立映射 | — |
| [ChangeSelectSlot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#changeselectslot) | 服务端 | 发现原生调用，待核对 | — |
| [GetCarriedItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#getcarrieditem) | 客户端 | 尚未建立映射 | — |
| [GetInvItemEnchantData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#getinvitemenchantdata) | 服务端 | 尚未建立映射 | — |
| [GetInvItemModEnchantData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#getinvitemmodenchantdata) | 服务端 | 尚未建立映射 | — |
| [GetOffhandItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#getoffhanditem) | 客户端 | 尚未建立映射 | — |
| [GetPlayerAllItems](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#getplayerallitems) | 服务端 | 尚未建立映射 | — |
| [GetPlayerAllItems](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#getplayerallitems) | 客户端 | 尚未建立映射 | — |
| [GetPlayerFishHookEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#getplayerfishhookentity) | 服务端 | 尚未建立映射 | — |
| [GetPlayerFishHookEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#getplayerfishhookentity) | 客户端 | 尚未建立映射 | — |
| [GetPlayerFishItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#getplayerfishitem) | 服务端 | 尚未建立映射 | — |
| [GetPlayerFishItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#getplayerfishitem) | 客户端 | 尚未建立映射 | — |
| [GetPlayerItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#getplayeritem) | 服务端 | 发现原生调用，待核对 | — |
| [GetPlayerItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#getplayeritem) | 客户端 | 发现原生调用，待核对 | — |
| [GetSelectSlotId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#getselectslotid) | 服务端 | 发现原生调用，待核对 | — |
| [GetSlotId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#getslotid) | 客户端 | 尚未建立映射 | — |
| [RemoveEnchantToInvItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#removeenchanttoinvitem) | 服务端 | 尚未建立映射 | — |
| [RemoveModEnchantToInvItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#removemodenchanttoinvitem) | 服务端 | 尚未建立映射 | — |
| [SetInvItemExchange](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#setinvitemexchange) | 服务端 | 尚未建立映射 | — |
| [SetInvItemNum](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#setinvitemnum) | 服务端 | 发现原生调用，待核对 | — |
| [SetPlayerAllItems](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#setplayerallitems) | 服务端 | 尚未建立映射 | — |
| [SpawnItemToPlayerCarried](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#spawnitemtoplayercarried) | 服务端 | 尚未建立映射 | — |
| [SpawnItemToPlayerInv](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E8%83%8C%E5%8C%85.md#spawnitemtoplayerinv) | 服务端 | 发现原生调用，待核对 | — |

</div>

## 玩家 / 摄像机

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddCameraAroundEntityMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#addcameraaroundentitymotion) | 客户端 | 尚未建立映射 | — |
| [AddCameraAroundPointMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#addcameraaroundpointmotion) | 客户端 | 尚未建立映射 | — |
| [AddCameraTrackMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#addcameratrackmotion) | 客户端 | 尚未建立映射 | — |
| [AddCameraVelocityMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#addcameravelocitymotion) | 客户端 | 尚未建立映射 | — |
| [DepartCamera](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#departcamera) | 客户端 | 已有离线核验路径 | [ClientCamera.location](client/reference/ClientCamera.md#location) |
| [GetCameraAnchor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#getcameraanchor) | 客户端 | 发现原生调用，待核对 | — |
| [GetCameraMotions](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#getcameramotions) | 客户端 | 发现原生调用，待核对 | — |
| [GetCameraOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#getcameraoffset) | 客户端 | 发现原生调用，待核对 | — |
| [GetCameraPitchLimit](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#getcamerapitchlimit) | 客户端 | 发现原生调用，待核对 | — |
| [GetCameraRotation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#getcamerarotation) | 客户端 | 发现原生调用，待核对 | — |
| [GetForward](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#getforward) | 客户端 | 发现原生调用，待核对 | — |
| [GetFov](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#getfov) | 客户端 | 发现原生调用，待核对 | — |
| [GetFpHeight](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#getfpheight) | 客户端 | 尚未建立映射 | — |
| [GetPerspective](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#getperspective) | 客户端 | 已有离线核验路径 | [ClientCamera.perspective](client/reference/ClientCamera.md#perspective) |
| [GetPosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#getposition) | 客户端 | 发现原生调用，待核对 | — |
| [IsModCameraLockPitch](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#ismodcameralockpitch) | 客户端 | 尚未建立映射 | — |
| [IsModCameraLockYaw](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#ismodcameralockyaw) | 客户端 | 尚未建立映射 | — |
| [LockCamera](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#lockcamera) | 客户端 | 发现原生调用，待核对 | — |
| [LockModCameraPitch](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#lockmodcamerapitch) | 客户端 | 尚未建立映射 | — |
| [LockModCameraYaw](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#lockmodcamerayaw) | 客户端 | 尚未建立映射 | — |
| [LockPerspective](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#lockperspective) | 客户端 | 尚未建立映射 | — |
| [RemoveCameraMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#removecameramotion) | 客户端 | 尚未建立映射 | — |
| [ResetCameraBindActorId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#resetcamerabindactorid) | 客户端 | 尚未建立映射 | — |
| [ResetCameraPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#resetcamerapos) | 客户端 | 发现原生调用，待核对 | — |
| [SetCameraAnchor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#setcameraanchor) | 客户端 | 发现原生调用，待核对 | — |
| [SetCameraBindActorId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#setcamerabindactorid) | 客户端 | 尚未建立映射 | — |
| [SetCameraDistanceFixed](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#setcameradistancefixed) | 客户端 | 尚未建立映射 | — |
| [SetCameraOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#setcameraoffset) | 客户端 | 发现原生调用，待核对 | — |
| [SetCameraPitchLimit](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#setcamerapitchlimit) | 客户端 | 已有离线核验路径 | [ClientCamera.pitchLimits](client/reference/ClientCamera.md#pitchLimits) |
| [SetCameraPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#setcamerapos) | 客户端 | 已有离线核验路径 | [ClientCamera.location](client/reference/ClientCamera.md#location) |
| [SetCameraRotation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#setcamerarotation) | 客户端 | 发现原生调用，待核对 | — |
| [SetFov](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#setfov) | 客户端 | 已有离线核验路径 | [ClientCamera.fov](client/reference/ClientCamera.md#fov) |
| [SetPerspective](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#setperspective) | 客户端 | 已有离线核验路径 | [ClientCamera.perspective](client/reference/ClientCamera.md#perspective) |
| [SetPlayerFovScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#setplayerfovscale) | 客户端 | 尚未建立映射 | — |
| [SetSpeedFovLock](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#setspeedfovlock) | 客户端 | 尚未建立映射 | — |
| [StartCameraMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#startcameramotion) | 客户端 | 尚未建立映射 | — |
| [StopCameraMotion](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#stopcameramotion) | 客户端 | 尚未建立映射 | — |
| [UnDepartCamera](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#undepartcamera) | 客户端 | 尚未建立映射 | — |
| [UnLockCamera](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%91%84%E5%83%8F%E6%9C%BA.md#unlockcamera) | 客户端 | 发现原生调用，待核对 | — |

</div>

## 玩家 / 动画

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [PlayTpAnimation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%8A%A8%E7%94%BB.md#playtpanimation) | 客户端 | 尚未建立映射 | — |
| [StopAnimation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%8A%A8%E7%94%BB.md#stopanimation) | 客户端 | 尚未建立映射 | — |

</div>

## 玩家 / 游戏模式

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetPlayerGameType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B8%E6%88%8F%E6%A8%A1%E5%BC%8F.md#getplayergametype) | 服务端 | 发现原生调用，待核对 | — |
| [GetPlayerGameType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B8%E6%88%8F%E6%A8%A1%E5%BC%8F.md#getplayergametype) | 客户端 | 发现原生调用，待核对 | — |
| [SetPlayerGameType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%B8%B8%E6%88%8F%E6%A8%A1%E5%BC%8F.md#setplayergametype) | 服务端 | 发现原生调用，待核对 | — |

</div>

## 玩家 / 权限

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetPlayerAbilities](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%9D%83%E9%99%90.md#getplayerabilities) | 服务端 | 尚未建立映射 | — |
| [GetPlayerOperation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%9D%83%E9%99%90.md#getplayeroperation) | 服务端 | 发现原生调用，待核对 | — |
| [SetAttackMobsAbility](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%9D%83%E9%99%90.md#setattackmobsability) | 服务端 | 尚未建立映射 | — |
| [SetAttackPlayersAbility](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%9D%83%E9%99%90.md#setattackplayersability) | 服务端 | 尚未建立映射 | — |
| [SetBuildAbility](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%9D%83%E9%99%90.md#setbuildability) | 服务端 | 尚未建立映射 | — |
| [SetMineAbility](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%9D%83%E9%99%90.md#setmineability) | 服务端 | 尚未建立映射 | — |
| [SetOpenContainersAbility](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%9D%83%E9%99%90.md#setopencontainersability) | 服务端 | 尚未建立映射 | — |
| [SetOperateDoorsAndSwitchesAbility](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%9D%83%E9%99%90.md#setoperatedoorsandswitchesability) | 服务端 | 尚未建立映射 | — |
| [SetOperatorCommandAbility](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%9D%83%E9%99%90.md#setoperatorcommandability) | 服务端 | 尚未建立映射 | — |
| [SetPermissionLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%9D%83%E9%99%90.md#setpermissionlevel) | 服务端 | 尚未建立映射 | — |
| [SetPlayerMute](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%9D%83%E9%99%90.md#setplayermute) | 服务端 | 尚未建立映射 | — |
| [SetTeleportAbility](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E6%9D%83%E9%99%90.md#setteleportability) | 服务端 | 尚未建立映射 | — |

</div>

## 玩家 / 导航

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetNavPath](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%AF%BC%E8%88%AA.md#getnavpath) | 客户端 | 尚未建立映射 | — |
| [StartNavTo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%AF%BC%E8%88%AA.md#startnavto) | 客户端 | 尚未建立映射 | — |
| [StopNav](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E5%AE%B6/%E5%AF%BC%E8%88%AA.md#stopnav) | 客户端 | 尚未建立映射 | — |

</div>

## 方块 / 方块状态与附加值

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetBlockAuxValueFromStates](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E7%8A%B6%E6%80%81%E4%B8%8E%E9%99%84%E5%8A%A0%E5%80%BC.md#getblockauxvaluefromstates) | 服务端 | 发现原生调用，待核对 | — |
| [GetBlockStates](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E7%8A%B6%E6%80%81%E4%B8%8E%E9%99%84%E5%8A%A0%E5%80%BC.md#getblockstates) | 服务端 | 发现原生调用，待核对 | — |
| [GetBlockStatesFromAuxValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E7%8A%B6%E6%80%81%E4%B8%8E%E9%99%84%E5%8A%A0%E5%80%BC.md#getblockstatesfromauxvalue) | 服务端 | 发现原生调用，待核对 | — |
| [SetBlockStates](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E7%8A%B6%E6%80%81%E4%B8%8E%E9%99%84%E5%8A%A0%E5%80%BC.md#setblockstates) | 服务端 | 发现原生调用，待核对 | — |

</div>

## 方块 / 属性

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetBlockBasicInfo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%B1%9E%E6%80%A7.md#getblockbasicinfo) | 服务端 | 尚未建立映射 | — |
| [GetBlockTags](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%B1%9E%E6%80%A7.md#getblocktags) | 服务端 | 发现原生调用，待核对 | — |
| [GetLoadBlocks](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%B1%9E%E6%80%A7.md#getloadblocks) | 服务端 | 尚未建立映射 | — |
| [SetBlockBasicInfo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%B1%9E%E6%80%A7.md#setblockbasicinfo) | 服务端 | 尚未建立映射 | — |
| [SetChestLootTable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%B1%9E%E6%80%A7.md#setchestloottable) | 服务端 | 尚未建立映射 | — |

</div>

## 方块 / 方块实体

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CleanBlockTileEntityCustomData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#cleanblocktileentitycustomdata) | 服务端 | 尚未建立映射 | — |
| [CreateFrameEffectForBlockEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#createframeeffectforblockentity) | 客户端 | 尚未建立映射 | — |
| [CreateParticleEffectForBlockEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#createparticleeffectforblockentity) | 客户端 | 尚未建立映射 | — |
| [ExecuteCommandBlock](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#executecommandblock) | 服务端 | 尚未建立映射 | — |
| [GetBlockEntityData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#getblockentitydata) | 服务端 | 尚未建立映射 | — |
| [GetBlockEntityData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#getblockentitydata) | 客户端 | 尚未建立映射 | — |
| [GetBlockEntityMolangValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#getblockentitymolangvalue) | 客户端 | 尚未建立映射 | — |
| [GetBlockTileEntityCustomData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#getblocktileentitycustomdata) | 服务端 | 尚未建立映射 | — |
| [GetBlockTileEntityWholeCustomData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#getblocktileentitywholecustomdata) | 服务端 | 尚未建立映射 | — |
| [GetCommandBlock](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#getcommandblock) | 服务端 | 尚未建立映射 | — |
| [GetFrameEffectIdInBlockEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#getframeeffectidinblockentity) | 客户端 | 尚未建立映射 | — |
| [GetFrameItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#getframeitem) | 服务端 | 尚未建立映射 | — |
| [GetFrameItemDropChange](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#getframeitemdropchange) | 服务端 | 尚未建立映射 | — |
| [GetFrameRotation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#getframerotation) | 服务端 | 尚未建立映射 | — |
| [GetHopperSpeed](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#gethopperspeed) | 服务端 | 尚未建立映射 | — |
| [GetParticleEffectIdInBlockEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#getparticleeffectidinblockentity) | 客户端 | 尚未建立映射 | — |
| [RemoveFrameEffectInBlockEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#removeframeeffectinblockentity) | 客户端 | 尚未建立映射 | — |
| [RemoveParticleEffectInBlockEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#removeparticleeffectinblockentity) | 客户端 | 尚未建立映射 | — |
| [SetBlockEntityData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#setblockentitydata) | 服务端 | 尚未建立映射 | — |
| [SetBlockEntityMolangValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#setblockentitymolangvalue) | 客户端 | 尚未建立映射 | — |
| [SetBlockTileEntityCustomData](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#setblocktileentitycustomdata) | 服务端 | 尚未建立映射 | — |
| [SetCommandBlock](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#setcommandblock) | 服务端 | 尚未建立映射 | — |
| [SetEnableBlockEntityAnimations](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#setenableblockentityanimations) | 客户端 | 尚未建立映射 | — |
| [SetFrameItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#setframeitem) | 服务端 | 尚未建立映射 | — |
| [SetFrameItemDropChange](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#setframeitemdropchange) | 服务端 | 尚未建立映射 | — |
| [SetFrameRotation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#setframerotation) | 服务端 | 尚未建立映射 | — |
| [SetHopperSpeed](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93.md#sethopperspeed) | 服务端 | 尚未建立映射 | — |

</div>

## 方块 / 方块几何体模型

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CombineBlockBetweenPosToGeometry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%87%A0%E4%BD%95%E4%BD%93%E6%A8%A1%E5%9E%8B.md#combineblockbetweenpostogeometry) | 客户端 | 尚未建立映射 | — |
| [CombineBlockFromPosListToGeometry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%87%A0%E4%BD%95%E4%BD%93%E6%A8%A1%E5%9E%8B.md#combineblockfromposlisttogeometry) | 客户端 | 尚未建立映射 | — |
| [CombineBlockPaletteToGeometry](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%87%A0%E4%BD%95%E4%BD%93%E6%A8%A1%E5%9E%8B.md#combineblockpalettetogeometry) | 客户端 | 尚未建立映射 | — |
| [EnableActorBlockGeometryTransparent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%87%A0%E4%BD%95%E4%BD%93%E6%A8%A1%E5%9E%8B.md#enableactorblockgeometrytransparent) | 客户端 | 尚未建立映射 | — |
| [GetActorBlockGeometryScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%87%A0%E4%BD%95%E4%BD%93%E6%A8%A1%E5%9E%8B.md#getactorblockgeometryscale) | 客户端 | 尚未建立映射 | — |
| [SetActorBlockGeometryOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%87%A0%E4%BD%95%E4%BD%93%E6%A8%A1%E5%9E%8B.md#setactorblockgeometryoffset) | 客户端 | 尚未建立映射 | — |
| [SetActorBlockGeometryRotation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%87%A0%E4%BD%95%E4%BD%93%E6%A8%A1%E5%9E%8B.md#setactorblockgeometryrotation) | 客户端 | 尚未建立映射 | — |
| [SetActorBlockGeometryScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%87%A0%E4%BD%95%E4%BD%93%E6%A8%A1%E5%9E%8B.md#setactorblockgeometryscale) | 客户端 | 尚未建立映射 | — |
| [SetActorBlockGeometryTransparency](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E5%87%A0%E4%BD%95%E4%BD%93%E6%A8%A1%E5%9E%8B.md#setactorblockgeometrytransparency) | 客户端 | 尚未建立映射 | — |

</div>

## 方块 / 方块调色板

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [DeleteBlockInBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#deleteblockinblockpalette) | 客户端 | 尚未建立映射 | — |
| [DeleteBlockInBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#deleteblockinblockpalette) | 服务端 | 尚未建立映射 | — |
| [DeserializeBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#deserializeblockpalette) | 客户端 | 发现原生调用，待核对 | — |
| [DeserializeBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#deserializeblockpalette) | 服务端 | 发现原生调用，待核对 | — |
| [GetBlockCountInBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#getblockcountinblockpalette) | 客户端 | 尚未建立映射 | — |
| [GetBlockCountInBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#getblockcountinblockpalette) | 服务端 | 尚未建立映射 | — |
| [GetLocalPosListOfBlocks](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#getlocalposlistofblocks) | 客户端 | 尚未建立映射 | — |
| [GetLocalPosListOfBlocks](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#getlocalposlistofblocks) | 服务端 | 尚未建立映射 | — |
| [GetVolumeOfBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#getvolumeofblockpalette) | 客户端 | 尚未建立映射 | — |
| [GetVolumeOfBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#getvolumeofblockpalette) | 服务端 | 尚未建立映射 | — |
| [ReplaceAirByStructureVoid](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#replaceairbystructurevoid) | 客户端 | 尚未建立映射 | — |
| [ReplaceAirByStructureVoid](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#replaceairbystructurevoid) | 服务端 | 尚未建立映射 | — |
| [ReplaceBlockInBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#replaceblockinblockpalette) | 客户端 | 尚未建立映射 | — |
| [ReplaceBlockInBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#replaceblockinblockpalette) | 服务端 | 尚未建立映射 | — |
| [SerializeBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#serializeblockpalette) | 客户端 | 发现原生调用，待核对 | — |
| [SerializeBlockPalette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%96%B9%E5%9D%97%E8%B0%83%E8%89%B2%E6%9D%BF.md#serializeblockpalette) | 服务端 | 发现原生调用，待核对 | — |

</div>

## 方块 / 渲染

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddDropItemToWorld](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#adddropitemtoworld) | 客户端 | 尚未建立映射 | — |
| [ChangeBlockTextures](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#changeblocktextures) | 客户端 | 尚未建立映射 | — |
| [DeleteClientDropItemEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#deleteclientdropitementity) | 客户端 | 尚未建立映射 | — |
| [DestroyCrackFrame](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#destroycrackframe) | 客户端 | 尚未建立映射 | — |
| [GetBlockEntityExtraUniforms](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#getblockentityextrauniforms) | 客户端 | 尚未建立映射 | — |
| [GetBlockRenderDistance](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#getblockrenderdistance) | 客户端 | 尚未建立映射 | — |
| [GetBlockTextures](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#getblocktextures) | 客户端 | 尚未建立映射 | — |
| [GetClientDropItemEntityIdList](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#getclientdropitementityidlist) | 客户端 | 尚未建立映射 | — |
| [SetBlockEntityExtraUniforms](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#setblockentityextrauniforms) | 客户端 | 尚未建立映射 | — |
| [SetBlockEntityFramePosOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#setblockentityframeposoffset) | 客户端 | 尚未建立映射 | — |
| [SetBlockEntityModelPosOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#setblockentitymodelposoffset) | 客户端 | 尚未建立映射 | — |
| [SetBlockEntityModelRotation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#setblockentitymodelrotation) | 客户端 | 尚未建立映射 | — |
| [SetBlockEntityModelScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#setblockentitymodelscale) | 客户端 | 尚未建立映射 | — |
| [SetBlockEntityParticlePosOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#setblockentityparticleposoffset) | 客户端 | 尚未建立映射 | — |
| [SetBlockRenderDistance](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#setblockrenderdistance) | 客户端 | 尚未建立映射 | — |
| [SetCrackFrame](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#setcrackframe) | 客户端 | 尚未建立映射 | — |
| [SetDropItemTransform](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E6%B8%B2%E6%9F%93.md#setdropitemtransform) | 客户端 | 尚未建立映射 | — |

</div>

## 方块 / 容器

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetBrewingStandSlotItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#getbrewingstandslotitem) | 服务端 | 尚未建立映射 | — |
| [GetChestBoxSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#getchestboxsize) | 服务端 | 尚未建立映射 | — |
| [GetChestPairedPosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#getchestpairedposition) | 服务端 | 尚未建立映射 | — |
| [GetContainerItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#getcontaineritem) | 服务端 | 发现原生调用，待核对 | — |
| [GetContainerSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#getcontainersize) | 服务端 | 发现原生调用，待核对 | — |
| [GetEnderChestItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#getenderchestitem) | 服务端 | 尚未建立映射 | — |
| [GetInputSlotItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#getinputslotitem) | 服务端 | 尚未建立映射 | — |
| [GetOpenContainerItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#getopencontaineritem) | 服务端 | 尚未建立映射 | — |
| [GetOutputSlotItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#getoutputslotitem) | 服务端 | 尚未建立映射 | — |
| [GetPlayerUIItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#getplayeruiitem) | 服务端 | 尚未建立映射 | — |
| [SetBrewingStandSlotItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#setbrewingstandslotitem) | 服务端 | 尚未建立映射 | — |
| [SetChestBoxItemExchange](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#setchestboxitemexchange) | 服务端 | 尚未建立映射 | — |
| [SetChestBoxItemNum](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#setchestboxitemnum) | 服务端 | 尚未建立映射 | — |
| [SetInputSlotItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#setinputslotitem) | 服务端 | 尚未建立映射 | — |
| [SetPlayerUIItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#setplayeruiitem) | 服务端 | 尚未建立映射 | — |
| [SpawnItemToContainer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#spawnitemtocontainer) | 服务端 | 发现原生调用，待核对 | — |
| [SpawnItemToEnderChest](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%AE%B9%E5%99%A8.md#spawnitemtoenderchest) | 服务端 | 尚未建立映射 | — |

</div>

## 方块 / 红石

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetBlockPoweredState](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E7%BA%A2%E7%9F%B3.md#getblockpoweredstate) | 服务端 | 尚未建立映射 | — |
| [GetStrength](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E7%BA%A2%E7%9F%B3.md#getstrength) | 服务端 | 尚未建立映射 | — |

</div>

## 方块 / 告示牌

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetSignBlockText](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%91%8A%E7%A4%BA%E7%89%8C.md#getsignblocktext) | 服务端 | 尚未建立映射 | — |
| [GetSignTextStyle](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%91%8A%E7%A4%BA%E7%89%8C.md#getsigntextstyle) | 服务端 | 尚未建立映射 | — |
| [SetSignBlockText](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%91%8A%E7%A4%BA%E7%89%8C.md#setsignblocktext) | 服务端 | 尚未建立映射 | — |
| [SetSignTextStyle](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%91%8A%E7%A4%BA%E7%89%8C.md#setsigntextstyle) | 服务端 | 尚未建立映射 | — |

</div>

## 方块 / 床

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetBedColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%BA%8A.md#getbedcolor) | 服务端 | 尚未建立映射 | — |
| [SetBedColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%96%B9%E5%9D%97/%E5%BA%8A.md#setbedcolor) | 服务端 | 尚未建立映射 | — |

</div>

## 物品

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [BindItemToMinecraftModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#binditemtominecraftmodel) | 客户端 | 尚未建立映射 | — |
| [BindItemToSkeletonModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#binditemtoskeletonmodel) | 客户端 | 尚未建立映射 | — |
| [CancelShearsDestroyBlockSpeed](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#cancelshearsdestroyblockspeed) | 服务端 | 尚未建立映射 | — |
| [CancelShearsDestroyBlockSpeedAll](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#cancelshearsdestroyblockspeedall) | 服务端 | 尚未建立映射 | — |
| [ChangeArmorTextures](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#changearmortextures) | 客户端 | 尚未建立映射 | — |
| [ChangeItemTexture](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#changeitemtexture) | 客户端 | 尚未建立映射 | — |
| [GetAllEnchantsInfo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getallenchantsinfo) | 服务端 | 发现原生调用，待核对 | — |
| [GetAllEnchantsInfo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getallenchantsinfo) | 客户端 | 发现原生调用，待核对 | — |
| [GetBindBoneForBindItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getbindboneforbinditem) | 客户端 | 尚未建立映射 | — |
| [GetBindItemOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getbinditemoffset) | 客户端 | 尚未建立映射 | — |
| [GetBindItemRotation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getbinditemrotation) | 客户端 | 尚未建立映射 | — |
| [GetBindItemScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getbinditemscale) | 客户端 | 尚未建立映射 | — |
| [GetCustomName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getcustomname) | 服务端 | 尚未建立映射 | — |
| [GetItemBasicInfo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getitembasicinfo) | 服务端 | 已有离线核验路径 | [EntityEquippableComponent.totalArmor](server/reference/EntityEquippableComponent.md#totalArmor), [EntityEquippableComponent.totalToughness](server/reference/EntityEquippableComponent.md#totalToughness) |
| [GetItemBasicInfo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getitembasicinfo) | 客户端 | 发现原生调用，待核对 | — |
| [GetItemDefenceAngle](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getitemdefenceangle) | 服务端 | 尚未建立映射 | — |
| [GetItemDurability](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getitemdurability) | 服务端 | 尚未建立映射 | — |
| [GetItemEffectName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getitemeffectname) | 客户端 | 尚未建立映射 | — |
| [GetItemFormattedHoverText](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getitemformattedhovertext) | 客户端 | 尚未建立映射 | — |
| [GetItemHoverName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getitemhovername) | 客户端 | 尚未建立映射 | — |
| [GetItemInfoByBlockName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getiteminfobyblockname) | 服务端 | 尚未建立映射 | — |
| [GetItemLayer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getitemlayer) | 服务端 | 尚未建立映射 | — |
| [GetItemMaxDurability](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getitemmaxdurability) | 服务端 | 尚未建立映射 | — |
| [GetItemTags](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getitemtags) | 服务端 | 尚未建立映射 | — |
| [GetItemTags](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getitemtags) | 客户端 | 尚未建立映射 | — |
| [GetItemTexture](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getitemtexture) | 客户端 | 尚未建立映射 | — |
| [GetLoadItems](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getloaditems) | 服务端 | 尚未建立映射 | — |
| [GetUserDataInEvent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getuserdatainevent) | 服务端 | 发现原生调用，待核对 | — |
| [GetUserDataInEvent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#getuserdatainevent) | 客户端 | 发现原生调用，待核对 | — |
| [LookupItemByName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#lookupitembyname) | 服务端 | 尚未建立映射 | — |
| [RemoveItemLayer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#removeitemlayer) | 服务端 | 尚未建立映射 | — |
| [SetAttackDamage](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setattackdamage) | 服务端 | 尚未建立映射 | — |
| [SetBindBoneForBindItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setbindboneforbinditem) | 客户端 | 尚未建立映射 | — |
| [SetBindItemOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setbinditemoffset) | 客户端 | 尚未建立映射 | — |
| [SetBindItemRotation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setbinditemrotation) | 客户端 | 尚未建立映射 | — |
| [SetBindItemScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setbinditemscale) | 客户端 | 尚未建立映射 | — |
| [SetCompassEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setcompassentity) | 客户端 | 尚未建立映射 | — |
| [SetCompassTarget](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setcompasstarget) | 客户端 | 尚未建立映射 | — |
| [SetCustomName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setcustomname) | 服务端 | 尚未建立映射 | — |
| [SetItemDefenceAngle](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setitemdefenceangle) | 服务端 | 尚未建立映射 | — |
| [SetItemDurability](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setitemdurability) | 服务端 | 尚未建立映射 | — |
| [SetItemLayer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setitemlayer) | 服务端 | 尚未建立映射 | — |
| [SetItemMaxDurability](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setitemmaxdurability) | 服务端 | 尚未建立映射 | — |
| [SetItemTierLevel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setitemtierlevel) | 服务端 | 尚未建立映射 | — |
| [SetItemTierSpeed](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setitemtierspeed) | 服务端 | 尚未建立映射 | — |
| [SetMaxStackSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setmaxstacksize) | 服务端 | 尚未建立映射 | — |
| [SetShearsDestroyBlockSpeed](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81.md#setshearsdestroyblockspeed) | 服务端 | 尚未建立映射 | — |

</div>

## 特效 / 通用

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [DestroyEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E9%80%9A%E7%94%A8.md#destroyentity) | 客户端 | 发现原生调用，待核对 | — |

</div>

## 特效 / 文字面板

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CreateTextBoardInWorld](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E6%96%87%E5%AD%97%E9%9D%A2%E6%9D%BF.md#createtextboardinworld) | 客户端 | 尚未建立映射 | — |
| [RemoveTextBoard](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E6%96%87%E5%AD%97%E9%9D%A2%E6%9D%BF.md#removetextboard) | 客户端 | 尚未建立映射 | — |
| [SetBoardBackgroundColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E6%96%87%E5%AD%97%E9%9D%A2%E6%9D%BF.md#setboardbackgroundcolor) | 客户端 | 尚未建立映射 | — |
| [SetBoardBindEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E6%96%87%E5%AD%97%E9%9D%A2%E6%9D%BF.md#setboardbindentity) | 客户端 | 尚未建立映射 | — |
| [SetBoardDepthTest](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E6%96%87%E5%AD%97%E9%9D%A2%E6%9D%BF.md#setboarddepthtest) | 客户端 | 尚未建立映射 | — |
| [SetBoardFaceCamera](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E6%96%87%E5%AD%97%E9%9D%A2%E6%9D%BF.md#setboardfacecamera) | 客户端 | 尚未建立映射 | — |
| [SetBoardPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E6%96%87%E5%AD%97%E9%9D%A2%E6%9D%BF.md#setboardpos) | 客户端 | 尚未建立映射 | — |
| [SetBoardRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E6%96%87%E5%AD%97%E9%9D%A2%E6%9D%BF.md#setboardrot) | 客户端 | 尚未建立映射 | — |
| [SetBoardScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E6%96%87%E5%AD%97%E9%9D%A2%E6%9D%BF.md#setboardscale) | 客户端 | 尚未建立映射 | — |
| [SetBoardTextColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E6%96%87%E5%AD%97%E9%9D%A2%E6%9D%BF.md#setboardtextcolor) | 客户端 | 尚未建立映射 | — |
| [SetText](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E6%96%87%E5%AD%97%E9%9D%A2%E6%9D%BF.md#settext) | 客户端 | 发现原生调用，待核对 | — |

</div>

## 特效 / 序列帧

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [Bind](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#bind) | 客户端 | 尚未建立映射 | — |
| [CreateEngineSfx](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#createenginesfx) | 客户端 | 发现原生调用，待核对 | — |
| [CreateEngineSfxFromEditor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#createenginesfxfromeditor) | 客户端 | 尚未建立映射 | — |
| [GetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#getpos) | 客户端 | 发现原生调用，待核对 | — |
| [GetRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#getrot) | 客户端 | 发现原生调用，待核对 | — |
| [GetScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#getscale) | 客户端 | 尚未建立映射 | — |
| [Pause](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#pause) | 客户端 | 发现原生调用，待核对 | — |
| [Play](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#play) | 客户端 | 尚未建立映射 | — |
| [SetDeepTest](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#setdeeptest) | 客户端 | 尚未建立映射 | — |
| [SetFaceCamera](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#setfacecamera) | 客户端 | 尚未建立映射 | — |
| [SetFadeDistance](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#setfadedistance) | 客户端 | 尚未建立映射 | — |
| [SetGlobal](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#setglobal) | 客户端 | 尚未建立映射 | — |
| [SetLayer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#setlayer) | 客户端 | 发现原生调用，待核对 | — |
| [SetLoop](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#setloop) | 客户端 | 尚未建立映射 | — |
| [SetMixColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#setmixcolor) | 客户端 | 尚未建立映射 | — |
| [SetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#setpos) | 客户端 | 尚未建立映射 | — |
| [SetRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#setrot) | 客户端 | 发现原生调用，待核对 | — |
| [SetRotUseZXY](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#setrotusezxy) | 客户端 | 尚未建立映射 | — |
| [SetScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#setscale) | 客户端 | 尚未建立映射 | — |
| [SetUsePointFiltering](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#setusepointfiltering) | 客户端 | 尚未建立映射 | — |
| [Stop](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BA%8F%E5%88%97%E5%B8%A7.md#stop) | 客户端 | 尚未建立映射 | — |

</div>

## 特效 / 粒子

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [Bind](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#bind) | 客户端 | 尚未建立映射 | — |
| [CreateEngineParticle](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#createengineparticle) | 客户端 | 发现原生调用，待核对 | — |
| [GetParticleEmissionRate](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#getparticleemissionrate) | 客户端 | 尚未建立映射 | — |
| [GetParticleMaxNum](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#getparticlemaxnum) | 客户端 | 尚未建立映射 | — |
| [GetParticleMaxSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#getparticlemaxsize) | 客户端 | 尚未建立映射 | — |
| [GetParticleMinSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#getparticleminsize) | 客户端 | 尚未建立映射 | — |
| [GetParticleVolumeSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#getparticlevolumesize) | 客户端 | 尚未建立映射 | — |
| [GetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#getpos) | 客户端 | 发现原生调用，待核对 | — |
| [GetRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#getrot) | 客户端 | 发现原生调用，待核对 | — |
| [Pause](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#pause) | 客户端 | 发现原生调用，待核对 | — |
| [Play](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#play) | 客户端 | 尚未建立映射 | — |
| [SetFadeDistance](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#setfadedistance) | 客户端 | 尚未建立映射 | — |
| [SetGlobal](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#setglobal) | 客户端 | 尚未建立映射 | — |
| [SetLayer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#setlayer) | 客户端 | 发现原生调用，待核对 | — |
| [SetParticleEmissionRate](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#setparticleemissionrate) | 客户端 | 尚未建立映射 | — |
| [SetParticleMaxNum](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#setparticlemaxnum) | 客户端 | 尚未建立映射 | — |
| [SetParticleSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#setparticlesize) | 客户端 | 尚未建立映射 | — |
| [SetParticleVolumeSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#setparticlevolumesize) | 客户端 | 尚未建立映射 | — |
| [SetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#setpos) | 客户端 | 尚未建立映射 | — |
| [SetRelative](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#setrelative) | 客户端 | 尚未建立映射 | — |
| [SetRotUseZXY](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#setrotusezxy) | 客户端 | 尚未建立映射 | — |
| [SetUsePointFiltering](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#setusepointfiltering) | 客户端 | 尚未建立映射 | — |
| [Stop](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E7%B2%92%E5%AD%90.md#stop) | 客户端 | 尚未建立映射 | — |

</div>

## 特效 / 模型特效

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CreateEngineEffectBind](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E6%A8%A1%E5%9E%8B%E7%89%B9%E6%95%88.md#createengineeffectbind) | 客户端 | 发现原生调用，待核对 | — |
| [Pause](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E6%A8%A1%E5%9E%8B%E7%89%B9%E6%95%88.md#pause) | 客户端 | 发现原生调用，待核对 | — |
| [Resume](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E6%A8%A1%E5%9E%8B%E7%89%B9%E6%95%88.md#resume) | 客户端 | 发现原生调用，待核对 | — |

</div>

## 特效 / 微软粒子

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [BindEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#bindentity) | 客户端 | 发现原生调用，待核对 | — |
| [BindModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#bindmodel) | 客户端 | 尚未建立映射 | — |
| [Create](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#create) | 客户端 | 发现原生调用，待核对 | — |
| [CreateBindEntityNew](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#createbindentitynew) | 客户端 | 尚未建立映射 | — |
| [EmitManually](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#emitmanually) | 客户端 | 发现原生调用，待核对 | — |
| [Exist](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#exist) | 客户端 | 发现原生调用，待核对 | — |
| [GetActiveDuration](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#getactiveduration) | 客户端 | 尚未建立映射 | — |
| [GetBindingID](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#getbindingid) | 客户端 | 发现原生调用，待核对 | — |
| [GetBindingModelID](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#getbindingmodelid) | 客户端 | 尚未建立映射 | — |
| [GetDuration](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#getduration) | 客户端 | 尚未建立映射 | — |
| [GetFacingMode](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#getfacingmode) | 客户端 | 尚未建立映射 | — |
| [GetLoopAge](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#getloopage) | 客户端 | 尚未建立映射 | — |
| [GetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#getpos) | 客户端 | 发现原生调用，待核对 | — |
| [GetRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#getrot) | 客户端 | 发现原生调用，待核对 | — |
| [GetSleepDuration](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#getsleepduration) | 客户端 | 尚未建立映射 | — |
| [GetTimeScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#gettimescale) | 客户端 | 尚未建立映射 | — |
| [GetVariable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#getvariable) | 客户端 | 发现原生调用，待核对 | — |
| [Hide](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#hide) | 客户端 | 尚未建立映射 | — |
| [IsHiding](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#ishiding) | 客户端 | 尚未建立映射 | — |
| [IsPausing](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#ispausing) | 客户端 | 尚未建立映射 | — |
| [Pause](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#pause) | 客户端 | 发现原生调用，待核对 | — |
| [Play](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#play) | 客户端 | 尚未建立映射 | — |
| [PlayAt](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#playat) | 客户端 | 尚未建立映射 | — |
| [Remove](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#remove) | 客户端 | 发现原生调用，待核对 | — |
| [RemoveByName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#removebyname) | 客户端 | 尚未建立映射 | — |
| [Replay](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#replay) | 客户端 | 尚未建立映射 | — |
| [Resume](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#resume) | 客户端 | 发现原生调用，待核对 | — |
| [SetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#setpos) | 客户端 | 尚未建立映射 | — |
| [SetRelative](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#setrelative) | 客户端 | 尚未建立映射 | — |
| [SetRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#setrot) | 客户端 | 发现原生调用，待核对 | — |
| [SetRotUseZXY](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#setrotusezxy) | 客户端 | 尚未建立映射 | — |
| [SetTimeScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#settimescale) | 客户端 | 尚未建立映射 | — |
| [SetVariable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#setvariable) | 客户端 | 发现原生调用，待核对 | — |
| [Show](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#show) | 客户端 | 尚未建立映射 | — |
| [Stop](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#stop) | 客户端 | 尚未建立映射 | — |
| [Unbind](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E7%89%B9%E6%95%88/%E5%BE%AE%E8%BD%AF%E7%B2%92%E5%AD%90.md#unbind) | 客户端 | 尚未建立映射 | — |

</div>

## 模型

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [BindItemToBone](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#binditemtobone) | 客户端 | 尚未建立映射 | — |
| [BindModelToEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#bindmodeltoentity) | 客户端 | 尚未建立映射 | — |
| [BindModelToModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#bindmodeltomodel) | 客户端 | 尚未建立映射 | — |
| [CancelAllBoneMask](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#cancelallbonemask) | 客户端 | 尚未建立映射 | — |
| [CreateFreeModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#createfreemodel) | 客户端 | 尚未建立映射 | — |
| [GetAllBindModelToEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#getallbindmodeltoentity) | 客户端 | 尚未建立映射 | — |
| [GetAnimLength](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#getanimlength) | 客户端 | 尚未建立映射 | — |
| [GetBonePositionFromMinecraftObject](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#getbonepositionfromminecraftobject) | 客户端 | 尚未建立映射 | — |
| [GetBoneWorldPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#getboneworldpos) | 客户端 | 尚未建立映射 | — |
| [GetEntityBoneWorldPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#getentityboneworldpos) | 客户端 | 尚未建立映射 | — |
| [GetEntityScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#getentityscale) | 服务端 | 尚未建立映射 | — |
| [GetExtraUniformValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#getextrauniformvalue) | 客户端 | 尚未建立映射 | — |
| [GetModelId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#getmodelid) | 客户端 | 尚未建立映射 | — |
| [GetModelMaterial](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#getmodelmaterial) | 客户端 | 尚未建立映射 | — |
| [GetModelName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#getmodelname) | 服务端 | 尚未建立映射 | — |
| [GetModelStyle](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#getmodelstyle) | 客户端 | 尚未建立映射 | — |
| [GetPlayingAnimList](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#getplayinganimlist) | 客户端 | 尚未建立映射 | — |
| [GetTexture](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#gettexture) | 客户端 | 尚未建立映射 | — |
| [HideModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#hidemodel) | 客户端 | 尚未建立映射 | — |
| [ModelPlayAni](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#modelplayani) | 客户端 | 尚未建立映射 | — |
| [ModelStopAni](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#modelstopani) | 客户端 | 尚未建立映射 | — |
| [PlayAnim](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#playanim) | 客户端 | 尚未建立映射 | — |
| [RegisterAnim1DControlParam](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#registeranim1dcontrolparam) | 客户端 | 尚未建立映射 | — |
| [RegisterAnim1DMultiControlParam](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#registeranim1dmulticontrolparam) | 客户端 | 尚未建立映射 | — |
| [RemoveAnim1DMultiControlParam](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#removeanim1dmulticontrolparam) | 客户端 | 尚未建立映射 | — |
| [RemoveFreeModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#removefreemodel) | 客户端 | 尚未建立映射 | — |
| [ResetModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#resetmodel) | 客户端 | 尚未建立映射 | — |
| [SetAnim1DControlParam](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setanim1dcontrolparam) | 客户端 | 尚未建立映射 | — |
| [SetAnim1DMultiControlParam](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setanim1dmulticontrolparam) | 客户端 | 尚未建立映射 | — |
| [SetAnimLayer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setanimlayer) | 客户端 | 尚未建立映射 | — |
| [SetAnimSpeed](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setanimspeed) | 客户端 | 尚未建立映射 | — |
| [SetAnimationAllBoneMask](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setanimationallbonemask) | 客户端 | 尚未建立映射 | — |
| [SetAnimationBoneMask](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setanimationbonemask) | 客户端 | 尚未建立映射 | — |
| [SetBrightness](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setbrightness) | 客户端 | 尚未建立映射 | — |
| [SetEntityOpacity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setentityopacity) | 客户端 | 尚未建立映射 | — |
| [SetEntityScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setentityscale) | 服务端 | 尚未建立映射 | — |
| [SetEntityShadowShow](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setentityshadowshow) | 客户端 | 尚未建立映射 | — |
| [SetExtraUniformValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setextrauniformvalue) | 客户端 | 尚未建立映射 | — |
| [SetFreeModelAniSpeed](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setfreemodelanispeed) | 客户端 | 尚未建立映射 | — |
| [SetFreeModelBoundingBox](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setfreemodelboundingbox) | 客户端 | 尚未建立映射 | — |
| [SetFreeModelPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setfreemodelpos) | 客户端 | 尚未建立映射 | — |
| [SetFreeModelRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setfreemodelrot) | 客户端 | 尚未建立映射 | — |
| [SetFreeModelScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setfreemodelscale) | 客户端 | 尚未建立映射 | — |
| [SetLegacyBindRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setlegacybindrot) | 客户端 | 尚未建立映射 | — |
| [SetModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setmodel) | 服务端 | 尚未建立映射 | — |
| [SetModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setmodel) | 客户端 | 尚未建立映射 | — |
| [SetModelMaterial](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setmodelmaterial) | 客户端 | 尚未建立映射 | — |
| [SetModelMultiPassMaterial](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setmodelmultipassmaterial) | 客户端 | 尚未建立映射 | — |
| [SetModelOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setmodeloffset) | 服务端 | 尚未建立映射 | — |
| [SetModelOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setmodeloffset) | 客户端 | 尚未建立映射 | — |
| [SetModelPartVisible](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setmodelpartvisible) | 客户端 | 尚未建立映射 | — |
| [SetModelPerspectiveEffect](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setmodelperspectiveeffect) | 客户端 | 尚未建立映射 | — |
| [SetModelTexture](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setmodeltexture) | 服务端 | 尚未建立映射 | — |
| [SetShowArmModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#setshowarmmodel) | 客户端 | 尚未建立映射 | — |
| [SetTexture](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#settexture) | 客户端 | 尚未建立映射 | — |
| [ShowCommonHurtColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#showcommonhurtcolor) | 服务端 | 尚未建立映射 | — |
| [ShowCommonHurtColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#showcommonhurtcolor) | 客户端 | 尚未建立映射 | — |
| [ShowModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#showmodel) | 客户端 | 尚未建立映射 | — |
| [UnBindModelToEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#unbindmodeltoentity) | 客户端 | 尚未建立映射 | — |
| [UnBindModelToModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%A8%A1%E5%9E%8B.md#unbindmodeltomodel) | 客户端 | 尚未建立映射 | — |

</div>

## 原生UI

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [ChangeSneakState](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#changesneakstate) | 客户端 | 尚未建立映射 | — |
| [ClickInteractGUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#clickinteractgui) | 客户端 | 尚未建立映射 | — |
| [GetOriginAreaOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#getoriginareaoffset) | 客户端 | 尚未建立映射 | — |
| [GetScreenSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#getscreensize) | 客户端 | 发现原生调用，待核对 | — |
| [GetScreenViewInfo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#getscreenviewinfo) | 客户端 | 尚未建立映射 | — |
| [GetWalkState](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#getwalkstate) | 客户端 | 尚未建立映射 | — |
| [HideAirSupplyGUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hideairsupplygui) | 客户端 | 尚未建立映射 | — |
| [HideArmorGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidearmorgui) | 客户端 | 尚未建立映射 | — |
| [HideChangePersonGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidechangepersongui) | 客户端 | 尚未建立映射 | — |
| [HideChatGUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidechatgui) | 客户端 | 尚未建立映射 | — |
| [HideCrossHairGUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidecrosshairgui) | 客户端 | 尚未建立映射 | — |
| [HideEmoteGUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hideemotegui) | 客户端 | 尚未建立映射 | — |
| [HideExpGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hideexpgui) | 客户端 | 尚未建立映射 | — |
| [HideFoldGUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidefoldgui) | 客户端 | 尚未建立映射 | — |
| [HideHealthGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidehealthgui) | 客户端 | 尚未建立映射 | — |
| [HideHorseHealthGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidehorsehealthgui) | 客户端 | 尚未建立映射 | — |
| [HideHudGUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidehudgui) | 客户端 | 尚未建立映射 | — |
| [HideHungerGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidehungergui) | 客户端 | 尚未建立映射 | — |
| [HideInteractGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hideinteractgui) | 客户端 | 尚未建立映射 | — |
| [HideJumpGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidejumpgui) | 客户端 | 尚未建立映射 | — |
| [HideMoveGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidemovegui) | 客户端 | 尚未建立映射 | — |
| [HideNeteaseStoreGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hideneteasestoregui) | 客户端 | 尚未建立映射 | — |
| [HidePauseGUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidepausegui) | 客户端 | 尚未建立映射 | — |
| [HideSlotBarGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hideslotbargui) | 客户端 | 尚未建立映射 | — |
| [HideSneakGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidesneakgui) | 客户端 | 尚未建立映射 | — |
| [HideSwimGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hideswimgui) | 客户端 | 尚未建立映射 | — |
| [HideVoiceGUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidevoicegui) | 客户端 | 尚未建立映射 | — |
| [HideWalkGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#hidewalkgui) | 客户端 | 尚未建立映射 | — |
| [OpenChatGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#openchatgui) | 客户端 | 尚未建立映射 | — |
| [OpenEmoteGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#openemotegui) | 客户端 | 尚未建立映射 | — |
| [OpenFoldGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#openfoldgui) | 客户端 | 尚未建立映射 | — |
| [OpenInventoryGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#openinventorygui) | 客户端 | 尚未建立映射 | — |
| [OpenNeteaseStoreGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#openneteasestoregui) | 客户端 | 尚未建立映射 | — |
| [OpenPauseGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#openpausegui) | 客户端 | 尚未建立映射 | — |
| [OpenReportGui](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#openreportgui) | 客户端 | 尚未建立映射 | — |
| [PlayHudHeartBlinkAnim](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#playhudheartblinkanim) | 客户端 | 尚未建立映射 | — |
| [SetCrossHair](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#setcrosshair) | 客户端 | 尚未建立映射 | — |
| [SetEmoteSwitch](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#setemoteswitch) | 客户端 | 尚未建立映射 | — |
| [SetHudChatStackPosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#sethudchatstackposition) | 客户端 | 尚未建立映射 | — |
| [SetHudChatStackVisible](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#sethudchatstackvisible) | 客户端 | 尚未建立映射 | — |
| [SetResponse](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#setresponse) | 客户端 | 尚未建立映射 | — |
| [SimulateJump](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%8E%9F%E7%94%9FUI.md#simulatejump) | 客户端 | 尚未建立映射 | — |

</div>

## 自定义UI / 通用

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CheckCanBindUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#checkcanbindui) | 客户端 | 尚未建立映射 | — |
| [CreateUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#createui) | 客户端 | 已有离线核验路径 | [UiService.createHud](ui/reference/UiService.md#createHud) |
| [EnableFontBatchRender](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#enablefontbatchrender) | 客户端 | 尚未建立映射 | — |
| [GetCustomUIControlProxyCls](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#getcustomuicontrolproxycls) | 客户端 | 尚未建立映射 | — |
| [GetMiniMapScreenNodeCls](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#getminimapscreennodecls) | 客户端 | 已有离线核验路径 | [UiService.openView](ui/reference/UiService.md#openView), [UiService.createHud](ui/reference/UiService.md#createHud) |
| [GetNativeScreenManagerCls](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#getnativescreenmanagercls) | 客户端 | 尚未建立映射 | — |
| [GetScreenNodeCls](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#getscreennodecls) | 客户端 | 发现原生调用，待核对 | — |
| [GetTopScreen](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#gettopscreen) | 客户端 | 已有离线核验路径 | [UiService.currentView](ui/reference/UiService.md#currentView) |
| [GetTopUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#gettopui) | 客户端 | 发现原生调用，待核对 | — |
| [GetTopUINode](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#gettopuinode) | 客户端 | 尚未建立映射 | — |
| [GetUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#getui) | 客户端 | 尚未建立映射 | — |
| [GetUIScreenProxyCls](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#getuiscreenproxycls) | 客户端 | 尚未建立映射 | — |
| [GetViewBinderCls](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#getviewbindercls) | 客户端 | 发现原生调用，待核对 | — |
| [GetViewViewRequestCls](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#getviewviewrequestcls) | 客户端 | 尚未建立映射 | — |
| [OpenDeveloperHomeWindow](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#opendeveloperhomewindow) | 客户端 | 尚未建立映射 | — |
| [OpenResourceCenterDetailWindow](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#openresourcecenterdetailwindow) | 客户端 | 尚未建立映射 | — |
| [PopScreen](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#popscreen) | 客户端 | 发现原生调用，待核对 | — |
| [PopTopUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#poptopui) | 客户端 | 尚未建立映射 | — |
| [PushScreen](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#pushscreen) | 客户端 | 已有离线核验路径 | [UiService.openView](ui/reference/UiService.md#openView) |
| [RegisterUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#registerui) | 客户端 | 已有离线核验路径 | [UiService.registerView](ui/reference/UiService.md#registerView), [UiService.openView](ui/reference/UiService.md#openView) |
| [RegisterUIAnimations](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#registeruianimations) | 客户端 | 已有离线核验路径 | [UiControl.animate](ui/reference/UiControl.md#animate) |
| [UnregisterUIAnimation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8.md#unregisteruianimation) | 客户端 | 已有离线核验路径 | [UiAnimation.dispose](ui/reference/UiAnimation.md#dispose) |

</div>

## 自定义UI / 自定义书本

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetBookManager](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E8%87%AA%E5%AE%9A%E4%B9%89%E4%B9%A6%E6%9C%AC.md#getbookmanager) | 客户端 | 尚未建立映射 | — |

</div>

## 自定义UI / 自定义成就系统

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddNodeProgress](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%88%90%E5%B0%B1%E7%B3%BB%E7%BB%9F.md#addnodeprogress) | 服务端 | 尚未建立映射 | — |
| [GetAchievementGatePosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%88%90%E5%B0%B1%E7%B3%BB%E7%BB%9F.md#getachievementgateposition) | 客户端 | 尚未建立映射 | — |
| [GetChildrenNode](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%88%90%E5%B0%B1%E7%B3%BB%E7%BB%9F.md#getchildrennode) | 服务端 | 尚未建立映射 | — |
| [GetNodeDetailInfo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%88%90%E5%B0%B1%E7%B3%BB%E7%BB%9F.md#getnodedetailinfo) | 服务端 | 尚未建立映射 | — |
| [SetAchievementGatePosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%88%90%E5%B0%B1%E7%B3%BB%E7%BB%9F.md#setachievementgateposition) | 客户端 | 尚未建立映射 | — |
| [SetNodeFinish](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E8%87%AA%E5%AE%9A%E4%B9%89%E6%88%90%E5%B0%B1%E7%B3%BB%E7%BB%9F.md#setnodefinish) | 服务端 | 尚未建立映射 | — |

</div>

## 自定义UI / UI界面

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [BindVirtualWorldModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#bindvirtualworldmodel) | 客户端 | 尚未建立映射 | — |
| [ChangeBindAutoScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#changebindautoscale) | 客户端 | 尚未建立映射 | — |
| [ChangeBindEntityId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#changebindentityid) | 客户端 | 尚未建立映射 | — |
| [ChangeBindOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#changebindoffset) | 客户端 | 尚未建立映射 | — |
| [Clone](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#clone) | 客户端 | 发现原生调用，待核对 | — |
| [Create](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#create) | 客户端 | 发现原生调用，待核对 | — |
| [CreateChildControl](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#createchildcontrol) | 客户端 | 已有离线核验路径 | [UiView.createControl](ui/reference/UiView.md#createControl) |
| [Destroy](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#destroy) | 客户端 | 发现原生调用，待核对 | — |
| [GetAllChildrenPath](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#getallchildrenpath) | 客户端 | 已有离线核验路径 | [UiControl.getChildren](ui/reference/UiControl.md#getChildren) |
| [GetBaseUIControl](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#getbaseuicontrol) | 客户端 | 已有离线核验路径 | [UiView.getControl](ui/reference/UiView.md#getControl) |
| [GetBindAutoScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#getbindautoscale) | 客户端 | 尚未建立映射 | — |
| [GetBindEntityId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#getbindentityid) | 客户端 | 尚未建立映射 | — |
| [GetBindOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#getbindoffset) | 客户端 | 尚未建立映射 | — |
| [GetBindWorldPosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#getbindworldposition) | 客户端 | 尚未建立映射 | — |
| [GetChildrenName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#getchildrenname) | 客户端 | 已有离线核验路径 | [UiControl.getChildren](ui/reference/UiControl.md#getChildren) |
| [GetIsHud](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#getishud) | 客户端 | 尚未建立映射 | — |
| [GetRichTextItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#getrichtextitem) | 客户端 | 尚未建立映射 | — |
| [GetScreenName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#getscreenname) | 客户端 | 尚未建立映射 | — |
| [GetSelf](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#getself) | 客户端 | 尚未建立映射 | — |
| [OnActive](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#onactive) | 客户端 | 尚未建立映射 | — |
| [OnDeactive](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#ondeactive) | 客户端 | 尚未建立映射 | — |
| [RemoveChildControl](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#removechildcontrol) | 客户端 | 已有离线核验路径 | [UiControl.remove](ui/reference/UiControl.md#remove) |
| [RemoveComponent](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#removecomponent) | 客户端 | 发现原生调用，待核对 | — |
| [SetBindWorldPosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#setbindworldposition) | 客户端 | 尚未建立映射 | — |
| [SetIsHud](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#setishud) | 客户端 | 尚未建立映射 | — |
| [SetRemove](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#setremove) | 客户端 | 已有离线核验路径 | [UiView.close](ui/reference/UiView.md#close) |
| [SetScreenVisible](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#setscreenvisible) | 客户端 | 已有离线核验路径 | [UiView.setVisible](ui/reference/UiView.md#setVisible) |
| [SetSelectControl](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#setselectcontrol) | 客户端 | 已有离线核验路径 | [UiControl.focus](ui/reference/UiControl.md#focus), [UiControl.blur](ui/reference/UiControl.md#blur) |
| [SetStackGridCount](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#setstackgridcount) | 客户端 | 尚未建立映射 | — |
| [SetUiEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#setuientity) | 客户端 | 尚未建立映射 | — |
| [SetUiModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#setuimodel) | 客户端 | 尚未建立映射 | — |
| [SetUiModelScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#setuimodelscale) | 客户端 | 尚未建立映射 | — |
| [Update](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#update) | 客户端 | 发现原生调用，待核对 | — |
| [UpdateScreen](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E7%95%8C%E9%9D%A2.md#updatescreen) | 客户端 | 已有离线核验路径 | [UiView.refresh](ui/reference/UiView.md#refresh) |

</div>

## 自定义UI / UI控件

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddEntityMarker](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#addentitymarker) | 客户端 | 已有离线核验路径 | [UiMiniMap.addMarker](ui/reference/UiMiniMap.md#addMarker) |
| [AddEntityTextMarker](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#addentitytextmarker) | 客户端 | 已有离线核验路径 | [UiMiniMap.addTextMarker](ui/reference/UiMiniMap.md#addTextMarker) |
| [AddHoverEventParams](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#addhovereventparams) | 客户端 | 已有离线核验路径 | [UiButton.afterEvents](ui/reference/UiButton.md#afterEvents) |
| [AddOption](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#addoption) | 客户端 | 已有离线核验路径 | [UiComboBox.addOption](ui/reference/UiComboBox.md#addOption) |
| [AddStaticMarker](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#addstaticmarker) | 客户端 | 已有离线核验路径 | [UiMiniMap.addMarker](ui/reference/UiMiniMap.md#addMarker) |
| [AddStaticTextMarker](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#addstatictextmarker) | 客户端 | 已有离线核验路径 | [UiMiniMap.addTextMarker](ui/reference/UiMiniMap.md#addTextMarker) |
| [AddTouchEventParams](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#addtoucheventparams) | 客户端 | 已有离线核验路径 | [UiButton.afterEvents](ui/reference/UiButton.md#afterEvents) |
| [ClearOptions](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#clearoptions) | 客户端 | 已有离线核验路径 | [UiComboBox.clearOptions](ui/reference/UiComboBox.md#clearOptions) |
| [ClearSelection](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#clearselection) | 客户端 | 已有离线核验路径 | [UiComboBox.selectedIndex](ui/reference/UiComboBox.md#selectedIndex) |
| [DisableTextShadow](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#disabletextshadow) | 客户端 | 已有离线核验路径 | [UiLabel.textShadow](ui/reference/UiLabel.md#textShadow) |
| [EnableTextShadow](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#enabletextshadow) | 客户端 | 已有离线核验路径 | [UiLabel.textShadow](ui/reference/UiLabel.md#textShadow) |
| [GetAnchorFrom](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getanchorfrom) | 客户端 | 已有离线核验路径 | [UiControl.anchorFrom](ui/reference/UiControl.md#anchorFrom), [UiControl.setAnchors](ui/reference/UiControl.md#setAnchors) |
| [GetAnchorTo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getanchorto) | 客户端 | 已有离线核验路径 | [UiControl.anchorTo](ui/reference/UiControl.md#anchorTo), [UiControl.setAnchors](ui/reference/UiControl.md#setAnchors) |
| [GetChildByName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getchildbyname) | 客户端 | 发现原生调用，待核对 | — |
| [GetChildByPath](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getchildbypath) | 客户端 | 发现原生调用，待核对 | — |
| [GetClipDirection](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getclipdirection) | 客户端 | 已有离线核验路径 | [UiImage.clipDirection](ui/reference/UiImage.md#clipDirection) |
| [GetClipOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getclipoffset) | 客户端 | 已有离线核验路径 | [UiControl.clipOffset](ui/reference/UiControl.md#clipOffset) |
| [GetClipsChildren](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getclipschildren) | 客户端 | 已有离线核验路径 | [UiControl.clipsChildren](ui/reference/UiControl.md#clipsChildren) |
| [GetCurrentSliceIndex](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getcurrentsliceindex) | 客户端 | 已有离线核验路径 | [UiSelectionWheel.selectedIndex](ui/reference/UiSelectionWheel.md#selectedIndex) |
| [GetEditText](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getedittext) | 客户端 | 已有离线核验路径 | [UiTextField.value](ui/reference/UiTextField.md#value) |
| [GetFullPosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getfullposition) | 客户端 | 已有离线核验路径 | [UiControl.setLayout](ui/reference/UiControl.md#setLayout) |
| [GetFullSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getfullsize) | 客户端 | 已有离线核验路径 | [UiControl.setLayout](ui/reference/UiControl.md#setLayout) |
| [GetGlobalPosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getglobalposition) | 客户端 | 已有离线核验路径 | [UiControl.globalPosition](ui/reference/UiControl.md#globalPosition) |
| [GetGlobalRotateAngle](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getglobalrotateangle) | 客户端 | 已有离线核验路径 | [UiImage.rotateAround](ui/reference/UiImage.md#rotateAround), [UiImage.orbitRotation](ui/reference/UiImage.md#orbitRotation), [UiImage.orbitPoint](ui/reference/UiImage.md#orbitPoint) |
| [GetGlobalRotatePoint](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getglobalrotatepoint) | 客户端 | 已有离线核验路径 | [UiImage.rotateAround](ui/reference/UiImage.md#rotateAround), [UiImage.orbitRotation](ui/reference/UiImage.md#orbitRotation), [UiImage.orbitPoint](ui/reference/UiImage.md#orbitPoint) |
| [GetGridItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getgriditem) | 客户端 | 已有离线核验路径 | [UiGrid.getItem](ui/reference/UiGrid.md#getItem), [UiGrid.setDimensions](ui/reference/UiGrid.md#setDimensions) |
| [GetIsModal](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getismodal) | 客户端 | 已有离线核验路径 | [UiInputPanel.isModal](ui/reference/UiInputPanel.md#isModal) |
| [GetIsSwallow](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getisswallow) | 客户端 | 已有离线核验路径 | [UiInputPanel.swallowInput](ui/reference/UiInputPanel.md#swallowInput) |
| [GetMaxSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getmaxsize) | 客户端 | 已有离线核验路径 | [UiControl.maximumSize](ui/reference/UiControl.md#maximumSize) |
| [GetMinSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getminsize) | 客户端 | 已有离线核验路径 | [UiControl.minimumSize](ui/reference/UiControl.md#minimumSize) |
| [GetModelId](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getmodelid) | 客户端 | 尚未建立映射 | — |
| [GetOffsetDelta](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getoffsetdelta) | 客户端 | 已有离线核验路径 | [UiInputPanel.dragOffset](ui/reference/UiInputPanel.md#dragOffset) |
| [GetOptionCount](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getoptioncount) | 客户端 | 已有离线核验路径 | [UiComboBox.optionCount](ui/reference/UiComboBox.md#optionCount) |
| [GetOptionIndexByShowName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getoptionindexbyshowname) | 客户端 | 已有离线核验路径 | [UiComboBox.findOption](ui/reference/UiComboBox.md#findOption) |
| [GetOptionShowNameByIndex](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getoptionshownamebyindex) | 客户端 | 已有离线核验路径 | [UiComboBox.getOptionLabel](ui/reference/UiComboBox.md#getOptionLabel) |
| [GetOrientation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getorientation) | 客户端 | 已有离线核验路径 | [UiStackPanel.orientation](ui/reference/UiStackPanel.md#orientation) |
| [GetPath](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getpath) | 客户端 | 发现原生调用，待核对 | — |
| [GetPosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getposition) | 客户端 | 已有离线核验路径 | [UiControl.position](ui/reference/UiControl.md#position) |
| [GetPropertyBag](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getpropertybag) | 客户端 | 已有离线核验路径 | [UiControl.getProperties](ui/reference/UiControl.md#getProperties) |
| [GetRotateAngle](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getrotateangle) | 客户端 | 已有离线核验路径 | [UiImage.rotation](ui/reference/UiImage.md#rotation), [UiImage.rotate](ui/reference/UiImage.md#rotate) |
| [GetRotatePivot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getrotatepivot) | 客户端 | 已有离线核验路径 | [UiImage.rotationPivot](ui/reference/UiImage.md#rotationPivot) |
| [GetRotateRect](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getrotaterect) | 客户端 | 尚未建立映射 | — |
| [GetScrollViewContentControl](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getscrollviewcontentcontrol) | 客户端 | 已有离线核验路径 | [UiScrollView.content](ui/reference/UiScrollView.md#content) |
| [GetScrollViewContentPath](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getscrollviewcontentpath) | 客户端 | 发现原生调用，待核对 | — |
| [GetScrollViewPercentValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getscrollviewpercentvalue) | 客户端 | 已有离线核验路径 | [UiScrollView.progress](ui/reference/UiScrollView.md#progress) |
| [GetScrollViewPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getscrollviewpos) | 客户端 | 已有离线核验路径 | [UiScrollView.scrollOffset](ui/reference/UiScrollView.md#scrollOffset) |
| [GetSelectOptionIndex](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getselectoptionindex) | 客户端 | 已有离线核验路径 | [UiComboBox.selectedIndex](ui/reference/UiComboBox.md#selectedIndex) |
| [GetSelectOptionShowName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getselectoptionshowname) | 客户端 | 已有离线核验路径 | [UiComboBox.selectedLabel](ui/reference/UiComboBox.md#selectedLabel) |
| [GetSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getsize) | 客户端 | 已有离线核验路径 | [UiControl.size](ui/reference/UiControl.md#size) |
| [GetSliceCount](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getslicecount) | 客户端 | 已有离线核验路径 | [UiSelectionWheel.sliceCount](ui/reference/UiSelectionWheel.md#sliceCount) |
| [GetSliderValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getslidervalue) | 客户端 | 已有离线核验路径 | [UiSlider.value](ui/reference/UiSlider.md#value) |
| [GetText](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#gettext) | 客户端 | 已有离线核验路径 | [UiLabel.text](ui/reference/UiLabel.md#text) |
| [GetTextAlignment](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#gettextalignment) | 客户端 | 已有离线核验路径 | [UiLabel.textAlignment](ui/reference/UiLabel.md#textAlignment) |
| [GetTextColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#gettextcolor) | 客户端 | 已有离线核验路径 | [UiLabel.color](ui/reference/UiLabel.md#color) |
| [GetTextLinePadding](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#gettextlinepadding) | 客户端 | 已有离线核验路径 | [UiLabel.lineSpacing](ui/reference/UiLabel.md#lineSpacing) |
| [GetToggleState](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#gettogglestate) | 客户端 | 已有离线核验路径 | [UiToggle.value](ui/reference/UiToggle.md#value) |
| [GetUiItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getuiitem) | 客户端 | 已有离线核验路径 | [UiItemRenderer.item](ui/reference/UiItemRenderer.md#item), [UiItemRenderer.setItem](ui/reference/UiItemRenderer.md#setItem) |
| [GetVisible](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#getvisible) | 客户端 | 已有离线核验路径 | [UiControl.visible](ui/reference/UiControl.md#visible) |
| [IsAnimEndCallbackRegistered](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#isanimendcallbackregistered) | 客户端 | 尚未建立映射 | — |
| [IsTextShadowEnabled](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#istextshadowenabled) | 客户端 | 已有离线核验路径 | [UiLabel.textShadow](ui/reference/UiLabel.md#textShadow) |
| [PauseAnimation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#pauseanimation) | 客户端 | 已有离线核验路径 | [UiAnimation.pause](ui/reference/UiAnimation.md#pause) |
| [PlayAnimation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#playanimation) | 客户端 | 已有离线核验路径 | [UiControl.animate](ui/reference/UiControl.md#animate), [UiAnimation.play](ui/reference/UiAnimation.md#play) |
| [RegisterCloseComboBoxCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#registerclosecomboboxcallback) | 客户端 | 已有离线核验路径 | [UiComboBox.afterEvents](ui/reference/UiComboBox.md#afterEvents) |
| [RegisterOpenComboBoxCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#registeropencomboboxcallback) | 客户端 | 已有离线核验路径 | [UiComboBox.afterEvents](ui/reference/UiComboBox.md#afterEvents) |
| [RegisterSelectItemCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#registerselectitemcallback) | 客户端 | 已有离线核验路径 | [UiComboBox.afterEvents](ui/reference/UiComboBox.md#afterEvents) |
| [RemoveAnimEndCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#removeanimendcallback) | 客户端 | 已有离线核验路径 | [UiAnimation.cancel](ui/reference/UiAnimation.md#cancel) |
| [RemoveAnimation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#removeanimation) | 客户端 | 已有离线核验路径 | [UiAnimation.cancel](ui/reference/UiAnimation.md#cancel) |
| [RemoveEntityMarker](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#removeentitymarker) | 客户端 | 已有离线核验路径 | [UiMapMarker.remove](ui/reference/UiMapMarker.md#remove) |
| [RemoveEntityTextMarker](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#removeentitytextmarker) | 客户端 | 已有离线核验路径 | [UiMapMarker.remove](ui/reference/UiMapMarker.md#remove) |
| [RemoveOptionByIndex](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#removeoptionbyindex) | 客户端 | 已有离线核验路径 | [UiComboBox.removeOption](ui/reference/UiComboBox.md#removeOption) |
| [RemoveOptionByShowName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#removeoptionbyshowname) | 客户端 | 已有离线核验路径 | [UiComboBox.removeOption](ui/reference/UiComboBox.md#removeOption) |
| [RemoveStaticMarker](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#removestaticmarker) | 客户端 | 已有离线核验路径 | [UiMapMarker.remove](ui/reference/UiMapMarker.md#remove) |
| [RemoveStaticTextMarker](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#removestatictextmarker) | 客户端 | 已有离线核验路径 | [UiMapMarker.remove](ui/reference/UiMapMarker.md#remove) |
| [RenderBlockGeometryModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#renderblockgeometrymodel) | 客户端 | 已有离线核验路径 | [UiModelRenderer.setBlockGeometry](ui/reference/UiModelRenderer.md#setBlockGeometry) |
| [RenderEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#renderentity) | 客户端 | 已有离线核验路径 | [UiModelRenderer.setEntity](ui/reference/UiModelRenderer.md#setEntity) |
| [RenderSkeletonModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#renderskeletonmodel) | 客户端 | 已有离线核验路径 | [UiModelRenderer.setSkeletonModel](ui/reference/UiModelRenderer.md#setSkeletonModel) |
| [RepaintMiniMap](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#repaintminimap) | 客户端 | 已有离线核验路径 | [UiMiniMap.refresh](ui/reference/UiMiniMap.md#refresh), [UiMiniMap.setHeightLimit](ui/reference/UiMiniMap.md#setHeightLimit) |
| [Rotate](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#rotate) | 客户端 | 已有离线核验路径 | [UiImage.rotation](ui/reference/UiImage.md#rotation), [UiImage.rotate](ui/reference/UiImage.md#rotate) |
| [RotateAround](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#rotatearound) | 客户端 | 已有离线核验路径 | [UiImage.rotateAround](ui/reference/UiImage.md#rotateAround), [UiImage.orbitRotation](ui/reference/UiImage.md#orbitRotation), [UiImage.orbitPoint](ui/reference/UiImage.md#orbitPoint) |
| [SetAlpha](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setalpha) | 客户端 | 已有离线核验路径 | [UiControl.setOpacity](ui/reference/UiControl.md#setOpacity) |
| [SetAnchorFrom](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setanchorfrom) | 客户端 | 已有离线核验路径 | [UiControl.anchorFrom](ui/reference/UiControl.md#anchorFrom), [UiControl.setAnchors](ui/reference/UiControl.md#setAnchors) |
| [SetAnchorTo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setanchorto) | 客户端 | 已有离线核验路径 | [UiControl.anchorTo](ui/reference/UiControl.md#anchorTo), [UiControl.setAnchors](ui/reference/UiControl.md#setAnchors) |
| [SetAnimEndCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setanimendcallback) | 客户端 | 已有离线核验路径 | [UiControl.animate](ui/reference/UiControl.md#animate) |
| [SetAnimation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setanimation) | 客户端 | 已有离线核验路径 | [UiControl.animate](ui/reference/UiControl.md#animate) |
| [SetButtonHoverInCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setbuttonhoverincallback) | 客户端 | 已有离线核验路径 | [UiButton.afterEvents](ui/reference/UiButton.md#afterEvents) |
| [SetButtonHoverOutCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setbuttonhoveroutcallback) | 客户端 | 发现原生调用，待核对 | — |
| [SetButtonScreenExitCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setbuttonscreenexitcallback) | 客户端 | 发现原生调用，待核对 | — |
| [SetButtonTouchCancelCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setbuttontouchcancelcallback) | 客户端 | 发现原生调用，待核对 | — |
| [SetButtonTouchDownCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setbuttontouchdowncallback) | 客户端 | 发现原生调用，待核对 | — |
| [SetButtonTouchMoveCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setbuttontouchmovecallback) | 客户端 | 发现原生调用，待核对 | — |
| [SetButtonTouchMoveInCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setbuttontouchmoveincallback) | 客户端 | 发现原生调用，待核对 | — |
| [SetButtonTouchMoveOutCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setbuttontouchmoveoutcallback) | 客户端 | 发现原生调用，待核对 | — |
| [SetButtonTouchUpCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setbuttontouchupcallback) | 客户端 | 已有离线核验路径 | [UiButton.afterEvents](ui/reference/UiButton.md#afterEvents) |
| [SetClipDirection](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setclipdirection) | 客户端 | 已有离线核验路径 | [UiImage.clipDirection](ui/reference/UiImage.md#clipDirection) |
| [SetClipOffset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setclipoffset) | 客户端 | 已有离线核验路径 | [UiControl.clipOffset](ui/reference/UiControl.md#clipOffset) |
| [SetClipsChildren](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setclipschildren) | 客户端 | 已有离线核验路径 | [UiControl.clipsChildren](ui/reference/UiControl.md#clipsChildren) |
| [SetCurrentSliceIndex](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setcurrentsliceindex) | 客户端 | 已有离线核验路径 | [UiSelectionWheel.selectedIndex](ui/reference/UiSelectionWheel.md#selectedIndex) |
| [SetEditText](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setedittext) | 客户端 | 已有离线核验路径 | [UiTextField.value](ui/reference/UiTextField.md#value) |
| [SetEditTextMaxLength](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setedittextmaxlength) | 客户端 | 发现原生调用，待核对 | — |
| [SetFullPosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setfullposition) | 客户端 | 已有离线核验路径 | [UiControl.setLayout](ui/reference/UiControl.md#setLayout) |
| [SetFullSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setfullsize) | 客户端 | 已有离线核验路径 | [UiControl.setLayout](ui/reference/UiControl.md#setLayout) |
| [SetGridDimension](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setgriddimension) | 客户端 | 已有离线核验路径 | [UiGrid.getItem](ui/reference/UiGrid.md#getItem), [UiGrid.setDimensions](ui/reference/UiGrid.md#setDimensions) |
| [SetHighestY](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#sethighesty) | 客户端 | 已有离线核验路径 | [UiMiniMap.setHeightLimit](ui/reference/UiMiniMap.md#setHeightLimit) |
| [SetHoverCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#sethovercallback) | 客户端 | 已有离线核验路径 | [UiSelectionWheel.afterEvents](ui/reference/UiSelectionWheel.md#afterEvents) |
| [SetImageAdaptionType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setimageadaptiontype) | 客户端 | 已有离线核验路径 | [UiImage.setImageFit](ui/reference/UiImage.md#setImageFit) |
| [SetIsModal](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setismodal) | 客户端 | 已有离线核验路径 | [UiInputPanel.isModal](ui/reference/UiInputPanel.md#isModal) |
| [SetIsSwallow](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setisswallow) | 客户端 | 已有离线核验路径 | [UiInputPanel.swallowInput](ui/reference/UiInputPanel.md#swallowInput) |
| [SetLayer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setlayer) | 客户端 | 已有离线核验路径 | [UiControl.setLayer](ui/reference/UiControl.md#setLayer) |
| [SetMaxSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setmaxsize) | 客户端 | 已有离线核验路径 | [UiControl.maximumSize](ui/reference/UiControl.md#maximumSize) |
| [SetMinSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setminsize) | 客户端 | 已有离线核验路径 | [UiControl.minimumSize](ui/reference/UiControl.md#minimumSize) |
| [SetOffsetDelta](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setoffsetdelta) | 客户端 | 已有离线核验路径 | [UiInputPanel.dragOffset](ui/reference/UiInputPanel.md#dragOffset) |
| [SetOrientation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setorientation) | 客户端 | 已有离线核验路径 | [UiStackPanel.orientation](ui/reference/UiStackPanel.md#orientation) |
| [SetPosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setposition) | 客户端 | 已有离线核验路径 | [UiControl.position](ui/reference/UiControl.md#position) |
| [SetPropertyBag](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setpropertybag) | 客户端 | 已有离线核验路径 | [UiControl.setProperties](ui/reference/UiControl.md#setProperties) |
| [SetRotatePivot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setrotatepivot) | 客户端 | 已有离线核验路径 | [UiImage.rotationPivot](ui/reference/UiImage.md#rotationPivot) |
| [SetScrollViewPercentValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setscrollviewpercentvalue) | 客户端 | 已有离线核验路径 | [UiScrollView.progress](ui/reference/UiScrollView.md#progress) |
| [SetScrollViewPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setscrollviewpos) | 客户端 | 已有离线核验路径 | [UiScrollView.scrollOffset](ui/reference/UiScrollView.md#scrollOffset) |
| [SetSelectOptionByIndex](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setselectoptionbyindex) | 客户端 | 已有离线核验路径 | [UiComboBox.selectedIndex](ui/reference/UiComboBox.md#selectedIndex) |
| [SetSelectOptionByShowName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setselectoptionbyshowname) | 客户端 | 已有离线核验路径 | [UiComboBox.selectLabel](ui/reference/UiComboBox.md#selectLabel) |
| [SetSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setsize) | 客户端 | 已有离线核验路径 | [UiControl.size](ui/reference/UiControl.md#size) |
| [SetSliderValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setslidervalue) | 客户端 | 已有离线核验路径 | [UiSlider.value](ui/reference/UiSlider.md#value) |
| [SetSprite](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setsprite) | 客户端 | 发现原生调用，待核对 | — |
| [SetSpriteClipRatio](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setspriteclipratio) | 客户端 | 发现原生调用，待核对 | — |
| [SetSpriteColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setspritecolor) | 客户端 | 已有离线核验路径 | [UiImage.setImage](ui/reference/UiImage.md#setImage) |
| [SetSpriteGray](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setspritegray) | 客户端 | 已有离线核验路径 | [UiImage.setImage](ui/reference/UiImage.md#setImage) |
| [SetSpritePlatformFrame](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setspriteplatformframe) | 客户端 | 尚未建立映射 | — |
| [SetSpritePlatformHead](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setspriteplatformhead) | 客户端 | 尚未建立映射 | — |
| [SetSpriteUV](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setspriteuv) | 客户端 | 已有离线核验路径 | [UiImage.setImage](ui/reference/UiImage.md#setImage) |
| [SetSpriteUVSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setspriteuvsize) | 客户端 | 已有离线核验路径 | [UiImage.setImage](ui/reference/UiImage.md#setImage) |
| [SetText](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#settext) | 客户端 | 已有离线核验路径 | [UiLabel.text](ui/reference/UiLabel.md#text) |
| [SetTextAlignment](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#settextalignment) | 客户端 | 已有离线核验路径 | [UiLabel.textAlignment](ui/reference/UiLabel.md#textAlignment) |
| [SetTextColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#settextcolor) | 客户端 | 已有离线核验路径 | [UiLabel.color](ui/reference/UiLabel.md#color) |
| [SetTextFontSize](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#settextfontsize) | 客户端 | 发现原生调用，待核对 | — |
| [SetTextLinePadding](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#settextlinepadding) | 客户端 | 已有离线核验路径 | [UiLabel.lineSpacing](ui/reference/UiLabel.md#lineSpacing) |
| [SetToggleState](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#settogglestate) | 客户端 | 已有离线核验路径 | [UiToggle.value](ui/reference/UiToggle.md#value) |
| [SetTouchEnable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#settouchenable) | 客户端 | 已有离线核验路径 | [UiControl.setEnabled](ui/reference/UiControl.md#setEnabled) |
| [SetTouchUpCallback](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#settouchupcallback) | 客户端 | 已有离线核验路径 | [UiSelectionWheel.afterEvents](ui/reference/UiSelectionWheel.md#afterEvents) |
| [SetUiItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setuiitem) | 客户端 | 已有离线核验路径 | [UiItemRenderer.item](ui/reference/UiItemRenderer.md#item), [UiItemRenderer.setItem](ui/reference/UiItemRenderer.md#setItem) |
| [SetValue](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setvalue) | 客户端 | 已有离线核验路径 | [UiProgressBar.setProgress](ui/reference/UiProgressBar.md#setProgress) |
| [SetVisible](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#setvisible) | 客户端 | 已有离线核验路径 | [UiControl.visible](ui/reference/UiControl.md#visible) |
| [StopAnimation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#stopanimation) | 客户端 | 尚未建立映射 | — |
| [ZoomIn](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#zoomin) | 客户端 | 已有离线核验路径 | [UiMiniMap.zoomIn](ui/reference/UiMiniMap.md#zoomIn) |
| [ZoomOut](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#zoomout) | 客户端 | 已有离线核验路径 | [UiMiniMap.zoomOut](ui/reference/UiMiniMap.md#zoomOut) |
| [ZoomReset](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#zoomreset) | 客户端 | 已有离线核验路径 | [UiMiniMap.resetZoom](ui/reference/UiMiniMap.md#resetZoom) |
| [asButton](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#asbutton) | 客户端 | 发现原生调用，待核对 | — |
| [asGrid](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#asgrid) | 客户端 | 已有离线核验路径 | [UiGrid.getItem](ui/reference/UiGrid.md#getItem), [UiGrid.setDimensions](ui/reference/UiGrid.md#setDimensions) |
| [asImage](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#asimage) | 客户端 | 发现原生调用，待核对 | — |
| [asInputPanel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#asinputpanel) | 客户端 | 已有离线核验路径 | [UiInputPanel.isModal](ui/reference/UiInputPanel.md#isModal), [UiInputPanel.swallowInput](ui/reference/UiInputPanel.md#swallowInput), [UiInputPanel.dragOffset](ui/reference/UiInputPanel.md#dragOffset) |
| [asItemRenderer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#asitemrenderer) | 客户端 | 已有离线核验路径 | [UiItemRenderer.item](ui/reference/UiItemRenderer.md#item), [UiItemRenderer.setItem](ui/reference/UiItemRenderer.md#setItem) |
| [asLabel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#aslabel) | 客户端 | 发现原生调用，待核对 | — |
| [asMiniMap](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#asminimap) | 客户端 | 已有离线核验路径 | [UiMiniMap](ui/reference/UiMiniMap.md) |
| [asNeteaseComboBox](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#asneteasecombobox) | 客户端 | 已有离线核验路径 | [UiComboBox](ui/reference/UiComboBox.md) |
| [asNeteasePaperDoll](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#asneteasepaperdoll) | 客户端 | 已有离线核验路径 | [UiModelRenderer.setEntity](ui/reference/UiModelRenderer.md#setEntity) |
| [asProgressBar](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#asprogressbar) | 客户端 | 已有离线核验路径 | [UiProgressBar.setProgress](ui/reference/UiProgressBar.md#setProgress) |
| [asScrollView](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#asscrollview) | 客户端 | 发现原生调用，待核对 | — |
| [asSelectionWheel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#asselectionwheel) | 客户端 | 已有离线核验路径 | [UiSelectionWheel](ui/reference/UiSelectionWheel.md) |
| [asSlider](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#asslider) | 客户端 | 发现原生调用，待核对 | — |
| [asStackPanel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#asstackpanel) | 客户端 | 已有离线核验路径 | [UiStackPanel.orientation](ui/reference/UiStackPanel.md#orientation) |
| [asSwitchToggle](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#asswitchtoggle) | 客户端 | 发现原生调用，待核对 | — |
| [asTextEditBox](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#astexteditbox) | 客户端 | 发现原生调用，待核对 | — |
| [resetAnimation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/UI%E6%8E%A7%E4%BB%B6.md#resetanimation) | 客户端 | 尚未建立映射 | — |

</div>

## 自定义UI / 通用设置

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CloseSettingUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8%E8%AE%BE%E7%BD%AE.md#closesettingui) | 客户端 | 尚未建立映射 | — |
| [GetSettingInst](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8%E8%AE%BE%E7%BD%AE.md#getsettinginst) | 客户端 | 尚未建立映射 | — |
| [OpenSettingUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8%E8%AE%BE%E7%BD%AE.md#opensettingui) | 客户端 | 尚未建立映射 | — |
| [RegisterSettingInst](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%87%AA%E5%AE%9A%E4%B9%89UI/%E9%80%9A%E7%94%A8%E8%AE%BE%E7%BD%AE.md#registersettinginst) | 客户端 | 尚未建立映射 | — |

</div>

## 音效

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [DisableOriginMusic](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%9F%B3%E6%95%88.md#disableoriginmusic) | 客户端 | 尚未建立映射 | — |
| [PlayCustomMusic](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%9F%B3%E6%95%88.md#playcustommusic) | 客户端 | 已有离线核验路径 | [Audio.playSound](client/reference/Audio.md#playSound) |
| [PlayCustomUIMusic](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%9F%B3%E6%95%88.md#playcustomuimusic) | 客户端 | 尚未建立映射 | — |
| [PlayGlobalCustomMusic](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%9F%B3%E6%95%88.md#playglobalcustommusic) | 客户端 | 已有离线核验路径 | [Audio.playMusic](client/reference/Audio.md#playMusic) |
| [SetCustomMusicLoop](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%9F%B3%E6%95%88.md#setcustommusicloop) | 客户端 | 尚未建立映射 | — |
| [SetCustomMusicLoopById](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%9F%B3%E6%95%88.md#setcustommusicloopbyid) | 客户端 | 尚未建立映射 | — |
| [StopCustomMusic](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%9F%B3%E6%95%88.md#stopcustommusic) | 客户端 | 发现原生调用，待核对 | — |
| [StopCustomMusicById](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E9%9F%B3%E6%95%88.md#stopcustommusicbyid) | 客户端 | 已有离线核验路径 | [SoundPlayback.stop](client/reference/SoundPlayback.md#stop) |

</div>

## 控制

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddPickBlacklist](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#addpickblacklist) | 客户端 | 尚未建立映射 | — |
| [ClearPickBlacklist](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#clearpickblacklist) | 客户端 | 尚未建立映射 | — |
| [GetChosen](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#getchosen) | 客户端 | 尚未建立映射 | — |
| [GetChosenEntity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#getchosenentity) | 客户端 | 尚未建立映射 | — |
| [GetHoldTimeThresholdInMs](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#getholdtimethresholdinms) | 客户端 | 已有离线核验路径 | [ClientInput.holdThresholdMilliseconds](client/reference/ClientInput.md#holdThresholdMilliseconds) |
| [GetInputVector](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#getinputvector) | 客户端 | 已有离线核验路径 | [ClientInput.getMovementVector](client/reference/ClientInput.md#getMovementVector) |
| [GetMousePosition](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#getmouseposition) | 客户端 | 已有离线核验路径 | [ClientInput.getMousePosition](client/reference/ClientInput.md#getMousePosition) |
| [GetTouchPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#gettouchpos) | 客户端 | 已有离线核验路径 | [ClientInput.getTouchPosition](client/reference/ClientInput.md#getTouchPosition) |
| [IsCanAttack](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#iscanattack) | 客户端 | 已有离线核验路径 | [ClientInput.getPermission](client/reference/ClientInput.md#getPermission), [ClientInput.getPermissions](client/reference/ClientInput.md#getPermissions) |
| [IsCanChat](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#iscanchat) | 客户端 | 已有离线核验路径 | [ClientInput.getPermission](client/reference/ClientInput.md#getPermission), [ClientInput.getPermissions](client/reference/ClientInput.md#getPermissions) |
| [IsCanDrag](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#iscandrag) | 客户端 | 已有离线核验路径 | [ClientInput.getPermission](client/reference/ClientInput.md#getPermission), [ClientInput.getPermissions](client/reference/ClientInput.md#getPermissions) |
| [IsCanInair](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#iscaninair) | 客户端 | 已有离线核验路径 | [ClientInput.getPermission](client/reference/ClientInput.md#getPermission), [ClientInput.getPermissions](client/reference/ClientInput.md#getPermissions) |
| [IsCanJump](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#iscanjump) | 客户端 | 已有离线核验路径 | [ClientInput.getPermission](client/reference/ClientInput.md#getPermission), [ClientInput.getPermissions](client/reference/ClientInput.md#getPermissions) |
| [IsCanMove](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#iscanmove) | 客户端 | 已有离线核验路径 | [ClientInput.getPermission](client/reference/ClientInput.md#getPermission), [ClientInput.getPermissions](client/reference/ClientInput.md#getPermissions) |
| [IsCanOpenInv](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#iscanopeninv) | 客户端 | 已有离线核验路径 | [ClientInput.getPermission](client/reference/ClientInput.md#getPermission), [ClientInput.getPermissions](client/reference/ClientInput.md#getPermissions) |
| [IsCanPause](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#iscanpause) | 客户端 | 已有离线核验路径 | [ClientInput.getPermission](client/reference/ClientInput.md#getPermission), [ClientInput.getPermissions](client/reference/ClientInput.md#getPermissions) |
| [IsCanPauseScreen](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#iscanpausescreen) | 客户端 | 已有离线核验路径 | [ClientInput.getPermission](client/reference/ClientInput.md#getPermission), [ClientInput.getPermissions](client/reference/ClientInput.md#getPermissions) |
| [IsCanPerspective](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#iscanperspective) | 客户端 | 已有离线核验路径 | [ClientInput.getPermission](client/reference/ClientInput.md#getPermission), [ClientInput.getPermissions](client/reference/ClientInput.md#getPermissions) |
| [IsCanScreenShot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#iscanscreenshot) | 客户端 | 已有离线核验路径 | [ClientInput.getPermission](client/reference/ClientInput.md#getPermission), [ClientInput.getPermissions](client/reference/ClientInput.md#getPermissions) |
| [IsCanWalkMode](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#iscanwalkmode) | 客户端 | 已有离线核验路径 | [ClientInput.getPermission](client/reference/ClientInput.md#getPermission), [ClientInput.getPermissions](client/reference/ClientInput.md#getPermissions) |
| [IsTouchWithMouse](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#istouchwithmouse) | 客户端 | 已有离线核验路径 | [ClientInput.isMouseEmulatingTouch](client/reference/ClientInput.md#isMouseEmulatingTouch) |
| [LockInputVector](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#lockinputvector) | 客户端 | 尚未建立映射 | — |
| [LockVerticalMove](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#lockverticalmove) | 客户端 | 尚未建立映射 | — |
| [PickFacing](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#pickfacing) | 客户端 | 尚未建立映射 | — |
| [SetCanAll](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcanall) | 客户端 | 尚未建立映射 | — |
| [SetCanAttack](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcanattack) | 客户端 | 已有离线核验路径 | [ClientInput.setPermission](client/reference/ClientInput.md#setPermission), [ClientInput.overridePermissions](client/reference/ClientInput.md#overridePermissions), [ClientInputOverride.dispose](client/reference/ClientInputOverride.md#dispose), [ClientInput.reset](client/reference/ClientInput.md#reset) |
| [SetCanChat](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcanchat) | 客户端 | 已有离线核验路径 | [ClientInput.setPermission](client/reference/ClientInput.md#setPermission), [ClientInput.overridePermissions](client/reference/ClientInput.md#overridePermissions), [ClientInputOverride.dispose](client/reference/ClientInputOverride.md#dispose), [ClientInput.reset](client/reference/ClientInput.md#reset) |
| [SetCanDrag](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcandrag) | 客户端 | 已有离线核验路径 | [ClientInput.setPermission](client/reference/ClientInput.md#setPermission), [ClientInput.overridePermissions](client/reference/ClientInput.md#overridePermissions), [ClientInputOverride.dispose](client/reference/ClientInputOverride.md#dispose), [ClientInput.reset](client/reference/ClientInput.md#reset) |
| [SetCanInair](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcaninair) | 客户端 | 已有离线核验路径 | [ClientInput.setPermission](client/reference/ClientInput.md#setPermission), [ClientInput.overridePermissions](client/reference/ClientInput.md#overridePermissions), [ClientInputOverride.dispose](client/reference/ClientInputOverride.md#dispose), [ClientInput.reset](client/reference/ClientInput.md#reset) |
| [SetCanJump](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcanjump) | 客户端 | 已有离线核验路径 | [ClientInput.setPermission](client/reference/ClientInput.md#setPermission), [ClientInput.overridePermissions](client/reference/ClientInput.md#overridePermissions), [ClientInputOverride.dispose](client/reference/ClientInputOverride.md#dispose), [ClientInput.reset](client/reference/ClientInput.md#reset) |
| [SetCanMove](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcanmove) | 客户端 | 已有离线核验路径 | [ClientInput.setPermission](client/reference/ClientInput.md#setPermission), [ClientInput.overridePermissions](client/reference/ClientInput.md#overridePermissions), [ClientInputOverride.dispose](client/reference/ClientInputOverride.md#dispose), [ClientInput.reset](client/reference/ClientInput.md#reset) |
| [SetCanOpenInv](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcanopeninv) | 客户端 | 已有离线核验路径 | [ClientInput.setPermission](client/reference/ClientInput.md#setPermission), [ClientInput.overridePermissions](client/reference/ClientInput.md#overridePermissions), [ClientInputOverride.dispose](client/reference/ClientInputOverride.md#dispose), [ClientInput.reset](client/reference/ClientInput.md#reset) |
| [SetCanPause](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcanpause) | 客户端 | 已有离线核验路径 | [ClientInput.setPermission](client/reference/ClientInput.md#setPermission), [ClientInput.overridePermissions](client/reference/ClientInput.md#overridePermissions), [ClientInputOverride.dispose](client/reference/ClientInputOverride.md#dispose), [ClientInput.reset](client/reference/ClientInput.md#reset) |
| [SetCanPauseScreen](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcanpausescreen) | 客户端 | 已有离线核验路径 | [ClientInput.setPermission](client/reference/ClientInput.md#setPermission), [ClientInput.overridePermissions](client/reference/ClientInput.md#overridePermissions), [ClientInputOverride.dispose](client/reference/ClientInputOverride.md#dispose), [ClientInput.reset](client/reference/ClientInput.md#reset) |
| [SetCanPerspective](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcanperspective) | 客户端 | 已有离线核验路径 | [ClientInput.setPermission](client/reference/ClientInput.md#setPermission), [ClientInput.overridePermissions](client/reference/ClientInput.md#overridePermissions), [ClientInputOverride.dispose](client/reference/ClientInputOverride.md#dispose), [ClientInput.reset](client/reference/ClientInput.md#reset) |
| [SetCanScreenShot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcanscreenshot) | 客户端 | 已有离线核验路径 | [ClientInput.setPermission](client/reference/ClientInput.md#setPermission), [ClientInput.overridePermissions](client/reference/ClientInput.md#overridePermissions), [ClientInputOverride.dispose](client/reference/ClientInputOverride.md#dispose), [ClientInput.reset](client/reference/ClientInput.md#reset) |
| [SetCanWalkMode](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcanwalkmode) | 客户端 | 已有离线核验路径 | [ClientInput.setPermission](client/reference/ClientInput.md#setPermission), [ClientInput.overridePermissions](client/reference/ClientInput.md#overridePermissions), [ClientInputOverride.dispose](client/reference/ClientInputOverride.md#dispose), [ClientInput.reset](client/reference/ClientInput.md#reset) |
| [SetControlMode](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcontrolmode) | 客户端 | 尚未建立映射 | — |
| [SetControlModeLock](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setcontrolmodelock) | 客户端 | 尚未建立映射 | — |
| [SetDeviceVibrate](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setdevicevibrate) | 客户端 | 尚未建立映射 | — |
| [SetGyroSensorReportRate](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setgyrosensorreportrate) | 客户端 | 尚未建立映射 | — |
| [SetHoldTimeThreshold](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setholdtimethreshold) | 客户端 | 已有离线核验路径 | [ClientInput.holdThresholdMilliseconds](client/reference/ClientInput.md#holdThresholdMilliseconds) |
| [SetMoveLock](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setmovelock) | 客户端 | 尚未建立映射 | — |
| [SetShowRideUI](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#setshowrideui) | 服务端 | 尚未建立映射 | — |
| [SimulateTouchWithMouse](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#simulatetouchwithmouse) | 客户端 | 尚未建立映射 | — |
| [ToggleGyroSensor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#togglegyrosensor) | 客户端 | 尚未建立映射 | — |
| [UnLockVerticalMove](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#unlockverticalmove) | 客户端 | 尚未建立映射 | — |
| [UnlockInputVector](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%8E%A7%E5%88%B6.md#unlockinputvector) | 客户端 | 尚未建立映射 | — |

</div>

## 游戏设置

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetControllerLayout](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B8%E6%88%8F%E8%AE%BE%E7%BD%AE.md#getcontrollerlayout) | 客户端 | 尚未建立映射 | — |
| [GetGamepadKeyMappings](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B8%E6%88%8F%E8%AE%BE%E7%BD%AE.md#getgamepadkeymappings) | 客户端 | 尚未建立映射 | — |
| [GetKeyMappings](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B8%E6%88%8F%E8%AE%BE%E7%BD%AE.md#getkeymappings) | 客户端 | 尚未建立映射 | — |
| [GetSliderOption](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B8%E6%88%8F%E8%AE%BE%E7%BD%AE.md#getslideroption) | 客户端 | 尚未建立映射 | — |
| [GetToggleOption](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B8%E6%88%8F%E8%AE%BE%E7%BD%AE.md#gettoggleoption) | 客户端 | 尚未建立映射 | — |
| [GetUIProfile](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B8%E6%88%8F%E8%AE%BE%E7%BD%AE.md#getuiprofile) | 客户端 | 尚未建立映射 | — |
| [HighlightBoxSelection](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B8%E6%88%8F%E8%AE%BE%E7%BD%AE.md#highlightboxselection) | 客户端 | 尚未建立映射 | — |
| [RegisterCustomGamepadMapping](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B8%E6%88%8F%E8%AE%BE%E7%BD%AE.md#registercustomgamepadmapping) | 客户端 | 尚未建立映射 | — |
| [RegisterCustomKeyMapping](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B8%E6%88%8F%E8%AE%BE%E7%BD%AE.md#registercustomkeymapping) | 客户端 | 尚未建立映射 | — |
| [SetSliderOption](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B8%E6%88%8F%E8%AE%BE%E7%BD%AE.md#setslideroption) | 客户端 | 尚未建立映射 | — |
| [SetSplitControlCanChange](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B8%E6%88%8F%E8%AE%BE%E7%BD%AE.md#setsplitcontrolcanchange) | 客户端 | 尚未建立映射 | — |
| [SetToggleOption](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B8%E6%88%8F%E8%AE%BE%E7%BD%AE.md#settoggleoption) | 客户端 | 尚未建立映射 | — |
| [SetUIProfile](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B8%E6%88%8F%E8%AE%BE%E7%BD%AE.md#setuiprofile) | 客户端 | 尚未建立映射 | — |

</div>

## 虚拟世界 / 世界

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [VirtualWorldCreate](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E4%B8%96%E7%95%8C.md#virtualworldcreate) | 客户端 | 尚未建立映射 | — |
| [VirtualWorldDestroy](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E4%B8%96%E7%95%8C.md#virtualworlddestroy) | 客户端 | 尚未建立映射 | — |
| [VirtualWorldSetCollidersVisible](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E4%B8%96%E7%95%8C.md#virtualworldsetcollidersvisible) | 客户端 | 尚未建立映射 | — |
| [VirtualWorldSetSkyBgColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E4%B8%96%E7%95%8C.md#virtualworldsetskybgcolor) | 客户端 | 尚未建立映射 | — |
| [VirtualWorldSetSkyTexture](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E4%B8%96%E7%95%8C.md#virtualworldsetskytexture) | 客户端 | 尚未建立映射 | — |
| [VirtualWorldToggleVisibility](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E4%B8%96%E7%95%8C.md#virtualworldtogglevisibility) | 客户端 | 尚未建立映射 | — |

</div>

## 虚拟世界 / 相机

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CameraGetClickModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E7%9B%B8%E6%9C%BA.md#cameragetclickmodel) | 客户端 | 尚未建立映射 | — |
| [CameraGetFov](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E7%9B%B8%E6%9C%BA.md#cameragetfov) | 客户端 | 尚未建立映射 | — |
| [CameraGetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E7%9B%B8%E6%9C%BA.md#cameragetpos) | 客户端 | 尚未建立映射 | — |
| [CameraGetZoom](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E7%9B%B8%E6%9C%BA.md#cameragetzoom) | 客户端 | 尚未建立映射 | — |
| [CameraLookAt](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E7%9B%B8%E6%9C%BA.md#cameralookat) | 客户端 | 尚未建立映射 | — |
| [CameraMoveTo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E7%9B%B8%E6%9C%BA.md#cameramoveto) | 客户端 | 尚未建立映射 | — |
| [CameraSetFov](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E7%9B%B8%E6%9C%BA.md#camerasetfov) | 客户端 | 尚未建立映射 | — |
| [CameraSetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E7%9B%B8%E6%9C%BA.md#camerasetpos) | 客户端 | 尚未建立映射 | — |
| [CameraSetZoom](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E7%9B%B8%E6%9C%BA.md#camerasetzoom) | 客户端 | 尚未建立映射 | — |
| [CameraStopActions](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E7%9B%B8%E6%9C%BA.md#camerastopactions) | 客户端 | 尚未建立映射 | — |

</div>

## 虚拟世界 / 模型

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [ModelCancelAllBoneMask](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelcancelallbonemask) | 客户端 | 尚未建立映射 | — |
| [ModelCreateMinecraftObject](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelcreateminecraftobject) | 客户端 | 尚未建立映射 | — |
| [ModelCreateObject](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelcreateobject) | 客户端 | 尚未建立映射 | — |
| [ModelGetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelgetpos) | 客户端 | 尚未建立映射 | — |
| [ModelGetRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelgetrot) | 客户端 | 尚未建立映射 | — |
| [ModelIsVisible](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelisvisible) | 客户端 | 尚未建立映射 | — |
| [ModelMoveTo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelmoveto) | 客户端 | 尚未建立映射 | — |
| [ModelPlayAnimation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelplayanimation) | 客户端 | 尚未建立映射 | — |
| [ModelRegisterAnim1DControlParam](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelregisteranim1dcontrolparam) | 客户端 | 尚未建立映射 | — |
| [ModelRemove](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelremove) | 客户端 | 尚未建立映射 | — |
| [ModelRotate](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelrotate) | 客户端 | 尚未建立映射 | — |
| [ModelRotateTo](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelrotateto) | 客户端 | 尚未建立映射 | — |
| [ModelSetAnim1DControlParam](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelsetanim1dcontrolparam) | 客户端 | 尚未建立映射 | — |
| [ModelSetAnimAllBoneMask](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelsetanimallbonemask) | 客户端 | 尚未建立映射 | — |
| [ModelSetAnimBoneMask](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelsetanimbonemask) | 客户端 | 尚未建立映射 | — |
| [ModelSetAnimLayer](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelsetanimlayer) | 客户端 | 尚未建立映射 | — |
| [ModelSetBoxCollider](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelsetboxcollider) | 客户端 | 尚未建立映射 | — |
| [ModelSetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelsetpos) | 客户端 | 尚未建立映射 | — |
| [ModelSetRot](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelsetrot) | 客户端 | 尚未建立映射 | — |
| [ModelSetScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelsetscale) | 客户端 | 尚未建立映射 | — |
| [ModelSetVisible](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelsetvisible) | 客户端 | 尚未建立映射 | — |
| [ModelStopActions](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelstopactions) | 客户端 | 尚未建立映射 | — |
| [ModelStopAnimation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelstopanimation) | 客户端 | 尚未建立映射 | — |
| [ModelUpdateAnimationMolangVariable](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E6%A8%A1%E5%9E%8B.md#modelupdateanimationmolangvariable) | 客户端 | 尚未建立映射 | — |

</div>

## 虚拟世界 / 其它对象

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [BindModel](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E5%85%B6%E5%AE%83%E5%AF%B9%E8%B1%A1.md#bindmodel) | 客户端 | 尚未建立映射 | — |
| [MoveToVirtualWorld](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%99%9A%E6%8B%9F%E4%B8%96%E7%95%8C/%E5%85%B6%E5%AE%83%E5%AF%B9%E8%B1%A1.md#movetovirtualworld) | 客户端 | 尚未建立映射 | — |

</div>

## 后处理 / 渐晕

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CheckVignetteEnabled](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E6%B8%90%E6%99%95.md#checkvignetteenabled) | 客户端 | 尚未建立映射 | — |
| [SetEnableVignette](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E6%B8%90%E6%99%95.md#setenablevignette) | 客户端 | 尚未建立映射 | — |
| [SetVignetteCenter](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E6%B8%90%E6%99%95.md#setvignettecenter) | 客户端 | 尚未建立映射 | — |
| [SetVignetteRGB](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E6%B8%90%E6%99%95.md#setvignettergb) | 客户端 | 尚未建立映射 | — |
| [SetVignetteRadius](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E6%B8%90%E6%99%95.md#setvignetteradius) | 客户端 | 尚未建立映射 | — |
| [SetVignetteSmoothness](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E6%B8%90%E6%99%95.md#setvignettesmoothness) | 客户端 | 尚未建立映射 | — |

</div>

## 后处理 / 模糊

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CheckGaussianBlurEnabled](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E6%A8%A1%E7%B3%8A.md#checkgaussianblurenabled) | 客户端 | 尚未建立映射 | — |
| [SetEnableGaussianBlur](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E6%A8%A1%E7%B3%8A.md#setenablegaussianblur) | 客户端 | 尚未建立映射 | — |
| [SetGaussianBlurRadius](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E6%A8%A1%E7%B3%8A.md#setgaussianblurradius) | 客户端 | 尚未建立映射 | — |

</div>

## 后处理 / 色彩

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CheckColorAdjustmentEnabled](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%89%B2%E5%BD%A9.md#checkcoloradjustmentenabled) | 客户端 | 尚未建立映射 | — |
| [SetColorAdjustmentBrightness](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%89%B2%E5%BD%A9.md#setcoloradjustmentbrightness) | 客户端 | 尚未建立映射 | — |
| [SetColorAdjustmentContrast](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%89%B2%E5%BD%A9.md#setcoloradjustmentcontrast) | 客户端 | 尚未建立映射 | — |
| [SetColorAdjustmentSaturation](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%89%B2%E5%BD%A9.md#setcoloradjustmentsaturation) | 客户端 | 尚未建立映射 | — |
| [SetColorAdjustmentTint](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%89%B2%E5%BD%A9.md#setcoloradjustmenttint) | 客户端 | 尚未建立映射 | — |
| [SetEnableColorAdjustment](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%89%B2%E5%BD%A9.md#setenablecoloradjustment) | 客户端 | 尚未建立映射 | — |

</div>

## 后处理 / 镜头效果

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CheckDepthOfFieldEnabled](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E9%95%9C%E5%A4%B4%E6%95%88%E6%9E%9C.md#checkdepthoffieldenabled) | 客户端 | 尚未建立映射 | — |
| [CheckLensStainEnabled](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E9%95%9C%E5%A4%B4%E6%95%88%E6%9E%9C.md#checklensstainenabled) | 客户端 | 尚未建立映射 | — |
| [ResetLensStainTexture](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E9%95%9C%E5%A4%B4%E6%95%88%E6%9E%9C.md#resetlensstaintexture) | 客户端 | 尚未建立映射 | — |
| [SetDepthOfFieldBlurRadius](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E9%95%9C%E5%A4%B4%E6%95%88%E6%9E%9C.md#setdepthoffieldblurradius) | 客户端 | 尚未建立映射 | — |
| [SetDepthOfFieldFarBlurScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E9%95%9C%E5%A4%B4%E6%95%88%E6%9E%9C.md#setdepthoffieldfarblurscale) | 客户端 | 尚未建立映射 | — |
| [SetDepthOfFieldFocusDistance](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E9%95%9C%E5%A4%B4%E6%95%88%E6%9E%9C.md#setdepthoffieldfocusdistance) | 客户端 | 尚未建立映射 | — |
| [SetDepthOfFieldNearBlurScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E9%95%9C%E5%A4%B4%E6%95%88%E6%9E%9C.md#setdepthoffieldnearblurscale) | 客户端 | 尚未建立映射 | — |
| [SetDepthOfFieldUseCenterFocus](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E9%95%9C%E5%A4%B4%E6%95%88%E6%9E%9C.md#setdepthoffieldusecenterfocus) | 客户端 | 尚未建立映射 | — |
| [SetEnableDepthOfField](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E9%95%9C%E5%A4%B4%E6%95%88%E6%9E%9C.md#setenabledepthoffield) | 客户端 | 尚未建立映射 | — |
| [SetEnableLensStain](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E9%95%9C%E5%A4%B4%E6%95%88%E6%9E%9C.md#setenablelensstain) | 客户端 | 尚未建立映射 | — |
| [SetLensStainColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E9%95%9C%E5%A4%B4%E6%95%88%E6%9E%9C.md#setlensstaincolor) | 客户端 | 尚未建立映射 | — |
| [SetLensStainIntensity](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E9%95%9C%E5%A4%B4%E6%95%88%E6%9E%9C.md#setlensstainintensity) | 客户端 | 尚未建立映射 | — |
| [SetLensStainTexture](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E9%95%9C%E5%A4%B4%E6%95%88%E6%9E%9C.md#setlensstaintexture) | 客户端 | 尚未建立映射 | — |

</div>

## 后处理 / 自定义

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddPostProcess](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%87%AA%E5%AE%9A%E4%B9%89.md#addpostprocess) | 客户端 | 尚未建立映射 | — |
| [CheckEnabledByName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%87%AA%E5%AE%9A%E4%B9%89.md#checkenabledbyname) | 客户端 | 尚未建立映射 | — |
| [GetParameter](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%87%AA%E5%AE%9A%E4%B9%89.md#getparameter) | 客户端 | 尚未建立映射 | — |
| [GetPostProcessOrder](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%87%AA%E5%AE%9A%E4%B9%89.md#getpostprocessorder) | 客户端 | 尚未建立映射 | — |
| [InsertPassToPostprocess](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%87%AA%E5%AE%9A%E4%B9%89.md#insertpasstopostprocess) | 客户端 | 尚未建立映射 | — |
| [PopBackPassInPostprocess](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%87%AA%E5%AE%9A%E4%B9%89.md#popbackpassinpostprocess) | 客户端 | 尚未建立映射 | — |
| [PostPassResultToOtherPass](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%87%AA%E5%AE%9A%E4%B9%89.md#postpassresulttootherpass) | 客户端 | 尚未建立映射 | — |
| [PushBackPassToPostprocess](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%87%AA%E5%AE%9A%E4%B9%89.md#pushbackpasstopostprocess) | 客户端 | 尚未建立映射 | — |
| [RemovePassInPostprocess](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%87%AA%E5%AE%9A%E4%B9%89.md#removepassinpostprocess) | 客户端 | 尚未建立映射 | — |
| [SetEnableByName](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%87%AA%E5%AE%9A%E4%B9%89.md#setenablebyname) | 客户端 | 尚未建立映射 | — |
| [SetParameter](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%90%8E%E5%A4%84%E7%90%86/%E8%87%AA%E5%AE%9A%E4%B9%89.md#setparameter) | 客户端 | 尚未建立映射 | — |

</div>

## 联机大厅

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetPlayerUid](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%81%94%E6%9C%BA%E5%A4%A7%E5%8E%85.md#getplayeruid) | 服务端 | 尚未建立映射 | — |
| [LobbyGetStorage](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%81%94%E6%9C%BA%E5%A4%A7%E5%8E%85.md#lobbygetstorage) | 服务端 | 尚未建立映射 | — |
| [LobbyGetStorageBySort](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%81%94%E6%9C%BA%E5%A4%A7%E5%8E%85.md#lobbygetstoragebysort) | 服务端 | 尚未建立映射 | — |
| [LobbySetStorageAndUserItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%81%94%E6%9C%BA%E5%A4%A7%E5%8E%85.md#lobbysetstorageanduseritem) | 服务端 | 尚未建立映射 | — |
| [QueryLobbyUserItem](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E8%81%94%E6%9C%BA%E5%A4%A7%E5%8E%85.md#querylobbyuseritem) | 服务端 | 尚未建立映射 | — |

</div>

## 成就

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [LobbyGetAchievementStorage](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%88%90%E5%B0%B1.md#lobbygetachievementstorage) | 服务端 | 尚未建立映射 | — |
| [LobbySetAchievementStorage](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%88%90%E5%B0%B1.md#lobbysetachievementstorage) | 服务端 | 尚未建立映射 | — |

</div>

## 商城

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [CloseShopWindow](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%95%86%E5%9F%8E.md#closeshopwindow) | 客户端 | 尚未建立映射 | — |
| [HideShopGate](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%95%86%E5%9F%8E.md#hideshopgate) | 客户端 | 尚未建立映射 | — |
| [OpenItemDetailWindow](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%95%86%E5%9F%8E.md#openitemdetailwindow) | 客户端 | 尚未建立映射 | — |
| [OpenShopWindow](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%95%86%E5%9F%8E.md#openshopwindow) | 客户端 | 尚未建立映射 | — |
| [ShowShopGate](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%95%86%E5%9F%8E.md#showshopgate) | 客户端 | 尚未建立映射 | — |

</div>

## 山头服务器

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [GetHostPlayerUid](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E5%B1%B1%E5%A4%B4%E6%9C%8D%E5%8A%A1%E5%99%A8.md#gethostplayeruid) | 服务端 | 尚未建立映射 | — |

</div>

## 渲染

<div className="modsapi-table-scroll" tabIndex={0} aria-label="原生接口映射，可横向滚动">

| 原生接口 | 执行端 | 当前记录 | 已核对的公开入口 |
| --- | --- | --- | --- |
| [AddArrowShape](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#addarrowshape) | 客户端 | 尚未建立映射 | — |
| [AddBoxShape](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#addboxshape) | 客户端 | 尚未建立映射 | — |
| [AddCircleShape](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#addcircleshape) | 客户端 | 尚未建立映射 | — |
| [AddLineShape](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#addlineshape) | 客户端 | 发现原生调用，待核对 | — |
| [AddSphereShape](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#addsphereshape) | 客户端 | 尚未建立映射 | — |
| [AddTextShape](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#addtextshape) | 客户端 | 尚未建立映射 | — |
| [GetBoxScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#getboxscale) | 客户端 | 尚未建立映射 | — |
| [GetColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#getcolor) | 客户端 | 尚未建立映射 | — |
| [GetEndPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#getendpos) | 客户端 | 发现原生调用，待核对 | — |
| [GetLength](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#getlength) | 客户端 | 尚未建立映射 | — |
| [GetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#getpos) | 客户端 | 发现原生调用，待核对 | — |
| [GetPriority](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#getpriority) | 客户端 | 尚未建立映射 | — |
| [GetRadius](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#getradius) | 客户端 | 尚未建立映射 | — |
| [GetSegments](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#getsegments) | 客户端 | 尚未建立映射 | — |
| [GetText](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#gettext) | 客户端 | 发现原生调用，待核对 | — |
| [GetType](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#gettype) | 客户端 | 尚未建立映射 | — |
| [GetVisible](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#getvisible) | 客户端 | 发现原生调用，待核对 | — |
| [Remove](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#remove) | 客户端 | 发现原生调用，待核对 | — |
| [RemoveAll](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#removeall) | 客户端 | 尚未建立映射 | — |
| [SetBoxScale](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#setboxscale) | 客户端 | 尚未建立映射 | — |
| [SetColor](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#setcolor) | 客户端 | 发现原生调用，待核对 | — |
| [SetEndPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#setendpos) | 客户端 | 尚未建立映射 | — |
| [SetLength](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#setlength) | 客户端 | 尚未建立映射 | — |
| [SetPos](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#setpos) | 客户端 | 尚未建立映射 | — |
| [SetPriority](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#setpriority) | 客户端 | 尚未建立映射 | — |
| [SetRadius](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#setradius) | 客户端 | 尚未建立映射 | — |
| [SetSegments](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#setsegments) | 客户端 | 尚未建立映射 | — |
| [SetText](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#settext) | 客户端 | 发现原生调用，待核对 | — |
| [SetVisible](https://github.com/MCNeteaseDevs/mc-netease-sdk/blob/main/1-ModAPI/%E6%8E%A5%E5%8F%A3/%E6%B8%B2%E6%9F%93.md#setvisible) | 客户端 | 发现原生调用，待核对 | — |

</div>