---
title: 界面流程与原生扩展
---

# 界面流程与原生扩展

使用 [client.ui](manager.md#ui) 声明和打开视图，通过 [UiView](../../ui/reference/UiView.md) 获取控件、绑定状态并处理交互。主题组合表单同时支持客户端与服务端。

- [完整视图流程与模板示例](../../guides/managed-ui.md)
- [主题表单与响应式状态](../../guides/themed-forms.md)
- [动画、常驻和跟随界面](../../guides/ui-animation-and-hud.md)
- [布局、网格与物品预览](../../guides/ui-layout-and-widgets.md)
- [自定义模板与控件组](../../guides/ui-custom-controls.md)

已有的 [client.screen](manager.md#screen) 提供直接管理原生 [ScreenNode](../../common/type-system.md#screennode) 的兼容入口；通过它创建的节点由调用者管理。需要本库统一释放控件、订阅和动画时，使用 [client.ui](manager.md#ui) 管理视图。