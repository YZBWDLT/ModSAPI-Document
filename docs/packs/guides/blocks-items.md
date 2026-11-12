---
title: 方块、体积、物品与容器
---

# 方块、体积、物品与容器

方块对象保存维度和坐标，每次读取可反映世界的新状态。负坐标按向下取整定位；区块卸载后读取可能报错，`isValid` 不能消除检查与使用之间的竞态。

```python
from ModSAPI.server.beta import world, BlockVolume, BlockPermutation

dimension = world.getDimension("overworld")
volume = BlockVolume((0, 64, 0), (3, 64, 3))
stone = BlockPermutation.resolve("minecraft:stone")
changed = dimension.fillBlocks(volume, stone)
print(changed.getCapacity())
block = dimension.getBlock((0, 64, 0))
print(block.typeId, block.permutation.getAllStates())
```

完整矩形优先走原生批量路径；带过滤或稀疏体积时可能逐点处理。过滤中的包含条件按并集组合，排除条件优先。默认遇到未加载区块报错；显式允许跳过未加载区块时，返回值只包含实际处理的位置。

`BlockPermutation.getItemStack()` 当前不能保证完整保留方块状态对应的 aux 变种；`Block.getItemStack(withData=True)` 不支持无损方块实体到物品转换。不要用它们搬运箱子内容或保留全部方块 NBT。

## 向玩家背包添加物品

```python
from ModSAPI.server.beta import world, ItemStack

def give_item(player):
    component = player.getComponent("minecraft:inventory")
    if component is None:
        return
    container = component.container
    if container is None or not container.isValid:
        return
    item = ItemStack("minecraft:diamond", 3)
    item.setLore(["Example reward"])
    remainder = container.addItem(item)
    if remainder is not None:
        player.dimension.spawnItem(remainder, player.location)

for player in world.getAllPlayers():
    give_item(player)
```

`getItem()` 返回物品副本；修改后需要 `setItem()` 回写。`getSlot()` 返回槽位包装器，支持的属性赋值会回写该槽位。空槽返回 [None](../common/type-system.md#none)，不要直接访问其 `typeId`。搜索接口通常忽略数量但比较元数据；查看具体方法说明。

容器合并、转移和回滚可能涉及多次原生写入。失败后应重新读取实际内容，再决定如何恢复，避免根据过期副本重复发放物品。