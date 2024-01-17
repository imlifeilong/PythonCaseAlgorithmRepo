m = int(input())
tasks = [[] for _ in range(m)]
for i in range(m):
    n = int(input())
    task = [[] for _ in range(n)]
    for j in range(n):
        task[j] = list(map(int, input().split()))
    tasks[i] = task


def result():
    tasks.sort(key=lambda x: -x[1]) # 运行时间降序排列
    n = len(task)
    #  dp[i] 第i个机器完成工作至少需要用时
    dp = [0] * n
    dp[0] = tasks[0][0] + task[0][1]
    for i in range(1, n):
        #
        dp[i] = max(dp[i-1], dp[i-1]-task[i-1][1] + task[i][0] + task[i][1])
    print(dp[n-1])

result()
# if __name__ == '__main__':
