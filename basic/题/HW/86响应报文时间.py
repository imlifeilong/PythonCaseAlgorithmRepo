"""
3
0 20
1 10
8 20

"""


def get_rtt(T, M):
    if M >= 128:
        mant = (M >> 3) & 0XF   # 低4位的数据
        exp = M & 0x7           # 高5~7位数据
        M = (mant | 0x10) << (exp + 3)
    return T + M


def main(data):
    C = data.pop(0)
    res = []
    for i in range(int(C)):
        T, M = map(int, data[i].split())
        res.append(get_rtt(T, M))
    res.sort()
    print(res[0])


s = """3
0 20
1 10
8 20"""
s = """2
0 255
200 60"""
data = s.split('\n')
main(data)
