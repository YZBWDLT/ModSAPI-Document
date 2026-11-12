"""Hand-authored Chinese guides and executable Python 2 examples."""

GUIDES = {
"packs/guide.md": r'''---
sidebar_position: 1
title: 接口总览与使用约定
---

# 接口总览与使用约定

ModSAPI 在网易 Python 2.7 运行环境中提供接近 Script API 风格的属性、方法、选项字典和事件信号。JavaScript/TypeScript 代码不能直接运行；类型标注用于编辑器与文档，不应复制进 Python 2 脚本。

本参考与当前实现同步，微软接口对照版本为 **server @@SERVER_VERSION@@ / server-ui @@SERVER_UI_VERSION@@**。这两个版本是比较基准，不是本库的发布版本，也不表示全部官方能力已经实现。

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
| `undefined` | 通常对应 `None`，请按方法的实际返回约定判断 |
| 选项对象 | `{"location": (0, 64, 0), "maxDistance": 16}` |
| 向量 | 三元组、带 x/y/z 的字典，或 `Vector3`；具体接受形式看接口 |
| `Promise.then` | 本库 `Promise.then(callback)` / `catch(callback)`；不是 JavaScript Promise 链 |
| 枚举 | 具名常量；有的值为字符串，有的为数值，不依赖枚举序号推断 |
| 保留字成员 | 使用文档列出的 Python 名称，例如体积的 `fromLocation` |

## 生命周期与错误

不要跨存档长期保存引擎对象。实体可能死亡或卸载，容器可能失效，客户端句柄在销毁或维度切换后可能不可用。调用前检查 `isValid`，调用中仍需处理异常；检查与使用之间可能发生状态变化。

坐标、音量和延迟等数值应为有限值。`True` 在 Python 中属于整数的子类，但许多接口明确拒绝用布尔值代替数字。读取返回的副本不会自动修改引擎状态。

计时、跨端通信、多步原生写入与实际渲染都有平台差异，详见 [时序与清理](guides/lifetime.md)、[错误处理](guides/errors.md) 和 [支持情况](compatibility.md)。
''',
"packs/guides/lifetime.md": r'''---
title: 调度、Promise 与资源清理
---

# 调度、Promise 与资源清理

服务端和客户端的计时器都按每个请求单位 0.05 秒换算。它们不保证与微软的执行阶段、客户端渲染帧或网易脚本更新严格一一对应；暂停与卡顿也会改变实际墙钟间隔。

```python
from ModSAPI.server.beta import system

def heartbeat():
    print("heartbeat")

run_id = system.runInterval(heartbeat, 20)

def stop():
    system.clearRun(run_id)

system.runTimeout(stop, 200)
system.waitTicks(2).then(lambda: print("wait completed"))
```

`runTimeout` 支持零延迟；服务端会对负延迟作下限处理，客户端要求非负整数。客户端 `runInterval` 和 `waitTicks` 要求正整数。不要将两端参数校验细节混为一谈。

服务端 `runJob(generator)` 分帧推进生成器，可用 `clearJob(jobId)` 取消。每次生成器步进仍应足够短，不应在游戏主线程执行长时间阻塞 I/O。

```python
from ModSAPI.server.beta import system

def work():
    for number in range(100):
        print(number)
        yield

job_id = system.runJob(work())
# 在所属功能结束时调用 system.clearJob(job_id)。
```

本库 Promise 在完成后保存结果，稍后注册的回调也能收到结果。`then` 与 `catch` 不返回可继续链式调用的新 Promise，不支持 `await`；回调异常不能当作 JavaScript Promise 链来处理。

事件要保留回调引用，并用同一个函数注销。对客户端原生信号，重复订阅同一回调幂等；对其他信号，重复订阅可能替换该回调原有的过滤配置。

```python
from ModSAPI.client.beta import client

def on_key(event):
    print(event.key, event.isDown)

client.afterEvents.keyPress.subscribe(on_key)

def dispose_feature():
    client.afterEvents.keyPress.unsubscribe(on_key)
```

粒子调用 `remove()`、绘图调用 `remove()`、Observable 调用 `dispose()`；音效句柄按需调用 `stop()`。系统销毁会尝试释放自己拥有的资源，但不应依赖销毁去重置其他模组共享的相机或音乐状态。原生释放失败会被报告或记录，不保证失败后引擎资源已消失。
''',
"packs/guides/errors.md": r'''---
title: 参数校验、失败与错误恢复
---

# 参数校验、失败与错误恢复

客户端扩展统一提供 `ExtensionError`、`UnsupportedFeatureError`、`InvalidClientObjectError`、`NativeOperationError`、`StorageDataError`。`NativeOperationError` 保留 `operation`、`code` 和 `cause`，便于区分原生拒绝、能力缺失和原异常。

```python
from ModSAPI.client.beta import client, NativeOperationError, InvalidClientObjectError

def set_fov(value):
    try:
        client.camera.fov = value
    except (TypeError, ValueError) as error:
        print("Invalid FOV: %s" % error)
    except InvalidClientObjectError:
        print("The client session has ended")
    except NativeOperationError as error:
        print(error.operation, error.code, error.cause)
```

较早的服务端封装还会直接传播 `RuntimeError`、`ValueError`、引擎异常或返回原生布尔结果；请看具体成员的错误说明。文档列出的显式 `raise` 不是穷尽列表：组件失效或引擎版本不匹配仍可能产生其他异常。

## 同步错误与异步错误

非法参数通常同步抛出。请求超时、断线、销毁和表单异步失败通过返回的 Promise 拒绝；两层都要处理。

```python
from ModSAPI.client.beta import client

def request_profile():
    try:
        request = client.getDataFromServer("example:profile", {}, timeout=5.0)
    except (TypeError, ValueError) as error:
        print(error)
        return
    request.then(lambda result: print(result))
    request.catch(lambda error: print("Request failed: %s" % error))
```

## 多步操作

相机位置赋值会先脱离跟随再设置位置；替换屏幕可能先弹出旧屏幕再压入新屏幕；存储和容器写入也不是跨原生调用的事务。后续步骤失败时，之前的原生效果可能已经发生。只在明确幂等且仍拥有相关对象时重试，避免吞掉错误后报告成功。

表单关闭和系统销毁会尽量清理所有已拥有的资源；用户回调抛错也不应阻止其他资源的清理。功能代码仍需在 `finally` 中释放自己创建的 Observable 或临时句柄。
''',
"packs/guides/communication.md": r'''---
title: 客户端与服务端通信
---

# 客户端与服务端通信

事件名建议带自己的命名空间，数据使用可传输的基础值。不要发送实体、容器、函数或 UI 对象本身；传 ID，再在接收端重新获取并验证。服务端必须验证玩家身份、参数类型、范围和权限。

## 单向事件

服务端入口：

```python
from ModSAPI.server.beta import world, system

def on_ping(event):
    player = event.player
    if player is None or not player.isValid:
        return
    system.sendToClient(player, "example:pong", {"message": "ready"})

system.afterEvents.clientEventReceive.subscribe("example:ping", on_ping)
```

客户端入口：

```python
from ModSAPI.client.beta import client

def on_pong(event):
    print(event.data["message"])

client.afterEvents.serverEventReceive.subscribe("example:pong", on_pong)
client.sendToServer("example:ping", {})
```

## 请求与响应

先注册响应方，再发起请求。响应回调返回可传输数据，不要返回另一个 Promise。

服务端入口：

```python
from ModSAPI.server.beta import system

def read_profile(event):
    # 此处按 event.player 查询调用玩家的数据，不能信任客户端传入的玩家 ID。
    return {"level": 1}

system.afterEvents.clientRequestData.subscribe("example:profile", read_profile)
```

客户端入口：

```python
from ModSAPI.client.beta import client

request = client.getDataFromServer("example:profile", {}, timeout=5.0)
request.then(lambda profile: print(profile["level"]))
request.catch(lambda error: print(error))
```

反向请求使用 `system.getDataFromClient(player, name, data, timeout)` 与 `client.afterEvents.serverRequestData.subscribe(name, callback)`。客户端返回值不应作为权威游戏状态或权限依据。响应、超时、发送失败、断线与系统销毁都会尝试释放请求所属的订阅和计时器。

`clientCallable`、`serverCallable` 也提供具名函数桥接。它们只是调用路由，不是安全沙箱；必须自己限制可调用函数与输入。普通功能更建议使用明确命名的数据事件或请求。
''',
"packs/guides/storage.md": r'''---
title: 世界存储与客户端配置
---

# 世界存储与客户端配置

`world.getStorage(namespace)` 使用世界 ExtraData；`client.getStorage(namespace, options)` 使用本机配置。二者互不共享，也不会自动网络同步。

```python
from ModSAPI.server.beta import world

storage = world.getStorage("example:quests")
storage.setMany({"version": 1, "completed": []})
quests = storage.get("completed", [])
quests.append("first_steps")
storage.set("completed", quests)
print(storage.has("completed"))
print(storage.getKeys())
```

读取和写入都采用副本。修改 `get()` 的结果不会自动保存。`None` 是可保存的 JSON null；删除键使用 `delete(key)`，不要用 `set(key, None)` 代替删除。

```python
from ModSAPI.client.beta import client

settings = client.getStorage("example:settings", {"isGlobal": True})
settings.set("volume", 0.5)
print(settings.get("volume", 1.0))
settings.delete("unused")
```

`isGlobal=False` 表示本机当前存档配置；`True` 表示本机不同存档共享配置。客户端值可被玩家修改，服务端不能把它当作可信数据。

每个命名空间保存一个 JSON 文档，UTF-8 编码上限 1 MiB、嵌套深度上限 32。键要求非空字符串，拒绝 NaN、无穷、循环引用和不支持的对象；详情见 KeyValueStorage 参考。`setMany` 先校验整批数据，再合并并发出一次原生写入，但不提供跨进程锁或事务。

世界动态属性接口属于另一组已有封装，使用共享 ExtraData。不要假设 `getDynamicPropertyIds()` 只包含本功能的数据，也不要用全局清空方式删除其他功能的内容。
''',
"packs/guides/client-camera.md": r'''---
title: 客户端相机与视角
---

# 客户端相机与视角

`client.camera` 控制当前客户端的相机，采用网易原生坐标和角度约定。

```python
from ModSAPI.client.beta import client, ClientPerspective

camera = client.camera
camera.perspective = ClientPerspective.ThirdPersonBack
camera.fov = 75
camera.pitchLimits = (-60, 60)
print(camera.location.getTuple())
print(camera.rotation.getTuple())
```

FOV 范围为 30–110 度；俯仰上下限均在 -90–90 度内，最小值不能大于最大值。旋转向量的 x/y/z 分别是 pitch/yaw/roll，单位为度。

## 固定相机与恢复跟随

```python
from ModSAPI.client.beta import client

position = client.localPlayer.location
client.camera.location = (position.x, position.y + 4, position.z - 6)
client.camera.rotation = (20, 0, 0)

def restore_following():
    client.camera.resetPosition()

client.runTimeout(restore_following, 60)
```

设置 `location` 先调用脱离跟随，再设置相机中心。`resetPosition()` 恢复跟随，不会自动恢复 FOV、偏移、俯仰限制或透视模式。设置 `anchor` 会改变客户端交互原点，可能影响交互距离体验。

`lock(location, rotation)` 与 `unlock()` 使用原生锁定接口；`detach()` 只脱离跟随。渲染可能到下一帧才反映更改。相机属于本机全局状态，多模组同时控制时需要自己协调，功能结束只恢复自己改变的配置。
''',
"packs/guides/client-audio.md": r'''---
title: 音效、音乐与通知
---

# 音效、音乐与通知

[client.audio.playSound()](../client/reference/Audio.md#playSound) 只在当前客户端播放。需要给所有在线玩家播放时，在服务端遍历 [world.getAllPlayers()](../server/apis/world.md#getAllPlayers)，并调用每个玩家的 [playSound()](../server/apis/player.md#playSound)。

声音标识必须在资源包中实际存在。音效返回 `SoundPlayback` 实例句柄；它的 `id` 是原生播放实例 ID，`soundId` 是声音定义名称。

```python
from ModSAPI.client.beta import client

playback = client.audio.playSound("example:bell", {
    "location": client.localPlayer.location,
    "volume": 0.5,
    "pitch": 1.0,
    "loop": False,
})

def stop_instance():
    playback.stop(0.2)

client.runTimeout(stop_instance, 40)
client.localPlayer.sendToast("Task complete", "Example")
```

音量为 0–1，音高为 0–256，零值会保留。指定 `entity` 时位置是相对偏移，默认零向量；未指定时默认使用本地玩家位置。原生返回 -1 到 -6 会抛出带失败码的 `NativeOperationError`，其中 -6 可能表示声音超出距离范围。

网易原生接口刚播放后立即按实例停止可能失败，不能把计时单位简单当作渲染帧。适配层不会自动无限重试；请捕获失败并根据实际场景决定是否再次停止。

`playback.isStopped` 只表示这个句柄已经成功请求停止，不是实时播放状态查询。`client.audio.stopSound(soundId)` 按定义名停止，可能影响其他脚本启动的实例；停止自己创建的实例应使用句柄。

```python
from ModSAPI.client.beta import client

client.audio.playMusic("example:theme", {"volume": 0.4, "loop": True})
```

音乐会替换当前背景音乐。不支持非零淡入；不要将官方完整音乐选项直接当作已实现。`musicStop` 事件携带声音定义名，不对应场景音效的实例 ID。
''',
"packs/guides/client-events.md": r'''---
title: 客户端事件、MoLang 与本地实体
---

# 客户端事件、MoLang 与本地实体

`keyPress` 提供整数原生键码、`isDown` 和 `screenName`；`mouseWheel.direction` 为 +1 或 -1。不要把原生键码写成 SAPI InputButton 值。

```python
from ModSAPI.client.beta import client

def on_key(event):
    if event.isDown:
        print(event.key, event.screenName)

def on_wheel(event):
    print(event.direction)

client.afterEvents.keyPress.subscribe(on_key)
client.afterEvents.mouseWheel.subscribe(on_wheel)
```

原生客户端信号同步派发，单个订阅者异常会被记录，后续订阅者继续执行。`uiReady` 可能在维度切换后再次触发，初始化逻辑需要支持重复调用；它不是只触发一次的 Promise。

## MoLang 和查询变量

```python
from ModSAPI.client.beta import client

name = "query.mod.example_state"
client.registerQueryVariable(name, 0)
client.localPlayer.setQueryVariable(name, 1)
print(client.localPlayer.getQueryVariable(name))
client.localPlayer.setMolangValue("variable.example_scale", 1.25)
print(client.localPlayer.getMolangValue("variable.example_scale"))

def cleanup():
    client.unregisterQueryVariable(name)
```

只允许注销这个客户端成功注册的查询节点。查询值是原生单精度浮点数，大整数可能失真。写 MoLang 变量仅允许 `variable.*` / `v.*` 和有限数值；表达式错误会检查原生 error 字段。某些只在渲染上下文可用的 query，在普通脚本回调里可能返回零。

## 本地实体

```python
from ModSAPI.client.beta import client

entity = client.spawnEntity("minecraft:pig", client.localPlayer.location, {
    "rotation": (0, 0),
})
print(entity.id, entity.typeId)
if entity.isValid:
    entity.remove()
```

是否支持某个模型取决于网易引擎和资源。只有 `spawnEntity` 返回的本地实体句柄可以移除该实体；`getEntity` 得到的服务端实体句柄不能删掉服务端实体。本地实体不保存，维度切换后可能失效，不能用于服务端碰撞、权限或权威战斗判定。
''',
"packs/guides/client-particles.md": r'''---
title: 粒子、绑定与表达式绘图
---

# 粒子、绑定与表达式绘图

`spawnParticle` 创建资源包中定义的原生发射器。表达式绘图 `spawnDynamicParticle` 使用原生绘图形状，二者生命周期与性能开销不同。

```python
from ModSAPI.client.beta import client

particle = client.spawnParticle("example:spark", client.localPlayer.location, {
    "rotation": (0, 0, 0),
    "molangVariables": {"variable.size": 1.0},
})
particle.setMolang("variable.size", 2.0)
particle.bindToEntity(client.localPlayer, {"bone": "", "offset": (0, 1, 0)})
particle.pause()
particle.resume()
particle.remove()
```

手动 `emit()` 需要资源定义本身支持手动发射。绑定的 `bone=""` 表示根节点；位置与旋转采用原生约定。原生创建返回 0 会视为失败，不会返回一个看似有效的句柄。

```python
from ModSAPI.client.beta import client

drawing = client.spawnDynamicParticle({
    "x": "math.cos(v.emitter_age / 10)",
    "y": 1.5,
    "z": "math.sin(v.emitter_age / 10)",
    "color": (1, 0.5, 0),
}, client.localPlayer.location, {
    "mode": "point",
    "interval": 1,
    "maxAmount": 60,
    "visible": True,
})

def finish():
    if drawing.lastError is not None:
        print(drawing.lastError)
    drawing.remove()

client.runTimeout(finish, 100)
```

表达式不是 Python 任意代码，只接受受限制的语法、变量和函数。绘图年龄按该句柄的自有更新推进；`maxAmount` 限制保留形状数量，不能代替对创建频率的控制。异步更新失败可通过 `lastError` 查看；功能结束要 `remove()`，不要每帧重复创建一组绘图句柄。
''',
"packs/guides/blocks-items.md": r'''---
title: 方块、体积、物品与容器
---

# 方块、体积、物品与容器

方块对象保存维度和坐标，每次读取可反映世界的新状态。负坐标按向下取整定位；区块卸载后读取可能报错，`isValid` 不能消除检查与使用之间的竞态。

```python
from ModSAPI.server.beta import world, BlockVolume, BlockPermutation

dimension = world.getDimension("overworld")
volume = BlockVolume((0, 64, 0), (3, 64, 3))
stone = BlockPermutation.resolve("minecraft:stone")
changed = dimension.fillBlocks(volume, stone)
print(changed.getCapacity())
block = dimension.getBlock((0, 64, 0))
print(block.typeId, block.permutation.getAllStates())
```

完整矩形优先走原生批量路径；带过滤或稀疏体积时可能逐点处理。过滤中的包含条件按并集组合，排除条件优先。默认遇到未加载区块报错；显式允许跳过未加载区块时，返回值只包含实际处理的位置。

`BlockPermutation.getItemStack()` 当前不能保证完整保留方块状态对应的 aux 变种；`Block.getItemStack(withData=True)` 不支持无损方块实体到物品转换。不要用它们搬运箱子内容或保留全部方块 NBT。

## 向玩家背包添加物品

```python
from ModSAPI.server.beta import world, ItemStack

def give_item(player):
    component = player.getComponent("minecraft:inventory")
    if component is None:
        return
    container = component.container
    if container is None or not container.isValid:
        return
    item = ItemStack("minecraft:diamond", 3)
    item.setLore(["Example reward"])
    remainder = container.addItem(item)
    if remainder is not None:
        player.dimension.spawnItem(remainder, player.location)

for player in world.getAllPlayers():
    give_item(player)
```

`getItem()` 返回物品副本；修改后需要 `setItem()` 回写。`getSlot()` 返回槽位包装器，支持的属性赋值会回写该槽位。空槽返回 `None`，不要直接访问其 `typeId`。搜索接口通常忽略数量但比较元数据；查看具体方法说明。

容器合并、转移和回滚可能涉及多次原生写入。失败后应重新读取实际内容，再决定如何恢复，避免根据过期副本重复发放物品。
''',
"packs/guides/server-events.md": r'''---
title: 服务端事件与实体查询
---

# 服务端事件与实体查询

从 `world.afterEvents`、`world.beforeEvents` 和 `system.afterEvents` 获取信号。回调接收本库包装后的事件对象；它的字段与网易原生事件字典不必相同。

```python
# -*- coding: utf-8 -*-
from ModSAPI.server.beta import world

def on_chat(event):
    if event.message == "!hello":
        event.cancel = True
        event.sender.sendMessage(u"你好")

world.beforeEvents.chatSend.subscribe(on_chat)
```

只有实际提供可写取消字段的 before 事件才能取消操作。网易原生事件时序与微软限制执行阶段并不完全一致，不能从名称推断全部执行阶段限制。after 聊天和部分伤害包装会延迟分发，不应假定回调执行时实体依然有效。

## 按维度、位置和距离查询

```python
from ModSAPI.server.beta import world

dimension = world.getDimension("overworld")
entities = dimension.getEntities({
    "type": "minecraft:zombie",
    "location": (0, 64, 0),
    "minDistance": 0,
    "maxDistance": 16,
    "closest": 3,
})
for entity in entities:
    if entity.isValid:
        print(entity.id, entity.location.getTuple())
```

零值条件不是“未填写”，不要用 `if option` 代替 `is not None` 判断。全局 `world.getPlayers()` 与维度查询的范围不同；不要忽略维度条件。选项包装与字典字段详见公共选项参考。

查询结果和事件中的实体对象只代表当前可访问的运行实例。跨回调保存 ID，之后重新 `world.getEntity(id)` 并检查返回值，通常比永久保存对象更稳妥。射线的部分过滤与碰撞面推断仍有实现差异，见支持情况。
''',
"packs/guides/forms.md": r'''---
title: Action、Modal 与 Message 表单
---

# Action、Modal 与 Message 表单

三种构建器都在服务端使用，最终由本库客户端 JSON UI 渲染。返回本库 Promise，成功响应也可能是用户取消；异步失败走 `catch()`。

`ActionFormData` 用于选择操作，`ModalFormData` 收集输入，`MessageFormData` 处理双按钮确认。它们在 `show(player)` 时指定接收玩家。`CustomForm` 和 `MessageBox` 在构造时绑定玩家，适合需要主动关闭、重复展示或动态更新的界面。需要定制客户端控件和布局时，使用 `client.screen` 注册和打开 JSON 界面。

```python
from ModSAPI.server.beta import world
from ModSAPI.serverui.beta import ActionFormData

def show_menu(player):
    form = ActionFormData().title("Example").body("Choose an action")
    form.button("Start").button("Help")
    response = form.show(player)
    def complete(result):
        if result.canceled:
            print(result.cancelationReason)
            return
        print(result.selection)
    response.then(complete)
    response.catch(lambda error: print(error))

players = world.getAllPlayers()
if players:
    show_menu(players[0])
```

## 输入表单

```python
from ModSAPI.serverui.beta import ModalFormData

def show_settings(player):
    form = ModalFormData().title("Settings")
    form.toggle("Enabled", {"defaultValue": True})
    form.slider("Volume", 0, 100, {"valueStep": 5, "defaultValue": 50})
    form.dropdown("Mode", ["Easy", "Hard"], {"defaultValueIndex": 0})
    form.textField("Name", "Input name", {"defaultValue": "Player"})
    response = form.show(player)
    def complete(result):
        if not result.canceled:
            enabled, volume, mode_index, name = result.formValues
            print(enabled, volume, mode_index, name)
    response.then(complete)
    response.catch(lambda error: print(error))
```

滑块上下限和步长必须有限，最小值不大于最大值，步长为正；下拉初始索引从零开始。`header`、`label`、`divider` 等非输入元素在本实现的 `formValues` 对应位置为 `None`，不要在混排后仍按纯输入位置解包。

## 双按钮确认

```python
from ModSAPI.serverui.beta import MessageFormData

def confirm(player):
    form = MessageFormData().title("Confirm").body("Continue?")
    form.button1("Yes").button2("No")
    response = form.show(player)
    response.then(lambda result: print(result.canceled, result.selection))
    response.catch(lambda error: print(error))
```

`selection` 为零起始按钮索引；取消时先检查 `canceled`。支持的 RawMessage 仅限字面 `text/rawtext`；`translate`、`score`、`selector` 和完整微软文本过滤没有实现。`tooltip`、`description`、输入占位符和原生聊天/背包忙碌状态检测仍有缺口，不能仅因参数可传入就认为已经渲染。
''',
"packs/guides/observable-forms.md": r'''---
title: 动态表单与 Observable
---

# 动态表单与 Observable

`CustomForm` 与 `Observable` 提供动态绑定。能被玩家修改的值必须显式设置 `clientWritable=True`，服务端仍会验证所属玩家、类型、范围和选项。

`close()` 结束当前展示，表单仍可再次打开；功能结束时调用 `dispose()` 关闭界面并释放监听器。`MessageBox` 也提供 `dispose()`。独立创建并可能共享的 Observable 由创建者释放。

```python
from ModSAPI.serverui.beta import CustomForm, ObservableBoolean, ObservableNumber

def show_dynamic(player):
    enabled = ObservableBoolean(True, {"clientWritable": True})
    mode = ObservableNumber(0, {"clientWritable": True})
    form = CustomForm(player, "Dynamic settings")
    form.toggle("Enabled", enabled)
    form.dropdown("Mode", mode, [
        {"label": "Easy", "value": 0},
        {"label": "Hard", "value": 1},
    ])
    form.closeButton()
    def cleanup(reason):
        try:
            print(enabled.getData(), mode.getData())
        finally:
            form.dispose()
            enabled.dispose()
            mode.dispose()
    response = form.show()
    response.then(cleanup)
    response.catch(lambda error: print(error))
    return form
```

外部创建的 Observable 由调用者负责清理；不要假设关闭表单自动销毁它。构建器内部临时创建的值由构建器拥有。`dispose()` 后不能再次读取或修改该值；表单销毁后也不能再追加控件。

`show()` 的 Promise 返回关闭原因，而三种标准构建器返回相应 `FormResponse`，不要混用。已关闭或不可见的控件会忽略迟到输入；动态下拉更新会重建变化的原生选项，未变化时复用节点。

## 组合窗口

```python
from ModSAPI.serverui.system import systems

MoreUI = systems.modules.MoreUI

def show_combined(player):
    window = MoreUI(player, {"row": [1], "column": [1, 1]})
    window.addCustomForm("Left").form.label("Content A")
    window.addCustomForm("Right").form.label("Content B")
    window.show()
    return window
```

组合窗口先登记子表单，再 `show()`；`close()` 尝试关闭全部子表单。若发送或用户回调抛错，会在其他子表单完成收尾后报告首个错误。功能不再需要子表单时，仍需释放其订阅和自己持有的 Observable。
''',
"packs/guides/custom-screen.md": r'''---
title: 注册 JSON UI 与屏幕栈
---

# 注册 JSON UI 与屏幕栈

`client.screen` 提供原生屏幕注册、压栈、弹栈和访问栈顶。注册路径必须对应自己的 Python ScreenNode 类和资源包 JSON UI 定义。

```python
from ModSAPI.client.beta import client

def register_ui(event):
    client.screen.registerUI("example:menu", "example.menu", "Scripts_Sample.menu.MenuScreen")

client.afterEvents.uiReady.subscribe(register_ui)

def open_menu():
    return client.screen.pushUI("example:menu", {"title": "Example"})
```

这里的 Python 类路径只是示例：需在自己的脚本包实现 `MenuScreen`，并创建 `example.menu` JSON UI。注册回调必须早于打开操作；`uiReady` 可重复触发，需要确保自己的注册逻辑能安全重复执行。

`screen.top` 是只读的自定义界面栈顶节点，空栈时为 `None`。通过 `pushUI()` 和 `popUI()` 打开或关闭界面，操作前确认栈顶节点属于当前功能。

原生注册、弹栈等返回 false 会报告失败。具体 `push` 返回值由引擎提供，不能把它当作本库动态表单或服务端句柄。高层动态表单见 [动态表单](observable-forms.md)，底层控件和数据类见 server-ui 参考。
''',
}

