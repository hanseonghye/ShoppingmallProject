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


class CategoryLV(TemplateView):
    template_name = 'super/category-list.html'

    def get_context_data(self, **kwargs):
        response = requests.get(root_url + api_url + "super/categorys/")
        data = dict()

        if response.status_code is not 200:
            data['categorys'] = []
            return data

        data['categorys'] = response.json()['data']
        return data

class CategoryCV(View):
    def get(self, request):
        data= dict()
        data['categorys'] = []
        category_response = requests.get(root_url + api_url + "super/categorys/")
        if category_response.status_code is 200:
            data["categorys"] = category_response.json()['data']
        return render(request,'super/categroy-add.html', data)

    def post(self, request):

        category = {
            "name" : request.POST['name'],
            "parent" : request.POST['parent'],
            "priority" : request.POST['priority']
        }

        headers = {'Content-Type': 'application/json; charset=utf-8'}
        requests.post(root_url+api_url+"super/categorys/", headers=headers, data= json.dumpb(category))
        return HttpResponseRedirect(reverse("super:category-list"))