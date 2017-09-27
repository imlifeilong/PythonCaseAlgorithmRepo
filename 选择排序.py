# _*_ coding:utf-8 _*_
'''
选择排序，每次从后面的序列中选取最小的
'''

def select(alist):
    alen = len(alist)
    for i in range(alen):
        min = i
        for j in range(i+1,alen):
            if alist[j] < alist[min]:
                alist[j],alist[min] = alist[min],alist[j]
    return alist


if __name__ == "__main__":
    alist = [23,4,66,43,14,8,32]
    print select(alist)

    