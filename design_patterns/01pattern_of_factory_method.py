"""
工厂方法模式是一种创建型设计模式，它定义了一个创建对象的接口，但让子类决定要实例化的类。这样，工厂方法模式允许一个类延迟实例化到其子类。

在工厂方法模式中，通常有一个抽象的工厂类，它声明了一个创建对象的抽象方法，具体的工厂子类负责实现这个方法以创建具体的对象。

何时使用工厂方法模式：
需要创建一系列相关或相互依赖的对象：工厂方法模式允许一个类的实例化延迟到其子类，这样在具体的子类中可以选择创建相关的对象。

希望封装对象的创建逻辑：将对象的创建过程放在一个独立的工厂类中，使得客户端代码不需要知道具体的实现细节。

需要控制子类创建的对象类型：通过使用工厂方法，可以让子类来决定创建的对象类型，而不是在父类中硬编码具体的类。

希望遵循开闭原则：通过引入工厂方法，可以方便地添加新的产品类和对应的工厂类，而不需要修改现有的代码。

优点：
符合开闭原则：工厂方法模式允许新增产品类和对应的工厂类而无需修改现有代码，符合开闭原则。

封装性好：工厂方法将对象的创建过程封装在独立的工厂类中，使得客户端代码与具体类的实现解耦。

具体产品和具体工厂之间的关联性低：客户端代码通过工厂接口与具体工厂进行交互，而不直接与具体产品类交互，降低了关联性。

缺点：
类的数量增加：引入工厂方法模式会增加类的数量，每个具体产品都需要一个对应的具体工厂类，可能会使得代码结构变得复杂。

可能导致继承层次的增加：每个具体产品都需要有对应的具体工厂，这可能导致继承层次的

增加，使得类的数量变得庞大。在一些情况下，这可能会使得代码结构过于复杂。

可能引入不必要的接口和抽象类：为了使用工厂方法模式，通常需要引入接口和抽象类，这可能会增加代码的抽象层次，使得代码变得更加抽象和复杂。
总体来说，工厂方法模式在需要创建一系列相关对象、希望封装对象创建逻辑、需要控制子类创建的对象类型等场景下是很有用的。然而，开发人员在使用该模式时应权衡其优缺点，确保其在特定情境下是合适的设计选择。
"""

from abc import ABC, abstractmethod


# 产品接口
class VideoFixtion(ABC):
    url = ''

    @abstractmethod
    def fixation(self):
        pass


# 具体的产品类
class VideoFixtionBiliBili(VideoFixtion):
    def fixation(self):
        print(f"下载B站视频:{self.url}")
        return "bilibili"


# 具体的产品类
class VideoFixtionYouTuBe(VideoFixtion):
    def fixation(self):
        print(f"下载油管视频:{self.url}")
        return "youtube"


# 抽象工厂接口
class Factory(ABC):
    @abstractmethod
    def create_fixation(self):
        pass


# 具体工厂类，用于创建VideoFixtionBiliBili对象
class FactoryBiliBili(Factory):
    def create_fixation(self):
        return VideoFixtionBiliBili()


# 具体工厂类，用于创建VideoFixtionYouTuBe对象
class FactoryYouTuBe(Factory):
    def create_fixation(self):
        return VideoFixtionYouTuBe()


# 客户端代码
def client(factory):
    product = factory.create_fixation()
    result = product.fixation()
    print(f"Client: {result}")


# 使用具体工厂创建产品
factory_bilibili = FactoryBiliBili()
factory_bilibili.url = 'https://www.bilibili.com/video/BV1At4y1R7Jn'
client(factory_bilibili)

# 使用具体工厂创建产品
factory_youtube = FactoryYouTuBe()
factory_youtube.url = 'https://www.youtube.com/watch?v=OPziteNr9W0'
client(factory_youtube)
