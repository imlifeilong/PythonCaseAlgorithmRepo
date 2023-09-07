# _*_ coding:utf-8 _*_
'''
快速排序是一种划分交换排序
基本思想是：
1．先从数列中取出一个数作为基准数，一般是第一个数。
2．将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3．再对左右区间重复第一、二步，直到各区间只有一个数。
最坏情况 序列已经有序，蜕变成冒泡，时间复杂度为O(n2)空间复杂的O(n)
最好情况 每次比较项刚好在中间位置， 时间复杂度O(nlogn)空间复杂度O(logn)
平均复杂度 实在大量样本下使用随机抽样快排计算出来得概率
不稳定
优势 代码简单常数项小

归并排序 时间复杂度O(nlogn) 空间复杂度 O(n) 常数项大
---------------------------------------------------------------------------------------------------------
快速排序采用“分而治之、各个击破”的观念，此为原地（In-place）分割版本。
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。

步骤为：

从数列中挑出一个元素，称为“基准”（pivot），
重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。在这个分割结束之后，该基准就处于数列的中间位置。这个称为分割（partition）操作。
递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。
递归到最底部时，数列的大小是零或一，也就是已经排序好了。这个算法一定会结束，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。
'''

"""
[5, 2, 8, 5, 9, 3, 5]
单路快速排序
    基准值选为 5
    小于等于基准值：[2, 3]
    大于基准值：[8, 9]
    基准值 5 有三个重复的元素在数组中，但它们被划分到了不同的部分。
    这会导致每次分区只能减少一个元素的规模，从而导致性能降低。
    即 基准值左边的值 [2, 3]
    基准值 右边的值 [5, 9, 5, 8] 和基准值相同的值是分散再右边的
双路快速排序 将数组分成三部分：小于基准、等于基准和大于基准，其中：
    小于基准值：[2, 3]
    等于基准值：[5, 5, 5]
    大于基准值：[8, 9]
    将重复的元素集中再一起，能够更好地处理存在重复元素的情况

三路快速排序 三路快速排序使用三个指针，从数组的左端、右端和中间开始分别向中间遍历
    左指针找到小于基准值的元素，
    右指针找到大于基准值的元素，
    而中间指针用于处理等于基准值的元素。
    遍历过程中，将小于基准值的元素交换到左边，将大于基准值的元素交换到右边，等于基准值的元素则保持在中间
    less 指向小于基准值的区域的末尾
    more 指向大于基准值的区域的起始
    left 用于遍历整个序列
"""


# def swift_1(data, left, right):
#     '''
#     选左边为基准数
#     '''
#     item = data[left]
#     index = left + 1
#     mid = index
#
#     while index <= right:
#         # 当left所指的值 小于基准值时，移动到mid左边
#         if data[index] < item:
#             data[index], data[mid] = data[mid], data[index]
#             mid += 1
#         index += 1
#     data[left], data[mid - 1] = data[mid - 1], data[left]
#     return mid - 1


def swift_1(data, left, right):
    """
    单路快速排序使用一个基准元素将数组分成两个部分：小于基准的部分和大于基准的部分。
    """
    # 选右边值为基准数
    item = data[right]
    mid = left
    while left < right:
        # 从左往右遍历，当left所指的值小于基准值时，和mid所指的值交换，
        # mid向右移动一位，保持mid左边的值小于基准值
        if data[left] < item:
            data[left], data[mid] = data[mid], data[left]
            mid += 1
        left += 1
    # 当扫描完成后，将right所指的数放到mid的位置，此时mid左边的数于，右边数大于等于
    data[mid], data[right] = data[right], data[mid]
    return mid


