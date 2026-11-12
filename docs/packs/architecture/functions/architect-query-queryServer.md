---
title: architect.query.queryServer
---

# architect.query.queryServer

这是核心包的架构辅助模块，不是模板 beta 入口的直接导出。下方示例中的 module 是此模块对象；仅在核心包开发或已经取得模块对象时使用。

## query {#query}

```python
query(entityId: int, comps: list) -> _Query
```

执行 query 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `entityId` | [int](../../common/type-system.md#int) | `必填` |
| `comps` | [list](../../common/type-system.md#list) | `必填` |

返回类型： [_Query](../../common/type-system.md#_query).


```python
def use_function(module, entityId, comps):
    return module.query(entityId, comps)
```

## callQueries {#callQueries}

```python
callQueries(entityId)
```

执行 callQueries 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `entityId` | 由值/所属选项确定 | `必填` |


```python
def use_function(module, entityId):
    return module.callQueries(entityId)
```

## Query {#Query}

```python
Query(*compCls)
```

执行 Query 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `*compCls` | 可变参数 | `可省略` |


```python
def use_function(module):
    return module.Query()
```