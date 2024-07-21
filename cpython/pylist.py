import ctypes
from pybase import PyObject, PyVarObject


class PyListObject(PyVarObject):
    _fields_ = [
        ("ob_item", ctypes.POINTER(ctypes.POINTER(ctypes.py_object))),
        ("allocated", ctypes.c_ssize_t)
    ]


def test_pylist_allocated():
    allocated_set = []
    data = []
    addr = id(data)
    pylist_obj = PyListObject.from_address(addr)
    for i in range(100):
        allocated = pylist_obj.allocated
        if allocated not in allocated_set:
            allocated_set.append(allocated)
            print("allocated:", pylist_obj.allocated)
        data.append(i)
    print("扩容序列", allocated_set)


def pylist():
    data = ['a', 1, 1.2, b'123', []]
    addr = id(data)
    pylist_obj = PyListObject.from_address(addr)
    print("ob_refcnt:", pylist_obj.ob_refcnt)
    print("ob_type:", pylist_obj.ob_type)
    print("ob_size:", pylist_obj.ob_size)
    print("allocated:", pylist_obj.allocated)

    ob_items = (ctypes.py_object * pylist_obj.ob_size).from_address(
        ctypes.addressof(pylist_obj.ob_item.contents)
    )
    for i in range(len(data)):
        print(f"ob_item[{i}]:", ob_items[i])


if __name__ == '__main__':
    # pylist()
    test_pylist_allocated()