def swift_2(data, left, right):
    # 单路快排 可能会在存在大量重复元素时性能下降
    # 二路快排 分别从数组的左端和右端开始，将数组分成两个部分：小于基准、等于或大于基准
    # 是通过 左右两个指针互相交换来减少交换操作，可以在存在重复元素的情况下保持较好的性能

    # 最左边的选为基准值，拿出来后，此时left的位置是空的
    item = data[left]
    # 应该有一个置空的操作
    # data[left] = None
    while left < right:
        # 从右往左扫，直到扫到小于基准值的 停下来，
        # 扫的时候要满足left < right 比如 [0,1,2,3,4] 这种数据，如果选第一个数为基准值，
        # 从右往左扫描的时候，直到第一个数也找不到一个数小于基准值的，
        # 不限制的话 right就会继续向左，从而越界，导致错误
        while left < right and data[right] > item:
            right -= 1

        # 如果left和right未相遇，把找到的那个小值，交换到基准值的位置，
        # 并将left向右移动，此时 right的位置为空了
        if left < right:
            data[left] = data[right]
            # 应该有一个置空的操作
            # data[right] = None
            left += 1

        # 然后从左往右扫，直到扫到大于或等于基准值的 停下来
        # 同理 [4,3,2,1,0] 的情况，如果第一个数为基准，从左往右扫描的时候，
        # 直到最后一个数也找不到一个大于等于基准数的值
        # 如果不限制的话，left就会继续向右，导致越界
        while left < right and data[left] < item:
            left += 1

        # 如果left和right未相遇，把找到的那个大值，交换到right的位置，并将right向左移动，此时left的位置为空
        if left < right:
            data[right] = data[left]
            # 应该有一个置空的操作
            # data[left] = None
            right -= 1

    # 当left和right相遇的时候，就是要好的mid的位置，即mid左边都是小于基准值，mid右边都是大于等于基准值
    # 所以将基准值放到mid的位置
    data[left] = item
    # 返回调整后基点的位置
    return left


def swift_3(data, left, right):
    """
    三路快排 将数组分为三个区 小于区 等于区 大于区 每次等于区域拍好之后，不会再参与下次排序
    [0, less) 小于 base
    [less, left) 等于 base
    [left, more] 未处理，所以要遍历的区域
    (more, right) 大于base
    """
    base = data[right]

    less = left  # less指向小于区域的下一位
    more = right  # more指向大于区域的前一位
    # left

    # 遍历整个未处理的区域
    # 小于区域 [0, less) 等于区域[less, left) 未处理[left, more] 大于区域(more, right)
    while left <= more:

        if data[left] < base:
            # 未处理的区域中，当前值 小于基准值，则交换到小于区域 less 和 left向右移动
            data[left], data[less] = data[less], data[left]
            left += 1
            less += 1
        elif data[left] > base:
            # 未处理的区域中，当前值，大于基准值，则交换的大于区域，more向左移动
            data[left], data[more] = data[more], data[left]
            more -= 1
        else:
            # 如果相等，跳过
            left += 1
    # 返回小于区域与等于区 和 等于区与大于区域的 边界
    return less, more


def quick1(alist, left, right):
    # 二分数列
    if left < right:
        # 索引 [0,1,2,3,4,5,6]
        # mid=3时，左边的索引范围0-2 右边的索引范围4-6
        # 因为每次分隔后，mid的位置就排好了，以后都不会变了，所以不参与以后的排序
        # 左闭右开的原则，所以左边的索引范围是 left, mid-1 右边的索引范围是 mid+1, right
        mid = swift_1(alist, left, right)
        quick1(alist, left, mid - 1)
        quick1(alist, mid + 1, right)
    return alist


def quick2(alist, left, right):
    # 二分数列
    if left < right:
        # 索引 [0,1,2,3,4,5,6]
        # mid=3时，左边的索引范围0-2 右边的索引范围4-6
        # 因为每次分隔后，mid的位置就排好了，以后都不会变了，所以不参与以后的排序
        # 左闭右开的原则，所以左边的索引范围是 left, mid-1 右边的索引范围是 mid+1, right
        mid = swift_2(alist, left, right)
        quick2(alist, left, mid - 1)
        quick2(alist, mid + 1, right)
    return alist


def quick3(alist, left, right):
    # 二分数列
    if left < right:
        # 索引 [0,1,2,3,4,5,6]
        # mid=3时，左边的索引范围0-2 右边的索引范围4-6
        # 因为每次分隔后，mid的位置就排好了，以后都不会变了，所以不参与以后的排序
        # 左闭右开的原则，所以左边的索引范围是 left, mid-1 右边的索引范围是 mid+1, right
        mid = swift_3(alist, left, right)
        quick3(alist, left, mid[0] - 1)
        quick3(alist, mid[1] + 1, right)
    return alist


if __name__ == "__main__":
    # alist = [23, 4, 66, 23, 4, 66, 43, 14, 8, 32, 43, 14, 8, 32]
    alist = [5, 4, 2, 6, 1, 8, 9, 5]
    alist = [5, 2, 8, 5, 9, 3, 5]
    alist = [5, 1, 3, 2, 5, 5, 2, 1, 3, 8, 5]
    # alist = [3, 1, 5, 2, 8, 5, 9, 3, 5, 1, 2, 3]
    # print(quick1(alist, 0, len(alist) - 1))
    print(quick2(alist, 0, len(alist) - 1))
    # print(quick3(alist, 0, len(alist) - 1))
