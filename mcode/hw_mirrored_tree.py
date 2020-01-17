'''
	判断一棵树是否是对称的
'''

class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

class MirroredTree():
	def is_mirrored(self, tree):
		# 空树对称
		if tree is None:
			return True
		return self.handler(tree.left, tree.right)

	def handler(self, left, right):
		# 无左右孩子页对称
		if left is None and right is None:
			return True
		# 左右只要又其中一个就不对称
		if left is None or right is None:
			return False

		if left and right:
			# 判断值是否相等，再递归 判断左孩子的左与右孩子的右，左孩子的右与右孩子的左是否相等
			return left.value == right.value and self.handler(left.left, right.right) and self.handler(left.right, right.left)

def printTree(root):
    if not root:
        return
    print("Binary Tree: ")
    printInOrder(root, 0, 'H', 10)

def printInOrder(root, height, preStr, length):
    if not root:
        return
    printInOrder(root.right, height+1, 'v', length)
    string = preStr + root.value + preStr
    leftLen = (length - len(string)) // 2
    rightLen = length - len(string)- leftLen
    res = " "*leftLen + string + " "*rightLen
    print(" "*height*length + res)
    printInOrder(root.left, height+1, '^', length)

if __name__ == '__main__':
	tree = Node('A')
	tree.left = Node('B', Node('D'), Node('C'))
	tree.right = Node('B', Node('C'), Node('D'))
	m = MirroredTree()
	print(m.is_mirrored(tree))
	printTree(tree)