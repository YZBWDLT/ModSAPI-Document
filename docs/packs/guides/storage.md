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