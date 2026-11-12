---
title: 音效、音乐与通知
---

# 音效、音乐与通知

[client.audio.playSound()](../client/reference/Audio.md#playSound) 只在当前客户端播放。需要给所有在线玩家播放时，在服务端遍历 [world.getAllPlayers()](../server/apis/world.md#getAllPlayers)，并调用每个玩家的 [playSound()](../server/apis/player.md#playSound)。

声音标识必须在资源包中实际存在。音效返回 [SoundPlayback](../client/reference/SoundPlayback.md) 实例句柄；它的 `id` 是原生播放实例 ID，`soundId` 是声音定义名称。

```python
from ModSAPI.client.beta import client

playback = client.audio.playSound("example:bell", {
    "location": client.localPlayer.location,
    "volume": 0.5,
    "pitch": 1.0,
    "loop": False,
})

def stop_instance():
    playback.stop(0.2)

client.runTimeout(stop_instance, 40)
client.localPlayer.sendToast("Task complete", "Example")
```

音量为 0–1，音高为 0–256，零值会保留。指定 `entity` 时位置是相对偏移，默认零向量；未指定时默认使用本地玩家位置。原生返回 -1 到 -6 会抛出带失败码的 [NativeOperationError](../common/reference/NativeOperationError.md)，其中 -6 可能表示声音超出距离范围。

网易原生接口刚播放后立即按实例停止可能失败，不能把计时单位简单当作渲染帧。适配层不会自动无限重试；请捕获失败并根据实际场景决定是否再次停止。

`playback.isStopped` 只表示这个句柄已经成功请求停止，不是实时播放状态查询。`client.audio.stopSound(soundId)` 按定义名停止，可能影响其他脚本启动的实例；停止自己创建的实例应使用句柄。

```python
from ModSAPI.client.beta import client

client.audio.playMusic("example:theme", {"volume": 0.4, "loop": True})
```

音乐会替换当前背景音乐。不支持非零淡入；不要将官方完整音乐选项直接当作已实现。`musicStop` 事件携带声音定义名，不对应场景音效的实例 ID。