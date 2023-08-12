def main(data):
    dp = [0] * len(data)
    dp[0] = data[0]
    for i in range(1, len(data)):
        # 索引从1开始
        if i < 3:
            # 状态转移 当前值与前一个值的关系
            # 前3轮 如果不选 则值为0
            dp[i] = max(dp[i - 1] + data[i], 0)
        else:
            # 如果不选则值还原为前3轮的值
            dp[i] = max(dp[i - 1] + data[i], dp[i - 3])
    print(dp[len(data) - 1])


s = '1,-5,-6,4,3,6,-2'.split(',')
# s = '1,-5,-6,4,3,6,-20'.split(',')
data = list(map(int, s))
main(data)
