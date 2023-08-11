def main(s1, s2):
    # 思路 只需要关注s2中值为0的位置，s1中对应的位置的值进行交换（0换1 1换0），才能改变值
    # s1 = 010
    # s2 = 110
    # s2中第三个位置是0 只需对s1中第三位置的值0 换为1，并且只有1中换法 s1 = 001

    # 找到s2中值为0位置
    s2_index_0 = []
    for i, c in enumerate(s2):
        if c == '0':
            s2_index_0.append(i)

    # 分别找到s1 中1 的位置 s1中0的位置

    s1_index_1 = []
    s1_index_0 = []
    for j, c in enumerate(s1):
        if c == '0':
            s1_index_0.append(j)
        else:
            s1_index_1.append(j)

    result = []
    for h in range(len(s1)):
        # 找到s2为0 的位置，s1对应的位置
        if h in s2_index_0:
            # s1中对应的位置如果是0 分别将s1中的所有1和该位置的0 进行交换
            if s1[h] == '0':
                for x in s1_index_1:
                    tmp = s1[:]
                    tmp[h], tmp[x] = tmp[x], tmp[h]
                    result.append(''.join(tmp))

            else:
                # s1中对应的位置如果是1 分别将s1中的所有0和该位置的1 进行交换
                for y in s1_index_0:
                    tmp = s1[:]
                    tmp[h], tmp[y] = tmp[y], tmp[h]
                    result.append(''.join(tmp))
    # 将结果去重
    reset = set(result)
    print(reset, len(reset))


s1 = list('011011')
s2 = list('110110')

s1 = list('010')
s2 = list('110')

s1 = list('1001')
s2 = list('0001')
main(s1, s2)
