# _*_ coding:utf-8 _*_
'''
位移比运算速率要高很多
'''

def _count1(num):
    flag = 1
    cou = 0
    while flag < 65536:
        if (num & flag):
            cou += 1
        flag = flag << 1
    print cou
    

def _count2(num):
    '''
    一个数减1，再与原数 做 &运算，相当于把该数（二进制）最右边的1变成0
    '''
    cou = 0
    while num:
        num = num & (num-1)
        cou += 1
    print cou
   
   
def _count3(num):
    '''
    2的次幂数（二进制中）只有一个1
    '''
    if num & (num-1) == 0:
        print num
     
     

    
   
if __name__=="__main__":
    #_count1(110)
    #_count2(110)
    _count3(5)