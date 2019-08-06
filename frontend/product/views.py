import requests
from django.shortcuts import render
from django.views.generic.base import View
import frontend.default as default

root_url= default.root_url
api_url = default.api_url

class ProductDV(View):
    def get(self, request, pk):
        category_response = requests.get(root_url + api_url + "categorys/")
        if category_response.status_code is not 200:
            return render(request, 'home.html', data=dict())
        product_response = requests.get(root_url+api_url+"products/"+pk)

        if product_response.status_code is not 200 :
            return render(requests,'home.html',data=dict())

        data = {
            "shop_name":"AWESOME SHOP",
            "categorys": category_response.json()["data"],
            "product" : product_response.json()["data"]
        }

        print(product_response.json()['data'])

        return render(request, 'product/detail.html', data)

