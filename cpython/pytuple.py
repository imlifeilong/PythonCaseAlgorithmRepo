import ctypes
from pybase import PyObject, PyVarObject


class PyTupleObject(PyVarObject):
    _fields_ = [
        ("ob_item", ctypes.POINTER(ctypes.py_object))
    ]


def pytyple():
    data = ('a', 1, 1.2, b'123')
    addr = id(data)
    pytuple_obj = PyTupleObject.from_address(addr)
    print("ob_refcnt:", pytuple_obj.ob_refcnt)
    print("ob_type:", pytuple_obj.ob_type)
    print("ob_size:", pytuple_obj.ob_size)
    _type = ctypes.py_object
    _size = pytuple_obj.ob_size
    #  创建长度为 _size 类型为 _type的数组
    ob_items = (_type * _size).from_address(
        # 计算pytuple_obj对象中ob_item的地址
        addr + ctypes.sizeof(PyTupleObject) - ctypes.sizeof(ctypes.POINTER(ctypes.py_object))
    )
    for i in range(len(data)):
        print(f"ob_item[{i}]:", ob_items[i])


if __name__ == '__main__':
    pytyple()
