# _*_ coding:utf-8 _*_
'''
反复扫描序列，在扫描过程中顺次比较两个元素大小，如果逆序交换位置（如果某一趟冒泡排序中，没有发现一个逆序，则可以直接结束整个排序）
最坏的情况：序列完全逆序。时间复杂度是O(n2)，空间复杂度O(1)，是稳定的排序。
'''

def bsort(nlist):
    nlen = len(nlist)
    if nlen == 0:
        return
    if nlen == 1:
        return nlist
    #i表示趟数，最多进行n-1趟    
    for i in range(nlen-1,0,-1):
        for j in range(i):
            if nlist[j] > nlist[j+1]:
                nlist[j],nlist[j+1] = nlist[j+1],nlist[j]
    return nlist
    
def bsort1(nlist):
    nlen = len(nlist)
    if nlen == 0:
        return
    if nlen == 1:
        return nlist
    flag = 1
    while flag and nlen:
        #如果哪一趟没有交换（全部顺序），则表示全部排好序（剩下的都排好序不用交换）
        flag = 0
        for j in range(nlen-1):
            if nlist[j] > nlist[j+1]:
                nlist[j],nlist[j+1] = nlist[j+1],nlist[j]
                flag = 1
        print flag,nlen,nlist
        nlen -= 1
        
    return nlist

if __name__ == "__main__":
    import time
    nlist1 = [3,1,4,5,6,7,8]
    nlist = [3,6,7,3,4,5,1]
    #bsort(nlist)
    #print bsort1(nlist)
    print bsort1(nlist1)
    '''
    1 7 [3, 6, 3, 4, 5, 1, 7]
    1 6 [3, 3, 4, 5, 1, 6, 7]
    1 5 [3, 3, 4, 1, 5, 6, 7]
    1 4 [3, 3, 1, 4, 5, 6, 7]
    1 3 [3, 1, 3, 4, 5, 6, 7]
    1 2 [1, 3, 3, 4, 5, 6, 7]
    0 1 [1, 3, 3, 4, 5, 6, 7]
    [1, 3, 3, 4, 5, 6, 7]
    '''
   