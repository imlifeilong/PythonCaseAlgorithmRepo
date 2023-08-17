# def main(nums, target):
#     length = len(nums)
#     for i in range(length):
#         for j in range(i + 1, length):
#             if nums[i] + nums[j] == target:
#                 print(i, j)
#                 return i, j
#
#
# nums = [2, 7, 11, 15]
# target = 9
#
# nums = [3, 2, 4]
# target = 6
#
# nums = [3, 3]
# target = 6
#
# main(nums, target)


res = 0
target = 0
numsSet = set()


def main():
    global res, target, numsSet

    nums = list(map(int, input().split()))
    k = int(input())
    target = int(input())

    nums.sort()
    combine(nums, k, [], 0, 0)

    print(res)


def combine(nums, n, lst, index, total):
    global res, target, numsSet

    if n == 0:
        if total == target:
            numsSet.add(tuple(lst))
            res += 1
    else:
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            if total + nums[i] > target:
                break
            lst.append(nums[i])
            combine(nums, n - 1, lst, i + 1, total + nums[i])
            lst.pop()


# main()


def ks(data, k, target):
    tmp = []
    res = process(0, 0, data, k, target, tmp)
    print(res)


def process(index, total, data, k, target, tmp):
    """
    第index个数的和时total
    :param index:
    :param total:
    :param data:
    :param k:
    :param target:
    :return:
    """
    # # 当k个数的和为target时，方案数+1
    if k == 0 and total == target:
        tmp.sort()
        print(tmp)
        return 1

    if index >= len(data) or (k <= 0 and total != target):
        return 0

    cur = data[index]
    print(f'当前值 {cur} 还剩{k - 1}')

    # 选择当前值
    tmp.append(data[index])
    p1 = process(index + 1, total + cur, data, k - 1, target, tmp)
    # 回溯
    tmp.pop()

    # 不选当前值
    p2 = process(index + 1, total, data, k, target, tmp)

    return p1 + p2


data = [int(i) for i in '-1 0 1 2 -1 -4'.split()]
k = 3
target = 0

# data = [int(i) for i in '2 7 11 15'.split()]
# k = 2
# target = 9

ks(data, k, target)
