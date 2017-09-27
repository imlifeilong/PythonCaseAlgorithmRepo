# _*_ coding:utf-8 _*_
'''
²åÈëÅÅĞò
'''

def insert(alist):
    alen = len(alist)
    for i in range(1,alen):
        index = i
        item = alist[index]
        
        while index > 0 and alist[index-1] > item:
            alist[index] = alist[index-1]
            index -= 1
        alist[index] = item
    return alist


if __name__ == "__main__":
    alist = [23,4,66,43,14,8,32]
    print insert(alist)

    