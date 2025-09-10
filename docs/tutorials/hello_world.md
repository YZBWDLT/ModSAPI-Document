---
sidebar_position: 1
---

# 编写 Hello World!

## 准备工作

跟随[***快速开始***](../intro.md)完成ModSAPI模组的导入、配置工作

## 开始编写

打开示例包中的文件 `index.py`

编写如下代码
```python title="b/Scripts_Sample/index.py"
print("Hello World!")
```

现在进入游戏（记得同时装载测试包），后台将会显示`Hello World!`

## 进阶

#### 目标：
编写一段代码，当玩家发送`Hello`时，向玩家发送`World`

#### 代码：
```python title="b/Scripts_Sample/index.py"
def onChatSend(arg):
    if arg.message == 'Hello':
        # 如果发送的消息是"Hello"
        arg.sender.sendMessage("World")
        # 发送"World"

world.afterEvents.chatSend.subscribe(onChatSend)
# 注册监听事件-玩家发送消息事件
```

现在进入游戏，发送`Hello`，聊天框中将同时出现`World`!
