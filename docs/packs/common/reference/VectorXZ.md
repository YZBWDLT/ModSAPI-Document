---
title: "VectorXZ"
sidebar_label: "VectorXZ"
---

# VectorXZ

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/Vector.py`；声明补充了静态类型信息。

这是值对象或结果包装对象，成员通过属性访问；是否接受字典输入由所属操作的签名决定。包装类型不一定是模板入口的直接导出符号。

由 x、z 分量构成的平面向量。

## 获取方式

水平向量包装对象，具有 x、z 属性。调用接受水平向量的操作时，也可按其签名传入对应字典；模板入口未直接导出该构造器。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| `x` | [float](../type-system.md#float) | `data['x'] if 'x' in data else 0.0` |  |
| `z` | [float](../type-system.md#float) | `data['z'] if 'z' in data else 0.0` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |

## 构造器 {#constructor}

```python
VectorXZ(data: dict[str, float]) -> None
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | [dict](../type-system.md#dict)[[str](../type-system.md#str), [float](../type-system.md#float)] | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 VectorXZ 对象。
    print(value.x)
    print(value.z)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)