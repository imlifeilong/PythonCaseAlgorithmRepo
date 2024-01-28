"""
外观模式是一种结构型设计模式，提供了一个简化的接口，用于访问系统中的一组接口。它定义了一个高层接口，使得系统更易于使用。

外观模式的核心思想是通过引入一个外观类（Facade），将系统中的一系列复杂的操作封装起来，为客户端提供一个简单的接口。外观模式有助于降低系统的复杂性，使得客户端与系统的交互更加简单。

优点：
简化接口：外观模式提供了一个简单的接口，隐藏了系统中复杂子系统的实现细节，使得客户端更易于使用。

降低耦合：外观模式将客户端与子系统之间的依赖关系降低到最小，减少了子系统的变化对客户端的影响。

更好的划分访问层次：外观模式可以帮助我们更好地划分系统的访问层次，使得客户端不直接与底层模块交互，而是通过外观类来进行访问。

缺点：
不符合开闭原则：当系统中的子系统发生变化时，可能需要修改外观类，不符合开闭原则。

可能引入不必要的依赖：某些情况下，客户端可能会直接访问子系统，导致不必要的依赖关系。

实际开发中的使用：
在实际开发中，外观模式常常用于以下场景：

简化复杂系统：当系统中包含多个子系统，而客户端只需要使用其中的一部分时，可以使用外观模式来简化客户端的操作。

统一接口：当系统中的接口较为复杂，不同的客户端需要访问不同的接口时，可以引入外观模式，提供一个统一的接口给客户端使用。

减少依赖：外观模式可以帮助客户端减少与子系统的直接依赖关系，降低耦合度。
"""


# 子系统类
class CDPlayer:
    def on(self):
        return "打开CD"

    def off(self):
        return "关闭CD"


class Amplifier:
    def on(self):
        return "打开扩音器"

    def off(self):
        return "关闭扩音器"


class Speakers:
    def on(self):
        return "打开扬声器"

    def off(self):
        return "关闭扬声器"


# 外观类
class HomeTheaterFacade:
    def __init__(self, cd_player, amplifier, speakers):
        self.cd_player = cd_player
        self.amplifier = amplifier
        self.speakers = speakers

    def watch_movie(self):
        result = []
        result.append(self.cd_player.on())
        result.append(self.amplifier.on())
        result.append(self.speakers.on())
        return result

    def end_movie(self):
        result = []
        result.append(self.cd_player.off())
        result.append(self.amplifier.off())
        result.append(self.speakers.off())
        return result


# 客户端代码
if __name__ == "__main__":
    # 创建子系统对象
    cd_player = CDPlayer()
    amplifier = Amplifier()
    speakers = Speakers()

    # 创建外观对象
    home_theater = HomeTheaterFacade(cd_player, amplifier, speakers)

    # 使用外观对象进行操作
    print("开始看电影:")
    print(home_theater.watch_movie())

    print("\n电影看完了:")
    print(home_theater.end_movie())
