def main(data, k):
    print(data)
    tree = {}
    for x in data:
        if x[1] not in tree:
            tree[x[1]] = []
        tree[x[1]].append(x[0])
    print(tree)

    # 获取子节点
    subtree = tree.get(k, [])
    result = []
    # 子节点不空
    while subtree:
        print(subtree)
        curval = subtree[0]

        # 继续 搜索剩余子节点
        subtree = subtree[1:]
        # 添加子节点的第一个值，以及子节点的子节点所有值
        result.append(curval)
        result.extend(tree.get(curval, []))
    result.sort()
    print(result)


s = '''b a
c a
d c
e c
f d'''.split('\n')

s = '''b a
c a
d c
e c
f d
z f
x e'''.split('\n')

data = list(map(lambda x: x.split(), s))

k = 'c'
main(data, k)
