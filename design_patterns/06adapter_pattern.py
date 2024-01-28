"""
适配器模式是一种结构型设计模式，它允许接口不兼容的对象进行合作。适配器模式允许将已存在的类的接口转换为客户端所期望的接口，以解决不同接口之间的不匹配问题。这使得原本由于接口不兼容而不能在一起工作的类可以一起工作。

适配器模式涉及三个主要角色：

目标接口（Target）：客户端所期望的接口，适配器模式通过适配器将已存在的接口转换为目标接口。

适配器（Adapter）：负责将已存在的接口转换为目标接口，使得客户端可以调用目标接口。

被适配者（Adaptee）：已存在的接口，需要被适配成目标接口。

优点：
解决接口不兼容问题：适配器模式能够解决由于不同接口而导致的系统组件之间的不兼容问题，使得它们可以协同工作。

复用已有功能：适配器模式可以复用已有的类，无需修改其源代码，仅通过适配器进行接口转换。

灵活性：通过适配器，可以灵活地增加、替换或排除已有的组件，而不影响客户端代码。

缺点：
增加复杂性：引入适配器模式会增加系统的复杂性，因为需要增加额外的适配器类。

可能降低性能：适配器模式可能引入一些性能损耗，特别是在处理大量数据时。

适用场景：
需要复用已有的类：当已有的类的接口与系统要求的接口不一致时，适配器模式可以用于复用已有的类。

与第三方库或组件集成：当需要将系统与第三方库或组件集成，但它们的接口不匹配时，适配器模式可以用于将它们协同工作。

需要替换已有的组件：当需要替换已有的组件，并且新组件的接口与原组件不一致时，适配器模式可以用于无缝替换

"""


# 适配器
class Target:
    def send(self):
        pass

    def close(self):
        pass


# 被适配的对象
class HttpAdaptee:
    def __init__(self, url):
        self.url = url

    def get(self):
        print("请求加密数据")
        print("组装HTTP协议")
        print(f"发送HTTP GET请求 {self.url}")

    def disconnect(self):
        print("断开链接")


# 被适配的对象
class FileAdaptee:
    def __init__(self, url):
        self.url = url

    def download(self):
        print("连接file服务器")
        print(f"下载文件 {self.url}")

    def disconnect(self):
        print("文件下载完成，断开服务器")

    def close_file(self):
        print("关闭文件句柄")


# 进行适配
class HttpAdapter(Target):
    def __init__(self, url):
        self.http = HttpAdaptee(url)

    def send(self):
        return self.http.get()

    def close(self):
        return self.http.disconnect()


class FileAdapter(Target):
    def __init__(self, url):
        self.file = FileAdaptee(url)

    def send(self):
        return self.file.download()

    def close(self):
        self.file.disconnect()
        self.file.close_file()


# 客户端
class Client:
    def get_adapter(self, url: str):
        """
        获取适配器
        :param url:
        :return:
        """
        if url.startswith('http'):
            return HttpAdapter(url)
        if url.startswith('file'):
            return FileAdapter(url)

    def main(self, url):
        adapter = self.get_adapter(url)
        adapter.send()
        adapter.close()


if __name__ == "__main__":
    client = Client()
    file_url = 'file:127.0.0.1:2020/home.mp4'
    client.main(file_url)
    http_url = 'http://127.0.0.1:8080/index.html'
    client.main(http_url)
