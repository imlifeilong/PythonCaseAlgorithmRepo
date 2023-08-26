# _*_ coding:utf-8 _*_
'''
缩小增量排序，首先取一个整数gap，将元素分为gap个子序列，所有距离为gap的元素放在一个子序列终，
然后在每个子序列终实现直接插入排序，然后缩小间隔gap，直到gap缩小到1
'''


def shell_sort(data):
    length = len(data)
    if length <= 1:
        return data

    # 初始步长
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            tmp = data[i]
            j = i

            # 子序列进行插入排序
            while j >= gap and tmp < data[j - gap]:
                data[j] = data[j - gap]
                j -= gap
            data[j] = tmp

        # 减小步长
        gap = gap // 2

    return data


if __name__ == "__main__":
    alist = [23, 4, 66, 43, 14, 8, 32, 22, 9]
    # alist = [23,]
    print(shell_sort(alist))
