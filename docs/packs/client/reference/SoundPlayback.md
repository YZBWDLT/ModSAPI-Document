---
title: "SoundPlayback"
sidebar_label: "SoundPlayback"
---

# SoundPlayback

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Audio.py`；声明补充了静态类型信息。

[Audio.playSound](Audio.md#playSound) 返回的场景音效实例。自然播放结束由引擎管理；isStopped 仅记录是否成功请求停止，不能用于判断自然结束。网易文档指出，创建后的七帧内按实例标识停止可能不可靠；建议至少等待十五帧再停止新声音。原生拒绝操作时会报告异常。

## 获取方式

由 `client.audio.playSound(...)` 返回。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [id](#id) | 只读属性 |
| [soundId](#soundId) | 只读属性 |
| [isStopped](#isStopped) | 只读属性 |
| [stop](#stop) | 方法 |

## 构造器 {#constructor}

```python
SoundPlayback(audio, identifier, soundId)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `audio` | 由值/所属选项确定 | `必填` | 传给 [SoundPlayback.__init__](SoundPlayback.md#constructor) 的 audio 参数；结合上方功能说明和下方调用示例使用。 |
| `identifier` | 由值/所属选项确定 | `必填` | 带命名空间的标识，推荐使用本模组前缀。 |
| `soundId` | 由值/所属选项确定 | `必填` | 资源包定义的声音标识，不是播放实例句柄的 id。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../../common/type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## id {#id}

```python
id: str
```

原生场景音效的实例标识，与声音资源标识不同。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.id
```

## soundId {#soundId}

```python
soundId: str
```

创建此实例时使用的声音资源标识。

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.soundId
```

## isStopped {#isStopped}

```python
isStopped: bool
```

是否已成功通过此对象请求 stop()。

:::note 当前实现说明
仅表示此句柄成功请求停止；不是原生实时播放状态。
:::

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isStopped
```

## stop {#stop}

```python
stop(fadeOutSeconds: float = 0) -> None
```

停止此实例；成功后重复停止不会产生额外影响。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `fadeOutSeconds` | [float](../../common/type-system.md#float) | `0` | 停止时的淡出秒数，需为有限非负值。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `StopCustomMusicById`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_stop(instance):
    return instance.stop()
```

## 使用示例


```python
from ModSAPI.client.beta import client

playback = client.audio.playSound("example:bell", {"loop": True})
client.runTimeout(lambda: playback.stop(0.2), 40)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)