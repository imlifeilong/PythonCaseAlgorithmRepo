def main(data):
    def f1(index, data):
        '''
        选第一个 不选最后一个
        0 - n-2
        0 2 4 ... n-2
        '''
        if len(data) == 1:
            return data[0]
        # 如果到最后一位不选，然后结束
        if index == len(data) - 1:
            return 0
        # 到倒数第2位的时候 选择 结束
        if index == len(data) - 2:
            return data[index]

        return max(f1(index + 1, data), f1(index + 2, data) + data[index])

    def f2(index, data):
        '''
        不选第一个， 选最后一个
        1 - n-1
        1 3 5 ... n-1
        '''
        # 整个序列遍历完 并结束
        if index == len(data):
            return 0
        # 到最后1位的时候，选择，并结束
        if index == len(data) - 1:
            return data[index]
        # 两种情况，
        # 1、不选下一个值，跳过 中间隔超过1个数，2个 3个的情况
        # 2、选下一个值因为中间要隔一个值所以是index+2
        # 取两种情况的最大的情况
        return max(f2(index + 1, data), f2(index + 2, data) + data[index])

    # 环形的 意味着第一个和最后一个中 只能选择一个
    # 分两种情况 选第一个的情况 不选第一个的情况
    res = max(f1(0, data), f2(1, data))
    print(res)

    def process_dp(data):
        dp = [0] * len(data)
        dp[0] = data[0]

        for i in range(1, len(data)):
            if i == 1:
                dp[i] = max(data[i], dp[i - 1])
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + data[i])

        return dp[len(data) - 1]

    if len(data) > 1:
        # 不选最后一个
        p1 = list(map(int, data[:-1]))
        # 不选第一个
        p2 = list(map(int, data[1:]))
        res = max(process_dp(p1), process_dp(p2))
        print(res)
    else:
        print(data[0])


s = '2 3 2'.split()
s = '1 2 3 1'.split()
s = '1 2'.split()
data = list(map(int, s))
main(data)
