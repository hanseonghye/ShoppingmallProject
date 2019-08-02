from django.urls import path

from .views import CartLV, CartDV, NonUserCartLV, NonUserCartDV

app_name = 'cart'

urlpatterns = [
    path('user/<int:pk>', CartLV.as_view(), name='list'),
    path('user/<int:pk>/<int:cartpk>', CartDV.as_view(), name='detail'),

    path('nonuser/<int:pk>', NonUserCartLV.as_view(), name='nonuser-list'),
    path('nonuser/<int:pk>/<int:cartpk>', NonUserCartDV.as_view(), name='nonuser-detail'),
]
