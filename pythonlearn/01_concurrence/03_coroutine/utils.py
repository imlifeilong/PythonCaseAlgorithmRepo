import typing
import time
import functools


def runtime(function: typing.Callable):
    """
    计算普通函数执行时间
    :param function:
    :return:
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = function(*args, **kwargs)
        end_time = time.perf_counter() - start_time
        print(f"{function.__name__} executed in {end_time:.4f} seconds")

        return result

    return wrapper


def aruntime(function: typing.Callable):
    """
    计算协程函数执行时间
    :param function:
    :return:
    """

    @functools.wraps(function)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await function(*args, **kwargs)
        end_time = time.perf_counter() - start_time
        print(f"{function.__name__} executed in {end_time:.4f} seconds")

        return result

    return wrapper
