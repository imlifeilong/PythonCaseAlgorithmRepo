import ctypes
from pybase import PyObject, PyVarObject


# 定义 PyDictKeyEntry 结构体
class PyDictKeyEntry(ctypes.Structure):
    _fields_ = [
        ('me_hash', ctypes.c_uint64),
        ('me_key', ctypes.py_object),
        ('me_value', ctypes.py_object),
    ]


# 定义 PyDictKeysObject 结构体
class PyDictKeysObject(ctypes.Structure):
    _fields_ = [
        ("dk_refcnt", ctypes.c_ssize_t),
        ("dk_size", ctypes.c_ssize_t),
        ("dk_lookup", ctypes.c_void_p),
        ("dk_usable", ctypes.c_ssize_t),
        ("dk_nentries", ctypes.c_ssize_t),
        ("dk_indices", ctypes.POINTER(ctypes.c_char)),
        ("dk_entries", ctypes.POINTER(PyDictKeyEntry)),
    ]


# 定义 PyDictObject 结构体
class PyDictObject(PyObject):
    _fields_ = [
        ('ma_used', ctypes.c_ssize_t),
        ("ma_version_tag", ctypes.c_uint64),
        ('ma_keys', ctypes.POINTER(PyDictKeysObject)),
        ('ma_values', ctypes.POINTER(ctypes.POINTER(ctypes.py_object))),
    ]


def pydict(d):
    print(len(d), d)
    pydict_obj = PyDictObject.from_address(id(d))
    print("ma_used", pydict_obj.ma_used)
    print("ma_version_tag", pydict_obj.ma_version_tag)

    # 获取 ma_keys 对象
    ma_keys = pydict_obj.ma_keys.contents
    print("dk_refcnt", ma_keys.dk_refcnt)
    print("dk_size", ma_keys.dk_size)
    print("dk_usable", ma_keys.dk_usable)
    print("dk_nentries", ma_keys.dk_nentries)

    # # 获取 dk_indices
    # dk_indices_addr = ctypes.addressof(ma_keys) + PyDictKeysObject.dk_indices.offset
    # dk_indices_ptr = ctypes.cast(dk_indices_addr, ctypes.POINTER(ctypes.c_char))

    dk_indices = (ctypes.c_char * ma_keys.dk_size).from_address(ctypes.addressof(ma_keys.dk_indices))
    dk_entries_addr = ctypes.addressof(ma_keys.dk_indices) + ma_keys.dk_size
    dk_entries = (PyDictKeyEntry * ma_keys.dk_nentries).from_address(dk_entries_addr)

    py_dk_indices = []
    for i in range(ma_keys.dk_size):
        index = dk_indices[i]
        py_dk_indices.append(ord(index))
        # print(f"Index: {ord(index)}")
    print(py_dk_indices)

    # 分割表
    if pydict_obj.ma_values:
        ma_values = (ctypes.py_object * pydict_obj.ma_used).from_address(
            ctypes.addressof(pydict_obj.ma_values.contents))
        # 组合表的键是共享的，节省内存
        print("组合表的键地址：", ctypes.addressof(ma_keys))
        print("组合表的值地址：", ctypes.addressof(ma_values))
    # 遍历 dk_entries 打印键值对
    for i in range(ma_keys.dk_nentries):
        entry = dk_entries[i]
        if pydict_obj.ma_values:
            print(f"Key: {entry.me_key}, MaValue: {ma_values[i]}, Hash: {entry.me_hash}")
        else:
            print(f"Key: {entry.me_key}, Value: {entry.me_value}, Hash: {entry.me_hash}")


class A:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


if __name__ == '__main__':
    d = {"name": "abc", "a": "a", "c": "c"}
    for i in range(10):
        d[str(i)] = str(i)

    d = {
        'name': 'abc', 'age': 1, 'c': 'c', '0': '0', '1': '1',
        '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
        "ok": "end", 1: 10, b'123': 123
    }
    d1 = A("li", 18, 88)
    d2 = A("fei", 20, 99)
    pydict(d1.__dict__)
    pydict(d2.__dict__)
