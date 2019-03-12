'''
先序遍历DLR：根节点->左子树->右子树
中序遍历LDR：左子树->根节点->右子树
后续遍历LRD：左子树->右子树->根节点
层次遍历：用一维数组存储二叉树时,总是以层次遍历的顺序存储结点。层次遍历应该借助队列。

'''

class Node():
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right


class TreeMirror():
    def image(self, tree):
        if not tree:
            return
        if not tree.left and not tree.right:
        	return

        tree.left, tree.right = tree.right, tree.left
        if tree.left:
        	self.image(tree.left)
        if tree.right:
        	self.image(tree.right)

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
    printTree(ct)
    tt = TreeMirror()
    tt.image(ct)
    printTree(ct)

