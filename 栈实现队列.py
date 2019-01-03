'''
栈结构实现队列
'''

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

class Stack2Queue():
    def __init__(self):
        self.__s = Stack()
        self.__h = Stack()

    def put(self, num):
        self.__s.push(num)

    def get(self):
        # get时先发生转换，再弹出辅助栈的数据
        self.convert()
        res = self.__h.pop()
    
        return res
    
    def convert(self):
        if self.__s.empty() and self.__h.empty():
            raise 'QueueEmptyError'
        # 辅助栈为空的时候，将主栈的数据一次弹出压入辅助栈
        elif self.__h.empty():
            while not self.__s.empty():
                self.__h.push(self.__s.pop())

    def empty(self):
        return len(self.__s) == 0


if __name__ == '__main__':
    sq = Stack2Queue()
    sq.put(3)
    sq.put(2)
    sq.put(1)
    # print(sq.get())
    print(sq.get())
    sq.put(8)
    print(sq.get())
    print(sq.get())
    sq.put(9)
    print(sq.get())
    print(sq.get())
    # s = Stack()
    # s.push(3)
    # # s.push(5)
    # print(s.peek())
    # print(s.pop())
    # print(s.pop())

