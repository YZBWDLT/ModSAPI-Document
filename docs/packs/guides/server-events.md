---
title: 服务端事件与实体查询
---

# 服务端事件与实体查询

从 [world.afterEvents](../server/apis/world.md#afterEvents)、[world.beforeEvents](../server/apis/world.md#beforeEvents) 和 [system.afterEvents](../server/reference/System.md#afterEvents) 获取信号。回调接收本库包装后的事件对象；它的字段与网易原生事件字典不必相同。

```python
# -*- coding: utf-8 -*-
from ModSAPI.server.beta import world

def on_chat(event):
    if event.message == "!hello":
        event.cancel = True
        event.sender.sendMessage(u"你好")

world.beforeEvents.chatSend.subscribe(on_chat)
```

只有实际提供可写取消字段的 before 事件才能取消操作。网易原生事件时序与微软限制执行阶段并不完全一致，不能从名称推断全部执行阶段限制。after 聊天和部分伤害包装会延迟分发，不应假定回调执行时实体依然有效。

## 按维度、位置和距离查询

```python
from ModSAPI.server.beta import world

dimension = world.getDimension("overworld")
entities = dimension.getEntities({
    "type": "minecraft:zombie",
    "location": (0, 64, 0),
    "minDistance": 0,
    "maxDistance": 16,
    "closest": 3,
})
for entity in entities:
    if entity.isValid:
        print(entity.id, entity.location.getTuple())
```

零值条件不是“未填写”，不要用 `if option` 代替 `is not None` 判断。全局 `world.getPlayers()` 与维度查询的范围不同；不要忽略维度条件。选项包装与字典字段详见公共选项参考。

查询结果和事件中的实体对象只代表当前可访问的运行实例。跨回调保存 ID，之后重新 `world.getEntity(id)` 并检查返回值，通常比永久保存对象更稳妥。射线的部分过滤与碰撞面推断仍有实现差异，见支持情况。


## 完整原生事件

物品、区块、天气、容器、实体、方块和平台事件见 [服务端事件目录](../server/native-events.md)。可写输出、取消和原生检测前提见 [完整用法与示例](native-events.md)。