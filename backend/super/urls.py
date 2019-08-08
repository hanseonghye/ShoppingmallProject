from django.urls import path

from .views import login

app_name = 'super'

urlpatterns = [
    path('login/', login, name='login'),
]
