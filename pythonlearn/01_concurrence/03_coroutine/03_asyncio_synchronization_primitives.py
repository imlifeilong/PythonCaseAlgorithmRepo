import asyncio
import random

shared_resource = 0  # 共享资源
shared_list = []  # 共享的list

total = 5


class Tutorial01:
    """
    协程 A 读取 total，假设当前值大于 0，发生切换。
    协程 B 也读取 total，此时它还未被修改，值仍然大于 0。
    协程 A 完成减 1 操作。
    协程 B 完成减 1 操作。
    这意味着两个协程完成后，total 被减了两次
    """

    async def update_resource(self):
        global total

        if total > 0:
            # 发生切换后就会出现同步问题，所以在写程序的时候要尽量避免
            await asyncio.sleep(0.1)  # 模拟异步操作中的延迟
            total -= 1

    async def amain(self):
        tasks = [asyncio.create_task(self.update_resource()) for _ in range(50)]
        await asyncio.gather(*tasks)
        print(f"最终资源值: {total}")

    def main(self):
        asyncio.run(self.amain())


class Tutorial02:
    """
    协程 A 读取 total，假设当前值大于 0，发生切换。
    协程 B 也读取 total，此时它还未被修改，值仍然大于 0。
    协程 A 完成减 1 操作。
    协程 B 完成减 1 操作。
    这意味着两个协程完成后，total 被减了两次
    """

    async def update_resource(self, lock):
        global total
        async with lock:  # 只有持有锁的协程可以修改共享资源
            if total > 0:
                # 发生切换后就会出现同步问题，所以在写程序的时候要尽量避免
                await asyncio.sleep(0.1)  # 模拟异步操作中的延迟
                total -= 1

    async def amain(self):
        lock = asyncio.Lock()  # 创建一个异步锁
        tasks = [asyncio.create_task(self.update_resource(lock)) for _ in range(50)]
        await asyncio.gather(*tasks)
        print(f"最终资源值: {total}")

    def main(self):
        asyncio.run(self.amain())


# class Tutorial01:
#     """
#     协程 A 读取 shared_resource，假设当前值为 0。
#     协程 B 也读取 shared_resource，此时它还未被修改，值仍然是 0。
#     协程 A 完成加 1 操作，将 shared_resource 设为 1。
#     协程 B 完成加 1 操作，因为它之前读取的值是 0，所以将 shared_resource 设为 1。
#     这意味着两个协程完成后，shared_resource 仅增加了一次，而不是两次
#     """
#
#     async def update_resource(self):
#         global shared_resource
#         temp = shared_resource
#         await asyncio.sleep(0.1)  # 模拟异步操作中的延迟
#         shared_resource = temp + 1
#
#     async def amain(self):
#         tasks = [asyncio.create_task(self.update_resource()) for _ in range(50)]
#         await asyncio.gather(*tasks)
#         print(f"最终资源值: {shared_resource}")
#
#     def main(self):
#         asyncio.run(self.amain())
#
#
# class Tutorial02:
#
#     async def safe_update_resource(self, lock):
#         global shared_resource
#         async with lock:  # 只有持有锁的协程可以修改共享资源
#             temp = shared_resource
#             await asyncio.sleep(0.1)  # 模拟异步操作中的延迟
#             shared_resource = temp + 1
#
#     async def amain(self):
#         lock = asyncio.Lock()  # 创建一个异步锁
#         tasks = [asyncio.create_task(self.safe_update_resource(lock)) for _ in range(50)]
#         await asyncio.gather(*tasks)
#         print(f"最终资源值: {shared_resource}")
#
#     def main(self):
#         asyncio.run(self.amain())


class Tutorial03:

    async def add_to_list(self, item):
        await asyncio.sleep(random.random())  # 模拟异步操作中的延迟
        shared_list.append(item)  # 并发地向共享list中添加数据

    async def amain(self):
        tasks = [asyncio.create_task(self.add_to_list(i)) for i in range(50)]
        await asyncio.gather(*tasks)
        print(f"无锁的情况下最终列表: {len(shared_list)} {shared_list}")

    def main(self):
        asyncio.run(self.amain())


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
    t1 = Tutorial01()
    t1.main()

    t2 = Tutorial02()
    t2.main()

    # t3 = Tutorial03()
    # t3.main()

    # t4 = Tutorial04()
    # t4.main()