# These snippets are complete call examples for the principal public objects.
CLASS_EXAMPLES = {
"World": 'from ModSAPI.server.beta import world\n\nfor player in world.getAllPlayers():\n    player.sendMessage("Hello")\nprint(world.getDimension("overworld").id)',
"System": 'from ModSAPI.server.beta import system\n\nrun_id = system.runInterval(lambda: print("tick"), 20)\nsystem.runTimeout(lambda: system.clearRun(run_id), 100)',
"Client": 'from ModSAPI.client.beta import client\n\nprint(client.localPlayer.id)\nclient.localPlayer.sendToast("Ready", "Example")',
"ClientPlayer": 'from ModSAPI.client.beta import client\n\nplayer = client.localPlayer\nprint(player.id, player.location.getTuple())\nplayer.sendToast("Ready", "Example")',
"ClientCamera": 'from ModSAPI.client.beta import client, ClientPerspective\n\ncamera = client.camera\ncamera.perspective = ClientPerspective.ThirdPersonBack\ncamera.fov = 75\nprint(camera.pitchLimits)',
"ClientPerspective": 'from ModSAPI.client.beta import client, ClientPerspective\n\nclient.camera.perspective = ClientPerspective.FirstPerson',
"Audio": 'from ModSAPI.client.beta import client\n\nplayback = client.audio.playSound("example:bell", {"volume": 0.5, "pitch": 1.0})\nprint(playback.id, playback.soundId)',
"SoundPlayback": 'from ModSAPI.client.beta import client\n\nplayback = client.audio.playSound("example:bell", {"loop": True})\nclient.runTimeout(lambda: playback.stop(0.2), 40)',
"ClientEntity": 'from ModSAPI.client.beta import client\n\nentity = client.getEntity(client.localPlayer.id)\nif entity is not None and entity.isValid:\n    print(entity.typeId, entity.location.getTuple())',
"KeyValueStorage": 'from ModSAPI.server.beta import world\n\nstore = world.getStorage("example:data")\nstore.setMany({"version": 1, "visits": 0})\nstore.set("visits", store.get("visits", 0) + 1)\nprint(store.getKeys())',
"Vector3": 'from ModSAPI.server.beta import Vector3\n\nposition = Vector3((1, 64, 2))\noffset = Vector3({"x": 0, "y": 1, "z": 0})\nprint((position + offset).getTuple())\nprint(position.distance)',
"Dimension": 'from ModSAPI.server.beta import world\n\ndimension = world.getDimension("overworld")\nfor entity in dimension.getEntities({"type": "minecraft:pig"}):\n    print(entity.id)',
"Entity": 'from ModSAPI.server.beta import world\n\nfor entity in world.getDimension("overworld").getEntities():\n    if entity.isValid:\n        print(entity.id, entity.typeId)',
"Player": 'from ModSAPI.server.beta import world\n\nfor player in world.getAllPlayers():\n    player.sendMessage("Hello, " + player.name)',
"ItemStack": 'from ModSAPI.server.beta import ItemStack\n\nitem = ItemStack("minecraft:diamond", 3)\nitem.setLore(["Example reward"])\ncopy = item.clone()\nprint(copy.typeId, copy.amount)',
"Block": 'from ModSAPI.server.beta import world\n\nblock = world.getDimension("overworld").getBlock((0, 64, 0))\nif block.isValid:\n    print(block.typeId, block.permutation.getAllStates())',
"BlockPermutation": 'from ModSAPI.server.beta import BlockPermutation\n\npermutation = BlockPermutation.resolve("minecraft:stone")\nprint(permutation.type.id, permutation.getAllStates())',
"BlockVolume": 'from ModSAPI.server.beta import BlockVolume\n\nvolume = BlockVolume((0, 64, 0), (2, 65, 2))\nprint(volume.getCapacity())\nfor location in volume.getBlockLocationIterator():\n    print(location.getTuple())',
"ListBlockVolume": 'from ModSAPI.server.beta import ListBlockVolume\n\nvolume = ListBlockVolume([(0, 64, 0), (2, 64, 2)])\nprint(volume.getCapacity())',
"Container": 'from ModSAPI.server.beta import world, ItemStack\n\nfor player in world.getAllPlayers():\n    inventory = player.getComponent("minecraft:inventory")\n    if inventory is not None and inventory.container.isValid:\n        remaining = inventory.container.addItem(ItemStack("minecraft:apple", 1))\n        print(remaining)',
"ContainerSlot": 'from ModSAPI.server.beta import world\n\nfor player in world.getAllPlayers():\n    inventory = player.getComponent("minecraft:inventory")\n    if inventory is not None:\n        slot = inventory.container.getSlot(0)\n        item = slot.getItem()\n        if item is not None:\n            print(item.typeId)',
"MolangVariableMap": 'from ModSAPI.server.beta import MolangVariableMap\n\nvariables = MolangVariableMap()\nvariables.setFloat("variable.size", 1.5)\nvariables.setColorRGB("variable.color", {"red": 1, "green": 0.5, "blue": 0})\nprint(variables.getData())',
"ActionFormData": 'from ModSAPI.serverui.beta import ActionFormData\n\ndef show(player):\n    result = ActionFormData().title("Menu").button("Start").show(player)\n    result.then(lambda response: print(response.canceled, response.selection))\n    result.catch(lambda error: print(error))',
"MessageFormData": 'from ModSAPI.serverui.beta import MessageFormData\n\ndef show(player):\n    form = MessageFormData().title("Confirm").body("Continue?")\n    form.button1("Yes").button2("No")\n    response = form.show(player)\n    response.then(lambda result: print(result.canceled, result.selection))\n    response.catch(lambda error: print(error))',
"ModalFormData": 'from ModSAPI.serverui.beta import ModalFormData\n\ndef show(player):\n    form = ModalFormData().title("Settings")\n    form.toggle("Enabled", {"defaultValue": True})\n    form.slider("Volume", 0, 100, {"defaultValue": 50, "valueStep": 5})\n    response = form.show(player)\n    response.then(lambda result: print(result.canceled, result.formValues))\n    response.catch(lambda error: print(error))',
"ObservableBoolean": 'from ModSAPI.serverui.beta import ObservableBoolean\n\nvalue = ObservableBoolean(True, {"clientWritable": True})\ntry:\n    value.subscribe(lambda current: print(current))\n    value.setData(False)\nfinally:\n    value.dispose()',
"ObservableNumber": 'from ModSAPI.serverui.beta import ObservableNumber\n\nvalue = ObservableNumber(10, {"clientWritable": True})\ntry:\n    value.setData(15)\n    print(value.getData())\nfinally:\n    value.dispose()',
"ObservableString": 'from ModSAPI.serverui.beta import ObservableString\n\nvalue = ObservableString("Ready")\ntry:\n    value.setData("Done")\n    print(value.getData())\nfinally:\n    value.dispose()',
"Observable": 'from ModSAPI.serverui.beta import Observable\n\nvalue = Observable.create(True, {"clientWritable": True})\ntry:\n    print(value.getData())\nfinally:\n    value.dispose()',
"CustomForm": 'from ModSAPI.serverui.beta import CustomForm\n\ndef show(player):\n    form = CustomForm(player, "Example").label("Hello").closeButton()\n    result = form.show()\n    result.then(lambda reason: form.dispose())\n    result.catch(lambda error: print(error))\n    return form',
"MoreUI": 'from ModSAPI.serverui.system import systems\n\nMoreUI = systems.modules.MoreUI\n\ndef show(player):\n    window = MoreUI(player, {"row": [1], "column": [1, 1]})\n    window.addCustomForm("Left").form.label("A")\n    window.addCustomForm("Right").form.label("B")\n    window.show()\n    return window',
"Promise": '# request 是 getDataFromServer / show / waitTicks 等方法的返回值。\ndef observe(request):\n    request.then(lambda value: print(value))\n    request.catch(lambda error: print(error))',
}

