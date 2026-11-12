---
title: SAPI 与 ModSDK 双向通信
---

# SAPI 与 ModSDK 双向通信

JavaScript 入口位于 `core_behavior/scripts/netease/index.js`。SAPI 仍在服务端运行，通过桥接调用 Python 服务端或指定玩家的 ModSDK 客户端。两端均使用命名空间标识、选项对象、消息信号和显式注册的处理器。

`main.js` 已加载桥接模块；业务处理器放在自己的模块中，再从入口导入。传输复用脚本指令和网易客户端通信，不会为每条消息创建实体。

## 在 SAPI 调用 Python 服务端

SAPI 端：

```javascript
import { system } from "@minecraft/server";
import { server } from "./netease/index.js";

system.run(async () => {
  try {
    const result = await server.request("example:double", { value: 21 });
    console.warn(result.value);
  } catch (error) {
    console.warn(error.code, error.remoteName, error.message);
  }
});
```

Python 服务端：

```python
from ModSAPI.server.beta import system


def double_value(event):
    value = event.data["value"]
    if isinstance(value, bool) or not isinstance(value, (int, long, float)):
        raise TypeError("value must be numeric")
    return {"value": value * 2}


system.scriptBridge.registerHandler("example:double", double_value)
```

处理器可以直接使用 ModSDK 或本库包装类。只有已注册的标识可以被调用，不按字符串执行任意 Python 代码。重复注册同名处理器会报错；功能结束时调用 `unregisterHandler`。

## 直接使用补充能力

以下代码中的 `player` 为原生 SAPI 的 [Player](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/player?view=minecraft-bedrock-stable) 对象。

```javascript
import { server, client } from "./netease/index.js";

async function inspectPlayer(player) {
  const nbt = await server.getEntityNbt(player);
  const local = client.forPlayer(player);
  await local.showToast("连接成功", "ModSAPI");
  const camera = await local.getCameraState();
  await local.setCameraFov(75);
  return { nbt, camera };
}
```

NBT 读取由 Python 服务端的原生实体组件执行；提示和相机操作由指定玩家的 ModSDK 客户端执行。原生能力缺失、对象失效或操作失败都会使异步结果失败。读取的 NBT 仍须符合数据类型和大小限制。

## 调用 ModSDK 客户端处理器

客户端 Python：

```python
from ModSAPI.client.beta import client


def read_local_name(event):
    return {"name": client.localPlayer.name}


client.scriptBridge.registerHandler("example:local_name", read_local_name)
```

SAPI 端取得玩家后调用：

```javascript
import { client } from "./netease/index.js";

async function readName(player) {
  return await client.forPlayer(player).request("example:local_name");
}
```

