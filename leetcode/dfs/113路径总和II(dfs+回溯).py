from leetcode.dfs import *


class Solution:
    def pathSum(self, root, targetSum):
        def dfs(root, sumval, tmp):
            # 上一个节点，没有子节点
            if not root:
                return
            # 记录当前节点的值
            tmp.append(root.val)

            # 没有子节点的时候，就是最末端的节点了，并且当前节点的值，等于目标值，记录这条路径
            if not root.left and not root.right and sumval == root.val:
                result.append(tmp[:])

            # 二叉树，分两种情况，第一个就是顺着左子树，继续往下找，直到某一条末端节点
            dfs(root.left, sumval - root.val, tmp)
            # 第二种情况就是顺着右子树，往下找，找的时候需要减掉当前节点的值
            dfs(root.right, sumval - root.val, tmp)
            # 回溯， 当前节点的所有子节点已经遍历完成
            tmp.pop()

        result = []

        dfs(root, targetSum, [])
        return result


if __name__ == '__main__':
    null = None
    root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]
    targetSum = 22
    # root = [1, 2, 3]
    # targetSum = 5
    # root = []
    # targetSum = 0
    tree = build_tree(root)

    print_tree_vertical(tree)

    s = Solution()
    res = s.pathSum(tree, targetSum)
    print(res)
