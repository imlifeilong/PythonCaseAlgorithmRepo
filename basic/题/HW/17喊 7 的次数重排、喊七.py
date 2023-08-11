def main(data):
    tmplist = list(range(len(data)))
    count = sum(data)  # 喊过的总次数
    result = [0] * len(data)

    index = 1
    # 总次数减完后就退出
    while count > 0:
        # 循环进行喊数，出队
        cur = tmplist.pop(0)
        # 喊过的情况，对应的位置加1次，总次数减1
        if '7' in str(index) or index % 7 == 0:
            result[cur] += 1
            count -= 1
        # 喊完后入队，继续喊数
        tmplist.append(cur)
        index += 1
    print(result)


s = '0 0 0 2 1'.split()
# s = '0 1 0'.split()
data = list(map(int, s))
# print(data)

main(data)
