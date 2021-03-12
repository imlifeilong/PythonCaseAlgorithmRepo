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

class TreeDeep():
    
    def get_depth(self, tree):
        if not tree:
            return 0
        # 如果一颗树只有一个节点，深度为1
        # 如果树只有左子树，深度就是左子树的深度加1
        # 如果树只有右子树，深度就是右子树的深度加1
        # 如果既有右子树，又有左子树，深度时左右子树较大的那个加1
        left_depth = self.get_depth(tree.left)
        right_depth = self.get_depth(tree.right)

        depth = left_depth + 1 if left_depth > right_depth else right_depth + 1

        return depth

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
    tt = TreeDeep()
    print(tt.get_depth(ct))
