---
title: "ClientSoundOptions"
sidebar_label: "ClientSoundOptions"
---

# ClientSoundOptions

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/options.pyi`；声明补充了静态类型信息。

:::info 字典结构或静态声明
此类型只出现在补全声明中，不是可从模板直接实例化的运行时类。作为选项时使用符合字段约定的 Python 字典。
:::

本地声音选项：位置通常为世界坐标；提供 entity 时为相对偏移。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `location` | [VectorLike](../../common/type-aliases.md#vectorlike) | `可选字段；省略规则见所属操作` |  |
| `volume` | [float](../../common/type-system.md#float) | `可选字段；省略规则见所属操作` |  |
| `pitch` | [float](../../common/type-system.md#float) | `可选字段；省略规则见所属操作` |  |
| `loop` | [bool](../../common/type-system.md#bool) | `可选字段；省略规则见所属操作` |  |
| `entity` | [ClientEntity](ClientEntity.md) \| [str](../../common/type-system.md#str) | `可选字段；省略规则见所属操作` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_options(options):
    print(options.get('location'))
    print(options.get('volume'))
    print(options.get('pitch'))
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)