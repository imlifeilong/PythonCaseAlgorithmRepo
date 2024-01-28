"""
解释器模式是一种行为型设计模式，它定义了一套语言文法，并提供了一个解释器来解释该语言中的句子。解释器模式主要包含以下几个角色：

抽象表达式（Abstract Expression）：声明一个抽象的解释操作，它是所有具体表达式的公共父类。

终结符表达式（Terminal Expression）：实现了抽象表达式中的解释操作，是语言中的基本元素。

非终结符表达式（Non-terminal Expression）：实现了抽象表达式中的解释操作，它是语言中的复杂元素，可以由终结符表达式和其他非终结符表达式组成。

上下文（Context）：包含解释器之外的一些全局信息，通常用于传递解释器所需要的信息。

客户端（Client）：构建表示语言文法的抽象语法树，并通过解释器来解释语法树。

优点：
易于扩展语法：通过增加新的终结符表达式和非终结符表达式，可以轻松扩展语言的语法。

易于实现解释：解释器模式提供了一种简洁的方式来实现语言的解释，每个表达式都有相应的解释操作。

缺点：
复杂度高：当语言的语法规则较为复杂时，可能需要大量的类来表示和解释语法规则，导致系统复杂度增加。

性能问题：解释器模式通常比较耗费性能，特别是对于复杂的语法规则。

实际开发中的使用：
解释器模式在实际开发中不常用，主要应用在对特定语言的解释和编译器设计中。在实际开发中，更常用的是其他设计模式，如策略模式、状态模式等。
"""


# 抽象表达式
class Expression:
    def interpret(self, context):
        pass


# 终结符表达式
class Number(Expression):
    def __init__(self, value):
        self._value = value

    def interpret(self, context):
        return self._value


# 非终结符表达式
class Add(Expression):
    def __init__(self, left, right):
        self._left = left
        self._right = right

    def interpret(self, context):
        return self._left.interpret(context) + self._right.interpret(context)


# 上下文
class Context:
    pass


# 客户端
if __name__ == "__main__":
    # 构建语法树
    context = Context()
    expression = Add(Number(10), Number(5))

    # 解释语法树
    result = expression.interpret(context)
    print(f"Result: {result}")  # 输出 "Result: 15"
