def main(data, k, m):
    result = []

    dataset = [i.split(',') for i in data]
    index = 0
    while len(dataset) > 0:
        row = dataset[index]

        text = []
        for i in range(k):
            # 当前数组取完时，将整个数组去除，索引也要-1，否则会越界
            # 然后处理下一个数组
            if len(row) == 0:
                dataset.pop(index)
                index -= 1
                break
            # 取前k个数
            text.append(row.pop(0))

        if text:
            result.extend(text)
        index += 1
        # 当到最后一组时，从头开始
        if index >= len(dataset):
            index = 0

    print(','.join(result))


k = 3
m = 2
s = """2,5,6,7,9,5,7
1,7,4,3,4"""

# k = 4
# m = 3
# s = """1,2,3,4,5,6
# 1,2,3
# 1,2,3,4"""

data = s.split('\n')
main(data, k, m)
