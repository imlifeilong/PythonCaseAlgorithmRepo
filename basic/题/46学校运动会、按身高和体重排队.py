def main(h, w):
    result = []
    for i, x in enumerate(zip(h, w)):
        result.append((i, x[0], x[1]))
    # 先根据身高排序，再根据体重排序
    result.sort(key=lambda x: (x[2], x[1]))
    res = ' '.join([str(i[0] + 1) for i in result])
    print(res)


h = list(map(int, '100 100 120 130'.split()))
w = list(map(int, '40 30 60 50'.split()))

h = list(map(int, '90 110 90'.split()))
w = list(map(int, '45 60 45'.split()))
main(h, w)
