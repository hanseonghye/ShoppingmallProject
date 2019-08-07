import json

import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View, TemplateView

from frontend import default

root_url= default.root_url
api_url = default.api_url
header = default.headers


class LoginView(View):
    def get(self, request):
        response = requests.get(root_url + api_url + "categorys/")
        if response.status_code is not 200:
            return render(request, 'home.html',dict())

        data = {
            "shop_name": "AWESOME SHOP",
            "categorys": response.json()["data"]
        }
        return render(request, 'user/login.html', data)

    def post(self, request):
        user = {
            'user_id':request.POST['member_id'],
            'password':request.POST['member_password']
        }

        login_response=requests.post(root_url+api_url+"users/login/", headers=header, data=user)

        if login_response.status_code is not 200 :
            return HttpResponseRedirect(reverse("user:login"))

        request.session['authuser'] = login_response.json()['data']

        return HttpResponseRedirect(reverse('home'))


class JoinView(View):
    def get(self, request):
        response = requests.get(root_url + api_url + "categorys/")
        if response.status_code is not 200:
            return render(request, 'home.html', dict())

        data = {
            "shop_name": "AWESOME SHOP",
            "categorys": response.json()['data']
        }
        return render(request, 'user/join.html', data)

    def post(selfs, request):
        response = requests.get(root_url + api_url + "categorys/")
        if response.status_code is not 200:
            return render(request, 'home.html', dict())

        data = {
            "shop_name": "AWESOME SHOP",
            "categorys": response.json()['data']
        }
        user={
            'user_id':request.POST['user_id'],
            'password':request.POST['password'],
            'username':request.POST['username'],
            'email':request.POST['email'],
            'phone_number':request.POST['phone']
        }
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(root_url + api_url + "users/",headers=headers, data=json.dumps(user))
        if response.status_code is not 201:
            print(response.json())
            return render(request, 'home.html', data)

        print(response.json()['data'])
        return render(request, 'user/join.html', data)

class CartView(TemplateView):
    template_name = 'user/cart.html'
    def get_context_data(self, **kwargs):
        default.set_base_data()
        data = default.base_data

        return data