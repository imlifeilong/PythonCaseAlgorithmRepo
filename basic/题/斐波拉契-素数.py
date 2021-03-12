# _*_ coding:utf-8 _*_
'''
'''
count = 1
def Fibonacci(n):
    '''
    前n个斐波拉契数
    '''
    if n == 0 or n == 1:
        return n
    # alist = []
    a,b = 0,1
    while n:
        # alist.append(a)
        a,b = b,a+b
        n -= 1
        print(a)

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
    print(alist)
    
def Fibonacci2(n):
    if n == 0 or n == 1:
        return n
    global count
    count += 1
    return Fibonacci2(n-1)+Fibonacci2(n-2)


# 记忆体，动态规划
def Fibonacci3(n, _dict={}):
    if n == 0 or n == 1:
        return n

    # 如果数据已经在字典中，直接返回
    if n in _dict:
        return _dict[n]
    global count
    count += 1
    # 如果没在字典中，就先计算，然后在放到字典
    res = Fibonacci3(n-1) + Fibonacci3(n-2)
    
    _dict[n] = res

    return res


def loopyears(year):
    if year == 0:
        return
    if year % 4 == 0 and year % 100 != 0:
        print(year)
    elif year % 400 == 0:
        print(year)
    else:
        print(year, "not a loopyear")
        
        
def sushu(n):
    for i in range(2,n):
        if n % i == 0:
            return
    print(n)
        
           
if __name__ == "__main__":
    #Fibonacci(10)
    # for i in range(10):
        # print(Fibonacci3(i))

    res = {}
    for i in range(10000):
        # Fibonacci3(i)
        if i == 0 or i == 1 or i == 2:
            res[i] = i
            continue
        if i not in res:
            res[i] = 0
        res[i] = res[i-1] + res[i-2]
    print(res)
    #loopyears(2004)
    # for i in range(1000):
    #     sushu(i)
    #print sushu(999)