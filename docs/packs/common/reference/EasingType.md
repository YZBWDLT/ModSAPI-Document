---
title: "EasingType"
sidebar_label: "EasingType"
---

# EasingType

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/enums/stable.py`；声明补充了静态类型信息。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 |
| --- | --- | --- |
| `InBack` | [str](../type-system.md#str) | `'InBack'` |
| `InBounce` | [str](../type-system.md#str) | `'InBounce'` |
| `InCirc` | [str](../type-system.md#str) | `'InCirc'` |
| `InCubic` | [str](../type-system.md#str) | `'InCubic'` |
| `InElastic` | [str](../type-system.md#str) | `'InElastic'` |
| `InExpo` | [str](../type-system.md#str) | `'InExpo'` |
| `InOutBack` | [str](../type-system.md#str) | `'InOutBack'` |
| `InOutBounce` | [str](../type-system.md#str) | `'InOutBounce'` |
| `InOutCirc` | [str](../type-system.md#str) | `'InOutCirc'` |
| `InOutCubic` | [str](../type-system.md#str) | `'InOutCubic'` |
| `InOutElastic` | [str](../type-system.md#str) | `'InOutElastic'` |
| `InOutExpo` | [str](../type-system.md#str) | `'InOutExpo'` |
| `InOutQuad` | [str](../type-system.md#str) | `'InOutQuad'` |
| `InOutQuart` | [str](../type-system.md#str) | `'InOutQuart'` |
| `InOutQuint` | [str](../type-system.md#str) | `'InOutQuint'` |
| `InOutSine` | [str](../type-system.md#str) | `'InOutSine'` |
| `InQuad` | [str](../type-system.md#str) | `'InQuad'` |
| `InQuart` | [str](../type-system.md#str) | `'InQuart'` |
| `InQuint` | [str](../type-system.md#str) | `'InQuint'` |
| `InSine` | [str](../type-system.md#str) | `'InSine'` |
| `Linear` | [str](../type-system.md#str) | `'Linear'` |
| `OutBack` | [str](../type-system.md#str) | `'OutBack'` |
| `OutBounce` | [str](../type-system.md#str) | `'OutBounce'` |
| `OutCirc` | [str](../type-system.md#str) | `'OutCirc'` |
| `OutCubic` | [str](../type-system.md#str) | `'OutCubic'` |
| `OutElastic` | [str](../type-system.md#str) | `'OutElastic'` |
| `OutExpo` | [str](../type-system.md#str) | `'OutExpo'` |
| `OutQuad` | [str](../type-system.md#str) | `'OutQuad'` |
| `OutQuart` | [str](../type-system.md#str) | `'OutQuart'` |
| `OutQuint` | [str](../type-system.md#str) | `'OutQuint'` |
| `OutSine` | [str](../type-system.md#str) | `'OutSine'` |
| `Spring` | [str](../type-system.md#str) | `'Spring'` |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EasingType 对象。
    print(value.InBack)
    print(value.InBounce)
    print(value.InCirc)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)