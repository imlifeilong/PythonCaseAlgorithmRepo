"""
模板模式是一种行为型设计模式，定义了一个算法的骨架，并将一些步骤的实现延迟到子类。模板模式使得子类可以在不改变算法结构的情况下重新定义算法中的某些步骤。

模板模式主要包含两个角色：

抽象类（Abstract Class）：定义了算法的骨架，包含了一些固定的步骤，其中的某些步骤的具体实现由子类完成。

具体子类（Concrete Class）：实现了抽象类中定义的某些步骤，完成算法中的具体细节。

优点：
提高代码复用性：模板模式将算法的结构和具体实现分离，使得子类可以重用父类中的算法结构。

提高系统扩展性：通过在抽象类中定义算法的骨架，可以在不改变算法结构的情况下增加新的具体子类，扩展系统功能。

缺点：
可能导致代码的复杂性：在一些简单的情况下，使用模板模式可能会导致代码变得复杂，因为算法的骨架可能包含了很多步骤。

不适用于所有场景：模板模式是一种固定算法结构的设计模式，不适用于所有情况。

实际开发中的使用：
模板模式在实际开发中常用于以下场景：

定义算法的骨架：当有一系列算法具有相似的结构，但其中的某些步骤的实现可能不同，可以考虑使用模板模式。

复用代码：当多个类中的一些代码重复，可以将这部分代码抽取到一个抽象类中，形成模板模式。
"""


# 抽象类
class CaffeineBeverage:
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    def brew(self):
        pass

    def add_condiments(self):
        pass


# 具体子类A
class Coffee(CaffeineBeverage):
    def brew(self):
        print("Brewing coffee grounds")

    def add_condiments(self):
        print("Adding sugar and milk")


# 具体子类B
class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")


# 客户端代码
if __name__ == "__main__":
    coffee = Coffee()
    tea = Tea()

    print("Making coffee:")
    coffee.prepare_recipe()

    print("\nMaking tea:")
    tea.prepare_recipe()
