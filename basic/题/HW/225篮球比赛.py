def main(data):
    def process(index, data, t):
        if index == len(data):
            return t
        if data[index] > t:
            return process(index + 1, data, t)
        p1 = process(index + 1, data, t - data[index])
        p2 = process(index + 1, data, t)
        return min(p1, p2)

    """
    将人分位两个对 A B
    所有人的整体实力为 w
    假设A 队的实力为 x，B队的实力为 (w - x)
    若要A队和B队的实力实力差最小，
    则 x - (w-x) 要无限接近 0
    x - w + x -> 0
    2x -> w
    x -> w/2
    也就是A队的实力接近 w/2
    
    """
    t = sum(data) / 2

    res = process(0, data, t)
    print(int(res * 2))

    t = sum(data) // 2
    n = len(data)
    dp = [[0] * (t + 1) for _ in range(n + 1)]
    # dp[i][j] 表示 前i个队员进入A队后实力为j
    # 依赖i+1 所以从下往上填表， 再从左往右

    for i in range(n - 1, -1, -1):
        # 背包容量从0开始，直到背包容量self.m被占满时
        for j in range(t + 1):
            # 当前货物的重量大于背包容量，装不上，只能去下个位置
            if data[i] > j:
                dp[i][j] = dp[i + 1][j]
            else:
                # 能装上货物， 装上当前货物后，再去下个位置，背包容量减去当前货物的重量
                p1 = dp[i + 1][j - data[i]] + data[i]
                # 能装上货物，但是不装，去下个位置
                p2 = dp[i + 1][j]
                dp[i][j] = max(p1, p2)

    # dp[0][t]表示A队最大的实力，则两队的差值为
    print(sum(data) - dp[0][t] * 2)


s = '10 9 8 7 6 5 4 3 2 1'.split()
data = list(map(int, s))
main(data)
