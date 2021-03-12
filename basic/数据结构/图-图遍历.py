'''
宽度优先遍历
    1、利用队列实现
    2、从源节点开始依次按照宽度进队列，然后弹出
    3、每弹出一个点，把该节点所有没有进过队列的邻接点放入队列
    4、直到队列变空
深度优先遍历
    1、利用栈实现
    2、从源节点开始把节点按照深度放入栈，然后弹出
    3、每弹出一个点，把该节点下一个没有进过栈的邻接点放入栈
    4、直到栈变空
'''
from queue import Queue

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

class Node:
    def __init__(self, value):
        # 节点值
        self._value = value
        # 节点入
        self._from = 0
        # 节点出
        self._to = 0
        # 该节点邻居
        self.nexts = []
        # 节点为from的情况下，边的集合
        self.edges = []

class Edge():
    def __init__(self, weight, _from, _to):
        # 权重
        self.weight = weight
        # from节点
        self._from = _from
        # to节点
        self._to = _to

class Graph():
    def __init__(self):
        # 节点集合，字典形式 {节点编号: 节点}
        self.nodes = {}
        # 边集合
        self.edges = []


def CreateGraph(matrix):
    graph = Graph()
    for edge in matrix:
        weight = edge[0]
        _from = edge[1]
        _to = edge[2]
        
        if _from not in graph.nodes:
            graph.nodes[_from] = Node(_from)
        
        if _to not in graph.nodes:
            graph.nodes[_to] = Node(_to)

        from_node = graph.nodes[_from]
        to_node = graph.nodes[_to]
        new_edge = Edge(weight, from_node, to_node)
        from_node.nexts.append(to_node)
        from_node._to += 1
        to_node._from += 1
        from_node.edges.append(new_edge)
        graph.edges.append(new_edge)
    return graph


class GraphTraverse():
    def __init__(self):
        self.__q = Queue()
        self.__s = set()
        self.__stack = Stack()


    def bfs(self, graph):
        if not graph:
            return
        self.__q.put(graph)
        self.__s.add(graph)

        while not self.__q.empty():
            current = self.__q.get()
            print(current._value)

            for _next in current.nexts:
                if _next not in self.__s:
                    self.__s.add(_next)
                    self.__q.put(_next)

    def dfs(self, graph):
        if graph is None:
            return
        print(graph._value)
        self.__s.add(graph)
        self.__stack.push(graph)
        while not self.__stack.empty():
            current = self.__stack.pop()               # 弹出最近入栈的节点
            for _next in current.nexts:         # 遍历该节点的邻接节点
                if _next not in self.__s:    # 如果邻接节点不重复
                    self.__stack.push(current)       # 把节点压入
                    self.__stack.push(_next)      # 把邻接节点压入
                    self.__s.add(_next)           # 登记节点
                    print(_next._value)       # 打印节点值
                    break

if __name__ == '__main__':
    m = [
        [2, 1, 2],
        [3, 1, 3],
        [3, 2, 5],
        [3, 2, 4],
        [1, 3, 4],
        [1, 3, 7],
        [1, 5, 4],
        [4, 4, 6],
        [4, 5, 6],
        [4, 7, 6],
    ]
    '''
                1
              /   \
             2     3
             | \  / \
             5-- 4   7
              \  |  /
                 6
    '''
    g = CreateGraph(m)
    gtbfs = GraphTraverse()
    gtbfs.bfs(g.nodes[1])
    # gtbfs.dfs(g.nodes[1])

