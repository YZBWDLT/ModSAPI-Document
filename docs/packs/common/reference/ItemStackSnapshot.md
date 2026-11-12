---
title: "ItemStackSnapshot"
sidebar_label: "ItemStackSnapshot"
---

# ItemStackSnapshot

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/ItemStackSnapshot.py`；声明补充了静态类型信息。

这是值对象或结果包装对象，成员通过属性访问；是否接受字典输入由所属操作的签名决定。包装类型不一定是模板入口的直接导出符号。

只读物品值，不会回写背包槽位。原生元数据在输入和输出时复制，原生已有的超量堆叠保持可读。clone 和 withAmount 创建独立值；实际背包写入应使用服务端容器接口。

## 获取方式

通过客户端背包、槽位或装备读取取得，也可创建独立值。继承 [EventItemStack](EventItemStack.md)，可直接用于本库物品界面渲染。

基类：[EventItemStack](EventItemStack.md).

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [auxValue](#auxValue) | 只读属性 |
| [clone](#clone) | 方法 |
| [withAmount](#withAmount) | 方法 |

## 继承成员

下列成员沿用基类约定；点击名称查看签名、参数、返回值和示例。

| 成员 | 定义位置 |
| --- | --- |
| [amount](EventItemStack.md#amount) | [EventItemStack](EventItemStack.md) |
| [getItemDict](EventItemStack.md#getItemDict) | [EventItemStack](EventItemStack.md) |
| [typeId](EventItemStack.md#typeId) | [EventItemStack](EventItemStack.md) |

## 构造器 {#constructor}

```python
ItemStackSnapshot(typeId: str, amount: int = 1, data: dict[str, Any] | None = None) -> None
```

构造独立物品值，并校验已知的原生变种字段。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `typeId` | [str](../type-system.md#str) | `必填` | 带命名空间的实体、物品或资源类型名称。 |
| `amount` | [int](../type-system.md#int) | `1` | 物品数量；新物品要求 1–255 的整数，并按最大堆叠数限制。 |
| `data` | [dict](../type-system.md#dict)[[str](../type-system.md#str), [Any](../type-system.md#any)] \| [None](../type-system.md#none) | [None](../type-system.md#none) | 传入的数据。跨端通信必须可传输；创建选项需符合该类型的数据结构。 |

**返回类型：** [None](../type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## auxValue {#auxValue}

```python
auxValue: int
```

原生物品变种值，不应一律解释为耐久值。

**访问：** 只读。

**返回类型：** [int](../type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../type-system.md#valueerror) | `'Native item aux value must be an integer'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.auxValue
```

## clone {#clone}

```python
clone() -> ItemStackSnapshot
```

复制完整物品值，不查询或修改槽位。

**返回类型：** [ItemStackSnapshot](ItemStackSnapshot.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_clone(instance):
    return instance.clone()
```

## withAmount {#withAmount}

```python
withAmount(amount: int) -> ItemStackSnapshot
```

创建数量为一到二百五十五的独立物品值，不改变源槽位。

:::note 当前实现说明
只创建新快照，不会修改源槽位；手动创建的新数量必须在一到二百五十五之间。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `amount` | [int](../type-system.md#int) | `必填` | 物品数量；新物品要求 1–255 的整数，并按最大堆叠数限制。 |

**返回类型：** [ItemStackSnapshot](ItemStackSnapshot.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_withAmount(instance, amount):
    return instance.withAmount(amount)
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ItemStackSnapshot 对象。
    print(value.auxValue)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)