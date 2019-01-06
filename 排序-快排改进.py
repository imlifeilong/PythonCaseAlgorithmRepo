import random

def partaion(data, left, right):
    less = left - 1 #小区域是从列表初始位置前一位开始
    more = right   #大区域是从列表末尾位置开始，因为末尾位置的数是分隔值，可以视为末尾位置无值

    # 遍历整个待定区域  left < 待定区域 < more
    while left < more:
        if data[left] < data[right]:
            less += 1
            data[left], data[less] = data[less], data[left]
            left += 1
        elif data[left] > data[right]:
            more -= 1
            data[left], data[more] = data[more], data[left]
        else:
            left += 1
    # 整个列表分隔完后，此时left已经来到大区域的第一个位置（等于区 < left 大于区域），和末尾值交换（末尾值是分隔值）
    data[more], data[right] = data[right], data[more]
    # 此时返回小于区域的末尾边界 和大于区域的开始边界
    return less, more+1

def sort(data, left, right):
    # 如果列表为空或者，所需区域不存在，则返回
    if not data or left > right:
        return
    # 随机选择一位作为分界点，将整个排序过程变成时间复杂度的期望值
    index = random.randint(left, right)
    # 交换到末尾，节省一个变量
    data[right], data[index] = data[right], data[index]
    
    # 将列表的数按分隔值分开
    mid = partaion(data, left, right)
    # 递归排序分隔值左边的列表
    sort(data, left, mid[0])
    # 递归排序分隔值右边的列表
    sort(data, mid[1], right)
    
    return data


if __name__ == '__main__':
    a = [5, 3, 4, 2, 6, 1, 1, 7, 8, 5, 9, 5, 5, 6, 5]
    a = [-1, -1, 0, -3, -99]
    print(sort(a, 0, len(a)-1))