from ctypes import Structure, c_ulong, POINTER, cast, py_object, CFUNCTYPE, c_ssize_t, c_void_p


class PyDictKeyEntry(Structure):
    _fields_ = [
        ('me_hash', c_ulong),
        ('me_key', py_object),
        ('me_value', py_object),
    ]


class PyDictObject(Structure):
    """A dictionary object."""
    pass


LOOKUPFUNC = CFUNCTYPE(POINTER(PyDictKeyEntry), POINTER(PyDictObject), py_object, c_ulong, POINTER(POINTER(py_object)))


class PyDictKeysObject(Structure):
    _fields_ = [
        ('dk_refcnt', c_ssize_t),
        ('dk_size', c_ssize_t),
        ('dk_lookup', LOOKUPFUNC),  # a function prototype per docs
        ('dk_usable', c_ssize_t),
        ('dk_entries', PyDictKeyEntry * 1),
        # an array of size 1; size grows as keys are inserted into dictionary; this variable-sized field was the trickiest part to translate into python
    ]


PyDictObject._fields_ = [
    ('ob_refcnt', c_ssize_t),  # Py_ssize_t translates to c_ssize_t per ctypes docs
    ('ob_type', c_void_p),  # could not find this in the docs
    ('ma_used', c_ssize_t),
    ('ma_keys', POINTER(PyDictKeysObject)),
    ('ma_values', POINTER(py_object)),  # Py_Object* translates to py_object per ctypes docs
]

PyDictKeysObject._dk_entries = PyDictKeysObject.dk_entries
PyDictKeysObject.dk_entries = property(lambda s: cast(s._dk_entries, POINTER(PyDictKeyEntry * s.dk_size))[0])
d = {0: 0, 1: 1, 2: 2, 3: 3}
obj = cast(id(d), POINTER(PyDictObject)).contents
key_obj = obj.ma_keys.contents
key = key_obj.dk_entries[0].me_key
print(key)
