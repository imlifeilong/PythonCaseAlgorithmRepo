# _*_ coding:utf-8 _*_
'''
二分法查找两个要求：1、顺序存储结构，2、序列已经排好序
思想：将关键字和序列中间位置的元素比较，如果相等查找结束，
否则将序列分割为两个子列，如果关键字大于中间元素，在后面序列查找，
否则在前面序列查找，重复之前的过程直到查到，或者关键字不在子列中
最多查找次数log2n + 1
平均查找长度 比较次数/序列长度
'''

def bsearch(alist,item):
    low = 0
    high = len(alist) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if alist[mid] > item:
            high = mid - 1
        elif alist[mid] < item:
            low = mid + 1
        else:
            return mid
    return

    
if __name__ == "__main__":
    alist = [2,5,12,15,26,35,66]
    print(bsearch(alist,3))