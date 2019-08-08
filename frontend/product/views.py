import json

import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View
import frontend.default as default

root_url = default.root_url
api_url = default.api_url


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
        cart = {
            'user': 1,
            'product': pk,
            "amount": request.POST['amount']
        }
        headers = {'Content-Type': 'application/json; charset=utf-8'}

        if 'buy-btn' in request.POST:
            pass

        if 'cart-btn' in request.POST:
            cart_response = requests.post(root_url + api_url + "carts/user/1", headers=headers, data=json.dumps(cart))
            if cart_response.status_code is not 201:
                return HttpResponseRedirect(reverse("product:detail", args=pk))
            return HttpResponseRedirect(reverse("user:cart"))
