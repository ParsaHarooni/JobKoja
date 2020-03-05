import requests

BASE_URL = "https://jobinja.ir"


class Request:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'})

    def get_request(self, url='', data=None):
        resp = self.session.get(BASE_URL + url, data=data)
        return resp.status_code, resp.content

    def post_request(self, url=None, data=None):
        resp = self.session.post(BASE_URL + url, data=data)
        return resp.status_code, resp.content

    def check_connection(self):
        resp = self.session.get(BASE_URL)
        return resp.status_code == 200
