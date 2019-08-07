import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView

from . import default

root_url= default.root_url
api_url = default.api_url


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        default.set_base_data()
        data = default.base_data
        products_response = requests.get(root_url + api_url + "products/main/")
        if products_response.status_code is not 200:
            return dict()
        data['products'] = products_response.json()["data"]

        return data

class CategoryView(TemplateView):
    template_name = 'product/list.html'

    def get_context_data(self, **kwargs):
        default.set_base_data()
        data=default.base_data

        categoryProduct_response = requests.get(root_url+api_url+"categorys/"+kwargs['pk'])

        if categoryProduct_response.status_code is not 200:
            return dict()
        data['products'] = categoryProduct_response.json()['data']
        friend_category_response = requests.get(root_url+api_url+"categorys/"+kwargs['pk']+"/friend/")
        if friend_category_response.status_code is not 200:
            return dict()
        data['child_categorys'] = friend_category_response.json()['data']['child_categorys'][0]['category_child'];
        data['choice_category'] = friend_category_response.json()['data']['choice_category']

        return data
