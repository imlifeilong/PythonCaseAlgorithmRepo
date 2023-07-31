"""
100个人围成一圈，每个人有一个编码，编号从1开始到100。
他们从1开始依次报数，报到为M的人自动退出圈圈，然后下一个人接着从1开始报数，
直到剩余的人数小于M。请问最后剩余的人在原先的编号为多少？
例如输入M=3时，输出为： “58,91” ，输入M=4时，输出为： “34,45,97”。

"""


def baoshu(k, nums):
    index = 1  # 大循环指针

    # 总人数小于k的时候，结束
    while len(nums) >= k:
        i = 1  # 小循环的指针
        length = len(nums)
        for j in range(length):
            # 当报到第k个人时，出队，循环指针重新指向1
            if index == k:
                # print("出队", nums[i-1])
                del nums[i - 1]
                index = 1

            else:
                # 继续下一个人报数
                index += 1
                i += 1

    print(nums)


def baoshu2(k, nums):
    """
    队列实现
    :param k:
    :param nums:
    :return:
    """
    index = 1
    while len(nums) >= k:
        n = nums.pop(0)  # 出队
        if index == k:
            
            index = 1  # 符合条件，重新开始报数
        else:
            nums.append(n)  # 不符合，入队继续报数
            index += 1
    print(nums)


k = 4
n = list(range(1, 10))
print(n)
baoshu(k, n)
# baoshu2(k, n)
