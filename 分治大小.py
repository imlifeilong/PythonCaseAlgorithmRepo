'''
给定一个数组arr，和一个数num，请把小于等于num的数放在数
组的左边，大于num的数放在数组的右边。
要求额外空间复杂度O(1)，时间复杂度O(N)
'''

def partion(data, num):
    left = 0
    less = -1

    while left < len(data):
        if data[left] <= num:
            # 如果小于等于则互换
            less += 1
            data[left], data[less] = data[less], data[left]
        # 否则挑下一个
        left += 1
    return data

def split_array(arr, num):
    """维持一个小于等于区域的index，
    如果一个数小于等于num，则和index位置交换
    如果一个数大于num，则直接跳下一个
    """
    i = 0
    for j in range(len(arr)):
        if arr[j] <= num:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    return arr

if __name__ == '__main__':
    a = [5, 3, 4, 2, 6, 1, 7, 8, 5, 9, 5, 5, 6, 5,]
    print(partion(a, 5))
    print(split_array(a, 5))