---
title: 参数校验、失败与错误恢复
---

# 参数校验、失败与错误恢复

客户端扩展统一提供 [ExtensionError](../common/reference/ExtensionError.md)、[UnsupportedFeatureError](../common/reference/UnsupportedFeatureError.md)、[InvalidClientObjectError](../common/reference/InvalidClientObjectError.md)、[NativeOperationError](../common/reference/NativeOperationError.md)、[StorageDataError](../common/reference/StorageDataError.md)。[NativeOperationError](../common/reference/NativeOperationError.md) 保留 `operation`、`code` 和 `cause`，便于区分原生拒绝、能力缺失和原异常。

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

较早的服务端封装还会直接传播 [RuntimeError](../common/type-system.md#runtimeerror)、[ValueError](../common/type-system.md#valueerror)、引擎异常或返回原生布尔结果；请看具体成员的错误说明。文档列出的显式 `raise` 不是穷尽列表：组件失效或引擎版本不匹配仍可能产生其他异常。

## 同步错误与异步错误

非法参数通常同步抛出。请求超时、断线、销毁和表单异步失败通过返回的 [Promise](../common/reference/Promise.md) 拒绝；两层都要处理。

```python
from __future__ import print_function

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

表单关闭和系统销毁会尽量清理所有已拥有的资源；用户回调抛错也不应阻止其他资源的清理。功能代码仍需在 `finally` 中释放自己创建的 [Observable](../ui/reference/Observable.md) 或临时句柄。