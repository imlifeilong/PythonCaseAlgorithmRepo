# _*_ coding:utf-8 _*_
'''
快速排序是一种划分交换排序
基本思想是：
1．先从数列中取出一个数作为基准数，一般是第一个数。
2．将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3．再对左右区间重复第二步，直到各区间只有一个数。
若序列基本有序时，蜕变成冒泡排序，最坏情况是已经排好序
平均时间复杂度O(nlogn)
'''

def swift(alist,left,right):
    low = left
    hight = right
    item = alist[left]
    while low < hight:
        #从右向左找小于item的数
        while alist[hight] > item and low < hight:
            hight -= 1
        #找到后换到item左边
        if low < hight:
            alist[low] = alist[hight]
            low += 1
        #从左往右找大于item的数
        while alist[low] < item and low < hight:
            low += 1
        #找到后换到item右边
        if low < hight:
            alist[hight] = alist[low]
            hight -= 1
    #item归位
    alist[low] = item
    return low

    
def quick(alist):
    left = 0
    right = len(alist) - 1
    #二分数列
    if left < right:
        mid = swift(alist,left,right)
        swift(alist,left,mid-1)
        swift(alist,mid+1,right)
    return alist
    
    
if __name__ == "__main__":
    alist = [23,4,66,23,4,66,43,14,8,32,43,14,8,32]
    print quick(alist)

    