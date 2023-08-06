def main(data):
    res = []
    index = 0
    while len(data) > index:
        # 出队
        n = data.pop(0)
        for i in data:
            if i > n:
                res.append(i)
                break
        else:
            res.append(-1)

        # 判断后入队
        data.append(n)
        index += 1
    print(','.join(map(str, res)))


s = '3,4,5,6,3'.split(',')
# s = '2,5,2'.split(',')
# s = '2,3,6,-1,6,7'.split(',')
data = [int(i) for i in s]

main(data)
