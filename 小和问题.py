'''
小和问题
    在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和。求一个数组的小和。
    例子：
    [1,3,4,2,5]
    1左边比1小的数，没有；
    3左边比3小的数，1；
    4左边比4小的数，1、3；
    2左边比2小的数，1；
    5左边比5小的数，1、3、4、2；
    所以小和为1+1+3+1+1+3+4+2=16
逆序对问题
    在一个数组中，左边的数如果比右边的数大，则折两个数构成一个逆序对，请打印所有逆序对
'''

n, m = 0, 0
def merge_sort(data):
    #不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
    if len(data) == 1:
        return data

    #取拆分的中间位置
    mid = len(data) // 2
    #拆分过后左右两侧子串
    left = data[:mid]
    right = data[mid:]

    #对拆分过后的左右再拆分 一直到只有一个元素为止
    #最后一次递归时候ll和lr都会接到一个元素的列表
    # 最后一次递归之前的ll和rl会接收到排好序的子序列
    ll = merge_sort(left)
    rl =merge_sort(right)

    # 我们对返回的两个拆分结果进行排序后合并再返回正确顺序的子列表
    # 这里我们调用拎一个函数帮助我们按顺序合并ll和lr
    return merge(ll, rl)

#这里接收两个列表
def merge(left, right):
    # 从两个有顺序的列表里边依次取数据比较后放入result
    # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result
    result = []
    # 将n置为全局变量，与每部分的小和求和
    global n, m

    while len(left) > 0 and len(right) > 0:

        # 如果左边第一位数比右边第一位数数小，左一就小于右边所有数，左一就是右边所有数的小和，否则不是
        if left[0] < right[0]:
            # 求和
            n += left[0] * len(right)
        # 如果右边第一个数小于左边第一位数，右一就和左边所有的数组成逆序对，否则不是
        elif left[0] > right[0]:
            m += len(left)
        
        else:
            n += 0; m += 0

        #为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    #while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
    if left:
        result += left
    if right:
        result += right
    return result

if __name__ == '__main__':
    li = [23,4,66,23,4,66,43,14,8,32,43,14,8]
    li = [1,3,4,2,5]
    li2 = merge_sort(li)
    print(n, m)
    # print(li2)