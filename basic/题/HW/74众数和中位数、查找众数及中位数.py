def main(data):
    mapping = {}

    for n in data:
        if n in mapping:
            mapping[n] += 1
        else:
            mapping[n] = 1
    maxval = max(mapping.values())
    tmp = []
    for k, v in mapping.items():
        if v == maxval:
            tmp.append(k)
    tmp.sort()

    mid = len(tmp) // 2
    # 偶数情况
    if len(tmp) % 2 == 0:
        # 中间两个数的 和 除2
        res = (tmp[mid] + tmp[mid - 1]) // 2
    else:
        res = tmp[mid]
    print(res)


s = '2 1 5 4 3 3 9 2 7 4 6 2 15 4 2 4'.split()
s = '10 11 21 19 21 17 21 16 21 18 16'.split()
s = '5 1 5 3 5 2 5 5 7 6 7 3 7 11 7 55 7 9 98 9 17 9 15 9 9 1 39'.split()
data = list(map(int, s))
main(data)
