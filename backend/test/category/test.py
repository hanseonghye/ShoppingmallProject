import json

from django.test import TestCase


class TestCategory(TestCase):

    def test_카테고리추가_성공(self):
        response = self.client.post('/api/v1/super/categorys/',
                                    {"name": "상의"})

        self.assertEqual(response.status_code, 201)
        json_response = json.loads(response.content)
        self.assertEqual(json_response['result'], 'success')
        self.assertEqual(json_response['data']['name'], '상의')
