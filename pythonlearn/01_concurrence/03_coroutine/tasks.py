import asyncio
import time
import utils
import requests


@utils.runtime
def io_task(url="https://www.baidu.com"):
    response = requests.get(url)
    print(response.status_code)
    return response


async def long_running_task():
    # 模拟一个耗时的异步任务
    print('任务开始...')
    await asyncio.sleep(10)  # 假设这里有一些耗时的IO操作
    print('任务结束')
    return '结果'


@utils.runtime
def cpu_task(total=100000000):
    """
    CPU密集型任务
    :return:
    """
    count = 0
    for i in range(total):
        count += 1
    return count


@utils.aruntime
async def acpu_task(total=100000000):
    """
    CPU密集型任务
    :return:
    """
    count = 0
    for i in range(total):
        count += 1
    return count


def callback(name):
    print(f"{int(time.time())} start callback {name}")
    time.sleep(1)
    print(f'{int(time.time())} over callback {name}')


def block_task(name):
    print(f'start block task {name}')
    time.sleep(3)
    print(f'over block task {name}')
    return f'block task result {name}'


async def get(name: str, timeout: int):
    """模拟请求数据接口"""
    print(f"get start {name}")
    await asyncio.sleep(timeout)
    print(f"get over {name}")

    return f"get {name} result"


async def post(name: str, timeout: int):
    """模拟请求数据接口"""
    print(f"post start {name}")
    await asyncio.sleep(timeout)
    print(f"post over {name}")

    return f"post {name} result"
