"""
中介者模式是一种行为型设计模式，它通过引入一个中介者对象来集中管理多个对象之间的交互。中介者模式的目标是降低多个对象之间的直接通信，从而降低系统的耦合度，使系统更易于维护和扩展。

在中介者模式中，中介者对象负责协调和管理系统中的多个对象之间的通信。对象之间的交互不再是直接的，而是通过中介者进行的。这样，当一个对象发生变化时，不会影响到系统中的其他对象，因为它们都通过中介者进行通信。

优点：
降低耦合度：中介者模式将对象之间的直接通信替换为通过中介者进行通信，降低了系统的耦合度。

易于维护和扩展：由于对象之间的通信集中在中介者中，当系统需要增加新的对象或修改通信规则时，只需要修改中介者即可，使系统更易于维护和扩展。

复用性提高：中介者模式可以将对象之间的通信逻辑抽象到中介者中，提高了通信逻辑的复用性。

缺点：
中介者复杂度增加：随着系统中对象的增多，中介者可能会变得复杂，难以维护。

单点故障：中介者对象可能成为系统的单点故障，一旦中介者对象发生故障，整个系统的通信就会受到影响。

实际开发中的使用：
中介者模式在实际开发中常用于以下场景：

对象之间的通信复杂：当系统中对象之间的通信关系变得复杂且难以维护时，可以考虑使用中介者模式。

避免对象之间的直接耦合：当希望减少对象之间的直接耦合，通过一个中介者来进行通信时，中介者模式是一种合适的选择。
"""


# 中介者接口
class ChatMediator:
    def send_message(self, message, user):
        pass


# 具体中介者
class ConcreteChatMediator(ChatMediator):
    def __init__(self):
        self._users = []

    def add_user(self, user):
        self._users.append(user)

    def send_message(self, message, user):
        for u in self._users:
            if u != user:
                u.receive_message(message)


# 抽象同事类
class User:
    def __init__(self, name, mediator):
        self._name = name
        self._mediator = mediator

    def send_message(self, message):
        self._mediator.send_message(message, self)

    def receive_message(self, message):
        print(f"{self._name} received message: {message}")


# 客户端代码
if __name__ == "__main__":
    # 创建中介者
    mediator = ConcreteChatMediator()

    # 创建用户并加入聊天室
    user1 = User("User 1", mediator)
    user2 = User("User 2", mediator)
    user3 = User("User 3", mediator)

    mediator.add_user(user1)
    mediator.add_user(user2)
    mediator.add_user(user3)

    # 用户发送和接收消息
    user1.send_message("Hello, everyone!")  # 输出 "User 1 received message: Hello, everyone!"
    user2.send_message("Hi, User 1!")  # 输出 "User 2 received message: Hi, User 1!"
