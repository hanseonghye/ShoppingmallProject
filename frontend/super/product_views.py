import json
import requests
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, View

from frontend import default
from product.models import ProductImage

root_url= default.root_url
api_url = default.api_url
header = default.headers


class ProductUV(View):
    def get(self, request,pk):
        response = requests.get(root_url+api_url+"super/categorys/")
        data = dict()

        if response.status_code is not 200:
            data['categorys'] = []
            return data

        product_response = requests.get(root_url+api_url+"super/products/"+pk)
        if product_response.status_code is not 200 :
            data['product'] = []
            return data

        data['categorys'] = response.json()['data']
        data['product'] = product_response.json()['data']

        return render(request,'super/product-add.html',data)

class ProductDV(View):
    def get(self, request,pk):
        requests.delete(root_url+api_url+"super/products/"+pk)
        return HttpResponseRedirect(reverse("super:product-list"))

class ProductCV(View):
    def get(self, request):
        response = requests.get(root_url+api_url+"super/categorys/")
        data = dict()

        if response.status_code is not 200:
            data['categorys'] = []
            return data

        data['categorys'] = response.json()['data']
        return  render(request, 'super/product-add.html',data)

    def post(self, request):
        pi = ProductImage.objects.create(main=request.FILES['img_main'], content = request.FILES['img_content'])
        print(request.POST)
        product = {
            'name':request.POST['name'],
            'price':request.POST['price'],
            'description':request.POST['description'],
            'image_url':settings.MEDIA_URL+pi.main.name,
            'file_url':settings.MEDIA_URL+pi.content.name,
            'category':request.POST['category'],
            'is_stock' : True if 'is_stock' in request.POST else False,
            'is_option' : True if 'is_option' in request.POST else False,
            'is_display' : True if 'is_display' in request.POST else False,
            'product_options':request.POST['product_options']
        }

        headers = {'Content-Type': 'application/json; charset=utf-8'}
        product_response = requests.post(root_url+api_url+"super/products/add/",headers=headers,data=json.dumps(product))
        if product_response.status_code is not 201 :
            print(product_response.json())
        return HttpResponseRedirect(reverse("super:product-add"))


class ProductLV(TemplateView):
    template_name = 'super/product-list.html'

    def get_context_data(self, **kwargs):
        response = requests.get(root_url+api_url+"super/products/")
        data = dict()

        if response.status_code is not 200:
            data['products'] = []
            return data

        data['products'] = response.json()['data']
        return data