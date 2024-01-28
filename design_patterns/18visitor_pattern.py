"""
访问者模式是一种行为型设计模式，它允许你定义一系列操作，而无需修改对象结构。通过使用访问者模式，你可以在不改变元素类的前提下定义新的操作。

在访问者模式中，有两个关键的角色：元素（Element）和访问者（Visitor）。元素是具体类的抽象，它包含接受访问者的方法。访问者是一个接口或抽象类，它定义了对不同元素的访问操作。

优点：
解耦元素和操作：访问者模式使得可以在不改变元素类的前提下定义新的操作，实现了元素和操作的解耦。

增加新操作容易：通过增加新的访问者类，可以轻松地增加新的操作，符合开闭原则。

提高可扩展性：可以通过增加新的元素类，扩展系统的功能。

缺点：
增加新元素困难：在访问者模式中，每次增加新的元素都需要修改所有的访问者类，可能会导致系统的复杂性增加。

破坏封装：访问者模式破坏了元素的封装性，因为访问者需要访问元素的内部状态。

实际开发中的使用：
访问者模式在实际开发中常用于以下场景：

操作需要在不同的元素类上执行：当需要在不同的元素类上执行一系列不同的操作时，可以使用访问者模式。

增加新操作而不改变元素类：当需要增加新的操作而不改变现有元素类的结构时，访问者模式是一种合适的选择。
"""


# 元素接口
class Shape:
    def accept(self, visitor):
        pass


# 具体元素A
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)


# 具体元素B
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def accept(self, visitor):
        visitor.visit_square(self)


# 访问者接口
class Visitor:
    def visit_circle(self, circle):
        pass

    def visit_square(self, square):
        pass


# 具体访问者A
class AreaCalculator(Visitor):
    def visit_circle(self, circle):
        print(f"Calculating area of circle with radius {circle.radius}")

    def visit_square(self, square):
        print(f"Calculating area of square with side {square.side}")


# 具体访问者B
class PerimeterCalculator(Visitor):
    def visit_circle(self, circle):
        print(f"Calculating perimeter of circle with radius {circle.radius}")

    def visit_square(self, square):
        print(f"Calculating perimeter of square with side {square.side}")


# 客户端代码
if __name__ == "__main__":
    # 创建具体元素对象
    circle = Circle(radius=5)
    square = Square(side=4)

    # 创建具体访问者对象
    area_calculator = AreaCalculator()
    perimeter_calculator = PerimeterCalculator()

    # 使用具体访问者计算面积和周长
    circle.accept(area_calculator)  # 输出 "Calculating area of circle with radius 5"
    square.accept(area_calculator)  # 输出 "Calculating area of square with side 4"

    circle.accept(perimeter_calculator)  # 输出 "Calculating perimeter of circle with radius 5"
    square.accept(perimeter_calculator)  # 输出 "Calculating perimeter of square with side 4"
