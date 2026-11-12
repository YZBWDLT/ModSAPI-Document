---
title: architect.component.index
---

# architect.component.index

这是核心包的架构辅助模块，不是模板 beta 入口的直接导出。下方示例中的 module 是此模块对象；仅在核心包开发或已经取得模块对象时使用。

## Component {#Component}

```python
Component(persist = False)
```

执行 [Component](../../server/reference/Component.md) 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `persist` | 由值/所属选项确定 | `False` |


```python
def use_function(module):
    return module.Component()
```

## registerComponents {#registerComponents}

```python
registerComponents(isServer)
```

执行 registerComponents 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `isServer` | 由值/所属选项确定 | `必填` |


```python
def use_function(module, isServer):
    return module.registerComponents(isServer)
```

## getComponentAnnotation {#getComponentAnnotation}

```python
getComponentAnnotation()
```

执行 getComponentAnnotation 架构辅助操作。


```python
def use_function(module, cls):
    return module.getComponentAnnotation(cls)
```

## isPersistComponent {#isPersistComponent}

```python
isPersistComponent()
```

执行 isPersistComponent 架构辅助操作。


```python
def use_function(module, cls):
    return module.isPersistComponent(cls)
```

## createComponent {#createComponent}

```python
createComponent(entityId)
```

执行 createComponent 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` |

显式异常：[RuntimeError](../../common/type-system.md#runtimeerror): `'Component is being destroyed'`


```python
def use_function(module, entityId, cls):
    return module.createComponent(entityId, cls)
```

## forgetEntity {#forgetEntity}

```python
forgetEntity(entityId, side = None)
```

引擎移除实体后，释放 Python 引用。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` |
| `side` | 由值/所属选项确定 | [None](../../common/type-system.md#none) |


```python
def use_function(module, entityId):
    return module.forgetEntity(entityId)
```

## destroyComponent {#destroyComponent}

```python
destroyComponent(entityId)
```

执行 destroyComponent 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` |

显式异常：[RuntimeError](../../common/type-system.md#runtimeerror): `'Engine failed to destroy component'`


```python
def use_function(module, entityId, cls):
    return module.destroyComponent(entityId, cls)
```

## getComponent {#getComponent}

```python
getComponent(entityId, clsList, filter = None)
```

执行 getComponent 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` |
| `clsList` | 由值/所属选项确定 | `必填` |
| `filter` | 由值/所属选项确定 | [None](../../common/type-system.md#none) |


```python
def use_function(module, entityId, clsList):
    return module.getComponent(entityId, clsList)
```

## getEntities {#getEntities}

```python
getEntities(side = None)
```

执行 getEntities 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `side` | 由值/所属选项确定 | [None](../../common/type-system.md#none) |


```python
def use_function(module):
    return module.getEntities()
```