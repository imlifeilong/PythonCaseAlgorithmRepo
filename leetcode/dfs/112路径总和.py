from leetcode.dfs import *


class Solution:
    def hasPathSum(self, root, targetSum):
        def dfs(root, sumval):
            # 上一个节点，没有子节点
            if not root:
                return False

            # 没有子节点的时候，就是最末端的节点了，并且当前节点的值，等于目标值
            if not root.left and not root.right:
                return root.val == sumval

            # tmp.append(root.val)
            # 二叉树，分两种情况，第一个就是顺着左子树，继续往下找，直到某一条末端节点
            p1 = dfs(root.left, sumval - root.val)
            # 第二种情况就是顺着右子树，往下找，找的时候需要减掉当前节点的值
            p2 = dfs(root.right, sumval - root.val)
            # or 是其中有一条路符合条件，就退出
            return p1 or p2

        return dfs(root, targetSum)


if __name__ == '__main__':
    null = None
    root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]
    targetSum = 22
    # root = [1, 2, 3]
    # targetSum = 5
    # root = []
    # targetSum = 0
    tree = build_tree(root)

    print_tree_vertical(tree)

    s = Solution()
    res = s.hasPathSum(tree, targetSum)
    print(res)
