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

    协程锁使用的场景
    1. 并发修改共享数据
    当多个协程需要并发修改同一数据时，如果没有适当的同步机制，就可能出现数据竞争（race condition），导致数据不一致或损坏。使用协程锁可以确保在任意时刻只有一个协程能够访问或修改共享资源，从而避免数据竞争。

    2. 控制执行顺序
    在某些情况下，协程的执行顺序可能很重要。虽然协程的并发执行可以提高程序的效率，但在某些特定场景下，可能需要按照特定的顺序执行某些协程。通过使用协程锁，可以人为地控制协程的执行顺序，确保它们按照预期的顺序运行。

    3. 协程间的依赖关系
    当协程之间存在依赖关系时，即一个协程的执行结果可能是另一个协程的输入，使用协程锁可以确保在依赖的协程完成之前，后续的协程不会开始执行。这样可以避免因为协程执行顺序的不可预测性而导致的错误或异常。

    4. 保护关键资源
    在异步编程中，一些资源（如数据库连接、文件句柄等）可能是有限的或需要特别保护的。通过使用协程锁，可以确保在任意时刻只有一个协程能够访问这些关键资源，从而避免资源耗尽或损坏的风险。
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
    """
    asyncio.Semaphore 是 asyncio 模块中的一个同步原语，用于限制并发协程的数量。在异步编程中，信号量是一种控制资源访问的机制，适用于限制同时访问共享资源的协程数量。

    主要特性：
    信号量值：Semaphore 允许多个协程同时访问资源，初始值决定了允许的最大并发协程数。
    获取和释放：协程通过 await semaphore.acquire() 来获取信号量。如果信号量的计数器为零，协程会等待；通过 semaphore.release() 来释放信号量，计数器增加，允许其他等待的协程继续执行。
    使用场景：
    控制并发数：限制某些操作的并发执行数量，例如限制并发的 HTTP 请求数。
    资源管理：确保多个协程不会超量访问有限的资源（数据库连接、文件句柄等）。
    """

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
    """
    asyncio 中的事件 (asyncio.Event) 是一种基于协程的同步原语，用来在协程之间通信或同步。事件通常用于通知多个协程某个状态的变化，类似于线程中的事件（threading.Event）。通过 set() 设置事件，通过 clear() 清除事件，通过 wait() 等待事件被设置。
    事件的工作原理
    set()：将事件的内部标志设置为 True，并通知所有等待事件的协程。
    clear()：将事件的内部标志重置为 False，让所有等待事件的协程进入等待状态。
    wait()：如果事件的内部标志为 True，则立即返回，否则协程会等待事件被设置为 True。
    使用场景
    asyncio.Event 常用于以下场景：
    协程之间的同步，确保某些操作在事件发生之后执行。
    用作简单的信号机制来通知其他协程某个状态的改变。
    """

    async def change_light(self, light_event: asyncio.Event):
        while True:
            print("红灯亮了! 停止通行")
            light_event.clear()  # 设置红灯，汽车不能通过
            await asyncio.sleep(5)  # 红灯持续 5 秒

            print("绿灯亮了! 开始通行")
            light_event.set()  # 设置绿灯，汽车可以通过
            await asyncio.sleep(5)  # 绿灯持续 5 秒

    async def car(self, car_id, light_event):
        print(f"汽车 {car_id} 等待绿灯")
        await light_event.wait()  # 等待绿灯
        print(f"汽车 {car_id} 通过")

    async def amain(self):
        light_event = asyncio.Event()  # 创建一个事件
        light_task = asyncio.create_task(self.change_light(light_event))
        car_tasks = [asyncio.create_task(self.car(i, light_event)) for i in range(1, 60)]

        # 等待所有汽车通过
        await asyncio.gather(*car_tasks)

        # 取消红绿灯任务（在现实场景中红绿灯不会停）
        light_task.cancel()

    def main(self):
        asyncio.run(self.amain())


# 条件
class Tutorial05:
    """
    asyncio.Condition 是一个协同的条件变量，用于协同程序之间的同步。它允许多个协同程序等待某个条件的满足，然后再继续执行。
    使用场景：
    当多个协同程序需要等待某个条件被设置时，asyncio.Condition 可以帮助协调它们的执行。
    一个协同程序可以通过 condition.notify() 来通知其他等待中的协同程序条件已经满足。
    主要方法：
    await condition.acquire()：获取条件的锁，用于在执行条件等待或通知之前确保同步访问。
    await condition.wait()：等待条件的满足，释放锁并挂起协同程序，直到另一个协同程序调用 notify() 或 notify_all()。
    condition.notify(n=1)：通知 n 个等待的协同程序（默认是 1 个），条件已经满足。
    condition.notify_all()：通知所有等待的协同程序条件已满足。
    condition.release()：释放锁。
    """
    data = None

    async def produce(self, item, condition):
        # 获取条件锁
        async with condition:
            self.data = item
            print(f"生产: {item}")
            # 通知等待的消费者
            condition.notify_all()

    async def consume(self, condition):
        # 获取条件锁
        async with condition:
            # 等待直到数据可用
            while self.data is None:
                print("等待消费")
                await condition.wait()

            # 消费数据
            item = self.data
            print(f"消费: {item}")
            self.data = None
            return item

    async def amain(self):
        condition = asyncio.Condition()

        # 创建生产者和消费者任务
        producer_task = asyncio.create_task(self.produce("item1", condition))
        consumer_task = asyncio.create_task(self.consume(condition))

        await producer_task
        await consumer_task

    def main(self):
        asyncio.run(self.amain())


