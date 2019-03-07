'''
搜索二叉树
    1、空树为搜索二叉树
    2、当前节点的左子树的值都小于当前节点，右子树都大于当前节点
    3、左、右子树都是搜索二叉树
    4、中序（左中右）遍历的时候，如果是按从小到大就是搜索二叉树
'''
import sys

class Node():
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    # @property
    # def root(self):
    #     return self.__root

    # @property
    # def left(self):
    #     return self.__left

    # @property
    # def right(self):
    #     return self.__right

class Stack():
    def __init__(self):
        self.__s = []

    def push(self, num):
        self.__s.append(num)

    def pop(self):
        if self.empty():
            raise 'StackEmptyError'
        return self.__s.pop()

    def empty(self):
        return len(self.__s) == 0

    def peek(self):
        if self.empty():
            raise 'StackEmptyError'

        return self.__s[-1]

    def size(self):
        return len(self.__s)

class BinarySearchTree():
    def __init__(self):
        self._is_binary_search = True
        self.pre_node = sys.float_info.min
        self.__s = Stack()

    def is_binary_search(self, tree):
        self._mid_order(tree)
        return self._is_binary_search

    def _mid_order(self, tree):
        if not tree.root:
            return

        while not self.__s.empty() or tree:
            if tree:
                self.__s.push(tree)
                tree = tree.left
            else:
                tree = self.__s.pop()
                current_node_value = int(tree.root)

                # 如果当前值小于上一个值，就不是搜索二叉树
                if current_node_value < self.pre_node:
                    self._is_binary_search = False
                    return
                else:
                    self.pre_node = current_node_value

                tree = tree.right

    def find_min(self, tree):
        while tree:
            if tree.left:
                tree = tree.left
            else:
                return tree.root

    def find_max(self, tree):
        while tree:
            if tree.right:
                tree = tree.right
            else:
                return tree.root

    def search(self, tree, value):
        if not tree.root:
            return

        while tree:
            if tree.root < value:
                tree = tree.right
            elif tree.root > value:
                tree = tree.left
            else:
                return tree.root

    def insert(self, tree, value):
        '''
        若插入的值比根节点小，则将其插入根节点的左子树，若比根节点大，则将其插入右子树
        '''
        if not tree:
            tree = Node(value)
        elif tree.root > value:
            tree.left = self.insert(tree.left, value)
        elif tree.root < value:
            tree.right = self.insert(tree.right, value)

        return tree


if __name__ == '__main__':
    '''
         4
       /   \
      2     5  
     / \     \
    1   3     7 
             /
            6  

    Node('4',Node('2',Node('1'),Node('3')),Node('5',right=Node('7',Node('6'))))
    '''
    ct = Node('4',Node('2',Node('1'),Node('3')),Node('5',right=Node('7',Node('6'))))
    tt = BinarySearchTree()
    ct = tt.insert(ct, '8')
    print(ct)
    print(tt.find_max(ct))
    # ct = Node()
    # print(tt.is_binary_search(ct))
    # print(tt.search(ct, '3'))
    # print(tt.find_max(ct))
    # print(tt.find_min(ct))
