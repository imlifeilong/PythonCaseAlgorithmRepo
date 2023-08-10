def main(data):
    from functools import reduce
    data.sort()
    maxval = float('-inf')

    for i in range(1, len(data) - 1):
        binsum_1 = reduce(lambda x, y: x ^ y, data[:i])
        binsum_2 = reduce(lambda x, y: x ^ y, data[i:])
        sum_1 = sum(data[:i])
        sum_2 = sum(data[i:])
        if binsum_1 == binsum_2:
            maxval = max(max(sum_1, sum_2), maxval)
    print(maxval)


def main1(data):
    # 两个相同二进制数按位异或的结果就是0，
    # 即 如果序列分割后，生成两份二进制相同的数，则所有的值异或后值为0
    data.sort()
    minval = data[0]
    binsum = minval
    decsum = minval
    for i in range(1, len(data)):
        binsum ^= data[i]  # 按A的方法 所有值进行累计异或
        decsum += data[i]  # 按B的方法 所有值进行累加
    if binsum == 0:  # 如果序列可以分为两组数 并且异或结果为0，则获取这两组数中和较大的结果
        print(f'{decsum - minval}')


s = '3 5 6'.split()
s = '7258 6579 2602 6716 3050 3564 5396 1773'.split()
data = list(map(int, s))
print(data)
main1(data)
main(data)
