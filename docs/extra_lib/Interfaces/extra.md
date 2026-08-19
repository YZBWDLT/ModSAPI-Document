---
sidebar_position: 4
---

# 枚举与常量

## ButtonCallbacks {#ButtonCallbacks}

创建按钮时需要传入的回调函数。

### 键

onClick: () -> None

按钮按下时触发（按下并抬起时）

onMoveIn: () -> None

手指移动入按钮范围内时触发

onMoveOut: () -> None

手指移出按钮范围时触发

## ControlStyle {#ControlStyle}

控件样式定义

### 键

class: str

控件样式定义，由`Control.register`注册

offsetX: str | int | float | [Observable](./observable)

X方向位移。

offsetY: str | int | float | [Observable](./observable)

Y方向位移。

width: str | int | float | [Observable](./observable)

宽度。

height: str | int | float | [Observable](./observable)

高度。

visible: bool | [Observable](./observable)

可见性。
