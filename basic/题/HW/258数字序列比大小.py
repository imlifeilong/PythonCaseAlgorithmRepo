def main(s1, s2):
    s1.sort()
    s2.sort()

    score = 0
    # 比较策略 类似田忌赛马 
    for i in range(len(s1)):
        # B胜后 分数减1 将B的最大值去掉
        # 继续用B的最小值与A的下一位进行比较
        if s1[i] < s2[0]:
            score -= 1
            s2.pop()

        elif s1[i] > s2[0]:
            # A胜利后 分数加1 去掉B的最小值
            score += 1
            s2.pop(0)
    print(score)


s1 = list(map(int, '2 4 8 10'.split()))
s2 = list(map(int, '3 3 6 4'.split()))
main(s1, s2)
