def main(data):
    minval = float('inf')
    for i in range(len(data) // 2):
        # i表示第一步
        tmp = 1  # 步数，从第二步开始计算
        index = i
        # 计算剩下的步数，能否到达终点
        while index < len(data[i:]):
            tmp += 1
            if data[index] == len(data[index:]) - 1:
                # 当前节点刚好可以到达终点，记录步数
                minval = min(tmp, minval)
                break
            if data[index] >= len(data) - 1:
                # 当前节点超过了终点
                break
            # 要走当data[index]步
            index += data[index]

    if minval == float('inf'):
        print('-1')
    else:
        print(minval)


s = '7 5 9 4 2 6 8 3 5 4 3 9'
# s = '7 5 9 4 2 7 1 1 1 1 1 1 1'
# s = '1 2 3 7 1 5 9 3 2 1'
data = list(map(int, s.split()))
main(data)
