---
title: 计分板与参与者
---

# 计分板与参与者

从 [world.scoreboard](../server/apis/world.md#scoreboard) 获取计分板。先查找目标，再在不存在时创建，避免重复注册。显示名称与目标 ID 是不同字段。

```python
from ModSAPI.server.beta import world

objective = world.scoreboard.getObjective("example_points")
if objective is None:
    objective = world.scoreboard.addObjective("example_points", "Example points")

for player in world.getAllPlayers():
    objective.addScore(player, 1)
    print(player.name, objective.getScore(player))
```

某些操作接受实体、计分板身份或字符串参与者，具体看方法签名。不要把 [ScoreboardIdentity.id](../server/reference/ScoreboardIdentity.md#id) 当作永久的玩家账号 ID；它是包装层运行时身份。假玩家名称也不等价于在线玩家实体。

当前实现部分操作依赖原生命令与 ExtraData 镜像。其他脚本或命令改变计分板后，缓存一致性仍有边界；不能把本库缓存当作跨所有外部命令的事务数据库。