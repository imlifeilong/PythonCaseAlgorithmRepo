def main(data, k):
    tmp = sorted(data)
    # 计算原数组的中位数
    mid = tmp[len(data) // 2]

    minval = float('inf')
    index = -1  # 符合条件的位置

    # len(data) - k +1 为了保证不溢出
    for i in range(len(data) - k + 1):
        # 计算i 到 i+k-1的区间 因为range左闭右开 所以end 等于 (i+k-1) +1
        start = i
        end = (i + k - 1) + 1

        # 计算 x[0]-x[1]-x[2]...x[i+k-1]
        tmp = data[start]
        for j in range(start + 1, end):
            tmp -= data[j]

        # 计算离中位数的距离
        tmpval = abs(tmp - mid)
        # 如果距离比较小，则记录下，并且记录当前值的位置i
        if tmpval < minval:
            minval = tmpval
            index = i

    print(index)


data = [1, 2, 3, 3]
k = 2

# data = [50, 50, 2, 3]
# k = 2

main(data, k)
