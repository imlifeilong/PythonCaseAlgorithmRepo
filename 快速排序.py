# _*_ coding:utf-8 _*_
'''
快速排序是一种划分交换排序
基本思想是：
1．先从数列中取出一个数作为基准数，一般是第一个数。
2．将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3．再对左右区间重复第二步，直到各区间只有一个数。
若序列基本有序时，蜕变成冒泡排序，最坏情况是已经排好序
平均时间复杂度O(nlogn)
---------------------------------------------------------------------------------------------------------
快速排序采用“分而治之、各个击破”的观念，此为原地（In-place）分割版本。
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。

步骤为：

从数列中挑出一个元素，称为“基准”（pivot），
重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。在这个分割结束之后，该基准就处于数列的中间位置。这个称为分割（partition）操作。
递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。
递归到最底部时，数列的大小是零或一，也就是已经排序好了。这个算法一定会结束，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。
'''

def swift(alist, low, hight):
    # 选择第一个数作为基点，位置为t0
    item = alist[low]
    while low < hight:
        #从右向左依次和基点的数比较，位置为t1，如果大于基点，位置向左挪1位(t1=t1-1)
        while alist[hight] >= item and low < hight:
            hight -= 1

        #如果有小于基点的数，放到t0，左端位置向右挪1位(t2=t2+1)
        if low < hight:
            alist[low] = alist[hight]
            low += 1

        #从左往右找大于基点的数，位置为t2，如果小于基点，位置向右挪1位(t2=t2+1)
        while alist[low] < item and low < hight:
            low += 1

        #如果有大于基点的数，放到t2，右端的位置向左挪1位(t1=t1-1)
        if low < hight:
            alist[hight] = alist[low]
            hight -= 1

    #调整完后基点左边的数小于基点，右边的数大于基点
    alist[low] = item
    # 返回调整后基点的位置
    return low
    
def quick(alist, left, right):
    #二分数列
    if left < right:
        mid = swift(alist, left, right)
        quick(alist, left, mid-1)
        quick(alist, mid+1, right)
    return alist


if __name__ == "__main__":
    alist = [23,4,66,23,4,66,43,14,8,32,43,14,8,32]
    print(quick(alist, 0, len(alist)-1))

    