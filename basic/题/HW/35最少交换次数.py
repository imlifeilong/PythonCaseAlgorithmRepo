def main(data, t):
    """
    思路
    1、找到data中所有小于t的值的个数 w
    2、固定滑动窗口的大小为w，遍历data，统计在窗口内小于t的个数
    3、取所有值的最小值
    """
    minval = float('inf')
    less_t_data = [x for x in data if x < t]
    less_t_data_len = len(less_t_data)
    for i in range(len(data) - less_t_data_len + 1):
        window = data[i:i + less_t_data_len]
        # 记录窗口中的值不小于t的个数，就是需要交换的次数
        count = 0
        for j in window:
            if j >= t:
                count += 1
        minval = min(minval, count)

    print(minval)


s = '1 3 1 4 0'.split()
t = 2

s = '1 6 3 9 8 4 2 5 7'.split()
t = 5
s = '0 0 0 1 0'.split()
t = 2

s = '2 3 2'.split()
t = 1
data = list(map(int, s))
main(data, t)
