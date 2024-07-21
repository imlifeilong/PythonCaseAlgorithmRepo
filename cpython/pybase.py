import ctypes


class PyObject(ctypes.Structure):
    _fields_ = [
        ("ob_refcnt", ctypes.c_long),
        ("ob_type", ctypes.c_void_p),
    ]


class PyVarObject(PyObject):
    _fields_ = [
        ("ob_size", ctypes.c_ssize_t),
    ]
