# class Animal(object):
#     _eat = None
#
#     # 只有@property时属性不能赋值操作
#     @property
#     def eat(self):
#         return self._eat
#
#     @eat.setter
#     def eat(self, value):
#         # 设置属性值，同时可以做校验、计算等
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self._eat = value
#
#     @eat.deleter
#     def eat(self):
#         del self._eat
#     # 另一种写法
#
#
# class Animals(object):
#     _eat = 'mi'
#
#     def get_eat(self):
#         return self._eat
#
#     def set_eat(self, value):
#         # 设置属性值，同时可以做校验、计算等
#         self._eat = value
#
#     def del_eat(self):
#         del self._eat
#
#     eat = property(get_eat, set_eat, del_eat)


# class Animal(object):
#     def __init__(self):
#         self.__age = 3
#
#     def age(self):
#         return self.__age
#
#
# a = Animal()
# # a.__age
# print(a._Animal__age)
# print(a.age())
# print(a.__dict__)

# class Animal(object):
#     def __init__(self):
#         self._name = 'Dog'
#
#
# a = Animal()
# class Animal(object):
#     def __init__(self, eat):
#         self.__eat = eat
#
#     # 只有@property时属性不能赋值操作
#     @property
#     def eat(self):
#         return self.__eat
#
#     @eat.setter
#     def eat(self, value):
#         # 设置属性值，同时可以做校验、计算等
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self.__eat = value
#
#     @eat.deleter
#     def eat(self):
#         del self.__eat

# # 另一种写法
# class Animal(object):
#     def __init__(self, eat):
#         self.__eat = eat
#
#     def get_eat(self):
#         return self.__eat
#
#     def set_eat(self, value):
#         # 设置属性值，同时可以做校验、计算等
#
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#         self.__eat = value
#
#     def del_eat(self):
#         del self.__eat
#
#     eat = property(get_eat, set_eat, del_eat)
#
#
# a = Animal('rot')
# print(a.eat)
# a.eat = 'cao'
# print(a.eat)


class ParseFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        """
        :param exc_type: 异常类型
        :param exc_value: 异常值
        :param traceback: 异常相关的堆栈跟踪信息，堆栈跟踪包括了引发异常的代码路径以及函数调用链
        :return:
        """
        self.file.close()


#
# # 使用上下文管理器打开文件
# with ParseFile('data.txt', 'r') as f:
#     print(f.read())
#     # file.re('Hello, World!')

#
# try:
#     # 尝试执行可能引发异常的代码
#     result = 10 / 0
# except ZeroDivisionError as e:
#     # 异常类型存储在 exc_type，异常值存储在 exc_value
#     exc_type = type(e)
#     exc_value = e
#     print(f"Exception Type: {exc_type}")
#     print(f"Exception Value: {exc_value}")
#     print("An error occurred.")
#     # traceback 可以用于获取堆栈跟踪信息
#     import traceback
#     traceback.print_exc()  # 打印堆栈跟踪

# from contextlib import contextmanager
# import time
#
#
# def adds():
#     for i in range(3):
#         print(i)
#         time.sleep(1)
#
#
# @contextmanager
# def timing_context(func):
#     start_time = time.time()
#
#     try:
#         func()
#         yield 'runtime'  # 进入上下文
#     finally:
#         end_time = time.time()
#         elapsed_time = end_time - start_time
#         print(f"Elapsed time: {elapsed_time} seconds")
#
#
# # 使用上下文管理器来测量代码块的执行时间
# with timing_context(adds) as msg:
#     # 模拟耗时操作
#     # time.sleep(1)
#     print(msg)
#
# # 上下文管理器会自动计算和打印执行时间

# def main(name, age=18):
#     print(name, age)
#
#
# main('alice')
# main('bob', 10)
# def add(num, *args):
#     print(args)
#     return num + sum(args)
#
#
# print(add(1))
# print(add(1, 2, 3, 4))


def add_x_to_list(x, xlist=None):
    if xlist is None:
        xlist = []
    for i in range(x):
        xlist.append(i ** 2)
    return xlist


# print(add_x_to_list(2,))
# print(add_x_to_list(3,))


