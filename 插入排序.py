# _*_ coding:utf-8 _*_
'''
一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：

从第一个元素开始，该元素可以认为已经被排序
取出下一个元素，在已经排序的元素序列中从后向前扫描
如果该元素（已排序）大于新元素，将该元素移到下一位置
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
将新元素插入到该位置后
重复步骤2~5
如果比较操作的代价比交换操作大的话，可以采用二分查找法来减少比较操作的数目。
该算法可以认为是插入排序的一个变种，称为二分查找插入排序。
'''

def insert(alist):
    alen = len(alist)
    for i in range(1,alen): #默认第一个数为有序序列
        index = i
        item = alist[index]
        # 原始序列中第一个元素，插入到有序列中合适的位置
        while index > 0 and alist[index-1] > item:
            alist[index] = alist[index-1]
            index -= 1
        alist[index] = item
    return alist


if __name__ == "__main__":
    alist = [23,4,66,43,14,8,32]
    print(insert(alist))

    