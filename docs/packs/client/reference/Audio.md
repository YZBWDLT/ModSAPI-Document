---
title: "Audio"
sidebar_label: "Audio"
---

# Audio

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Audio.py`；声明补充了静态类型信息。

播放本地音效和背景音乐；原生调用失败时明确抛出异常。

## 获取方式

使用 [client.audio](../apis/manager.md#audio)。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [playSound](#playSound) | 方法 |
| [playMusic](#playMusic) | 方法 |
| [stopSound](#stopSound) | 方法 |

## 构造器 {#constructor}

```python
Audio(playerId: str | None = None, owner: Any = None) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `playerId` | [str](../../common/type-system.md#str) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 玩家运行 ID，不是玩家显示名称。 |
| `owner` | [Any](../../common/type-system.md#any) | [None](../../common/type-system.md#none) | 传给 [Audio.__init__](Audio.md#constructor) 的 owner 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## playSound {#playSound}

```python
playSound(soundId: str, soundOptions: ClientSoundOptions | PlayerSoundOptions | None = None) -> SoundPlayback
```

返回 [SoundPlayback](SoundPlayback.md)。支持 location、volume、pitch、loop、entity 选项。音量范围为 0–1，音高范围为 0–256。传入 entity 时，location 是相对偏移，默认为零；否则默认使用本地玩家的位置。原生返回 -1 至 -6 时抛出 [NativeOperationError](../../common/reference/NativeOperationError.md)，并保留错误码。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `soundId` | [str](../../common/type-system.md#str) | `必填` | 资源包定义的声音标识，不是播放实例句柄的 id。 |
| `soundOptions` | [ClientSoundOptions](ClientSoundOptions.md) \| [PlayerSoundOptions](../../common/reference/PlayerSoundOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Audio.playSound](Audio.md#playSound) 的 soundOptions 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [SoundPlayback](SoundPlayback.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'PlayCustomMusic'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `PlayCustomMusic`, `CreatePos`, `GetPos`, `GetEngineCompFactory`, `GetLocalPlayerId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_playSound(instance, soundId):
    return instance.playSound(soundId)
```

## playMusic {#playMusic}

```python
playMusic(trackId: str, musicOptions: ClientMusicOptions | MusicOptions | None = None) -> None
```

替换背景音乐，支持 volume 和 loop 选项。原生播放不支持淡入参数，非零淡入值会被拒绝。旧 [MusicOptions](../../common/reference/MusicOptions.md) 仅在 fade 为零时可用。

:::note 当前实现说明
替换背景音乐；不支持非零淡入。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `trackId` | [str](../../common/type-system.md#str) | `必填` | 传给 [Audio.playMusic](Audio.md#playMusic) 的 trackId 参数；结合上方功能说明和下方调用示例使用。 |
| `musicOptions` | [ClientMusicOptions](ClientMusicOptions.md) \| [MusicOptions](../../common/reference/MusicOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [Audio.playMusic](Audio.md#playMusic) 的 musicOptions 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [UnsupportedFeatureError](../../common/reference/UnsupportedFeatureError.md) | `'Native music playback does not support fade-in'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `PlayGlobalCustomMusic`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_playMusic(instance, trackId):
    return instance.playMusic(trackId)
```

## stopSound {#stopSound}

```python
stopSound(soundId: str, fadeOutSeconds: float = 0) -> None
```

停止使用此资源名称的全部场景音效和背景音乐实例。这可能影响其他脚本启动的声音；若只需停止单个场景音效，请使用 [SoundPlayback.stop](SoundPlayback.md#stop)。

:::note 当前实现说明
按声音定义名停止，可能影响其他脚本；单个实例使用 [SoundPlayback.stop](SoundPlayback.md#stop)。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `soundId` | [str](../../common/type-system.md#str) | `必填` | 资源包定义的声音标识，不是播放实例句柄的 id。 |
| `fadeOutSeconds` | [float](../../common/type-system.md#float) | `0` | 停止时的淡出秒数，需为有限非负值。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `StopCustomMusic`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_stopSound(instance, soundId):
    return instance.stopSound(soundId)
```

## 使用示例


```python
from ModSAPI.client.beta import client

playback = client.audio.playSound("example:bell", {"volume": 0.5, "pitch": 1.0})
print(playback.id, playback.soundId)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)