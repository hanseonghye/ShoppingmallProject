from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

# Create your views here.
from users.forms import CreateUserForm


class UserCreateTV(CreateView):
    template_name = 'registration/register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('register_done')


class UserCreateDonwTV(TemplateView):
    template_name = 'registration/register_done.html'