NOTES = {
"World.getStorage": "网易扩展。与客户端存储不共享；每个命名空间为独立 JSON 文档。",
"World.getLootTableManager": "当前为空返回，不能作为已实现的战利品 API 使用。",
"Player.camera": "当前服务端属性为空返回。使用客户端入口的 client.camera 控制本机相机。",
"Player.clientSystemInfo": "当前为空返回；没有可靠的服务端同步系统信息缓存。",
"BlockPermutation.getItemStack": "只保留类型和数量，不能保证将状态完整转换成物品 aux/颜色变种。",
"Block.getItemStack": "withData=True 会明确拒绝；没有无损方块实体到物品转换。",
"Block.type": "每次读取一个原生快照；aux 为网易扩展信息。失效/未加载位置读取会报错。",
"Block.isWaterloggeed": "拼写兼容别名。新代码使用 isWaterlogged。",
"BlockVolume.fromLocation": "Python 名称，不使用保留字 from。体积端点包含边界。",
"System.runTimeout": "原生延迟按 0.05 秒乘请求值换算；服务端负值限制为零，不代表微软执行阶段。",
"System.runInterval": "原生周期按 0.05 秒换算，服务端最小周期为一个请求单位。",
"System.waitTicks": "返回本库 Promise；完成回调不接收参数。销毁时拒绝未完成等待。",
"Container.getItem": "返回物品副本，修改后要 setItem 回写；空槽为 None。",
"Container.addItem": "返回未能放入的剩余 ItemStack；全部放入时为 None。",
"Container.getSlot": "返回槽位包装器；支持的属性修改会回写原生容器。",
"Client.getStorage": "isGlobal=False 为本机存档配置，True 为本机全局配置；不会自动同步服务端。",
"Client.runTimeout": "tickDelay 为非负整数；一个请求单位换算为 0.05 秒，不是渲染帧。",
"Client.runInterval": "tickInterval 为正整数；一个请求单位换算为 0.05 秒。",
"Client.waitTicks": "ticks 为正整数；返回本库 Promise，销毁会拒绝未完成等待。",
"Client.spawnEntity": "只创建本地实体，不保存；只有此方法返回的拥有者句柄可以 remove。",
"Client.spawnParticle": "创建原生粒子发射器，需要资源定义存在；原生 0 表示创建失败。",
"ClientCamera.location": "写入前脱离跟随。后续设置失败不能保证回滚脱离操作。",
"ClientCamera.resetPosition": "恢复跟随，不自动恢复 FOV、偏移、俯仰限制或视角模式。",
"ClientCamera.fov": "有限角度，闭区间 30–110 度。",
"ClientCamera.pitchLimits": "(minimum, maximum)，各自在 -90–90 度内且 minimum <= maximum。",
"ClientCamera.rotation": "x/y/z = pitch/yaw/roll，单位为度，采用网易原生约定。",
"SoundPlayback.isStopped": "仅表示此句柄成功请求停止；不是原生实时播放状态。",
"Audio.stopSound": "按声音定义名停止，可能影响其他脚本；单个实例使用 SoundPlayback.stop。",
"Audio.playMusic": "替换背景音乐；不支持非零淡入。",
"ClientEventSignal.subscribe": "重复订阅同一回调幂等；原生同步分发，订阅者异常分别记录。",
"ClientAfterEvents.uiReady": "可能在维度切换后再次触发，不是只触发一次的事件。",
"CustomForm.show": "Promise 返回关闭原因；与标准构建器返回 FormResponse 的约定不同。",
"CustomForm.dispose": "释放表单拥有的订阅和值；外部 Observable 的所有权仍属于创建者。",
"ModalFormData.textField": "placeholderText 参数被保存，但客户端占位符渲染尚未接入。",
"ModalFormData.show": "formValues 保留非输入元素的位置，并以 None 占位；先检查 canceled。",
"UIManager.closeAllForms": "尽量关闭全部匹配表单，之后抛出首个关闭错误。",
"KeyValueStorage.setMany": "校验整批数据后合并并发出一次写入；不提供跨进程事务或锁。",
"KeyValueStorage.get": "返回副本；None 是合法存储值，缺失键才使用 defaultValue。",
"KeyValueStorage.delete": "成功删除返回 True，键不存在返回 False。",
"Promise.then": "没有链式返回值；不要接着调用 .catch，也不支持 await。",
"Promise.catch": "在原对象注册错误回调；不是 JavaScript Promise 链。",
"CustomCommandRegistry.registerCommand": "只绑定脚本回调；命令声明、参数和权限还需要网易 netease_commands JSON。",
"DataDrivenEntityTriggerAfterEvent.getModifiers": "当前为空实现，不能得到微软组件组修改器上下文。",
}

