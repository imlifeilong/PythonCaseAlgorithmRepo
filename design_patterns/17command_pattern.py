"""
命令模式是一种行为型设计模式，它将请求发送者和接收者解耦，将一个请求封装成一个对象，从而使得不同的请求可以被参数化、排队、操作和日志化。

在命令模式中，请求被封装成一个命令对象，包含了调用操作的对象和调用的方法。命令对象可以被存储、传递、调用和取消。这样，命令模式可以实现请求的发送者和接收者之间的解耦，以及对请求进行灵活的控制。

优点：
解耦请求发送者和接收者：命令模式将请求的发送者和接收者解耦，使得它们不需要直接相互关联。

可扩展性：通过添加新的命令类，可以轻松扩展命令模式，符合开闭原则。

可组合命令：命令模式支持将多个命令组合成一个复合命令，实现更复杂的操作。

支持撤销和恢复：可以通过保存历史命令对象的方式支持撤销和恢复功能。

缺点：
可能引起类膨胀：每个具体命令类都需要一个对应的命令对象，可能会导致类的数量膨胀。

调用时的性能开销：在某些情况下，命令模式的实现可能引入额外的调用开销。

实际开发中的使用：
命令模式在实际开发中常用于以下场景：

需要将请求发送者和接收者解耦：当需要解耦请求发送者和接收者，以支持更灵活的命令处理时，可以考虑使用命令模式。

支持撤销和恢复功能：当需要实现撤销和恢复功能时，命令模式提供了一种方便的方式来管理命令的历史记录。
"""


# 命令接口
class Command:
    def execute(self):
        pass


# 具体命令A
class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()


# 具体命令B
class LightOffCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()


# 接收者
class Light:
    def turn_on(self):
        print("开灯")

    def turn_off(self):
        print("关灯")


# 调用者
class RemoteControl:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def press_button(self):
        self._command.execute()


# 客户端代码
if __name__ == "__main__":
    # 创建接收者对象
    light = Light()

    # 创建具体命令对象
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # 创建调用者对象
    remote = RemoteControl()

    # 设置具体命令对象并执行
    remote.set_command(light_on)
    remote.press_button()  # 输出 "Light is ON"

    # 切换具体命令对象并执行
    remote.set_command(light_off)
    remote.press_button()  # 输出 "Light is OFF"
