# _*_ coding:utf-8 _*_
'''
选择排序过程：
    1、首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    2、然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    3、以此类推，直到所有元素均排序完毕。
比较次数n(n-1)/2
时间复杂度O(n2)
'''


def select_sort(data):
    length = len(data)

    for i in range(length):
        # 选择第一个元素为记为最小值，min_index左边是排行顺序的
        min_index = i

        # 扫描剩下的元素，选取比min_index所指的值小的
        for j in range(i + 1, length):
            # 迭代找到最小的值的索引，赋给min_index
            if data[j] < data[min_index]:
                min_index = j

        # 找到最小值后，排到顺序的后面
        data[i], data[min_index] = data[min_index], data[i]

    return data


if __name__ == "__main__":
    data = [5, 3, 2, 6, 1, 7, 8, 4, 5, 1, 9, 5, 5, 6]
    # data = [5, 3, 2, 6, 1]
    res = select_sort(data)
    print(res)
