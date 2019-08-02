import json

from django.test import TestCase


class TestUser(TestCase):
    setup_done = False

    def setUp(self):
        if TestUser.setup_done:
            return
        TestUser.setup_done = True
        # todo something

    def test_userID로_회원검색(self):
        self.client.post('/api/v1/users/',
                         {"username": "한성혜", "user_id": "searchId", "password": "dfsdfs!!",
                          "email": "hans12312@naver.com",
                          "phone_number": "01072163428"})
        response = self.client.get('/api/v1/users/searchId/')
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)
        self.assertEqual(json_response['result'], 'success')
        self.assertEqual(json_response['data']['user_id'], "searchId")

    def test_회원가입_성공(self):
        response = self.client.post('/api/v1/users/',
                                    {"username": "한성혜", "user_id": "test_1", "password": "ffdfsaa@!",
                                     "email": "hans12312@naver.com",
                                     "phone_number": "01072163428"})

        self.assertEqual(response.status_code, 201)
        json_response = json.loads(response.content)
        self.assertEqual(json_response['result'], 'success')
        self.assertEqual(json_response['data']['username'], "한성혜")

    def test_회원가입_실패(self):
        response = self.client.post('/api/v1/users/',
                                    {"username": "한성혜", "user_id": "test_1", "password": "testdkdk!",
                                     "email": "hans12312",
                                     "phone_number": "01072163428"})

        self.assertEqual(response.status_code, 400)
        json_response = json.loads(response.content)
        self.assertEqual(json_response['result'], 'fail')


    # data값으로 중복 여부 확인할 수 있다.
    def test_이메일중복확인_성공(self):
        response = self.client.get('/api/v1/users/check/email/hans123@naver.com')
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)
        self.assertEqual(json_response['result'], 'success')
        # print(json_response['data'])

    def get_all_user(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)
        print(json_response)
