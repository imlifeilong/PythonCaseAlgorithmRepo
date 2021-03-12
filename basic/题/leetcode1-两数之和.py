from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in mapping:
                return i, mapping[j]
            mapping[j] = i

if __name__ == '__main__':
    st = '[][]'
    s = Solution()
    print(s.twoSum([3,2,4], 6))