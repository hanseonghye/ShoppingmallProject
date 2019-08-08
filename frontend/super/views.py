import json
import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, View

from frontend import default

root_url= default.root_url
api_url = default.api_url
header = default.headers

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
        product = {
            'name':request.POST['name'],
            'price':request.POST['price'],
            'image_url':request.POST['image_url'],
            'file_url':request.POST['file_url'],
            'category':request.POST['category'],
            'is_stock' : True if 'is_stock' in request.POST else False,
            'is_option' : True if 'is_option' in request.POST else False,
            'is_display' : True if 'is_display' in request.POST else False,
            'product_options':[]
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

class MemberLV(TemplateView):
    template_name = 'super/member-list.html'

    def get_context_data(self, **kwargs):
        response = requests.get(root_url + api_url + "super/users/")
        data = dict()
        if response.status_code is not 200:
            data['members'] = []
            return data

        data['members']=response.json()['data']
        return data



class LoginView(View):
    def get(self, request):
        return render(request,'super/login.html')

    def post(self, request):
        super = {
            'user_id':request.POST['user_id'],
            'password':request.POST['password']
        }
        print(super)
        response = requests.post(root_url+api_url+'super/login/', headers=header, data=super)
        if response.status_code is not 200 :
            return HttpResponseRedirect(reverse("super:login"))

        print(response.json())
        return render(request, 'super/home.html')

class Home(TemplateView):
    template_name = 'super/home.html'