---
title: 世界存储与客户端配置
---

# 世界存储与客户端配置

`world.getStorage(namespace)` 使用世界 ExtraData；`client.getStorage(namespace, options)` 使用本机配置。二者互不共享，也不会自动网络同步。

```python
from ModSAPI.server.beta import world

storage = world.getStorage("example:quests")
storage.setMany({"version": 1, "completed": []})
quests = storage.get("completed", [])
quests.append("first_steps")
storage.set("completed", quests)
print(storage.has("completed"))
print(storage.getKeys())
```

读取和写入都采用副本。修改 `get()` 的结果不会自动保存。[None](../common/type-system.md#none) 是可保存的 JSON null；删除键使用 `delete(key)`，不要用 `set(key, None)` 代替删除。

```python
from ModSAPI.client.beta import client

settings = client.getStorage("example:settings", {"isGlobal": True})
settings.set("volume", 0.5)
print(settings.get("volume", 1.0))
settings.delete("unused")
```

`isGlobal=False` 表示本机当前存档配置；`True` 表示本机不同存档共享配置。客户端值可被玩家修改，服务端不能把它当作可信数据。

每个命名空间保存一个 JSON 文档，UTF-8 编码上限 1 MiB、嵌套深度上限 32。键要求非空字符串，拒绝 NaN、无穷、循环引用和不支持的对象；详情见 [KeyValueStorage](../common/reference/KeyValueStorage.md) 参考。`setMany` 先校验整批数据，再合并并发出一次原生写入，但不提供跨进程锁或事务。

世界动态属性接口属于另一组已有封装，使用共享 ExtraData。不要假设 `getDynamicPropertyIds()` 只包含本功能的数据，也不要用全局清空方式删除其他功能的内容。

## 动态属性的批量保存

实体和世界均提供 `setDynamicProperties`。整批标识和值会先完成校验与复制，再调用引擎，最后统一保存一次；空字典直接返回。标识必须是非空字符串，并且不能包含空字符。这里的 [None](../common/type-system.md#none) 表示删除，与上方命名空间存储保存 JSON null 的语义不同。

```python
from ModSAPI.server.beta import world

world.setDynamicProperties({
    "example:version": 2,
    "example:enabled": True,
    "example:retired": None,
})

def save_player_progress(player):
    player.setDynamicProperties({
        "example:level": 3,
        "example:checkpoint": "village",
    })
```

单条写入、删除以及批量保存都会检查原生结果。失败时抛出 [NativeOperationError](../common/reference/NativeOperationError.md)，可读取 `operation`、`code` 和 `cause` 定位失败的操作。读取属性返回副本；缺失的属性返回 [None](../common/type-system.md#none)，已保存的 `False` 和 `0` 保持原值。

批量操作不会为每个键重复保存，但引擎没有事务保证。某个键写入或最终保存失败时，此前的原生内存修改可能已经发生，不能将异常解释为整批自动回滚。