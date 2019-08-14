import json
from urllib.parse import urlparse

import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.base import View
import frontend.default as default
from product.forms import OrderForm

root_url = default.root_url
api_url = default.api_url
header = default.headers


class ProductDV(View):
    def get(self, request, pk):
        default.set_base_data()
        product_response = requests.get(root_url + api_url + "products/" + pk)
        if product_response.status_code is not 200:
            return render(requests, 'home.html', data=dict())
        data = default.base_data
        data['product'] = product_response.json()["data"]

        return render(request, 'product/detail.html', data)

    def post(self, request, pk):

        if 'buy-btn' in request.POST:
            if 'authuser' in request.session:
                response = requests.get(root_url + api_url + "products/" + pk)
                product = response.json()['data']
                data = {
                    "order_products": [
                        {
                            'product': product,
                            'amount': request.POST['amount'],
                            'all_price': int(product['price']) * int(request.POST['amount'])
                        },
                    ]
                }

                return render(request, 'order.html', data)

        if 'cart-btn' in request.POST:
            if 'authuser' in request.session:
                cart = {
                    'user': request.session['authuser']['pk'],
                    'product': pk,
                    "amount": request.POST['amount']
                }
                headers = {'Content-Type': 'application/json; charset=utf-8'}
                cart_response = requests.post(
                    root_url + api_url + "carts/user/" + str(request.session['authuser']['pk']) + "/add/",
                    headers=headers,
                    data=json.dumps(cart))
                if cart_response.status_code is 201:
                    return HttpResponseRedirect(reverse("user:cart"))
        return HttpResponseRedirect(reverse("product:detail", args=pk))


class OrderView(View):
    def post(self, request):
        product_pk = request.POST.getlist('pk')
        product_amount = request.POST.getlist('amount')
        cart_data = [{'product': product, 'amount': amount} for product, amount in zip(product_pk, product_amount)]

        order = {'user': request.session['authuser']['pk'],
                 'sender_name': request.POST['sender_name'],
                 'sender_email': request.POST['sender_email'],
                 'sender_phone_number': request.POST['sender_phone_number'],
                 'receiver_name': request.POST['receiver_name'],
                 'receiver_phone_number': request.POST['receiver_phone_number'],
                 'receiver_address': request.POST['receiver_address'],
                 'pay_type': request.POST['pay_type'],
                 'delivery_message': request.POST.get('delivery_message', ''),
                 'order_products': cart_data
                 }

        header = {'Content-Type': 'application/json; charset=utf-8'}
        requests.post(root_url + api_url + "orders/", headers=header, data=json.dumps(order))

        previous_url = self.request.META.get('HTTP_REFERER')
        if 'cart' in urlparse(previous_url).path:
            for pk in request.POST.getlist('cart_pk'):
                requests.delete(root_url+api_url+f'carts/user/{request.session["authuser"]["pk"]}/{pk}')


        return render(request, 'home.html')
