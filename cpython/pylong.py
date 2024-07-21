# cpython长整数底层存储算法
import math
import ctypes


class PyLong:
    SHIFT = 30
    MASK = (2 ** SHIFT)

    def restore_number(self, num_list):
        bignum = 0
        for i, n in enumerate(num_list):
            bignum += n * (2 ** (self.SHIFT * i))
        return bignum
    def parse_ob_size(self, longint):
        """
        解析数组长度
        :param longint:
        :return:
        """
        ob_size = int(math.log(10) / math.log(self.MASK) * len(str(longint)) + 1)
        print(ob_size)
        return ob_size

    def parse_ob_digit(self, longint):
        n = abs(longint)
        ob_digit = []
        while n != 0:
            digit = n % self.MASK
            ob_digit.append(digit)

            n //= self.MASK # or n >>= self.SHIFT

        print(ob_digit) # [829168817, 76039122, 1]

    def parse_ob_digit_by_struct(self, longint):
        """
        通过访问底层地址查看ob_digit数组
        :param longint:
        :return:
        """
        _ob_size = self.parse_ob_size(longint)

        class _PyLongObject(ctypes.Structure):
            # c_ssize_t 是一个表示 C 语言中 ssize_t 类型的外包装类。ssize_t 是一个有符号整数类型，即 Py_ssize_t
            # c_void_p 是一个表示通用指针类型的外包装类，它对应于 C 语言中的 void* 类型。void* 是一个泛型指针
            # c_uint32 是一个外包装类，用于表示无符号的 32 位整数，对应于 C 语言中的 uint32_t 类型
            _fields_ = [("ob_refcnt", ctypes.c_ssize_t),
                        ("ob_type", ctypes.c_void_p),
                        ("ob_size", ctypes.c_ssize_t),
                        ("ob_digit", ctypes.c_uint32 * _ob_size)]

        long_object = _PyLongObject.from_address(id(longint))
        ob_size = abs(long_object.ob_size)
        ob_digit = long_object.ob_digit[:ob_size]
        print(ob_digit, ob_size) # [829168817, 76039122, 1], 3


if __name__ == '__main__':
    pylong = PyLong()
    data = 1234567890987654321
    # data = 1073741824
    # data = 1234567890987654322
    pylong.parse_ob_size(data)
    pylong.parse_ob_digit(data)

    pylong.parse_ob_digit_by_struct(data)

    ob_digits = [829168818, 76039120, 1]
    res = pylong.restore_number(ob_digits)
    print(res)