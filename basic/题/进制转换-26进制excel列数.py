# _*_ coding:utf-8 _*_
'''
excel中字母即对应的列数
'''

def _26toten(string):
    char = {}
    for x in range(97,123):
        char[chr(x)] = x-96
    num = []
    for x in string:
        num.append(char[x])
    #print num
    nlen = len(num)
    n=0
    for x in num:
        i = 26 ** (nlen-1)
        n += x * i
        nlen -= 1
    print n

def _tento_oth(n,m):
    '''
    n 转换成 m进制
    '''
    if n is None and m is None:
        return
    temp = []
    su = 0
    while n :
        temp.append(n % m)
        n = n / m
    temp.reverse()
    for i in temp:
        su = su * 10 + i
    print su

def _othto_ten(n,m):
    '''
    m 进制的 n转成 10进制
    '''
    if n is None and m is None:
        return
    temp = []
    while n:
        temp.append(n % 10)
        n = n / 10
    temp.reverse()

    su = 0
    nlen = len(temp)
    for i in temp:
        t = m ** (nlen - 1)
        su = su + i * t
        nlen -= 1
    print su



def _strto_int(string):
    '''
    字符串转换整数
    '''
    st ={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    num = []
    su = 0
    if string == "":
        return
    
    for x in string:
        num.append(st[x])
    for i in num:
        su = su * 10 +i
    return su




'''
def _tento26(num):
    char = {}
    for x in range(97,123):
        char[x-96] = chr(x)
    print char
    l = []
    while num > 0:
        if num % 26 == 0:
            l.append(26)
        else:
            n = num % 26
            n = n-1
            l.append(n)           
        num /= 26
    l.reverse()
    print l
    if l[0] == 0:
        l = l[1:]
    
    s = []
    for x in l:
        s.append(char[x])
    print ''.join(s)
'''

if __name__ == '__main__':
    #_26toten("aaa")
    #_tento_oth(260,26)
    #_strto_int("111")
    _othto_ten(0,0)









