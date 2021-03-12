# -*- coding: utf-8 -*-

class EmptyStackError(BaseException):
    r'EmptyStackError'

class StackOverflowError(BaseException):
    r'StackOverflowError'

class StackSizeError(BaseException):
    r'StackSizeError'


class Stack():
    def __init__(self, size):
        self.size = size
        if self.size <= 0:
            raise StackSizeError
        self.data = [None] * self.size
        self.top = -1
    
    def push(self, num):
        '''入栈：
            1、若top大于栈长度时，栈满报错
            2、top加1，指向入栈地址
            3、data[top] = x
        '''
        if self.top == self.size:
            raise StackOverflowError
        self.top += 1
        self.data[self.top] = num
        
        

    def pop(self):
        '''出栈：
            1、若top小于等于0，栈空报错
            2、x = data[top]，弹出x
            3、top减1，指向栈顶
            
        '''
        if self.top == -1:
            raise EmptyStackError
        res = self.data[self.top]
        self.top -= 1
        return res

    def peek(self):
        if self.top == -1:
            return
        return self.data[self.top]

class PyStack():
    def __init__(self, size=0):
        self.size = size
        self.__s = []

    def push(self, num):
        self.__s.append(num)

    def pop(self):
        if self.empty():
            raise 'EmptyStackError'    
        
        return self.__s.pop()

    def peek(self):
        if self.empty():
            raise 'EmptyStackError'
        return self.__s[-1]

    def empty(self):
        return len(self.__s) == 0


if __name__ == '__main__':
    # pys = PyStack()
    # pys.push(3)
    # pys.push(2)
    # pys.push(1)
    # # print(pys.pop())
    # # print(pys.pop())
    # # print(pys.pop())
    # print(pys.peek())
    # # print(pys.pop())
    s = Stack(3)
    s.push(1)
    s.push(11)
    s.push(12)
    # s.push(12)

    print(s.data)
    print(s.pop())
    print(s.pop())
    # print(s.pop())
    print(s.peek())
    # print(s.pop())
    # s.pop()
    # s.pop()

    # print(s.data)
    # print(s.peek())