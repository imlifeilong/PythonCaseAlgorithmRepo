import threading
import time

def daemon_function():
    """守护线程的任务"""
    while True:
        print("Daemon thread is running...")
        time.sleep(2)
        print("Daemon thread is exiting...")

# 创建守护线程
daemon_thread = threading.Thread(target=daemon_function)
daemon_thread.daemon = True  # 将线程设置为守护线程

# 启动线程
daemon_thread.start()

print("Main thread is exiting... 3s time")
time.sleep(3)