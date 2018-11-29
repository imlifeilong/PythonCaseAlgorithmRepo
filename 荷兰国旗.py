'''
给定一个数组arr，和一个数num，请把小于num的数放在数组的
左边，等于num的数放在数组的中间，大于num的数放在数组的
右边。
要求额外空间复杂度O(1)，时间复杂度O(N)
'''

def netherlands(data, num):
    length = len(data)
    less = -1 #小于区域
    more = length #大于区域
    index = 0
    # [小于区域，等于区域， 待定区域， 大于区域]
    # 
    while index < more:
        # 如果当前数据小于 值，小于区域向下一位，并和当前数交换，当前位置向下一位
        if data[index] < num:
            less += 1
            data[index], data[less] = data[less], data[index]
            index += 1
        # 如果当前数大于 值，大于区域向前一位，并和当前值交换
        elif data[index] > num:
            more -= 1
            data[index], data[more] = data[more], data[index]
        # 如果等于 值，直接跳下一位
        else:
            index += 1
    print(less+1, more-1)
    return data


if __name__ == '__main__':
    a = [5, 3, 4, 2, 6, 1, 7, 8, 5, 9, 5, 5, 6, 5]
    b = [0,2,1,2,2,1,1,0,2,1,0]
    print(netherlands(a, 5))

