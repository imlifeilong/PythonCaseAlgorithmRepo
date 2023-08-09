result = {}


def main(line):
    # 处理数字行
    if line.isdigit():
        topn = int(line)
        # key=lambda x: (x[1], x[0]) 先对字典的值进行排序，再对字典的key排序（字符串排序）
        data = sorted(result.items(), key=lambda x: (x[1], x[0]), reverse=True)
        urls = ';'.join([i[0] for i in data][:topn])
        print(urls)
    else:
        # 使用字典统计URL个数
        if line not in result:
            result[line] = 1
        else:
            result[line] += 1


s = """news.qq.com
news.sina.com.cn
news.qq.com
news.qq.com
game.163.com
game.163.com
www.huawei.com
www.cctv.com
3
www.huawei.com
www.cctv.com
www.huawei.com
www.cctv.com
www.huawei.com
www.cctv.com
www.huawei.com
www.cctv.com
www.huawei.com
3"""

s = """news.qq.com
www.cctv.com
1
www.huawei.com
www.huawei.com
2
3"""
data = s.split('\n')
for line in data:
    main(line)
