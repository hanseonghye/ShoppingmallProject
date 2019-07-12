import json

from django.test import TestCase, Client


class TestMember(TestCase):

    def test_회원가입_실패(self):
        response = self.client.post('/member/api/member/signup/',
                                    {"name": "", "id": "hans", "password": "passw0rd"})
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)
        self.assertEqual(json_response['status'], True)
        self.assertEqual(json_response['result'], 'fail')

    def test_회원가입_성공(self):
        response = self.client.post('/member/api/member/signup/',
                                    {"name": "hanseonghye", "id": "hans", "password": "passw0rd"})
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)
        self.assertEqual(json_response['status'], True)
        self.assertEqual(json_response['result'], 'success')
        self.assertEqual(json_response['data']['name'], "hanseonghye")

    def test_회원가입_아이디중복체크_성공(self):
        response = self.client.get('/member/api/member/checkid/', {'id': 'user1'})
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)
        self.assertEqual(json_response['status'], True)
        self.assertEqual(json_response['result'], 'success')
