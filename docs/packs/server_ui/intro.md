---
sidebar_position: 1
title: 标准表单
---

# 标准表单

标准表单入口：`from ModSAPI.serverui.beta import ActionFormData, ModalFormData, MessageFormData`。其他类型与入口见 [导出符号](../exports.md)。

标准构建器在服务端调用；JSON [UI](reference/UI.md) 控件底层类型在客户端工作，不要混用执行端。

[场景与完整示例](../examples.md) · [支持情况与差异](../compatibility.md)

<div className="modsapi-table-scroll" tabIndex={0} aria-label="接口表格，可横向滚动">

| 类型 | 说明 |
| --- | --- |
| [ActionFormData](reference/ActionFormData.md) | 签名、字段、属性、方法与调用示例 |
| [ActionFormResponse](reference/ActionFormResponse.md) | 操作表单的玩家响应数据。 |
| [BackgroundData](reference/BackgroundData.md) | 签名、字段、属性、方法与调用示例 |
| [Button](reference/Button.md) | 按钮控件。 |
| [ButtonCallbackArgument](reference/ButtonCallbackArgument.md) | 按钮回调函数参数 |
| [ButtonData](reference/ButtonData.md) | 按钮的数据定义。 |
| [ButtonOptions](reference/ButtonOptions.md) | 签名、字段、属性、方法与调用示例 |
| [ButtonTextures](reference/ButtonTextures.md) | 签名、字段、属性、方法与调用示例 |
| [ButtonTouchCallbacks](reference/ButtonTouchCallbacks.md) | 签名、字段、属性、方法与调用示例 |
| [Control](reference/Control.md) | 控件基类 |
| [ControlData](reference/ControlData.md) | 全部控件数据的基类。 |
| [ControlGroupOptions](reference/ControlGroupOptions.md) | 签名、字段、属性、方法与调用示例 |
| [CustomControlGroup](reference/CustomControlGroup.md) | 可添加到表单中的控件组。 |
| [CustomForm](reference/CustomForm.md) | 可自定义的动态表单，支持按钮、标签、开关、下拉框、滑块等控件。基于 [Observable](reference/Observable.md)，观察值变化时会更新表单。 |
| [CustomOptions](reference/CustomOptions.md) | 签名、字段、属性、方法与调用示例 |
| [DataDrivenScreenClosedReason](reference/DataDrivenScreenClosedReason.md) | 签名、字段、属性、方法与调用示例 |
| [DividerOptions](reference/DividerOptions.md) | 签名、字段、属性、方法与调用示例 |
| [DragableButton](reference/DragableButton.md) | 可拖动按钮控件。 |
| [DragableButtonData](reference/DragableButtonData.md) | 可拖动按钮的数据定义。 |
| [DropdownItem](reference/DropdownItem.md) | 签名、字段、属性、方法与调用示例 |
| [DropdownOptions](reference/DropdownOptions.md) | 签名、字段、属性、方法与调用示例 |
| [DynamicForm](reference/DynamicForm.md) | 动态表单的基类，包括 [CustomForm](reference/CustomForm.md) 和 MessageForm。 |
| [FormCancelationReason](reference/FormCancelationReason.md) | 签名、字段、属性、方法与调用示例 |
| [FormLayout](reference/FormLayout.md) | 签名、字段、属性、方法与调用示例 |
| [FormLayoutDict](reference/FormLayoutDict.md) | 签名、字段、属性、方法与调用示例 |
| [FormRejectError](reference/FormRejectError.md) | 签名、字段、属性、方法与调用示例 |
| [FormRejectReason](reference/FormRejectReason.md) | 签名、字段、属性、方法与调用示例 |
| [FormResponse](reference/FormResponse.md) | 表单响应的基类。 |
| [FormVisibilityError](reference/FormVisibilityError.md) | 签名、字段、属性、方法与调用示例 |
| [FormVisibilityErrorReason](reference/FormVisibilityErrorReason.md) | 签名、字段、属性、方法与调用示例 |
| [Image](reference/Image.md) | 图像的数据定义。 |
| [ImageData](reference/ImageData.md) | 图像的数据定义。 |
| [InvalidFormError](reference/InvalidFormError.md) | 签名、字段、属性、方法与调用示例 |
| [InvalidFormModificationError](reference/InvalidFormModificationError.md) | 签名、字段、属性、方法与调用示例 |
| [InvalidObservableError](reference/InvalidObservableError.md) | 签名、字段、属性、方法与调用示例 |
| [Label](reference/Label.md) | 文本标签控件。 |
| [LabelData](reference/LabelData.md) | 文本标签的数据定义。 |
| [LabelOptions](reference/LabelOptions.md) | 签名、字段、属性、方法与调用示例 |
| [MessageBox](reference/MessageBox.md) | 签名、字段、属性、方法与调用示例 |
| [MessageBoxResult](reference/MessageBoxResult.md) | 签名、字段、属性、方法与调用示例 |
| [MessageFormData](reference/MessageFormData.md) | 签名、字段、属性、方法与调用示例 |
| [MessageFormResponse](reference/MessageFormResponse.md) | 选择值 0 对应 button1，选择值 1 对应 button2。 |
| [ModalFormData](reference/ModalFormData.md) | 签名、字段、属性、方法与调用示例 |
| [ModalFormDataDropdownOptions](reference/ModalFormDataDropdownOptions.md) | 签名、字段、属性、方法与调用示例 |
| [ModalFormDataSliderOptions](reference/ModalFormDataSliderOptions.md) | 签名、字段、属性、方法与调用示例 |
| [ModalFormDataTextFieldOptions](reference/ModalFormDataTextFieldOptions.md) | 签名、字段、属性、方法与调用示例 |
| [ModalFormDataToggleOptions](reference/ModalFormDataToggleOptions.md) | 签名、字段、属性、方法与调用示例 |
| [ModalFormResponse](reference/ModalFormResponse.md) | 操作表单的玩家响应数据。 |
| [MoreUI](reference/MoreUI.md) | 由多个表单组成的自定义界面。 |
| [MoreUICustomData](reference/MoreUICustomData.md) | 签名、字段、属性、方法与调用示例 |
| [MoreUILayout](reference/MoreUILayout.md) | 布局配置。 |
| [MoreUILayoutDict](reference/MoreUILayoutDict.md) | 签名、字段、属性、方法与调用示例 |
| [Observable](reference/Observable.md) | 可被观察的数据，主要用于界面更新。 |
| [ObservableBoolean](reference/ObservableBoolean.md) | 签名、字段、属性、方法与调用示例 |
| [ObservableNumber](reference/ObservableNumber.md) | 签名、字段、属性、方法与调用示例 |
| [ObservableOptions](reference/ObservableOptions.md) | 签名、字段、属性、方法与调用示例 |
| [ObservableString](reference/ObservableString.md) | 签名、字段、属性、方法与调用示例 |
| [ObservableUIRawMessage](reference/ObservableUIRawMessage.md) | 签名、字段、属性、方法与调用示例 |
| [Options](reference/Options.md) | 签名、字段、属性、方法与调用示例 |
| [Panel](reference/Panel.md) | 面板的数据定义。 |
| [PanelData](reference/PanelData.md) | 面板的数据定义。 |
| [PlayerLeftError](reference/PlayerLeftError.md) | 签名、字段、属性、方法与调用示例 |
| [ScreenData](reference/ScreenData.md) | 屏幕的数据定义。 |
| [ScreenUI](reference/ScreenUI.md) | 签名、字段、属性、方法与调用示例 |
| [ScrollPanel](reference/ScrollPanel.md) | 滚动面板（竖向） |
| [ScrollPanelData](reference/ScrollPanelData.md) | 签名、字段、属性、方法与调用示例 |
| [SliderOptions](reference/SliderOptions.md) | 签名、字段、属性、方法与调用示例 |
| [SpacerOptions](reference/SpacerOptions.md) | 签名、字段、属性、方法与调用示例 |
| [TextFieldOptions](reference/TextFieldOptions.md) | 签名、字段、属性、方法与调用示例 |
| [TextFilteringError](reference/TextFilteringError.md) | 签名、字段、属性、方法与调用示例 |
| [Textures](reference/Textures.md) | 签名、字段、属性、方法与调用示例 |
| [ToggleOptions](reference/ToggleOptions.md) | 签名、字段、属性、方法与调用示例 |
| [TraceData](reference/TraceData.md) | 签名、字段、属性、方法与调用示例 |
| [UI](reference/UI.md) | 本库专有的自定义界面。 |
| [UIManager](reference/UIManager.md) | 签名、字段、属性、方法与调用示例 |
| [Variables](reference/Variables.md) | 签名、字段、属性、方法与调用示例 |

</div>