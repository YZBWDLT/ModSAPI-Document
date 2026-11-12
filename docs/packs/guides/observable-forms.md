---
title: 动态表单与 Observable
---

# 动态表单与 Observable

[CustomForm](../server_ui/reference/CustomForm.md) 与 [Observable](../ui/reference/Observable.md) 提供动态绑定。能被玩家修改的值必须显式设置 `clientWritable=True`，服务端仍会验证所属玩家、类型、范围和选项。

`close()` 结束当前展示，表单仍可再次打开；功能结束时调用 `dispose()` 关闭界面并释放监听器。[MessageBox](../server_ui/reference/MessageBox.md) 也提供 `dispose()`。独立创建并可能共享的 [Observable](../ui/reference/Observable.md) 由创建者释放。

```python
from __future__ import print_function

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

外部创建的 [Observable](../ui/reference/Observable.md) 由调用者负责清理；不要假设关闭表单自动销毁它。构建器内部临时创建的值由构建器拥有。`dispose()` 后不能再次读取或修改该值；表单销毁后也不能再追加控件。

`show()` 的 [Promise](../common/reference/Promise.md) 返回关闭原因，而三种标准构建器返回相应 [FormResponse](../server_ui/reference/FormResponse.md)，不要混用。已关闭或不可见的控件会忽略迟到输入；动态下拉更新会重建变化的原生选项，未变化时复用节点。

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

组合窗口先登记子表单，再 `show()`；`close()` 尝试关闭全部子表单。若发送或用户回调抛错，会在其他子表单完成收尾后报告首个错误。功能不再需要子表单时，仍需释放其订阅和自己持有的 [Observable](../ui/reference/Observable.md)。