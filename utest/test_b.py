# class Solution:
#     def letterCombinations(self, digits):
#         mapping = {
#             '2': ['a', 'b', 'c'],
#             '3': ['d', 'e', 'f'],
#             '4': ['g', 'h', 'i'],
#             '5': ['j', 'k', 'l'],
#             '6': ['m', 'n', 'o'],
#             '7': ['p', 'q', 'r', 's'],
#             '8': ['t', 'u', 'v'],
#             '9': ['w', 'x', 'y', 'z']
#         }
#
#         # def dfs(index):
#         #     for i in range(index, len(digits)):
#         #         tmps = mapping[digits[i]]
#         #         for j in range(len(tmps)):
#         #             print(tmps[j])
#         #
#         # dfs(0)
#
#         def dfs(index, tmp):
#             if index == len(digits):
#                 print(tmp)
#                 return
#                 # for i in range(index, len(digits)):
#             # print(digits[i])
#             string = mapping[digits[index]]
#             for i in range(len(string)):
#                 tmp.append(string[i])
#                 # print(string)
#                 dfs(index + 1, tmp)
#                 tmp.pop()
#
#         dfs(0, [])
#
#
# if __name__ == '__main__':
#     digits = "234"
#     s = Solution()
#     s.letterCombinations(digits)
# class Solution:
#     def combine(self, n, k):
#         def dfs(index, tmp):
#             # index是递归深度
#             if len(tmp) == k:
#                 print(tmp)
#                 return
#
#             for i in range(index, n + 1):
#                 tmp.append(i)
#                 dfs(i+1, tmp)
#                 tmp.pop()
#
#         dfs(1, [])
#
#
# if __name__ == '__main__':
#     n = 4
#     k = 2
#     s = Solution()
#     s.combine(n, k)

# class Solution:
#     def permute(self, nums):
#
#         def dfs(index, tmp):
#             if index == len(nums):
#                 print(tmp)
#                 return
#
#             for i in range(len(nums)):
#                 if nums[i] not in tmp:
#                     tmp.append(nums[i])
#                     dfs(index + 1, tmp)
#                     tmp.pop()
#
#         dfs(0, [])
#
#
# if __name__ == '__main__':
#     nums = [1, 2, 3]
#     s = Solution()
#     s.permute(nums)

class Solution:
    def combinationSum(self, candidates, target):
        # def dfs(index, tmp, t):
        #     if t < 0:
        #         return
        #     if t == 0:
        #         print(tmp)
        #         return
        #
        #     for i in range(len(candidates)):
        #         # if candidates[i] not in tmp:
        #             tmp.append(candidates[i])
        #             dfs(index + 1, tmp, t - candidates[i])
        #             tmp.pop()

        def process(index, tmp, t):
            if t < 0 or index >= len(candidates):
                return
            if t == 0:
                print(tmp)
                return

            if t - candidates[index] < 0:
                return process(index + 1, tmp, t)
            tmp.append(candidates[index])
            p1 = process(index, tmp, t - candidates[index])
            tmp.pop()
            p2 = process(index + 1, tmp, t)

        # process(0, [], target)

        def dfs1(index, tmp, t):
            if t == 0:
                print(tmp)
                return

            for i in range(index, len(candidates)):
                if t - candidates[i] >= 0:
                    tmp.append(candidates[i])
                    dfs1(i, tmp, t - candidates[i])
                    tmp.pop()

        dfs1(0, [], target)


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    candidates = [2, 3, 5]
    target = 8
    # candidates = [2]
    # target =1
    s = Solution()
    s.combinationSum(candidates, target)
