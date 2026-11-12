---
title: "StructureUneditableError"
sidebar_label: "StructureUneditableError"
---

# StructureUneditableError

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/errors/structure.py`。

结构无效时抛出。结构被删除后会失效。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 使用示例


```python
def inspect_value(value):
    # value 是所属 API 返回或接收的 StructureUneditableError 值。
    print(value)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)