from django.urls import path

from product.views import ProductRV

app_name = 'product'

urlpatterns = [
    path('<int:pk>/', ProductRV.as_view(), name='detail'),
]
