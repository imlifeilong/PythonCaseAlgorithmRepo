"""
双指针 滑动窗口
本质上来说，滑窗是双指针，一根指针指向左端点，一根指针指向右端点。
右指针移动可以表示扩张窗口，左指针移动表示缩小窗口。
如果当前元素满足题目要求时，可以挪动右指针尝试更优解，并且更新需要记录的变量（元素，元素个数++等）
如果当前窗口内的元素不满足条件，可以挪动左指针尝试调整，并且更新需要记录的变量（元素，元素个数--等）
通过以上步骤窗口就开始“滑动”起来，在滑动过程中，要记得及时更新答案。一般为求最大或最小。


子串：连续的
子序列：可以不连续

本题与1004. 最大连续1的个数 III 相同
题意转换：
理解为有树的位置值为1，没树的位置值为0
即把K个0变成1后，求仅包含1的最长的子串的长度
再理解为 找出一个最长的子串，要求该子串中最多包含K个0

思路：
使用两个指针 left指向滑动窗口左边界，right指向右边界
每次先移动right 当right指向的值为0时，说明窗口内增加了一个0
每次移动right后 需要判断窗口内0的个数，是否超过K，
如果超过了，left必须移动，直到窗口内0的个数小于等于K
最后记录并且返回滑动窗口的最大长度
"""
# 扩展
# 485. 最大连续 1 的个数
# 487. 最大连续1的个数 II
# 1004. 最大连续1的个数 III 解法




# 1004. 最大连续1的个数 III 解法
def process(data, k):
    # 求data中找出一个最长的子串，该子串中最多包含k个0
    n = len(data)
    result = 0  # 结果
    left = 0
    right = 0
    count = 0  # 记录子串中0的个数
    while right < n:
        # 移动右指针，统计窗口内0的个数
        if data[right] == 0:
            count += 1
        # print(data[left:right + 1])
        # 每移动一次right，统计一次，就需要判断窗口内0的个数
        # 如果 0的个数已经超过k，必须移动left，来控制0的个数小于等于k
        while count > k:
            # left移动的过程中遇见0，则0的个数-1，继续移动left，直到0的个数小于等于K时停止
            # print(data[left:right + 1])
            if data[left] == 0:
                count -= 1
            left += 1
        # 记录满足条件的子串的长度，并且和之前的满足条件的子串进行对比，取较长的长度
        result = max(result, right - left + 1)

        right += 1
    print(result)
    return result


def main(n, data, k):
    mapping = []
    # 将数据归一化 有树的位置值为1 没树的位置值为0
    for i in range(1, n + 1):
        if i in data:
            mapping.append(0)
        else:
            mapping.append(1)
    print(mapping)
    res = process(mapping, k)
    print(res)


n = 10
m = 3
s = '2 4 7'.split()
k = 1
data = list(map(int, s))
main(n, data, k)
