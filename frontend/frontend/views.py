import requests
from django.shortcuts import render
from . import default

root_url= default.root_url
api_url = default.api_url


def home(request):
    category_response = requests.get(root_url+api_url+"categorys/")
    if category_response.status_code is not 200:
        return render(request,'home.html',data=dict())

    products_response = requests.get(root_url + api_url + "products/main/")

    if products_response.status_code is not 200:
        return render(request,'home.html',data=dict())

    data = {
        "shop_name":"AWESOME SHOP",
        "categorys": category_response.json()["data"],
        "products" : products_response.json()["data"]
    }
    return render(request,'home.html', data)