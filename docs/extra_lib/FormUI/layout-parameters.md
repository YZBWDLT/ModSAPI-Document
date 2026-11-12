---
title: 界面布局
---

# 界面布局

界面功能已整合到 ModSAPI.ui。通过 [client.ui](../../packs/client/apis/manager.md#ui) 或 [system.ui](../../packs/server/reference/System.md#ui) 使用现有运行时，不需要额外注册系统。

[完整教程与示例](../../packs/guides/themed-forms.md) · [界面模块全部类型](../../packs/ui/intro.md)

```python
from ModSAPI.ui import Form, Observable, Control, Theme
```

服务端显示表单时传入 [Player](../../packs/server/apis/player.md) 对象；客户端省略目标时使用本地玩家。关闭结果通过 player 属性取得包装对象。

[Form](../../packs/ui/reference/Form.md) · [Observable](../../packs/ui/reference/Observable.md) · [Control](../../packs/ui/reference/Control.md) · [Theme](../../packs/ui/reference/Theme.md)