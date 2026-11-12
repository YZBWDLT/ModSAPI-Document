---
title: "ClientInput"
sidebar_label: "ClientInput"
---

# ClientInput

作用域：客户端。

源码：`core_behavior/ModSAPI/modules/client/Input.py`；声明补充了静态类型信息。

通过 [client.input](../apis/manager.md#input) 取得本机输入服务。权限修改只影响当前设备的输入响应，不代表服务端授权。临时覆盖层无需轮询，可叠加管理；直接权限写入修改覆盖层下方的基础值。reset 与客户端退出会尝试恢复所持有的初始值，并保留不同的外部写入。鼠标模拟模式也会保留可读取的初始值。控制布局、布局锁定和原生点击响应没有已核验的读取接口，属于直接配置，不能由 reset 恢复未知旧值。

## 获取方式

通过 [client.input](../apis/manager.md#input) 取得本地输入服务，无需手动构造或注册系统。权限仅影响当前设备，不代表服务端授权。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [walkMode](#walkMode) | 只读属性 |
| [triggerAction](#triggerAction) | 方法 |
| [setControlMode](#setControlMode) | 方法 |
| [setControlModeLocked](#setControlModeLocked) | 方法 |
| [setNativeResponseEnabled](#setNativeResponseEnabled) | 方法 |
| [overrides](#overrides) | 只读属性 |
| [getPermission](#getPermission) | 方法 |
| [getPermissions](#getPermissions) | 方法 |
| [setPermission](#setPermission) | 方法 |
| [overridePermissions](#overridePermissions) | 方法 |
| [getMovementVector](#getMovementVector) | 方法 |
| [getMousePosition](#getMousePosition) | 方法 |
| [getTouchPosition](#getTouchPosition) | 方法 |
| [isMouseEmulatingTouch](#isMouseEmulatingTouch) | 可读写属性 |
| [holdThresholdMilliseconds](#holdThresholdMilliseconds) | 可读写属性 |
| [reset](#reset) | 方法 |

## walkMode {#walkMode}

```python
walkMode: str
```

读取当前原生模式并返回 [ClientWalkMode](ClientWalkMode.md) 名称，不推断实际运动。原生一、二、三分别对应行走、潜行和跑步模式，未知值会报错。需要判断实际移动或疾跑时，应读取玩家状态或速度。

:::note 当前实现说明
返回 [ClientWalkMode](ClientWalkMode.md) 名称，不等于实际移动或疾跑状态。每次重新查询，未知原生编号不会被改成默认模式。
:::

**访问：** 只读。

**返回类型：** [str](../../common/type-system.md#str)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [NativeOperationError](../../common/reference/NativeOperationError.md) | `'GetWalkState'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetWalkState`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.walkMode
```

## triggerAction {#triggerAction}

```python
triggerAction(action: str) -> None
```

按当前本地游戏情景请求一次 [ClientInputAction](ClientInputAction.md)。跳跃、潜行切换和情景交互共用此入口，不猜测目标，不模拟持续按住时间，也不伪造动作结果。实际移动或交互由引擎决定；同步递归请求会被拒绝。本地输入响应标记不代表服务端授权。

:::note 当前实现说明
使用 [ClientInputAction](ClientInputAction.md) 的 Jump、ToggleSneak 或 Interact。[None](../../common/type-system.md#none) 不代表动作完成；交互依据当前原生情景，不接受任意目标。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `action` | [str](../../common/type-system.md#str) | `必填` | 传给 [ClientInput.triggerAction](ClientInput.md#triggerAction) 的 action 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown ClientInputAction value: ' + action` |
| [RuntimeError](../../common/type-system.md#runtimeerror) | `'Native actions cannot reenter an input action or mutation'` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_triggerAction(instance, action):
    return instance.triggerAction(action)
```

## setControlMode {#setControlMode}

```python
setControlMode(mode: str, options: ClientControlModeOptions | None = None) -> None
```

请求 [ClientControlMode](ClientControlMode.md) 指定的布局，可选传入 locked。三种原生布局各调用一次设置；方向键准星先选择方向键点击布局，再开启其原生准星开关。写入前检查全部请求方法是否存在。后续失败可能保留先前修改，没有已核验的模式、锁定读取或自动回滚。此接口配置触控布局，不重映射物理键盘或手柄按键。

:::note 当前实现说明
使用 [ClientControlMode](ClientControlMode.md)。DirectionalCrosshair 是两步组合请求，不是新的原生枚举编号。没有已核验的布局旧值读取，部分失败不自动回滚。
:::

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `mode` | [str](../../common/type-system.md#str) | `必填` | 传给 [ClientInput.setControlMode](ClientInput.md#setControlMode) 的 mode 参数；结合上方功能说明和下方调用示例使用。 |
| `options` | [ClientControlModeOptions](ClientControlModeOptions.md) \| [None](../../common/type-system.md#none) | [None](../../common/type-system.md#none) | 附加选项字典。字段及默认值见本页选项与关联类型；未实现字段不会因此生效。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [ValueError](../../common/type-system.md#valueerror) | `'Unknown ClientControlMode value: ' + mode` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetControlMode`, `SetControlModeLock`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setControlMode(instance, mode):
    return instance.setControlMode(mode)
```

## setControlModeLocked {#setControlModeLocked}

```python
setControlModeLocked(locked: bool) -> None
```

锁定或解除原生控制模式设置，不重新选择布局。没有已核验的读取接口；此直接配置不是可释放的权限覆盖层，reset 不会自动写入相反值。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `locked` | [bool](../../common/type-system.md#bool) | `必填` | 传给 [ClientInput.setControlModeLocked](ClientInput.md#setControlModeLocked) 的 locked 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `SetControlModeLock`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setControlModeLocked(instance, locked):
    return instance.setControlModeLocked(locked)
```

## setNativeResponseEnabled {#setNativeResponseEnabled}

```python
setNativeResponseEnabled(enabled: bool) -> None
```

设置原生场景点击响应，包括点击破坏方块和攻击实体；不保证禁用所有设备或自定义界面。没有已核验的原生读取，reset 不猜测初始值。菜单中的临时输入限制优先使用可释放的权限覆盖层。

### 参数

| 名称 | 类型线索 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `enabled` | [bool](../../common/type-system.md#bool) | `必填` | 传给 [ClientInput.setNativeResponseEnabled](ClientInput.md#setNativeResponseEnabled) 的 enabled 参数；结合上方功能说明和下方调用示例使用。 |

**返回类型：** [None](../../common/type-system.md#none)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def call_setNativeResponseEnabled(instance, enabled):
    return instance.setNativeResponseEnabled(enabled)
```

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

:::note 当前实现说明
电脑端可读写。首次实际修改保留初始值，reset 与客户端退出会尝试恢复；其他代码的不同值会保留，相同值写入不可区分。
:::

**访问：** 可读写。

写入方式：`instance.isMouseEmulatingTouch = value`。参数类型线索：`(enabled: bool) -> None`。

设置电脑端鼠标模拟触控界面模式，并保留可读取的初始值。相同状态不取得恢复所有权，也不创建游戏组件。reset 与客户端退出会尝试恢复所持有的修改，保留不同的外部写入。失败写入保留未确认的清理状态供重试。此类似 F11 的模式仅针对电脑端，不是输入设备查询。

写入参数 `enabled`：[bool](../../common/type-system.md#bool)。

**返回类型：** [bool](../../common/type-system.md#bool)。静态声明不替代本页的实现限制。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.isMouseEmulatingTouch

def write_value(instance, value):
    instance.isMouseEmulatingTouch = value
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

尝试恢复所持有的权限、长按阈值和鼠标模式，失败部分保留供重试。不调用全局输入开关，保留未持有的标记和不同的外部值。权限组件获取或恢复失败时，仍独立尝试鼠标恢复。布局、锁定及原生点击响应的未知旧值不会被猜测。原生写入不是跨模组事务。

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
    print(value.walkMode)
    print(value.overrides)
    print(value.isMouseEmulatingTouch)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)