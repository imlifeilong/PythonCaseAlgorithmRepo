"""
桥接模式是一种结构型设计模式，它将抽象部分与实现部分分离，使它们可以独立变化。桥接模式通过将继承关系转换为组合关系，使得抽象和实现可以独立地变化，互不影响。

在桥接模式中，有两个关键的角色：抽象部分和实现部分。抽象部分定义了抽象类和抽象接口，实现部分定义了实现类和实现接口。通过桥接模式，抽象部分和实现部分可以分别扩展，而不相互制约。

优点：
分离抽象和实现：桥接模式将抽象部分和实现部分分离，使它们可以独立变化，符合开闭原则。

适应变化：抽象和实现可以独立扩展，不影响彼此，可以更灵活地适应变化。

优秀的扩展能力：桥接模式通过组合而非继承的方式，具有很好的扩展能力。

缺点：
增加复杂度：桥接模式引入了抽象和实现的分离，可能会增加系统的复杂度。

对客户端的要求较高：桥接模式要求客户端能理解抽象和实现的区别，可能需要更高的抽象层次。

实际开发中的使用：
桥接模式在实际开发中常用于以下场景：

多维度变化：当一个类有多个维度的变化，且这些变化需要独立扩展时，桥接模式是一个很好的选择。

抽象和实现不应固定在一起：当抽象和实现的关系不应该固定在一起时，桥接模式能够很好地将它们分离。
"""


# 实现部分的接口
class Device:
    def power_on(self):
        pass

    def power_off(self):
        pass

    def set_channel(self, channel):
        pass


# 具体实现A
class TV(Device):
    def power_on(self):
        print("打开电视机")

    def power_off(self):
        print("关闭电视机")

    def set_channel(self, channel):
        print(f"选择电视机频道 {channel}")


# 具体实现B
class Radio(Device):
    def power_on(self):
        print("打开收音机")

    def power_off(self):
        print("关闭收音机")

    def set_channel(self, channel):
        print(f"选择收音机频道 {channel}")


# 抽象部分的接口
class RemoteControl:
    def __init__(self, device):
        self._device = device

    def turn_on(self):
        self._device.power_on()

    def turn_off(self):
        self._device.power_off()

    def set_channel(self, channel):
        self._device.set_channel(channel)


# 客户端代码
if __name__ == "__main__":
    # 创建具体实现A和B
    tv = TV()
    radio = Radio()

    # 创建抽象部分，连接到具体实现A和B
    remote_tv = RemoteControl(tv)
    remote_radio = RemoteControl(radio)

    # 使用遥控器操作电视和收音机
    remote_tv.turn_on()
    remote_tv.set_channel(5)
    remote_tv.turn_off()

    remote_radio.turn_on()
    remote_radio.set_channel(102.5)
    remote_radio.turn_off()
