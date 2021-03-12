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

class TreeTraverse():
    def __init__(self):
        self.__s = Stack()
        self.__h = Stack()


    def _pre(self, tree):
        if not tree:
            return
        self.__s.push(tree)
        while not self.__s.empty():
            data = self.__s.pop()
            print(data.root)
            # 先压右孩子，后弹出
            if data.right:
                self.__s.push(data.right)
            # 后压左孩子，先弹出
            if data.left:
                self.__s.push(data.left)

    def _mid(self, tree):
        if not tree:
            return

        while not self.__s.empty() or tree:
            # 当前节点不为空，压入栈，再将当前节点指向他的左孩子，进行下轮判断
            if tree:
                self.__s.push(tree)
                tree = tree.left
            else:
                # 如果当前节点为空，弹出栈顶元素置为当前节点，并打印，再将当前节点指他的右孩子
                tree = self.__s.pop()
                print(tree.root)
                tree = tree.right

    def _aft(self, tree):
        if not tree:
            return
        # 将树的元素依次按照，中右左压入栈中，然后再从栈弹出，顺序就是左右中
        self.__s.push(tree)
        while not self.__s.empty():
            data = self.__s.pop()
            
            self.__h.push(data.root)
            
            if data.left:
                self.__s.push(data.left)
            if data.right:
                self.__s.push(data.right) 

        while not self.__h.empty():
            print(self.__h.pop())

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
    tt = TreeTraverse()
    # print('前序--->')
    # tt._pre(ct)
    # print('中序--->')
    # tt._mid(ct)
    print('后序--->')
    tt._aft(ct)

