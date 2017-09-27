# _*_ coding:utf-8 _*_
'''
打印1到n位最大数，考虑大数
'''
def _1to_n(n):
    if n == 0 or n == 1:
        return n
    num = ['0'] * n
    for i in range(10):
        num[0] = str(i)
        _print_1ton(num,n,0)
    num = []
    
def _print_1ton(num,slen,index):
    if index == slen-1:
        _print(num)
        return
    for i in range(10):
        num[index+1] = str(i)
        _print_1ton(num,slen,index+1)
    
def _print(string):
    flag = True
    slen = len(string)
    for i in range(slen):
        if flag and string[i] != '0':
            flag = False
        if not flag:
            print "%c" %string[i],
    print ""
                  
if __name__ == "__main__":
    a='0099'
    #_print(a)
    _1to_n(10)
