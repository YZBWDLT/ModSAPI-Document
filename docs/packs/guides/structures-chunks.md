---
title: 结构模板与区块加载
---

# 结构模板与区块加载

结构从维度中的包含边界区域创建。先使用内存模式验证结果，需要存档持久化时再显式选择 [World](../server/apis/world.md) 保存模式。结构可能包含容器、方块实体和实体，不应当作普通方块数组处理。

```python
from ModSAPI.server.beta import world, StructureSaveMode

dimension = world.getDimension("overworld")
manager = world.structureManager
structure = manager.createFromWorld("example:platform", dimension,
    (0, 64, 0), (3, 64, 3), {
        "includeEntities": False,
        "includeAir": False,
        "saveMode": StructureSaveMode.Memory,
    })
manager.place(structure, dimension, (10, 64, 10))
```

删除结构会使相应包装对象失效。复杂旋转状态、结构中的实体以及实际落盘仍需要网易环境验证；不要承诺与所有微软结构选项完全一致。某些从原生存储读取的结构只能放置，不能通过可编辑调色板接口修改。

## 加载区块后执行操作

```python
from __future__ import print_function

from ModSAPI.server.beta import world

dimension = world.getDimension("overworld")
areas = world.tickingAreaManager
area_id = "example_work"
request = areas.createTickingArea(area_id, {
    "dimension": dimension,
    "from": (0, 60, 0),
    "to": (15, 70, 15),
})

def ready():
    try:
        print(dimension.getBlock((0, 64, 0)).typeId)
    finally:
        areas.removeTickingArea(area_id)

request.then(ready)
request.catch(lambda error: print(error))
```

这个接口提供加载等待，不保证开启实体、方块实体或随机 tick。区域标识要独占；不要删除其他功能或命令创建的区域。功能结束应移除自己创建的区域，不依赖退出游戏才释放。