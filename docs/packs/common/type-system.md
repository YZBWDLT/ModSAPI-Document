---
title: 类型标记与原生类型
---

# 类型标记与原生类型

类型名保留代码中的原文，说明统一使用中文。方括号表示类型参数，竖线表示多个允许类型之一。类型链接不代表该类型可以从模板直接导入，获取方式以各类型参考页为准。

## str {#str}

字符串；Python 2 运行时还须留意字节串与 Unicode 文本的区别。

## unicode {#unicode}

Python 2 的 Unicode 文本。

## int {#int}

整数；具体范围由所属接口校验。

## long {#long}

Python 2 的长整数。

## float {#float}

浮点数；位置、角度等接口通常要求有限值。

## bool {#bool}

布尔值 True 或 False；不应以整数代替严格布尔参数。

## None {#none}

无结果或缺失值；其具体含义由字段约定确定。

## list {#list}

有序、可修改的列表；方括号中的类型描述元素。

## tuple {#tuple}

元组；多个类型按位置对应，省略号表示可变长度。

## dict {#dict}

键值字典；两个类型参数依次描述键和值。

## set {#set}

不重复元素的集合。

## Any {#any}

静态声明未限制具体类型；仍须满足接口的运行时约束。

## Optional {#optional}

允许给定类型或 [None](type-system.md#none)，例如 [Optional](type-system.md#optional)[[Entity](../server/apis/entity.md)]。

## Union {#union}

多个允许类型之一；竖线连接的类型具有相同含义。

## Literal {#literal}

仅允许所列出的字面量值；其中的字符串是值，不是类型名。

## Callable {#callable}

可调用对象；[Callable](type-system.md#callable)[[参数类型], 返回类型] 描述回调签名。

## FunctionType {#functiontype}

Python 函数对象；可接受的回调签名见所属事件或方法。

## GeneratorType {#generatortype}

Python 生成器对象，逐次产生任务步骤或值。

## Iterator {#iterator}

迭代器，按需返回指定类型的元素。

## Iterable {#iterable}

可迭代对象，可用于依次读取元素。

## Sequence {#sequence}

序列，提供有序元素访问。

## Mapping {#mapping}

键值映射；是否可修改取决于实际对象。

## object {#object}

通用 Python 对象，不能据此推断其具有特定业务成员。

## type {#type}

类对象，用于传递类型本身而不是实例。

## Generic {#generic}

泛型声明基类，其类型参数在具体使用位置确定。

## Final {#final}

不可重新赋值的静态声明；具体值仍由源码和所属接口决定。

## BaseUIControl {#baseuicontrol}

网易原生界面控件。仅用于明确需要调用原生接口的自定义控件回调。

## TypedDict {#typeddict}

描述字典字段的静态类型；运行时通常传普通字典。

## NamedTuple {#namedtuple}

带命名字段的元组声明。

## TypeVar {#typevar}

泛型类型变量；[T](type-system.md#typevar)、[_TEvent](type-system.md#typevar) 和 [_TSemantic](type-system.md#typevar) 表示由具体用法确定的类型。

## Exception {#exception}

Python 异常基类，可通过异常对象取得错误详情。

## TypeError {#typeerror}

参数或值的类型不符合要求。

## ValueError {#valueerror}

参数类型可接受，但值、范围或组合不合法。

## RuntimeError {#runtimeerror}

当前运行状态不允许操作，例如在同步分发结束后写入事件输出。

## AttributeError {#attributeerror}

成员不存在或不允许写入。

## KeyError {#keyerror}

指定键或名称不存在。

## IndexError {#indexerror}

序列或槽位索引越界。

## NotImplementedError {#notimplementederror}

当前实现未提供所请求的功能。

## StopIteration {#stopiteration}

迭代器已没有后续元素。

## ZeroDivisionError {#zerodivisionerror}

除数为零。

## ScreenNode {#screennode}

网易原生屏幕基类。通过 client.screen.getScreenNode() 获取；其原生成员不属于本库封装接口。

## BlockPaletteComponent {#blockpalettecomponent}

网易原生方块调色板组件；生命周期和原生数据约定由开发包规定。

## Matrix {#matrix}

网易 mod.common.utils.mcmath 提供的矩阵类型，用于架构层坐标变换。由底层数学函数返回，不是模板入口导出的类。

## NativeVector3 {#nativevector3}

网易 mod.common.utils.mcmath 提供的三维向量类型，供底层矩阵运算使用；与本库公开的 [Vector3](../server/extra/vector.md) 包装类不同。

## _Query {#_query}

架构层查询工厂返回的内部查询对象。此名称来自类型声明，不是模板导出的公共类；应通过所属查询函数获取。