`forPlayer` 接受玩家对象，返回缓存的 [PlayerBridge](#playerbridge)。玩家离开时，对应连接失效，待完成请求会失败；不会将其他客户端的响应匹配到此玩家。

## 从 Python 调用 SAPI

SAPI 注册处理器：

```javascript
import { server, client } from "./netease/index.js";

server.registerHandler("example:format", event => ({ text: String(event.data.value) }));
client.registerHandler("example:acknowledge", event => {
  event.player.sendMessage("已收到客户端请求");
  return { accepted: true };
});
```

Python 服务端请求 `server` 上的处理器：

```python
from __future__ import print_function

from ModSAPI.server.beta import system

request = system.scriptBridge.request("example:format", {"value": 42})
request.then(lambda result: print(result["text"]))
request.catch(lambda error: print(error.code, error.remoteName))
```

Python 客户端请求对应玩家连接或 `client.registerHandler` 注册的处理器：

```python
from __future__ import print_function

from ModSAPI.client.beta import client

request = client.scriptBridge.request("example:acknowledge", {"ready": True})
request.then(lambda result: print(result["accepted"]))
request.catch(lambda error: print(error.code))
```

JavaScript 使用原生 [Promise](../common/reference/Promise.md)，可用 `await`。Python 使用本库 [Promise](../common/reference/Promise.md)，通过 `then`、`catch` 接收结果，不支持直接套用 JavaScript 的异步语法。

## 消息通知与注销

SAPI 服务端连接的通知信号为 `server.afterEvents.messageReceive`；单个玩家使用 `client.forPlayer(player).afterEvents.messageReceive`；所有客户端的通知可统一订阅 `client.afterEvents.messageReceive`。

```javascript
import { client } from "./netease/index.js";

const callback = client.afterEvents.messageReceive.subscribe(event => {
  console.warn(event.player.name, event.id, event.data);
}, { ids: ["example:status"] });

// 功能结束时调用：
// client.afterEvents.messageReceive.unsubscribe(callback);
```

Python 客户端发送通知：

```python
from __future__ import print_function

from ModSAPI.client.beta import client

client.scriptBridge.sendMessage("example:status", {"ready": True}).catch(
    lambda error: print(error.code))
```

Python 两端的通知信号分别为 [system.scriptBridge.afterEvents.messageReceive](../common/reference/ScriptBridgeAfterEvents.md#messageReceive) 与 [client.scriptBridge.afterEvents.messageReceive](../common/reference/ScriptBridgeAfterEvents.md#messageReceive)，用法与其他事件相同。通知的异步结果只确认本地原生传输接受了全部分包；需要远端处理结果时使用 `request`。

## 数据与对象引用 {#bridgevalue}

[BridgeValue](#bridgevalue) 支持空值、布尔值、有限数值、字符串、数组及字符串键字典，也支持原生 SAPI 的 [Entity](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/entity?view=minecraft-bedrock-stable)、[Dimension](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/dimension?view=minecraft-bedrock-stable) 和 [Block](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/block?view=minecraft-bedrock-stable) 引用。Python 端自动恢复为对应包装类；Python 返回这些对象时，SAPI 端恢复为原生对象。

```javascript
async function inspectEntity(player) {
  return await server.request("example:inspect_entity", { entity: player });
}
```

```python
def inspect_entity(event):
    entity = event.data["entity"]
    if not entity.isValid:
        raise ValueError("entity is no longer valid")
    return {"entity": entity, "location": entity.location}
```

传输不会使实体保持加载。对象在解码时已失效或客户端不可见时，返回 `INVALID_REFERENCE`；客户端独有实体无法因此变成服务端实体。客户端不提供可修改世界的方块包装能力，涉及方块操作请使用服务端处理器。

字符串、字典和数组会复制；循环引用、函数、非有限数值及不支持的对象会报错。Python 整数须处于 JavaScript 安全整数范围。单个序列化数据包最多 64 KiB，嵌套最多 32 层。选择器文本按原文传输，不会被命令解析器展开。

## 连接与公共方法 {#bridge}

[Bridge](#bridge) 由运行时管理，使用 `server` 或 `client.forPlayer(player)` 获取。Python 对应类型为 [ScriptBridge](../common/reference/ScriptBridge.md)。

| 成员 | 参数与返回值 |
| --- | --- |
| `isValid` | 只读布尔值，表示本地连接及目标玩家是否仍有效 |
| `player` | 只读的原生玩家对象；服务端连接不提供玩家 |
| `afterEvents` | [BridgeAfterEvents](#bridgeafterevents) |
| `sendMessage(id, data)` | 命名空间标识、[BridgeValue](#bridgevalue)；返回无结果的异步完成通知 |
| `request(id, data, options)` | 命名空间标识、数据、[BridgeRequestOptions](#bridgerequestoptions)；异步返回远端结果 |
| `registerHandler(id, callback)` | 回调接收 [BridgeMessageAfterEvent](#bridgemessageafterevent)，可返回数据或异步结果 |
| `unregisterHandler(id)` | 返回布尔值，表示处理器是否存在 |
| `dispose()` | 使待完成请求失败，释放本连接的订阅、处理器和待发送数据 |

## 服务端连接 {#serverbridge}

[ServerBridge](#serverbridge) 继承 [Bridge](#bridge)，通过 `server` 单例获取。

| 补充方法 | 参数与结果 |
| --- | --- |
| `getEntityNbt(entity, options)` | 原生实体对象和请求选项；异步返回 ModSDK 读取的 NBT 数据 |

## 单个玩家连接 {#playerbridge}

[PlayerBridge](#playerbridge) 继承 [Bridge](#bridge)，其 `player` 始终为选中的原生玩家对象。

| 补充方法 | 参数与结果 |
| --- | --- |
| `showToast(message, title, options)` | 文本、可选标题和请求选项；异步完成本地提示显示请求 |
| `getCameraState(options)` | 请求选项；异步返回 [ClientCameraState](#clientcamerastate) |
| `setCameraFov(fov, options)` | 30–110 度的有限视野角度和请求选项；异步完成原生设置 |

## 客户端连接管理 {#clientbridgemanager}

[ClientBridgeManager](#clientbridgemanager) 通过 `client` 单例获取。

| 成员 | 说明 |
| --- | --- |
| `forPlayer(player)` | 取得该玩家的 [PlayerBridge](#playerbridge) |
| `disconnect(player)` | 释放该玩家的连接 |
| `afterEvents.messageReceive` | 所有客户端的消息通知；事件的玩家对象必定存在 |
| `registerHandler(id, callback)` | 为当前和后续玩家连接注册共同的 SAPI 处理器 |
| `unregisterHandler(id)` | 注销共同处理器；保留连接自己注册的其他处理器 |

## 事件集合与信号 {#bridgeafterevents}

[BridgeAfterEvents](#bridgeafterevents) 包含只读的 `messageReceive`，类型为 [BridgeEventSignal](#bridgeeventsignal)。

### 订阅信号 {#bridgeeventsignal}

`subscribe(callback, options)` 返回传入的回调；`unsubscribe(callback)` 注销它。重复订阅同一回调会替换筛选条件；回调抛错会单独报告，后续订阅者仍会执行。选项类型见 [BridgeEventOptions](#bridgeeventoptions)。

### 消息参数 {#bridgemessageafterevent}

| 属性 | 类型与含义 |
| --- | --- |
| `id` | 字符串，命名空间消息或处理器名称 |
| `data` | [BridgeValue](#bridgevalue)，当前消息的解码数据 |
| `player` | 可选的原生玩家对象；客户端连接及所有客户端通知中必定存在 |

`ClientBridgeMessageAfterEvent` 使用相同字段，并保证 `player` 存在。Python 参数类型为 [ScriptBridgeMessage](../common/reference/ScriptBridgeMessage.md)；客户端为 [ClientPlayer](../client/reference/ClientPlayer.md) 对象，服务端为 [None](../common/type-system.md#none)。

### 事件筛选选项 {#bridgeeventoptions}

`BridgeEventOptions.ids` 为可选字符串数组，逐项按完整消息标识匹配。省略时接收全部消息，空数组不匹配任何消息；注册时复制，之后修改原数组不会改变筛选。

### 请求选项 {#bridgerequestoptions}

`BridgeRequestOptions.timeoutTicks` 为可选整数，范围 1–1200，默认 200。每单位为 1/20 秒，Python 端也遵循此换算。超时从本地提交请求开始计时，包含排队和网络等待；不会撤销远端已开始执行的操作。

### 相机状态 {#clientcamerastate}

`ClientCameraState.location`、`rotation` 为复制的三维坐标，`fov` 为角度数值，`perspective` 为 `FirstPerson`、`ThirdPersonBack` 或 `ThirdPersonFront`。旋转遵循网易原生的俯仰、偏航、翻滚约定。

## 错误与生命周期 {#bridgeerror}

SAPI 端使用 [BridgeError](#bridgeerror)，Python 端使用 [ScriptBridgeError](../common/reference/ScriptBridgeError.md)。`code` 为错误码，`remoteName` 保留远端异常类型，`message` 为异常说明。

| 错误码 | 含义 |
| --- | --- |
| `TIMEOUT` | 等待远端结果超时 |
| `DISPOSED` | 连接、所属系统或目标玩家已失效 |
| `DISCONNECTED` | 服务端转发时发现玩家离线 |
| `NOT_READY` | ModSDK 客户端尚未获得服务端通信会话 |
| `TRANSPORT_ERROR` | 原生指令、通信或计时器调用失败 |
| `UNKNOWN_HANDLER` | 远端没有注册指定处理器 |
| `DUPLICATE_HANDLER` | 本地重复注册处理器 |
| `INVALID_REFERENCE` | 对象已失效、不可见或当前端无法恢复此引用 |
| `PAYLOAD_TOO_LARGE` | 序列化数据包超过限制 |
| `PROTOCOL_ERROR` | 版本、分包或路由数据不合法 |
| `BUSY` | 待完成请求、队列或分包缓存达到上限 |
| `REMOTE_ERROR` | 远端处理器抛出了普通异常 |

处理器应验证业务数据及权限。通信成功不能替代业务授权。客户端路由会校验服务端分发到该玩家连接的会话信息，并核对待完成请求所属玩家。

系统销毁或玩家离开时会清理请求和订阅。SAPI 层只卸载某项功能时，先调用 `unregisterHandler`、`unsubscribe` 或 `dispose`；共享连接被销毁后，使用它的其他功能也会失去连接。

协议使用固定的私有脚本事件通道，单个分包不超过 1800 个字符，发送队列每次最多处理 16 个分包。未完成分包在十秒后释放，重复分包不会再次交付已完成的数据包。该机制不提供持久队列、事务或断线重放；需要结果确认时使用请求，而不是通知。