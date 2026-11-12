---
title: 客户端事件、MoLang 与本地实体
---

# 客户端事件、MoLang 与本地实体

`keyPress` 提供整数原生键码、`isDown` 和 `screenName`；`mouseWheel.direction` 为 +1 或 -1。不要把原生键码写成 SAPI [InputButton](../common/reference/InputButton.md) 值。

```python
from ModSAPI.client.beta import client

def on_key(event):
    if event.isDown:
        print(event.key, event.screenName)

def on_wheel(event):
    print(event.direction)

client.afterEvents.keyPress.subscribe(on_key)
client.afterEvents.mouseWheel.subscribe(on_wheel)
```

原生客户端信号同步派发，单个订阅者异常会被记录，后续订阅者继续执行。`uiReady` 可能在维度切换后再次触发，初始化逻辑需要支持重复调用；它不是只触发一次的 [Promise](../common/reference/Promise.md)。

## MoLang 和查询变量

```python
from ModSAPI.client.beta import client

name = "query.mod.example_state"
client.registerQueryVariable(name, 0)
client.localPlayer.setQueryVariable(name, 1)
print(client.localPlayer.getQueryVariable(name))
client.localPlayer.setMolangValue("variable.example_scale", 1.25)
print(client.localPlayer.getMolangValue("variable.example_scale"))

def cleanup():
    client.unregisterQueryVariable(name)
```

只允许注销这个客户端成功注册的查询节点。查询值是原生单精度浮点数，大整数可能失真。写 MoLang 变量仅允许 `variable.*` / `v.*` 和有限数值；表达式错误会检查原生 error 字段。某些只在渲染上下文可用的 query，在普通脚本回调里可能返回零。

## 本地实体

```python
from ModSAPI.client.beta import client

entity = client.spawnEntity("minecraft:pig", client.localPlayer.location, {
    "rotation": (0, 0),
})
print(entity.id, entity.typeId)
if entity.isValid:
    entity.remove()
```

是否支持某个模型取决于网易引擎和资源。只有 `spawnEntity` 返回的本地实体句柄可以移除该实体；`getEntity` 得到的服务端实体句柄不能删掉服务端实体。本地实体不保存，维度切换后可能失效，不能用于服务端碰撞、权限或权威战斗判定。


## 完整原生事件

当前额外提供完整的输入、界面、实体、方块、音效与物理事件。见 [客户端事件目录](../client/events.md) 和 [同步取消、输出修改与示例](native-events.md)。