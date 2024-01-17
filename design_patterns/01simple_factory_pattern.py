from abc import ABC, abstractmethod

"""
工厂模式是一种创建型设计模式，其目的是提供一个接口，让子类决定实例化哪个类。
它隐藏了对象的具体创建过程，使得客户端代码不需要知道实际创建的类。
工厂模式主要分为三种：简单工厂模式、工厂方法模式和抽象工厂模式。


何时使用工厂模式：
当一个类不能预先指定要创建的对象类型：工厂模式通过提供一个接口来创建对象，
使得客户端代码可以根据需要选择合适的类，而无需知道具体的实现。

当类的实例化过程比较复杂，包含了很多步骤或逻辑：工厂模式将对象的创建逻辑封装到一个单独的地方，
使得客户端代码可以更简洁，而且易于维护。

当系统中的某些类需要被重复创建：通过工厂模式，可以减少代码的重复，提高代码的可维护性。

优点：
封装对象的创建过程：客户端代码不需要了解对象的创建过程，只需关注接口即可。

降低耦合度：客户端代码与具体类的耦合度降低，因为客户端代码仅依赖于接口而不依赖于具体类。

易于扩展：可以通过添加新的工厂类来创建新的对象类型，而无需修改现有的代码。

符合开闭原则：增加新的产品类型时，不需要修改现有代码，只需添加新的工厂类。

缺点：
增加了系统的复杂度：引入了额外的类和接口，可能会增加系统的抽象层次，使得代码更加复杂。

不适合简单的场景：在某些情况下，使用工厂模式可能会显得过度设计，不适合简单的对象创建。

可能需要大量的工厂类：随着产品类型的增加，可能需要创建大量的工厂类，增加了系统的复杂性。

"""


# 简单工厂模式
# 定义一个抽象类或接口，所有具体类都实现这个接口
class VideoFixtion(ABC):
    @abstractmethod
    def fixation(self, url):
        pass


# 具体的产品类
class VideoFixtionBiliBili(VideoFixtion):
    def fixation(self, url):
        print(f"下载B站视频:{url}")


# 具体的产品类
class VideoFixtionYouTuBe(VideoFixtion):
    def fixation(self, url):
        print(f"下载油管视频:{url}")


# 定义一个工厂类，其中包含一个工厂方法，用于实例化具体对象
class Factory:
    def create_fixtion(self, domain):
        if domain == "bilibili":
            return VideoFixtionBiliBili()
        elif domain == "youtube":
            return VideoFixtionYouTuBe()
        else:
            raise ValueError("Invalid domain type.")


# 在客户端代码中，通过调用工厂类的工厂方法获取所需的对象
factory = Factory()
url = 'https://www.bilibili.com/video/BV1At4y1R7Jn'
bilibili = factory.create_fixtion("bilibili")
bilibili.fixation(url)

url = 'https://www.youtube.com/watch?v=OPziteNr9W0'
youtube = factory.create_fixtion("youtube")
youtube.fixation(url)
