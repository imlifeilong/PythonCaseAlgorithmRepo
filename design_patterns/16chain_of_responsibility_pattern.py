"""
责任链模式是一种行为型设计模式，它通过将请求的发送者和接收者解耦，使得多个对象都有机会处理这个请求。每个处理者都包含对下一个处理者的引用，形成一条责任链。当请求发出时，责任链上的每个处理者都有机会处理请求，直到其中一个处理者处理完成为止，或者请求达到链的末端仍未被处理。

责任链模式的关键点在于每个处理者对请求的处理方式以及是否继续传递请求的判断。

优点：
降低耦合度：责任链模式使得发送者和接收者都不需要知道对方的具体信息，降低了它们之间的耦合度。

灵活性：可以灵活地增加、删除或修改处理者，改变处理者的顺序，以满足不同的需求。

单一职责原则：每个处理者都只关心自己能够处理的请求，符合单一职责原则。

缺点：
性能问题：在责任链较长的情况下，可能会导致请求遍历整条链，性能上的开销较大。

可能造成循环引用：在设计责任链时，需要注意避免循环引用的问题。

实际开发中的使用：
责任链模式在实际开发中常用于以下场景：

请求的处理需要动态确定：当请求的处理方式需要在运行时动态确定时，可以使用责任链模式。

多个对象可以处理同一请求：当多个对象都有机会处理同一请求，但客户端不知道哪个对象最终会处理请求时，可以使用责任链模式。

避免请求的发送者和接收者之间的耦合关系：当需要避免请求的发送者和接收者之间存在直接的依赖关系时，可以使用责任链模式
"""


# 处理者抽象类
class Approver:
    def __init__(self, name):
        self.name = name
        self.next_approver = None

    def set_next_approver(self, next_approver):
        self.next_approver = next_approver

    def process_request(self, amount):
        pass


# 具体处理者A
class ConcreteApproverA(Approver):
    def process_request(self, amount):
        if amount <= 1000:
            return f"{self.name} 审批通过"
        elif self.next_approver:
            return self.next_approver.process_request(amount)
        else:
            return "不能审批"


# 具体处理者B
class ConcreteApproverB(Approver):
    def process_request(self, amount):
        if amount <= 5000:
            return f"{self.name} 审批通过"
        elif self.next_approver:
            return self.next_approver.process_request(amount)
        else:
            return "不能审批"


# 具体处理者C
class ConcreteApproverC(Approver):
    def process_request(self, amount):
        if amount <= 10000:
            return f"{self.name} 审批通过"
        elif self.next_approver:
            return self.next_approver.process_request(amount)
        else:
            return "不能审批"


# 客户端代码
if __name__ == "__main__":
    # 创建具体处理者对象
    approver_a = ConcreteApproverA("部门领导")
    approver_b = ConcreteApproverB("总监")
    approver_c = ConcreteApproverC("总经理")

    # 构建责任链
    approver_a.set_next_approver(approver_b)
    approver_b.set_next_approver(approver_c)

    # 发起采购请求
    print(approver_a.process_request(800))  # 输出 "Approver A approved the purchase request"
    print(approver_a.process_request(4500))  # 输出 "Approver B approved the purchase request"
    print(approver_a.process_request(12000))  # 输出 "Approver C approved the purchase request"
