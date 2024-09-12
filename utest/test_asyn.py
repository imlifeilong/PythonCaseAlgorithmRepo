import time
import threading
from concurrent.futures import ThreadPoolExecutor

class MyFutureWithEvent:
    def __init__(self):
        self._result = None
        self._done_event = threading.Event()
        self._exception = None

    def set_result(self, result):
        """ 设置结果，并标记为已完成 """
        self._result = result
        self._done_event.set()  # 通知所有等待的线程，任务已经完成

    def set_exception(self, exception):
        """ 设置异常，并标记为已完成 """
        self._exception = exception
        self._done_event.set()  # 通知所有等待的线程，任务已经完成

    def result(self):
        """ 获取结果，如果未完成则阻塞等待 """
        self._done_event.wait()  # 等待任务完成
        if self._exception:
            raise self._exception  # 如果有异常，则抛出异常
        return self._result

    def done(self):
        """ 返回 Future 是否已完成 """
        return self._done_event.is_set()


def background_work(future):
    try:
        # 模拟耗时操作
        time.sleep(2)
        if time.time() % 2 == 0:  # 模拟偶尔发生的异常
            raise ValueError("An error occurred during the operation")
        future.set_result("Operation completed")
    except Exception as e:
        future.set_exception(e)


# 创建自定义 Future 对象
my_future = MyFutureWithEvent()

# 在后台线程中执行异步操作
thread = threading.Thread(target=background_work, args=(my_future,))
thread.start()

# 主线程等待结果
print("Waiting for result...")
try:
    result = my_future.result()
    print(f"Result: {result}")
except Exception as e:
    print(f"Caught exception: {e}")
