'''
层次遍历：用一维数组存储二叉树时,总是以层次遍历的顺序存储结点。层次遍历应该借助队列。

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


class TreeTraverse():
    def __init__(self):
        self.__q = Queue()


    def traverse(self, tree):
        if not tree:
            return

        self.__q.put(tree)
        while not self.__q.empty():
            # 如果队列不为空，出队一个元素，然后打印
            tree = self.__q.get()
            print(tree.root)
            # 如果该元素有左孩子，左孩子入队
            if tree.left:
                self.__q.put(tree.left)
            # 如果有右孩子，右孩子入队
            if tree.right:
                self.__q.put(tree.right)


if __name__ == '__main__':
    '''
         A
       /   \
      B     C
     / \     \
    D   E     F
             /
            G
    '''
    ct = Node('A',Node('B',Node('D'),Node('E')),Node('C',right=Node('F',Node('G'))))
    tt = TreeTraverse()
    tt.traverse(ct)

