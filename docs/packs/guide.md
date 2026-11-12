---
sidebar_position: 1
title: 接口总览与使用约定
---

# 接口总览与使用约定

ModSAPI 在网易 Python 2.7 运行环境中提供接近 Script API 风格的属性、方法、选项字典和事件信号。JavaScript/TypeScript 代码不能直接运行；类型标注用于编辑器与文档，不应复制进 Python 2 脚本。

本参考与当前实现同步，微软接口对照版本为 **server 2.11.0 / server-ui 2.3.0**。这两个版本是比较基准，不是本库的发布版本，也不表示全部官方能力已经实现。

## 模块入口

| 模块 | 模板中的导入 | 执行位置 |
| --- | --- | --- |
| 服务端 | `from ModSAPI.server.beta import world, system` | 服务端入口文件 |
| 客户端 | `from ModSAPI.client.beta import client` | 客户端入口文件 |
| 表单 | `from ModSAPI.serverui.beta import ActionFormData` | 服务端入口文件 |

模板会在注册核心系统后加载入口文件。若修改了模板中 `ModSAPI` 包的名称，应同步调整导入。类型页的“获取方式”会区分导出符号、返回对象和选项字典；不要假定所有类型都能从 `beta` 直接导入。

```python
# -*- coding: utf-8 -*-
from ModSAPI.server.beta import world

def welcome(event):
    if event.initialSpawn:
        event.player.sendMessage(u"欢迎进入世界")

world.afterEvents.playerSpawn.subscribe(welcome)
```

## 读参考页

参考页列出当前 Python 签名、默认值、属性读写性、参数、返回类型线索、显式抛出的异常和原生调用。源码与补全声明有差异时，以源码签名为准；无法从源码或声明确定的返回类型会明确说明，不猜测官方行为。

“空实现”不会提供可用性承诺。“部分支持”需要阅读限制；原生调用没有显式错误检查时，文档也不会承诺一定抛出某种错误。

## Python 与 SAPI 的差异

| SAPI 概念 | Python 写法 |
| --- | --- |
| `undefined` | 通常对应 [None](common/type-system.md#none)，请按方法的实际返回约定判断 |
| 选项对象 | `{"location": (0, 64, 0), "maxDistance": 16}` |
| 向量 | 三元组、带 x/y/z 的字典，或 [Vector3](server/extra/vector.md)；具体接受形式看接口 |
| [Promise.then](common/reference/Promise.md#then) | 本库 `Promise.then(callback)` / `catch(callback)`；不是 JavaScript [Promise](common/reference/Promise.md) 链 |
| 枚举 | 具名常量；有的值为字符串，有的为数值，不依赖枚举序号推断 |
| 保留字成员 | 使用文档列出的 Python 名称，例如体积的 `fromLocation` |

## 生命周期与错误

不要跨存档长期保存引擎对象。实体可能死亡或卸载，容器可能失效，客户端句柄在销毁或维度切换后可能不可用。调用前检查 `isValid`，调用中仍需处理异常；检查与使用之间可能发生状态变化。

坐标、音量和延迟等数值应为有限值。`True` 在 Python 中属于整数的子类，但许多接口明确拒绝用布尔值代替数字。读取返回的副本不会自动修改引擎状态。

计时、跨端通信、多步原生写入与实际渲染都有平台差异，详见 [时序与清理](guides/lifetime.md)、[错误处理](guides/errors.md) 和 [支持情况](compatibility.md)。