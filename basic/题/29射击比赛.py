def main(data):
    index = list(map(int, data[0].split(',')))
    score = list(map(int, data[1].split(',')))

    # 聚合选手分数
    mapping = {}
    for i in range(len(index)):
        if index[i] not in mapping:
            mapping[index[i]] = []
        mapping[index[i]].append(score[i])

    # 求个选手前3分数之和
    result = []
    for k, v in mapping.items():
        x = k, sum(sorted(v, reverse=True)[:3])
        result.append(x)

    # 先对分数排序，再对序号排序
    res1 = sorted(result, key=lambda x: (x[1], x[0]), reverse=True)

    res = ','.join([str(i[0]) for i in res1])
    print(res)


s = """3,3,7,4,4,4,4,7,7,3,5,5,5
53,80,68,24,39,76,66,16,100,55,53,80,55"""
data = s.split('\n')
main(data)
