"""
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

思路

快慢指针 left 指向0 right 指向1
比较left 和 right 指向的值是否相等，如果相等，right向前移动
如果不相等，left移动一位，然后将right的值赋到left上

相当于 left 用来记录，right用来扫描，当right扫到新值（新值就是和当前left所指的值比较）时，left就记录下，
当right没有扫的新值时， 就一直扫下去直到遇见新值或结束

上面所有的前提是 所给的是 升序排列 的数组

"""


class Solution:
    def removeDuplicates(self, nums):
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                # right扫到不同的值时，left记录一下
                left += 1
                nums[left] = nums[right]
                # right继续扫描后面的值
                right += 1
        # 最后返回left停止位置的长度
        return left + 1, nums


if __name__ == '__main__':
    nums = [1, 1, 2]
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    s = Solution()
    res = s.removeDuplicates(nums)
    print(res)
