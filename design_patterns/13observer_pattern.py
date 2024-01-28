"""
观察者模式是一种行为型设计模式，它定义了一种一对多的依赖关系，让多个观察者对象同时监听某一个主题对象。当主题对象状态发生变化时，所有依赖于它的观察者都会得到通知并更新。

在观察者模式中，主题对象维护一个观察者列表，当主题对象的状态发生改变时，它会遍历通知所有注册的观察者。观察者则根据主题的通知来更新自己的状态。

优点：
解耦：观察者模式将主题和观察者解耦，使得它们可以独立变化，互不影响。

扩展性：可以灵活地增加或删除观察者，而不影响主题对象。

通知机制：主题对象状态的改变会自动通知所有观察者，无需手动通知。

缺点：
过多的通知：如果主题对象频繁地改变状态，可能会导致观察者接收过多的通知，影响性能。

可能引起循环依赖：观察者和主题之间的依赖关系可能导致循环引用的问题。

实际开发中的使用：
观察者模式在实际开发中常用于以下场景：

事件处理系统：GUI 应用中，用户交互和界面元素状态变化通常使用观察者模式实现。

消息通知机制：系统中的消息通知机制，例如订阅-发布模型，常使用观察者模式。

分布式系统中的消息队列：观察者模式可用于实现分布式系统中的消息队列，其中生产者产生消息，而多个消费者监听并处理消息。
"""


# 主题抽象类
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


# 观察者抽象类
class Observer:
    def update(self, message):
        pass


# 具体主题类
class ConcreteSubject(Subject):
    def set_state(self, state):
        print(f"设置状态为: {state}")
        self.notify_observers(state)


# 具体观察者类
class ConcreteObserverA(Observer):
    def update(self, message):
        print(f"员工老A收到消息: {message}，开始打扫卫视")


class ConcreteObserverB(Observer):
    def update(self, message):
        print(f"员工老B收到消息: {message}，开始整理资料")


# 客户端代码
if __name__ == "__main__":
    # 创建主题对象
    subject = ConcreteSubject()

    # 创建观察者对象
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    # 注册观察者
    subject.add_observer(observer_a)
    subject.add_observer(observer_b)

    # 主题对象状态发生改变，通知所有观察者
    subject.set_state("老板视察来了")
