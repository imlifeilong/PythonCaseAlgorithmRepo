"""
状态模式是一种行为型设计模式，它允许对象在内部状态发生改变时改变其行为。状态模式将对象的状态封装成不同的类，并将对象在不同状态下的行为进行抽象，从而使得对象状态的改变不会影响到客户端。

在状态模式中，上下文对象持有一个当前状态对象，该状态对象定义了上下文对象在特定状态下的行为。当上下文对象的状态发生改变时，它会切换到对应的状态对象，从而改变其行为。

优点：
封装了状态：状态模式将每个状态封装成一个类，使得每个状态的实现都是独立的，易于理解和维护。

简化了上下文：状态模式使得上下文对象不再需要包含大量的条件语句来判断当前状态，减少了复杂度。

易于扩展：通过添加新的状态类，可以轻松地扩展状态模式，符合开闭原则。

缺点：
可能引起类膨胀：如果状态类的数量过多，可能会导致类的数量膨胀，增加系统的复杂性。

状态切换的逻辑分散：状态切换的逻辑可能分散在各个具体状态类中，不利于维护。

实际开发中的使用：
状态模式在实际开发中常用于以下场景：

对象的行为依赖于其状态，并且状态经常发生改变：当一个对象的行为随着其状态的改变而改变，且状态的改变频繁发生时，可以考虑使用状态模式。

消除大量的条件语句：当一个对象包含大量的条件语句来判断当前状态时，可以使用状态模式来消除这些条件语句，使代码更清晰。
"""


# 状态接口
class State:
    def handle(self):
        pass


# 具体状态A
class StateA(State):
    def handle(self):
        print("State A: Performing action for State A")


# 具体状态B
class StateB(State):
    def handle(self):
        print("State B: Performing action for State B")


# 上下文类
class Context:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def request(self):
        self._state.handle()


# 客户端代码
if __name__ == "__main__":
    # 创建具体状态A和B
    state_a = StateA()
    state_b = StateB()

    # 创建上下文对象，初始状态为A
    context = Context(state_a)

    # 发送请求，执行当前状态的操作
    context.request()

    # 切换状态为B，并再次发送请求
    context.set_state(state_b)
    context.request()
