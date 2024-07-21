import ctypes

class PyUnicodeObject(ctypes.Structure):
    # internal fields of the string object
    _fields_ = [("ob_refcnt", ctypes.c_long),
                ("ob_type", ctypes.c_void_p),
                ("length", ctypes.c_ssize_t),
                ("hash", ctypes.c_ssize_t),
                ("interned", ctypes.c_uint, 2),
                ("kind", ctypes.c_uint, 3),
                ("compact", ctypes.c_uint, 1),
                ("ascii", ctypes.c_uint, 1),
                ("ready", ctypes.c_uint, 1),
                # ...
                # ...
                ]


def get_string_kind(string):
    return PyUnicodeObject.from_address(id(string))

# 定义 PyObject 结构体
class PyObject(ctypes.Structure):
    _fields_ = [
        ('ob_refcnt', ctypes.c_ssize_t),  # 引用计数
        ('ob_type', ctypes.POINTER(ctypes.c_void_p))  # 类型指针
    ]


class PyVarObject(ctypes.Structure):
    _fields_ = [
        ('ob_base', PyObject),  # 基本对象头部
        ('ob_size', ctypes.c_ssize_t)  # 可变对象长度
    ]


# 定义 PyFloatObject 结构体，继承自 PyObject
# class PyFloatObject(ctypes.Structure):
#     _fields_ = [
#         ('ob_refcnt', ctypes.c_ssize_t),  # 引用计数
#         ('ob_type', ctypes.POINTER(ctypes.c_void_p))  # 类型指针
#         ('ob_fval', ctypes.c_double)  # 浮点数值
#     ]


# class PyLongObject(ctypes.Structure):
#     # c_ssize_t 是一个表示 C 语言中 ssize_t 类型的外包装类。ssize_t 是一个有符号整数类型，即 Py_ssize_t
#     # c_void_p 是一个表示通用指针类型的外包装类，它对应于 C 语言中的 void* 类型。void* 是一个泛型指针
#     # c_uint32 是一个外包装类，用于表示无符号的 32 位整数，对应于 C 语言中的 uint32_t 类型
#
#     SHIFT = 30
#     MASK = (2 ** SHIFT)
#     _fields_ = [
#         ('ob_refcnt', ctypes.c_ssize_t),  # 引用计数
#         ('ob_type', ctypes.POINTER(ctypes.c_void_p))  # 类型指针
#         ('ob_size', ctypes.c_ssize_t)  # 可变对象长度
#         ("ob_digit", ctypes.c_uint32 * _ob_size)
#     ]
#
#     def parse_ob_size(self, longint):
#         """
#         解析数组长度
#         :param longint:
#         :return:
#         """
#         self._ob_size = int(math.log(10) / math.log(self.MASK) * len(str(longint)) + 1)
#         print(self._ob_size)
#         return _ob_size

# def main():
#     a = 1234567890987654321
#     long_object = PyLongObject.from_address(id(a))
#     ob_size = abs(long_object.ob_base.ob_size)
#     ob_digit = long_object.ob_digit[:ob_size]
#     print(ob_digit, ob_size)  # [829168817, 76039122, 1], 3


if __name__ == '__main__':
    # main()
    string = 'Hello'
    string = '你好'
    string = '🐍'
    obj = get_string_kind(string)
    print(obj)
