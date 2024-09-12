from threading import Thread
import threading
import queue

from f_concurrent.crawlab import Crawlab


class ProducerConsumerModel(Crawlab):

    def crawl_producer(self, crawl_queue: queue.Queue, parse_queue: queue.Queue):
        """
        生产者
        :return:
        """
        while True:
            crawl = crawl_queue.get()
            # 入队完成
            if crawl is None:
                # 多生产者时，将结束标志放回队列，传递给其他线程
                crawl_queue.put(crawl)
                break
            response = self.crawl(crawl)
            parse_queue.put(response)

        # 数据入队完成后，告诉队列已经没有数据了
        parse_queue.put(None)

    def crawl_consumer(self, parse_queue: queue.Queue):
        """
        消费者
        :return:
        """
        while True:
            response = parse_queue.get()
            print(f'{threading.current_thread().name}解析出队{response}')
            if response is None:
                print('队列传输完毕')
                # 多消费者时，将结束标志放回队列，传递给其他线程
                parse_queue.put(response)
                break
            self.parse(response)

    def main(self):

        parse_queue = queue.Queue()
        crawl_queue = queue.Queue()
        for i in range(1, self.max_count + 1):
            crawl_queue.put(i)
        crawl_queue.put(None)

        # 生产者0
        t0 = Thread(target=self.crawl_producer, args=(crawl_queue, parse_queue,), name='produce0')
        t0.start()
        # 生产者1
        t1 = Thread(target=self.crawl_producer, args=(crawl_queue, parse_queue,), name='produce1')
        t1.start()
        # 消费者1
        t2 = Thread(target=self.crawl_consumer, args=(parse_queue,), name='consumer1')
        t2.start()

        # # 消费者2
        t3 = Thread(target=self.crawl_consumer, args=(parse_queue,), name='consumer2')
        t3.start()


if __name__ == '__main__':
    cl = ProducerConsumerModel()
    cl.main()
