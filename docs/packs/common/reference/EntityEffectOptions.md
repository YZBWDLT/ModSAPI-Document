---
title: "EntityEffectOptions"
sidebar_label: "EntityEffectOptions"
---

import ApiFieldAnchor from '@docusaurus/Link';

# EntityEffectOptions

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/EntityOptions.py`；声明补充了静态类型信息。

选项通常可直接传 Python 字典；包装类名本身不保证通过模板导出。只使用所属操作已经实现的字段。

实体状态效果的附加选项。

## 获取方式

使用下方构造签名，或从拥有它的对象/事件读取。底层包装类型不一定是模板入口的直接导出符号。

## 字段与常量

| 名称 | 类型线索 | 默认值 / 来源 | 说明 |
| --- | --- | --- | --- |
| <ApiFieldAnchor id="field-amplifier" />`amplifier` | [int](../type-system.md#int) | `self.__data['amplifier'] if 'amplifier' in self.__data else 0` | 效果的强度。 |
| <ApiFieldAnchor id="field-showParticles" />`showParticles` | [bool](../type-system.md#bool) | `self.__data.get('showParticles', self.__data.get('showParticle', True))` |  |

字段显示为源码赋值来源时，该表达式不是调用者应直接执行的初始化代码。常量值以当前 Python 实现为准。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [showParticle](#showParticle) | 可读写属性 |

## 构造器 {#constructor}

```python
EntityEffectOptions(data: dict)
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `data` | [dict](../type-system.md#dict) | `必填` | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## showParticle {#showParticle}

```python
showParticle
```

读取 `showParticle` 的当前值。

**访问：** 可读写。

写入方式：`instance.showParticle = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回值：** 源码/声明未给出精确类型，请按上方语义及原生调用的实际结果使用；不要套用未实现的官方返回契约。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.showParticle

def write_value(instance, value):
    instance.showParticle = value
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 EntityEffectOptions 对象。
    print(value.showParticle)
    print(value.amplifier)
    print(value.showParticles)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)