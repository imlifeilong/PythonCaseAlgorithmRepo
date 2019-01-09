
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


class RebuildTree():
    def _pre_and_mid(self, pre, mid):
        if len(pre) == 0 or len(mid) == 0:
            return

        if len(pre) == 1:
            return Node(pre[0])
        
        left = self._pre_and_mid(pre[1:mid.index(pre[0])+1], mid[:mid.index(pre[0])])
        right = self._pre_and_mid(pre[mid.index(pre[0])+1:], mid[mid.index(pre[0])+1:])

        return Node(pre[0], left, right)

    def _mid_and_aft(self, mid, aft):
        if len(mid) == 0 or len(aft) == 0:
            return
        if len(mid) == 1 or len(aft) == 1:
            return Node(aft[-1])

        left = self._mid_and_aft(mid[:mid.index(aft[-1])], aft[:mid.index(aft[-1])])
        right = self._mid_and_aft(mid[mid.index(aft[-1])+1:], aft[mid.index(aft[-1]):-1])
        return Node(aft[-1], left, right)

if __name__ == '__main__':
    _pre = [1, 2, 4, 5, 8, 9, 3, 6, 7]    
    _mid = [4, 2, 8, 5, 9, 1, 6, 3, 7]
    _aft = [4, 8, 9, 5, 2, 6, 7, 3, 1]
    # ===================== 前序-中序 =====================
    # 前序遍历的第一个元素1就是树的根，中序中该元素左边的[4, 2, 8, 5, 9]就是它的左子树中序，
    # 右边的[6, 3, 7]就是它的右子树中序
    # 前序中1后面的 和左子树中序一样长度的 就是左子树的前序[2, 4, 5, 8, 9] 和右子树一样长度的 就是右子树的前序[3, 6, 7]
    # ===================== 中序-后序 =====================
    # 后序遍历的最后一个元素1就是树的根，中序中该元素左边的[4, 2, 8, 5, 9]就是它的左子树中序，
    # 右边的[6, 3, 7]就是它的右子树
    # 后序中1之前 和右子树一样长度的就是右子树的后序[6, 7, 3] 和左子树一样长度的 就是左子树的后序[4, 8, 9, 5, 2] 
    rt = RebuildTree()
    pmt = rt._pre_and_mid([str(i) for i in _pre], [str(j) for j in _mid])
    mat = rt._mid_and_aft([str(i) for i in _mid], [str(j) for j in _aft])
    print('pat-------->')
    printTree(pmt)
    print('mat-------->')
    printTree(mat)
