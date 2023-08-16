def main(s1, s2):
    def counter(sx):
        tmp = {}
        for c in sx:
            if c in tmp:
                tmp[c] += 1
            else:
                tmp[c] = 1
        return tmp
    # 记录字符串中字符出现的次数
    a = counter(s1)
    b = counter(s2)

    res = {}
    for k, v in a.items():
        if k in b:
            # 找到共同出现的，记录最小的次数
            key = min(v, b[k])
            if key not in res:
                res[key] = []
            res[key].append(int(k))
    if res:
        ress = sorted(res.items(), key=lambda x: x[0])
        for i in ress:
            print(f"{i[0]}:{','.join(map(str, sorted(i[1])))}")
    else:
        print('NULL')


s1 = '''5,8,11,3,6,8,8,-1,11,2,11,11'''.split(',')
s2 = '''11,2,11,8,6,8,8,-1,8,15,3,-9,11'''.split(',')


s1 = '''8,5,3,6,-8,8,11,12'''.split(',')
s2 = '''8,2,8,8,8,-1,15,12'''.split(',')
main(s1, s2)