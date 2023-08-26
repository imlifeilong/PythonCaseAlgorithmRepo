# _*_ coding:utf-8 _*_
'''
反复扫描序列，在扫描过程中顺次比较两个元素大小，
如果逆序交换位置（如果某一趟冒泡排序中，没有发现一个逆序，则可以直接结束整个排序）
最好情况：序列都是正序的，时间复杂度O(n)，比较n-1次 交换0次
最坏的情况：序列完全逆序。时间复杂度是O(n2)，空间复杂度O(1)
平均O(n2)
'''


def bubble_sort(data):
    length = len(data)
    # i表示趟数，每一趟将当前区间[0,i)的最大值放到i位置
    for i in range(length, -1, -1):
        # 因为要比较j+1，为了当值越界，所以是i-1
        # [0,1,2 ... i-1]

        # 优化 判断剩余的元素 是否已经排好序
        # is_sorted = True

        for j in range(i - 1):
            # 每次判断相邻两个元素是否逆序，如果逆序就调整
            # 此处可以优化，当所有相邻的元素都顺序的时候，就不用再扫描剩下的区间
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                # 优化 如果交换操作，就需要排序
                # is_sorted = False
        # 优化 如果剩余的元素已经是顺序的了，就无需再进行扫描
        # if is_sorted:
        #     break
    return data


if __name__ == "__main__":
    data = [5, 3, 2, 6, 1, 7, 8, 4, 5, 1, 9, 5, 5, 6]
    # data = [1, 1, 2, 3, 4, 7, 8, 4, 5, 1, 9, 5, 5, 6]
    res = bubble_sort(data)
    print(res)
