import ctypes
from pybase import PyObject, PyVarObject


# It's recommended to go to see [python 3.10 unicodeobject.h](https://github.com/python/cpython/blob/3.10/Include/cpython/unicodeobject.h#L85-L244)
class PyASCIIObject(PyObject):
    # internal fields of the string object
    _fields_ = [
        # ("ob_refcnt", ctypes.c_long),
        # ("ob_type", ctypes.c_void_p),
        ("length", ctypes.c_ssize_t),
        ("hash", ctypes.c_ssize_t),
        ("interned", ctypes.c_uint, 2),
        ("kind", ctypes.c_uint, 3),
        ("compact", ctypes.c_uint, 1),
        ("ascii", ctypes.c_uint, 1),
        ("ready", ctypes.c_uint, 1),
        ("_padding", ctypes.c_uint, 24),
        ("wstr", ctypes.POINTER(ctypes.c_wchar))
    ]


class PyCompactUnicodeObject(PyASCIIObject):
    # internal fields of the string object
    _fields_ = [
        ("utf8_length", ctypes.c_ssize_t),
        ("utf8", ctypes.POINTER(ctypes.c_char)),
        ("wstr_length", ctypes.c_ssize_t),
    ]


class PyUnicodeObject(PyCompactUnicodeObject):
    class _Data(ctypes.Union):
        _fields_ = [
            ("any", ctypes.c_void_p),
            ("latin1", ctypes.POINTER(ctypes.c_uint8)),
            ("ucs2", ctypes.POINTER(ctypes.c_uint16)),
            ("ucs4", ctypes.POINTER(ctypes.c_uint32)),
        ]

    _fields_ = [
        ("data", _Data),
    ]


class string:
    def get_ascii(self, source):
        addr = id(source)
        ascii_obj = PyASCIIObject.from_address(addr)
        # print(ascii_obj)

        data_addr = addr + ctypes.sizeof(PyASCIIObject)
        data = ctypes.cast(data_addr, ctypes.c_char_p)
        print(f"ascii data: {data.value}")

    def get_latin1(self, source):
        addr = id(source)
        compact_obj = PyCompactUnicodeObject.from_address(addr)

        data_addr = addr + ctypes.sizeof(PyCompactUnicodeObject)
        data = ctypes.cast(data_addr, ctypes.POINTER(ctypes.c_uint8))

        for i in range(len(source) + 1):
            print(f"latin1 data: {data[i]}, {data[i]:#06x}, {chr(data[i])}")

    def get_compactunicode(self, source):
        addr = id(source)
        compact_obj = PyCompactUnicodeObject.from_address(addr)
        # print(compact_obj)

        data_addr = addr + ctypes.sizeof(PyCompactUnicodeObject)
        data = ctypes.cast(data_addr, ctypes.POINTER(ctypes.c_uint16))

        for i in range(len(source) + 1):
            print(f"UCS2 data: {data[i]}, {data[i]:#06x}, {chr(data[i])}")

    def get_unicode(self, source):
        addr = id(source)
        compact_obj = PyCompactUnicodeObject.from_address(addr)
        # print(compact_obj)

        data_addr = addr + ctypes.sizeof(PyCompactUnicodeObject)
        data = ctypes.cast(data_addr, ctypes.POINTER(ctypes.c_uint32))
        for i in range(len(source) + 1):
            print(f"UCS4 data: {data[i]}, {data[i]:#010x}, {chr(data[i])}")


if __name__ == '__main__':
    string_object = string()
    s = 'abc'
    string_object.get_ascii(s)
    s += 'çais'
    string_object.get_latin1(s)
    s += '你好'
    string_object.get_compactunicode(s)
    s += '😎'
    string_object.get_unicode(s)
