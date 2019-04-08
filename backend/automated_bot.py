import requests


class UserActivity:
    def __init__(self):
        self.url = 'http://127.0.0.1:8000/'

    def process(self):
        self.register()
        self.login()

    def register(self):
        body = {
            "city": "Kherson",
            "phone": "0991233113",
            "country": "Ukraine",
            "email": "test@test.com",
            "username": "test_user",
            "password": "123qwe1231"
        }
        r = requests.post(self.url + 'registration/', body)

        assert r.status_code == 201

    def login(self):
        body = {
            'username': 'test_user',
            'password': '123qwe1231'
        }
        r = requests.post(self.url + 'auth-jwt/', body)

        assert r.status_code == 200


class PostEndpoint:
    def __init__(self):
        self.url = 'http://127.0.0.1:8000/post-endpoint/'

    def process(self):
        self.create()
        # like post
        self.put()
        # unlike post
        self.put()
        self.delete()

    def create(self):
        body = {
            'user_id': 1,
            'text': 'Test text for creating new post'
        }
        r = requests.post(self.url, body)

    def put(self):
        body = {
            'user_id': 1,
            'post_id': 1
        }
        r = requests.put(self.url, body)

    def delete(self):
        body = {
            'user_id': 1,
            'post_id': 1
        }
        r = requests.delete(self.url, data=body)


if __name__ == '__main__':
    UserActivity().process()
    PostEndpoint().process()
