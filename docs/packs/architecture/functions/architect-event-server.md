---
title: architect.event.server
---

# architect.event.server

这是核心包的架构辅助模块，不是模板 beta 入口的直接导出。下方示例中的 module 是此模块对象；仅在核心包开发或已经取得模块对象时使用。

## event {#event}

```python
event(eventType, isCustomEvent = False)
```

执行 event 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `eventType` | 由值/所属选项确定 | `必填` |
| `isCustomEvent` | 由值/所属选项确定 | `False` |


```python
def use_function(module, eventType):
    return module.event(eventType)
```

## EventListener {#EventListener}

```python
EventListener(eventType, isCustomEvent = False)
```

执行 EventListener 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `eventType` | 由值/所属选项确定 | `必填` |
| `isCustomEvent` | 由值/所属选项确定 | `False` |


```python
def use_function(module, eventType):
    return module.EventListener(eventType)
```