---
title: "TickingArea"
sidebar_label: "TickingArea"
---

import ApiFieldAnchor from '@docusaurus/Link';

# TickingArea

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/TickingArea.py`；声明补充了静态类型信息。

这是值对象或结果包装对象，成员通过属性访问；是否接受字典输入由所属操作的签名决定。包装类型不一定是模板入口的直接导出符号。

特定常加载区域的上下文信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-dimension" />`dimension` | [Dimension](../../server/apis/dimension.md) | `data['dimension']` |  |
| <ApiFieldAnchor id="field-identifier" />`identifier` | [str](../type-system.md#str) | `data['identifier']` |  |
| <ApiFieldAnchor id="field-chunkCount" />`chunkCount` | [int](../type-system.md#int) | `data['chunkCount']` |  |
| <ApiFieldAnchor id="field-boundingBox" />`boundingBox` | [BlockBoundingBox](BlockBoundingBox.md) | `data['boundingBox']` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [isFullyLoaded](#isFullyLoaded) | 只读属性 |

## 构造器 {#constructor}

```python
TickingArea(data: dict) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | [dict](../type-system.md#dict) | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## isFullyLoaded {#isFullyLoaded}

```python
isFullyLoaded: bool
```

所有区块是否均已加载。ModSDK 的 SetAddArea 不会开启区块内的逻辑更新。

**访问：** 只读。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetLevelId`, `GetEngineCompFactory`, `CheckChunkState`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isFullyLoaded
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 TickingArea 对象。
    print(value.isFullyLoaded)
    print(value.dimension)
    print(value.identifier)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)