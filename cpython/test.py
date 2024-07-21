import ctypes


class UnicodeDataUnion(ctypes.Union):
    _fields_ = [
        ("any", ctypes.c_void_p),
        ("latin1", ctypes.POINTER(ctypes.c_uint8)),
        ("ucs2", ctypes.POINTER(ctypes.c_uint16)),
        ("ucs4", ctypes.POINTER(ctypes.c_uint32))
    ]
class PyUnicodeObject(ctypes.Structure):
    _fields_ = [
        ("ob_refcnt", ctypes.c_long),
        ("ob_type", ctypes.c_void_p),
        ("length", ctypes.c_ssize_t),
        ("hash", ctypes.c_ssize_t),
        ("interned", ctypes.c_uint, 2),
        ("kind", ctypes.c_uint, 3),
        ("compact", ctypes.c_uint, 1),
        ("ascii", ctypes.c_uint, 1),
        ("ready", ctypes.c_uint, 1),
        ("reserved", ctypes.c_uint, 24),
        ("wstr", ctypes.c_wchar_p),  # wchar_t representation (null-terminated)
        ("utf8_length", ctypes.c_ssize_t),
        ("utf8", ctypes.c_char_p),
        ("wstr_length", ctypes.c_ssize_t),
        ("data", UnicodeDataUnion)
    ]


class PyCompactUnicodeObject(ctypes.Structure):
    _fields_ = [
        ("ob_refcnt", ctypes.c_long),
        ("ob_type", ctypes.c_void_p),
        ("length", ctypes.c_ssize_t),
        ("hash", ctypes.c_ssize_t),
        ("interned", ctypes.c_uint, 2),
        ("kind", ctypes.c_uint, 3),
        ("compact", ctypes.c_uint, 1),
        ("ascii", ctypes.c_uint, 1),
        ("ready", ctypes.c_uint, 1),
        ("reserved", ctypes.c_uint, 24),
        ("wstr", ctypes.c_wchar_p),  # wchar_t representation (null-terminated)
        ("utf8_length", ctypes.c_ssize_t),
        ("utf8", ctypes.c_char_p),
        ("wstr_length", ctypes.c_ssize_t),
    ]


class PyASCIIObject(ctypes.Structure):
    _fields_ = [
        ("ob_refcnt", ctypes.c_long),
        ("ob_type", ctypes.c_void_p),
        ("length", ctypes.c_ssize_t),
        ("hash", ctypes.c_ssize_t),
        ("interned", ctypes.c_uint, 2),
        ("kind", ctypes.c_uint, 3),
        ("compact", ctypes.c_uint, 1),
        ("ascii", ctypes.c_uint, 1),
        ("ready", ctypes.c_uint, 1),
        ("reserved", ctypes.c_uint, 24),
        ("wstr", ctypes.c_wchar_p),  # wchar_t representation (null-terminated)
        ("string", ctypes.c_char_p),
    ]


# 创建一个 Python 字符串对象
string = "aaa"

# 获取字符串对象的地址
string_address = id(string)

# 从地址创建 PyASCIIObject 实例
py_ascii_obj = PyASCIIObject.from_address(string_address)

# 打印 PyASCIIObject 的字段值
print("Length:", py_ascii_obj.length)
print("Hash:", py_ascii_obj.hash)
print("reserved:", py_ascii_obj.reserved)
print("compact:", py_ascii_obj.compact)
print("Wstr:", py_ascii_obj.wstr)
# print("string:", py_ascii_obj.string)

py_compactunicode_obj = PyCompactUnicodeObject.from_address(string_address)

print("Length:", py_compactunicode_obj.length)
print("Hash:", py_compactunicode_obj.hash)
print("Wstr:", py_compactunicode_obj.wstr)


# 创建一个 Python 字符串对象
string = "aaa"

# 获取字符串对象的地址
string_address = id(string)

py_unicode_obj = PyUnicodeObject.from_address(string_address)
print("Length:", py_unicode_obj.length)
print("Hash:", py_unicode_obj.hash)
print("wstr:", py_unicode_obj.wstr)
print("data:", ctypes.string_at(py_unicode_obj.data.any, py_unicode_obj.length))
