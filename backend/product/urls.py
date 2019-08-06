from django.urls import path

from .views import ProductRV, ProductLV

app_name = 'product'

urlpatterns = [
    path('<int:pk>/', ProductRV.as_view(), name='detail'),
    path('main/', ProductLV.as_view(), name='main-list'),
]
