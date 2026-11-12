---
title: 粒子、绑定与表达式绘图
---

# 粒子、绑定与表达式绘图

`spawnParticle` 创建资源包中定义的原生发射器。表达式绘图 `spawnDynamicParticle` 使用原生绘图形状，二者生命周期与性能开销不同。

```python
from ModSAPI.client.beta import client

particle = client.spawnParticle("example:spark", client.localPlayer.location, {
    "rotation": (0, 0, 0),
    "molangVariables": {"variable.size": 1.0},
})
particle.setMolang("variable.size", 2.0)
particle.bindToEntity(client.localPlayer, {"bone": "", "offset": (0, 1, 0)})
particle.pause()
particle.resume()
particle.remove()
```

手动 `emit()` 需要资源定义本身支持手动发射。绑定的 `bone=""` 表示根节点；位置与旋转采用原生约定。原生创建返回 0 会视为失败，不会返回一个看似有效的句柄。

```python
from ModSAPI.client.beta import client

drawing = client.spawnDynamicParticle({
    "x": "math.cos(v.emitter_age / 10)",
    "y": 1.5,
    "z": "math.sin(v.emitter_age / 10)",
    "color": (1, 0.5, 0),
}, client.localPlayer.location, {
    "mode": "point",
    "interval": 1,
    "maxAmount": 60,
    "visible": True,
})

def finish():
    if drawing.lastError is not None:
        print(drawing.lastError)
    drawing.remove()

client.runTimeout(finish, 100)
```

表达式不是 Python 任意代码，只接受受限制的语法、变量和函数。绘图年龄按该句柄的自有更新推进；`maxAmount` 限制保留形状数量，不能代替对创建频率的控制。异步更新失败可通过 `lastError` 查看；功能结束要 `remove()`，不要每帧重复创建一组绘图句柄。