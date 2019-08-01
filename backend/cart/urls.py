from django.urls import path

from .views import CartLV, CartDV

app_name = 'cart'

urlpatterns = [
    path('user/<int:pk>', CartLV.as_view(), name='list'),
    path('user/<int:pk>/<int:cartpk>', CartDV.as_view(), name='detail'),
]
