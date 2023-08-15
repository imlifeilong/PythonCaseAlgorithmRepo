import math


def main(data, n):
    def process(index, data, t):
        # 块数占满了 或者 遍历完了所有的文件
        if t == 0 or index == n:
            return 0
        # 文件占用块数 大于软盘容量，去下一个
        curval = math.ceil(data[index] / 512)
        if curval > t:
            return process(index + 1, data, t)

        # 可以装当前文件的时候，分两种情况 选择当前值 或 不选， 取两种情况的最大值
        # 选择当前文件，减去当前文件所占的块数，加上文件真实字节大小，然后去下一个
        p1 = process(index + 1, data, t - curval) + data[index]
        # 不选当前值，去下一个
        p2 = process(index + 1, data, t)

        return max(p1, p2)

    w = 1474560 // 512  # 总块数 即 背包容量

    res = process(0, data, w)
    print(res)

    # 动态规划
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    # dp[i][j] 表示前i个文件放到块数为j的盘里最大能放的文件字节大小
    # 依赖i+1 所以从下往上填表， 再从左往右

    for i in range(n - 1, -1, -1):
        for j in range(w + 1):
            # 文件占用空间
            real_size = math.ceil(data[i] / 512)
            # 文件的空间大于容量时，只能 去下一个位置
            if real_size > j:
                dp[i][j] = dp[i + 1][j]
            else:
                # 装上当前的文件， 加上文件真实大小
                p1 = dp[i + 1][j - real_size] + data[i]
                # 不装当前的文件
                p2 = dp[i + 1][j]
                dp[i][j] = max(p1, p2)
    print(dp[0][w])


n = 6
s = '''400000
200000
200000
200000
400000
400000'''.split('\n')

# n = 3
# s = '''737270
# 737272
# 737288'''.split('\n')
data = list(map(int, s))

main(data, n)
