"""
优点：
全局唯一实例：确保一个类只有一个实例，方便全局访问。

延迟实例化：在需要时才创建实例，可以节省资源。

避免重复实例化：通过全局访问点，避免了重复创建实例的可能性。

缺点：
可能引起全局状态：由于单例模式的实例是全局唯一的，可能会引起全局状态的共享，导致程序的耦合度增加。

不适用于多线程环境：在多线程环境下，如果多个线程同时判断_instance为None，可能会导致创建多个实例。可以通过加锁等方式解决这个问题。

违反了单一职责原则：因为单例类即负责自己的职责，又负责管理自己的生命周期，违反了单一职责原则。

适用场景：
资源共享：在整个系统中只需要一个实例来协调共享资源，例如数据库连接池等。

控制资源访问：例如，某个文件系统对象只能有一个对象可以控制对它的访问。

配置管理：对于全局配置信息，通过单例模式可以确保在整个系统中只有一个配置对象。
"""
class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# 使用单例模式创建对象
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # 输出 True