GUIDES.update({
"packs/guides/scoreboard.md": r'''---
title: 计分板与参与者
---

# 计分板与参与者

从 `world.scoreboard` 获取计分板。先查找目标，再在不存在时创建，避免重复注册。显示名称与目标 ID 是不同字段。

```python
from ModSAPI.server.beta import world

objective = world.scoreboard.getObjective("example_points")
if objective is None:
    objective = world.scoreboard.addObjective("example_points", "Example points")

for player in world.getAllPlayers():
    objective.addScore(player, 1)
    print(player.name, objective.getScore(player))
```

某些操作接受实体、计分板身份或字符串参与者，具体看方法签名。不要把 `ScoreboardIdentity.id` 当作永久的玩家账号 ID；它是包装层运行时身份。假玩家名称也不等价于在线玩家实体。

当前实现部分操作依赖原生命令与 ExtraData 镜像。其他脚本或命令改变计分板后，缓存一致性仍有边界；不能把本库缓存当作跨所有外部命令的事务数据库。
''',
"packs/guides/structures-chunks.md": r'''---
title: 结构模板与区块加载
---

# 结构模板与区块加载

结构从维度中的包含边界区域创建。先使用内存模式验证结果，需要存档持久化时再显式选择 World 保存模式。结构可能包含容器、方块实体和实体，不应当作普通方块数组处理。

```python
from ModSAPI.server.beta import world, StructureSaveMode

dimension = world.getDimension("overworld")
manager = world.structureManager
structure = manager.createFromWorld("example:platform", dimension,
    (0, 64, 0), (3, 64, 3), {
        "includeEntities": False,
        "includeAir": False,
        "saveMode": StructureSaveMode.Memory,
    })
manager.place(structure, dimension, (10, 64, 10))
```

删除结构会使相应包装对象失效。复杂旋转状态、结构中的实体以及实际落盘仍需要网易环境验证；不要承诺与所有微软结构选项完全一致。某些从原生存储读取的结构只能放置，不能通过可编辑调色板接口修改。

## 加载区块后执行操作

```python
from ModSAPI.server.beta import world

dimension = world.getDimension("overworld")
areas = world.tickingAreaManager
area_id = "example_work"
request = areas.createTickingArea(area_id, {
    "dimension": dimension,
    "from": (0, 60, 0),
    "to": (15, 70, 15),
})

def ready():
    try:
        print(dimension.getBlock((0, 64, 0)).typeId)
    finally:
        areas.removeTickingArea(area_id)

request.then(ready)
request.catch(lambda error: print(error))
```

这个接口提供加载等待，不保证开启实体、方块实体或随机 tick。区域标识要独占；不要删除其他功能或命令创建的区域。功能结束应移除自己创建的区域，不依赖退出游戏才释放。
''',
})

ACQUIRE_EXTRA = {
    "Scoreboard": "从 world.scoreboard 获取。",
    "ScoreboardObjective": "通过 world.scoreboard.getObjective(id) 或 addObjective(id, displayName) 获取。",
    "StructureManager": "从 world.structureManager 获取。",
    "TickingAreaManager": "从 world.tickingAreaManager 获取。",
    "Structure": "通过结构管理器创建或读取；原生只读结构不一定支持编辑。",
    "GameRules": "从 world.gameRules 获取；只使用当前实现已映射的规则属性。",
    "ObservableBoolean": "通过 `from ModSAPI.serverui.beta import ObservableBoolean` 导入；构造值必须是 bool。",
    "ObservableNumber": "通过 `from ModSAPI.serverui.beta import ObservableNumber` 导入；构造值必须是有限数值。",
    "ObservableString": "通过 `from ModSAPI.serverui.beta import ObservableString` 导入；构造值必须是字符串。",
    "ObservableUIRawMessage": "通过 `from ModSAPI.serverui.beta import ObservableUIRawMessage` 导入；当前仅支持字面 RawMessage 结构。",
}

