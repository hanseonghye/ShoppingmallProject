from django.urls import path

from .views import *

app_name='user'

urlpatterns=[
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('join/', JoinView.as_view(), name='join'),
    path('checkid/<check_id>/', check_id, name='check_id'),
    path('cart/', CartView.as_view(), name='cart'),
    path('order/', order, name='order'),
]
