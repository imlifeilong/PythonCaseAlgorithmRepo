from threading import Thread
import threading
import time

from f_concurrent.crawlab import Crawlab


class MultithreadCrawl(Crawlab):

    def serial_crawl(self):
        """
        单线程任务
        :return:
        """
        for i in range(1, self.max_count + 1):
            self.crawl(i)

    def thread_crawl(self):
        """
        多线程任务
        :return:
        """
        jobset = set()
        for i in range(1, self.max_count + 1):
            t = Thread(target=self.crawl, args=(i,), name=f'crawl{i}')
            t.start()  # 开始执行线程，此时正在等待CPU调度
            jobset.add(t)

        print(threading.active_count())

        for t in jobset:
            t.join()  # 阻塞等待所有线程执行完成

    def main(self):
        start = time.time()
        self.serial_crawl()
        print('单线程用时', time.time() - start)

        start = time.time()
        self.thread_crawl()
        print('多线程用时', time.time() - start)


if __name__ == '__main__':
    cl = MultithreadCrawl()
    cl.main()
