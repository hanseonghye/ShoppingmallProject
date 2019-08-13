import json

import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View, TemplateView, CreateView, FormView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from frontend import default
from product.forms import OrderForm

root_url = default.root_url
api_url = default.api_url
header = default.headers


class Logout(View):
    def get(self, request):
        del request.session['authuser']
        return HttpResponseRedirect(reverse('home'))


class LoginView(View):
    def get(self, request):
        response = requests.get(root_url + api_url + "categorys/")
        if response.status_code is not 200:
            return render(request, 'home.html', dict())

        data = {
            "shop_name": "AWESOME SHOP",
            "categorys": response.json()["data"]
        }
        return render(request, 'user/login.html', data)

    def post(self, request):
        user = {
            'user_id': request.POST['member_id'],
            'password': request.POST['member_password']
        }

        login_response = requests.post(root_url + api_url + "users/login/", headers=header, data=user)

        if login_response.status_code is not 200:
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
        user = {
            'user_id': request.POST['user_id'],
            'password': request.POST['password'],
            'username': request.POST['username'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone']
        }
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(root_url + api_url + "users/", headers=headers, data=json.dumps(user))
        if response.status_code is not 201:
            return render(request, 'home.html', data)

        return HttpResponseRedirect(reverse('home'))


class CartView(View):

    def get(self, request):
        default.set_base_data()
        data = default.base_data
        data['carts'] = []
        if 'authuser' in request.session:
            response = requests.get(root_url + api_url + "carts/user/" + str(request.session['authuser']['pk']))
            if response.status_code is not 200:
                return render(request, 'user/cart.html', data)

            data['carts'] = response.json()['data']
        else:
            pass

        return render(request, 'user/cart.html', data)

    def post(self, request):
        default.set_base_data()
        data = default.base_data
        product_amount = request.POST.getlist('amount')
        product_check = request.POST.getlist('checks')
        cart_data = []
        for check, amount in zip(product_check, product_amount):
            response = requests.get(root_url + api_url + "products/" + check)
            print(response.json())
            product = response.json()['data']
            temp_data = {
                'product': product,
                'amount': amount,
                'all_price': int(product['price']) * int(amount)
            }
            cart_data.append(temp_data)

        data["order_products"] = cart_data
        return render(request, 'order.html', data)


class OrderView(View):
    def get(self, request):
        default.set_base_data()
        data = default.base_data
        data[''] = []
        if 'authuser' in request.session:
            response = requests.get(root_url + api_url + "orders/user/" + str(request.session['authuser']['pk']))
            if response.status_code is not 200:
                return render(request, 'user/order.html', data)
            data['orders'] = response.json()['data']
        else:
            pass

        return render(request, 'user/order.html', data)


@api_view(['GET'])
def check_id(request, check_id):
    response = requests.get(root_url + api_url + "users/check/id/" + check_id)
    return Response(response.json())
