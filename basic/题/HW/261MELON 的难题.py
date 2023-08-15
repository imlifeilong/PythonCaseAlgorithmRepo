def main(data):
    def process(index, data, t, tmp, cache):
        key = (index, t)
        if key in cache:
            return cache[key]

        if t == 0:
            curlen = min(len(tmp), len(data) - len(tmp))
            cache[key] = curlen
        elif index == len(data):
            cache[key] = float('inf')

        # 选择当前后比目标值大
        elif data[index] - t > 0:
            cache[key] = process(index + 1, data, t, tmp, cache)
        else:
            tmp.append(data[index])
            p1 = process(index + 1, data, t - data[index], tmp, cache)
            tmp.pop()
            p2 = process(index + 1, data, t, tmp, cache)
            cache[key] = min(p1, p2)
        return cache[key]

    cache = {}
    if sum(data) % 2 != 0:
        print(-1)
    else:
        t = sum(data) // 2
        res = process(0, data, t, [], cache)
        print(res)


def main1(data):
    n = len(data)
    if sum(data) % 2 != 0:
        print(-1)
    else:
        t = sum(data) // 2
        dp = [[0] * (t + 1) for _ in range(n + 1)]
        print(dp)
        # dp[i][j] 表示 前i个数 和为j的最少个数
        for i in range(t + 1):
            dp[0][i] = n
        dp[0][0] = 0

        for i in range(1, n + 1):
            c = data[i - 1]

            for j in range(1, t + 1):
                # 当前的值，大于剩余的值
                if c > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - c] + 1)

        if dp[n][t] == n:
            print(-1)
        else:
            print(dp[n][t])


s = '1 1 2 2'.split()
s = '1 1 1 1 1 9 8 3 7 10'.split()
data = list(map(int, s))
# main(data)
main1(data)
