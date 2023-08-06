import struct


def int2bytes(data):
    res = 0
    for i in range(4):
        res += data >> (i * 8) & 0xff
    return res


def _int2bytes(data):
    return sum(struct.pack('I', data))


def main(data):
    c, b, *a = data

    mapping = {}
    for i in range(len(a)):
        hexsum = int2bytes(int(a[i]))
        mod = hexsum % int(b)

        if mod < int(c):
            if mod not in mapping:
                mapping[mod] = 1
            else:
                mapping[mod] += 1

    # 类型最多的个数
    print(max(mapping.values()))


# s = '3 4 256 257 258 259 260 261 262 263 264 265'
s = '1 4 256 257 258 259 260 261 262 263 264 265'
data = s.split()
main(data)
