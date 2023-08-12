def main(s1, s2):
    one = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    tmps = {x: 4 for x in one}
    # 去除自己的牌
    for c1 in s1:
        if c1 in one:
            tmps[c1] -= 1
    # 去除已经出的牌
    for c2 in s2:
        if c2 in one:
            tmps[c2] -= 1
    res = 'NO-CHAIN'

    # tmps = {'3': 1, '4': 1, '5': 1, '6': 2, '7': 2, '8': 1, '9': 0, '10': 3, 'J': 3, 'Q': 3, 'K': 3, 'A': 1}

    # 剩下对手的牌
    maxlen = 0

    # for i in range(len(one)):
    #     print('-------', one[i])
    #     # 判断是否右当前的牌
    #     if tmps[one[i]] > 0:
    #         left = i
    #         right = i
    #         while right < len(one) - 1:
    #             # 下一位牌是连续的
    #             if tmps[one[right + 1]] > 0:
    #                 print(one[right + 1])
    #                 right += 1
    #             else:
    #                 break
    #         if tmps[one[len(one) - 1]] > 0:
    #             right += 1
    #         curlen = right - left + 1
    #         if curlen >= 5 and curlen >= maxlen:
    #             maxlen = curlen
    #             res = '-'.join(one[left:left + curlen])
    # print(res)



    i = 0
    while i < len(one):
        # 判断是否右当前的牌
        if tmps[one[i]] > 0:
            left = i
            right = i
            # 找到连续的右边界
            while right < len(one) - 1:
                # 下一位牌是连续的
                if tmps[one[right + 1]] > 0:
                    right += 1
                else:
                    break

            # 判断最后一位是否连续
            if right < len(one) - 1 and tmps[one[right + 1]] > 0:
                right += 1
            # 计算当前区间的长度， 大于5的 并且比之前长度长的，记录下来
            curlen = right - left + 1
            if curlen >= 5 and curlen >= maxlen:
                maxlen = curlen
                res = '-'.join(one[left:left + curlen])
            # 加速
            i = left + curlen + 1
        else:
            i += 1
    print(res)


s1 = '3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A'.split('-')
s2 = '4-5-6-7-8-8-8'.split('-')
# s1 = '3-3-3-3-8-8-8-8'.split('-')
# s2 = 'K-K-K-K'.split('-')
main(s1, s2)
