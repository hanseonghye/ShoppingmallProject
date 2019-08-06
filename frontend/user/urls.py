from django.urls import path

from .views import *

app_name='user'

urlpatterns=[
    path('login/', LoginView.as_view(), name='login'),
    path('join/', JoinView.as_view(), name='join'),
]