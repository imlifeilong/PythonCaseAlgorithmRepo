import requests
import json
import random
import time
import threading


class Crawlab:
    def __init__(self):
        self.session = requests.Session()
        self.max_count = 50

    def crawl(self, page=1):
        """
        爬取任务
        :param page:
        :return:
        """
        response = self.session.get(
            url=f'https://bbs.tianya.cn/api',
            params={
                'method': 'bbs.ice.getHotArticleList',
                'params.pageSize': '40',
                'params.pageNum': page,
                'var': 'apiData',
                '_r': random.random(),
                '_': round(time.time() * 1000),

            },
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
        )
        print(f"线程名：{threading.current_thread().name}, 页码：{page}, 结果：{response}")
        return response

    def parse(self, response):
        """
        解析任务
        :param response:
        :return:
        """
        print(f"线程名：{threading.current_thread().name}")
        data = response.text[14:]
        result = json.loads(data)
        for row in result.get('data', {}).get('rows', []):
            title = row.get('title', '')
            url = row.get('url', '')
            print(title, url)


if __name__ == '__main__':
    cl = Crawlab()
    response = cl.crawl()
    cl.parse(response)
