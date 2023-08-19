def main(s, k):
    n = len(s)
    left = 0
    right = 0
    count = 0
    # maxlen = 0
    points = {}  # 记录符合长度时 所有可以放棋的位置 key是长度 val是所有能达到key长度时，0的位置
    while right < n:
        # print(right, s[right])
        if s[right] == '0':
            count += 1
        # right 指向的值不是当前要下的棋时 str(int(k) * -1) 当前棋的对方
        elif s[right] == str(int(k) * -1):
            # left 到 right之间0的位置
            if '0' in s[left:right + 1]:
                index0 = s.index('0', left, right + 1)
                # 记录 能达到当前长度时 0的位置
                if right - left not in points:
                    points[right - left] = []
                points[right - left].append(index0)
            # maxlen = max(maxlen, right - left)
            # 0的个数重新开始计算
            count = 0
            # right 移向下一个位置
            right += 1
            # left 紧跟right，然后进行下一位置的比较
            left = right
            continue

        # 当窗口中的0的个数超过1个时，需要移动left来控制0的个数
        while count > 1:
            # 当left指的位置值为0时，此时0的个数需要减1，然后移动left
            if s[left] == '0':
                count -= 1
            left += 1
        # print(right - left + 1)

        # 记录此时 窗口长度 0所在的位置
        if '0' in s[left:right + 1]:
            index0 = s.index('0', left, right + 1)

            if right - left + 1 not in points:
                points[right - left + 1] = []
            points[right - left + 1].append(index0)

        # maxlen = max(maxlen, right - left + 1)
        right += 1

    # 找到最大的长度时 所有0的位置，取最靠近中间的位置
    maxkey = max(points.keys())
    # print(maxkey)
    # abs(x - n // 2) 每个值与中间值的差，绝对值最小的，就是离中间近的
    res = sorted(points[maxkey], key=lambda x: abs(x - n // 2))
    print(res[0])


s = '-1 0 1 1 -1 1 0 1 0 1 -1 1'.split()
s = '-1 0 1 1 1 0 1 0 1 -1 1'.split()
n = '1'

# n = '-1'
# s = '-1 0 1 1 1 0 1 0 1 -1 1'.split()

# n = '1'
# s = '0 0 0 0 1 0 0 0 0 1 0'.split()

main(s, n)

import collections


def function(numList, nums) -> int:
    n = len(numList)
    counter = collections.Counter()
    left = 0
    right = 0
    ans = 0
    pos = []
    while right < n:
        counter[numList[right]] += 1
        while counter[-nums] > 0 or right - left + 1 - counter[nums] > 1:
            counter[numList[left]] -= 1
            left += 1
        if ans < right - left + 1:
            ans = right - left + 1
            for i, x in enumerate(numList[left:right + 1]):
                if x == 0:
                    pos = [left + i]
        elif ans == right - left + 1:
            for i, x in enumerate(numList[left:right + 1]):
                if x == 0:
                    pos.append(left + i)
        right += 1
    mid = (n - 1) // 2
    pos.sort(key=lambda x: abs(x - mid))
    return pos[0]


numsList = [-1, 0, 1, 1, 1, 0, 1, -1, 1]
# numsList = [0,0,0,0,1,0,0,0,0,1,0]

# print(function(numsList, 1))
