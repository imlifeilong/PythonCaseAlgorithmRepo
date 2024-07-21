import requests


class GS:
    def __init__(self):
        self.session = requests.Session()

    def crawl(self):
        r = self.session.get(
            url="http://qywh1.com/qywhyinpin2/gushi/json/gushi.json",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            }
        )
        # print(r.text)
        result = r.json()
        for row in result.get("data", {}).get("video1", []):
            print(row)

            url = f"http://qywh1.com/qywhyinpin2/gushi{row.get('src')[1:]}"
            print(url)
            r = self.session.get(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            })
            name = f"{row.get('id')}_{row.get('name')}.mp3"
            with open(name, 'wb') as f:
                f.write(r.content)


if __name__ == '__main__':
    gs = GS()
    gs.crawl()
