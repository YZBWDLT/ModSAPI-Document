---
title: architect.subsystem
---

# architect.subsystem

这是核心包的架构辅助模块，不是模板 beta 入口的直接导出。下方示例中的 module 是此模块对象；仅在核心包开发或已经取得模块对象时使用。

## isServer {#isServer}

```python
isServer()
```

执行 isServer 架构辅助操作。


```python
def use_function(module):
    return module.isServer()
```

## SubsystemClient {#SubsystemClient}

```python
SubsystemClient(subsystemCls)
```

自动注册子系统类的装饰器。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `subsystemCls` | 由值/所属选项确定 | `必填` |


```python
def use_function(module, subsystemCls):
    return module.SubsystemClient(subsystemCls)
```

## SubsystemServer {#SubsystemServer}

```python
SubsystemServer(subsystemCls)
```

自动注册子系统类的装饰器。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `subsystemCls` | 由值/所属选项确定 | `必填` |


```python
def use_function(module, subsystemCls):
    return module.SubsystemServer(subsystemCls)
```

## getSubsystemCls {#getSubsystemCls}

```python
getSubsystemCls()
```

执行 getSubsystemCls 架构辅助操作。


```python
def use_function(module):
    return module.getSubsystemCls()
```