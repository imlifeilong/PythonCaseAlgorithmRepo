'''
使用辅助栈对已知栈内元素进行排序
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

    def size(self):
        return len(self.__s)

class StackSort():
    def __init__(self, stack):
        self.__s = stack
        self.__h = Stack()

    def sort(self):
        
        while not self.__s.empty():
            data = self.__s.pop()
            # 如果 data 大于辅助栈顶元素，此时data是辅助栈的最大元素，应该在栈底
            # 将辅助栈元素依次弹出，压入原来栈中，此时辅助栈为空
            while not self.__h.empty() and self.__h.peek() > data:
                self.__s.push(self.__h.pop())
            
            # 如果辅助栈顶元素小于等于当前元素，压入辅助栈
            self.__h.push(data)

        # 将辅助栈的数据压回 原始栈
        while not self.__h.empty():
            self.__s.push(self.__h.pop())

        return self.__s

if __name__ == '__main__':
    src_stack = Stack()
    for i in [3, 5, 9, 4, 8, 2, 7]:
        src_stack.push(i)

    sort_stack = StackSort(src_stack)
    res = sort_stack.sort()
    while not res.empty():
        print(res.pop(), res.size())