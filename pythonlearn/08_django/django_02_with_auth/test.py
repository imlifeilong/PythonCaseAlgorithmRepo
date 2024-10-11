import requests
import json


def test_api():
    url = 'http://127.0.0.1:8888/api/token-auth/'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "Content-Type": "application/json"
    }
    data = {
        "username": "admin",
        "password": "123"
    }
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    # print(r.headers)
    print(r.text)

    token = r.json().get("token")
    url = 'http://127.0.0.1:8888/api/protected/'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "Authorization": f"JWT {token}"
    }
    print(headers)
    r = requests.get(url=url, headers=headers)
    print(r.text)


if __name__ == '__main__':
    test_api()
