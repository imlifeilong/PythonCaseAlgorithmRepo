'''
用队列实现栈结构
'''

from queue import Queue

class Queue2Stack():
    def __init__(self):
        self.__q = Queue()
        self.__h = Queue()

    def push(self, num):
        self.__q.put(num)

    def pop(self):
        if self.__q.empty():
            raise 'StackEmptyError'

        # 将队列里的数据依次放入辅助队列中，然后把最后一个数弹出
        while self.__q.qsize() > 1:
            self.__h.put(self.__q.get())
        res = self.__q.get()
        
        # 将辅助队列和数据队列互换
        self.__q, self.__h = self.__h, self.__q

        return res

if __name__ == '__main__':
    q = Queue2Stack()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())