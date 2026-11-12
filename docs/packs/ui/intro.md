---
sidebar_position: 1
title: 界面与主题表单
---

# 界面与主题表单

入口：[client.ui](../client/apis/manager.md#ui)、[system.ui](../server/reference/System.md#ui) 和 ModSAPI.ui。视图、控件、主题、状态和组合表单共用现有运行时。

[视图与生命周期](../guides/managed-ui.md) · [布局与控件](../guides/ui-layout-and-widgets.md) · [选择控件与小地图](../guides/ui-choices-and-minimap.md) · [模型与图片](../guides/ui-models-and-images.md) · [组合表单](../guides/themed-forms.md) · [动画与跟随界面](../guides/ui-animation-and-hud.md) · [自定义模板](../guides/ui-custom-controls.md)

[场景与完整示例](../examples.md) · [支持情况与差异](../compatibility.md)

<div className="modsapi-table-scroll" tabIndex={0} aria-label="接口表格，可横向滚动">

| 类型 | 说明 |
| --- | --- |
| [Button](reference/Button.md) | 按钮模板描述，包含按钮节点与文字节点的路径。 |
| [ButtonCallbacks](reference/ButtonCallbacks.md) | 可选处理函数接收触发交互的玩家包装对象。 |
| [Control](reference/Control.md) | 通过统一入口登记具有明确类型的控件描述。 |
| [ControlDescriptor](reference/ControlDescriptor.md) | 控件模板描述基类；创建回调在客户端执行。 |
| [ControlStyle](reference/ControlStyle.md) | 签名、字段、属性、方法与调用示例 |
| [CreateArguments](reference/CreateArguments.md) | 签名、字段、属性、方法与调用示例 |
| [Custom](reference/Custom.md) | 自定义模板，支持客户端创建和状态更新回调。回调参数包含原生控件、屏幕及独立的参数副本；嵌套状态更新按顶层参数名通知。 |
| [Divider](reference/Divider.md) | 无交互分割线的模板描述。 |
| [Dropdown](reference/Dropdown.md) | 下拉框模板描述，包含弹出容器和已登记的选项模板。 |
| [DropdownItem](reference/DropdownItem.md) | 静态下拉选项；label 和 value 本身不接受状态绑定。 |
| [FluentStyles](reference/FluentStyles.md) | Fluent 风格的浅色和深色模板标识。 |
| [FlutterStyles](reference/FlutterStyles.md) | Flutter／Material 风格的浅色和深色模板标识。 |
| [Form](reference/Form.md) | 两端通用的主题组合表单，使用包装后的玩家对象作为显示目标。 |
| [FormCloseEvent](reference/FormCloseEvent.md) | 签名、字段、属性、方法与调用示例 |
| [FormSession](reference/FormSession.md) | 本次显示的表单会话；目标玩家关闭或离线时释放相应监听。 |
| [FormStyle](reference/FormStyle.md) | 签名、字段、属性、方法与调用示例 |
| [GridLayout](reference/GridLayout.md) | 签名、字段、属性、方法与调用示例 |
| [GridPosition](reference/GridPosition.md) | 签名、字段、属性、方法与调用示例 |
| [Group](reference/Group.md) | 由具名控件组成的注册模板，组内位置相对根节点计算。 |
| [GroupChildData](reference/GroupChildData.md) | 子控件的值；嵌套组合控件使用 children，各种控件均可提供 params。 |
| [GroupControlStyle](reference/GroupControlStyle.md) | 登记的组合控件子项定义；class 必填，布局字段可以省略。 |
| [GroupStyle](reference/GroupStyle.md) | 签名、字段、属性、方法与调用示例 |
| [InnerStyles](reference/InnerStyles.md) | 内置 OreUI、Flutter 和 Fluent 风格的模板标识集合。 |
| [Label](reference/Label.md) | 文字标签模板描述，可选客户端创建回调。 |
| [ListView](reference/ListView.md) | 滚动列表模板描述，selectedPath 指向每行内部的选中标记。 |
| [ListViewItem](reference/ListViewItem.md) | 普通列表行，value 必须唯一；行内字段本身不接受状态绑定。 |
| [ListViewStyle](reference/ListViewStyle.md) | 签名、字段、属性、方法与调用示例 |
| [Observable](reference/Observable.md) | 具有独立数据副本、顺序更新队列和可释放派生值的状态对象。运算符生成派生状态；布尔转换读取当前值，取得普通结果时使用 value 或 getValue。 |
| [ObservableUpdateArguments](reference/ObservableUpdateArguments.md) | 签名、字段、属性、方法与调用示例 |
| [OreUIStyles](reference/OreUIStyles.md) | 内置 OreUI 风格表单和控件的模板标识。 |
| [ScrollingPanel](reference/ScrollingPanel.md) | 表单面板模板描述，包含滚动区域、标题和关闭按钮路径。 |
| [Slider](reference/Slider.md) | 滑动条模板描述，包含滑动条、标题和数值标签路径。 |
| [TextField](reference/TextField.md) | 文本输入模板描述，包含原生控件路径和可选创建回调。 |
| [Theme](reference/Theme.md) | 在创建表单的一端登记静态主题样式。 |
| [Toggle](reference/Toggle.md) | 开关模板描述，包含开关节点和文字节点路径。 |
| [UiAnchor](reference/UiAnchor.md) | anchorFrom、anchorTo 和 setAnchors 接受的锚点常量。 |
| [UiAnimation](reference/UiAnimation.md) | 单个原生动画通道，完成、取消或视图关闭时释放。支持透明度、位置、尺寸和图片裁剪比例；原生只写属性需要明确的起始值，时长以秒计。暂停后调用 play 继续播放。 |
| [UiAnimationEvent](reference/UiAnimationEvent.md) | 控件动画完成或失败时的事件参数。 |
| [UiAnimationEvents](reference/UiAnimationEvents.md) | 动画原生完成及适配失败信号，不通过轮询检测完成。 |
| [UiAnimationOptions](reference/UiAnimationOptions.md) | 签名、字段、属性、方法与调用示例 |
| [UiButton](reference/UiButton.md) | 按钮控件，提供可取消的指针与悬浮事件订阅。 |
| [UiButtonEvents](reference/UiButtonEvents.md) | 按需启用的原生按钮订阅，事件参数使用包装对象。 |
| [UiChoiceEvent](reference/UiChoiceEvent.md) | 选择事件的独立快照，不公开原生事件字典中的其他字段。 |
| [UiComboBox](reference/UiComboBox.md) | 本地原生下拉框，与表单中的组合下拉控件分别使用。选项值为普通数据的独立副本；原生读取接口只提供文字和索引，不提供已有选项自定义值的读取方法。 |
| [UiComboBoxEvents](reference/UiComboBoxEvents.md) | 原生下拉框弹出、收起及选中选项的事件容器。 |
| [UiComboBoxOption](reference/UiComboBoxOption.md) | 本地原生下拉框选项的可选显示图标。 |
| [UiControl](reference/UiControl.md) | 由视图拥有的原生控件；原生操作要求所属视图存活且已经就绪。 |
| [UiEntityRenderOptions](reference/UiEntityRenderOptions.md) | 实体预览的变换参数与可选整数渲染深度。 |
| [UiEvent](reference/UiEvent.md) | 本地界面事件参数，提供包装后的玩家、视图和控件引用。 |
| [UiEventSignal](reference/UiEventSignal.md) | 由所属界面对象管理的事件信号；订阅返回可重复调用的取消函数。 |
| [UiGrid](reference/UiGrid.md) | 由原生模板驱动的网格控件，与表单的权重布局分别使用。 |
| [UiHudOptions](reference/UiHudOptions.md) | 签名、字段、属性、方法与调用示例 |
| [UiImage](reference/UiImage.md) | 图片控件，支持贴图、裁剪，以及围绕自身锚点或全局位置的原生旋转。 |
| [UiImageClipDirection](reference/UiImageClipDirection.md) | [UiImage.clipDirection](reference/UiImage.md#clipDirection) 接受的裁剪方向常量。 |
| [UiImageFit](reference/UiImageFit.md) | [UiImage.setImageFit](reference/UiImage.md#setImageFit) 接受的图片适配方式。 |
| [UiImageInsets](reference/UiImageInsets.md) | 九宫格的左、右、上、下边距；全部为非负有限数值。 |
| [UiInputPanel](reference/UiInputPanel.md) | 原生输入面板，支持模态、输入拦截和拖拽偏移设置。 |
| [UiItem](reference/UiItem.md) | 只读的物品显示值，与背包和堆叠数量无关。特殊物品可通过 userData 提供渲染数据；原生预览读取接口不返回这部分数据，因此不能从现有控件恢复。此值不导入或查询服务端组件。 |
| [UiItemOptions](reference/UiItemOptions.md) | 签名、字段、属性、方法与调用示例 |
| [UiItemRenderer](reference/UiItemRenderer.md) | 物品预览控件；修改显示内容不会改变任何背包。 |
| [UiLabel](reference/UiLabel.md) | 文字标签控件，支持读取和设置文字及三通道颜色。 |
| [UiMapMarker](reference/UiMapMarker.md) | 由界面管理的图片或文字标记，移除时不影响其他标记。 |
| [UiMapMarkerOptions](reference/UiMapMarkerOptions.md) | 地图图片标记的尺寸，以及仅用于实体标记的旋转选项。 |
| [UiMapTextMarkerOptions](reference/UiMapTextMarkerOptions.md) | 地图文字标记的缩放选项；文字内容单独传入。 |
| [UiMiniMap](reference/UiMiniMap.md) | 显示已加载客户端区块的小地图，可管理固定和跟随实体的标记。显示效果由原生模板与渲染规则决定；标记属于地图当前维度，只渲染 X/Z 坐标。 |
| [UiModelRenderer](reference/UiModelRenderer.md) | 由当前视图管理的网易模型预览控件。切换预览内容只更新控件，不向世界发起创建实体的请求。省略的选项沿用原生默认值；关闭视图或移除控件时，沿用引擎的界面所有权释放预览。 |
| [UiModelTransformOptions](reference/UiModelTransformOptions.md) | 三类模型预览共用的独立变换参数。 |
| [UiProgressBar](reference/UiProgressBar.md) | 原生进度条，提供只写的归一化进度设置。 |
| [UiScrollView](reference/UiScrollView.md) | 滚动容器；滚动进度统一为 0～1。 |
| [UiSelectionWheel](reference/UiSelectionWheel.md) | 由原生模板提供可选扇区的轮盘控件。 |
| [UiSelectionWheelEvents](reference/UiSelectionWheelEvents.md) | 悬浮选项变化与指针完成选择的事件容器。 |
| [UiService](reference/UiService.md) | 管理本地视图以及组合表单、状态工厂。原生视图在客户端操作；服务端创建表单并向玩家对象显示，不能直接读取远端原生界面树。 |
| [UiSkeletonRenderOptions](reference/UiSkeletonRenderOptions.md) | 骨骼预览的变换、动画播放和原生光照选项。 |
| [UiSlider](reference/UiSlider.md) | 原生滑动条，数值范围和步进由界面模板决定。 |
| [UiStackPanel](reference/UiStackPanel.md) | 原生堆叠布局，按水平或垂直方向排列子控件。 |
| [UiTextField](reference/UiTextField.md) | 原生文本输入控件，通过 value 读取和设置输入内容。 |
| [UiToggle](reference/UiToggle.md) | 使用编辑器模板中 this_toggle 子节点的开关控件。 |
| [UiView](reference/UiView.md) | 本地界面或常驻视图；视图关闭时，它拥有的控件和绑定随之失效。 |
| [UiViewCallbacks](reference/UiViewCallbacks.md) | 签名、字段、属性、方法与调用示例 |
| [UiViewDefinition](reference/UiViewDefinition.md) | 一个界面注册标识及其资源模板和生命周期回调配置。 |
| [UiViewEvents](reference/UiViewEvents.md) | 单个视图的就绪、更新和关闭生命周期信号。 |
| [UiViewOptions](reference/UiViewOptions.md) | 签名、字段、属性、方法与调用示例 |

</div>