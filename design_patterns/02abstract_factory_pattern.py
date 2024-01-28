"""
为什么需要抽象工厂模式：
创建一系列相关的产品：有时候，一个系统可能需要一组相关的产品，而这些产品之间存在一定的关联性。抽象工厂模式通过提供一个抽象工厂接口，让具体的工厂类负责创建相关的产品，从而实现了这种需求。

保持产品系列的一致性：抽象工厂模式可以确保一组相关的产品在一起使用时是兼容的，因为它们都是由同一个工厂创建的。

降低客户端代码与具体类的耦合度：客户端代码通过抽象工厂接口与具体工厂进行交互，而不直接与具体产品类交互，从而降低了客户端代码与具体类的耦合度。

优点：
确保产品的一致性：抽象工厂模式能够确保一组相关的产品在一起使用时是兼容的，因为它们都是由同一个工厂创建的。

易于替换产品系列：由于客户端代码依赖于抽象工厂接口而非具体类，因此可以轻松替换整个产品系列，而不需要修改客户端代码。

符合开闭原则：增加新的产品系列时，只需要添加新的工厂类和对应的产品类，而无需修改现有的代码，符合开闭原则。

缺点：
增加系统的抽象性和复杂性：引入抽象工厂模式会增加系统中抽象层次和类的数量，可能使得系统变得更加抽象和复杂。

不容易支持新种类的产品：如果需要添加新种类的产品，那么需要修改所有的工厂类，这可能会导致系统变得更加复杂。

不够灵活：抽象工厂模式中产品的种类一旦确定，就不容易变化。如果需要支持新的产品种类，可能需要修改工厂接口以及所有的工厂实现。
"""

from abc import ABC, abstractmethod


# 抽象产品角色
# 请求功能接口
class FixtionRequest(ABC):

    @abstractmethod
    def request(self):
        pass


# 下载功能接口
class FixtionDownload(ABC):

    @abstractmethod
    def download(self):
        pass


# 具体产品角色
# B站具体的功能
class FixtionRequestBiliBili(FixtionRequest):
    def request(self):
        print("请求B站链接")


class FixtionDownloadBiliBili(FixtionDownload):
    def download(self):
        print("下载B站链接")


# YouTube具体的功能
class FixtionRequestYouTube(FixtionRequest):
    def request(self):
        print("请求YouTube链接")


class FixtionDownloadYouTube(FixtionDownload):
    def download(self):
        print("下载YouTube链接")


# 抽象工厂角色
# 定义工厂有什么方法
class Factory(ABC):
    @abstractmethod
    def request(self) -> FixtionRequest:
        pass

    @abstractmethod
    def download(self) -> FixtionDownload:
        pass


# 具体工厂角色
# B站工厂
class FactoryBiliBili(Factory):
    def request(self) -> FixtionRequest:
        return FixtionRequestBiliBili()

    def download(self) -> FixtionDownload:
        return FixtionDownloadBiliBili()


# YouTube工厂
class FactoryYouTuBe(Factory):
    def request(self) -> FixtionRequest:
        return FixtionRequestYouTube()

    def download(self) -> FixtionDownload:
        return FixtionDownloadYouTube()


# 客户端代码
def client_code(factory: Factory):
    request_factory = factory.request()
    download_factory = factory.download()

    request_factory.request()
    download_factory.download()


# 使用具体工厂1创建产品A1和产品B1
bilibili = FactoryBiliBili()
client_code(bilibili)

# 使用具体工厂2创建产品A2和产品B2
youtube = FactoryYouTuBe()
client_code(youtube)
