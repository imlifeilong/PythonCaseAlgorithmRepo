class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")


def print_tree_vertical(root, space=0):
    if root is None:
        return

    space += 5

    print_tree_vertical(root.right, space)

    print(" " * space + str(root.val))

    print_tree_vertical(root.left, space)


# def build_tree(data):
#     def build_node(index):
#         if index >= len(data) or data[index] is None:
#             return None
#
#         root = index
#         left = root * 2 + 1
#         right = left + 1
#         print(data[root], root, left, right)
#
#         node = TreeNode(data[index])
#         node.left = build_node(2 * index + 1)
#         node.right = build_node(2 * index + 2)
#         return node
#
#     root = build_node(0)
#     return root


def build_tree(data):
    if not data:
        return None

    # 创建根节点并将其添加到队列中
    root = TreeNode(data[0])
    queue = [root]  # 使用队列来暂存待添加子节点的父节点
    data_index = 1  # 数据索引，用于遍历输入数据数组

    # 遍历队列中的节点并添加子节点
    while queue and data_index < len(data):
        node = queue.pop(0)  # 取出队首节点，该节点是待添加子节点的父节点

        # 添加左子节点
        if data[data_index] is not None:
            node.left = TreeNode(data[data_index])
            queue.append(node.left)  # 将左子节点加入队列，以便后续添加其子节点

        data_index += 1

        # 添加右子节点
        if data_index < len(data) and data[data_index] is not None:
            node.right = TreeNode(data[data_index])
            queue.append(node.right)  # 将右子节点加入队列，以便后续添加其子节点

        data_index += 1

    return root  # 返回构建好的根节点
