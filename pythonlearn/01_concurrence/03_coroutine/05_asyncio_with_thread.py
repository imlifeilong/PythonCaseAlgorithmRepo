import asyncio
from multiprocessing import Process, Pool
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import tasks
import utils

cpu_task = tasks.cpu_task
io_task = tasks.io_task


class Tutorial01:
    # 同步IO代码
    @utils.runtime
    def main(self):
        for i in range(100):
            print(io_task())
        # print(io_task())


class Tutorial02:
    # 线程池 异步请求
    @utils.runtime
    def main(self):
        with ThreadPoolExecutor() as pool:
            urls = ["https://www.baidu.com"] * 100
            results = pool.map(io_task, urls)
            for r in results:
                print(r)


class Tutorial03:
    # 使用协程异步IO
    @utils.aruntime
    async def amain(self):
        loop = asyncio.get_running_loop()
        with ThreadPoolExecutor() as pool:
            urls = ["https://www.baidu.com"] * 100
            task_list = [loop.run_in_executor(pool, partial(io_task, u)) for u in urls]
            results = await asyncio.gather(*task_list)

            for r in results:
                print(r)

    @utils.runtime
    def main(self):
        asyncio.run(self.amain())


if __name__ == '__main__':
    # t1 = Tutorial01()
    # t1.main() # 18.7305 seconds

    # t2 = Tutorial02()
    # t2.main()  # 1.5463 seconds

    t3 = Tutorial03()
    t3.main()  # 1.5463 seconds
