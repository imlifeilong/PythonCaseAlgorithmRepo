# _*_ coding:utf-8 _*_
'''
'''

def Fibonacci(n):
    '''
    前n个斐波拉契数
    '''
    if n == 0 or n == 1:
        return n
    alist = []
    a,b = 0,1
    while n:
        alist.append(a)
        a,b = b,a+b
        n -= 1
    print alist

def Fibonacci1(n):
    '''
    前n内的斐波拉契数
    '''
    if n == 0 or n == 1:
        return n
    alist = []
    a,b = 0,1
    while a < n:
        alist.append(a)
        a,b = b,a+b
    print alist
    
def Fibonacci2(n):
    if n == 0 or n == 1:
        return n
    return Fibonacci2(n-1)+Fibonacci2(n-2)


def loopyears(year):
    if year == 0:
        return
    if year % 4 == 0 and year % 100 != 0:
        print year
    elif year % 400 == 0:
        print year
    else:
        print year,"not a loopyear"
        
        
def sushu(n):
    for i in range(2,n):
        if n % i == 0:
            return
    print  n
        
           
if __name__ == "__main__":
    #Fibonacci(10)
    #Fibonacci1(10)
    #for i in range(10):
        #print Fibonacci2(i)
    #loopyears(2004)
    for i in range(1000):
        sushu(i)
    #print sushu(999)