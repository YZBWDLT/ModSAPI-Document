---
title: architect.basic
---

# architect.basic

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

## getComponentCls {#getComponentCls}

```python
getComponentCls()
```

执行 getComponentCls 架构辅助操作。


```python
def use_function(module):
    return module.getComponentCls()
```

## getGoalCls {#getGoalCls}

```python
getGoalCls()
```

执行 getGoalCls 架构辅助操作。


```python
def use_function(module):
    return module.getGoalCls()
```

## serverTick {#serverTick}

```python
serverTick()
```

执行 serverTick 架构辅助操作。


```python
def use_function(module):
    return module.serverTick()
```