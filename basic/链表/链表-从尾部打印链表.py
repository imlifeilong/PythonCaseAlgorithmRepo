
class Node():
    def __init__(self, value=None, _next=None):
        self.value = value
        self.next = _next

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

class LinkTail():
    __s = Stack()
    def _print(self, link):
        # 遍历将所有节点压入栈中，最后依次从栈中弹出
        while link:
            self.__s.push(link.value)
            link = link.next
        
        while not self.__s.empty():
            print(self.__s.pop())

if __name__ == '__main__':
    link1 = Node(1, Node(3, Node(5, Node(7, Node(10, Node(15))))))
    link2 = Node(5, Node(8, Node(10, Node(11, Node(12, Node(15))))))
    lcp = LinkTail()
    lcp._print(link1)
    lcp._print(link2)