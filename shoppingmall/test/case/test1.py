from django.test import TestCase, Client


class Test01(TestCase):
    c = Client()
    response = c.get('/member/api/login/')
    print(response.content)

    # response = c.post("/account/api/signup/", data={
    #     'name':'hans',
    #     'id':'user1',
    #     'password':'passw0rd'
    # })
    #
    # print(response.content)
