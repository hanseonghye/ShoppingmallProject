from django.urls import path

from product.views import ProductDV

app_name = 'product'

urlpatterns = [
    path('<int:pk>/', ProductDV.as_view(), name='detail'),
]
