---
title: 脚本指令事件
---

# 脚本指令事件

[system.afterEvents.scriptEventReceive](../server/reference/SystemAfterEvents.md#scriptEventReceive) 通过服务端的 [GlobalCommandServerEvent](../server/native-events.md#globalcommandserverevent) 监听完整指令字符串，从 `/scriptevent <id> <message>` 中取得事件标识和消息。无需将 scriptevent 注册为自定义命令，也不依赖原生自定义命令的参数数组。

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

`namespaces` 按完整命名空间匹配；省略、设为 [None](../common/type-system.md#none) 或传空列表时接收全部有效标识。订阅时复制筛选条件，之后修改原列表不会改变已注册的筛选。类型不合法时抛出 [TypeError](../common/type-system.md#typeerror)，未知选项或不合法的名称抛出 [ValueError](../common/type-system.md#valueerror)。

事件参数为 [ScriptEventCommandMessageAfterEvent](../server/reference/ScriptEventCommandMessageAfterEvent.md)。实体来源包装为 [Entity](../server/apis/entity.md) 或 [Player](../server/apis/player.md)，可从 `sourceEntity` 读取；命令方块来源包装为 [Block](../server/apis/block.md)，可从 `sourceBlock` 读取，其维度保留原生值。无法确定的来源对象为 [None](../common/type-system.md#none)。`sourceType` 使用 [ScriptEventSource](../common/reference/ScriptEventSource.md) 常量；全局钩子不提供对话发起者，因此 `initiator` 始终为 [None](../common/type-system.md#none)，也不会仅凭实体类型猜测对话来源。

## 触发时机

网易全局指令钩子在执行前同步触发，所以收到本事件不等于引擎已经完成执行或通过权限校验。业务需要自行验证来源及消息内容。适配器保留原生指令数据和取消状态，已被取消的指令不分发。

外层 execute 的条件与执行上下文交由引擎处理。只有引擎实际报告具体的 scriptevent 指令时才解析，不从外层字符串模拟执行，以免条件未满足时错误触发回调。

接口参考：[ScriptEventCommandMessageAfterEventSignal](../server/reference/ScriptEventCommandMessageAfterEventSignal.md)、[ScriptEventCommandMessageAfterEvent](../server/reference/ScriptEventCommandMessageAfterEvent.md)、[SystemAfterEvents](../server/reference/SystemAfterEvents.md)。