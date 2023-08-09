def main(n):
    cache = {}
    res = action_cache(n, cache)
    print(res)
    res = action_dp(n)
    print(res)


def action_cache(n, cache):
    if n == 0:
        return 0
    # 1个或2个台阶的时候 只能一步一步爬，只有1种方法
    if n in (1, 2):
        return 1
    # 3个台阶的时候 一步一步的爬，或者一次三步
    if n == 3:
        return 2
    if n not in cache:
        cache[n] = action_cache(n - 1, cache) + action_cache(n - 3, cache)
    return cache[n]


def action_dp(n):
    if n == 0:
        return 0
    # 1个或2个台阶的时候 只能一步一步爬，只有1种方法
    if n in (1, 2):
        return 1
    # 3个台阶的时候 一步一步的爬，或者一次三步
    # if n == 3:
    #     return 2

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3]

    return dp[n]


# f(n) = f(n-1)+f(n-3)

n = 4
main(n)