# 队列
class Tutorial06:
    """
    asyncio.Queue 是 asyncio 模块中的一个异步队列，用于协程之间的通信和数据传递。它是线程安全的，并且可以在异步编程中用于协调生产者和消费者任务。

    主要特性：
    先进先出 (FIFO)：Queue 按照先进先出的顺序处理任务或数据项。
    协程间通信：多个生产者和消费者协程可以通过 Queue 进行数据共享和同步。
    容量限制：可以指定队列的最大容量，如果达到容量限制，生产者协程将会等待直到队列中有空位。
    使用场景：
    生产者-消费者模型：生产者协程将任务或数据放入队列，消费者协程从队列中获取数据并处理。
    任务调度：可以用 Queue 来存储待处理的任务，并控制任务的处理顺序。
    主要方法：
    await queue.put(item)：将 item 放入队列。如果队列满了，协程会等待直到有空位。
    await queue.get()：从队列中获取一个项目。如果队列为空，协程会等待直到有新项目被放入。
    queue.qsize()：返回队列中的项目数量。
    queue.empty()：如果队列为空，返回 True。
    queue.full()：如果队列满了，返回 True。
    """
    data = None

    async def produce(self, queue, n):
        """生产者协程，向队列中放入数据"""
        for i in range(n):
            await asyncio.sleep(random.uniform(0.1, 1))  # 模拟生产时间
            item = f'item {i}'
            await queue.put(item)  # 将数据放入队列
            print(f'Produced {item}')
        await queue.put(None)  # 发送结束信号（终止消费者）

    async def consume(self, queue):
        while True:
            item = await queue.get()  # 获取队列中的数据
            if item is None:  # 检查结束信号
                break
            print(f'Consumed {item}')
            await asyncio.sleep(random.uniform(0.1, 1))  # 模拟消费时间
        print('Consumer done')

    async def amain(self):
        # queue = asyncio.Queue()
        queue = asyncio.Queue(maxsize=3)  # 限制队列容量为3
        # 创建生产者和消费者任务
        producer_task = asyncio.create_task(self.produce(queue, 10))
        consumer_task = asyncio.create_task(self.consume(queue))

        await producer_task
        await consumer_task

    def main(self):
        asyncio.run(self.amain())


# 队列
class Tutorial07:
    """
    queue.task_done()：消费者在处理完一个任务后调用，告知队列任务已完成。
    queue.join()：生产者调用，等待队列中的所有任务都被标记为完成（即所有任务都调用了 task_done()）。
    """
    data = None

    async def produce(self, queue, n):
        """生产者协程，向队列中放入数据"""
        for i in range(n):
            await asyncio.sleep(random.uniform(0.1, 1))  # 模拟生产时间
            item = f'item {i}'
            await queue.put(item)  # 将数据放入队列
            print(f'Produced {item}')
        await queue.put(None)  # 发送结束信号（终止消费者）

    async def consume(self, queue):
        while True:
            item = await queue.get()  # 获取队列中的数据
            if item is None:  # 检查结束信号
                break
            print(f'Consumed {item}')
            await asyncio.sleep(random.uniform(0.1, 1))  # 模拟消费时间
        print('Consumer done')
        queue.task_done() # 标记任务完成

    async def amain(self):
        queue = asyncio.Queue()
        # 创建生产者和消费者任务
        producer_task = asyncio.create_task(self.produce(queue, 10))
        consumer_task = asyncio.create_task(self.consume(queue))

        await producer_task
        await queue.join()  # 等待队列中的所有任务都被处理（消费者调用task_done）

    def main(self):
        asyncio.run(self.amain())


if __name__ == '__main__':
    # t1 = Tutorial01()
    # t1.main()
    #
    # t2 = Tutorial02()
    # t2.main()

    # t3 = Tutorial03()
    # t3.main()

    # t4 = Tutorial04()
    # t4.main()

    # t5 = Tutorial05()
    # t5.main()
    #
    # t6 = Tutorial06()
    # t6.main()

    t7 = Tutorial07()
    t7.main()
