def main(data, n):
    def process(index, data, n, tmp, idxset):
        # 剪枝，长度大于3的不考虑
        if len(tmp) > 3:
            return
        # 考虑到有0的情况下，长度必须为3才满足退出条件
        if n == 0 and len(tmp) == 3:
            # nonlocal 用来声明修改外部函数值
            nonlocal result, minval
            if minval > sum(idxset):
                minval = sum(idxset)
                result = tmp[:]
            return

        if index == len(data):
            return
        # 当前值太大，去下一位置
        if data[index] > n:
            return process(index + 1, data, n, tmp, idxset)

        # 选择当前值，并记录值和索引
        tmp.append(data[index])
        # print('选择当前值', tmp)
        idxset.append(index)

        process(index + 1, data, n - data[index], tmp, idxset)
        # 不选的情况
        tmp.pop()
        idxset.pop()

        process(index + 1, data, n, tmp, idxset)

    result = None
    minval = float('inf')
    process(0, data, n, [], [])
    print(result)


n = 9
data = [1, 4, 5, 2, 0, 2]  # [4,5,0]
n = 9
data = [1, 5, 2, 0, 2, 4]
#
n = 12
data = [-1, 2, 4, 9]
main(data, n)
