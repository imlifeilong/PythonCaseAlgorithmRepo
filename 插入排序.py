# _*_ coding:utf-8 _*_
'''
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

    