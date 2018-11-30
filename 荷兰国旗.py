'''
给定一个数组arr，和一个数num，请把小于num的数放在数组的
左边，等于num的数放在数组的中间，大于num的数放在数组的
右边。
要求额外空间复杂度O(1)，时间复杂度O(N)
'''

def netherlands(data, left, right, num):
    less = -1 #小于区域，从列表初始位置前一位开始
    more = right #大于区域， 从列表末尾位置后一位开始
    # [小于区域，等于区域， 待定区域， 大于区域]
    
    # 只对待定区域遍历left左边是小于，等于， more右边是大于，之间是待定区域
    while left < more:
        # 如果当前数据小于 值，小于区域向下一位，并和当前数交换，当前位置向下一位
        if data[left] < num:
            less += 1
            data[left], data[less] = data[less], data[left]
            left += 1
        # 如果当前数大于 值，大于区域向前一位，并和当前值交换
        elif data[left] > num:
            more -= 1
            data[left], data[more] = data[more], data[left]
        # 如果等于 值，直接跳下一位
        else:
            left += 1
    print(less, more)
    return data


if __name__ == '__main__':
    a = [5, 3, 4, 2, 6, 1, 7, 8, 5, 9, 5, 5, 6, 5]
    b = [0,2,1,2,2,1,1,0,2,1,0]
    print(netherlands(b, 0, len(b), 1))

