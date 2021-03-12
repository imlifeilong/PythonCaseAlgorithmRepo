'''
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

def printTree(root):
    if not root:
        return
    print("Binary Tree: ")
    printInOrder(root, 0, 'H', 10)

def printInOrder(root, height, preStr, length):
    if not root:
        return
    printInOrder(root.right, height+1, 'v', length)
    string = preStr + root.root + preStr
    leftLen = (length - len(string)) // 2
    rightLen = length - len(string)- leftLen
    res = " "*leftLen + string + " "*rightLen
    print(" "*height*length + res)
    printInOrder(root.left, height+1, '^', length)

class CountCompleteBinaryTreeNode():

    # 获取整棵树的高度
    def _height(self, tree, level):
        while tree:
            tree = tree.left
            level += 1
        return level - 1

    def _traverse(self, tree, level, height):
        # 如果当前节点所在层 与 整棵树的高度一样，该节点为叶节点，节点个数1
        if level == height:
            return 1

        # 如果 右子树的高 与整棵树一样高， 则整棵树的左子树就是满二叉树(2 的h次方 减 1，h是高度 )
        # 然后递归左子树，层数加1
        if self._height(tree.right, level+1) == height:


            return (1 << height-level) + self._traverse(tree.right, level+1, height)
        # 否则 右子树 必是满二叉树，然后递归左子树，层数加1
        else:

            return (1 << height-level-1) + self._traverse(tree.left, level+1, height)

    def start(self, tree):
        if not tree:
            return 0

        return self._traverse(tree, 1, self._height(tree, 1))



if __name__ == '__main__':
    '''
              4
           /     \
          2        5  
        /  \      / \
        1   3    7   8
      / |  / |   | 
     9 10 11 12 13 

    Node('4',Node('2',Node('1'),Node('3')),Node('5',Node('7',Node('6'))))
    '''
    ct = Node('4',Node('2',Node('1', Node('9'), Node('10')),Node('3', Node('11'), Node('12'))),\
        Node('5',Node('7', Node('13')), Node('8')))
    # printTree(ct)
    tt = CountCompleteBinaryTreeNode()
    node = tt.start(ct)
    print(node)