# def add_item(item, my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append(item)
#     return my_list
#
#
# print(add_item(1))
# print(add_item(2))


# def avgs():
#     dataset = []
#
# #     def _avg(newdata):
# #         dataset.append(newdata)
# #         return sum(dataset) / len(dataset)
# #
# #     return _avg
# #
# # avg = avgs()
# # print(avg(1))
# # print(avg(2))
# # print(avg(3))
# #
# #
# # class avgs:
# #     dataset = []
# #     def _avg(self, newdata):
# #         self.dataset.append(newdata)
# #         return sum(self.dataset) / len(self.dataset)
# #
# # avg = avgs()
# # avg()
#
# # main = lambda :"hello world"
# # res =main()
# # print(res)
#
# # main = lambda x: print(x)
# #
# # main(123)
# #
# # main = lambda x, y, z: x + y + z
# # res = main(1, 2, 3)
# # print(res)
# #
# # names = 'The shear plate is a simple device used to observe interference and test the collimation of light beams'.split()
# # print(names)
# # names = ['The', 'plate', 'is', 'a', 'simple', 'interference', 'light']
# # names.sort(key=lambda name: len(name))
# # print(names)  # 输出 ['a', 'is', 'The', 'plate', 'light', 'simple', 'interference']
# # student = [('li', 12, 3), ('long', 33, 4), ('fei', 20, 1), ('zhang', 20, 3), ('mengd', 20, 0)]
# # res = sorted(student, key=lambda x: (x[1], -x[2]))
# # print(res)
#
#
# class A:
#     def show(self):
#         print("A")
#
#     def test(self):
#         print('A test')
#
#
# class B(A):
#     def show(self):
#         print("B")
#
#
# class C(A):
#     def show(self):
#         print("C")
#
#     def test(self):
#         print('C test')
#
#
# class D(B, C):
#     pass
#
#
# # d = D()
# # d.test()  # 输出 "B"
# # print(D.__mro__)
#
#
# class Animal:
#     def method(self):
#         print("Animal's method")
#
#
# class Dog(Animal):
#     def method(self):
#         super().method()  # 调用父类的方法
#         print("Dog's method")
#
#
# class Parent:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#
# class Child(Parent):
#     def __init__(self, name, age, score):
#         super().__init__(name, score)  # 调用父类的构造函数
#         self.age = age
#
#
# # child = Child("Alice", 30, 100)
# # print(child.name)  # 获取父类的属性
# # print(child.score)  # 获取父类的属性
# # print(child.age)  # 子类的属性
#
#
# class Base:
#     def __init__(self):
#         print('Base.__init__')
#
#
# class A(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('A.__init__')
#
#
# class B(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('B.__init__')
#
#
# class C(A, B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         print('C.__init__')
#
#
# # c = C()
#
# class Base:
#     def __init__(self):
#         print('Base.__init__')
#
#
# class A(Base):
#     def __init__(self):
#         super().__init__()
#         print('A.__init__')
#
#
# class B(Base):
#     def __init__(self):
#         super().__init__()
#         print('B.__init__')
#
#
# class C(A, B):
#     def __init__(self):
#         super().__init__()  # Only one call to super() here
#         print('C.__init__')
# c = C()

#
# class Animal:
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls)
#         return instance
#
#
# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls, *args, **kwargs)
#         return cls._instance
#
#     def __init__(self, x=0):
#         self.x = x


# a = Singleton()
# b = Singleton()
# print(id(a), id(b))
# class absint(int):
#     # 取整数绝对值
#     def __new__(cls, value):
#         return super().__new__(cls, abs(value))
#
#
# a = absint(-1)
# print(a)
from abc import ABC, ABCMeta, abstractmethod


class Animal(ABC):

    @abstractmethod
    def walk(self):
        pass


class Dog(Animal):
    def walk(self):
        print('wang wang walk!')


# a = Dog()
# a.walk()

# list()

from collections.abc import Iterable, Iterator


class myiterator:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __iter__(self):
        return self

    def __next__(self):
        return 0


mi = myiterator()
print(isinstance(mi, Iterator))
print(isinstance(mi, Iterable))
print(next(mi))
print(next(mi))
