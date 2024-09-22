import json
import time
import uuid
import threading
import websocket
from concurrent.futures import Future
from queue import Queue


class WebSocketClient:
    def __init__(self, uri):
        self.uri = uri
        self.futures = {}  # 存储消息ID与Future对象的映射
        self.lock = threading.Lock()  # 用于多线程安全访问futures
        self.queue = Queue()  # 用于从接收线程中传递消息
        self.ws = None  # WebSocket连接对象

    def connect(self):
        # 开启追踪日志
        websocket.enableTrace(True)
        # 创建WebSocket连接
        self.ws = websocket.WebSocketApp(self.uri,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)

        # 启动接收消息的线程
        self.receive_thread = threading.Thread(target=self.ws.run_forever, kwargs={'ping_interval': 60})
        self.receive_thread.daemon = True
        self.receive_thread.start()

    def send_message(self, message):
        # 生成唯一的消息ID
        message_id = str(uuid.uuid4())
        message_with_id = json.dumps({
            'id': message_id,
            'data': message
        })

        # 创建一个Future对象并存储它
        future = Future()
        with self.lock:
            self.futures[message_id] = future

        # 发送消息
        self.ws.send(message_with_id)

        # 返回Future对象
        return future

    def on_message(self, ws, message):
        # 接收到消息时，解析消息并提取ID
        data = json.loads(message)
        message_id = data.get('id')

        # 根据消息ID查找对应的Future对象
        with self.lock:
            if message_id in self.futures:
                future = self.futures.pop(message_id)
                if not future.done():
                    # 设置Future的结果
                    future.set_result(data.get('data'))

    def on_error(self, ws, error):
        print(f"WebSocket error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print(f"WebSocket closed: {close_msg}")

    def close(self):
        # 关闭WebSocket连接
        if self.ws:
            self.ws.close()
        if self.receive_thread:
            self.receive_thread.join()


# 测试客户端
def test_client():
    ws_client = WebSocketClient('ws://localhost:8765')  # 替换成实际WebSocket地址
    ws_client.connect()
    time.sleep(2)
    while True:
        # try:
        # 发送消息并等待响应
        future = ws_client.send_message({'action': 'ping'})
        response = future.result()  # 阻塞等待服务器的响应
        print(f"Received response: {response}")
    # except Exception as e:
    #     print("error", e)
    # time.sleep(1)

    # 关闭WebSocket客户端
    ws_client.close()


# 启动测试
if __name__ == "__main__":
    test_client()
