# _*_ coding:utf-8 _*_
'''
选择排序，每次从原始的序列中选取最小的元素，放到有序列的末尾
比较次数n(n-1)/2
时间复杂度O(n2)
'''

def select(alist):
    alen = len(alist)
    for i in range(alen):
        _min = i #选择最小点的位置
        for j in range(i+1,alen):
            # 取剩余序列的第一个元素，与最小点比较，如果小于最小点，则选择该点位置为最小点
            if alist[j] < alist[_min]:
                _min = j
        # 将最小点位置放到有序序列的末尾
        alist[i], alist[_min] = alist[_min], alist[i]
    return alist


if __name__ == "__main__":
    alist = [23,4,66,43,14,8,32]
    print(select(alist))

    