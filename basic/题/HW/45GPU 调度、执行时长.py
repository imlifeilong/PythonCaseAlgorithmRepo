def main(data, n):
    count = 0
    task = 0
    for i in range(len(data)):
        # 当前任务和上一轮留下的任务 总和大于 n，执行完后需要遗留任务
        if data[i] + task > n:
            task = data[i] + task - n
        else:
            # 不虚遗留任务
            task = 0
        count += 1

    # 调度完后，剩余任务完成需要的时间
    while task > 0:
        task -= n
        count += 1
    print(count)


"""
第一组
3
1 2 3 4 5
第1秒 1
2 2
3 3
4 3 剩余1
5 2 剩余3
6 3

第二组
4
5 4 1 1 1
第1秒 4 剩余1
2 3 剩余 1
3 2 本次1 加上次1
4 1
5 1
"""
s = '1 2 3 4 5'.split()
n = 3

s = '5 4 1 1 1'.split()
n = 4
data = list(map(int, s))
main(data, n)
