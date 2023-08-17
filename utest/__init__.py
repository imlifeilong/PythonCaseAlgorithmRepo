# # import re
# #
# #
# # def solve_method(capacities):
# #     capacities.sort(key=convert)
# #     for c in capacities:
# #         print(c)
# #
# #
# # def convert(capacity):
# #     size = 0
# #     upper = capacity.upper()
# #     split = re.split("[A-Z]", upper)
# #     unit_pos = 0
# #     for s in split:
# #         if s == '':
# #             continue
# #         num = int(s)
# #         unit = upper[unit_pos + len(s)]
# #         if unit == 'M':
# #             size += num
# #         elif unit == 'G':
# #             size += num * 1024
# #         elif unit == 'T':
# #             size += num * 1024 * 1024
# #         unit_pos += len(s) + 1
# #     return size
# #
# #
# # if __name__ == '__main__':
# #     n = int(input().strip())
# #     capacities = [input().strip() for _ in range(n)]
# #     solve_method(capacities)
#
#
# def solve_method(n):
#     step1 = 1
#     step2 = 1
#     step3 = 2
#     step4 = 1 if n == 1 or n == 2 else 2
#     for i in range(4, n + 1):
#         step4 = step3 + step1
#         step1 = step2
#         step2 = step3
#         step3 = step4
#     print(step4)
#
#
# # # n = int(input().strip())
# n = 50
# solve_method(n)
#
# def count_ways_to_climb_stairs(n):
#     if n <= 1:
#         return 1
#
#     ways = [0] * (n + 1)
#     ways[0] = 0
#     ways[1] = 1
#     ways[2] = 1
#     ways[3] = 2
#
#     for i in range(4, n + 1):
#         ways[i] = ways[i - 1] + ways[i - 3]
#
#     return ways[n]
# res = count_ways_to_climb_stairs(50)
# print(res)


# def solve_method(line):
#     numStrArray = line.split(",")
#     map = {}
#     for m in range(len(numStrArray)):
#         num = int(numStrArray[m])
#         if m < 3:
#             if m == 0:
#                 map[m + 1] = max(0, num)
#             else:
#                 map[m + 1] = max(0, map[m] + num)
#         else:
#             map[m + 1] = max(map[m] + num, map[m - 2])
#     print(map[numStrArray.__len__()])
#
#
# line = '1,-5,-6,4,3,6,-20'
# solve_method(line)

# def is_prime(num):
#
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# def is_product_of_primes(num):
#     for i in range(2, num):
#         if is_prime(i) and num % i == 0 and is_prime(num // i):
#             return i, num // i
#     return -1, -1
#
#
# number = 33
# res = is_product_of_primes(number)
# print(res)

# def getResult(k, s):
#     stack = []
#     res = []
#
#     for c in s:
#         if c == '_' and (len(stack) == 0 or stack[0] != '"'):
#             res.append("".join(stack))
#             stack = []
#         elif c == '"' and len(stack) != 0:
#             stack.append(c)
#             res.append("".join(stack))
#             stack = []
#         else:
#             stack.append(c)
#
#     if len(stack) > 0:
#         res.append("".join(stack))
#
#     ans = list(filter(lambda x: x != "", res))
#
#     if k > len(ans) - 1:
#         return "ERROR"
#
#     ans[k] = "******"
#
#     return "_".join(ans)
#
#
# k = 1
# s = 'password__a12345678_timeout_100'
#
# k = 2
# s = 'aaa_password_"a12_45678"_timeout__100_""_'
# # 算法调用
# print(getResult(k, s))

# num_of_dice = 10
# num_of_sides = 3
# dice_strings = '2 4 7'.split()
# k = 1
# # num_of_dice, num_of_sides = map(int, input().split())
# # dice_strings = input().split()
#
# rolls = [0] * num_of_dice
# # k = int(input())
#
# for i in range(num_of_sides):
#     rolls[int(dice_strings[i]) - 1] = 1
#
# left = 0
# right = 0
# count = 0
#
# result = 0
# while right < num_of_dice:
#     while right < num_of_dice and count <= k:
#         if rolls[right] == 1:
#             count += 1
#         right += 1
#
#         if count <= k:
#             result = max(right - left, result)
#
#     while left <= right and count > k:
#         if rolls[left] == 1:
#             count -= 1
#         left += 1
#
# print(result)

import sys


