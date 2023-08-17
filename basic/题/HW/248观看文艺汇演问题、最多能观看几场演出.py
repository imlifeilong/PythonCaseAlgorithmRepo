def main(data):
    cache = []
    for row in data:
        start = row[0]
        end = start + row[1]
        cache.append((start, end))

    # 第一场结束时间
    prev = cache[0][1]
    count = 1
    # 从第二场开始
    for i in range(1, len(data)):
        # 当前的开始时间，结束时间
        start = data[i][0]
        end = data[i][1]
        # 计算当前场的开始时间 比 上一场的结束时间间隔超过15分钟的 说明可以连续观看
        if start - prev > 15:
            # 在继续比较当前场的结束时间  和 下一场的开始时间
            prev = end
            count += 1
    print(count)


s = '''720 120
840 120'''.split('\n')
s = '''0 60
90 60'''.split('\n')
data = list(map(lambda x: [int(i) for i in x.split()], s))

main(data)