GUIDES['packs/guides/native-events.md'] = r'''---
title: 原生事件全覆盖、取消与清理
---

# 原生事件全覆盖、取消与清理

当前目录对照网易 ModSDK 原生文档索引，提供 **120 个客户端、178 个服务端事件绑定**，覆盖输入、UI、音效、实体、玩家、物品、方块、区块、天气、模型、物理和平台事件。服务端事件从 `world` 取得；客户端事件从 `client` 取得。

- [客户端全部事件与前提](../client/events.md)
- [服务端全部事件与前提](../server/native-events.md)

## 风格与边界

```python
from ModSAPI.client.beta import client

def on_entity_added(event):
    print(event.entity, event.engineTypeStr, event.dimension)

signal = client.afterEvents.getNativeEvent('AddEntityClientEvent')
signal.subscribe(on_entity_added)

def cleanup():
    signal.unsubscribe(on_entity_added)
```

信号统一采用 `subscribe(callback)` / `unsubscribe(callback)`。重复订阅同一个函数或绑定方法不会重复调用；订阅返回该回调。没有订阅时不注册原生监听器；最后一个订阅移除时释放监听。客户端或世界销毁时关闭所属信号，不再派发迟到回调。

属性名采用 lowerCamelCase。实体、玩家和维度引用直接返回 `Entity` / `Player` / `Dimension`，客户端对应 `ClientEntity` / `ClientPlayer` / `ClientDimension`；远程玩家使用只含客户端实体能力的 `ClientEntity`。未知引用返回 `None`。原生数字编号和字符串 ID 只通过显式的 `getNativeData()` / `getNativeValue()` 读取。资源名、枚举和物品字典保留其数据语义；Python 保留字 `from` 对应 `fromValue`。

已有 SAPI 事件优先沿用标准名称和参数类型，例如 `effectAdd`、`playerInventoryItemChange`、`itemUse`。不再建立表示同一观察的第二个属性入口。需要检查原生编码时调用 `getNativeEvent(...)`；例如原生滚轮方向仍为 0/1，而 `mouseWheel.direction` 为 -1/+1。

## 查找事件

```python
from ModSAPI.client.beta import client

print(client.beforeEvents.getEventNames())
print(client.afterEvents.getNativeEventNames())

signal = client.beforeEvents.getNativeEvent("ClientItemUseOnEvent")
print(signal.nativeEventName)
```

查询只接受当前端、当前集合目录中的准确原生名；未知名称或错误的 before/after 集合抛出 `KeyError`，不会偷偷创建一个永远不触发的信号。属性入口和 `getNativeEvent` 返回同一个信号。

## 客户端拦截输入与界面

```python
from ModSAPI.client.beta import client

def block_creative_inventory(event):
    if event.isCreative:
        event.cancel = True

def disable_jump(event):
    event.cancel = True

client.beforeEvents.getNativeEvent('ClientPlayerInventoryOpenEvent').subscribe(block_creative_inventory)
client.beforeEvents.getNativeEvent('ClientJumpButtonPressDownEvent').subscribe(disable_jump)
```

`jumpButtonPress.cancel = True` 写入原生 `continueJump = False`；`itemUseOn.cancel = True` 写入原生 `ret = True`。原生字段仍可直接读写。`cancelShears` 只取消剪刀特殊效果，`cancelDrop` 只取消掉落，不会被误包装成取消整个动作。

自定义键位和手柄事件保持原生编码，`isDown` 可能是字符串 `"1"` / `"0"`：

```python
from ModSAPI.client.beta import client

def on_custom_key(event):
    if event.name == "example:action" and event.isDown == "1":
        print("action pressed", event.key)

def on_gamepad_stick(event):
    print(event.key, event.x, event.y)

client.afterEvents.getNativeEvent('OnCustomKeyPressInGame').subscribe(on_custom_key)
client.afterEvents.getNativeEvent('OnGamepadStickClientEvent').subscribe(on_gamepad_stick)
```

键位需要先由模组注册。UI 事件可用于响应屏幕尺寸和原生 HUD 按钮布局变化：

```python
from ModSAPI.client.beta import client

def on_resize(event):
    print(event.beforeX, event.beforeY, event.afterX, event.afterY)

def on_hud_change(event):
    for button in event.changedList or ():
        print(button.get("areaEnum"), button.get("afterSize"))

client.afterEvents.getNativeEvent('ScreenSizeChangedClientEvent').subscribe(on_resize)
client.afterEvents.getNativeEvent('HudButtonChangedClientEvent').subscribe(on_hud_change)
```

## 客户端音效拦截

```python
from ModSAPI.client.beta import client

def filter_sound(event):
    if event.name == "example:muted_sound":
        event.cancel = True

client.beforeEvents.getNativeEvent('PlaySoundClientEvent').subscribe(filter_sound)
```

此事件只影响本机音效播放，不修改服务端状态。播放、停止音乐和场景声音使用不同的原生事件，不应拿音乐定义 ID 当作场景音效实例 ID。

## 服务端伤害、物品与掉落

```python
from ModSAPI.server.beta import world

def cap_damage(event):
    if event.damage is not None and event.damage > 10:
        event.damage = 10.0

def prevent_pickup(event):
    item = event.itemDict or {}
    if item.get("newItemName") == "example:restricted":
        event.cancel = True
        event.pickupDelay = 30

world.beforeEvents.getNativeEvent('DamageEvent').subscribe(cap_damage)
world.beforeEvents.getNativeEvent('ServerPlayerTryTouchEvent').subscribe(prevent_pickup)
```

`DamageEvent` 是吸收计算前的伤害，`ActuallyHurtServerEvent` 是吸收后的可写伤害，`ActorHurtServerEvent` 的最终伤害只读。客户端攻击通知也只读；服务端 `playerAttackEntity` 设置伤害后还需设置 `isValid = 1`。这些原生条件不会因接口名字相似而消失。

掉落列表读取返回副本；修改后必须重新赋值，并设置原生要求的提交标志：

```python
from ModSAPI.server.beta import world

def change_loot(event):
    items = event.itemList or []
    for item in items:
        if item.get("newItemName") == "minecraft:diamond":
            item["count"] = 1
    event.itemList = items
    event.dirty = True

world.beforeEvents.getNativeEvent('EntityDieLoottableServerEvent').subscribe(change_loot)
```

容器战利品使用 `containerLoot` 与 `dirty`；钓鱼使用 `playerFishing` 与 `itemChange`；附魔台选项使用 `itemPutInEnchantingModel` 与 `change`。返回的嵌套容器也不会因原地修改而自动回写。物品 UserData 是否存在取决于原生配置，封装不会修改全局扩展设置。

## 方块与高频事件

```python
from ModSAPI.server.beta import world

def on_block_tick(event):
    if event.blockName == "example:machine":
        print(event.dimension, event.posX, event.posY, event.posZ)

def on_chunk_loaded(event):
    print(event.dimension, event.chunkPosX, event.chunkPosZ)

world.afterEvents.getNativeEvent('ServerBlockEntityTickEvent').subscribe(on_block_tick)
world.afterEvents.getNativeEvent('ChunkLoadedServerEvent').subscribe(on_chunk_loaded)
```

`blockEntityTick` 需要方块配置 `netease:block_entity` 且 `tick = true`，并处于模拟距离或 tickingarea。`entityTick` 需要实体白名单；碰撞、AOI、刚体触发器、方块内部/踩踏事件也需要原生注册或 JSON 开关，逐项见目录。订阅不会自动开启所有检测。

脚本 `tick` 为网易原生每秒 30 次，渲染 `render` 随帧率变化，部分实体/方块 tick 为每秒 20 次。它们与 `runInterval` 的 0.05 秒请求单位不同。在高频回调中优先检查 ID/类型，只处理目标对象；批处理昂贵的全世界扫描，不要每帧创建 UI、读取存档或打印日志。

## 同步写入、平台和失败处理

before 表示 pending action 或仍接受输出的原生钩子，不等于微软的限制执行阶段。部分原生名称含 After 的钩子仍接受后续力学计算参数，会放在 before 集合；最终事件目录是准确入口。只有 SDK 明确接受的输出可写，不能从 before 名称推断所有字段都可写。

取消、掉落列表和力学参数必须在当前同步回调中写完。回调结束或所属对象销毁后，写入抛出 `RuntimeError`；此时仍可读取快照。`getNativeData()` 返回容器副本并保留新版引擎的未知字段，`setNativeValue()` 仍只允许文档确认的输出。原生句柄与任意用户对象保留身份及其原生生命周期，不能把它们当作深度冻结或永久有效的数据。

```python
from ModSAPI.client.beta import client, NativeOperationError

def on_inventory_close(event):
    print(event.nativeEventName)

try:
    client.afterEvents.getNativeEvent('ClientPlayerInventoryCloseEvent').subscribe(on_inventory_close)
except NativeOperationError as error:
    print(error.operation, error.code, error.cause)
```

非函数回调或错误字段类型抛出 `TypeError`；非有限数或已知越界值抛出 `ValueError`；只读/未知字段写入抛出 `AttributeError`；失效客户端、世界或事件集合抛出 `InvalidClientObjectError`。原生订阅/注销失败抛出 `NativeOperationError`，普通注销失败保留订阅以便重试；销毁时即使原生注销失败也先逻辑关闭，避免迟到回调继续操作状态。单个回调异常会被记录，其余订阅者继续执行，已写入原生的输出不会回滚。

某些动作需要客户端和服务端同时取消，例如停止骑乘、开始挖掘、扑灭火焰、释放蓄力物品和剪断绊线。客户端取消不能代替服务端权限校验。`cancelable = False` 的盾牌事件和 `canChange = False` 的耐久事件会拒绝相应写入。

Apollo 旋转攻击、商城、联机大厅、成就等事件仅在对应环境/系统启用后触发。一次性加载事件必须在加载完成前订阅，封装不补发历史事件。旧引擎可能静默忽略新事件，订阅调用成功不代表该事件在当前版本可用；需要按目标引擎和资源做实机验证。本轮未以空实现占位任何目录事件，也没有合成引擎不存在的 after 通知。
'''

GUIDES['packs/guides/client-events.md'] += '\n\n## 完整原生事件\n\n当前额外提供完整的输入、界面、实体、方块、音效与物理事件。见 [客户端事件目录](../client/events.md) 和 [同步取消、输出修改与示例](native-events.md)。\n'
GUIDES['packs/guides/server-events.md'] += '\n\n## 完整原生事件\n\n物品、区块、天气、容器、实体、方块和平台事件见 [服务端事件目录](../server/native-events.md)。可写输出、取消和原生检测前提见 [完整用法与示例](native-events.md)。\n'

