import json

import requests
from django.shortcuts import render
from django.views.generic import View

from frontend import default

root_url= default.root_url
api_url = default.api_url

class LoginView(View):
    def get(self, request):
        response = requests.get(root_url + api_url + "categorys/")
        if response.status_code is not 200:
            return render(request, 'home.html', data=dict())

        data = {
            "shop_name": "AWESOME SHOP",
            "categorys": response.json()["data"]
        }
        return render(request, 'user/login.html', data)

    def post(self, request):
        response = requests.get(root_url + api_url + "categorys/")
        if response.status_code is not 200:
            return render(request, 'home.html', data=dict())
        data = {
            "shop_name": "AWESOME SHOP",
            "categorys": response.json()["data"]
        }

        user = {
            'user_id':request.POST['member_id'],
            'password':request.POST['member_password']
        }
        response=requests.post(root_url+api_url+"users/login/", data=json.dumps(user))
        print(response.json())
        return render(request, 'home.html',data)

class JoinView(View):
    def get(self, request):
        # response = requests.get(root_url + api_url + "categorys/")
        # if response.status_code is not 200:
        #     return render(request, 'home.html', data=dict())

        data = {
            "shop_name": "AWESOME SHOP",
            "categorys": []
        }
        return render(request, 'user/join.html', data)

    def post(selfs, request):
        pass