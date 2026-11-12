---
title: architect.utils.server
---

# architect.utils.server

这是核心包的架构辅助模块，不是模板 beta 入口的直接导出。下方示例中的 module 是此模块对象；仅在核心包开发或已经取得模块对象时使用。

## runCommand {#runCommand}

```python
runCommand(cmd, entityId)
```

执行 runCommand 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `cmd` | 由值/所属选项确定 | `必填` |
| `entityId` | 由值/所属选项确定 | `必填` |


```python
def use_function(module, cmd, entityId):
    return module.runCommand(cmd, entityId)
```

## motion {#motion}

```python
motion(entityId, mot)
```

执行 motion 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` |
| `mot` | 由值/所属选项确定 | `必填` |


```python
def use_function(module, entityId, mot):
    return module.motion(entityId, mot)
```

## sound {#sound}

```python
sound(entityId, sound)
```

执行 sound 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` |
| `sound` | 由值/所属选项确定 | `必填` |


```python
def use_function(module, entityId, sound):
    return module.sound(entityId, sound)
```

## particle {#particle}

```python
particle(particle, pos)
```

执行 particle 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `particle` | 由值/所属选项确定 | `必填` |
| `pos` | 由值/所属选项确定 | `必填` |


```python
def use_function(module, particle, pos):
    return module.particle(particle, pos)
```