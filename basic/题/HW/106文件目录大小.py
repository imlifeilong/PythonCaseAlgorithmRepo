def main(data, n):
    cache_tree = {}  # 存树结构，一键多值
    cache_size = {}  # 存每个节点的大小
    for x in data:
        a = x[0]
        b = int(x[1])
        c1 = x[2].strip('()')
        c = c1.split(',') if c1 and ',' in c1 else c1

        cache_size[a] = b
        if a not in cache_tree:
            cache_tree[a] = []

        cache_tree[a].extend(c)

    def dfs(n):
        '''递归获取子节点的大小'''
        result = cache_size.get(n, 0)
        subtree = cache_tree.get(n, [])
        # 获取当前节点的大小，和所有子节点
        for i in range(len(subtree)):
            result += dfs(subtree[i])
        return result

    res = dfs(n)
    print(res)


s = """3 15 ()
1 20 (2)
2 10 (3)""".split('\n')
n = '1'

s = """4 20 ()
5 30 ()
2 10 (4,5)
1 40 ()""".split('\n')

n = '2'
data = list(map(lambda x: x.split(), s))
main(data, n)
