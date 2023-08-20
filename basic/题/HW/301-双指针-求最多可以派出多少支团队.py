def main(data, k):
    n = len(data)
    left = 0
    right = n - 1
    count = 0
    # 对数据排序
    data.sort()
    while left < right:
        # 先判断右边的大值 能否单独达到标准
        if data[right] >= k:
            count += 1
            right -= 1

        # 使用对撞指针，判断左+右的值 是否满足标准
        elif data[right] + data[left] >= k:
            count += 1
            right -= 1
            left += 1
        # 如果两种情况，都不满足，移动left
        else:
            left += 1
    print(count)


s = '3 1 5 7 9'.split()
s = '3 1 5 7 9 2 6'.split()
s = '1 1 9'.split()
n = 8
data = list(map(int, s))
main(data, n)
