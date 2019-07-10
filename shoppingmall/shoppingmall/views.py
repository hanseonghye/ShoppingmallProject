from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


class Homeview(TemplateView):
    template_name = 'home.html'


class UserCreateTV(CreateView):
    # template_name = 'registraion/register.html'
    form_class = UserCreationForm
    # success_url = reverse_lazy('register_done')

    def get(self, request, *args, **kwargs):
        print(request.GET['name'])
        return HttpResponse('hello')