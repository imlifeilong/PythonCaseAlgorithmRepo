from typing import List

'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


全排列是指对一组元素进行排列，以得到所有可能的排列方式。
每个元素在排列中都出现一次，但它们的顺序可能不同

第一层选择1 第二层选择2或3 因为每层的for循环 第三层选择剩余的元素
第一层选择2 第二层选择1或3 第三层选择剩余的元素
第一层选择3 第二层选择1或2 第三层选择剩余的元素

(1)23   (12)3   (123)
        (13)2   (132)

1(2)3   (21)3   (213)
        (23)1   (231)

12(3)   (31)2   (312)
        (32)1   (321)

'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)
        self.nums = nums
        # 用来标记原序列，对应的位置上的元素是否被入栈过
        self.position = [False] * self.length
        self.result = []

        self.backtrack(0, [])

        print(self.result)
        return self.result

    def backtrack(self, h, tmp):
        # h 递归就是纵向的遍历，h则是表示要遍历的层数，即递归的深度
        # tmp 存放过程元素的栈，因为栈是先进后出的

        # 退出条件就是 递归的深度达到了 原序列的长度
        # 如果不限制就一直遍历下去，可能元素个数就会是 4个 5个 100个。。。
        if h == self.length:
            # 使用[:] 为什么要拷贝 因为append操作是result引用了tmp，也就是说虽然已经将tmp追加到result，
            # 但是tmp改变时，result中也会跟着变，因为result只是存了指向tmp的指针，
            # 如果使用浅拷贝的话，就相当于重新开辟了一块地址，将tmp中值的引入新地址中

            self.result.append(tmp[:])
            return

        # for循环就是在每一层进行横向的遍历
        # 问题，当上一层是从0号元素开始遍历，到了第二层也是从0号元素开始遍历，此时就会出行重复的元素，就必须去重
        for i in range(self.length):
            # 采用标记位置法进行去重，就是每入栈一个元素时，记录下此元素的索引，
            # 当下一层再从0号开始遍历的时候，只需要判断0号索引是否已经标记过即可
            # 如果标记了，就说明此元素已经入过栈了，跳过
            # 标记位置的索引可以是一个列表或者数组，长度和原序列长度一样，是一个全局的遍历
            if self.position[i]:
                continue

            # 将一个元素加到栈顶，然后去下一层试探，直到到达设定的深度后返回，否则就返回None
            tmp.append(nums[i])
            # 入栈后，标记此元素位置
            self.position[i] = True
            # 去下一层时 深度就要加1
            self.backtrack(h + 1, tmp)

            # 试探完成后，利用栈的属性，然后弹出最后一位元素，再加入同层下一位元素
            tmp.pop()
            # 完成后还原此元素位置的标记
            self.position[i] = False


if __name__ == '__main__':
    nums = [1, 2, 3]
    nums = ['a', 'b', 'ab']
    nums.sort()
    s = Solution()
    res = s.permute(nums)
    for row in res:
        print(''.join(row))