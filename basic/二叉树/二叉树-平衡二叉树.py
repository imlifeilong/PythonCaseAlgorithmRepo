'''
平衡二叉树
    0、高度是☞从叶节点（高度为1）向上逐层累加，深度是指从根节点（深度为1），向下逐层累加
    1、每个节点的左子树高度和右子树高度相差不大于1
    2、空树也是平衡二叉树
'''

class Node():
    def __init__(self, root=None, left=None, right=None):
        self.__root = root
        self.__left = left
        self.__right = right

    @property
    def root(self):
        return self.__root

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

class BalanceTree():
    def __init__(self):
        self._is_balabce = True

    def is_balabce(self, tree):
        self.tree_level(tree)
        return self._is_balabce

    def tree_level(self, tree):
        # 空树是平衡的
        if not tree:
            return 0

        # 分别递归遍历左右子树，返回各自高度
        left_level = self.tree_level(tree.left)
        right_level = self.tree_level(tree.right)

        # 如果左右子树高度差大于1，则不是平衡树
        if abs(left_level - right_level) > 1:
            self._is_balabce = False
        
        # 左右子树较大的高度，再加1就是当前节点的高度
        current_node_level = max(left_level, right_level) + 1
        
        return current_node_level

if __name__ == '__main__':
    '''
         A
       /   \
      B     C   高度3，右子树高度2，左为0 ，相差2，不平衡，所以整棵树不平衡
     / \     \
    D   E     F 高度2，左右子树高度不超过1，平衡
             /
            G   高度1，左右平衡

    Node('A',Node('B',Node('D'),Node('E')),Node('C',right=Node('F',Node('G'))))
    '''
    # ct = Node('A',Node('B',Node('D'),Node('E')),Node('C',right=Node('F')))
    ct = Node('A',Node('B',Node('D'),Node('E')),Node('C',right=Node('F',Node('G'))))
    tt = BalanceTree()
    print(tt.is_balabce(ct))
