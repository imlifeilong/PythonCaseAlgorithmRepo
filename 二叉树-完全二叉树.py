'''
搜索二叉树
    1、如果树为空，则直接返回错
　　2、如果树不为空：层序遍历二叉树
　　  2.1、如果一个结点左右孩子都不为空，则pop该节点，将其左右孩子入队列；
　　  2.1、如果遇到一个结点，左孩子为空，右孩子不为空，则该树一定不是完全二叉树；
　　  2.2、如果遇到一个结点，左孩子不为空，右孩子为空；或者左右孩子都为空；
        则该节点之后的队列中的结点都为叶子节点；
'''
from queue import Queue

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

class CompleteBinaryTree():
    def __init__(self):
        self._is_complete_binary = True
        self._is_leaf = False
        self.__q = Queue()

    def is_complete_binary(self, tree):
        self._start(tree)
        return self._is_complete_binary

    def _start(self, tree):
        if not tree:
            return

        self.__q.put(tree)
        while not self.__q.empty():
            tree = self.__q.get()
            left = tree.left
            right = tree.right
            # 如果一个节点，左孩子为空，右孩子不为空，不是完全二叉树
            # 如果一个节点，左孩子不为空，右孩子为空，或者左右孩子都为空，则该节点之后的节点，都为叶节点，
            # 否则不是完全二叉树
            if ((not left and right) or (self._is_leaf and (left or right))):
                self._is_complete_binary = False
                return
            # 左孩子不为空，入队 
            if left:
                self.__q.put(left)

            # 右孩子不为空，入队
            if right:
                self.__q.put(right)
            # 如果右孩子不为空，则该节点之后的节点都为叶
            else:
                self._is_leaf = True


if __name__ == '__main__':
    '''
          4
       /     \
      2       5  
     / \     / 
    1   3   7  

    Node('4',Node('2',Node('1'),Node('3')),Node('5',Node('7',Node('6'))))
    '''
    ct = Node('4',Node('2',Node('1'),Node('3')),Node('5',Node('7'), Node('8')))
    tt = CompleteBinaryTree()
    print(tt.is_complete_binary(ct))
