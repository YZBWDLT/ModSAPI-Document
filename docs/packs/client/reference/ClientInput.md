---
title: "ClientInput"
sidebar_label: "ClientInput"
---

# ClientInput

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Input.py`；声明补充了静态类型信息。

通过 [client.input](../apis/manager.md#input) 取得的本地输入服务。权限写入只影响当前设备的输入处理，不代表服务端授权。临时覆盖层可组合，无需轮询；直接写入修改有效覆盖层下的基础值。reset() 与客户端退出时尝试恢复本服务持有的初始值，释放时保留外部写入的不同值。

## 获取方式

通过 [client.input](../apis/manager.md#input) 取得本地输入服务，无需手动构造或注册系统。权限仅影响当前设备，不代表服务端授权。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [overrides](#overrides) | 只读属性 |
| [getPermission](#getPermission) | 方法 |
| [getPermissions](#getPermissions) | 方法 |
| [setPermission](#setPermission) | 方法 |
| [overridePermissions](#overridePermissions) | 方法 |
| [getMovementVector](#getMovementVector) | 方法 |
| [getMousePosition](#getMousePosition) | 方法 |
| [getTouchPosition](#getTouchPosition) | 方法 |
| [isMouseEmulatingTouch](#isMouseEmulatingTouch) | 只读属性 |
| [holdThresholdMilliseconds](#holdThresholdMilliseconds) | 可读写属性 |
| [reset](#reset) | 方法 |

## overrides {#overrides}

```python
overrides: tuple[ClientInputOverride, ...]
```

本服务仍持有的覆盖层，包含创建或清理失败后等待重试的工作。

**访问：** 只读。

**返回类型：** [tuple](../../common/type-system.md#tuple)[[ClientInputOverride](ClientInputOverride.md), ...]。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.overrides
```

## getPermission {#getPermission}

```python
getPermission(permission: str) -> bool
```

读取当前原生有效权限值，包含外部代码的写入结果。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `permission` | [str](../../common/type-system.md#str) | `必填` | 传给 [ClientInput.getPermission](ClientInput.md#getPermission) 的 permission 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getPermission(instance, permission):
    return instance.getPermission(permission)
```

## getPermissions {#getPermissions}

```python
getPermissions(permissions: list[str] | tuple[str, ...] | None = None) -> dict[str, bool]
```

使用同一个原生操作组件读取权限快照，返回独立字典。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `permissions` | [list](../../common/type-system.md#list)[[str](../../common/type-system.md#str)] \| [tuple](../../common/type-system.md#tuple)[[str](../../common/type-system.md#str), ...] \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 传给 [ClientInput.getPermissions](ClientInput.md#getPermissions) 的 permissions 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [bool](../../common/type-system.md#bool)]。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'permissions must be a list or tuple'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getPermissions(instance):
    return instance.getPermissions()
```

## setPermission {#setPermission}

```python
setPermission(permission: str, isEnabled: bool) -> None
```

修改本服务持有的基础权限值，有效覆盖层仍然优先。写入失败会立即尝试恢复，并抛出原始错误；回滚失败的部分仍由本服务持有，可通过 reset 重试。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `permission` | [str](../../common/type-system.md#str) | `必填` | 传给 [ClientInput.setPermission](ClientInput.md#setPermission) 的 permission 参数；结合上方功能说明和下方调用示例使用。 |
| `isEnabled` | [bool](../../common/type-system.md#bool) | `必填` | 传给 [ClientInput.setPermission](ClientInput.md#setPermission) 的 isEnabled 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `参见本成员的前置条件。` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setPermission(instance, permission, isEnabled):
    return instance.setPermission(permission, isEnabled)
```

## overridePermissions {#overridePermissions}

```python
overridePermissions(permissions: dict[str, bool]) -> ClientInputOverride
```

复制并应用权限覆盖字典，返回可释放句柄。先验证全部字段并读取全部初始值，再执行写入。创建失败会尝试回滚所有通道；未完成的清理保留在 overrides 中。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `permissions` | [dict](../../common/type-system.md#dict)[[str](../../common/type-system.md#str), [bool](../../common/type-system.md#bool)] | `必填` | 传给 [ClientInput.overridePermissions](ClientInput.md#overridePermissions) 的 permissions 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [ClientInputOverride](ClientInputOverride.md)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [Exception](../../common/type-system.md#exception) | `参见本成员的前置条件。` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_overridePermissions(instance, permissions):
    return instance.overridePermissions(permissions)
```

## getMovementVector {#getMovementVector}

```python
getMovementVector() -> Vector2
```

读取二维移动输入，正 X 表示向右，正 Y 表示向前。原生第一分量向左为正，因此适配时取反。读取的是输入意图，不是实体速度。

**返回类型：** [Vector2](../../common/reference/Vector2.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetInputVector`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getMovementVector(instance):
    return instance.getMovementVector()
```

## getMousePosition {#getMousePosition}

```python
getMousePosition() -> Vector2 | None
```

原生屏幕坐标，非电脑平台可能返回 [None](../../common/type-system.md#none)。网易仅保证通过原生界面栈打开界面期间能正确取得鼠标位置；不会自动转换为控件的局部界面坐标。

**返回类型：** [Vector2](../../common/reference/Vector2.md) \| [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetMousePosition`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getMousePosition(instance):
    return instance.getMousePosition()
```

## getTouchPosition {#getTouchPosition}

```python
getTouchPosition() -> Vector2
```

在点击或长按释放回调中读取触摸的原生屏幕坐标。

**返回类型：** [Vector2](../../common/reference/Vector2.md)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetTouchPos`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_getTouchPosition(instance):
    return instance.getTouchPosition()
```

## isMouseEmulatingTouch {#isMouseEmulatingTouch}

```python
isMouseEmulatingTouch: bool
```

电脑端是否正在使用鼠标点击模拟触摸输入。

**访问：** 只读。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `IsTouchWithMouse`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isMouseEmulatingTouch
```

## holdThresholdMilliseconds {#holdThresholdMilliseconds}

```python
holdThresholdMilliseconds: int
```

长按阈值，单位为整数毫秒，原生默认值为 400。

**访问：** 可读写。

写入方式：`instance.holdThresholdMilliseconds = value`。参数类型线索：`(value: int) -> None`。

设置非负整数毫秒，reset 尝试恢复本服务持有的修改。

写入参数 `value`：[int](../../common/type-system.md#int)。

**返回类型：** [int](../../common/type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [TypeError](../../common/type-system.md#typeerror) | `'holdThresholdMilliseconds must be an integer'` |
| [ValueError](../../common/type-system.md#valueerror) | `'holdThresholdMilliseconds must be nonnegative'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.holdThresholdMilliseconds

def write_value(instance, value):
    instance.holdThresholdMilliseconds = value
```

## reset {#reset}

```python
reset() -> None
```

尝试恢复本服务持有的全部权限及阈值修改；失败部分保留以便重试。不调用全局权限重置，未持有的通道及外部写入的不同值会保留。原生写入不构成跨模组事务。

:::note 当前实现说明
恢复全部由本服务持有的修改，包括尚未关闭的界面的输入覆盖。通常优先释放所属流程自己的句柄。外部不同值会保留，相同值写入无法识别；恢复失败可重试。
:::

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_reset(instance):
    return instance.reset()
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 ClientInput 对象。
    print(value.overrides)
    print(value.isMouseEmulatingTouch)
    print(value.holdThresholdMilliseconds)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)