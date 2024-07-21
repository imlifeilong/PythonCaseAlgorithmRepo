import ctypes
from pybase import PyObject, PyVarObject


class setentry(ctypes.Structure):
    _fields_ = [
        ('key', ctypes.py_object),
        ('hash', ctypes.c_ssize_t)
    ]


class PySetObject(PyObject):
    _fields_ = [
        ('fill', ctypes.c_ssize_t),
        ('used', ctypes.c_ssize_t),
        ('mask', ctypes.c_ssize_t),
        ('table', ctypes.POINTER(setentry)),
        ('hash', ctypes.c_ssize_t),
        ('finger', ctypes.c_ssize_t),
        ('smalltable', setentry * 8),
        ('weakreflist', ctypes.POINTER(ctypes.py_object))
    ]


# 创建一个简单的 Python 集合
s = {"abc", "def"}

# 将 Python 集合的地址映射到我们的 PySetObject 结构体
pyset_obj = PySetObject.from_address(id(s))

# 打印集合的基本信息
print(f"Fill: {pyset_obj.fill}")
print(f"Used: {pyset_obj.used}")
print(f"Mask: {pyset_obj.mask}")
print(f"Hash: {pyset_obj.hash}")
print(f"Finger: {pyset_obj.finger}")

# 如果 table 不为空，则打印 table 的内容
if pyset_obj.table:
    for i in range(pyset_obj.mask + 1):
        entry = pyset_obj.table[i]
        try:
            if entry.key is not None:
                print(f"Table[{i}]: Key: {entry.key}, Hash: {entry.hash}")
        except:
            pass

# 打印 smalltable 的内容
for i in range(8):
    entry = pyset_obj.smalltable[i]
    try:
        if entry.key is not None:
            print(f"Smalltable[{i}]: Key: {entry.key}, Hash: {entry.hash}")
    except:
        pass
