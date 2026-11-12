---
title: 客户端相机与视角
---

# 客户端相机与视角

[client.camera](../client/apis/manager.md#camera) 控制当前客户端的相机，采用网易原生坐标和角度约定。

```python
from ModSAPI.client.beta import client, ClientPerspective

camera = client.camera
camera.perspective = ClientPerspective.ThirdPersonBack
camera.fov = 75
camera.pitchLimits = (-60, 60)
print(camera.location.getTuple())
print(camera.rotation.getTuple())
```

FOV 范围为 30–110 度；俯仰上下限均在 -90–90 度内，最小值不能大于最大值。旋转向量的 x/y/z 分别是 pitch/yaw/roll，单位为度。

## 固定相机与恢复跟随

```python
from ModSAPI.client.beta import client

position = client.localPlayer.location
client.camera.location = (position.x, position.y + 4, position.z - 6)
client.camera.rotation = (20, 0, 0)

def restore_following():
    client.camera.resetPosition()

client.runTimeout(restore_following, 60)
```

设置 `location` 先调用脱离跟随，再设置相机中心。`resetPosition()` 恢复跟随，不会自动恢复 FOV、偏移、俯仰限制或透视模式。设置 `anchor` 会改变客户端交互原点，可能影响交互距离体验。

`lock(location, rotation)` 与 `unlock()` 使用原生锁定接口；`detach()` 只脱离跟随。渲染可能到下一帧才反映更改。相机属于本机全局状态，多模组同时控制时需要自己协调，功能结束只恢复自己改变的配置。