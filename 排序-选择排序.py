# _*_ coding:utf-8 _*_
'''
选择排序过程：
    1、首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    2、然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    3、以此类推，直到所有元素均排序完毕。
比较次数n(n-1)/2
时间复杂度O(n2)
'''

def select(alist):
    alen = len(alist)
    for i in range(alen):
        _min = i #选择第一个点为最小点
        # 再扫描剩下的元素，和最小点比较
        for j in range(i+1, alen):
            # 如果小于最小点，则选择该点位置为最小点
            _min = j if alist[j] < alist[_min] else _min
        
        # 将最小点位置放到有序序列的末尾
        alist[i], alist[_min] = alist[_min], alist[i]
    return alist


if __name__ == "__main__":
    alist = [23,4,66,43,14,8,32]
    print(select(alist))

    