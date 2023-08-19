"""
找到一个子串，要求子串中最多只包含一个字母，，其余为数字
与 75 补种未成活的胡杨树 类似
"""


def process(s):
    n = len(s)
    left = 0
    right = 0
    count = 0
    result = 0
    only_alpha = True  # 滑动窗口中是否全为字母
    while right < n:
        # 如果right所指是字母，则记录字母个数
        if s[right].isalpha():
            count += 1
        # 当窗口内的字母个数大于1时，必须移动left来保证窗口的字母个数
        while count > 1:
            # 当left遇见字母时，此时统计字母的个数需要-1，再移动left
            if s[left].isalpha():
                count -= 1
            left += 1

        # 判断窗口中是否包含数字
        for c in s[left:right + 1]:
            if c.isdigit():
                only_alpha = False
                break
        # 当窗口中包含字母和数字时，记录窗口长度，并且与之前记录的比较，取较大的一个
        if not only_alpha:
            result = max(result, right - left + 1)
        right += 1

    if result:
        print(result)
    else:
        print(-1)


def process1(s):
    # 归一化数据
    nums = []
    for c in s:
        if c.isdigit():
            nums.append(1)
        else:
            nums.append(0)
    print(nums)
    # 此时问题转换成，求一个最长的连续子数组，该子数组包含0的个数不超过1，并且要包含0 和 1

    n = len(nums)
    left = 0
    rigth = 0
    count = 0
    result = 0
    only_zero = True # 窗口只包含0
    while rigth < n:
        # 统计left和right种的0的个数
        if nums[rigth] == 0:
            count += 1

        # 如果0的个数大于1，则需要移动left，控制0的个数保持在1个
        while count > 1:
            # 如果left指向的值为0，则记录0的个数-1
            if nums[left] == 0:
                count -= 1
            left += 1

        # 判断窗口中是否只包含0
        for i in nums[left:rigth+1]:
            if i == 1:
                only_zero = False
                break

        if not only_zero:
            # 记录left和right的长度，并且与之前的比较，取长度较长的
            result = max(result, rigth - left + 1)

        rigth += 1
    print(result)
    return result


def main(s):
    indexs = []
    indexs.append(-1)  # 添加左边界
    # 找到所有字母的索引
    for i, c in enumerate(s):
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            indexs.append(i)
    indexs.append(len(s))  # 添加右边界，处理只有1个字母，或者indexs中间隔小于2的情况 a123b
    # 然后根据字母索引之间的间隔，得知连续数字的长度
    maxval = -1
    for j in range(len(indexs) - 2):
        tmp = indexs[j + 2] - indexs[j]

        if tmp > 2:  # 间隔大于2的情况中间可以插一个数字，
            maxval = max(tmp - 1, maxval)  # 更新最大值
    print(maxval)


s = '12ab4C124ACb'
s = '1a123b123fd'
s = 'a'
# s = 'aa5'
# s = 'abcdef'
# main(s)
process(s)
process1(s)
