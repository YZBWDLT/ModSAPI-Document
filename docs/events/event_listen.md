---
sidebar_position: 1
---

# 事件监听

在模组开发过程中，往往会使用到大量事件，以满足模组需求

在ModSAPI中，我们使用与SAPI相同的事件监听方法，用法如下：

```python
world.afterEvents.entityDie.subscribe(function)
```

- `afterEvents` 存储了一系列已发生的事件（后事件）
    - 注：后续还会更新其他如`beforeEvents`等世界属性
- `entityDie` 事件名，即要监听的事件
- `subscribe` 监听（订阅），即表明在该事件发生时会执行一些操作
- `function` 回调函数，即要执行的操作

#### 示例
```python
def onEntityHurt(arg):
    print(arg)

world.afterEvents.entityHurt.subscribe(onEntityHurt)
```