GUIDES['packs/guides/semantic-events.md'] = r'''---
title: 语义化事件与筛选
---

# 语义化事件与筛选

ModSAPI 按开发用途提供 55 个事件入口，参考 SAPI 的属性、信号、类型化参数和选项字典设计。多个原生通知可以合并为同一个操作；一个批量原生通知也可以拆成多个有明确用途的回调。

- [客户端语义事件与映射表](../client/semantic-events.md)
- [服务端语义事件与映射表](../server/semantic-events.md)

普通业务优先从这两页查找。已有 SAPI 事件保持标准名称，扩展事件使用 add、remove、change 等动词形式。完整的原生字段、平台条件和检测前提仍可在原生目录查阅，原生入口统一通过 `getNativeEvent` 显式访问。

## 对象引用

回调直接使用 `event.entity`、`event.player`、`event.dimension` 和 `event.otherEntity`，无需再次按 ID 查询。维度未知时为 `None`，不会默认成主世界。客户端维度对象提供身份和会话有效性，不提供服务端世界修改能力。

实体卸载或玩家离开时仍返回对象，身份从对象的 `id` 读取；调用实时接口前检查 `isValid`。`EventBlock.dimension` 同样返回维度对象。订阅筛选 `entities` 和 `dimensions` 接收对象列表，拒绝裸 ID 和数字编号。

```python
from ModSAPI.server.beta import world

def on_weather(event):
    if event.dimension is not None:
        print(event.dimension.id, event.newLevel)

world.afterEvents.weatherChange.subscribe(on_weather, {
    "dimensions": [world.getDimension("overworld")],
})
```

## 设计约定

| 常见需求 | 统一入口 | 整理方式 |
| --- | --- | --- |
| 键盘、手柄、自定义按键 | `client.afterEvents.inputButton` | 多个来源统一为按钮、设备和 Pressed/Released |
| 只处理按下或抬起 | `inputButtonDown` / `inputButtonUp` | 同一来源按状态拆分 |
| 主操作、副操作、点按、长按 | `client.beforeEvents.pointerAction` | 保留原生同步取消能力 |
| 手柄摇杆、扳机 | `inputAxis` / `inputStick` / `inputTrigger` | 合并入口和专用入口共存，保留向量与标量区别 |
| 玩家潜行、冲刺等状态 | `playerStateChange` / `playerSneakChange` 等 | 一个动作事件拆为多个具体状态信号 |
| 背包、主手、副手、盔甲 | `playerInventoryItemChange` / `equipmentChange` | 统一前后物品及所属位置 |
| 实体进入、离开 AOI 区域 | `entityEnterArea` / `entityLeaveArea` | 批量原生数据拆成逐实体事件 |
| 碰撞开始、结束，触发器进入、离开 | `physicsContactBegin` 等 | 批量碰撞对拆成逐对事件 |
| 状态效果新增、刷新、移除 | `effectAdd` / `effectRefresh` / `effectRemove` | 新增沿用已有 SAPI 事件，各入口提供 effect 对象 |
| 全局与独立维度天气强度 | `world.afterEvents.weatherChange` | 保留降雨、雷暴及强度，不猜测未知维度 |
| 实体掉落、箱子战利品、钓鱼掉落 | `world.beforeEvents.lootGenerate` | 统一物品列表写入，自动设置提交标志 |

## 参数类型与关联接口

点击类型名称可查看全部属性、参数、返回值及继承成员。`Optional` 表示允许为空，`Union` 表示多个类型之一；事件数据中的嵌套类型也可继续点击查看。

| 用途 | 事件参数或辅助类型 |
| --- | --- |
| 订阅和筛选 | EventSignal、EventSubscriptionOptions |
| 按键与手柄轴 | InputButtonEvent、InputAxisEvent、InputDevice |
| 指针交互与释放 | PointerActionBeforeEvent、PointerReleaseEvent |
| 玩家状态与实体可见性 | PlayerStateChangeEvent、EntityPresenceEvent |
| 库存与装备 | InventoryChangeEvent、PlayerInventoryItemChangeAfterEvent |
| 状态效果 | EffectAddAfterEvent、EffectChangeEvent、Effect |
| 物品及方块交互 | ItemUseAttemptEvent、BlockInteractionEvent |
| 区域与物理接触 | EntityAreaEvent、PhysicsContactEvent |
| 界面栈与关闭 | ScreenStackChangeEvent、ScreenClosingEvent |
| 天气和战利品 | WeatherLevelChangeEvent、LootGenerateBeforeEvent |
| 物品与方块快照 | EventItemStack、EventBlock |
| 服务端对象引用 | Player、Entity、Dimension |
| 客户端对象引用 | ClientPlayer、ClientEntity、ClientDimension |
| 坐标与原生详情 | Vector3、NativeEventData、NativeEventSignal |

具体事件入口及其参数类型见 [客户端事件目录](../client/semantic-events.md) 和 [服务端事件目录](../server/semantic-events.md)。

## 统一按钮输入与订阅筛选

```python
from ModSAPI.client.beta import client, InputDevice

def on_dash(event):
    print(event.button, event.newButtonState, event.player)

client.afterEvents.customButtonInput.subscribe(on_dash, {
    "buttons": ["example:dash"],
    "state": "Pressed",
    "devices": [InputDevice.Keyboard, InputDevice.Gamepad],
})
```

自定义绑定需先由模组注册。物理按钮的 `button` 是原生编码转成的字符串，自定义按钮则为绑定名称；`key` 保留原始编码。它们没有被强行映射成微软的逻辑 InputButton，因为键位、设备和游戏控制设置可能不同。

```python
from ModSAPI.client.beta import client

def on_press(event):
    print(event.device, event.button, event.isDown)

client.afterEvents.inputButtonDown.subscribe(on_press, {"devices": ["Keyboard"]})
```

主操作可能来自鼠标、触控或手柄，不将它误标成固定物理设备。同步取消写法如下：

```python
from ModSAPI.client.beta import client

def intercept(event):
    event.cancel = True

client.beforeEvents.pointerAction.subscribe(intercept, {"actions": ["Primary", "Tap"]})
```

```python
from ModSAPI.client.beta import client

def on_axis(event):
    if event.controlType == "Stick":
        print(event.key, event.x, event.y)
    else:
        print(event.key, event.value)

client.afterEvents.inputAxis.subscribe(on_axis)
```

扳机没有编造的第二坐标；摇杆也不会被压成标量。需要单一类型时直接订阅 `inputStick` 或 `inputTrigger`。

## 玩家状态

```python
from ModSAPI.server.beta import world

def on_sneak(event):
    print(event.player, event.isEnabled)

world.afterEvents.playerSneakChange.subscribe(on_sneak)
```

客户端提供同名入口。也可只订阅 `playerStateChange` 并传 `{"states": ["sneaking", "sprinting"]}`。已知原生开始、停止动作被解释为新状态；未知动作不会被猜测成某个状态，也不补发订阅前的历史状态。

## 物品变化

```python
from ModSAPI.server.beta import world

def on_inventory(event):
    before = event.beforeItemStack
    after = event.itemStack
    print(event.player, event.inventoryType, event.slot)
    print(before.typeId if before else None, after.amount if after else 0)

world.afterEvents.playerInventoryItemChange.subscribe(on_inventory, {
    "inventoryTypes": ["Inventory"],
    "allowedSlots": [0, 1, 2],
    "includeItems": ["minecraft:diamond"],
    "ignoreQuantityChange": True,
})
```

`includeItems` 和 `excludeItems` 会考虑前后两个物品，所以移除目标物品也能被筛选出来。`ignoreQuantityChange` 仅在提供了旧物品、且除数量之外的原生元数据相同时忽略通知。旧数据未提供时 `hasPreviousItem` 为 False；旧槽位为空但字段已提供时为 True。

`inventoryType` 为 Inventory、Mainhand、Offhand 或 Armor。一次玩家操作可能改变多个存储位置，会保留各位置的通知；封装不按相同时间戳丢掉真实变化。客户端原生主手通知缺少旧物品和槽位时，对应属性保持未知。

`EventItemStack` 提供只读的 `typeId`、`amount`、`clone()`、`withAmount()` 和 `getItemDict()`，保留可用的原生元数据和用户数据。它在两端都不需要查引擎，不会因修改快照而修改背包。新建数量为 1..255；读取已有超量物品保留实际数量。

## 自动处理战利品提交

```python
from ModSAPI.server.beta import world, EventItemStack

def replace_loot(event):
    event.itemStacks = [EventItemStack("minecraft:diamond", 1)]

world.beforeEvents.lootGenerate.subscribe(replace_loot, {
    "lootTypes": ["Entity", "Container", "Fishing"],
})
```

这一个入口接收实体死亡掉落、容器战利品和钓鱼掉落。写入 `itemStacks` 会先校验全部物品，再提交原生 `itemList`，并自动写入正确的 `dirty` 或 `itemChange`。可以传快照、现有服务端 ItemStack 或完整原生物品字典；赋空列表即可清空掉落。

写入只在当前同步回调中有效；不对实体死亡本身进行取消，也不合成不存在的成功后事件。`nativeEvent` 仍保留来源特有字段。

## 交互中的主体、物品与坐标

```python
from ModSAPI.client.beta import client

def inspect_use(event):
    block = event.block
    if block and block.typeId == "example:locked":
        event.cancel = True
    if event.itemStack:
        print(event.itemStack.typeId, event.itemStack.amount)

client.beforeEvents.playerUseItemOnBlock.subscribe(inspect_use)
```

`itemUse` 处理尝试使用物品，`playerUseItemOnBlock` 处理物品对方块的使用，`playerInteractWithBlock` 处理已配置监听的方块交互。它们保留不同的原生触发范围，避免把重叠的钩子合并后对同一次交互重复执行逻辑。

主体通过 `player` / `entity` / `source` 延迟取得；客户端远程玩家是 ClientEntity，本地玩家复用 `client.localPlayer`。句柄可能已经失效，需检查 `isValid`。所属会话销毁后对象仍可读取身份；客户端对象的 isValid 返回 False。

`block` 是只读 EventBlock，含 `typeId`、复制的位置和已知维度对象。`blockLocation`、`faceLocation`、`location` 都是复制的 Vector3。来源没有维度时保留 None；服务端维度已知时可用 `event.dimension.getBlock(event.blockLocation)` 显式读取当前方块。封装不假定未知方块位于主世界。

## 区域与物理

```python
from ModSAPI.server.beta import world

def entered(event):
    print(event.areaName, event.entity)

world.afterEvents.entityEnterArea.subscribe(entered, {"areaNames": ["example:room"]})
```

区域需要先通过原生 AOI 注册；每个进入/离开的实体分别调用一次回调。原生区域事件只提供区域名和实体 ID，不凭空加入维度。离开时实体可能已经失效；可读取事件实体对象的身份信息进行资源清理。

```python
from ModSAPI.client.beta import client

def contact(event):
    print(event.entity, event.otherEntity, event.location)

client.afterEvents.physicsContactBegin.subscribe(contact, {"entities": [client.localPlayer]})
```

`physicsContactEnd`、`physicsTriggerEnter`、`physicsTriggerLeave` 同样支持逐对处理。`entities` 过滤匹配任一参与者；原生两者顺序不表示固定的触发器/被触发者角色。碰撞细节、检测开关和 物理碰撞掩码 仍由原生配置决定；无详细检测时位置、法线保持 None。

## 界面与效果

```python
from ModSAPI.client.beta import client

def top_changed(event):
    print(event.operation, event.topScreenName)

client.afterEvents.screenStackChange.subscribe(top_changed)
```

Pop 后原生给出的是新顶层界面，因此使用明确的 `topScreenName` / `topScreenDefinition`。要读即将移除的界面，订阅 `client.beforeEvents.screenClose`，其字段描述 outgoing screen；该通知无法取消关闭。不会把新顶层界面错误标成被关闭的界面。

```python
from ModSAPI.server.beta import world

def effect_changed(event):
    print(event.entity, event.changeType, event.effect.typeId, event.effect.duration)

world.afterEvents.effectRefresh.subscribe(effect_changed, {"effectTypes": ["minecraft:speed"]})
```

效果新增使用原有的 `effectAdd`，读取 `event.effect` 和 `event.entity`。刷新使用 `effectRefresh`，移除使用 `effectRemove`，二者同样返回 effect 对象。`effect.duration` 将原生秒数乘 20 转成名义 SAPI tick 数；刷新、移除事件的 `durationSeconds` 保留原值。原生永久效果的特殊数值仍需按目标引擎判断。

`weatherChange` 统一 Rain / Thunder 及强度变化，提供 `isGlobal`、`dimension`、`previousLevel`、`newLevel`。全局天气不假定某个固定维度，不把强度渐变误解成一次天气切换。

## 筛选、错误与性能

所有语义信号接受 `subscribe(callback, options=None)`。公共筛选为 `entities`、`entityTypes`、`dimensions`；各信号专有选项见目录。`entities` 和 `dimensions` 接收对象，空列表匹配零个事件。传入的筛选会复制，同一回调再次订阅可更新其筛选；保存回调以便注销。

已移除的实体若未由原生事件提供类型，`entityTypes` 可能无法再查询到它，不能据此保证收到卸载通知。需要可靠清理时向 `entities` 传入之前保存的实体对象；此筛选只比较身份，不要求实体仍有效。

不支持的选项、拼写错误和无效枚举会抛出 ValueError，错误类型抛出 TypeError。每个用户回调独立处理异常，其他订阅者继续执行。不会因为过滤一个维度或物品而自动开启额外的检测。

多个便利入口复用同一原生源；只在首次订阅时安装引擎监听。ID、已知类型、物品和坐标先从快照筛选，只有显式的 entityTypes 查询可能在原生类型缺失时查引擎。大批量事件逐项派发，退出或注销可立即停止后续回调。

多来源订阅中途失败会回滚已订阅来源。语义信号注销先逻辑禁用回调；若原生注销失败会抛出 NativeOperationError，重复 unsubscribe 可重试残余清理，已禁用回调不再运行。这与原生高级信号保留订阅以便重试的约定不同。销毁会关闭所属信号，保留其他消费者的监听。
'''

