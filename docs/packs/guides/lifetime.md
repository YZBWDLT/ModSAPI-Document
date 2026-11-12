---
title: 调度、Promise 与资源清理
---

# 调度、Promise 与资源清理

服务端和客户端的计时器都按每个请求单位 0.05 秒换算。它们不保证与微软的执行阶段、客户端渲染帧或网易脚本更新严格一一对应；暂停与卡顿也会改变实际墙钟间隔。

```python
from __future__ import print_function

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

本库 [Promise](../common/reference/Promise.md) 在完成后保存结果，稍后注册的回调也能收到结果。`then` 与 `catch` 不返回可继续链式调用的新 [Promise](../common/reference/Promise.md)，不支持 `await`；回调异常不能当作 JavaScript [Promise](../common/reference/Promise.md) 链来处理。

事件要保留回调引用，并用同一个函数注销。对客户端原生信号，重复订阅同一回调幂等；对其他信号，重复订阅可能替换该回调原有的过滤配置。

```python
from ModSAPI.client.beta import client

def on_key(event):
    print(event.key, event.isDown)

client.afterEvents.keyPress.subscribe(on_key)

def dispose_feature():
    client.afterEvents.keyPress.unsubscribe(on_key)
```

粒子调用 `remove()`、绘图调用 `remove()`、[Observable](../ui/reference/Observable.md) 调用 `dispose()`；音效句柄按需调用 `stop()`。系统销毁会尝试释放自己拥有的资源，但不应依赖销毁去重置其他模组共享的相机或音乐状态。原生释放失败会被报告或记录，不保证失败后引擎资源已消失。