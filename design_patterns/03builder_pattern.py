"""
建造者模式（Builder Pattern）是一种创建型设计模式，它用于构建一个复杂对象的创建过程与表示分离，使得同样的构建过程可以创建不同的表示。建造者模式的核心思想是将一个复杂对象的构建过程抽象出来，使得具体的构建过程可以独立于其表示。

在建造者模式中，通常有一个抽象的建造者接口，定义了构建对象的各个部分的方法，然后有一个具体的建造者类，实现了这个接口，负责实际构建对象的过程。最后有一个指导者类，它通过调用建造者的方法来完成对象的构建。

优点：
分离构建过程和表示：建造者模式将一个复杂对象的构建过程与它的表示分离，使得构建过程可以独立于表示。

可控制构建过程：客户端代码可以通过指导者类来控制构建过程，按照需要选择不同的建造者。

更好的复用性：具体的建造者类可以被复用，可以用于创建不同的产品。

缺点：
增加了代码量：引入了抽象建造者接口和具体建造者类，可能增加了代码的复杂性和阅读难度。

不适用于简单对象的构建：建造者模式主要用于构建复杂对象，对于简单对象可能显得繁琐。

适用场景：
需要构建的对象具有复杂的内部结构：如果一个对象的构建过程比较复杂，涉及到多个部分的组合，可以考虑使用建造者模式。

需要构建的对象的表示需要灵活性：当需要构建的对象可以有不同的表示时，可以使用建造者模式。

需要控制构建过程：如果希望客户端代码可以控制对象的构建过程，可以使用建造者模式。

"""

from abc import ABC, abstractmethod


# 产品类 - 商品套餐
class Meal:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(f"商品: {item.name}, 包装: {item.packing.pack()}, 价格: {item.price}")


# 抽象建造者接口
class ItemBuilder(ABC):
    @abstractmethod
    def build_burger(self):
        pass

    @abstractmethod
    def build_drink(self):
        pass

    @abstractmethod
    def get_meal(self) -> Meal:
        pass


# 具体建造者A - 套餐A
class MealBuilderA(ItemBuilder):
    def __init__(self):
        self.meal = Meal()

    def build_burger(self):
        self.meal.add_item(LiangPi())

    def build_drink(self):
        self.meal.add_item(DrinkIcecrown())

    def get_meal(self) -> Meal:
        return self.meal


# 具体建造者B - 套餐B
class MealBuilderB(ItemBuilder):
    def __init__(self):
        self.meal = Meal()

    def build_burger(self):
        self.meal.add_item(MiPi())

    def build_drink(self):
        self.meal.add_item(DrinkCoke())

    def get_meal(self) -> Meal:
        return self.meal


# 产品部分 - 食品
class Food(ABC):
    def __init__(self):
        self.packing = None
        self.name = None
        self.price = None


# 具体凉皮
class LiangPi(Food):
    def __init__(self):
        super().__init__()
        self.name = "凉皮"
        self.price = 7
        self.packing = Box()


# 具体米皮
class MiPi(Food):
    def __init__(self):
        super().__init__()
        self.name = "米皮"
        self.price = 8
        self.packing = Box()


# 抽象产品饮料
class Drink(ABC):
    def __init__(self):
        self.packing = None
        self.name = None
        self.price = None


# 具体冰峰
class DrinkIcecrown(Drink):
    def __init__(self):
        super().__init__()
        self.name = "冰峰"
        self.price = 3
        self.packing = Bottle()


# 具体可乐
class DrinkCoke(Drink):
    def __init__(self):
        super().__init__()
        self.name = "可乐"
        self.price = 3.5
        self.packing = Bottle()


# 产品包装
class Packing(ABC):
    @abstractmethod
    def pack(self):
        pass


# 具体瓶装
class Bottle(Packing):
    def pack(self):
        return "瓶子"


# 具体盒子
class Box(Packing):
    def pack(self):
        return "盒子"


# 指导者类
class Director:
    def __init__(self, builder: ItemBuilder):
        self.builder = builder

    def construct(self) -> Meal:
        """
        确定建造顺序
        :return:
        """
        self.builder.build_burger()
        self.builder.build_drink()
        return self.builder.get_meal()


# 客户端代码
def main():
    meal_builder_a = MealBuilderA()
    meal_builder_b = MealBuilderB()

    director_a = Director(meal_builder_a)
    director_b = Director(meal_builder_b)

    meal_a = director_a.construct()
    meal_b = director_b.construct()

    print("套餐 A:")
    meal_a.show_items()

    print("\n套餐 B:")
    meal_b.show_items()


if __name__ == "__main__":
    main()
