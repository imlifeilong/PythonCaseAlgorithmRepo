import ctypes
from pybase import PyObject, PyVarObject


class PyBytesObject(PyVarObject):
    _fields_ = [
        ("ob_shash", ctypes.c_ssize_t),
        ("ob_sval", ctypes.POINTER(ctypes.c_char))
    ]


def pybytes():
    data = "你好".encode()
    addr = id(data)
    pybytes_obj = PyBytesObject.from_address(addr)
    print("ob_refcnt:", pybytes_obj.ob_refcnt)
    print("ob_type:", pybytes_obj.ob_type)
    print("ob_size:", pybytes_obj.ob_size)

    ob_sval = (ctypes.c_char * pybytes_obj.ob_size).from_address(
        ctypes.addressof(pybytes_obj.ob_sval)
    )
    print(b''.join(ob_sval).decode())


if __name__ == '__main__':
    pybytes()
