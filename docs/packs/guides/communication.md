---
title: 客户端与服务端通信
---

# 客户端与服务端通信

事件名建议带自己的命名空间，数据使用可传输的基础值。不要发送实体、容器、函数或 [UI](../server_ui/reference/UI.md) 对象本身；传 ID，再在接收端重新获取并验证。服务端必须验证玩家身份、参数类型、范围和权限。

## 单向事件

服务端入口：

```python
from ModSAPI.server.beta import world, system

def on_ping(event):
    player = event.player
    if player is None or not player.isValid:
        return
    system.sendToClient(player, "example:pong", {"message": "ready"})

system.afterEvents.clientEventReceive.subscribe("example:ping", on_ping)
```

客户端入口：

```python
from ModSAPI.client.beta import client

def on_pong(event):
    print(event.data["message"])

client.afterEvents.serverEventReceive.subscribe("example:pong", on_pong)
client.sendToServer("example:ping", {})
```

## 请求与响应

先注册响应方，再发起请求。响应回调返回可传输数据，不要返回另一个 [Promise](../common/reference/Promise.md)。

服务端入口：

```python
from ModSAPI.server.beta import system

def read_profile(event):
    # 此处按 event.player 查询调用玩家的数据，不能信任客户端传入的玩家 ID。
    return {"level": 1}

system.afterEvents.clientRequestData.subscribe("example:profile", read_profile)
```

客户端入口：

```python
from __future__ import print_function

from ModSAPI.client.beta import client

request = client.getDataFromServer("example:profile", {}, timeout=5.0)
request.then(lambda profile: print(profile["level"]))
request.catch(lambda error: print(error))
```

反向请求使用 `system.getDataFromClient(player, name, data, timeout)` 与 `client.afterEvents.serverRequestData.subscribe(name, callback)`。客户端返回值不应作为权威游戏状态或权限依据。响应、超时、发送失败、断线与系统销毁都会尝试释放请求所属的订阅和计时器。

`clientCallable`、`serverCallable` 也提供具名函数桥接。它们只是调用路由，不是安全沙箱；必须自己限制可调用函数与输入。普通功能更建议使用明确命名的数据事件或请求。