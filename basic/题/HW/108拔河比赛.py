def main(data):
    n = len(data)
    # for i in range(n):
    #     for j in range(0, n - i - 1):
    #         # # 如果第二个字段相同，则比较第一个字段
    #         if data[j][1] == data[j + 1][1]:
    #             if data[j][0] > data[j + 1][0]:
    #                 data[j], data[j + 1] = data[j + 1], data[j]
    #         # 如果第二个字段不同，则比较第二个字段
    #         elif data[j][1] > data[j + 1][1]:
    #             data[j], data[j + 1] = data[j + 1], data[j]
    #
    #         # 第2个先顺序再第1个排序
    #         # 需要交换的情况
    #         # 1、当第二个字段不同，并且当前的小于下一个的时候
    #         # 2、当第二个字段相同，第一个字段不同，并且当前的小于下一个的时候
    #         # if data[j][1] < data[j + 1][1] or \
    #         #         (data[j][1] == data[j + 1][1] and data[j][0] < data[j + 1][0]):
    #         #     data[j], data[j + 1] = data[j + 1], data[j]

    # 使用冒泡排序进行 时间复杂度O(N^2)
    for i in range(n):
        for j in range(0, n - i - 1):
            # # 逆序 需要交换的情况
            # # 1、当第1个字段不同，并且当前的小于下一个的时候
            # # 2、当第1个字段相同，第2个字段不同，并且当前的小于下一个的时候
            if data[j][0] < data[j + 1][0] or (data[j][0] == data[j + 1][0] and data[j][1] < data[j + 1][1]):
                data[j], data[j + 1] = data[j + 1], data[j]

    # python 自带的排序 双轴快排算法（timsort） 复杂度是 O(N*log(N))
    # data.sort(key=lambda x: (-x[0], -x[1]))
    for row in data[:10]:
        print(*row)


s = """181 70
182 70
183 70
184 70
185 70
186 70
180 71
180 72
180 73
180 74
180 75""".split('\n')
data = list(map(lambda x: [int(i) for i in x.split()], s))

main(data)
