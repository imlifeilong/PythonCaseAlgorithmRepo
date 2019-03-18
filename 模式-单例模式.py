'''
注意
    1、单例只能有一个实例；
    2、单例必须自己创建自己的唯一实例；
    3、必须向整个系统提供这个实例。
意图
    保证以恶搞类仅有一个实例，并提供一个访问它的全局访问点

主要解决
    一个全局使用的类频繁的创建与销毁

何时使用
    控制实例数目，节省系统资源
实现
    判断系统时由已经有这个实例，如果有则返回，没有则创建
'''

'''
方法1: 实现__new__方法,然后将类的一个实例绑定到类变量_instance上
如果cls._instance为None, 说明该类没有被实例化过, new一个该类的实例,并返回
如果cls._instance不是None, 直接返回_instance
'''

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            obj = super(Singleton, cls)
            cls._instance = obj.__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self, x=0):
        self.x = x

###############################################################
class SingletonT(type):
    def __init__(cls, name, bases, _dict):
        super(SingletonT, cls).__init__(name, bases, _dict)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(SingletonT, cls).__call__(*args, **kwargs)
        return cls.instance

class TestUnit(metaclass=SingletonT):
    mytest = 'test'

    def __init__(self, xx=11):
        self.xx = xx

################################################################
def singleton_dec(cls, *args, **kwargs):
    instances = {}
    def get_instances():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instances

@singleton_dec
class OBS(object):
    a = 1
    def __init__(self, x=0):
        self.x = x

if __name__ == '__main__':
    # a = Singleton()
    # b = Singleton()
    # a.x = 90
    # print(a.x, b.x)
    ###########################
    # a = OBS()
    # b = OBS()
    # b.a = 4
    # print(a.a, a, b)
    ###########################
    t1 = TestUnit()
    t2 = TestUnit()
    t2.myname = 'lion'
    print(t1.myname)