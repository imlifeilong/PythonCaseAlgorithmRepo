"""
代理模式是一种结构型设计模式，它允许通过代理对象控制对另一个对象的访问。代理模式主要有三个角色：主题接口（Subject Interface）、真实主题（Real Subject）和代理主题（Proxy Subject）。代理主题实现了主题接口，并包含对真实主题对象的引用，客户端通过代理主题访问真实主题对象。

代理模式的主要目的是在访问对象时引入一定程度的间接性，以提供更多的控制和管理。

优点：
控制对对象的访问：代理模式允许在访问对象时添加一些控制逻辑，例如权限控制、日志记录等。

封装：代理模式可以隐藏真实主题的实现细节，使客户端无需关心具体的实现。

延迟加载：代理模式可以延迟加载真实主题，提高系统的性能。

缺点：
复杂性增加：引入代理会增加代码的复杂性，因为需要额外的类和逻辑。

性能问题：在某些情况下，代理模式可能导致性能下降，特别是在频繁访问真实主题对象时。

适用场景：
远程代理：在网络通信中，代理模式可以用于在本地代理对象上控制远程对象。

虚拟代理：当一个对象的创建和初始化很昂贵时，可以使用代理模式实现虚拟代理，延迟对象的创建。

权限控制：代理模式可以用于控制对对象的访问权限，例如在访问敏感信息时进行权限验证。

日志记录：代理模式可以用于记录对象的操作，实现日志记录功能。
"""


# 主题接口
class Subject:
    def request(self):
        pass


# 真实主题
class RealSubject(Subject):
    def request(self):
        print("RealSubject: 开始处理请求")


# 代理主题
class Proxy(Subject):
    def __init__(self, real_subject, user):
        self.real_subject = real_subject
        self.user = user

    def request(self):
        if self.check_access():
            self.real_subject.request()
        else:
            print("Proxy: Access denied")

    def check_access(self):
        # 检查用户权限
        return self.user == "admin"


# 客户端代码
def client_code(subject):
    subject.request()


if __name__ == "__main__":
    # 创建真实主题和代理主题
    real_subject = RealSubject()
    proxy = Proxy(real_subject, user="admin")

    # 客户端通过代理访问真实主题
    client_code(proxy)
