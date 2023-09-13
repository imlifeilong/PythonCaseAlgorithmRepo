import os
import heapq


class CounterURL:

    def process(self, filepath):
        counter = {}
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                line = f.readline()
                while line:
                    line = f.readline().strip()
                    if line:
                        if line not in counter:
                            counter[line] = 1
                        else:
                            counter[line] += 1

        result = sorted(counter.items(), key=lambda x: -x[1])
        for url, count in result[:10]:
            print(f"{url}:{count}")

    """
    sorted 时间复杂度 O(n * log(n))
    优化可以使用小根堆 进行流式处理 时间复杂度 O(n * log(10))
    如果文件很大，需要分开处理，将文件分割成在内存可处理的大小，然后分别进行统计，最后再合并时获取前10条
    """


if __name__ == '__main__':
    c = CounterURL()
    filepath = 'access.log'
    c.process(filepath)
