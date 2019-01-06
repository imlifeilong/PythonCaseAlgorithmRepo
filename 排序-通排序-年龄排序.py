# _*_ coding:utf-8 _*_
'''
公司员工年龄排序，桶排序，时间复杂度O(n)
'''
def agesort(ages, oldage):
    if ages is None or oldage == 0:
        return
    temp = {}
    ret = []
    for i in range(oldage):
        temp[i]=0
    
    for a in ages:
        if a < 0 or a > oldage:
            print "age bad"
            return 
        temp[a] += 1
    #print temp
    for i in range(oldage):
        for j in range(temp[i]):
            ret.append(i)
    print ret
                  
if __name__ == "__main__":
    string = "aabaaaab"
    ages = [22,44,11,33,45,23,24,22,45,32,44,67]
    agesort(ages,100)
