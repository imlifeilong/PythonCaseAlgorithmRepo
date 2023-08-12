def main(data):
    last_index = -1
    res = 0
    i = 0
    while i < len(data):
        # 第一行
        if last_index < 0:
            res += min(data[i])
            last_index = data[i].index(res)
        else:
            # 找到上次索引位置，然后删除对应的值
            last_value = data[i].pop(last_index)
            # 在剩余的值中选择最小的
            minval = min(data[i])
            # 将删除的值还原，找到本次选择的索引
            data[i].insert(last_index, last_value)
            last_index = data[i].index(minval)
            res += minval
        i += 1
    print(res)


s = """15 8 17
12 20 9
11 7 5""".split('\n')
data = list(map(lambda x: [int(i) for i in x.split()], s))
print(data)
main(data)
