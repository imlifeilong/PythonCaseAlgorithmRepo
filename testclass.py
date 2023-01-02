class Student:
    """
    This is Student class.
    """
    # __slots__ = 'name', 'age', 'score'
    __score = 0
    __birthday = "1990-12-12"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def score(self):
        """
        获取属性
        :return:
        """
        return self._core

    @score.setter
    def score(self, value):
        """
        设置属性，不能直接进行赋值，赋值前需要判断是否合理
        :param value:
        :return:
        """

        if 0 <= value <= 100:
            raise ValueError('hour must be in 0..100', value)
        self.__score = value

    @score.deleter
    def score(self):
        """
        删除属性
        :return:
        """
        del self.__score

    def get_birthday(self):
        return self.__birthday

    def set_birthday(self, value):
        import datetime
        datetime.datetime.strptime(value, '%Y-%m-%d')
        self.__birthday = value

    def delete_birthday(self):
        del self.__birthday

    birthday = property(get_birthday, set_birthday, delete_birthday)

    def __len__(self):
        print('__len__')
        return 0

    def __str__(self):
        return 'str'

    #
    def __repr__(self):
        return 'repr'

    # def __getitem__(self, item):
    #     """
    #     以 s["name"] 形式访问实例变量，没定义该方法时，这样调用会报错
    #     :param item:
    #     :return:
    #     """
    #     value = self.__dict__.get(item, None)
    #     print(f'以s["{item}"]方式调用实例变量{item} {value}')
    #     return value
    #
    # def __setitem__(self, key, value):
    #     """
    #     以 s["name"]=lisan 形式赋值
    #     :param key:
    #     :param value:
    #     :return:
    #     """
    #     print(f'以s["{key}"]="{value}"形式赋值{key} {value}')
    #     self.__dict__.update({key: value})
    #
    # def __delitem__(self, key):
    #     """
    #     del s["name"] 删除变量
    #     :param key:
    #     :return:
    #     """
    #     if key in self.__dict__:
    #         self.__dict__.pop(key)
    #
    # @property
    # def getip(self):
    #     return '127.0.0.1'


s = Student('zhangliang', 33)
# print(s['name'])
# print(s['getip'])
# s['name'] = 'lisan'
# s['score'] = 98
#
# print(s['name'], s['age'], s['score'])
# import datetime
# print(Student.__dict__)
# print(dict(s))
# s.__class__
# print(s.__module__)
#
# d = datetime.datetime.today()
# print(datetime.datetime.__module__)
# s.score = 0
# s.sex = "male"
'''
{'__module__': '__main__', '__init__': <function Student.__init__ at 0x0000025C1F4BA168>, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}
{'__module__': '__main__', '__slots__': ('name', 'age', 'score'), '__init__': <function Student.__init__ at 0x00000172344AA168>, 'age': <member 'age' of 'Student' objects>, 'name': <member 'name' of 'Student' objects>, 'score': <member 'score' of 'Student' objects>, '__doc__': None}
'''


# s.birthday = '1990-1-1'
# print(s.birthday)
# print(len(s))
# print(str(s))
# print(repr(s))
# print(str(Student))
# print(s.__doc__)
# print(__file__)
# print(s.__dir__())
# print(dir(s))

class date:
    def __new__(cls, year, month, day, *args, **kwargs):
        assert isinstance(year, int)
        assert isinstance(month, int)
        assert isinstance(day, int)
        self = object.__new__(cls)
        self._day = day
        self._month = month
        self._year = year
        return self

d = date(1992, 12, 1)
print(d._day)