GUIDES['packs/guides/native-events.md'] += '\n\n## 更便捷的业务入口\n\n优先使用 [语义化事件与筛选](semantic-events.md)，从按键、玩家状态、库存变化、战利品和区域等需求出发；本页继续提供准确的原生映射与约束。\n'

ACQUIRE_EXTRA.update({
    'EventSignal':'从 client/world 的 beforeEvents 或 afterEvents 属性获取；不自行构造。',
    'EventItemStack':'从语义化事件读取，或从对应端 beta 导入并创建待写入战利品的值。',
    'EventBlock':'从语义化方块交互事件的 block 属性读取；这是纯数据快照。',
    'InputDevice':'从 ModSAPI.client.beta 导入，用于输入事件的 devices 筛选。',
})


GUIDES['packs/guides/script-events.md'] = r'''---
title: 脚本指令事件
---

# 脚本指令事件

`system.afterEvents.scriptEventReceive` 通过服务端的 GlobalCommandServerEvent 监听完整指令字符串，从 `/scriptevent <id> <message>` 中取得事件标识和消息。无需将 scriptevent 注册为自定义命令，也不依赖原生自定义命令的参数数组。

## 订阅与获取消息

```python
from ModSAPI.server.beta import system


def on_script_event(event):
    print(event.id, event.message)
    if event.sourceEntity is not None:
        print(event.sourceEntity.id)


system.afterEvents.scriptEventReceive.subscribe(on_script_event, {
    "namespaces": ["modsapi"],
})


def cleanup():
    system.afterEvents.scriptEventReceive.unsubscribe(on_script_event)
```

执行以下指令：

```text
/scriptevent modsapi:process {"text": "hello  world", "value": 1}
```

回调中 `id` 为 `modsapi:process`，`message` 为 `{"text": "hello  world", "value": 1}`。消息内部及末尾的空白、引号和选择器文本保持原样；只有标识与消息之间的分隔空白被去除。不会自动解析消息中的 JSON，也不会自行将选择器替换为实体名称。省略消息时得到空字符串。

指令可带或不带开头的斜线，也支持 `minecraft:scriptevent`。标识必须包含非空的命名空间和名称；保留的 minecraft 命名空间、格式错误或不相关的指令不会触发此事件。

## 筛选与来源对象

`namespaces` 按完整命名空间匹配；省略、设为 None 或传空列表时接收全部有效标识。订阅时复制筛选条件，之后修改原列表不会改变已注册的筛选。类型不合法时抛出 TypeError，未知选项或不合法的名称抛出 ValueError。

事件参数为 ScriptEventCommandMessageAfterEvent。实体来源包装为 Entity 或 Player，可从 `sourceEntity` 读取；命令方块来源包装为 Block，可从 `sourceBlock` 读取，其维度保留原生值。无法确定的来源对象为 None。`sourceType` 使用 ScriptEventSource 常量；全局钩子不提供对话发起者，因此 `initiator` 始终为 None，也不会仅凭实体类型猜测对话来源。

## 触发时机

网易全局指令钩子在执行前同步触发，所以收到本事件不等于引擎已经完成执行或通过权限校验。业务需要自行验证来源及消息内容。适配器保留原生指令数据和取消状态，已被取消的指令不分发。

外层 execute 的条件与执行上下文交由引擎处理。只有引擎实际报告具体的 scriptevent 指令时才解析，不从外层字符串模拟执行，以免条件未满足时错误触发回调。

接口参考：ScriptEventCommandMessageAfterEventSignal、ScriptEventCommandMessageAfterEvent、SystemAfterEvents。
'''

NOTES['SystemAfterEvents.scriptEventReceive'] = '基于全局执行前钩子解析完整指令，覆盖原生钩子报告的聊天栏、接口、命令方块及行为包命令。事件不会证明引擎执行成功。用法见脚本指令事件指南。'
NOTES['ScriptEventCommandMessageAfterEventSignal.subscribe'] = '仅监听 GlobalCommandServerEvent，不依赖自定义命令注册或参数数组。格式错误或已取消的指令会被忽略；不会改写原生指令和取消标志。'


