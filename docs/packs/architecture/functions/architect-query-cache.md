---
title: architect.query.cache
---

# architect.query.cache

这是核心包的架构辅助模块，不是模板 beta 入口的直接导出。下方示例中的 module 是此模块对象；仅在核心包开发或已经取得模块对象时使用。

## cache {#cache}

```python
cache(getter, default = None)
```

执行 cache 架构辅助操作。

| 参数 | 类型线索 | 默认值 |
| --- | --- | --- |
| `getter` | 由值/所属选项确定 | `必填` |
| `default` | 由值/所属选项确定 | [None](../../common/type-system.md#none) |


```python
def use_function(module, getter):
    return module.cache(getter)
```