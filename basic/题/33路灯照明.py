def main(data, n):

    res = 0
    for i in range(n - 1):
        # 路灯距离100米，求两个路灯都未照到的距离
        tmp = 100 - sum(data[i:i + 2])
        if tmp > 0:
            res += tmp
    print(res)


s = '50 50'.split()
data = list(map(int, s))
n = 2

s = '30 50 20 20'.split()
data = list(map(int, s))
n = 4

main(data, n)
