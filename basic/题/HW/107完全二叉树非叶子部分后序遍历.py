class Tree:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right


def insert_complete_tree(data, root, i, n):
    # 创建完全二叉树
    if i < n:
        temp = Tree(root=data[i])
        root = temp
        root.left = insert_complete_tree(data, root.left, 2 * i + 1, n)
        root.right = insert_complete_tree(data, root.right, 2 * i + 2, n)
    return root


def main(s):
    def after(tree, result):
        if not tree:
            return
        after(tree.left, result)
        after(tree.right, result)
        # 打印有子节点的
        if tree.left or tree.right:
            result.append(tree.root)
            # print(tree.root)

    result = []
    # 建树
    tree = insert_complete_tree(s, None, 0, len(s))
    # 后续遍历
    after(tree, result)
    print(' '.join(result))


s = '1 2 3 4 5 6 7 8'.split()
main(s)
