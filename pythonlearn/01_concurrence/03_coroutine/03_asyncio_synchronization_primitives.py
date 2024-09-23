import asyncio
import random
import tasks

shared_list = []  # 共享的list

shared_total = 5  # 共享资源

get = tasks.get


# 协程锁
class Tutorial01:
    """
    不加锁的时候
    协程 A 读取 total，假设当前值大于 0，发生切换。
    协程 B 也读取 total，此时它还未被修改，值仍然大于 0。
    协程 A 完成减 1 操作。
    协程 B 完成减 1 操作。
    这意味着两个协程完成后，total 被减了两次
    """

    async def update_resource(self):
        global shared_total

        if shared_total > 0:
            # 发生切换后就会出现同步问题，所以在写程序的时候要尽量避免
            await asyncio.sleep(0.1)  # 模拟异步操作中的延迟
            shared_total -= 1

    async def amain(self):
        tasks = [asyncio.create_task(self.update_resource()) for _ in range(50)]
        await asyncio.gather(*tasks)
        print(f"最终资源值: {shared_total}")

    def main(self):
        asyncio.run(self.amain())


class Tutorial02:
    """
    加锁后
    协程 A 先获取锁，然后读取 total，假设当前值大于 0，发生切换。
    协程 B 获取锁的时候发现，锁被A占用了，只能等待A释放了再读取 total。
    等待协程 A 完成减 1 操作释放了锁。
    此时协程 B 等到了锁，再进行减 1 操作。
    两个并发操作，通过锁变成了串行操作
    """

    async def update_resource(self, lock):
        global shared_total
        async with lock:  # 只有持有锁的协程可以修改共享资源
            if shared_total > 0:
                # 发生切换后就会出现同步问题，所以在写程序的时候要尽量避免
                await asyncio.sleep(0.1)  # 模拟异步操作中的延迟
                shared_total -= 1

    async def amain(self):
        lock = asyncio.Lock()  # 创建一个异步锁
        tasks = [asyncio.create_task(self.update_resource(lock)) for _ in range(50)]
        await asyncio.gather(*tasks)
        print(f"最终资源值: {shared_total}")

    def main(self):
        asyncio.run(self.amain())


# 协程信号量
class Tutorial03:

    async def worker(self, semaphore, site):
        async with semaphore:
            await get(site)

    async def amain(self):
        semaphore = asyncio.Semaphore(4)  # 信号量限制并发数量为4
        tasks_list = []
        for site in ["baidu", "sina", "163", "web", "douyin", "kuaishou", "qq"]:
            task = asyncio.create_task(self.worker(semaphore, site))
            tasks_list.append(task)

        await asyncio.gather(*tasks_list)

    def main(self):
        asyncio.run(self.amain())


# 事件
class Tutorial04:

    async def add_to_list(self, lock, item):
        await asyncio.sleep(random.random())  # 模拟异步操作中的延迟
        async with lock:  # 确保每次只有一个协程可以访问和修改共享list
            shared_list.append(item)

    async def amain(self):
        lock = asyncio.Lock()  # 创建一个异步锁
        tasks = [asyncio.create_task(self.add_to_list(lock, i)) for i in range(50)]
        await asyncio.gather(*tasks)
        print(f"无锁的情况下最终列表: {len(shared_list)} {shared_list}")

    def main(self):
        asyncio.run(self.amain())


if __name__ == '__main__':
    # t1 = Tutorial01()
    # t1.main()
    #
    # t2 = Tutorial02()
    # t2.main()

    t3 = Tutorial03()
    t3.main()

    # t4 = Tutorial04()
    # t4.main()
