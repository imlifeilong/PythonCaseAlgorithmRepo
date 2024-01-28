"""
什么是装饰模式：
装饰模式是一种结构型设计模式，它允许动态地给一个对象添加一些额外的职责，而不需要修改其源代码。装饰模式通过创建一系列包装对象（装饰器），这些包装对象包裹原始的对象，从而在不改变原始对象结构的情况下，增加新的功能或责任。

在装饰模式中，装饰器和被装饰的对象具有相同的接口，这使得装饰器可以递归地嵌套，从而实现各种组合。装饰器模式强调的是对类的透明性，即被装饰的对象无需关心其被装饰的过程。

优点：
灵活性：装饰模式允许动态地添加或移除对象的职责，具有很高的灵活性。

遵循开闭原则：通过装饰器可以在不修改现有代码的基础上引入新功能，符合开闭原则。

透明性：被装饰的对象无需知道装饰器的存在，保持了对象接口的一致性。

缺点：
产生大量小对象：由于每个装饰器都是一个独立的对象，可能会导致系统中存在大量的小对象，影响性能。

复杂性增加：随着装饰器的增加，可能会增加系统的复杂性，难以理解和维护。

实际开发中的使用：
装饰模式在实际开发中常用于以下场景：

动态添加功能：当需要动态地添加对象的功能而不影响其接口时，装饰模式是一个好的选择。

透明地扩展类的功能：通过装饰器，可以透明地扩展类的功能，而无需修改原始类。
"""


# 组件接口
class Coffee:
    def cost(self):
        pass


# 具体组件
class SimpleCoffee(Coffee):
    def cost(self):
        return 5


# 装饰器抽象类
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()


# 加牛奶
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2


# 加糖
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1


# 客户端代码
if __name__ == "__main__":
    # 创建简单咖啡
    simple_coffee = SimpleCoffee()
    print("普通咖啡", simple_coffee.cost())

    # 添加牛奶
    coffee_with_milk = MilkDecorator(simple_coffee)
    print("添加牛奶", coffee_with_milk.cost())

    # 添加糖
    coffee_with_sugar = SugarDecorator(simple_coffee)
    print("添加糖", coffee_with_sugar.cost())

    # 同时添加牛奶和糖
    coffee_with_milk_and_sugar = MilkDecorator(SugarDecorator(simple_coffee))
    print("加糖加奶", coffee_with_milk_and_sugar.cost())