#
# def find_indexes(input_string):
#     if len(input_string) < 5 or len(input_string) > 30:
#         return [0, 0]
#
#     char_values = [ord(char) for char in input_string]
#     total_sum = sum(char_values)
#
#     begin = (total_sum - 122 * 2) // 3
#     end = (total_sum - 97 * 2) // 3
#
#     if begin < 0 or end < 0:
#         return [0, 0]
#
#     left_sum = 0
#     left_index = 0
#     result = [0, 0]
#
#     # 从左侧找到第一个满足条件的索引位置
#     while left_sum < end + 1:
#         left_sum += char_values[left_index]
#         left_index += 1
#         if left_sum >= begin:
#             right_sum = 0
#             right_index = len(char_values) - 1
#
#             # 从右侧找到第一个满足条件的索引位置
#             while right_sum < end:
#                 right_sum += char_values[right_index]
#                 right_index -= 1
#
#                 # 使得字符串被这两个节点分成三个部分，每个部分的 ASCII 码的值之和都相等
#                 if ( right_sum == left_sum == sum(char_values[left_index + 1 : right_index]) and left_index <= right_index ):
#                     result = [left_index, right_index]
#                     break
#             else:
#                 continue
#             break
#
#     return result
#
#
# if __name__ == "__main__":
#     input_string = s = 'aabaacaa'
#     indexes = find_indexes(input_string)
#     print(*indexes, sep=",")


# 输入获取
# n = 6
#
# data = '''b a
# c a
# d c
# e c
# f d
# z f
# x e'''.split('\n')
#
# tree = {}
# for _ in range(n):
#     ch, fa = data[_].split()
#     tree.setdefault(fa, set())  # 每个节点建一个默认的set集合。
#     tree[fa].add(ch)  # 然后把他添加到set里去。要去重啊
# target = 'c'
#
#
# # 算法入口
# def result():
#     if tree.get(target) is None:
#         print("")  # 没找到
#         return
#     # 找到了，就把他的直接的子节点添加到队列里。广搜
#     queue = list(tree[target])
#     ans = []
#     # 队列不为空就一直循环。广搜的固定套路。
#     while len(queue) > 0:
#         # 弹出来
#         node = queue.pop(0)
#         # 加入结果中。
#         ans.append(node)
#         # 处理字节点
#         if tree.get(node) is not None:
#             queue.extend(list(tree[node]))  # 这里注意是extend，不是append()
#     # 循环完了，结果也找完了,排序一波
#     ans.sort()
#     # 打印结果
#     for v in ans:
#         print(v)


# result()

# while True:
#     try:
# n, m = 6, 7
# ints = list(map(int, '2 12 6 3 5 5'.split()))
#
# pre_sum = 0
# is_true = False
# remainders = set()
# for i in range(n):
#     pre_sum = (pre_sum + ints[i]) % m
#     if pre_sum in remainders:
#         is_true = True
#         break
#     remainders.add(pre_sum)
#
# print(1 if is_true else 0)
#
#     # except EOFError:
#     #     break

# class Solution:
#     def maxAreaOfIsland(self, grid):
#         m, n = len(grid), len(grid[0])
#
#         def dfs(i, j):
#             if 0 <= i < m and 0 <= j < n and grid[i][j]:
#                 tmp = grid[i][j]
#                 grid[i][j] = 0
#                 return tmp + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
#             return 0
#
#         res = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]:
#                     rr = dfs(i, j)
#                     res = max(res, dfs(i, j))
#         return res
#
#
# data = [[2, 2, 2, 2, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 1]]
# s = Solution()
# res = s.maxAreaOfIsland(data)
# print(res)


# def custom_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             # 如果第二个字段相同，则比较第一个字段
#             if arr[j][1] == arr[j+1][1]:
#                 if arr[j][0] > arr[j+1][0]:
#                     arr[j], arr[j+1] = arr[j+1], arr[j]
#             # 如果第二个字段不同，则比较第二个字段
#             elif arr[j][1] > arr[j+1][1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
# data = [('John', 25), ('Jane', 30), ('Tom', 22), ('Alice', 30)]
#
# custom_sort(data)
#
# for item in data:
#     print(item)


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert_complete_tree(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        root.left = insert_complete_tree(arr, root.left, 2 * i + 1, n)
        root.right = insert_complete_tree(arr, root.right, 2 * i + 2, n)
    return root

arr = ['1', '2', '3', '4', '5', '6', '7']
root = insert_complete_tree(arr, None, 0, len(arr))

print(root)