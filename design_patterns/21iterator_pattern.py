"""
迭代器模式是一种行为型设计模式，它提供了一种访问一个容器对象（如列表、集合）元素的方法，而不需要暴露该对象的内部表示。迭代器模式将遍历集合的责任交给了迭代器对象，而不是集合对象本身。

迭代器模式主要包含两个关键的角色：

迭代器（Iterator）：定义访问和遍历元素的接口。

具体迭代器（ConcreteIterator）：实现迭代器接口，负责管理和追踪集合中的当前位置。

可迭代对象（Iterable）：定义创建迭代器的接口。

具体可迭代对象（ConcreteIterable）：实现可迭代对象接口，负责创建具体迭代器。

优点：
简化集合的遍历：迭代器模式提供了一种简化集合遍历的方法，不需要直接操作集合，使得代码更加清晰和易维护。

隔离集合的实现：迭代器模式将集合的实现与遍历操作分离，使得集合可以独立于其遍历算法变化。

支持多种遍历方式：通过提供不同的迭代器，可以支持多种遍历方式，例如正序、逆序、跳跃等。

缺点：
增加了类的数量：迭代器模式引入了迭代器和可迭代对象的接口和实现，可能会增加系统中类的数量。
实际开发中的使用：
迭代器模式在实际开发中常用于以下场景：

需要遍历不同类型集合的场景：当需要遍历不同类型的集合对象，但又不希望直接操作集合对象时，可以使用迭代器模式。

希望隔离集合和遍历算法的场景：当希望隔离集合的实现和遍历算法，使得它们可以独立变化时，可以考虑使用迭代器模式。
"""


# 迭代器接口
class Iterator:
    def has_next(self):
        pass

    def next(self):
        pass


# 可迭代对象接口
class Iterable:
    def create_iterator(self):
        pass


# 具体迭代器
class CartIterator(Iterator):
    def __init__(self, cart):
        self._cart = cart
        self._index = 0

    def has_next(self):
        return self._index < len(self._cart.items)

    def next(self):
        if self.has_next():
            item = self._cart.items[self._index]
            self._index += 1
            return item
        else:
            return None


# 具体可迭代对象
class ShoppingCart(Iterable):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def create_iterator(self):
        return CartIterator(self)


# 客户端代码
if __name__ == "__main__":
    # 创建购物车
    cart = ShoppingCart()

    # 添加商品到购物车
    cart.add_item("Product 1")
    cart.add_item("Product 2")
    cart.add_item("Product 3")

    # 创建迭代器
    iterator = cart.create_iterator()

    # 遍历购物车
    while iterator.has_next():
        item = iterator.next()
        print(f"Item: {item}")
