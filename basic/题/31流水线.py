def main(data, m, n):
    data.sort()
    # 任务小于流水线时，直接返回最耗时的
    if n < m:
        print(data[-1])
        return
    # 任务大于流水线时，先处理m个耗时小的任务，再按顺序处理其他的
    start_job = data[:m]
    for i in range(m, n):
        # i%m 获取start_job中的索引，然后按顺序加上剩余任务的时间
        start_job[i % m] += data[i]
    print(max(start_job))


# m 个流水线
# n 个任务
m, n = 3, 5
s = '8 4 3 2 10'.split()

m, n = 3, 6
s = '8 4 6 7 1 10'.split()

data = list(map(int, s))
main(data, m, n)
