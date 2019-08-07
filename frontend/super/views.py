import requests
from django.shortcuts import render
from django.views.generic import TemplateView, View

from frontend import default

root_url = default.root_url
api_url = default.api_url


class MemberLV(TemplateView):
    template_name = 'super/member.html'

    def get_context_data(self, **kwargs):
        response = requests.get(root_url + api_url + "admin/users/")
        if response.status_code is not 200:
            return dict()
        data = dict()
        data['members']=response.json()['data']
        return data



class LoginView(View):
    def get(self, request):
        return render(request,'super/login.html')

    def post(self, request):
        print(request.POST)
        return render(request, 'user/login.html')