GUIDES['packs/guides/sapi-modsdk-bridge.md'] = '---\ntitle: SAPI 与 ModSDK 双向通信\n---\n\n# SAPI 与 ModSDK 双向通信\n\nJavaScript 入口位于 `core_behavior/scripts/netease/index.js`。SAPI 仍在服务端运行，通过桥接调用 Python 服务端或指定玩家的 ModSDK 客户端。两端均使用命名空间标识、选项对象、消息信号和显式注册的处理器。\n\n`main.js` 已加载桥接模块；业务处理器放在自己的模块中，再从入口导入。传输复用脚本指令和网易客户端通信，不会为每条消息创建实体。\n\n## 在 SAPI 调用 Python 服务端\n\nSAPI 端：\n\n```javascript\nimport { system } from "@minecraft/server";\nimport { server } from "./netease/index.js";\n\nsystem.run(async () => {\n  try {\n    const result = await server.request("example:double", { value: 21 });\n    console.warn(result.value);\n  } catch (error) {\n    console.warn(error.code, error.remoteName, error.message);\n  }\n});\n```\n\nPython 服务端：\n\n```python\nfrom ModSAPI.server.beta import system\n\n\ndef double_value(event):\n    value = event.data["value"]\n    if isinstance(value, bool) or not isinstance(value, (int, long, float)):\n        raise TypeError("value must be numeric")\n    return {"value": value * 2}\n\n\nsystem.scriptBridge.registerHandler("example:double", double_value)\n```\n\n处理器可以直接使用 ModSDK 或本库包装类。只有已注册的标识可以被调用，不按字符串执行任意 Python 代码。重复注册同名处理器会报错；功能结束时调用 `unregisterHandler`。\n\n## 直接使用补充能力\n\n以下代码中的 `player` 为原生 SAPI 的 [Player](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/player?view=minecraft-bedrock-stable) 对象。\n\n```javascript\nimport { server, client } from "./netease/index.js";\n\nasync function inspectPlayer(player) {\n  const nbt = await server.getEntityNbt(player);\n  const local = client.forPlayer(player);\n  await local.showToast("连接成功", "ModSAPI");\n  const camera = await local.getCameraState();\n  await local.setCameraFov(75);\n  return { nbt, camera };\n}\n```\n\nNBT 读取由 Python 服务端的原生实体组件执行；提示和相机操作由指定玩家的 ModSDK 客户端执行。原生能力缺失、对象失效或操作失败都会使异步结果失败。读取的 NBT 仍须符合数据类型和大小限制。\n\n## 调用 ModSDK 客户端处理器\n\n客户端 Python：\n\n```python\nfrom ModSAPI.client.beta import client\n\n\ndef read_local_name(event):\n    return {"name": client.localPlayer.name}\n\n\nclient.scriptBridge.registerHandler("example:local_name", read_local_name)\n```\n\nSAPI 端取得玩家后调用：\n\n```javascript\nimport { client } from "./netease/index.js";\n\nasync function readName(player) {\n  return await client.forPlayer(player).request("example:local_name");\n}\n```\n\n`forPlayer` 接受玩家对象，返回缓存的 [PlayerBridge](#playerbridge)。玩家离开时，对应连接失效，待完成请求会失败；不会将其他客户端的响应匹配到此玩家。\n\n## 从 Python 调用 SAPI\n\nSAPI 注册处理器：\n\n```javascript\nimport { server, client } from "./netease/index.js";\n\nserver.registerHandler("example:format", event => ({ text: String(event.data.value) }));\nclient.registerHandler("example:acknowledge", event => {\n  event.player.sendMessage("已收到客户端请求");\n  return { accepted: true };\n});\n```\n\nPython 服务端请求 `server` 上的处理器：\n\n```python\nfrom ModSAPI.server.beta import system\n\nrequest = system.scriptBridge.request("example:format", {"value": 42})\nrequest.then(lambda result: print(result["text"]))\nrequest.catch(lambda error: print(error.code, error.remoteName))\n```\n\nPython 客户端请求对应玩家连接或 `client.registerHandler` 注册的处理器：\n\n```python\nfrom ModSAPI.client.beta import client\n\nrequest = client.scriptBridge.request("example:acknowledge", {"ready": True})\nrequest.then(lambda result: print(result["accepted"]))\nrequest.catch(lambda error: print(error.code))\n```\n\nJavaScript 使用原生 Promise，可用 `await`。Python 使用本库 Promise，通过 `then`、`catch` 接收结果，不支持直接套用 JavaScript 的异步语法。\n\n## 消息通知与注销\n\nSAPI 服务端连接的通知信号为 `server.afterEvents.messageReceive`；单个玩家使用 `client.forPlayer(player).afterEvents.messageReceive`；所有客户端的通知可统一订阅 `client.afterEvents.messageReceive`。\n\n```javascript\nimport { client } from "./netease/index.js";\n\nconst callback = client.afterEvents.messageReceive.subscribe(event => {\n  console.warn(event.player.name, event.id, event.data);\n}, { ids: ["example:status"] });\n\n// 功能结束时调用：\n// client.afterEvents.messageReceive.unsubscribe(callback);\n```\n\nPython 客户端发送通知：\n\n```python\nfrom ModSAPI.client.beta import client\n\nclient.scriptBridge.sendMessage("example:status", {"ready": True}).catch(\n    lambda error: print(error.code))\n```\n\nPython 两端的通知信号分别为 `system.scriptBridge.afterEvents.messageReceive` 与 `client.scriptBridge.afterEvents.messageReceive`，用法与其他事件相同。通知的异步结果只确认本地原生传输接受了全部分包；需要远端处理结果时使用 `request`。\n\n## 数据与对象引用 {#bridgevalue}\n\n[BridgeValue](#bridgevalue) 支持空值、布尔值、有限数值、字符串、数组及字符串键字典，也支持原生 SAPI 的 [Entity](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/entity?view=minecraft-bedrock-stable)、[Dimension](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/dimension?view=minecraft-bedrock-stable) 和 [Block](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/block?view=minecraft-bedrock-stable) 引用。Python 端自动恢复为对应包装类；Python 返回这些对象时，SAPI 端恢复为原生对象。\n\n```javascript\nasync function inspectEntity(player) {\n  return await server.request("example:inspect_entity", { entity: player });\n}\n```\n\n```python\ndef inspect_entity(event):\n    entity = event.data["entity"]\n    if not entity.isValid:\n        raise ValueError("entity is no longer valid")\n    return {"entity": entity, "location": entity.location}\n```\n\n传输不会使实体保持加载。对象在解码时已失效或客户端不可见时，返回 `INVALID_REFERENCE`；客户端独有实体无法因此变成服务端实体。客户端不提供可修改世界的方块包装能力，涉及方块操作请使用服务端处理器。\n\n字符串、字典和数组会复制；循环引用、函数、非有限数值及不支持的对象会报错。Python 整数须处于 JavaScript 安全整数范围。单个序列化数据包最多 64 KiB，嵌套最多 32 层。选择器文本按原文传输，不会被命令解析器展开。\n\n## 连接与公共方法 {#bridge}\n\n[Bridge](#bridge) 由运行时管理，使用 `server` 或 `client.forPlayer(player)` 获取。Python 对应类型为 ScriptBridge。\n\n| 成员 | 参数与返回值 |\n| --- | --- |\n| `isValid` | 只读布尔值，表示本地连接及目标玩家是否仍有效 |\n| `player` | 只读的原生玩家对象；服务端连接不提供玩家 |\n| `afterEvents` | [BridgeAfterEvents](#bridgeafterevents) |\n| `sendMessage(id, data)` | 命名空间标识、[BridgeValue](#bridgevalue)；返回无结果的异步完成通知 |\n| `request(id, data, options)` | 命名空间标识、数据、[BridgeRequestOptions](#bridgerequestoptions)；异步返回远端结果 |\n| `registerHandler(id, callback)` | 回调接收 [BridgeMessageAfterEvent](#bridgemessageafterevent)，可返回数据或异步结果 |\n| `unregisterHandler(id)` | 返回布尔值，表示处理器是否存在 |\n| `dispose()` | 使待完成请求失败，释放本连接的订阅、处理器和待发送数据 |\n\n## 服务端连接 {#serverbridge}\n\n[ServerBridge](#serverbridge) 继承 [Bridge](#bridge)，通过 `server` 单例获取。\n\n| 补充方法 | 参数与结果 |\n| --- | --- |\n| `getEntityNbt(entity, options)` | 原生实体对象和请求选项；异步返回 ModSDK 读取的 NBT 数据 |\n\n## 单个玩家连接 {#playerbridge}\n\n[PlayerBridge](#playerbridge) 继承 [Bridge](#bridge)，其 `player` 始终为选中的原生玩家对象。\n\n| 补充方法 | 参数与结果 |\n| --- | --- |\n| `showToast(message, title, options)` | 文本、可选标题和请求选项；异步完成本地提示显示请求 |\n| `getCameraState(options)` | 请求选项；异步返回 [ClientCameraState](#clientcamerastate) |\n| `setCameraFov(fov, options)` | 30–110 度的有限视野角度和请求选项；异步完成原生设置 |\n\n## 客户端连接管理 {#clientbridgemanager}\n\n[ClientBridgeManager](#clientbridgemanager) 通过 `client` 单例获取。\n\n| 成员 | 说明 |\n| --- | --- |\n| `forPlayer(player)` | 取得该玩家的 [PlayerBridge](#playerbridge) |\n| `disconnect(player)` | 释放该玩家的连接 |\n| `afterEvents.messageReceive` | 所有客户端的消息通知；事件的玩家对象必定存在 |\n| `registerHandler(id, callback)` | 为当前和后续玩家连接注册共同的 SAPI 处理器 |\n| `unregisterHandler(id)` | 注销共同处理器；保留连接自己注册的其他处理器 |\n\n## 事件集合与信号 {#bridgeafterevents}\n\n[BridgeAfterEvents](#bridgeafterevents) 包含只读的 `messageReceive`，类型为 [BridgeEventSignal](#bridgeeventsignal)。\n\n### 订阅信号 {#bridgeeventsignal}\n\n`subscribe(callback, options)` 返回传入的回调；`unsubscribe(callback)` 注销它。重复订阅同一回调会替换筛选条件；回调抛错会单独报告，后续订阅者仍会执行。选项类型见 [BridgeEventOptions](#bridgeeventoptions)。\n\n### 消息参数 {#bridgemessageafterevent}\n\n| 属性 | 类型与含义 |\n| --- | --- |\n| `id` | 字符串，命名空间消息或处理器名称 |\n| `data` | [BridgeValue](#bridgevalue)，当前消息的解码数据 |\n| `player` | 可选的原生玩家对象；客户端连接及所有客户端通知中必定存在 |\n\n`ClientBridgeMessageAfterEvent` 使用相同字段，并保证 `player` 存在。Python 参数类型为 ScriptBridgeMessage；客户端为 ClientPlayer 对象，服务端为 None。\n\n### 事件筛选选项 {#bridgeeventoptions}\n\n`BridgeEventOptions.ids` 为可选字符串数组，逐项按完整消息标识匹配。省略时接收全部消息，空数组不匹配任何消息；注册时复制，之后修改原数组不会改变筛选。\n\n### 请求选项 {#bridgerequestoptions}\n\n`BridgeRequestOptions.timeoutTicks` 为可选整数，范围 1–1200，默认 200。每单位为 1/20 秒，Python 端也遵循此换算。超时从本地提交请求开始计时，包含排队和网络等待；不会撤销远端已开始执行的操作。\n\n### 相机状态 {#clientcamerastate}\n\n`ClientCameraState.location`、`rotation` 为复制的三维坐标，`fov` 为角度数值，`perspective` 为 `FirstPerson`、`ThirdPersonBack` 或 `ThirdPersonFront`。旋转遵循网易原生的俯仰、偏航、翻滚约定。\n\n## 错误与生命周期 {#bridgeerror}\n\nSAPI 端使用 [BridgeError](#bridgeerror)，Python 端使用 ScriptBridgeError。`code` 为错误码，`remoteName` 保留远端异常类型，`message` 为异常说明。\n\n| 错误码 | 含义 |\n| --- | --- |\n| `TIMEOUT` | 等待远端结果超时 |\n| `DISPOSED` | 连接、所属系统或目标玩家已失效 |\n| `DISCONNECTED` | 服务端转发时发现玩家离线 |\n| `NOT_READY` | ModSDK 客户端尚未获得服务端通信会话 |\n| `TRANSPORT_ERROR` | 原生指令、通信或计时器调用失败 |\n| `UNKNOWN_HANDLER` | 远端没有注册指定处理器 |\n| `DUPLICATE_HANDLER` | 本地重复注册处理器 |\n| `INVALID_REFERENCE` | 对象已失效、不可见或当前端无法恢复此引用 |\n| `PAYLOAD_TOO_LARGE` | 序列化数据包超过限制 |\n| `PROTOCOL_ERROR` | 版本、分包或路由数据不合法 |\n| `BUSY` | 待完成请求、队列或分包缓存达到上限 |\n| `REMOTE_ERROR` | 远端处理器抛出了普通异常 |\n\n处理器应验证业务数据及权限。通信成功不能替代业务授权。客户端路由会校验服务端分发到该玩家连接的会话信息，并核对待完成请求所属玩家。\n\n系统销毁或玩家离开时会清理请求和订阅。SAPI 层只卸载某项功能时，先调用 `unregisterHandler`、`unsubscribe` 或 `dispose`；共享连接被销毁后，使用它的其他功能也会失去连接。\n\n协议使用固定的私有脚本事件通道，单个分包不超过 1800 个字符，发送队列每次最多处理 16 个分包。未完成分包在十秒后释放，重复分包不会再次交付已完成的数据包。该机制不提供持久队列、事务或断线重放；需要结果确认时使用请求，而不是通知。\n'

NOTES['ScriptBridge.__init__'] = '由 system.scriptBridge 或 client.scriptBridge 创建并持有；业务代码不直接构造传输器。'
NOTES['ScriptBridgeMessageSignal.subscribe'] = 'ids 按完整标识匹配，空列表不匹配任何通知；绑定方法可使用同一对象的新方法引用注销。'
CLASS_EXAMPLES['ScriptBridge'] = 'from ModSAPI.server.beta import system\n\ndef echo(event):\n    return event.data\n\nsystem.scriptBridge.registerHandler("example:echo", echo)\n\ndef cleanup():\n    system.scriptBridge.unregisterHandler("example:echo")'
