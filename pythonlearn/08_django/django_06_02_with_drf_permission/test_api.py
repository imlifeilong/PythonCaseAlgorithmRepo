import requests


class TestApi:
    def __init__(self):
        self.session = requests.Session()

    def login(self, username, password):
        response = self.session.post(
            url="http://127.0.0.1:8888/auth/",
            data={
                "username": username,
                "password": password,
            }
        )
        print(response.text)
        self.token = response.json().get("token")
        # self.token = ""

    def get_common_book(self):
        response = self.session.get(
            url=f"http://127.0.0.1:8888/common/?token={self.token}",
        )
        print(response.text)

    def get_vip_book(self):
        response = self.session.get(
            url=f"http://127.0.0.1:8888/vip/?token={self.token}",
        )
        print(response.text)

    def get_svip_book(self):
        response = self.session.get(
            url=f"http://127.0.0.1:8888/svip/?token={self.token}",
        )
        print(response.text)

    def main(self):
        username = "admin"
        password = "admin"

        # username = "root"
        # password = "root"

        # username = "lifeilong"
        # password = "lifeilong"

        for username, password in (
                ("admin", "admin"),
                ("root", "root"),
                ("lifeilong", "lifeilong"),
        ):

            self.login(username, password)
            self.get_common_book()
            self.get_vip_book()
            self.get_svip_book()


if __name__ == '__main__':
    ta = TestApi()
    ta.main()
