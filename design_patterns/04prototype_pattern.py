"""
原型模式是一种创建型设计模式，其主要思想是通过复制现有对象来创建新的对象，而不是通过实例化的方式。在原型模式中，一个对象充当原型，其他对象通过复制这个原型来创建，从而实现对象的创建和初始化。

在原型模式中，原型对象是被复制的对象，而新创建的对象是克隆或复制的结果。这种方式可以隐藏对象创建的细节，同时提供了一种更灵活的创建对象的方式。

优点：
减少对象的创建时间和资源消耗：通过复制现有对象，避免了对象的重新实例化，减少了对象的创建时间和资源消耗。

简化对象的创建过程：对于一些复杂对象，通过原型模式可以简化对象的创建过程，避免了繁琐的初始化操作。

支持动态配置对象：通过在运行时改变原型对象的属性，可以动态配置新对象的属性。

缺点：
可能导致循环引用问题：在克隆对象的时候，如果对象之间存在循环引用，可能会导致无限循环的复制。

需要实现克隆方法：要使用原型模式，需要在对象类中实现克隆方法，这可能会增加代码的复杂性。

适用场景：
对象的创建比较复杂，但复制比较简单：当对象的创建过程比较复杂，但新对象的初始化比较简单时，可以考虑使用原型模式。

需要避免构造函数的复杂性：如果一个对象的构造函数过于复杂，而你只需要一个相似的对象，那么使用原型模式可以避免复杂的构造函数。

动态配置对象：在运行时根据需要改变对象的属性，可以使用原型模式。

需要避免重复的初始化代码：当需要创建多个相似对象，并且它们的初始化代码重复时，原型模式可以避免这种重复。
"""

import copy


# 原型基类
class PrototypeShape:
    def clone(self):
        # 使用 copy 模块进行深拷贝
        return copy.deepcopy(self)


# 具体原型类 A
class ConcreteTriangle(PrototypeShape):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"三角形: {self.name}")


# 具体原型类 B
class ConcreteSquare(PrototypeShape):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"正方形: {self.name}")


# 客户端代码
def main():
    prototype_a = ConcreteTriangle("红色的")
    prototype_b = ConcreteSquare("白色的")

    # 克隆对象
    clone_a = prototype_a.clone()
    clone_b = prototype_b.clone()

    # 显示克隆后的对象信息
    clone_a.show()  # 输出 "ConcretePrototypeA: Prototype A"
    clone_b.show()  # 输出 "ConcretePrototypeB: 100"


if __name__ == "__main__":
    main()
