class Solution:
    def threeSum(self, nums):
        def dfs(index, tmp):
            if len(tmp) == 3:
                sumval = 0
                for j in tmp:
                    sumval += nums[j]
                print(sumval)
                if sumval == 0:
                    result.append([nums[x] for x in tmp][:])
                return

            for i in range(index, len(nums)):
                print(i)
                tmp.append(i)
                dfs(i + 1, tmp)
                tmp.pop()

        result = []
        dfs(0, [])
        print(result)


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0, 1, 1]
    # nums = [0, 0, 0]
    s = Solution()
    s.threeSum(nums)
