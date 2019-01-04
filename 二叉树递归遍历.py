'''
先序遍历DLR：根节点->左子树->右子树
中序遍历LDR：左子树->根节点->右子树
后续遍历LRD：左子树->右子树->根节点
层次遍历：用一维数组存储二叉树时,总是以层次遍历的顺序存储结点。层次遍历应该借助队列。

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


class TreeTraverse():
    def _pre(self, tree):
        if not tree:
            return
        print(tree.root)
        self._pre(tree.left)
        self._pre(tree.right)

    def _mid(self, tree):
        if not tree:
            return        
        self._mid(tree.left)
        print(tree.root)
        self._mid(tree.right)

    def _aft(self, tree):
        if not tree:
            return        
        self._aft(tree.left)
        self._aft(tree.right)
        print(tree.root)

if __name__ == '__main__':
    '''
         A
       /   \
      B     C
     / \     \
    D   E     F
             /
            G
    递归过程 ABDDDBEEEBACCFGGGFFCA
    前序 各元素第一次出现的时候打印 ABDECFG
    中序 各元素第二次出现的时候打印 DBEACGF
    后序 各元素第三次出现的时候打印 DEBGFCA
    '''
    ct = Node('A',Node('B',Node('D'),Node('E')),Node('C',right=Node('F',Node('G'))))
    print('前序--->')
    tt = TreeTraverse()
    tt._pre(ct)
    print('中序--->')
    tt._mid(ct)
    print('后序--->')
    tt._aft(ct)

