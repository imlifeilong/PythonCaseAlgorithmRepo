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

最好情况是数据已经有序，O(N)
最坏情况是数据逆序，O(N2)
'''


def insert_sort(data):
    length = len(data)
    # 从1 开始，默认第一个是有序的
    for i in range(1, length):
        # i表示 当前要排序的元素的位置
        item = data[i]

        # index 左边是已经排好序的
        index = i
        # 在区间[0,index)上找到一个合适的位置把item插进去
        # 因为每次是index-1用来比较，所以index>0（而不是index>=0）
        while index > 0 and data[index - 1] > item:
            # 如果有序序列中的元素比item大，就往后挪一个位置
            data[index] = data[index - 1]
            # 为了更直观的看，此处应该有个置空的操作
            # data[index - 1] = None
            # print(data, item)
            # index向左移一位，再进行下次比较
            index -= 1

        # 找到一个位置，index左边小于或等于item
        data[index] = item
    return data


if __name__ == "__main__":
    data = [23, 4, 66, 43, 14, 8, 32]
    print(insert_sort(data))
