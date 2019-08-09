import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, View

from frontend import default

root_url= default.root_url
api_url = default.api_url
header = default.headers

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
        response = requests.post(root_url+api_url+'super/login/', headers=header, data=super)
        if response.status_code is not 200 :
            return HttpResponseRedirect(reverse("super:login"))

        request.session['superuser'] = response.json()['data']

        return render(request, 'super/home.html')


class Logout(View):
    def get(self, request):
        del request.session['superuser']
        return HttpResponseRedirect(reverse('super:login'))


class Home(View):
    def get(self, request):
        if 'superuser' in request.session:
            return render(request,'super/home.html')
        return HttpResponseRedirect(reverse("super:login"))
