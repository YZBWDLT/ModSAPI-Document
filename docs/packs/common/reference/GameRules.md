---
title: "GameRules"
sidebar_label: "GameRules"
---

# GameRules

作用域：公共数据、选项、枚举与错误。

源码：`core_behavior/ModSAPI/interfaces/Game.py`；声明补充了静态类型信息。

这是值对象或结果包装对象，成员通过属性访问；是否接受字典输入由所属操作的签名决定。包装类型不一定是模板入口的直接导出符号。

游戏规则，也可通过 /gamerule 命令控制。

## 获取方式

从 [world.gameRules](../../server/apis/world.md#gameRules) 获取；只使用当前实现已映射的规则属性。

## 成员索引

| 名称 | 形态 |
| --- | --- |
| [__init__](#constructor) | 构造器 |
| [commandBlocksEnabled](#commandBlocksEnabled) | 可读写属性 |
| [doDayLightCycle](#doDayLightCycle) | 可读写属性 |
| [doEntityDrops](#doEntityDrops) | 可读写属性 |
| [doFireTick](#doFireTick) | 可读写属性 |
| [doImmediateRespawn](#doImmediateRespawn) | 可读写属性 |
| [doMobLoot](#doMobLoot) | 可读写属性 |
| [doMobSpawning](#doMobSpawning) | 可读写属性 |
| [doTileDrops](#doTileDrops) | 可读写属性 |
| [doWeatherCycle](#doWeatherCycle) | 可读写属性 |
| [keepInventory](#keepInventory) | 可读写属性 |
| [mobGriefing](#mobGriefing) | 可读写属性 |
| [naturalRegeneration](#naturalRegeneration) | 可读写属性 |
| [pvp](#pvp) | 可读写属性 |
| [randomTickSpeed](#randomTickSpeed) | 可读写属性 |
| [respawnBlocksExplode](#respawnBlocksExplode) | 可读写属性 |
| [showCoordinates](#showCoordinates) | 可读写属性 |
| [spawnRadius](#spawnRadius) | 可读写属性 |
| [tntExplodes](#tntExplodes) | 可读写属性 |

## 构造器 {#constructor}

```python
GameRules()
```

构造该类型。通常通过下方获取方式使用；需要引擎上下文的包装器不建议自行构造。

:::warning 空实现 / 基类占位
源码没有可执行的功能实现。文档保留签名用于识别缺口；不要据此认为原生能力可用。
:::

**返回值：** 当前实现不显式返回结果，Python 返回 [None](../type-system.md#none)。

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

## commandBlocksEnabled {#commandBlocksEnabled}

```python
commandBlocksEnabled: bool
```

读取 `commandBlocksEnabled` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 command_blocks_enabled；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.commandBlocksEnabled = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.commandBlocksEnabled

def write_value(instance, value):
    instance.commandBlocksEnabled = value
```

## doDayLightCycle {#doDayLightCycle}

```python
doDayLightCycle: bool
```

读取 `doDayLightCycle` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 daylight_cycle；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.doDayLightCycle = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.doDayLightCycle

def write_value(instance, value):
    instance.doDayLightCycle = value
```

## doEntityDrops {#doEntityDrops}

```python
doEntityDrops: bool
```

读取 `doEntityDrops` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 entities_drop_loot；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.doEntityDrops = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.doEntityDrops

def write_value(instance, value):
    instance.doEntityDrops = value
```

## doFireTick {#doFireTick}

```python
doFireTick: bool
```

读取 `doFireTick` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 fire_spreads；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.doFireTick = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.doFireTick

def write_value(instance, value):
    instance.doFireTick = value
```

## doImmediateRespawn {#doImmediateRespawn}

```python
doImmediateRespawn: bool
```

读取 `doImmediateRespawn` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 immediate_respawn；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.doImmediateRespawn = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.doImmediateRespawn

def write_value(instance, value):
    instance.doImmediateRespawn = value
```

## doMobLoot {#doMobLoot}

```python
doMobLoot: bool
```

读取 `doMobLoot` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 mob_loot；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.doMobLoot = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.doMobLoot

def write_value(instance, value):
    instance.doMobLoot = value
```

## doMobSpawning {#doMobSpawning}

```python
doMobSpawning: bool
```

读取 `doMobSpawning` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 mob_spawn；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.doMobSpawning = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.doMobSpawning

def write_value(instance, value):
    instance.doMobSpawning = value
```

## doTileDrops {#doTileDrops}

```python
doTileDrops: bool
```

读取 `doTileDrops` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 tile_drops；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.doTileDrops = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.doTileDrops

def write_value(instance, value):
    instance.doTileDrops = value
```

## doWeatherCycle {#doWeatherCycle}

```python
doWeatherCycle: bool
```

读取 `doWeatherCycle` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 weather_cycle；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.doWeatherCycle = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.doWeatherCycle

def write_value(instance, value):
    instance.doWeatherCycle = value
```

## keepInventory {#keepInventory}

```python
keepInventory: bool
```

读取 `keepInventory` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 keep_inventory；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.keepInventory = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.keepInventory

def write_value(instance, value):
    instance.keepInventory = value
```

## mobGriefing {#mobGriefing}

```python
mobGriefing: bool
```

读取 `mobGriefing` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 mob_griefing；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.mobGriefing = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.mobGriefing

def write_value(instance, value):
    instance.mobGriefing = value
```

## naturalRegeneration {#naturalRegeneration}

```python
naturalRegeneration: bool
```

读取 `naturalRegeneration` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 natural_regeneration；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.naturalRegeneration = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.naturalRegeneration

def write_value(instance, value):
    instance.naturalRegeneration = value
```

## pvp {#pvp}

```python
pvp: bool
```

读取 `pvp` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 pvp；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.pvp = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.pvp

def write_value(instance, value):
    instance.pvp = value
```

## randomTickSpeed {#randomTickSpeed}

```python
randomTickSpeed: int
```

读取 `randomTickSpeed` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 random_tick_speed；值类型为 [int](../type-system.md#int)。范围 (0, 2147483647)。
:::

**访问：** 可读写。

写入方式：`instance.randomTickSpeed = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [int](../type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.randomTickSpeed

def write_value(instance, value):
    instance.randomTickSpeed = value
```

## respawnBlocksExplode {#respawnBlocksExplode}

```python
respawnBlocksExplode: bool
```

读取 `respawnBlocksExplode` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 respawn_block_explosion；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.respawnBlocksExplode = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.respawnBlocksExplode

def write_value(instance, value):
    instance.respawnBlocksExplode = value
```

## showCoordinates {#showCoordinates}

```python
showCoordinates: bool
```

读取 `showCoordinates` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 show_coordinates；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.showCoordinates = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.showCoordinates

def write_value(instance, value):
    instance.showCoordinates = value
```

## spawnRadius {#spawnRadius}

```python
spawnRadius: int
```

读取 `spawnRadius` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 respawn_radius；值类型为 [int](../type-system.md#int)。范围 (0, 128)。
:::

**访问：** 可读写。

写入方式：`instance.spawnRadius = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [int](../type-system.md#int)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.spawnRadius

def write_value(instance, value):
    instance.spawnRadius = value
```

## tntExplodes {#tntExplodes}

```python
tntExplodes: bool
```

读取 `tntExplodes` 的当前值。底层调用 `GetGameRulesInfoServer`, `GetLevelId`。

:::note 当前实现说明
原生规则键 tnt_explodes；值类型为 [bool](../type-system.md#bool)。传入真正的 [bool](../type-system.md#bool)，不接受整数代替。
:::

**访问：** 可读写。

写入方式：`instance.tntExplodes = value`。参数类型线索：`(value)`。

写入参数 `value`：由值/所属选项确定。

**返回类型：** [bool](../type-system.md#bool)。静态声明不替代本页的实现限制。

### 显式异常

| 异常 | 校验信息 / 条件线索 |
| --- | --- |
| [RuntimeError](../type-system.md#runtimeerror) | `'Game rule is unavailable: ' + key` |
| [ValueError](../type-system.md#valueerror) | `'Invalid game rule value for ' + key` |
| [RuntimeError](../type-system.md#runtimeerror) | `'Unable to set game rule: ' + key` |

引擎调用、失效对象或下层校验仍可能抛出其他异常；这里只列出当前成员内显式写出的错误。

**原生调用：** `GetGameRulesInfoServer`, `GetLevelId`。

### 调用形状

此函数接收已经取得的有效对象和业务参数，展示准确调用形状；完整场景见下方示例与模块使用指南。

```python
def read_value(instance):
    return instance.tntExplodes

def write_value(instance, value):
    instance.tntExplodes = value
```

## 使用示例


```python
def inspect_value(value):
    # value 是上方获取方式取得的 GameRules 对象。
    print(value.commandBlocksEnabled)
    print(value.doDayLightCycle)
    print(value.doEntityDrops)
```

需要特定资源、玩家或已加载区块的示例，应在相应引擎环境中执行。

[返回接口总览](../../guide.md) · [场景指南](../../examples.md)